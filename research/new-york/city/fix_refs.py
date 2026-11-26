import json
from pathlib import Path
CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
s = json.loads(STORE.read_text())
fix = {
    'photos (28 venue collections)': 'captures/venue-nyc-041ec8557e6d.html',
    'claim: rights field per photo record': 'city.json photos[*].rights',
    'coverage (4 rows)': 'coverage:US,US-NY,US-NY:nyc,US-NY:nycps',
    'access-blocks.json': 'access-blocks.json',
    'venues.*.fields.programme_windows.12': 'venues.nyc-4f482327c22f.fields.programme_windows.value.12',
}
for gap in s['declared_gaps']:
    gap['evidence_refs'] = [fix.get(r, r) for r in gap['evidence_refs']]
STORE.write_text(json.dumps(s, indent=1, ensure_ascii=False))
print([g['evidence_refs'] for g in s['declared_gaps'] if g['kind'] in ('photos', 'access')])
