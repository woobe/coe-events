import json, re
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
s = json.load(open(BASE / 'city.json'))


def norm(x):
    return re.sub(r'[^a-z0-9]+', ' ', str(x).lower()).strip()


def located(loc, count):
    nums = []
    for a, b in re.findall(r'(\d+)\s*-\s*(\d+)', loc):
        a, b = int(a), int(b)
        if 0 < a <= b <= count:
            nums.extend(range(a, b + 1))
    for n in re.findall(r'(?<![-\d])(\d+)(?![-\d])', loc):
        n = int(n)
        if 0 < n <= count:
            nums.append(n)
    return sorted(set(nums))


bad = []
ok = 0
for vid, v in s['venues'].items():
    for field in ('address', 'coordinates', 'access_window', 'programme_windows'):
        e = v['fields'].get(field) or {}
        cap = e.get('capture')
        loc = e.get('source_locator')
        quote = e.get('quote')
        if loc is None:
            if e.get('locator_note'):
                ok += 1
                continue
            bad.append((vid, field, 'null locator without note', cap, e.get('value')))
            continue
        if not cap or not quote:
            bad.append((vid, field, 'missing capture/quote', cap, loc)); continue
        p = BASE / cap
        if not p.exists():
            bad.append((vid, field, 'capture absent', cap, loc)); continue
        lines = p.read_text(encoding='utf-8', errors='replace').splitlines()
        nums = located(loc, len(lines))
        if not nums:
            bad.append((vid, field, 'locator has no line number', cap, loc)); continue
        window = norm('\n'.join(re.sub(r'^\s*\d+\|\s?', '', lines[n-1]) for n in nums[:80]))
        if norm(quote)[:45] not in window:
            bad.append((vid, field, 'quote not on located line', cap, loc, norm(quote)[:60])); continue
        ok += 1
print('checked ok', ok, 'bad', len(bad))
for b in bad[:12]:
    print(' ', b)
