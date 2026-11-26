#!/usr/bin/env python3
"""Six-theme event sweep: 9 lanes x 6 themes, each cell logged with URL and yield."""
import json
import re
import subprocess
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11')
CAPS = BASE / 'captures' / 'events'
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/158.0.0.0 Safari/537.36')
UA_SHORT = 'CoeEventsResearch/1.0'

THEMES = {
    'ai': ['artificial intelligence', ' ai ', 'ai-', 'a.i.', 'generative', 'llm', 'agentic'],
    'machine learning': ['machine learning', 'ml ', 'deep learning', 'pytorch', 'tensorflow'],
    'data science': ['data science', 'data scientist', 'analytics', 'data engineering'],
    'web3': ['web3', 'web 3', 'dapp', 'defi', 'nft', 'metaverse'],
    'crypto': ['crypto', 'bitcoin', 'ethereum', 'token', 'digital asset'],
    'blockchain': ['blockchain', 'distributed ledger', 'smart contract', 'ledger'],
}

LANES = [
    ('luma-city', 'Luma city page', 'https://lu.ma/kuala-lumpur', UA),
    ('luma-alias-kl', 'Luma alias KL', 'https://lu.ma/kl', UA),
    ('luma-alias-klang', 'Luma alias Klang Valley', 'https://lu.ma/klang-valley', UA),
    ('luma-organisers', 'Luma organiser calendars', 'https://luma.com/malaysianai', UA),
    ('meetup', 'Meetup group/theme search', 'https://www.meetup.com/find/?location=my--Kuala+Lumpur&keywords={theme}', UA),
    ('eventbrite', 'Eventbrite Kuala Lumpur', 'https://www.eventbrite.com/d/malaysia--kuala-lumpur/{slug}/', UA),
    ('miragather-main', 'MiraGather main', 'https://miragather.com/', UA),
    ('miragather-side', 'MiraGather side events', 'https://miragather.com/?tab=side', UA),
    ('miragather-ai', 'MiraGather AI', 'https://miragather.com/ai', UA),
    ('aitinkerers', 'AI Tinkerers all cities', 'https://aitinkerers.org/all_cities', UA),
    ('aitinkerers-kl', 'AI Tinkerers Kuala Lumpur', 'https://kuala-lumpur.aitinkerers.org/', UA),
]
EB_SLUG = {'ai': 'artificial-intelligence', 'machine learning': 'machine-learning',
           'data science': 'data-science', 'web3': 'web3', 'crypto': 'crypto',
           'blockchain': 'blockchain'}
DATE27 = re.compile(r'2027|2026-1[12]|jan(uary)?|feb(ruary)?|mar(ch)?|apr(il)?|may|jun(e)?|'
                    r'jul(y)?|aug(ust)?|sep(tember)?|oct(ober)?|nov(ember)?|dec(ember)?', re.I)


def fetch(url):
    proc = subprocess.run(['curl', '-sS', '-L', '--compressed', '--max-time', '45',
                           '-A', UA, '-o', '/tmp/_ev.bin', '-w',
                           '%{http_code} %{content_type}', url],
                          capture_output=True, timeout=90)
    code, ctype = (proc.stdout.decode().split() + ['', ''])[:2]
    raw = Path('/tmp/_ev.bin').read_bytes() if Path('/tmp/_ev.bin').exists() else b''
    if raw[:2] == b'\x1f\x8b':
        import gzip
        try:
            raw = gzip.decompress(raw)
        except Exception:  # noqa: BLE001
            pass
    text = raw.decode('utf-8', 'replace')
    text = re.sub(r'(?s)<(script|style)[^>]*>.*?</\1>', ' ', text)
    text = re.sub(r'(?s)<[^>]+>', '\n', text)
    lines = [re.sub(r'\s+', ' ', ln).strip() for ln in text.split('\n')]
    return int(code or 0), ctype, [ln for ln in lines if ln]


def main():
    CAPS.mkdir(parents=True, exist_ok=True)
    cells = []
    cache = {}
    for lane_id, lane_label, url_t, ua in LANES:
        for theme in THEMES:
            url = url_t.format(theme=theme.replace(' ', '+'), slug=EB_SLUG[theme])
            if url not in cache:
                if url_t.endswith('{theme}') or url_t.endswith('{slug}/'):
                    import time
                    time.sleep(1.0)
                code, ctype, lines = fetch(url)
                slug = '%s-%s' % (lane_id, EB_SLUG.get(theme, theme).replace(' ', '-'))
                (CAPS / (slug + '.txt')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
                cache[url] = (code, ctype, lines, slug)
            code, ctype, lines, slug = cache[url]
            words = THEMES[theme]
            hits = []
            for i, line in enumerate(lines, 1):
                low = ' ' + line.lower() + ' '
                if any(w in low for w in words) and DATE27.search(line) and len(line) < 300:
                    hits.append({'line': i, 'text': line[:220]})
            dates27 = [h for h in hits if '2027' in h['text']]
            cells.append({
                'lane': lane_id, 'lane_label': lane_label, 'theme': theme,
                'url': url, 'capture': 'captures/events/' + slug + '.txt',
                'status': code, 'content_type': ctype, 'pages_read': 1,
                'lines_read': len(lines), 'raw_hits': len(hits),
                'hits_with_2027': len(dates27), 'retained': 0,
                'samples': hits[:4],
                'disposition': ('opened; ' + ('2027 hits reviewed' if dates27 else
                                              'no 2027 date printed in any theme line')
                                if code == 200 else 'blocked/unreadable (%s)' % code),
            })
            print('%-18s %-16s %s hits=%d 2027=%d lines=%d' % (
                lane_id, theme, code, len(hits), len(dates27), len(lines)))
    (BASE / 'event-matrix.json').write_text(
        json.dumps({'checked_on': '2026-11-26', 'cells': cells}, indent=1,
                   ensure_ascii=False) + '\n', encoding='utf-8')
    print('cells', len(cells), 'with 2027 hits', sum(1 for c in cells if c['hits_with_2027']))


if __name__ == '__main__':
    main()
