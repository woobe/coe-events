#!/usr/bin/env python3
import json
from pathlib import Path

sf = json.loads(Path('/home/joe/repo_dev/coe-events/research/san-francisco/city/city.json').read_text())
print('refresh_revision', sf.get('refresh_revision'), 'events', len(sf['events']))
for eid, ev in list(sf['events'].items())[:3]:
    print('===', eid, ev.get('name'))
    for f, row in ev['fields'].items():
        print('  ', f, '=', repr(row.get('value'))[:70], '| loc', row.get('source_locator'), '| quote', repr(row.get('quote'))[:60])
    print('  evidence', [e.get('inference') for e in ev.get('evidence', [])])
