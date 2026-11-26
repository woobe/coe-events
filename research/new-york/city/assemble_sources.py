"""R9: sources ledger, declared gaps, revision flag and store timestamp."""
import json, hashlib
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
RUN = 'run-20261126-nyc-r9'
CHECKED = '2026-11-26'
store = json.loads(STORE.read_text())
inv = json.loads((CITY / 'event-inventory.json').read_text())
matrix = json.loads((CITY / 'event-matrix.json').read_text())

EVENT_URLS = {}
for row in inv:
    EVENT_URLS[row['urls'][0]] = row['name']
EVENT_URLS.update({
    'https://ethglobal.com/events': 'ETHGlobal events directory (ETHConf 2027)',
    'https://www.eventbrite.com/e/daos-con-7-tickets-1994392414399': 'DAOS CON 7 — Eventbrite',
    'https://www.eventbrite.com/e/blockchain-tech-summit-4th-annual-tickets-1990305841349':
        'Blockchain Tech Summit (4th Annual) — Eventbrite',
    'https://events.linuxfoundation.org/agntsummit-new-york-city/':
        'AGNTSummit New York City — Linux Foundation event page',
})

rows = store['sources_consulted']
by_url = {}
for r in rows:
    r.setdefault('lane', 'venue' if 'tagvenue' in (r.get('url') or '') else 'other')
    r.setdefault('pages_read', 1)
    r.setdefault('hits', 0)
    r.setdefault('dedupe', 0)
    r.setdefault('event_yield', 0)
    r.setdefault('venue_yield', 0)
    r.setdefault('disposition', 'checked')
    r.setdefault('mandatory', False)
    r.setdefault('accessed_on', r.get('checked_on'))
    by_url[r['url']] = r

for url, name in EVENT_URLS.items():
    row = by_url.get(url)
    if row is None:
        row = {'url': url, 'title': name, 'checked_on': CHECKED, 'accessed_on': CHECKED,
               'check_status': 'checked' if url != 'https://events.chainalysis.com/Links-2027' else 'blocked',
               'lane': 'event', 'pages_read': 1, 'hits': 1, 'dedupe': 0,
               'event_yield': 1, 'venue_yield': 0, 'mandatory': False,
               'disposition': 'kept'}
        rows.append(row)
        by_url[url] = row
    else:
        row['event_yield'] = 1
        row['lane'] = 'event'
        row['hits'] = max(1, int(row.get('hits') or 0))
        row['disposition'] = 'kept'

ADD = [
    ('lane', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=machine%20learning',
     'Meetup New York machine-learning search', 200),
    ('lane', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=data%20science',
     'Meetup New York data-science search', 200),
    ('lane', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=web3',
     'Meetup New York Web3 search', 200),
    ('lane', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=crypto',
     'Meetup New York crypto search', 200),
    ('lane', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=blockchain',
     'Meetup New York blockchain search', 200),
    ('lane', 'https://www.eventbrite.com/d/ny--new-york/machine-learning/',
     'Eventbrite New York machine-learning browse', 200),
    ('lane', 'https://www.eventbrite.com/d/ny--new-york/data-science/',
     'Eventbrite New York data-science browse', 200),
    ('lane', 'https://www.eventbrite.com/d/ny--new-york/web3/', 'Eventbrite New York Web3 browse', 200),
    ('lane', 'https://www.eventbrite.com/d/ny--new-york/crypto/', 'Eventbrite New York crypto browse', 200),
    ('lane', 'https://www.eventbrite.com/d/ny--new-york/blockchain/',
     'Eventbrite New York blockchain browse', 200),
    ('holiday', 'https://www.nyc.gov/assets/opa/downloads/pdf/three-year-calendar-25-26-27.pdf',
     'NYC Office of Payroll Administration — 2025-2027 Holiday and Pay Calendar', 200),
    ('holiday', 'https://www.nyc.gov/assets/dcas/downloads/pdf/reports/440_2.pdf',
     'DCAS Personnel Services Bulletin 440-2 — Observance of Public Holidays', 200),
    ('holiday', 'https://newyork.public.law/laws/n.y._general_construction_law_section_24',
     'New York General Construction Law §24 — Public holidays', 200),
    ('holiday', 'https://www.schools.nyc.gov/calendar/2027-2028-school-year-calendar',
     'NYC Public Schools 2027-2028 calendar (not published)', 404),
    ('venue', 'https://civichall.org/contact-us', 'Civic Hall — Contact Us (address)', 200),
    ('venue', 'https://s-media.nyc.gov/agencies/lpc/lp/1963.pdf',
     'NYC Landmarks Preservation Commission LP-1963 — Brooklyn Public Library, Central Building', 200),
    ('venue', 'https://www.bklynlibrary.org/locations/central/meeting-rooms',
     'Brooklyn Public Library — Central Library meeting rooms (blocked)', 403),
    ('venue', 'https://events.chainalysis.com/Links-2027?calendar-iCal&u=677a5829ece36522',
     'Chainalysis Links 2027 — iCal export (blocked)', 403),
]
for lane, url, title, status in ADD:
    if url in by_url:
        continue
    rows.append({'url': url, 'title': title, 'checked_on': CHECKED, 'accessed_on': CHECKED,
                 'check_status': 'blocked' if status >= 400 else 'checked',
                 'lane': lane, 'pages_read': 1, 'hits': 0, 'dedupe': 0, 'event_yield': 0,
                 'venue_yield': 0, 'mandatory': url in (
                     'https://miragather.com/', 'https://miragather.com/?tab=side',
                     'https://miragather.com/ai', 'https://aitinkerers.org/all_cities',
                     'https://luma.com/decentralized_ai_events?period=past'),
                 'disposition': 'blocked — HTTP %d' % status if status >= 400 else 'opened — no 2027 lead',
                 'note': ('HTTP %d on %s.' % (status, CHECKED)) if status >= 400 else None})

store['sources_consulted'] = rows

store['refresh_revision'] = 1
store['updated_at'] = '2026-11-26T12:00:00Z'

gaps = [
    ('coordinates',
     'The Monroe Room sits on two OSM points for 15 West 38th Street; the west-side office node '
     '(-73.9837008) is used and the east-side node is recorded as a conflict, so the pin is the '
     'building, not a proven door.',
     ['geocode/nyc-75c0f7334372.json', 'venues.nyc-75c0f7334372.fields.coordinates']),
    ('coordinates',
     'Ridgewood Hall is pinned to the 60-47 Metropolitan Avenue house number, but OSM places it in '
     'Middle Village 11378 while the operator prints Ridgewood 11385; the tier is building.',
     ['geocode/nyc-6d04b6ce2634.json', 'venues.nyc-6d04b6ce2634.fields.coordinates']),
    ('address',
     'Civic Hall was stored at 28 East 28th Street; the operator contact page prints 124 East 14th '
     'Street, New York, NY 10003 (Zero Irving, Union Square). The address claim was corrected and '
     'the venue re-geocoded to the named Civic Hall POI.',
     ['captures/rev1-civic-hall-contact.html', 'venues.nyc-4c6638c43df6.fields.address']),
    ('photos',
     'Four venues carry no cleared photo: NYU Kimmel (page HTTP 202, empty body), the Monroe Room '
     '(Peerspace HTTP 403), Seminar Room A (HTTP 429) and Brooklyn Public Library (HTTP 403). '
     'Nothing is shown rather than an unplaceable image.',
     ['captures/venue-nyc-12c98ff34e33.html', 'captures/venue-nyc-75c0f7334372.html',
      'captures/venue-nyc-ca43f10af68d.html', 'captures/venue-nyc-lead-bpl-meeting-rooms.html']),
    ('photos',
     'The Advent Hope page carries one uncaptioned hero image and no room gallery, so it is '
     'withheld; no licence text or room caption exists to place it.',
     ['captures/venue-nyc-lead-advent-hope.html']),
    ('photos',
     'Most cleared photos are operator-uploaded gallery assets served by the Tagvenue listing. '
     'The listings publish no separate licence text; each record carries an attributed hotlink and '
     'the operator brand, and 5 files are CC-licensed Wikimedia Commons building/interior views.',
     ['photos (28 venue collections)', 'claim: rights field per photo record']),
    ('holiday-authority',
     'The NYC Public Schools 2027-2028 edition is not published: '
     'schools.nyc.gov/calendar/2027-2028-school-year-calendar returned HTTP 404 on 2026-11-26. '
     'School coverage therefore stops at the 2026-2027 last day, 28 June 2027.',
     ['captures/rev1-nycps-2027-2028.html', 'coverage:US-NY:nycps']),
    ('holiday-scope',
     'The city layer is the OPA/DCAS employee-holiday scope, not a mayoral proclamation of every '
     'office closure. Lincoln\u2019s Birthday (12 February 2027) is stored as a floating, '
     'eligible-only row per PSB 440-2, not as a universal closure.',
     ['captures/rev1-dcas-psb-440-2.pdf', 'holidays[US-NY:nyc 2027-02-12]']),
    ('holiday-scope',
     'General Construction Law \u00a724 also lists Flag Day (14 June); it is a public holiday in the '
     'statute but is not observed as a closure by the authorities read, so no Flag Day row is stored.',
     ['captures/rev1-gcl-24-public-law.txt']),
    ('event',
     'PE4KS prints only "March 2027 NYC" on 2026-11-26; the stored 23\u201324 March days come from the '
     '2026-11-24 read and are flagged needs_human_verify.',
     ['captures/event-nyc-ev-0a26f2593747.txt', 'events.nyc-ev-0a26f2593747']),
    ('event',
     'tech-week.com returned HTTP 429 twice on 2026-11-26; the 7\u201313 June 2027 dates are retained '
     'from the prior read and corroborated by the MiraGather Tech Week NYC 2027 listing.',
     ['captures/event-nyc-ev-bd7f1957c460.html', 'captures/lane-miragather-main.html']),
    ('event',
     'events.chainalysis.com returned HTTP 403 on 2026-11-26; the 30\u201331 March 2027 dates are '
     'retained from the prior indexed read and corroborated by the MiraGather Chainalysis Links 2027 '
     'listing.',
     ['captures/event-nyc-ev-links2027.html', 'captures/lane-miragather-main.html']),
    ('event',
     'Meetup and Luma city/alias pages printed no 2027 New York occurrence on 2026-11-26 (near-term '
     '2026 listings only); the AI Tinkerers directory returned HTTP 403. Those lanes are recorded as '
     'opened-and-empty or blocked, not as coverage.',
     ['lane-report.json', 'event-matrix.json']),
    ('access',
     'Five rooms print "Open 24 hours" on the Saturday price row with no hire interval (Nomadworks '
     'Conference Center, Event Loft 1505, Large Flex Event Loft, La Victoria and Ideal Glass Atrium); '
     'that is an availability/opening line, so their 12-hour state fell from yes to unknown.',
     ['access-blocks.json', 'venues.*.fields.programme_windows.12']),
    ('access',
     'Two rows price Saturday per session, not per hour (SAINT Secret Garden and Producers Club '
     'Sonnet); no session length is published, so a continuous 09:00-21:00 booking is unknown.',
     ['access-blocks.json']),
    ('card-conflict',
     'Acceptance criterion 4 on this card names Lovdata and Utdanningsetaten (the Oslo authorities). '
     'This is a copy of the Oslo card: the body and the named-sources section direct New York to OPM, '
     'NYS Civil Service, NYC OPA/DCAS and NYC Public Schools, and that is what was read.',
     ['local/design/refresh-plan-v1.md §4 named sources', 'coverage (4 rows)']),
]
store['declared_gaps'] = [
    {'kind': kind, 'text': text, 'evidence_refs': refs, 'checked_on': CHECKED}
    for kind, text, refs in gaps
]

STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
print('sources', len(store['sources_consulted']),
      'yield sum', sum(int(r.get('event_yield') or 0) for r in store['sources_consulted']),
      'events', len(store['events']), 'gaps', len(store['declared_gaps']))
