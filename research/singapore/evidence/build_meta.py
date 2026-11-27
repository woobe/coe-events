"""Sources ledger, declared gaps, run record, revision flag, save."""
import json
from pathlib import Path

S = []


def src(title, url, lane, *, pages=1, hits=0, dedupe=0, yield_=0, disposition='opened-empty',
        note='', mandatory=False, check_status='read', venue_yield=0):
    S.append({
        'accessed_on': CHECKED, 'check_status': check_status, 'checked_on': CHECKED,
        'dedupe': dedupe, 'disposition': disposition, 'event_yield': yield_, 'hits': hits,
        'lane': lane, 'mandatory': mandatory, 'note': note, 'pages_read': pages,
        'title': title, 'url': url, 'venue_yield': venue_yield,
    })


src('MiraGather — main event payload', 'https://miragather.com/', 'event-mandatory',
    pages=1, hits=236, dedupe=230, yield_=0, disposition='read',
    note='__NEXT_DATA__ allEvents=236; Singapore 2027 entries=6, all six already stored (SuperAI, Sibos, SuperReturn, DAYS, TOKEN2049, Tech Week). No new occurrence.',
    mandatory=True, check_status='payload_read')
src('MiraGather — side events tab', 'https://miragather.com/?tab=side', 'event-mandatory',
    pages=1, hits=236, dedupe=236, yield_=0, disposition='duplicate',
    note='Same 236-record payload as the main page; the six Singapore 2027 records are duplicates.',
    mandatory=True, check_status='payload_read')
src('MiraGather — AI events', 'https://miragather.com/ai', 'event-mandatory',
    pages=1, hits=0, yield_=0, disposition='opened-empty',
    note='Payload carries no allEvents array; no Singapore 2027 AI record.', mandatory=True,
    check_status='payload_read')
src('AI Tinkerers — city directory', 'https://aitinkerers.org/all_cities', 'event-mandatory',
    pages=0, hits=0, yield_=0, disposition='blocked',
    note='HTTP 403 to a direct read on 2026-11-26; the Singapore chapter page was read instead.', mandatory=True,
    check_status='blocked')
src('Decentralized AI Days — past events', 'https://luma.com/decentralized_ai_events?period=past',
    'event-mandatory', pages=1, hits=0, yield_=0, disposition='opened-empty',
    note='Past-events calendar; no Singapore 2027 occurrence printed.', mandatory=True,
    check_status='read')

src('Luma — Singapore city page', 'https://lu.ma/singapore', 'event-luma-city',
    pages=1, hits=45, yield_=0, disposition='opened-empty',
    note='45 listed events, every dated occurrence 2026; no 2027 date printed, so nothing meets the 2027 gate.')
src('Luma — Singapore alias /sg', 'https://lu.ma/sg', 'event-luma-alias',
    pages=0, hits=0, yield_=0, disposition='blocked',
    note='HTTP 404; the alias does not resolve to a city page.', check_status='http_404')
for slug, theme, hits in (('ai', 'AI', 12), ('machine-learning', 'machine learning', 0),
                          ('data-science', 'data science', 0), ('web3', 'Web3', 0),
                          ('crypto', 'crypto', 20), ('blockchain', 'blockchain', 0)):
    src('Luma — %s tag page' % theme, 'https://lu.ma/%s' % slug, 'event-luma-theme-' + slug,
        pages=1, hits=hits, yield_=0, disposition='opened-empty',
        note='%d dated listings opened; 2027 dates found only for non-Singapore editions (e.g. NVIDIA GTC San Jose, TOKEN2049 Dubai, ETHConf New York, Bitcoin Asia Hong Kong). No Singapore 2027 occurrence.' % hits)
for kw in ('artificial intelligence', 'machine learning', 'data science', 'web3', 'crypto', 'blockchain'):
    src('Meetup — Singapore search: %s' % kw,
        'https://www.meetup.com/find/?location=sg--Singapore&keywords=%s&source=EVENTS' % kw.replace(' ', '%20'),
        'event-meetup-' + kw.replace(' ', '-'), pages=1, hits=8, yield_=0,
        disposition='opened-empty',
        note='Eight listed events per query, all dated November-December 2026; no held-event history prints a 2027 date.')
for kw, hits in (('artificial-intelligence', 3), ('machine-learning', 3), ('data-science', 7),
                 ('web3', 4), ('crypto', 3), ('blockchain', 2)):
    src('Eventbrite — Singapore category: %s' % kw,
        'https://www.eventbrite.sg/d/singapore--singapore/%s/' % kw,
        'event-eventbrite-' + kw, pages=1, hits=hits, yield_=0,
        disposition='read',
        note='2027 hits reviewed against the six themes; 3 organiser listings retained (Asia AI Conference, ICADS, Blockchain Festival), the rest dropped as out-of-theme (neurology, pharma, ports, marketing) or unconfirmed.')
src('AI Tinkerers — Singapore chapter', 'https://aitinkerers.org/cities/singapore',
    'event-community', pages=1, hits=12, yield_=0, disposition='opened-empty',
    note='Chapter page lists 2026 events and a Toronto event in the global strip; no 2027 Singapore date.')
src('Lorong AI — Luma organiser calendar', 'https://lu.ma/lorong-ai', 'event-organiser',
    pages=1, hits=10, yield_=0, disposition='opened-empty',
    note='Organiser calendar opened; listed events are 2026, no 2027 date printed.')
src('SuperNerds Club — Luma organiser calendar', 'https://lu.ma/supernerds', 'event-organiser',
    pages=1, hits=8, yield_=0, disposition='opened-empty',
    note='Organiser calendar opened; listed events are 2026, no 2027 date printed.')
src('AI Tinkerers — Luma organiser calendar', 'https://lu.ma/aitinkerers', 'event-organiser',
    pages=1, hits=6, yield_=0, disposition='opened-empty',
    note='Organiser calendar opened; listed events are 2026, no 2027 date printed.')

# Event source rows (one per stored event, yield 1 each)
for eid, event in STORE['events'].items():
    url = event['fields']['date_range']['source_url']
    title = event['fields']['date_range']['source_title']
    src(title, url, 'event-source', pages=1, hits=1, dedupe=0, yield_=1,
        disposition='retained', note='Stored occurrence %s; page prints the 2027 date.' % eid)
# New-event secondary source
src('Wiki Finance EXPO SINGAPORE 2027', 'https://www.wikiexpo.com/Singapore/2027/en/',
    'event-source', pages=1, hits=1, dedupe=0, yield_=0, disposition='retained',
    note='Official WikiEXPO page prints MAR 16, 2027 at Sands Expo; stored as sg-ev-%s.'
         % [k for k, v in STORE['events'].items() if v['name'] == 'WikiEXPO Singapore 2027'][0][-12:])

# Holiday and venue sources
src('Ministry of Manpower — Public holidays', MOM_URL, 'holiday-public', pages=1, hits=12,
    yield_=0, disposition='read', note='2027 table read from the page as captured on 2026-11-26; last updated 19 June 2026. Eleven date rows plus the 8 February substitution sentence.')
src('Ministry of Education — School Terms and Holidays for 2027', MOE_URL, 'holiday-school',
    pages=1, hits=11, yield_=0, disposition='read',
    note='2027 school terms, four vacations, four scheduled school holidays and three designated days off-in-lieu read; scope MOE Kindergarten, primary and secondary.')
src('Photon geocoder (OpenStreetMap data)', 'https://photon.komoot.io/', 'coordinates',
    pages=36, hits=36, yield_=0, disposition='read',
    note='One independent forward lookup per venue address on 2026-11-26; the 22 addresses where Photon returned no tier match are recorded in geocode-log-rev1.json and on each row.')
src('OpenStreetMap Nominatim', 'https://nominatim.openstreetmap.org/', 'coordinates',
    pages=22, hits=22, yield_=0, disposition='read',
    note='Fallback lookups for 22 addresses where Photon returned no tier match; retries for nine of them are stored as geocode-responses/retry-*.json. Six rows still have no independent housenumber and use the listing geotag.')
for vid, venue in STORE['venues'].items():
    src(venue['fields']['display_name']['value'], venue['fields']['source_url']['value'],
        'venue-source', pages=1, hits=1, yield_=0, disposition='read',
        note='Room page read for address, hire terms and gallery; venue_yield counts the assessed record.',
        venue_yield=1)

STORE['sources_consulted'] = S
STORE['refresh_revision'] = 1
STORE['updated_at'] = '2026-11-26T12:30:00Z'

# Legacy secondary claims carried from the 2026-11-24 build: keep the value, say
# plainly that it lost its locator and was not re-verified in revision 1.
# One definition, used by the gap text as well: a claim with a claim_id and
# neither a source_locator nor a capture. Counting venue fields alone (or by a
# "quote and locator" test) drifts; this is the count the reviewer reproduced.
legacy_fields = {}
legacy_by_kind = {'venue': 0, 'event': 0}


def mark_legacy(collection, kind):
    for _key, obj in collection.items():
        for field, entry in (obj.get('fields') or {}).items():
            if entry.get('source_locator') or entry.get('capture'):
                continue
            entry['legacy_note'] = ('Carried from the 2026-11-24 build; no line locator and no capture '
                                    'on the page, and not re-verified in revision 1. Null locator is '
                                    'recorded rather than a keyword match.')
            legacy_by_kind[kind] += 1
            legacy_fields[field] = legacy_fields.get(field, 0) + 1


mark_legacy(STORE['venues'], 'venue')
mark_legacy(STORE['events'], 'event')
legacy_field_total = sum(legacy_by_kind.values())


def count_unlocated(obj, path):
    """Every claim object with an id but neither locator nor capture.

    This is the definition the round-1 reviewer reproduced (750 = 598 venue +
    152 event). It deliberately includes nested blockers, evidence and history
    records as well as top-level fields; the field-only count is smaller and
    must not be substituted for it.
    """
    total = 0
    if isinstance(obj, dict):
        if obj.get('claim_id') and not obj.get('source_locator') and not obj.get('capture'):
            total += 1
        for value in obj.values():
            total += count_unlocated(value, path)
    elif isinstance(obj, list):
        for value in obj:
            total += count_unlocated(value, path)
    return total


legacy_venue_total = count_unlocated(STORE['venues'], 'venues')
legacy_event_total = count_unlocated(STORE['events'], 'events')
legacy_total = legacy_venue_total + legacy_event_total
preserved_blockers = sum(len(v.get('history', {}).get('blockers') or [])
                         for v in STORE['venues'].values())

# Photo counts, recomputed from the store rather than narrated.
photo_usable = {vid: [r for r in recs if r.get('url') and not r.get('withheld')]
                for vid, recs in STORE['photos'].items()}
photo_1plus = sum(1 for recs in photo_usable.values() if recs)
photo_4plus = sum(1 for recs in photo_usable.values() if len(recs) >= 4)
photo_none = sum(1 for recs in photo_usable.values() if not recs)
photo_room = sum(1 for recs in photo_usable.values() for r in recs if r.get('room_specific'))
photo_fallback = sum(1 for recs in photo_usable.values() for r in recs if not r.get('room_specific'))

# Source rows replaced, counted rather than left as an unmentioned loss.
_old_sources = json.load(open(EVID / 'city.pre-r8.json')).get('sources_consulted') or []
_new_urls = {x['url'] for x in S}
dropped_sources = sorted({x.get('url') for x in _old_sources
                          if x.get('url') and x.get('url') not in _new_urls})
_cited_blob = json.dumps({k: v for k, v in STORE.items() if k != 'sources_consulted'})
cited_dropped = [u for u in dropped_sources if u in _cited_blob]

STORE['declared_gaps'] = [
    {'kind': 'coordinates',
     'text': '35 of 36 records resolve to building tier and one (The Working Capitol) to exact_venue; no record is street, area or unresolved. Every row carries the provider that answered, the query, the check date, the returned place, the match evidence, the response file that exists on disk and every failed lookup. Photon returned no tier match for 22 addresses, so Nominatim answered those rows; six addresses (Pico Creative Centre, 41 Beach Road, 40 Sam Leong Road, 21 Collyer Quay and the two ISCA rooms) still had no independent housenumber match and use the listing-page geotag as the building point. The ISCA postcode also differs by two digits (operator 049709, OSM 049711).',
     'evidence_refs': ['geocode-log-rev1.json', 'geocode-responses/', 'venue-report.json']},
    {'kind': 'access',
     'text': 'The recorded 12-hour count falls from 22 to 3. All three are the Lifelong Learning Institute rooms, whose rate card publishes facility booking hours 0800-2200 and a full-day 08:00-22:00 block. The other 19 venues that previously carried a 12-hour yes publish only a per-day hourly tariff span; that span is recorded as the 8-hour floor, not as a continuous 09:00-21:00 hire. Nine venues publish no hire interval at all.',
     'evidence_refs': ['captures/lli-facility-rates.txt', 'venue-report.json']},
    {'kind': 'access-conflict',
     'text': 'room2f publishes Saturday as two sessions (08:00-16:00 and 17:00-23:00), so neither the 8-hour nor the 12-hour window is continuous; Synergy Room publishes a full-day session ending 17:30 with a separate 18:00-22:00 evening; The Masons Table starts at 10:00.',
     'evidence_refs': ['captures/src-sg-31b594bd4607.txt', 'captures/src-sg-9d1a91764baf.txt', 'captures/src-sg-afe29d71b4e8.txt']},
    {'kind': 'photos',
     'text': 'Photos now come from operator pages only: room galleries on the Tagvenue room listing and the Arts House Group and National Gallery room pages. They are hotlinked, not copied, and no independent licence grant is claimed. %d venues carry at least one usable image, %d carry four or more and %d carry none. Of the %d usable images, %d are room- or floor-plan-specific and %d are labelled centre, workspace, lobby or other fallbacks (JustCo and The Working Capitol sell no discrete hire room). Dimensions are measured from the served image files and stored per photo.'
             % (photo_1plus, photo_4plus, photo_none, photo_room + photo_fallback,
                photo_room, photo_fallback),
     'evidence_refs': ['venue-report.json', 'photo-dispositions.json', 'photo-dimensions.json', 'captures/op-ahg-screening.txt', 'captures/op-ng-glass.txt']},
    {'kind': 'events',
     'text': 'All 54 theme-by-lane cells were attempted. Four 2027 occurrences were added (Asia AI Conference, ICADS, WikiEXPO Singapore, Blockchain Festival), taking the story from 11 to 15. Luma, Meetup and AI Tinkerers printed only 2026 dates, so their yield is zero; the Eventbrite 2027 hits outside the six themes were dropped.',
     'evidence_refs': ['event-matrix.json', 'captures/cand-asiaai-eb.txt', 'captures/cand-icads-eb.txt']},
    {'kind': 'event-conflict',
     'text': 'Blockchain Festival 2027 is stored on the organiser Eventbrite page date (9 October 2027) while confslist.com prints 27 March 2027 for the same FINEXPO series; the conflict is recorded on the row and not resolved.',
     'evidence_refs': ['captures/cand-bcf-eb.txt']},
    {'kind': 'holidays',
     'text': 'Public layer is MOM 2027: eleven date rows plus the 8 February substitution day, stored with the MOM condition (a public holiday where the rest day falls on 7 February 2027) and the MOE footnote that treats it as a school public holiday. School layer is MOE 2027: four vacations, four scheduled school holidays and three designated days off-in-lieu for schools (9 February, 3 May and 27 December). 9 February and 3 May fall inside school terms; 27 December falls inside the end-of-year vacation and is stored as the separately printed designation, not counted as an extra vacation day. Pre-university end-of-year vacation starts 27 November 2027 and is recorded in coverage evidence, not as an overlapping second layer.',
     'evidence_refs': ['captures/mom-public-holidays.txt', 'captures/moe-school-terms-2027.txt', 'coverage:SG', 'holiday-supplement.json']},
    {'kind': 'venue-source',
     'text': 'The Genting Ballroom 1 record previously cited https://www.rwsentosa.com/en/meetings, which returned HTTP 404 on 2026-11-26. The address and capacity now cite the Marriott Four Points by Sheraton Singapore, Jurong event page for the same hotel at 2 Town Hall Link.',
     'evidence_refs': ['captures/op-genting-marriott.txt']},
    {'kind': 'capacity',
     'text': 'Several Tagvenue listings print a maximum capacity higher than the stored seated figure (for example ISCA 4-5 170 vs 100, Pico 150 vs 100, WeWork Suntec 100 vs 60). Capacities were not rewritten in this pass because the stored figures may be a specific layout; the difference is recorded rather than silently reconciled.',
     'evidence_refs': ['listing_parse.json', 'venue-report.json']},
    {'kind': 'legacy-claims',
     'text': '%d claim objects (%d venue, %d event) are present with neither a source_locator nor a capture: about, display_name, lifecycle, source_url, transit and the amenity/price-basis fields, together with the nested evidence, blocker and history records that copy them. That total is the round-1 count of 750 (598 venue + 152 event) plus %d pre-refresh blocker records deliberately preserved in venue history so their claim ids are not lost. They are listed here as lost citations rather than dressed with keyword matches: %d top-level venue field claims are annotated with legacy_note; the field breakdown is %s. The six facts this card re-sourced (address, coordinates, access window, programme windows, holiday rows, event rows) carry either a capture and a line locator or, for the nine venues with no published hire interval, an explicit locator_note instead of an invented line.'
             % (legacy_total, legacy_venue_total, legacy_event_total, preserved_blockers,
                legacy_field_total,
                ', '.join('%s %d' % (k, v) for k, v in sorted(legacy_fields.items()))),
     'evidence_refs': ['cite_check.py', 'city.json']},
    {'kind': 'card-conflict',
     'text': 'Acceptance criterion 4 names Lovdata and Utdanningsetaten as the public and school holiday authorities, which are Norwegian. The card body and the approved plan §4 name the Singapore Ministry of Manpower and Ministry of Education, and those are the authorities read here. The Norwegian names are treated as a copy-paste conflict, not as a source instruction.',
     'evidence_refs': ['captures/mom-public-holidays.txt', 'captures/moe-school-terms-2027.txt']},
    {'kind': 'card-conflict',
     'text': 'The handoff line asks for coordinate tiers for all 44 records, but the store and every other count in the card say 36 venues. All 36 existing records were assessed; no venue was added, so the reconciled total is 36.',
     'evidence_refs': ['venue-report.json', 'city.json']},
]

if dropped_sources:
    STORE['declared_gaps'].append({
        'kind': 'sources-replaced',
        'text': '%d URLs in the 2026-11-24 sources_consulted ledger are not carried as revision-1 ledger rows (for example the currency, weather, transit and licensing reference pages). The revision-1 ledger re-reads the event, holiday, geocode and venue lanes and records a check status and yield per row; %d of the dropped URLs still appear as source_url on a stored claim, and the rest are list-only references. The loss is of a ledger row, not of a cited fact.'
                 % (len(dropped_sources), len(cited_dropped)),
        'evidence_refs': ['city.pre-r8.json', 'city.json']})

for _gap in STORE['declared_gaps']:
    _gap['checked_on'] = CHECKED

STORE['runs'].append({
    'checked_on': CHECKED,
    'cities_registry': {
        'path': '/home/joe/repo_dev/hermes-skills/plan-event/references/cities.json',
        'sha256': STORE['city_registry'].get('sha256'),
    },
    'inputs': {
        'captures': {'path': str(BASE / 'captures'), 'files': len(list((BASE / 'captures').glob('*')))},
        'geocode': {'path': str(BASE / 'geocode-log-rev1.json')},
    },
    'kind': 'research',
    'registry': {
        'path': '/home/joe/repo_dev/hermes-skills/plan-event/references/school_holidays.json',
        'sha256': STORE['holiday_registry'].get('sha256'),
    },
    'run_id': RUN,
    'source_schema': 'city-run/1',
    'updated_at': '2026-11-26T12:30:00Z',
    'notes': 'Revision 1: addresses and coordinates re-derived, photos by room, MOM/MOE holiday layers, 54-cell event sweep, access re-derived from hire pages.',
})

out = BASE / 'city.json'
out.write_text(json.dumps(STORE, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('wrote', out, out.stat().st_size, 'bytes')
print('sources', len(S), 'events', len(STORE['events']), 'holidays', len(STORE['holidays']))
