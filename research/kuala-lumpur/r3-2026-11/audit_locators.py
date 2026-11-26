import json
import re
import sys
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
R3 = BASE / 'r3-2026-11'
store = json.loads((BASE / 'city' / 'city.json').read_text())


def lines(slug, run_id=''):
    order = (R3 / 'captures', BASE / 'city' / 'captures')
    if 'kl-b1' in str(run_id):
        order = (BASE / 'city' / 'captures', R3 / 'captures')
    for d in order:
        p = d / (slug + '.txt')
        if p.exists():
            return [ln.rstrip('\n') for ln in p.read_text(errors='replace').splitlines()]
    return None


checked = bad = 0
problems = []
for vid, v in store['venues'].items():
    for field, row in (v.get('fields') or {}).items():
        loc = str(row.get('source_locator') or '')
        m = re.match(r'capture ([a-z0-9-]+) lines (\d+)(?:-(\d+))?', loc)
        if not m:
            continue
        slug, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        text = lines(slug, row.get('run_id'))
        checked += 1
        if text is None:
            bad += 1
            problems.append((vid, field, 'missing capture ' + slug))
            continue
        window = '\n'.join(text[a - 1:b])
        quote = str(row.get('quote') or '').strip()
        first = quote.split('\n')[0].strip()
        if first and first not in window and first not in '\n'.join(text[a - 1:b + 3]):
            bad += 1
            problems.append((vid, field, 'quote not in locator window: %r' % first[:60]))

for h in store['holidays']:
    if h['kind'] != 'school_holiday':
        continue
    loc = str(h.get('source_locator') or '')
    m = re.search(r'line (\d+)', loc)
    checked += 1
    if not m:
        bad += 1
        problems.append(('holiday', h['holiday_name'], 'no line locator'))
        continue
    i = int(m.group(1)) - 1
    text = lines('kpm-kalendar-2027-ocr', h.get('run_id'))
    quote = str(h.get('quote') or '').strip().replace('\n', ' ')
    if text is None or quote not in ' '.join(text[i - 1:i + 5]):
        bad += 1
        problems.append(('holiday', h['holiday_name'], 'quote not at OCR line %d' % (i + 1)))

print('claims checked', checked, 'failures', bad)
for p in problems[:15]:
    print('  ', p)
