import re, sys
from pathlib import Path
caps = Path('/home/joe/repo_dev/coe-events/research/singapore/city/captures')
files = {
 'sg-0285e3753fc2': 'op-rws-ghj',
 'sg-09795cef4b0f': 'op-justco-marina',
 'sg-13d49f8566fb': 'src-sg-13d49f8566fb',
 'sg-34d6bf1ba39c': 'op-ahg-screening',
 'sg-5d3fcedef47c': 'src-sg-5d3fcedef47c',
 'sg-61c5043af885': 'src-sg-61c5043af885',
 'sg-bff0f516d53e': 'op-vidacity',
 'sg-c5e0795f1042': 'op-ahg-aliwal-mph',
 'sg-d9552dd03dd7': 'src-sg-d9552dd03dd7',
}
for vid, name in files.items():
    p = caps / (name + '.html')
    if not p.exists():
        print(vid, name, 'MISSING'); continue
    html = p.read_text(encoding='utf-8', errors='replace')
    print('=' * 80, vid, name)
    for m in re.finditer(r'<meta[^>]+(?:property|name)="(og:image|twitter:image)"[^>]+content="([^"]+)"', html):
        print('  META', m.group(1), m.group(2)[:160])
    for m in re.finditer(r'<img[^>]+>', html):
        tag = m.group(0)
        src = re.search(r'(?:src|data-src)="([^"]+)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        if src and ('jpg' in src.group(1).lower() or 'jpeg' in src.group(1).lower() or 'webp' in src.group(1).lower()):
            print('  IMG', (alt.group(1) if alt else '')[:90], '|', src.group(1)[:140])
