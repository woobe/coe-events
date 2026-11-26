import json
from pathlib import Path
probe = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/photo-probe.json').read_text())
for slug in ('colony-events', 'cg-klcc', 'publika', 'mo-meet', 'wtckl'):
    print('==', slug)
    for r in probe.get(slug, {}).get('images', []):
        if r['src'].startswith('data:'):
            continue
        print('   %s | alt=%r | under=%r' % (r['src'][-80:], r['alt'][:50], r['heading'][:60]))
