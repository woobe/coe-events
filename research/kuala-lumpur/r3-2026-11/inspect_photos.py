#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city')
pre = json.loads((p / 'city.pre-r3.json').read_text())
cur = json.loads((p / 'city.json').read_text())
for vid in ['kl-a2b2e1986ea5', 'kl-73ee37f91926', 'kl-13ee3afff10b', 'kl-d86dffabc235', 'kl-ade0334f2820']:
    print('===', vid, cur['venues'][vid]['name'])
    for s, label in ((pre, 'pre'), (cur, 'cur')):
        rows = s['photos'].get(vid, [])
        print(' ', label, len(rows))
        for r in rows:
            print('   ', {k: r.get(k) for k in ('view_kind', 'room', 'alt', 'rights', 'rights_basis', 'withheld')}, str(r.get('url'))[-70:])
