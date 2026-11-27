import json, collections
p = 'research/singapore/city/city.json'
s = json.load(open(p))
print('TOP KEYS')
for k, v in s.items():
    if isinstance(v, (dict, list)):
        print(' ', k, type(v).__name__, len(v))
    else:
        print(' ', k, repr(v)[:300])
print()
print('VENUE COUNT', len(s['venues']))
print('EVENT COUNT', len(s['events']))
print('HOLIDAY COUNT', len(s['holidays']))
print('PHOTO KEYS', len(s.get('photos', {})))
print()
vids = list(s['venues'])
print('FIRST 6 VENUE IDS')
for i in vids[:6]:
    print(' ', i)
print()
print('FULL FIRST VENUE')
print(json.dumps(s['venues'][vids[0]], indent=1)[:6000])
print()
print('FULL FIRST EVENT')
print(json.dumps(s['events'][0], indent=1)[:3000])
print()
print('FULL FIRST HOLIDAY')
print(json.dumps(s['holidays'][0], indent=1)[:1500])
print()
print('FIELD KEYS PER VENUE (union)')
c = collections.Counter()
for v in s['venues'].values():
    for k in v.get('fields', {}):
        c[k] += 1
for k, n in c.most_common():
    print(' ', k, n)
print()
print('LIFECYCLE COUNTS', collections.Counter(v.get('lifecycle') for v in s['venues'].values()))
print('REFRESH KEYS', [k for k in s if 'refresh' in k or 'gap' in k or 'coverage' in k])
print('DECLARED GAPS', json.dumps(s.get('declared_gaps'), indent=1)[:2000])
