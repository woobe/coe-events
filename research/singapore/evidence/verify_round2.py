import json, os
from collections import Counter
BASE='research/singapore/city'
s=json.load(open(BASE+'/city.json'))
print('=== HOLIDAYS', len(s['holidays']))
for h in s['holidays']:
    print(h['start_date'], h['kind'], '|', h['holiday_name'], '|', h.get('observance'), '|', h['source_locator'], h['capture'], '| quote_ok', bool(h.get('quote')))
print('=== COORDS')
resp_ok=resp_missing=0
prov=Counter(); failed_nonempty=0; failed_none=0; bad_me=[]
for vid,v in s['venues'].items():
    e=v['fields']['coordinates']
    p=BASE+'/'+e['geocode_response']
    if os.path.exists(p): resp_ok+=1
    else:
        resp_missing+=1; print('MISSING',vid,e['geocode_response'])
    if e.get('retry_response') and not os.path.exists(BASE+'/'+e['retry_response']):
        print('MISSING RETRY',vid,e['retry_response'])
    prov[e['provider']]+=1
    fl=e.get('failed_lookups','')
    if fl=='none': failed_none+=1
    else: failed_nonempty+=1
    if e['provider'].startswith('OpenStreetMap Nominatim') and 'Photon lookup' in e.get('match_evidence',''):
        bad_me.append(vid)
print('responses exist',resp_ok,'missing',resp_missing)
print('providers',dict(prov))
print('failed_lookups none',failed_none,'recorded',failed_nonempty)
print('Nominatim rows still claiming Photon lookup',bad_me)
print('=== PHOTOS')
room=fb=0; nulls=0; total=0
for vid,recs in s['photos'].items():
    for r in recs:
        if r.get('url') and not r.get('withheld'):
            total+=1
            if r.get('room_specific'): room+=1
            else: fb+=1
            d=r.get('dimensions') or {}
            if not d.get('width') or not d.get('height'): nulls+=1
print('usable',total,'room',room,'fallback',fb,'dims missing',nulls)
print('venues 1+',sum(1 for r in s['photos'].values() if any(x.get('url') and not x.get('withheld') for x in r)),
      '4+',sum(1 for r in s['photos'].values() if sum(1 for x in r if x.get('url') and not x.get('withheld'))>=4),
      'none',sum(1 for r in s['photos'].values() if not any(x.get('url') and not x.get('withheld') for x in r)))
print('=== CLAIM IDS')
c=Counter()
for coll in (s['venues'],s['events']):
    for k,v in coll.items():
        for f,e in (v.get('fields') or {}).items(): c[e.get('claim_id')]+=1
print('field-level duplicate ids', [(k,n) for k,n in c.items() if n>1])
print('=== LEGACY')
un=0; by={'venue':0,'event':0}
for kind,coll in (('venue',s['venues']),('event',s['events'])):
    for k,v in coll.items():
        for f,e in (v.get('fields') or {}).items():
            if not e.get('source_locator') and not e.get('capture'):
                un+=1; by[kind]+=1
print('unlocated claims',un,by)
print('gap text legacy', [g['text'][:120] for g in s['declared_gaps'] if g['kind']=='legacy-claims'])
print('=== ACCESS')
ac=Counter()
for vid,v in s['venues'].items():
    w=v['fields']['programme_windows']['value']
    ac[(w['8']['state'],w['12']['state'])]+=1
print(ac)
