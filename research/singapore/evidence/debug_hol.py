import json, re
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
s = json.load(open(BASE / 'city.json'))
for h in s['holidays']:
    if h['holiday_name'] in ('Youth Day (observed school holiday)', "Children's Day"):
        print(h['holiday_name'], h['source_locator'], repr(h['quote']))
        lines = (BASE / h['capture']).read_text().splitlines()
        for n in range(141, 151):
            print(n, repr(lines[n-1]))
        def norm(x): return re.sub(r'[^a-z0-9]+', ' ', str(x).lower()).strip()
        nums = [int(n) for n in re.findall(r'\d+', h['source_locator']) if 0 < int(n) <= len(lines)]
        w = norm('\n'.join(re.sub(r'^\s*\d+\|\s?', '', lines[n-1]) for n in nums))
        print('W', w)
        print('Q', norm(h['quote']))
        print('IN', norm(h['quote'])[:40] in w)
