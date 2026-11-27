import json, sys
sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
from city_rank import build_ranking
store = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/city/city.json'))
r = build_ranking(store, '2026-11-26')
print(type(r), list(r) if isinstance(r, dict) else len(r))
if isinstance(r, dict):
    for k, v in r.items():
        print(k, type(v).__name__, len(v) if hasattr(v, '__len__') else v)
        if isinstance(v, list) and v:
            print('  first:', json.dumps(v[0], indent=1)[:800])
