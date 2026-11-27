"""Main pass: rewrite the 36 venues, holidays, events, gaps, then save."""
import json
import re
from decimal import Decimal

import build_photos as BP

BP.STORE = STORE
BP.LISTING = LISTING
BP.CHECKED = CHECKED

# ---------------------------------------------------------------- venues
venue_report = []
for vid, venue in sorted(STORE['venues'].items()):
    fields = venue.setdefault('fields', {})
    src_url = fields['source_url']['value']
    title = fields.get('display_name', {}).get('value') or venue['name']

    # ---- address
    if vid in MANUAL_ADDRESS:
        addr_value, capture, locator, quote, addr_title, addr_url = MANUAL_ADDRESS[vid]
        # the capture path stored in the claim is relative to the city dir
        cap_name = capture.replace('captures/', '')
        addr_line = locator
    else:
        cap_name = 'src-%s.txt' % vid
        pc = LISTING[vid]['spans']  # ensure listing parsed
        # find the postal address line
        line_no, line_text = None, None
        for raw in lines_of(cap_name):
            m = re.match(r'^\s*(\d+)\|\s?(.*)$', raw)
            if not m:
                continue
            if re.search(r'Singapore,?\s*\d{6}', m.group(2)):
                line_no, line_text = int(m.group(1)), m.group(2).strip()
                break
        if not line_no:
            line_no, line_text = find_line(cap_name, fields['address']['value'].split(',')[-2].strip() if ',' in fields['address']['value'] else 'Singapore')
        addr_value = fields['address']['value']
        # normalise the operator listing's printed address to block + street + postcode
        m = re.search(r'(.+?),\s*Singapore,?\s*(\d{6})', line_text or '')
        if m:
            head = re.sub(r',\s*#', ' #', m.group(1).strip())
            addr_value = '%s, Singapore %s' % (head, m.group(2))
        locator = 'line %s' % line_no
        quote = line_text or addr_value
        addr_title = title
        addr_url = src_url

    ADDRESS_FIX = {
        'sg-31b594bd4607': '231 Bain Street, Bras Basah Complex #04-07, Singapore 180231',
        'sg-afe29d71b4e8': '23A Coleman Street, Singapore 179806',
    }
    addr_value = ADDRESS_FIX.get(vid, addr_value)

    set_field(venue, 'address', claim(
        'address', addr_value, title=addr_title, url=addr_url,
        capture='captures/' + cap_name, locator=locator, quote=quote,
        confidence='high'))

    # ---- coordinates
    geo = GEO[vid]
    chosen = geo.get('chosen') or {}
    provider = geo.get('provider') or ''
    is_photon = provider.startswith('Photon')
    if vid in COORD_OVERRIDE:
        tier, lat, lon, returned, note = COORD_OVERRIDE[vid]
    else:
        tier = 'building'
        lat, lon = chosen.get('lat'), chosen.get('lon')
        returned = ', '.join(filter(None, [chosen.get('name'), chosen.get('street'), chosen.get('pc')]))
        if is_photon:
            note = ('Independent Photon lookup on the operator-printed address; the point is the matched '
                    'building/number, not a surveyed room entrance.')
        else:
            note = ('Photon returned no tier-matching result; the independent Nominatim lookup on the '
                    'operator-printed address answered. The point is the matched building/number, not a '
                    'surveyed room entrance.')
    if vid == 'sg-13d49f8566fb':
        tier = 'exact_venue'
        note = ('Photon returned the venue POI "The Working Capitol" at house number 1 on Keong Saik Road '
                'with postcode 089109; the record is the whole venue, so the venue point is recorded as '
                'exact_venue.')
    if lat is None or lon is None:
        raise SystemExit('no coordinates for ' + vid)
    # every failed lookup, including the Photon attempt behind a Nominatim answer
    failed = list(FAILED_LOOKUPS.get(vid, []))
    if not is_photon and not any(f.startswith('Photon:') for f in failed):
        failed.insert(0, "Photon: no tier-matching result for '%s' (geocode-log-rev1.json provider note)"
                      % geo.get('query'))
    for cand in geo.get('candidates') or []:
        if cand.get('tier') is None:
            line = '%s, %s %s -> no tier match' % (cand.get('name'), cand.get('street'), cand.get('pc'))
            if line not in failed:
                failed.append(line)
    coord_value = {'latitude': float(lat), 'longitude': float(lon),
                   'precision': tier,
                   'map_target': returned}
    geo_extra = {
        'derived': True, 'derived_from': 'address', 'provider': provider,
        'query': geo.get('query'), 'checked_on': CHECKED,
        'geocode_response': 'geocode-responses/%s-%s.json' % (vid, 'photon' if is_photon else 'nominatim'),
        'returned_place': returned,
        'match_evidence': note,
        'failed_lookups': '; '.join(failed) if failed else 'none',
        'refused_lookups': '; '.join(failed) if failed else 'none',
        'note': ('One independent lookup per address on 2026-11-26, re-run for every venue including those '
                 'that already carried a point; the stored point is the tier stated, not a surveyed entrance. '
                 'The locator is the operator address line that was geocoded.'),
    }
    if vid in RETRY_RESPONSE:
        geo_extra['retry_response'] = 'geocode-responses/' + RETRY_RESPONSE[vid]
    set_field(venue, 'coordinates', claim(
        'coordinates', coord_value,
        title='Geocode of the operator-printed address (2026-11-26)',
        url=geo['request_url'] if isinstance(geo.get('request_url'), str) else 'https://photon.komoot.io/',
        capture='captures/' + cap_name,
        locator=locator,
        quote=quote,
        **geo_extra))

    # ---- access
    if vid in ACCESS_OVERRIDE:
        st8, st12, window, aq, aloc, basis, cond = ACCESS_OVERRIDE[vid]
    elif vid in UNKNOWN_ACCESS:
        st8, st12, window, aq, aloc = 'unknown', 'unknown', None, None, None
        basis = UNKNOWN_ACCESS[vid]
        cond = UNKNOWN_ACCESS[vid]
    else:
        sat = LISTING[vid]['spans'].get('Saturday') or LISTING[vid]['spans'].get('Sunday')
        span = normalise_span(sat.split('-'))
        first, last, text = price_row('src-%s.txt' % vid, 'Saturday')
        st8 = 'yes' if covers(span, '09:00', '17:00') else 'no'
        st12 = 'no'
        window = 'Sat %s (hire tariff)' % display_span(span)
        aq = text
        aloc = 'capture src-%s.txt lines %s-%s (Saturday price row)' % (vid, first, last)
        basis = ('The Saturday price row publishes hourly hire %s–%s%s; the span covers 09:00–17:00 but the page publishes no continuous 09:00–21:00 hire block, so only the 8-hour floor is claimed.'
                 % (span[0], span[1], (', minimum %s hours' % LISTING[vid]['min_hours']) if LISTING[vid]['min_hours'] else ''))
        cond = 'Hours differ by day; see the listing price table. Opening hours alone are not treated as a hire window.'

    access_value = window
    access_capture = 'captures/lli-facility-rates.txt' if vid in ('sg-86d82fc69fcf', 'sg-b57c010c7380', 'sg-c6889650a7db') else 'captures/' + cap_name
    extra = {'locator_note': cond} if aloc is None else {}
    set_field(venue, 'access_window', claim(
        'access_window', access_value, title=title, url=src_url,
        capture=access_capture,
        locator=aloc,
        quote=aq,
        conditions=cond, confidence='medium', **extra))
    w8 = {'state': st8, 'basis': basis if st8 != 'unknown' else cond}
    w12 = {'state': st12, 'basis': basis if st12 != 'unknown' else cond}
    set_field(venue, 'programme_windows', claim(
        'programme_windows', {'8': w8, '12': w12}, title=title, url=src_url,
        capture=access_capture,
        locator=aloc,
        quote=aq, confidence='medium', **extra))

    # ---- lifecycle stays as assessed; does not grow the list
    fields['lifecycle']['verified_at'] = TODAY
    fields['lifecycle']['run_id'] = RUN
    venue['lifecycle'] = fields['lifecycle']['value']
    venue['needs_human_verify'] = bool(st8 == 'unknown' and st12 == 'unknown')

    # derived blockers, never carried template text (rule 11)
    new_blockers = []
    aw = fields['access_window']
    if aw.get('value') is None:
        new_blockers.append({'claim_id': aw['claim_id'], 'field': 'access_window',
                             'text': cond, 'source_url': aw['source_url'],
                             'verified_at': TODAY})
    price = fields.get('price') or {}
    if price.get('value') in (None, ''):
        new_blockers.append({'claim_id': price.get('claim_id') or claim_id(RUN, vid, 'price'),
                             'field': 'price',
                             'text': 'No hire price is published on the captured page; the cost is unknown, not zero (checked 2026-11-26).',
                             'source_url': src_url, 'verified_at': TODAY})
    cap = fields.get('capacity') or {}
    if cap.get('value') in (None, ''):
        new_blockers.append({'claim_id': cap.get('claim_id') or claim_id(RUN, vid, 'capacity'),
                             'field': 'capacity',
                             'text': 'No room-level capacity is printed on the captured page (checked 2026-11-26).',
                             'source_url': src_url, 'verified_at': TODAY})
    old_blockers = venue.get('blockers') or []
    if old_blockers:
        venue.setdefault('history', {}).setdefault('blockers', []).extend(old_blockers)
    venue['blockers'] = new_blockers
    if venue['lifecycle'] == 'lead':
        reasons = []
        if aw.get('value') is None:
            reasons.append(cond)
        if cap.get('value') in (None, ''):
            reasons.append('No room-level capacity is published on the captured page.')
        venue['tier_reasons'] = reasons or ['Lead: the captured page publishes no hire terms or bookable interval.']
    else:
        venue['tier_reasons'] = []

    venue_report.append({'id': vid, 'name': title, 'address': addr_value,
                         'tier': tier, 'lat': float(lat), 'lon': float(lon),
                         'access8': st8, 'access12': st12, 'window': window,
                         'photos': None})

# ---------------------------------------------------------------- photos
photo_counts = {}
for vid, venue in STORE['venues'].items():
    recs = BP.photo_records(vid)
    STORE['photos'][vid] = recs
    usable = [r for r in recs if r.get('url') and not r.get('withheld')]
    photo_counts[vid] = {
        'total': len(usable),
        'room': sum(1 for r in usable if r.get('room_specific')),
        'fallback': sum(1 for r in usable if not r.get('room_specific')),
        'withheld': sum(1 for r in recs if r.get('withheld')),
        'views': sorted({r['view_kind'] for r in usable if r.get('view_kind')}),
    }
for row in venue_report:
    row['photos'] = photo_counts[row['id']]

json.dump({'venues': venue_report, 'photos': photo_counts},
          open(EVID / 'venue-report.json', 'w'), indent=1)
print('venues rebuilt', len(venue_report))
