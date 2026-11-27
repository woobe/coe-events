import hashlib, json, sys
from pathlib import Path
sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
from city_rank import build_ranking
from city_store import validate_store
p = Path('/home/joe/repo_dev/coe-events/research/singapore/city/city.json')
b = p.read_bytes()
s = json.loads(b)
print('sha256', hashlib.sha256(b).hexdigest())
print('bytes', len(b))
print('check errors', len(validate_store(s, store_dir=str(p.parent))))
rk = build_ranking(s, '2026-11-26')
print('rank rows', len(rk['rows']), 'leads', len(rk['leads']), 'sequence', len(rk['sequence']),
      'unique', len(set(rk['sequence'])), 'counts', rk['counts'])
print('venues', len(s['venues']), 'events', len(s['events']), 'holidays', len(s['holidays']),
      'coverage', len(s['coverage']), 'gaps', len(s['declared_gaps']),
      'sources', len(s['sources_consulted']))
print('event yield', sum(x['event_yield'] for x in s['sources_consulted']),
      'venue yield', sum(x['venue_yield'] for x in s['sources_consulted']))
print('public', sum(1 for h in s['holidays'] if h['kind'] == 'public_holiday'),
      'school', sum(1 for h in s['holidays'] if h['kind'] == 'school_holiday'))
print('school rows', [(h['start_date'], h['end_date'], h.get('school_scope')) for h in s['holidays'] if h['kind'] == 'school_holiday'])
print('tiers', {t: sum(1 for v in s['venues'].values() if v['fields']['coordinates']['value']['precision'] == t)
                for t in ('exact_venue', 'building', 'street', 'area')})
print('matrix cells', json.load(open('/home/joe/repo_dev/coe-events/research/singapore/evidence/event-matrix.json'))['total'])
