"""R9: capture manifest + research log for the New York city subtree."""
import json, hashlib
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
CAP = CITY / 'captures'
CHECKED = '2026-11-26'

KIND = {}
for name in CAP.iterdir():
    if not name.is_file():
        continue
    stem = name.stem
    if stem.startswith('venue-'):
        kind = 'venue page'
    elif stem.startswith('event-'):
        kind = 'event page' if 'candidate' not in stem else 'event candidate'
    elif stem.startswith('lane-'):
        kind = 'event lane'
    elif stem.startswith('rev1-'):
        kind = 'authority'
    else:
        kind = 'probe'
    KIND[name.name] = kind

rows = []
for name in sorted(CAP.iterdir()):
    if not name.is_file():
        continue
    rows.append({
        'file': 'captures/' + name.name,
        'kind': KIND.get(name.name, 'capture'),
        'bytes': name.stat().st_size,
        'sha256': hashlib.sha256(name.read_bytes()).hexdigest(),
        'fetched_on': CHECKED,
    })
(CITY / 'capture-manifest.json').write_text(json.dumps({
    'city_slug': 'new-york-ny-us',
    'checked_on': CHECKED,
    'run_id': 'run-20261126-nyc-r9',
    'captures': rows,
}, indent=1))
print('captures', len(rows))
