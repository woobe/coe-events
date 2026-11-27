import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
OUT = ROOT / 'captures'
OUT.mkdir(exist_ok=True)
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'

def slug(url):
    s = re.sub(r'^https?://', '', url)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    return s[:120]

def fetch(url, name):
    html_path = OUT / (name + '.html')
    txt_path = OUT / (name + '.txt')
    if html_path.exists() and html_path.stat().st_size > 2000:
        return 'cached', html_path.stat().st_size
    req = urllib.request.Request(url, headers={'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/pdf,*/*'})
    try:
        with urllib.request.urlopen(req, timeout=35) as r:
            body = r.read()
            ctype = r.headers.get('Content-Type', '')
    except Exception as e:
        return 'ERR ' + repr(e)[:200], 0
    if b'%PDF' in body[:8] or 'pdf' in ctype:
        html_path.with_suffix('.pdf').write_bytes(body)
        return 'pdf %s %d' % (ctype, len(body)), len(body)
    html = body.decode('utf-8', errors='replace')
    html_path.write_text(html, encoding='utf-8')
    text = to_text(html)
    txt_path.write_text('\n'.join('%4d| %s' % (i+1, line) for i, line in enumerate(text.splitlines())), encoding='utf-8')
    return 'ok %d chars %d lines' % (len(html), len(text.splitlines())), len(html)

def to_text(html):
    html = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', html)
    html = re.sub(r'(?is)<!--.*?-->', ' ', html)
    html = re.sub(r'(?i)<br\s*/?>', '\n', html)
    html = re.sub(r'(?i)</(p|div|li|tr|h[1-6]|section|article|table|dd|dt|button|a)>', '\n', html)
    html = re.sub(r'(?i)<td[^>]*>', ' | ', html)
    text = re.sub(r'(?s)<[^>]+>', ' ', html)
    import html as H
    text = H.unescape(text)
    lines = []
    for line in text.splitlines():
        line = re.sub(r'[ \t\r\f\v]+', ' ', line).strip()
        if line:
            lines.append(line)
    return '\n'.join(lines)

def main():
    jobs = json.load(open(sys.argv[1]))
    for j in jobs:
        name = j.get('capture') or slug(j['url'])
        status, size = fetch(j['url'], name)
        print('%-60s %-8s %s' % (name, j['id'], status), flush=True)
        time.sleep(0.4)

if __name__ == '__main__':
    main()
