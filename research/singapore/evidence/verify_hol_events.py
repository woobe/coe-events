import json, re
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
s = json.load(open(BASE / 'city.json'))


def norm(x):
    return re.sub(r'[^a-z0-9]+', ' ', str(x).lower()).strip()


def located(loc, count):
    nums = []
    for a, b in re.findall(r'(\d+)\s*-\s*(\d+)', loc or ''):
        a, b = int(a), int(b)
        if 0 < a <= b <= count:
            nums.extend(range(a, b + 1))
    for n in re.findall(r'(?<![-\d])(\d+)(?![-\d])', loc or ''):
        n = int(n)
        if 0 < n <= count:
            nums.append(n)
    return sorted(set(nums))


def check(cap, loc, quote):
    p = BASE / cap
    if not p.exists():
        return 'capture absent'
    lines = p.read_text(encoding='utf-8', errors='replace').splitlines()
    nums = located(loc, len(lines))
    if not nums:
        return 'no line'
    window = norm('\n'.join(re.sub(r'^\s*\d+\|\s?', '', lines[n-1]) for n in nums[:80]))
    return None if norm(quote)[:40] in window else 'quote not on line'


bad = []
for h in s['holidays']:
    err = check(h['capture'], h['source_locator'], h['quote'])
    if err:
        bad.append(('holiday', h['holiday_name'], h['start_date'], err))
for eid, e in s['events'].items():
    for field, v in e['fields'].items():
        err = check(v.get('capture'), v.get('source_locator'), v.get('quote'))
        if err:
            bad.append(('event', eid, field, err))
print('holidays', len(s['holidays']), 'events', len(s['events']), 'bad', len(bad))
for b in bad[:12]:
    print(' ', b)
