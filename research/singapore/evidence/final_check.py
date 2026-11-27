import json, sys, collections
sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
from city_rank import build_ranking
from city_store import validate_store
p = 'research/singapore/city/city.json'
s = json.load(open(p))
errs = validate_store(s, store_dir='research/singapore/city')
print('errors', len(errs))
for e in errs[:20]:
    print(' ', e)
rk = build_ranking(s, '2026-11-26')
print('counts', rk['counts'])
print('rows', len(rk['rows']), 'leads', len(rk['leads']), 'sequence', len(rk['sequence']),
      'unique', len(set(rk['sequence'])))
print('event_yield sum', sum(x.get('event_yield') or 0 for x in s['sources_consulted']),
      'events', len(s['events']))
print('venue_yield sum', sum(x.get('venue_yield') or 0 for x in s['sources_consulted']))
print('gaps', len(s['declared_gaps']))
print('12h yes', [v['fields']['display_name']['value'] for v in s['venues'].values()
                  if v['fields']['programme_windows']['value']['12']['state'] == 'yes'])
print('8h no', [v['fields']['display_name']['value'] for v in s['venues'].values()
               if v['fields']['programme_windows']['value']['8']['state'] == 'no'])
