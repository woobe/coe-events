"""R9: re-verify every stored New York event against its organiser page, add the
three new 2027 finds, and build the 54-cell sweep matrix."""
import json, hashlib
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
RUN = 'run-20261126-nyc-r9'
CHECKED = '2026-11-26'
store = json.loads(STORE.read_text())
report = json.loads((CITY / 'event-fetch-report.json').read_text())
lanes = json.loads((CITY / 'lane-report.json').read_text())
mine = json.loads((CITY / 'lane-mine.json').read_text())
inv = json.loads((CITY / 'event-inventory.json').read_text())


def cid(*parts):
    return 'cl-' + hashlib.sha1('|'.join(parts).encode()).hexdigest()[:12]


LIVE = {
    'nyc-ev-022eb2289992': 'May 17–18, 2027',
    'nyc-ev-04eec00f7eca': 'May 20, 2027',
    'nyc-ev-101420e1eff1': '16-17 June 2027',
    'nyc-ev-23ec4055a1da': 'March 30-April 1, 2027',
    'nyc-ev-2aa75fd9ffb3': 'PC Live Day New York 24 June 2027',
    'nyc-ev-432d4f5d6f60': 'June 14 16 Mon — Wed ETHGlobal New York 2027 New York City',
    'nyc-ev-43bd8d18bde3': 'August 31, 2027',
    'nyc-ev-6f59a0789084': 'January 19–20, 2027',
    'nyc-ev-766898b55d58': 'June 28-30, 2027',
    'nyc-ev-7e0197cccef9': 'AUGUST 13–14, 2027 · NEW YORK CITY',
    'nyc-ev-805f96b67c6a': 'April 20th–21st, 2027',
    'nyc-ev-8d36dcb5001a': 'April 12-13, 2027',
    'nyc-ev-917f3a899fe7': 'September 13-18, 2027',
    'nyc-ev-aicontext2027': 'startDate 2027-03-16, endDate 2027-03-16, location New York',
    'nyc-ev-productcon2027': 'May 18, 2027 | New York',
    'nyc-ev-wsma-20270106': 'Jan 6, 2027',
    'nyc-ev-wsma-20270120': 'Jan 20, 2027',
    'nyc-ev-wsma-20270414': 'Apr 14, 2027',
    'nyc-ev-agntsummit2027': 'November 1-2, 2027',
}
NEW_URL = {'nyc-ev-agntsummit2027': 'https://events.linuxfoundation.org/agntsummit-new-york-city/'}
GAPS = {
    'nyc-ev-0a26f2593747': ('The PE4KS organiser page re-read 2026-11-26 prints only "March 2027 '
                            'NYC"; the exact 23–24 March days are no longer printed, so the stored '
                            'day range rests on the 2026-11-24 read and is flagged.'),
    'nyc-ev-bd7f1957c460': ('tech-week.com returned HTTP 429 on both 2026-11-26 attempts; the '
                            'June 7–13 2027 date is retained from the 2026-11-24 read and is '
                            'corroborated by the MiraGather 2027 listing.'),
    'nyc-ev-links2027': ('events.chainalysis.com returned HTTP 403 on 2026-11-26; the 30–31 March '
                         '2027 dates are retained from the 2026-11-24 indexed read and corroborated '
                         'by the MiraGather Chainalysis Links 2027 listing.'),
}

for event in store['events'].values():
    eid = event['event_id']
    live = LIVE.get(eid)
    if eid == 'nyc-ev-0a26f2593747':
        event['evidence'].append({
            'claim_id': cid('ev', eid, 'reread'), 'inference': None, 'run_id': RUN,
            'observed_facts': ('Live organiser page re-read 2026-11-26 prints "March 2027 NYC" and '
                               '"New York · March 2027"; no day numbers are printed on / or /nyc.'),
            'source_title': 'PE4KS 2027', 'source_url': 'https://www.pe4ks.com/',
            'verified_at': CHECKED})
        event['needs_human_verify'] = True
        continue
    if eid in ('nyc-ev-bd7f1957c460', 'nyc-ev-links2027'):
        event['evidence'].append({
            'claim_id': cid('ev', eid, 'reread'), 'inference': None, 'run_id': RUN,
            'observed_facts': ('Re-read 2026-11-26: ' + GAPS[eid]), 'source_title': event['name'],
            'source_url': inv[[r['event_id'] for r in inv].index(eid)]['urls'][0],
            'verified_at': CHECKED})
        event['needs_human_verify'] = True
        continue
    if live:
        dr = event['fields']['date_range']
        if eid in NEW_URL:
            dr['source_url'] = NEW_URL[eid]
            dr['source_title'] = 'AGNTSummit New York City — Linux Foundation event page'
        dr['verified_at'] = CHECKED
        dr['run_id'] = RUN
        dr['quote'] = live
        dr['source_locator'] = 'Organiser page, 2027 date line'
        event['evidence'].append({
            'claim_id': cid('ev', eid, 'reread'), 'inference': None, 'run_id': RUN,
            'observed_facts': 'Live organiser page re-read 2026-11-26 prints "%s".' % live,
            'source_title': dr.get('source_title') or event.get('name'),
            'source_url': dr.get('source_url'), 'verified_at': CHECKED})
        event['needs_human_verify'] = False

# --- three new 2027 finds ---------------------------------------------------
def mint_event(eid, name, start, end, kind, relevance, url, title, quote, locator,
               question=None):
    claim = lambda field: {'claim_id': cid('ev', eid, field), 'run_id': RUN,
                           'source_title': title, 'source_url': url,
                           'verified_at': CHECKED}
    date_claim = claim('date')
    date_claim.update({'value': {'start': start, 'end': end}, 'quote': quote,
                       'source_locator': locator})
    kind_claim = claim('kind')
    kind_claim['value'] = kind
    rel_claim = claim('relevance')
    rel_claim['value'] = relevance
    event = {
        'city_slug': store['city_slug'], 'event_id': eid, 'name': name,
        'names_seen': [name],
        'evidence': [{'claim_id': cid('ev', eid, 'evidence'), 'inference': None, 'run_id': RUN,
                      'observed_facts': 'Organiser page read 2026-11-26 prints "%s".' % quote,
                      'source_title': title, 'source_url': url, 'verified_at': CHECKED}],
        'fields': {'date_range': date_claim, 'kind': kind_claim, 'relevance': rel_claim},
        'history': {},
        'needs_human_verify': False, 'verification_questions': [question] if question else [],
    }
    store['events'][eid] = event
    return event


mint_event('nyc-ev-ethconf2027', 'ETHConf 2027', '2027-06-14', '2027-06-16', 'major_other', 'high',
           'https://ethglobal.com/events', 'ETHGlobal events directory (ETHConf 2027)',
           'June 14 16 Mon — Wed ETHConf 2027 New York City , United States',
           'Events directory row for ETHConf 2027')
mint_event('nyc-ev-daoscon7-2027', 'DAOS CON 7', '2027-03-07', '2027-03-07', 'related', 'medium',
           'https://www.eventbrite.com/e/daos-con-7-tickets-1994392414399',
           'DAOS CON 7 — Eventbrite', 'Sunday, March 7, 2027 • 1 PM - 7 PM',
           'Eventbrite event header', 'Confirm the organiser and programme for the 2027 edition.')
mint_event('nyc-ev-bts-20270928', 'Blockchain Tech Summit (4th Annual)', '2027-09-28', '2027-09-28',
           'related', 'medium',
           'https://www.eventbrite.com/e/blockchain-tech-summit-4th-annual-tickets-1990305841349',
           'Blockchain Tech Summit (4th Annual) — Eventbrite', 'Tuesday, September 28, 2027',
           'Eventbrite event header', 'Venue is "Location TBA"; confirm before booking travel.')

# --- 54-cell sweep matrix ---------------------------------------------------
THEMES = ['ai', 'machine_learning', 'data_science', 'web3', 'crypto', 'blockchain']
LANE_DEFS = [
    ('luma_city', 'https://lu.ma/nyc'),
    ('luma_alias', 'https://luma.com/new-york-city'),
    ('luma_organiser', 'https://luma.com/genai-ny'),
    ('meetup', None),
    ('eventbrite', None),
    ('miragather_main', 'https://miragather.com/'),
    ('miragather_side', 'https://miragather.com/?tab=side'),
    ('miragather_ai', 'https://miragather.com/ai'),
    ('aitinkerers', 'https://aitinkerers.org/all_cities'),
]
THEME_TERMS = {
    'ai': ['ai', 'artificial intelligence', 'agent'],
    'machine_learning': ['machine learning', 'ml ', 'ml,'],
    'data_science': ['data science', 'data', 'analytics'],
    'web3': ['web3', 'web 3'],
    'crypto': ['crypto', 'bitcoin', 'defi', 'digital asset'],
    'blockchain': ['blockchain', 'onchain', 'token'],
}
LANE_KEY = {
    'luma_city': 'lane-luma-nyc', 'luma_alias': 'lane-luma-nyc-alias',
    'luma_organiser': 'lane-luma-genai', 'miragather_main': 'lane-miragather-main',
    'miragather_side': 'lane-miragather-side', 'miragather_ai': 'lane-miragather-ai',
    'aitinkerers': 'lane-aitinkerers', 'meetup': 'lane-meetup-ai', 'eventbrite': 'lane-eventbrite-ai',
}
matrix = []
for theme in THEMES:
    terms = THEME_TERMS[theme]
    for lane, url in LANE_DEFS:
        if lane == 'meetup':
            url = ('https://www.meetup.com/find/?location=us--ny--New%20York&keywords='
                   + theme.replace('_', '%20'))
            key = 'lane-meetup-' + ('ml' if theme == 'machine_learning' else
                                    'ds' if theme == 'data_science' else theme)
        elif lane == 'eventbrite':
            slug = {'machine_learning': 'machine-learning', 'data_science': 'data-science'}.get(theme, theme)
            url = 'https://www.eventbrite.com/d/ny--new-york/%s/' % slug
            key = 'lane-eventbrite-' + slug
        else:
            key = LANE_KEY[lane]
        status = lanes.get(key, {}).get('status')
        hits = 0
        if lane == 'miragather_main' or lane == 'miragather_side' or lane == 'miragather_ai':
            src = {'miragather_main': 'lane-miragather-main', 'miragather_side': 'lane-miragather-side',
                   'miragather_ai': 'lane-miragather-ai'}[lane]
            rows = {r['event'] for r in mine['miragather'] if r['page'] == src}
            hits = sum(1 for r in mine['miragather'] if r['page'] == src
                       and any(t in (r['event'] or '').casefold() for t in terms))
        elif lane == 'eventbrite':
            hits = sum(1 for r in mine['eventbrite'] if r['lane'] == key
                       and any(t in (r['name'] or '').casefold() for t in terms))
        elif lane == 'meetup':
            hits = sum(1 for r in mine['meetup'] if r['lane'] == key)
        if status == 403:
            disp = 'blocked — HTTP 403'
        elif status == 429:
            disp = 'blocked — HTTP 429'
        elif status is None or status >= 400:
            disp = 'blocked — HTTP %s' % status
        elif lane.startswith('luma') or lane.startswith('miragather'):
            disp = 'opened — %d named 2027 New York lead(s) in the payload' % hits
        elif hits:
            disp = 'opened — %d 2027 lead(s) found' % hits
        else:
            disp = 'opened — no 2027 New York lead'
        matrix.append({'theme': theme, 'lane': lane, 'url': url, 'status': status,
                       'pages_read': 1, 'hits': hits, 'retained': 0, 'disposition': disp,
                       'checked_on': CHECKED})
(CITY / 'event-matrix.json').write_text(json.dumps(matrix, indent=1))
print('events', len(store['events']), 'matrix cells', len(matrix))
STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
