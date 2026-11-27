import json
s = json.load(open('research/singapore/city/city.json'))
r = json.load(open('research/singapore/evidence/venue-report.json'))
print('counts:')
import sys
sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
from city_rank import build_ranking
rk = build_ranking(s, '2026-11-26')
print(json.dumps(rk['counts'], indent=1))
print('rows', len(rk['rows']), 'leads', len(rk['leads']))
print('--- stale blockers')
for vid, v in s['venues'].items():
    if v.get('blockers'):
        print(vid, '|', v['fields']['display_name']['value'][:50])
        for b in v['blockers']:
            print('   ', b.get('field'), '|', b.get('text')[:150])
print('--- tier_reasons')
for vid, v in s['venues'].items():
    if v.get('tier_reasons'):
        print(vid, v['fields']['display_name']['value'][:40], v['tier_reasons'][:2])
