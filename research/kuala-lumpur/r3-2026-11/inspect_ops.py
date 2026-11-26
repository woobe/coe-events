#!/usr/bin/env python3
import json
from pathlib import Path

store = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
for vid in store['venues']:
    for p in store['photos'].get(vid, []):
        if p.get('withheld') or p.get('hotlink_ok') is False:
            continue
        if not str(p.get('url')).startswith('http'):
            continue
        if 'wikimedia' not in str(p.get('rights_basis') or ''):
            print(vid, store['venues'][vid]['name'], '|', p.get('view_kind'), '|', repr(p.get('rights_basis')), '|', p['url'][-50:])
print('---- rights_basis values on live rows')
vals = {}
for vid in store['venues']:
    for p in store['photos'].get(vid, []):
        if p.get('withheld') or not str(p.get('url')).startswith('http'):
            continue
        vals[repr(p.get('rights_basis'))] = vals.get(repr(p.get('rights_basis')), 0) + 1
print(vals)
