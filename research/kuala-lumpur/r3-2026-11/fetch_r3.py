#!/usr/bin/env python3
"""Fetch pages into r3 captures with a pinned manifest (URL, status, sha256).

Usage: python fetch_r3.py <slug>=<url> ...   (or a JSON list via @file)
Writes: captures/<slug>.txt, capture-manifest.json (merged by slug).
"""
import hashlib
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11')
CAPS = BASE / 'captures'
MANIFEST = BASE / 'capture-manifest.json'
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/158.0.0.0 Safari/537.36')
SKIP = {'script', 'style', 'noscript', 'svg', 'head'}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.title = []
        self._skip = 0
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self._skip += 1
        if tag == 'title':
            self._in_title = True
        if tag in ('p', 'div', 'br', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'section',
                   'td', 'th'):
            self.out.append('\n')

    def handle_endtag(self, tag):
        if tag in SKIP and self._skip:
            self._skip -= 1
        if tag == 'title':
            self._in_title = False
        if tag in ('p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'h4'):
            self.out.append('\n')

    def handle_data(self, data):
        if self._in_title:
            self.title.append(data)
        if self._skip:
            return
        text = re.sub(r'[ \t\r\f\v]+', ' ', data)
        if text.strip():
            self.out.append(text.strip())

    def text(self):
        raw = ''.join(self.out)
        lines = [re.sub(r' +', ' ', ln).strip() for ln in raw.split('\n')]
        return '\n'.join([ln for ln in lines if ln])


def fetch(url):
    proc = subprocess.run(
        ['curl', '-sS', '-L', '--compressed', '--max-time', '45', '-A', UA,
         '-H', 'Accept-Language: en-MY,en;q=0.9,ms;q=0.6',
         '-w', '\n__META__%{http_code}%{content_type}%{size_download}%{url_effective}',
         url], capture_output=True, timeout=90)
    body = proc.stdout
    meta = b''
    if b'__META__' in body:
        body, _, meta = body.rpartition(b'__META__')
    status = ctype = ''
    size = 0
    final = url
    if meta:
        m = re.match(rb'(\d{3})([^0-9]*?)(\d+)(https?://.*)$', meta.strip(), re.S)
        if m:
            status = m.group(1).decode()
            ctype = m.group(2).decode()
            size = int(m.group(3))
            final = m.group(4).decode('utf-8', 'replace')
    return proc.returncode, status, ctype, size, final, body


def _text(body):
    if body[:2] == b'\x1f\x8b':
        try:
            import gzip
            body = gzip.decompress(body)
        except Exception:  # noqa: BLE001
            pass
    return body


def main(pairs):
    CAPS.mkdir(parents=True, exist_ok=True)
    state = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {'pages': []}
    by_slug = {row['slug']: row for row in state['pages']}
    for slug, url in pairs:
        code, status, ctype, size, final, body = fetch(url)
        text, title = '', ''
        try:
            parser = Text()
            parser.feed(_text(body).decode('utf-8', 'replace'))
            text = parser.text()
            title = ' '.join(''.join(parser.title).split())
        except Exception as exc:  # noqa: BLE001
            text = ''
            title = 'parse-failed: %s' % exc
        path = CAPS / (slug + '.txt')
        path.write_text(text + '\n', encoding='utf-8')
        digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
        by_slug[slug] = {
            'slug': slug, 'url': url, 'final_url': final, 'status': int(status or 0),
            'content_type': ctype, 'bytes': len(text.encode('utf-8')),
            'body_bytes': size, 'title': title, 'file': 'captures/' + slug + '.txt',
            'sha256_text': digest, 'checked_on': '2026-11-26', 'curl_exit': code,
        }
        print('%-32s %s %6d body=%7d %s | %s' % (
            slug, status, len(text), size, title[:70], final[:90]))
    state['pages'] = sorted(by_slug.values(), key=lambda r: r['slug'])
    MANIFEST.write_text(json.dumps(state, indent=1, ensure_ascii=False) + '\n',
                        encoding='utf-8')


if __name__ == '__main__':
    args = sys.argv[1:]
    pairs = []
    for arg in args:
        if arg.startswith('@'):
            for row in json.loads(Path(arg[1:]).read_text()):
                pairs.append((row['slug'], row['url']))
            continue
        slug, _, url = arg.partition('=')
        pairs.append((slug, url))
    main(pairs)
