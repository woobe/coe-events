import json, collections
p = 'research/singapore/city/city.json'
s = json.load(open(p))
print('FIELD KEYS PER VENUE (union)')
c = collections.Counter()
for v in s['venues'].values():
    for k in v.get('fields', {}):
        c[k] += 1
for k, n in c.most_common():
    print(' ', k, n)
print()
print('LIFECYCLE', collections.Counter((v.get('fields',{}).get('lifecycle',{}).get('value')) for v in s['venues'].values()))
print('REFRESH REV', s.get('refresh_revision'))
print('DECLARED GAPS', json.dumps(s.get('declared_gaps'), indent=1)[:1500])
print()
print('COVERAGE')
print(json.dumps(s['coverage'], indent=1)[:2500])
print()
print('CITY REGISTRY')
print(json.dumps(s['city_registry'], indent=1)[:1500])
print()
print('HOLIDAY REGISTRY KEYS')
print(json.dumps(s['holiday_registry'], indent=1)[:3000])
print()
print('HOLIDAYS')
for h in s['holidays']:
    print(json.dumps(h, ensure_ascii=False)[:600])
print()
print('LOCAL REQ')
print(json.dumps(s['local_requirements'], indent=1)[:1500])
print()
print('EVENT CONTEXT')
print(json.dumps(s['event_context'], indent=1)[:1500])
print()
print('PHOTOS summary')
for vid, ps in s['photos'].items():
    print(vid, len(ps), [ (p.get('view_kind'), p.get('rights'), p.get('withheld')) for p in ps])
