import json, collections
s = json.load(open('research/singapore/city/city.json'))
c8 = collections.Counter(); c12 = collections.Counter(); win = collections.Counter()
for v in s['venues'].values():
    pw = v['fields']['programme_windows']['value']
    c8[pw['8']['state']] += 1; c12[pw['12']['state']] += 1
    w = v['fields'].get('access_window', {}).get('value')
    win['null' if w is None else 'set'] += 1
print('8', c8, '12', c12, 'window', win)
# photo counts
ph = s['photos']
n1 = sum(1 for k, ps in ph.items() if any(p.get('url') and not p.get('withheld') and p.get('hotlink_ok', True) for p in ps))
n4 = sum(1 for k, ps in ph.items() if sum(1 for p in ps if p.get('url') and not p.get('withheld') and p.get('hotlink_ok', True)) >= 4)
n0 = sum(1 for k, ps in ph.items() if not any(p.get('url') and not p.get('withheld') for p in ps))
room = sum(1 for ps in ph.values() for p in ps if p.get('url') and not p.get('withheld') and p.get('room_specific'))
fall = sum(1 for ps in ph.values() for p in ps if p.get('url') and not p.get('withheld') and not p.get('room_specific'))
print('photos 1+', n1, '4+', n4, 'none', n0, 'room views', room, 'fallback views', fall)
print('tiers', collections.Counter(v['fields']['coordinates']['value']['precision'] for v in s['venues'].values()))
