import re, json
from pathlib import Path
CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
CAP = CITY / 'captures'
pages = json.loads((CITY / 'venue-pages.json').read_text())
out = {}
for vid, rec in pages.items():
    text = None
    for e in rec['pages']:
        if e.get('status') == 200 and e.get('text'):
            text = (CAP / e['text']).read_text(errors='ignore')
            url = e['url']
            break
    if not text:
        continue
    lines = text.splitlines()
    row = None
    for i, line in enumerate(lines):
        if line.strip() == 'Saturday':
            row = lines[i:i + 7]
            break
    pay = None
    for i, line in enumerate(lines):
        if 'hire fee per hour' in line or 'hire fee' in line:
            pay = lines[max(0, i - 4):i + 2]
            break
    out[vid] = {'source': url, 'saturday_block': row, 'price_block': pay}
    print(vid, '|', row, '|', pay)
(CITY / 'access-blocks.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
