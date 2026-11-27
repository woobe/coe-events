import json, re
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
s = json.load(open(BASE / 'city.json'))
vid, field = 'sg-123024e521a4', 'access_window'
e = s['venues'][vid]['fields'][field]
print('quote:', repr(e['quote']))
print('loc:', e['source_locator'])
lines = (BASE / e['capture']).read_text().splitlines()
for n in range(146, 152):
    print(n, repr(lines[n-1]))
def norm(x): return re.sub(r'[^a-z0-9]+', ' ', str(x).lower()).strip()
w = norm('\n'.join(re.sub(r'^\s*\d+\|\s?', '', lines[n-1]) for n in range(146, 152)))
q = norm(e['quote'])
print('W:', w)
print('Q:', q)
print('in?', q[:45] in w)
