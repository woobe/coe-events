import hashlib
import json
from collections import Counter
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
store = json.loads((BASE / 'city/city.json').read_text())
before = json.loads((BASE / 'city/city.pre-r3.json').read_text())


def f(v, k):
    return (v['fields'].get(k) or {}).get('value')


pinless = [vid for vid, v in before['venues'].items() if not (f(v, 'coordinates') or {}).get('latitude')]
print('pinless before', len(pinless))
print('pinless tiers', Counter(f(store['venues'][v], 'coordinates')['precision'] for v in pinless))
print('all tiers', Counter(f(v, 'coordinates')['precision'] for v in store['venues'].values()))

ROOM = {'interior', 'layout', 'floor_plan'}
room_v, fb_v, none_v = [], [], []
for vid in store['venues']:
    rows = [p for p in store['photos'].get(vid, []) if p.get('url') and not p.get('withheld')]
    kinds = {p.get('view_kind') for p in rows}
    if kinds & ROOM:
        room_v.append(vid)
    elif rows:
        fb_v.append(vid)
    else:
        none_v.append(vid)
print('venues room-view', len(room_v), 'fallback-only', len(fb_v), 'none', len(none_v))
print('fallback venues', [(store['venues'][v]['name'], [p.get('view_kind') for p in store['photos'][v] if p.get('url') and not p.get('withheld')]) for v in fb_v])
print('sha256', hashlib.sha256((BASE / 'city/city.json').read_bytes()).hexdigest())
print('media', Counter(p.get('licence') for rows in store['photos'].values() for p in rows if not p.get('withheld') and p.get('url')))
print('operator hosts', Counter(p['url'].split('/')[2] for rows in store['photos'].values() for p in rows if not p.get('withheld') and p.get('url') and 'wikimedia' not in p['url']))
