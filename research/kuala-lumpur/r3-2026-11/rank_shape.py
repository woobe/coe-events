import json
import sys
from pathlib import Path
sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
import city_rank

store = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
r = city_rank.build_ranking(store, '2026-11-26')
print(json.dumps({k: (type(v).__name__, (len(v) if hasattr(v, '__len__') else v)) for k, v in r.items()}, indent=1))
print('counts', json.dumps(r.get('counts'), indent=1))
for key in ('leads', 'closed', 'ordering', 'open'):
    val = r.get(key)
    if isinstance(val, list):
        print(key, len(val), 'sample', json.dumps(val[0], indent=1)[:400] if val else '')
print(json.dumps(r.get('event'), indent=1)[:300])
