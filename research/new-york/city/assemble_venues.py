"""R9 New York store assembly: revision 1 coordinates, access windows, addresses."""
import json, re, shutil, hashlib
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
RUN = 'run-20261126-nyc-r9'
CHECKED = '2026-11-26'
store = json.loads(STORE.read_text())
if not (CITY / 'city.pre-r9.json').exists():
    shutil.copy2(STORE, CITY / 'city.pre-r9.json')
log = json.loads((CITY / 'geocode-log.json').read_text())
pages = json.loads((CITY / 'venue-pages.json').read_text())
access = json.loads((CITY / 'access-blocks.json').read_text())
extra = json.loads((CITY / 'geocode' / 'nyc-4c6638c43df6-124e14.json').read_text())

# venue -> (lookup key, index, tier, remark)
DECISIONS = {
    'nyc-041ec8557e6d': ('name', 0, 'exact_venue', ''),
    'nyc-12462819aebd': ('street', 0, 'building', ''),
    'nyc-12c98ff34e33': ('address', 0, 'exact_venue', ''),
    'nyc-16d4e38fd069': ('name', 0, 'exact_venue', ''),
    'nyc-2703d407680f': ('address', 0, 'building', ''),
    'nyc-3ba4751ef6e7': ('address', 0, 'building', ''),
    'nyc-4c6638c43df6': ('__extra__', 0, 'exact_venue', ''),
    'nyc-4f482327c22f': ('address', 0, 'building', ''),
    'nyc-5e5134d4deff': ('street', 0, 'building', ''),
    'nyc-6205aa000e1b': ('street', 0, 'building', ''),
    'nyc-646e1e5393b6': ('name', 0, 'exact_venue', ''),
    'nyc-6d04b6ce2634': ('address', 0, 'building',
                         'OSM returns Middle Village/Queens 11378 for the 60-47 house number while '
                         'the operator prints Ridgewood 11385; the number matches and the block is '
                         'the Ridgewood/Middle Village border.'),
    'nyc-75c0f7334372': ('clean', 0, 'building',
                         'Two OSM points carry 15 West 38th Street; the Permanent Mission of Cyprus '
                         'office node at 40.7516359,-73.9837008 sits west of Fifth Avenue as a West '
                         '38th address must, while the other node (-73.9806779) sits east of Fifth '
                         'Avenue and cannot be the printed address.'),
    'nyc-7abec7622696': ('street', 0, 'building', ''),
    'nyc-862e759a55a6': ('street', 0, 'building', ''),
    'nyc-93bc87ce76a0': ('address', 0, 'exact_venue', ''),
    'nyc-a2a23c94407e': ('address', 0, 'building', ''),
    'nyc-aa32c5682549': ('address', 1, 'building', ''),
    'nyc-b07f42f9c9bc': ('street', 0, 'building', ''),
    'nyc-b9a5252396f3': ('clean', 1, 'building', ''),
    'nyc-bb0e8d8d6dc2': ('address', 0, 'exact_venue', ''),
    'nyc-bb4d0d62028d': ('clean', 1, 'building', ''),
    'nyc-bcb5bfbbb45a': ('address', 0, 'building', ''),
    'nyc-ca43f10af68d': ('clean', 0, 'building', ''),
    'nyc-ccb3bfa2e5d7': ('address', 0, 'building',
                         'OSM names the building 11 Times Square and files it on 11 8th Avenue; the '
                         'operator prints 11 Times Square, New York, NY 10036.'),
    'nyc-cf2d116c0745': ('address', 0, 'building', ''),
    'nyc-d6ff494b9504': ('clean', 0, 'building', ''),
    'nyc-dcd959417eb2': ('name', 0, 'exact_venue', ''),
    'nyc-fbae6569ad6a': ('address', 1, 'building', ''),
    'nyc-ffb2d5d73020': ('street', 0, 'building', ''),
    'nyc-lead-advent-hope': ('address', 0, 'building',
                             'The first OSM hit is 111 East 87th Street, Yorkville, 10128; a second '
                             '111 East 87th Street exists in Brooklyn 11236 and is rejected by the '
                             'operator ZIP and borough.'),
    'nyc-lead-bpl-meeting-rooms': ('name', 0, 'exact_venue', ''),
    'nyc-lead-cuny-gc': ('name-city', 0, 'exact_venue', ''),
}

ADDRESS_FIX = {
    'nyc-4c6638c43df6': ('124 East 14th Street, New York, NY 10003',
                         'Civic Hall, 124 East 14th Street, New York, NY 10003',
                         'Civic Hall contact page prints "124 East 14th Street, New York, NY 10003"; '
                         'the stored "28 East 28th Street (Zero Irving)" address was wrong. Zero Irving '
                         'is 124 East 14th Street (Union Square).'),
}
LEAD_NAMES = {
    'nyc-lead-advent-hope': 'Church of the Advent Hope — Space Rentals',
    'nyc-lead-bpl-meeting-rooms': 'Brooklyn Public Library — Meeting Rooms',
    'nyc-lead-cuny-gc': 'CUNY Graduate Center — Event and Space Rentals',
}
LEAD_ADDRESS = {
    'nyc-lead-advent-hope': ('111 East 87th Street, New York, NY 10128',
                             'https://www.adventhope.org/rent',
                             'LOCATION Manhattan 111 E 87th St. New York, NY 10128'),
    'nyc-lead-bpl-meeting-rooms': ('10 Grand Army Plaza, Brooklyn, NY 11238',
                                   'https://www.bklynlibrary.org/locations/central/meeting-rooms',
                                   '10 Grand Army Plaza, Brooklyn, NY 11238'),
    'nyc-lead-cuny-gc': ('365 Fifth Avenue, New York, NY 10016',
                         'https://spacerentals.gc.cuny.edu/',
                         'Our event spaces are located at the CUNY Graduate Center at 365 Fifth Avenue, New York, NY 10016.'),
}

def hit(vid):
    key, idx, tier, remark = DECISIONS[vid]
    if key == '__extra__':
        data = extra
    else:
        data = log[vid]['lookups'][key]['response']
    h = data[idx]
    return key, idx, tier, remark, h

def quote_for(h):
    return h.get('display_name') or ''

errors = []
for vid, venue in store['venues'].items():
    fields = venue['fields']
    key, idx, tier, remark, h = hit(vid)
    addr_obj = h.get('address') or {}
    road = addr_obj.get('road') or ''
    number = addr_obj.get('house_number') or ''
    op_addr = (ADDRESS_FIX.get(vid, (None,))[0] if vid in ADDRESS_FIX else None)
    if not op_addr:
        op_addr = venue['fields'].get('address', {}).get('value') or LEAD_ADDRESS.get(vid, (''))[0]
    if not op_addr:
        op_addr = log[vid]['address']
        errors.append('no address for ' + vid)
    # address claim
    if vid in ADDRESS_FIX:
        text, printed, note = ADDRESS_FIX[vid]
        a = fields['address']
        a.update({'value': text, 'quote': printed, 'verified_at': CHECKED,
                  'source_url': 'https://civichall.org/contact-us',
                  'source_locator': 'Contact page, Visit Us block',
                  'verified_at': CHECKED, 'run_id': RUN})
        fields['address'] = a
    elif vid in LEAD_ADDRESS:
        text, url, quoted = LEAD_ADDRESS[vid]
        a = fields.get('address') or {}
        a.update({'claim_id': a.get('claim_id'), 'value': text, 'quote': quoted,
                  'source_url': url, 'source_locator': 'Operator page address line',
                  'verified_at': CHECKED, 'run_id': RUN,
                  'source_title': venue.get('name') or LEAD_NAMES.get(vid)})
        fields['address'] = a
    # coordinates
    c = fields.get('coordinates') or {}
    lat, lon = float(h['lat']), float(h['lon'])
    name = h.get('name') or ''
    if tier == 'exact_venue':
        map_target = '%s, %s' % (name or venue.get('name'), op_addr)
    elif tier == 'building':
        map_target = op_addr
    elif tier == 'street':
        map_target = road + ', New York'
    else:
        map_target = addr_obj.get('neighbourhood') or addr_obj.get('suburb') or 'New York'
    if tier == 'exact_venue':
        evidence = ('Nominatim returns the named POI %r (%s/%s) at house number %s on %s; the '
                    'operator prints %r.' % (name, h.get('category'), h.get('type'), number, road,
                                              op_addr))
    elif tier == 'building':
        evidence = ('Nominatim returns house number %s on %s (%s/%s); the operator prints %r. No '
                    'room entrance is proven.' % (number, road, h.get('category'), h.get('type'),
                                                  op_addr))
    else:
        evidence = ('Nominatim returns %s only; no house number matched the operator address %r.'
                    % (road or 'the street', op_addr))
    if remark:
        evidence += ' ' + remark
    refused = []
    for k, look in log[vid]['lookups'].items():
        if not look.get('response'):
            refused.append('%s -> %s' % (look.get('query'), look.get('error') or 'no result'))
    if key == '__extra__':
        qtext = '124 East 14th Street, New York, NY 10003'
        qurl = ('https://nominatim.openstreetmap.org/search?format=jsonv2&addressdetails=1'
                '&extratags=1&limit=4&accept-language=en&q=124+East+14th+Street%2C+New+York%2C+NY+10003')
    else:
        qtext = log[vid]['lookups'][key]['query']
        qurl = log[vid]['lookups'][key]['url']
    c.update({
        'claim_id': c.get('claim_id'),
        'value': {'latitude': lat, 'longitude': lon, 'precision': tier,
                  'map_target': map_target},
        'provider': 'OpenStreetMap Nominatim',
        'query': qtext,
        'request_url': qurl,
        'returned_place': h.get('display_name'),
        'match_evidence': evidence,
        'checked_on': CHECKED,
        'verified_at': CHECKED,
        'run_id': RUN,
        'derived': True,
        'derived_from': 'address',
        'note': ('One live Nominatim search per address on 2026-11-26, re-run for every row '
                 'including those that already carried a point; the point is the tier stated, not a '
                 'surveyed entrance.'),
        'refused_lookups': '; '.join(refused) if refused else None,
        'quote': quote_for(h),
        'source_title': 'Nominatim (OpenStreetMap) forward geocode',
        'source_url': qurl,
        'source_locator': 'Nominatim response, checked 2026-11-26',
    })
    fields['coordinates'] = c
    if vid in LEAD_NAMES:
        venue['name'] = LEAD_NAMES[vid]
        dn = fields.get('display_name') or {}
        lead_url = LEAD_ADDRESS.get(vid, (None, None))[1]
        dn.update({'claim_id': dn.get('claim_id'), 'value': LEAD_NAMES[vid],
                   'quote': LEAD_NAMES[vid], 'verified_at': CHECKED, 'run_id': RUN,
                   'source_url': lead_url, 'source_locator': 'Operator page title'})
        fields['display_name'] = dn

STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
print('venues updated', len(store['venues']), 'errors', errors)
tiers = {}
for v in store['venues'].values():
    t = v['fields']['coordinates']['value']['precision']
    tiers[t] = tiers.get(t, 0) + 1
print('tiers', tiers)
