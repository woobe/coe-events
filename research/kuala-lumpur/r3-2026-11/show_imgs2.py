import json
from pathlib import Path
probe = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/photo-probe.json').read_text())
print(sorted(probe))
for slug in ('colony-events', 'cg-bukit-bintang', 'cg-kl-eco', 'mitec-venues', 'klpac-venue'):
    print('==', slug, len(probe.get(slug, {}).get('images', [])))
    for r in probe.get(slug, {}).get('images', []):
        if r['src'].startswith('data:'):
            continue
        if any(k in r['src'].lower() for k in ('web', 'hall', 'room', 'level', 'pentas',
                                               'indicine', 'event', 'nexus', 'glass', 'roof',
                                               'lounge', 'floor')):
            print('   %s | under=%r' % (r['src'][-70:], r['heading'][:60]))
