import json
import re
import subprocess
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11')
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/158.0.0.0 Safari/537.36')


def raw(url, ua=UA):
    proc = subprocess.run(['curl', '-sS', '-L', '--compressed', '-m', '45', '-A', ua,
                           url], capture_output=True, timeout=90)
    body = proc.stdout
    if body[:2] == b'\x1f\x8b':
        import gzip
        try:
            body = gzip.decompress(body)
        except Exception:  # noqa: BLE001
            pass
    return body.decode('utf-8', 'replace')


def probe(url, patterns, label, ua=UA):
    text = raw(url, ua)
    print('== %s %s bytes=%d' % (label, url, len(text)))
    for pat in patterns:
        for m in re.finditer(pat, text):
            s = max(0, m.start() - 160)
            print('   ...%s...' % re.sub(r'\s+', ' ', text[s:m.end() + 200])[:330])
            break
    return text


probe('https://lu.ma/kuala-lumpur', [r'2027'], 'luma-kl-2027')
probe('https://lu.ma/selangor', [r'2027', r'event'], 'luma-selangor')
probe('https://lu.ma/malaysia', [r'2027'], 'luma-malaysia')
probe('https://aitinkerers.org/all_cities', [r'Kuala Lumpur'], 'aitinkerers-all',
      UA_SHORT := 'CoeEventsResearch/1.0')
for url in ('https://miragather.com/', 'https://miragather.com/ai'):
    probe(url, [r'2027', r'event'], 'miragather ' + url)
text = Path(BASE / 'captures/events/eventbrite-ai.txt').read_text()
print('== eventbrite ai capture 2027 lines')
for line in text.splitlines():
    if '2027' in line:
        print('   ', line[:200])
