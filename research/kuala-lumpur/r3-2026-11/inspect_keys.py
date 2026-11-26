#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city')
pre = json.loads((p / 'city.pre-r3.json').read_text())
cur = json.loads((p / 'city.json').read_text())
for s, label in ((pre, 'pre'), (cur, 'cur')):
    have = sum(1 for rows in s['photos'].values() for r in rows if 'view_kind' in r)
    rows_n = sum(len(v) for v in s['photos'].values())
    print(label, 'rows', rows_n, 'with view_kind key', have)
    for vid, rows in s['photos'].items():
        for r in rows:
            if r.get('withheld'):
                print(label, 'sample withheld', vid, sorted(r.keys()))
                break
        else:
            continue
        break
