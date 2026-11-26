#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city')
cur = json.loads((p / 'city.json').read_text())
for eid, ev in cur['events'].items():
    print('===', eid, ev.get('name'))
    for f, row in ev['fields'].items():
        print('  ', f, '=', repr(row.get('value'))[:90])
        print('      loc', row.get('source_locator'), '| quote', repr(row.get('quote'))[:90])
    print('  evidence', [e.get('inference') for e in ev.get('evidence', [])])
