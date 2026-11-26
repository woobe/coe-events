"""R9: fix validation findings (host scope, lead display names, address quote)."""
import json, hashlib
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
store = json.loads(STORE.read_text())
CHECKED = '2026-11-26'
RUN = 'run-20261126-nyc-r9'

store['holiday_registry']['host_jurisdiction_id'] = 'US-NY:nycps'

adv = store['venues']['nyc-lead-advent-hope']
adv['fields']['address']['quote'] = '111 E. 87th Street NY, NY 10128'
adv['fields']['address']['source_locator'] = 'Rent page footer address line'

names = {
    'nyc-lead-advent-hope': ('Church of the Advent Hope', 'https://www.adventhope.org/rent'),
    'nyc-lead-bpl-meeting-rooms': ('Brooklyn Public Library — Rooms',
                                   'https://www.bklynlibrary.org/locations/central/meeting-rooms'),
    'nyc-lead-cuny-gc': ('CUNY Graduate Center — Rentals',
                          'https://spacerentals.gc.cuny.edu/'),
}
for vid, (name, url) in names.items():
    venue = store['venues'][vid]
    venue['name'] = name
    dn = venue['fields']['display_name']
    dn.update({'claim_id': 'cl-' + hashlib.sha1(('dn|' + vid).encode()).hexdigest()[:12],
               'value': name, 'quote': name, 'source_url': url,
               'source_locator': 'Operator page title', 'verified_at': CHECKED, 'run_id': RUN})

STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
print('patched')
