import json
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
store = json.loads((BASE / 'city/city.json').read_text())
groups = {}
for vid, v in store['venues'].items():
    p = ((v['fields'].get('coordinates') or {}).get('value') or {})
    groups.setdefault(p.get('precision'), []).append((v['name'], (p.get('map_target') or '')[:70]))
for tier in ('exact_venue', 'building', 'street', 'area'):
    print('###', tier, len(groups.get(tier, [])))
    for name, target in sorted(groups.get(tier, [])):
        print('* %s — %s' % (name, target))
