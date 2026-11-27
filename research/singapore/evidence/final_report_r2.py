import json, os, hashlib
from collections import Counter
p='research/singapore/city/city.json'
raw=open(p,'rb').read()
s=json.loads(raw)
print('sha256', hashlib.sha256(raw).hexdigest())
print('bytes', len(raw))
print('venues', len(s['venues']), 'events', len(s['events']), 'holidays', len(s['holidays']))
print('tiers', Counter(v['fields']['coordinates']['value']['precision'] for v in s['venues'].values()))
print('dates', Counter(h['start_date'] for h in s['holidays'] if h['start_date'] in ('2027-02-08','2027-02-09','2027-05-03','2027-12-27')))
print('holiday kinds', Counter(h['kind'] for h in s['holidays']))
print('weekdays', [(h['start_date'], h['weekday']) for h in s['holidays'][-5:]])
print('access', Counter((v['fields']['programme_windows']['value']['8']['state'], v['fields']['programme_windows']['value']['12']['state']) for v in s['venues'].values()))
rights=Counter(); room=fb=0; dimnull=0
for recs in s['photos'].values():
    for r in recs:
        if r.get('url') and not r.get('withheld'):
            rights[r.get('rights_basis')]+=1
            room += 1 if r.get('room_specific') else 0
            fb += 0 if r.get('room_specific') else 1
            if not (r.get('dimensions') or {}).get('width'): dimnull+=1
print('rights', dict(rights), 'room', room, 'fallback', fb, 'dims null', dimnull)
print('gaps', len(s['declared_gaps']))
for g in s['declared_gaps']:
    print(' -', g['kind'], ':', g['text'][:180].replace('\n',' '))
print('registry', {k:s['holiday_registry'].get(k) for k in ('holiday_rows','coverage_rows','jurisdiction_ids')})
print('sources holiday', [(x['title'][:40], x['hits'], x['pages_read']) for x in s['sources_consulted'] if x['lane'].startswith('holiday')])
