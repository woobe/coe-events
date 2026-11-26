#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city')
pre = json.loads((p / 'city.pre-r3.json').read_text())
cur = json.loads((p / 'city.json').read_text())
for s, label in ((pre, 'pre'), (cur, 'cur')):
    rooms = {}
    kinds = {}
    for vid, rows in s['photos'].items():
        for r in rows:
            rooms[repr(r.get('room'))] = rooms.get(repr(r.get('room')), 0) + 1
            kinds[repr(r.get('view_kind'))] = kinds.get(repr(r.get('view_kind')), 0) + 1
    print(label, 'rooms', rooms)
    print(label, 'kinds', kinds)
    print(label, 'venues with photos key', len(s['photos']), 'total rows', sum(len(v) for v in s['photos'].values()))
