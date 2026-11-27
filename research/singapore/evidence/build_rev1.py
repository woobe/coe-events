"""Build the revision-1 Singapore city store from the 2026-11-26 captures.

Every written claim names the capture file and the line(s) carrying its value.
Only facts read from a captured page are stored; everything else is a dated gap.
"""
import hashlib
import json
import re
from datetime import date
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
CAP = BASE / 'captures'
EVID = Path('/home/joe/repo_dev/coe-events/research/singapore/evidence')
STORE = json.load(open(BASE / 'city.json'))
LISTING = json.load(open(EVID / 'listing_parse.json'))
GEO = {r['venue_id']: r for r in json.load(open(BASE / 'geocode-log-rev1.json'))}
TODAY = '2026-11-26'
RUN = 'run-20261126-sg-r8'
CHECKED = '2026-11-26'


def claim_id(*parts):
    return 'cl-' + hashlib.md5(('|'.join(parts)).encode('utf-8')).hexdigest()[:12]


def claim(field, value, *, title, url, capture, locator, quote, confidence='high',
          **extra):
    rec = {
        'claim_id': claim_id(RUN, field, url, str(locator)),
        'value': value,
        'verified_at': TODAY,
        'run_id': RUN,
        'source_title': title,
        'source_url': url,
        'source_locator': locator,
        'quote': quote,
        'confidence': confidence,
        'capture': capture,
        'checked_on': CHECKED,
    }
    rec.update(extra)
    return rec


USED_CLAIM_IDS = set()


def set_field(venue, field, entry):
    # One claim id per fact. The id built from field + url + locator collides when
    # two rooms share a source page and locator (the three LLI rooms, the two High
    # Street Centre rooms, the two ISCA rooms). Keep the first id as built so no
    # legacy claim id is lost, and re-scope only the later collision to the venue.
    cid = entry.get('claim_id')
    if cid in USED_CLAIM_IDS and venue.get('venue_id'):
        cid = claim_id(venue['venue_id'], field, entry.get('source_url'),
                       str(entry.get('source_locator')))
        entry['claim_id'] = cid
    USED_CLAIM_IDS.add(cid)
    old = (venue.get('fields') or {}).get(field)
    venue.setdefault('fields', {})[field] = entry
    if old:
        venue.setdefault('history', {}).setdefault(field, []).append(old)


def lines_of(capture):
    p = CAP / capture
    if not p.exists():
        return []
    return p.read_text(encoding='utf-8', errors='replace').splitlines()


def find_line(capture, needle, start=1):
    for line in lines_of(capture):
        m = re.match(r'^\s*(\d+)\|\s?(.*)$', line)
        if not m:
            continue
        n = int(m.group(1))
        text = m.group(2).replace('\xa0', ' ').strip()
        if n >= start and needle.replace('\xa0', ' ').lower() in text.lower():
            return n, text
    return None, None


def price_row(capture, day):
    """Return (first_line, last_line, joined_text) for a day's price block."""
    rows = lines_of(capture)
    for i, raw in enumerate(rows):
        m = re.match(r'^\s*(\d+)\|\s?(.*)$', raw)
        if not m:
            continue
        if m.group(2).strip() == day:
            chunk = []
            nums = []
            for raw2 in rows[i:i + 10]:
                m2 = re.match(r'^\s*(\d+)\|\s?(.*)$', raw2)
                if not m2:
                    continue
                nums.append(int(m2.group(1)))
                chunk.append(m2.group(2).strip())
                if 'hire fee' in m2.group(2).lower():
                    break
            return nums[0], nums[-1], ' '.join(chunk)
    return None, None, None


def span_from(text):
    m = re.search(r'(\d{1,2}:\d{2})\s*[–-]\s*(\d{1,2}:\d{2})', text or '')
    return (m.group(1), m.group(2)) if m else (None, None)


def _mins(t):
    h, m = t.split(':')
    return int(h) * 60 + int(m)


def covers(span, start='09:00', end='21:00'):
    if not span[0]:
        return False
    s, e = span
    if e in ('0:00', '00:00'):
        e = '24:00'
    smin, emin = _mins(s), _mins(e)
    if emin <= smin:
        emin += 24 * 60  # a span ending after midnight
    return smin <= _mins(start) and emin >= _mins(end)


def display_span(span):
    s, e = span
    suffix = ''
    if e in ('0:00', '00:00'):
        e = '24:00'
    elif _mins(e) <= _mins(s):
        e = '%02d:%s' % (int(e.split(':')[0]) + 24, e.split(':')[1])
        suffix = ' (+1 day)'
    return '%02d:%s–%02d:%s%s' % (int(s.split(':')[0]), s.split(':')[1],
                                  int(e.split(':')[0]) % 24, e.split(':')[1], suffix)


def normalise_span(span):
    s, e = span
    if e in ('0:00', '00:00'):
        e = '24:00'
    return s, e


# ---------------------------------------------------------------- non-listing venues
# (address value, capture, line, quote, source title, source url)
MANUAL_ADDRESS = {
    'sg-0285e3753fc2': (
        '2 Town Hall Link, Singapore, 608516', 'captures/op-genting-marriott.txt', 'lines 879-880',
        '2 Town Hall Link, Singapore, 608516',
        'Four Points by Sheraton Singapore, Jurong — event spaces (Genting Hotel Jurong)',
        'https://www.marriott.com/en-gb/hotels/sinsp-four-points-singapore-jurong/events/'),
    'sg-09795cef4b0f': (
        '6 Raffles Boulevard, Marina Square, #03-308, Singapore 039594', 'captures/op-justco-marina.txt', 'line 128',
        '6 Raffles Boulevard, Marina Square, #03-308, Singapore 039594',
        'JustCo Marina Square — centre page', 'https://www.justcoglobal.com/en-sg/centre/justco-marina-square/'),
    'sg-13d49f8566fb': (
        '1 Keong Saik Road, Singapore 089109', 'captures/src-sg-13d49f8566fb.txt', 'lines 132-133',
        '1 Keong Saik Road Singapore 089109',
        'The Working Capitol — home', 'https://www.theworkingcapitol.com/'),
    'sg-34d6bf1ba39c': (
        'The Arts House at the Old Parliament, 1 Old Parliament Lane, Singapore 179429',
        'captures/op-ahg-screening.txt', 'lines 95-97',
        'Address: The Arts House at the Old Parliament 1 Old Parliament Lane, Singapore 179429',
        'Arts House Group — Screening Room', 'https://www.artshousegroup.sg/venue-hire/our-venues/tah-venue-details/screening-room'),
    'sg-5d3fcedef47c': (
        "1 St Andrew's Road, Singapore 178957", 'captures/op-ng-glass.txt', 'lines 180-181',
        "1 St Andrew's Road, Singapore 178957",
        'National Gallery Singapore — Glass Room', 'https://www.nationalgallery.sg/sg/en/about/venue-rental/glass-room.html'),
    'sg-61c5043af885': (
        '80 Bras Basah Road, Singapore 189560', 'captures/src-sg-61c5043af885.txt', 'line 1018',
        '80 Bras Basah Road, 189560, SINGAPORE, Singapore',
        'Fairmont Singapore — meetings', 'https://www.fairmont.com/en/hotels/singapore/fairmont-singapore/meetings.html'),
    'sg-86d82fc69fcf': (
        '11 Eunos Road 8, Singapore 408601', 'captures/op-lli-contact.txt', 'lines 22-23',
        '11 Eunos Road 8 Singapore 408601',
        'Lifelong Learning Institute — contact', 'https://www.lifelonglearningsg.org/contact-us/'),
    'sg-b57c010c7380': (
        '11 Eunos Road 8, Singapore 408601', 'captures/op-lli-contact.txt', 'lines 22-23',
        '11 Eunos Road 8 Singapore 408601',
        'Lifelong Learning Institute — contact', 'https://www.lifelonglearningsg.org/contact-us/'),
    'sg-c6889650a7db': (
        '11 Eunos Road 8, Singapore 408601', 'captures/op-lli-contact.txt', 'lines 22-23',
        '11 Eunos Road 8 Singapore 408601',
        'Lifelong Learning Institute — contact', 'https://www.lifelonglearningsg.org/contact-us/'),
    'sg-bff0f516d53e': (
        'Block 69 Ayer Rajah Crescent, Level 3 Vidacity, Singapore 139961', 'captures/op-lorong-about.txt', 'line 39',
        'Block 69 Ayer Rajah Crescent, Singapore 139961',
        'Lorong AI — about', 'https://lorong.ai/about.html'),
    'sg-c5e0795f1042': (
        '28 Aliwal Street, Singapore 199918', 'captures/op-ahg-aliwal-mph.txt', 'lines 94-95',
        'Aliwal Arts Centre 28 Aliwal St, Singapore 199918',
        'Arts House Group — Aliwal Arts Centre Multi-Purpose Hall',
        'https://www.artshousegroup.sg/venue-hire/our-venues/aac-venue-details/multi-purpose-hall'),
    'sg-d9552dd03dd7': (
        "1 St Andrew's Road, Singapore 178957", 'captures/op-ng-aud.txt', 'lines 203-204',
        "1 St Andrew's Road, Singapore 178957",
        'National Gallery Singapore — Ngee Ann Kongsi Auditorium & Foyer',
        'https://www.nationalgallery.sg/sg/en/about/venue-rental/ngee-ann-kongsi-auditorium-foyer.html'),
}

# coordinate overrides: tier, lat, lon, returned place, note
# Every note names the geocoder that actually answered; `provider` in the
# geocode log is Photon for 14 rows and Nominatim for 22.
COORD_OVERRIDE = {
    'sg-0285e3753fc2': ('building', 1.3314839, 103.7393574, 'Genting Hotel Jurong, 2 Town Hall Link',
                        'Photon returned the hotel POI at the operator-printed address; the ballroom itself has no separate OSM point, so the tier is building, not exact_venue.'),
    'sg-5d80f59cd550': ('building', 1.3096883, 103.8650884, '20 Kallang Avenue (listing geotag)',
                        'Photon returned street-level Kallang Avenue rows only (postcodes 339412, 339413 and 339416) with no house number; the Nominatim retry (geocode-responses/retry-pico.json) returned no result. The listing-page geotag for the room is recorded as the building point.'),
    'sg-9787a5fba342': ('building', 1.2962347, 103.8558084, '41 Beach Road (listing geotag)',
                        'Photon returned no result and the Nominatim retry (geocode-responses/retry-enclosed.json) returned no result for 41 Beach Road; the listing-page geotag for the room is recorded as the building point.'),
    'sg-bea2d52eb16e': ('building', 1.3097843, 103.8565905, '40 Sam Leong Road (listing geotag)',
                        'Photon returned no tier match; Nominatim matched Sam Leong Road with no house number at four postcodes (207274, 207900, 207903 and 207907), and the retry (geocode-responses/retry-highfive.json) repeated the street-level result. The listing-page geotag at the operator-printed number is recorded as the building point.'),
    'sg-ed2e35df4121': ('building', 1.2851901, 103.852758, '21 Collyer Quay (listing geotag)',
                        'Photon returned no result; Nominatim and its retry (geocode-responses/retry-wework21.json) matched Collyer Quay only, with no house number for 21. The listing-page geotag is recorded as the building point.'),
    'sg-bff0f516d53e': ('building', 1.2962231, 103.786897, '69 Ayer Rajah Crescent (Train Pod @ one-north)',
                        'Photon returned no tier match; Nominatim matched house number 69 with postcode 139961 but named a different tenant at the block (the retry, geocode-responses/retry-vidacity.json, returned no result). The block match is the building point, not a Vidacity entrance.'),
    'sg-c5e0795f1042': ('building', 1.302719, 103.8610238, 'Aliwal Arts Centre, 28-30 Aliwal Street',
                        'Photon returned no tier match; Nominatim returned the Aliwal Arts Centre entry with house number "30;28" and postcode 199918 at street level (retry geocode-responses/retry-aliwal.json the same); the operator prints 28, so this is a building match.'),
    'sg-a5d5d094bf2e': ('building', 1.2822208, 103.8495701, 'KPB Building, 60 Cecil Street, 049711',
                        'Photon returned no tier match; Nominatim matched KPB Building at house number 60 and Cecil Street but postcode 049711, two digits from the operator postcode 049709, and the retry (geocode-responses/retry-isca.json) returned no result. Recorded as a building match with the postcode conflict noted.'),
    'sg-b5dffa99af1f': ('building', 1.2822208, 103.8495701, 'KPB Building, 60 Cecil Street, 049711',
                        'Photon returned no tier match; Nominatim matched KPB Building at house number 60 and Cecil Street but postcode 049711, two digits from the operator postcode 049709, and the retry (geocode-responses/retry-isca.json) returned no result. Recorded as a building match with the postcode conflict noted.'),
}

# second-attempt Nominatim responses that exist on disk (venue id -> filename)
RETRY_RESPONSE = {
    'sg-5d80f59cd550': 'retry-pico.json',
    'sg-9787a5fba342': 'retry-enclosed.json',
    'sg-bea2d52eb16e': 'retry-highfive.json',
    'sg-ed2e35df4121': 'retry-wework21.json',
    'sg-bff0f516d53e': 'retry-vidacity.json',
    'sg-c5e0795f1042': 'retry-aliwal.json',
    'sg-a5d5d094bf2e': 'retry-isca.json',
    'sg-b5dffa99af1f': 'retry-isca.json',
    'sg-31b594bd4607': 'retry-brasbasah.json',
}

# lookups that did not produce the stored tier, stated per row
FAILED_LOOKUPS = {
    'sg-5d80f59cd550': ['Photon: street-level matches only (Kallang Avenue 339412, 339413, 339416); no house number',
                        'Nominatim: no result (geocode-responses/retry-pico.json)'],
    'sg-9787a5fba342': ['Photon: no result',
                        'Nominatim: no result (geocode-responses/retry-enclosed.json)'],
    'sg-bea2d52eb16e': ['Photon: no tier-matching result',
                        'Nominatim: street-level matches only (Sam Leong Road 207274, 207900, 207903, 207907); no house number (geocode-responses/retry-highfive.json)'],
    'sg-ed2e35df4121': ['Photon: no result',
                        'Nominatim: street-level matches only (Collyer Quay 049246, 049315, 049321, 049325, 018989); no house number for 21 (geocode-responses/retry-wework21.json)'],
    'sg-a5d5d094bf2e': ['Photon: no tier-matching result',
                        'Nominatim: KPB Building at 60 Cecil Street, postcode 049711 against operator 049709; strict postcode match failed (retry geocode-responses/retry-isca.json returned no result)'],
    'sg-b5dffa99af1f': ['Photon: no tier-matching result',
                        'Nominatim: KPB Building at 60 Cecil Street, postcode 049711 against operator 049709; strict postcode match failed (retry geocode-responses/retry-isca.json returned no result)'],
}

# access overrides: (state8, state12, window, quote, locator, basis, conditions)
ACCESS_OVERRIDE = {
    'sg-31b594bd4607': ('no', 'no', 'Sat 08:00–16:00 and 17:00–23:00 (two sessions)',
                        'Sat to Sun & PH, 8am to 4pm / 5pm to 11pm',
                        'captures/src-sg-31b594bd4607.txt line 107',
                        'The operator publishes two weekend sessions with a 16:00–17:00 gap, so neither a 09:00–17:00 nor a 09:00–21:00 continuous hire is sold.',
                        'Weekday package 08:00–23:00; Friday and PH eve split at 18:00.'),
    'sg-9d1a91764baf': ('yes', 'no', 'Sat 08:00–17:30 (full-day session)',
                        'Full Day (08:00 - 17:30 hours) Mon-Fri-$1,050 Weekend-$1,155',
                        'captures/src-sg-9d1a91764baf.txt lines 320-323',
                        'The listed full-day session ends at 17:30, so 09:00–17:00 is covered but 09:00–21:00 is not sold continuously; the 18:00–22:00 evening is a separate block.',
                        'Morning 08:00–12:30, afternoon 13:00–17:30 and evening 18:00–22:00 are separate blocks.'),
    'sg-afe29d71b4e8': ('no', 'no', 'Sat 10:00–23:30 (restaurant sessions)',
                        'Saturday 10:00 – 23:30',
                        'captures/src-sg-afe29d71b4e8.txt lines 225-230',
                        'The earliest published start is 10:00, so a 09:00–17:00 or 09:00–21:00 hire is not published; sessions run 10:00–15:00 and 16:00–23:30 per the listing.',
                        'Restaurant with in-house catering; lunch and dinner sessions.'),
    'sg-bea2d52eb16e': ('yes', 'no', 'Sat 08:00–24:00 (10-hour package, 12-hour access)',
                        '10-hour flexi package with 12 hours total access (incl. setup/teardown)',
                        'captures/src-sg-bea2d52eb16e.txt lines 104-109',
                        'The wedding package is a 10-hour hire with 12 hours of access including setup and teardown; it does not publish a 09:00–21:00 continuous event block.',
                        'Hourly hire 08:00–24:00; package pricing is per session.'),
    'sg-86d82fc69fcf': ('yes', 'yes', 'Daily 08:00–22:00 (facility booking hours)',
                        'Full day block (8am-10pm)',
                        'captures/lli-facility-rates.txt lines 22-23',
                        'The operator rate card publishes bookable facility hours 0800–2200 every day including public holidays and a full-day block 08:00–22:00, which covers 09:00–21:00 continuously.',
                        'Facility booking hours 0800–2200 are printed at line 7; four-hour blocks 08:00–12:00, 13:00–17:00 and 18:00–22:00; 08:00–17:00 and 13:00–22:00 blocks; full day 08:00–22:00.'),
    'sg-b57c010c7380': ('yes', 'yes', 'Daily 08:00–22:00 (facility booking hours)',
                        'Full day block (8am-10pm)',
                        'captures/lli-facility-rates.txt lines 22-23',
                        'The operator rate card publishes bookable facility hours 0800–2200 every day including public holidays and a full-day block 08:00–22:00, which covers 09:00–21:00 continuously.',
                        'Facility booking hours 0800–2200 are printed at line 7; four-hour blocks 08:00–12:00, 13:00–17:00 and 18:00–22:00; 08:00–17:00 and 13:00–22:00 blocks; full day 08:00–22:00.'),
    'sg-c6889650a7db': ('yes', 'yes', 'Daily 08:00–22:00 (facility booking hours)',
                        'Full day block (8am-10pm)',
                        'captures/lli-facility-rates.txt lines 22-23',
                        'The operator rate card publishes bookable facility hours 0800–2200 every day including public holidays and a full-day block 08:00–22:00, which covers 09:00–21:00 continuously.',
                        'Facility booking hours 0800–2200 are printed at line 7; four-hour blocks 08:00–12:00, 13:00–17:00 and 18:00–22:00; 08:00–17:00 and 13:00–22:00 blocks; full day 08:00–22:00.'),
}

UNKNOWN_ACCESS = {
    'sg-0285e3753fc2': 'The Marriott/Genting Hotel Jurong event page publishes capacity and a floor plan but no hire rate, hire interval or booking terms; the RWS venue page returned HTTP 404 on 2026-11-26. No hire window is published.',
    'sg-09795cef4b0f': 'The JustCo centre page publishes staffed hours (Mon–Fri 08:30–18:00, members 24/7) and no event-space hire interval or rate; staffed hours are not a booking window.',
    'sg-13d49f8566fb': 'The Working Capitol site sells desks and offices and publishes no function-room hire terms or interval.',
    'sg-34d6bf1ba39c': 'The Arts House Screening Room page publishes address, capacity and area but the venue-rate tab is not rendered in the captured HTML; no hire interval is published.',
    'sg-5d3fcedef47c': 'The Glass Room page publishes capacity, area and a floor plan but no hire rate or interval; rental is by enquiry.',
    'sg-61c5043af885': 'The Fairmont meetings page publishes room capacities and floor plans but no hire rate or interval; booking is through the sales team.',
    'sg-bff0f516d53e': 'Lorong AI and Vidacity describe the community hub and event space but publish no hire rate or bookable interval.',
    'sg-c5e0795f1042': 'The Aliwal Multi-Purpose Hall page publishes the centre opening hours (07:00–23:00 daily) and a rate tab that is not rendered; opening hours are not a hire window.',
    'sg-d9552dd03dd7': 'The Ngee Ann Kongsi Auditorium page publishes capacity, area and floor plans but no hire rate or interval; rental is by enquiry.',
}
