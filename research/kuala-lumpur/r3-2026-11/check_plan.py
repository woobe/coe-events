import json
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
store = json.loads((BASE/'city/city.json').read_text())
plan = json.loads((BASE/'r3-2026-11/address-plan.json').read_text())['venues']
ids = list(store['venues'])
print('store', len(ids), 'plan', len(plan))
missing = [i for i in ids if i not in plan]
extra = [i for i in plan if i not in store['venues']]
print('missing', missing)
print('extra', extra)
for i in missing:
    print('  ', i, store['venues'][i]['name'])
