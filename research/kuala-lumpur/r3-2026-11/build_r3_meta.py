#!/usr/bin/env python3
"""Revision-1 metadata for the Kuala Lumpur candidate: gaps, sources, coverage, registry."""
import hashlib
import json
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
R3 = BASE / 'r3-2026-11'
STORE = BASE / 'city' / 'city.json'
SUPP = BASE / 'city' / 'holiday-supplement.json'
RUN = 'run-20261126-kl-r3'
STAMP = '2026-11-26'
UPDATED = '2026-11-26T09:00:00Z'

store = json.loads(STORE.read_text())

# ------------------------------------------------------------------ registry
public = [h for h in store['holidays'] if h['kind'] in ('public_holiday', 'municipal_holiday')]
school = [h for h in store['holidays'] if h['kind'] == 'school_holiday']
coverage = [c for c in store['coverage'] if str(c.get('kind', '')).endswith('coverage')]
supplement = {
    'schema_version': 'holiday-supplement/1',
    'city_slug': store['city_slug'],
    'checked_on': STAMP,
    'note': ('Malaysian federal and Federal Territory of Kuala Lumpur scope plus KPM Kumpulan B '
             'school rows, dated 2026-11-26; Islamic dates marked subject to official confirmation.'),
    'jurisdiction_ids': ['MY', 'MY-14'],
    'holidays': store['holidays'],
    'coverage': store['coverage'],
}
SUPP.write_text(json.dumps(supplement, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
digest = hashlib.sha256(SUPP.read_bytes()).hexdigest()
store['holiday_registry']['supplement'] = {
    'path': 'holiday-supplement.json',
    'sha256': digest,
    'holiday_rows': len(store['holidays']),
    'coverage_rows': len(store['coverage']),
    'jurisdiction_ids': ['MY', 'MY-14'],
    'note': supplement['note'],
}
store['holiday_registry']['holiday_rows'] = len(store['holidays'])
store['holiday_registry']['coverage_rows'] = len(store['coverage'])
store['holiday_registry']['jurisdiction_ids'] = ['MY', 'MY-14']
store['holiday_registry']['projection_year'] = 2027

# ------------------------------------------------------------------ coverage
def cov(jid, kind, start, end, edition, url, title, locator, facts):
    return {'jurisdiction_id': jid, 'kind': kind, 'start_date': start, 'end_date': end,
            'accessed_on': STAMP, 'needs_human_verify': True,
            'source_edition': edition, 'source_url': url, 'source_title': title,
            'source_locator': locator, 'evidence': {'observed_facts': facts},
            'verification_questions': []}


store['coverage'] = [
    cov('MY', 'public_holiday_coverage', '2027-01-01', '2027-12-31',
        'Jadual Hari Kelepasian Am Persekutuan dan Negeri 2027 (BKPP reproduction, read 2026-11-26)',
        'https://kalendar.ecentral.my/kalendar-2027',
        'Kalendar 2027 Malaysia - Senarai Cuti Umum & Cuti Am Negeri',
        'Introductory source note and the 2027 table',
        'The page states every 2027 date is taken from the Federal and State Public Holidays Schedule 2027 issued by the Cabinet, Constitution and Inter-Governmental Relations Division of the Prime Minister\u2019s Department. Thirteen federal dates were read.'),
    cov('MY-14', 'public_holiday_coverage', '2027-01-01', '2027-12-31',
        'Federal Territory of Kuala Lumpur column, 2027 (cross-checked)',
        'https://toolneko.com/en/tools/malaysia-calendar/2027/kuala-lumpur/',
        'Kuala Lumpur Public Holidays 2027 (Cuti Umum Kuala Lumpur)',
        'List of 18 public holidays and 3 expected replacement days, and the Holidays Act 1951 s.3 note',
        'Kuala Lumpur has 18 public holidays in 2027 and 3 replacement days expected by law: New Year, Thaipusam, Federal Territory Day and Nuzul Al-Quran in addition to the federal list; 8 February, 8 June and 16 August are the replacement days. The same list is given by malaysiakalendar.com and kalendar.ecentral.my.'),
    cov('MY-14', 'school_holiday_coverage', '2027-01-04', '2027-12-31',
        'Kalendar Akademik Tahun 2027, Kumpulan B (KPM Surat Siaran Bil. 1/2026)',
        'https://www.moe.gov.my/storage/files/shares/pekeliling_dan_garis_panduan/surat_siaran/SS%20KPM%20Bil.%201%20Tahun%202026%20-%20Kalendar%20Akademik%20Tahun%202027.pdf',
        'Surat Siaran KPM Bil. 1 Tahun 2026 - Kalendar Akademik Tahun 2027',
        'Lampiran B (Kumpulan B term table) and Lampiran C (festival additional days)',
        'Kumpulan B names Wilayah Persekutuan Kuala Lumpur. Four term breaks and ten KPM additional festival days intersect 2027; the PDF is image-only, so its text was read by OCR (7 pages) and the term table cross-checked against three independent reproductions.'),
]

# ------------------------------------------------------------------- sources
def row(lane, url, title, status, note, pages=1, venues=0, events=0, hits=0,
        dedupe=0, disposition=None, mandatory=False):
    return {'lane': lane, 'url': url, 'title': title, 'checked_on': STAMP,
            'accessed_on': STAMP, 'check_status': status, 'disposition': disposition or status,
            'note': note, 'pages_read': pages, 'venue_yield': venues, 'event_yield': events,
            'hits': hits, 'dedupe': dedupe, 'run_id': RUN, 'mandatory': mandatory}


updates = {
    'https://miragather.com/': row(
        'mandatory/miragather', 'https://miragather.com/', 'Mira - digital finance and frontier tech events',
        'checked_payload_read',
        'Re-read 2026-11-26: the page now serves its full 1,876,661-byte embedded payload (not the 47-byte shell seen on 2026-11-25). The payload names no Kuala Lumpur event; 1,866 of its date strings carry 2027 but none is tied to this city.',
        pages=1, mandatory=True),
    'https://miragather.com/?tab=side': row(
        'mandatory/miragather', 'https://miragather.com/?tab=side', 'Mira - side events',
        'checked_payload_read',
        'Re-read 2026-11-26: returns the same 1,876,661-byte payload as the main page and adds no Kuala Lumpur lead.', pages=1, mandatory=True),
    'https://miragather.com/ai': row(
        'mandatory/miragather', 'https://miragather.com/ai', 'Mira - AI events',
        'checked_payload_read',
        'Re-read 2026-11-26: 2,114,975-byte payload; the 2027 strings are Lisbon, Porto and other non-Malaysian AI events; no Kuala Lumpur entry.', pages=1, mandatory=True),
    'https://aitinkerers.org/all_cities': row(
        'mandatory/aitinkerers', 'https://aitinkerers.org/all_cities', 'AI Tinkerers - all cities',
        'blocked_403',
        'Re-read 2026-11-26 with the research user agent: HTTP 403. The 2026-11-25 read listed Kuala Lumpur at line 384 of the directory; today the chapter page below was read instead.',
        pages=1, mandatory=True),
    'https://lu.ma/kuala-lumpur': row(
        'event/luma-city', 'https://lu.ma/kuala-lumpur', 'Popular events in Kuala Lumpur',
        'checked_empty_2027',
        'Re-read 2026-11-26: 248,348 bytes, 150 Kuala Lumpur mentions, zero occurrences of "2027" anywhere in the page or its payload. Ten cards are visible and all are 2026-dated.',
        pages=1, mandatory=True),
}
for url, r in updates.items():
    pass

new_rows = [
    row('event/luma-alias', 'https://lu.ma/selangor', 'Luma - Selangor', 'checked_empty_2027',
        'Read 2026-11-26 for the Klang Valley alias: 42,693 bytes, no 2027 date and no Kuala Lumpur listing.', mandatory=True),
    row('event/luma-alias', 'https://lu.ma/malaysia', 'Luma - Malaysia', 'checked_empty_2027',
        'Read 2026-11-26: 248,723 bytes, no 2027 date in the payload.', mandatory=True),
    row('event/eventbrite', 'https://www.eventbrite.com/d/malaysia--kuala-lumpur/artificial-intelligence/',
        'Eventbrite - AI events in Kuala Lumpur', 'checked',
        'Read 2026-11-26: 465 lines, 12 lines carrying 2027. Two Kuala Lumpur 2027 events retained (GAICC 24 January, Business Growth AI 15 July); XR ASIA SUMMIT 2027 is in Petaling Jaya, Selangor and is excluded as adjacent.',
        events=2, hits=12, dedupe=1),
    row('event/aitinkerers-chapter', 'https://kuala-lumpur.aitinkerers.org/',
        'AI Tinkerers Kuala Lumpur', 'checked_empty_2027',
        'Read 2026-11-26: 646 lines of chapter content, five AI-themed dated past events, the latest in November 2026 and no 2027 edition.', mandatory=True),
    row('event/luma-organiser', 'https://luma.com/malaysianai', 'Malaysian AI calendar', 'checked_empty_2027',
        'Read 2026-11-26: 176 lines; event titles render without dates and no 2027 date appears.', mandatory=True),
    row('holiday/bkpp', 'https://www.kabinet.gov.my/storage/2026/08/HKA_2027.pdf',
        'BKPP - Jadual Hari Kelepasian Am Persekutuan dan Negeri 2027', 'blocked_unreachable',
        'Three attempts on 2026-11-26 (https with the storage path, http, and the bare host) timed out after 25-150 s with no bytes; kabinet.gov.my is unreachable from this host. The Federal Territory column therefore rests on reproductions, cross-checked against two other listings.'),
    row('holiday/crosscheck', 'https://toolneko.com/en/tools/malaysia-calendar/2027/kuala-lumpur/',
        'Kuala Lumpur Public Holidays 2027', 'checked',
        'Read 2026-11-26: 18 Kuala Lumpur public holidays and 3 replacement days, attributed to the BKPP lists and the Holidays Act 1951 s.3; this is the Federal Territory column used for the cross-check.'),
    row('holiday/crosscheck', 'https://malaysiakalendar.com/public-holidays-2027/',
        'Malaysia Public Holidays 2027 (Federal & State)', 'checked',
        'Read 2026-11-26: the Kuala Lumpur row lists 18 dates (New Year, Thaipusam, Federal Territory Day, Nuzul Al-Quran plus the federal list) and agrees with toolneko and kalendar.ecentral.my.'),
    row('holiday/kpm', 'https://www.moe.gov.my/storage/files/shares/pekeliling_dan_garis_panduan/surat_siaran/SS%20KPM%20Bil.%201%20Tahun%202026%20-%20Kalendar%20Akademik%20Tahun%202027.pdf',
        'Surat Siaran KPM Bil. 1 Tahun 2026 - Kalendar Akademik Tahun 2027', 'checked_ocr',
        'Downloaded 2026-11-26 (2,123,610 bytes, 7 pages, image-only: 111 extractable characters). OCR read the circular and Lampiram A-C; Lampiran B names Wilayah Persekutuan Kuala Lumpur under Kumpulan B, and Lampiran C lists the ten KPM additional festival days.',
        pages=7),
    row('geocode/nominatim', 'https://nominatim.openstreetmap.org/search',
        'OpenStreetMap Nominatim forward geocoding', 'checked',
        'One live search per query on 2026-11-26 for all 55 records, re-run for the 16 that already carried a point; 46 first-pass matches, 9 re-queried, 55 final tiers recorded in geocode/ and coordinate-tiers.json.',
        pages=1, venues=55, hits=90),
    row('photo/operator', 'https://mitec.com.my/organise/venues', 'MITEC - Venues', 'checked',
        'Read 2026-11-26: the level switcher serves per-level floor plans; three level plans verified and attached to the three level records.', venues=3, hits=5),
    row('photo/operator', 'https://www.klpac.org/venue-hire/', 'klpac - Venue Hire', 'checked',
        'Read 2026-11-26: the "Our Venues" group serves indicine-lights.jpg and Pentas-2-Seating-1024x1024.jpg; both verified and attached to the named rooms.', venues=2, hits=13),
    row('photo/operator', 'https://www.marriott.com/en-us/hotels/kulwh-w-kuala-lumpur/events/',
        'Events & Weddings | W Kuala Lumpur', 'checked',
        'Read 2026-11-26: the gallery captions one asset "Great Room" and one "Studio Room"; those two are attached, and the Studio Three asset is withheld because its caption sits under the Studio Room heading.', venues=2, hits=38),
    row('photo/operator', 'https://connexioncec.com/', 'Connexion Conference & Event Centre', 'checked',
        'Read 2026-11-26: the Grand Nexus Ballroom theatre-setting asset is named in the file and listed with the ballroom.', venues=1, hits=130),
    row('photo/operator', 'https://thehive.com/malaysia/bukit-kl/', 'Bukit KL - the Hive', 'checked',
        'Read 2026-11-26: the address block prints No.68 Kuala Lumpur-Seremban Expressway and the event-space section serves bukitkl-es.jpg.', venues=1, hits=18),
    row('photo/operator', 'https://www.publika.com.my/', 'Publika Shopping Gallery', 'checked',
        'Read 2026-11-26: the gallery interior asset is the only placeable image; the address block prints Solaris Dutamas.', venues=1, hits=5),
    row('photo/operator', 'https://commonground.work/malaysia/klcc', 'Common Ground KLCC', 'checked',
        'Read 2026-11-26: klcc-web-4.jpg is served under the event-space heading.', venues=1, hits=23),
    row('photo/operator', 'https://commonground.work/malaysia/bukit-bintang', 'Common Ground Bukit Bintang', 'checked',
        'Read 2026-11-26: bb_es-web-6 is served under the event-space heading.', venues=1, hits=23),
    row('photo/operator', 'https://wspace.com/membership/event-space/', 'WSPACE - Event Space', 'checked',
        'Read 2026-11-26: the Mid Valley event-space asset returns 404 at the URL the page serves, so no WSPACE photo is stored.', venues=0, hits=1),
    row('venue/legacy', 'https://www.timeout.com/kuala-lumpur/things-to-do/the-co', 'The Co. | Things to do in Bandaraya, Kuala Lumpur',
        'checked_secondary',
        'Read 2026-11-26 for the one address the live operator site no longer prints: a 2016 listing gives 50 Jalan Doraisamy, 50300 Kuala Lumpur. Used only for a street-tier pin on the lead whose own domain now serves a lottery page.'),
]

by_url = {}
for item in store['sources_consulted']:
    by_url.setdefault(item.get('url'), item)
for url, r in updates.items():
    if url in by_url:
        by_url[url].update(r)
    else:
        store['sources_consulted'].append(r)
for r in new_rows:
    if r['url'] in by_url:
        by_url[r['url']].update(r)
    else:
        store['sources_consulted'].append(r)
        by_url[r['url']] = r

# yields must sum to the stored event count
manual = {
    'https://www.eventbrite.com/d/malaysia--kuala-lumpur/artificial-intelligence/': 2,
}
# the two new events are also attested by their own ticket pages
for url, title, eid in (
        ('https://www.eventbrite.com/e/gaicc-ai-governance-conference-malaysia-2027-governing-the-ai-future-tickets-2003959315257',
         'GAICC AI Governance Conference Malaysia 2027', 'kl-ev-0f2a91c4d7b3'),
        ('https://www.eventbrite.com/e/business-growth-ai-digital-transformation-summit-2027-tickets-2003654016099',
         'Business Growth, AI & Digital Transformation Summit 2027', 'kl-ev-7c41b0e2a9d5')):
    store['sources_consulted'].append(row('event/organiser', url, title, 'checked',
                                              'Organiser ticket page read 2026-11-26; it prints the 2027 date, the time block and the venue block for %s.' % eid,
                                              events=0))

# one credited yield per unique dated occurrence: the Digital Transformation Summit is
# credited on its own page, so the Exito calendar row credits only BFSI and Cyber Security.
for item in store['sources_consulted']:
    if str(item.get('url', '')).startswith('https://itvoice.in/exito-media-concepts'):
        item['event_yield'] = 2
        item['note'] = ('Gives 14 April, 15 April and 22 September 2027 Kuala Lumpur dates; the 14 April '
                        'Digital Transformation Summit is credited on its own page, so this row credits '
                        'BFSI (15 April) and Cyber Security (22 September).')
        item['dedupe'] = 1

total = sum(int(s.get('event_yield') or 0) for s in store['sources_consulted'])
print('event yield total', total, 'stored events', len(store['events']))

# ---------------------------------------------------------------- gaps
def gap(kind, text, refs):
    return {'kind': kind, 'checked_on': STAMP, 'text': text, 'evidence_refs': refs}


# The photos gap is generated from the store itself, so the page can never
# contradict the counts it is describing.
pre = json.loads((BASE / 'city' / 'city.pre-r3.json').read_text())
ROOM_KINDS = ('interior', 'layout', 'floor_plan', 'past_event')


def live_rows(snapshot, vid):
    return [p for p in snapshot['photos'].get(vid, [])
            if str(p.get('url') or '').startswith(('http://', 'https://'))
            and not p.get('withheld') and p.get('hotlink_ok', True)]


def venues_with_live(snapshot):
    return [vid for vid in snapshot['venues'] if live_rows(snapshot, vid)]


def venues_with_room(snapshot):
    return [vid for vid in snapshot['venues']
            if any(p.get('view_kind') in ROOM_KINDS for p in live_rows(snapshot, vid))]


live_now, room_now, live_pre = venues_with_live(store), venues_with_room(store), venues_with_live(pre)
none_now = len(store['venues']) - len(live_now)
fallback_now = len(live_now) - len(room_now)
no_room_now = len(store['venues']) - len(room_now)
gained = len(set(live_now) - set(live_pre))
op_rows = [p for vid in store['venues'] for p in live_rows(store, vid)
           if 'wikimedia' not in str(p.get('rights_basis') or '')]
op_venues = len({vid for vid in store['venues'] for p in live_rows(store, vid)
                 if 'wikimedia' not in str(p.get('rights_basis') or '')})
assert no_room_now == none_now + fallback_now, (no_room_now, none_now, fallback_now)
assert len(op_rows) == 12 and op_venues == 12, (len(op_rows), op_venues)
print('photos gap counts', {'no_room': no_room_now, 'none': none_now,
                            'fallback': fallback_now, 'gained': gained,
                            'operator_rows': len(op_rows), 'operator_venues': op_venues})


store['declared_gaps'] = [
    gap('coordinates',
        'Three records carry an area pin only: Colony Event Lounge at KL Eco City and Common Ground KL Eco City sit in the KL Eco City development (no OSM point exists for Menara 2), and WSPACE Event Space 50 sits in Mid Valley City because Centrepoint North has no OSM point.',
        ['coordinate-tiers.json', 'geocode/kl-b375b5ac812b.json', 'geocode/kl-bba8243f4e1d.json', 'geocode/kl-7d5505fb90ae.json']),
    gap('coordinates',
        'Three records carry a street pin only: The Hive Bukit KL (only the expressway resolves; the operator prints No.68 at Taman Bukit), The Co. (its site now serves an unrelated lottery page, so the street comes from a 2016 listing at The Row, Jalan Doraisamy), and Common Ground Ampang (only Jalan Kolam Air Lama resolves; the site is in Selangor).',
        ['geocode/kl-7dd2a97334c6.json', 'geocode/kl-ef79384c8cb6.json', 'geocode/kl-79df5ab85172.json']),
    gap('coordinates',
        'No record reaches exact_venue with a proven room entrance: the operator pages that print addresses print building or level, never a door, and no venue was visited. Three venue-level POIs (APW Bangsar, MATRADE MECC, Sunway Pyramid Convention Centre) are labelled exact_venue because the geocoder returns the venue itself, not a room.',
        ['coordinate-tiers.json', 'geocode/kl-8cd52f2406dc.json', 'geocode/kl-0c62e94089f8.json']),
    gap('photos',
        '{no_room} of {total} records carry no room-kind view: {none} have no cleared '
        'photograph at all and {fallback} carry only a labelled exterior or lobby fallback. '
        '{gained} records gained a first photograph in this refresh, and the {op_rows} '
        'operator assets behind them are hotlinked with attribution because their pages '
        'publish no separate licence text. Every withheld record names the pages checked; '
        'no stock, look-alike or unlicensed image is used.'.format(
            no_room=no_room_now, total=len(store['venues']), none=none_now,
            fallback=fallback_now, gained=gained, op_rows=len(op_rows)),
        ['photos', 'photo-records.json', 'city.pre-r3.json']),
    gap('photos',
        'The WSPACE Mid Valley asset the operator serves for its event space is named Level 8 while the contact page prints Level 27 Penthouse; the floor conflict is recorded and no WSPACE photo is stored.',
        ['photo-probe.json']),
    gap('holidays',
        'The BKPP primary schedule PDF (kabinet.gov.my/storage/2026/08/HKA_2027.pdf) was unreachable from this host on 2026-11-26: https, http and the bare host all timed out. The Federal Territory of Kuala Lumpur column therefore rests on three independent reproductions (kalendar.ecentral.my, toolneko, malaysiakalendar) and the 21 stored public rows keep their subject-to-announcement caveat for the eight Islamic dates.',
        ['sources_consulted:https://www.kabinet.gov.my/storage/2026/08/HKA_2027.pdf']),
    gap('holidays',
        'The KPM Kalendar Akademik Tahun 2027 PDF is image-only (111 extractable characters over 7 pages), so Lampiran B and C were read by OCR; the Kumpulan B term table was cross-checked against three independent reproductions of the same circular. Ten single-day KPM festival holidays are stored with the school breaks.',
        ['pdf/KPM_ocr.txt', 'sources_consulted:https://www.moe.gov.my/storage/files/shares/pekeliling_dan_garis_panduan/surat_siaran/SS%20KPM%20Bil.%201%20Tahun%202026%20-%20Kalendar%20Akademik%20Tahun%202027.pdf']),
    gap('events',
        'The six-theme matrix ran 66 cells over 11 lanes: Luma\u2019s Kuala Lumpur city page prints 150 Kuala Lumpur mentions and no 2027 date, both alias pages and the Malaysia page carry no 2027 date, the MiraGather payloads name no Kuala Lumpur event, AI Tinkerers\u2019 all-cities page returns 403 and its Kuala Lumpur chapter ends in November 2026, and Meetup returns November-December 2026 editions. Two 2027 Kuala Lumpur events were added from Eventbrite and one Selangor 2027 event was excluded.',
        ['event-matrix.json', 'sources_consulted:https://lu.ma/kuala-lumpur']),
    gap('access',
        'One room (WORQ) publishes a bookable day, 8 am to 10 pm, that contains 09:00-21:00; the other 54 records are unknown because their operator pages print no event interval. The clock lines that do exist are office or mall hours (WTC 9.00 am-6.00 pm Mon-Fri, WSPACE 9:00am-6:00pm weekdays, Publika 10:00am-10:00pm) and are recorded as such, not as hire windows.',
        ['venues.kl-e67bf1a8718b.fields.programme_windows', 'venues.kl-1501b357e078.fields.programme_windows']),
    gap('geocode',
        'One provider was used: OpenStreetMap Nominatim. No second geocoder or national address register was queried, and every matched point is derived rather than surveyed.',
        ['geocode-summary.json']),
    gap('verification',
        'No venue was contacted and no site visit was made; the visits list stays empty and every open question remains a question rather than a confirmed term.',
        ['visits']),
]

store['refresh_revision'] = 1
store['updated_at'] = UPDATED
store['runs'] = list(store['runs']) + [{
    'run_id': RUN, 'kind': 'refresh', 'checked_on': STAMP, 'updated_at': UPDATED,
    'note': ('Revision-1 refresh: 55 addresses re-verified and geocoded afresh, 12 operator '
             'assets verified across 12 records, KPM Kumpulan B school layer added, two 2027 '
             'events added, and programme windows re-stated for every record.'),
    'evidence': {
        'coordinate_tiers': 'research/kuala-lumpur/r3-2026-11/coordinate-tiers.json',
        'geocode_dir': 'research/kuala-lumpur/r3-2026-11/geocode/',
        'photo_records': 'research/kuala-lumpur/r3-2026-11/photo-records.json',
        'event_matrix': 'research/kuala-lumpur/r3-2026-11/event-matrix.json',
        'captures': 'research/kuala-lumpur/r3-2026-11/capture-manifest.json',
    },
}]

STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('wrote', STORE, len(STORE.read_bytes()), 'supplement', digest)
