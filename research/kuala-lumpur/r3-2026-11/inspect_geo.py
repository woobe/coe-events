import json
from pathlib import Path
G = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/geocode')
for vid in ['kl-73ee37f91926', 'kl-7d5505fb90ae', 'kl-6521a5218690', 'kl-b375b5ac812b',
            'kl-b32ee88b3dc6', 'kl-81d962290b05', 'kl-de410ec2db9b', 'kl-d86dffabc235',
            'kl-2758407243f1', 'kl-7dd2a97334c6', 'kl-8cd52f2406dc']:
    r = json.loads((G / (vid + '.json')).read_text())
    print('==', vid, r['name'], '| addr:', r['address'])
    for a in r['attempts']:
        print('   q:', a.get('query'), '| err:', a.get('error'))
        for c in (a.get('candidates') or [])[:4]:
            print('      -', (c.get('display_name') or '')[:130], '| name=', c.get('name'), '| score', c.get('_score', {}).get('hits'))
