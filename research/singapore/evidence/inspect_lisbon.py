import json
p='/home/joe/repo_dev/coe-events/research/lisbon/city/city.json'
s=json.load(open(p))
vs=list(s['venues'])
print('venue ids', vs[:3])
v=s['venues'][vs[0]]
print(json.dumps(v, indent=1)[:7000])
print('=== PHOTOS sample')
for vid in vs[:3]:
    print(vid, json.dumps(s['photos'].get(vid), indent=1)[:1800])
print('=== HOLIDAY samples')
for h in s['holidays'][:4]:
    print(json.dumps(h, indent=1)[:1200])
print('=== SCHOOL rows')
for h in s['holidays']:
    if h.get('kind')=='school_holiday':
        print(json.dumps(h, indent=1)[:1200]); break
print('=== GAPS')
print(json.dumps(s.get('declared_gaps'), indent=1)[:2500])
print('=== SOURCES sample')
print(json.dumps(s.get('sources_consulted',[])[:3], indent=1)[:1500])
print('=== RUNS')
print(json.dumps(s.get('runs'), indent=1)[:1500])
