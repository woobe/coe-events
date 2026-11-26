#!/usr/bin/env python3
"""List <img> candidates with alt/title and the nearest preceding heading."""
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/158.0.0.0 Safari/537.36')
OUT = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/photo-probe.json')


class Imgs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.heading = ''
        self.rows = []
        self._h = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self._h = []
        if tag == 'img':
            src = a.get('src') or a.get('data-src') or ''
            srcset = a.get('srcset') or a.get('data-srcset') or ''
            if not src and srcset:
                src = srcset.split(',')[0].strip().split(' ')[0]
            if src:
                self.rows.append({'src': src, 'alt': a.get('alt') or '',
                                  'title': a.get('title') or '',
                                  'heading': self.heading,
                                  'w': a.get('width'), 'h': a.get('height')})

    def handle_endtag(self, tag):
        if tag in ('h1', 'h2', 'h3', 'h4') and self._h:
            self.heading = ' '.join(''.join(self._h).split())
            self._h = []

    def handle_data(self, data):
        if self._h is not None:
            self._h.append(data)


def fetch(url):
    proc = subprocess.run(['curl', '-sS', '-L', '--compressed', '-m', '60', '-A', UA,
                           url], capture_output=True, timeout=90)
    body = proc.stdout
    if body[:2] == b'\x1f\x8b':
        import gzip
        body = gzip.decompress(body)
    return body.decode('utf-8', 'replace')


def main(pairs):
    state = json.loads(OUT.read_text()) if OUT.exists() else {}
    for slug, url in pairs:
        html = fetch(url)
        p = Imgs()
        p.feed(html)
        base = re.match(r'https?://[^/]+', url).group(0)
        rows = []
        for r in p.rows:
            src = r['src']
            if src.startswith('//'):
                src = 'https:' + src
            elif src.startswith('/'):
                src = base + src
            r['src'] = src
            rows.append(r)
        state[slug] = {'url': url, 'checked_on': '2026-11-26', 'images': rows}
        print('== %s  %d images' % (slug, len(rows)))
        for r in rows[:40]:
            print('   %s | alt=%r title=%r under=%r' % (r['src'][:110], r['alt'][:60],
                                                        r['title'][:40], r['heading'][:50]))
    OUT.write_text(json.dumps(state, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    pairs = []
    for arg in sys.argv[1:]:
        slug, _, url = arg.partition('=')
        pairs.append((slug, url))
    main(pairs)
