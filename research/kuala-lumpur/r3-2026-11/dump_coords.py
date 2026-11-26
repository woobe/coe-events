import json
from pathlib import Path
G = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11')
summary = json.loads((G / 'geocode-summary.json').read_text())
for vid, row in sorted(summary.items()):
    if row:
        print('%-16s %.7f %.7f | %s | %s' % (vid, row['latitude'], row['longitude'],
                                             row['query'], (row['display_name'] or '')[:70]))
probe = json.loads((G / 'geocode-probe.json').read_text())
print('--- probe picks')
for q, row in probe.items():
    for c in row['candidates'][:3]:
        nm = c.get('name') or ''
        if any(k in nm for k in ('MATRADE', 'KLCC', 'Connexion', 'Publika', 'Nexus', 'KLPAC',
                                 'Suria', 'KL Eco City', 'Mid Valley City', 'A Place Where',
                                 'Centrepoint')):
            print('%.7f %.7f | %s | q=%s' % (float(c['lat']), float(c['lon']), c.get('display_name'), q))
