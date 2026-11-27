"""Events: re-verify 11, add 4 confirmed 2027 Singapore occurrences."""
import hashlib

EVID_SOURCES = {
    'sg-ev-07845e88aaaa': ('re-2027-govware', '25 - 27 October 2027', 'GovWare 2027 | 25-27 Oct', 'https://www.govware.sg/'),
    'sg-ev-0a9e3abc85a8': ('re-2027-atxsg', '28 May 2027', 'Asia Tech x Singapore — 26-28 May 2027', 'https://asiatechxsg.com/'),
    'sg-ev-15ca8471fad2': ('re-2027-sibos', '20 - 23 September 2027', 'Sibos — future host cities', 'https://www.sibos.com/about/future-sibos'),
    'sg-ev-3319d59e5801': ('re-2027-token2049', '6-7 October 2027', 'TOKEN2049 | 6-7 October 2027 | Singapore', 'https://www.token2049.com/singapore'),
    'sg-ev-5d035781601c': ('re-2027-days', '5 October 2027', 'Digital Asset Yield Summit — Singapore | DAYS', 'https://daysevent.com/singapore-2027'),
    'sg-ev-7008209eed94': ('re-2027-superreturn', '27 - 30 September 2027', 'SuperReturn Asia — Informa Connect', 'https://informaconnect.com/superreturnasia/'),
    'sg-ev-753a37a6a034': ('re-2027-techweek', '13-14 October 2027', 'Tech Week Singapore | 13-14 October 2027', 'https://www.singaporetechnologyweek.com/'),
    'sg-ev-9450357bd291': ('re-2027-gitex', '29-30 April 2027', 'GITEX AI ASIA 2027 | 29-30 April | Singapore', 'https://gitexasia.com/'),
    'sg-ev-dcd2a2408b64': ('re-2027-sff', '10–12 November 2027', 'Singapore FinTech Festival 2027 — super early bird', 'https://www.fintechfestival.sg/sff2027-super-early-bird'),
    'sg-ev-f8db450a082e': ('re-2027-switch', '2 - 4 Nov 2027', 'SWITCH — Singapore Week of Innovation and Technology', 'https://www.switchsg.org/'),
    'sg-ev-fe69ef6a8926': ('re-2027-superai', '8-9 September 2027', 'SuperAI Global 2027 — London & Singapore AI Conferences', 'https://www.superai.com/singapore'),
}


def ev_claim(eid, field, value, *, title, url, capture, locator, quote, confidence='high'):
    return {
        'claim_id': claim_id('event', eid, field, url, str(locator)),
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


refreshed = 0
for eid, event in STORE['events'].items():
    if eid not in EVID_SOURCES:
        continue
    capture, needle, title, url = EVID_SOURCES[eid]
    line_no, line_text = find_line(capture + '.txt', needle)
    if not line_no:
        raise SystemExit('event line not found: %s %s' % (eid, needle))
    loc = 'line %d' % line_no
    for field in ('date_range', 'venue', 'status', 'kind', 'relevance', 'conflict_severity'):
        old = event['fields'].get(field)
        if not old:
            continue
        new = dict(old)
        new.update({'verified_at': TODAY, 'run_id': RUN, 'source_title': title,
                    'source_url': url, 'source_locator': loc, 'quote': line_text,
                    'capture': 'captures/' + capture + '.txt', 'checked_on': CHECKED})
        event.setdefault('history', {}).setdefault(field, []).append(old)
        event['fields'][field] = new
    event['evidence'].append({
        'claim_id': claim_id('evidence', eid, TODAY, line_text[:40]),
        'inference': '',
        'observed_facts': 'Organiser page re-fetched on 2026-11-26 still prints: %s' % line_text,
        'run_id': RUN,
        'source_title': title,
        'source_url': url,
        'verified_at': TODAY,
    })
    event['needs_human_verify'] = False
    refreshed += 1

NEW = [
    dict(name='Asia AI Conference 2027', start='2027-08-26', end='2027-08-26',
         venue='The Inspire Space, Singapore', kind='related', relevance='major_related',
         title='Asia AI Conference — Eventbrite organiser listing',
         url='https://www.eventbrite.com/e/asia-ai-conference-tickets-2003592234308',
         capture='cand-asiaai-eb', needle='Thursday, August 26, 2027',
         venue_line='The Inspire Space Singapore', theme='AI'),
    dict(name='3rd International Conference on AI and Data Science 2027', start='2027-04-08', end='2027-04-10',
         venue='Crowne Plaza Changi Airport by IHG, Singapore', kind='related', relevance='major_related',
         title='3rd International Conference on AI and Data Science — Eventbrite organiser listing',
         url='https://www.eventbrite.com/e/3rd-international-conference-on-ai-and-data-science-tickets-1986995020595',
         capture='cand-icads-eb', needle='Thursday, April 8-Saturday, April 10, 2027',
         venue_line='Crowne Plaza Changi Airport by IHG Singapore', theme='AI / data science'),
    dict(name='WikiEXPO Singapore 2027', start='2027-03-16', end='2027-03-16',
         venue='Sands Expo and Convention Centre, Marina Bay Sands', kind='related', relevance='major_related',
         title='Wiki Finance EXPO SINGAPORE 2027', url='https://www.wikiexpo.com/Singapore/2027/en/',
         capture='cand-wikiexpo', needle='MAR 16, 2027',
         venue_line='Sands Expo and Convention Centre, MBS, Singapore', theme='crypto / Web3'),
    dict(name='Blockchain Festival 2027 Singapore', start='2027-10-09', end='2027-10-09',
         venue='Sands Expo & Convention Centre, Singapore', kind='related', relevance='major_related',
         title='Blockchain Festival 2027 Singapore — Eventbrite organiser listing',
         url='https://www.eventbrite.com/e/blockchain-festival-2027-singapore-event-free-expo-conference-tickets-867282564497',
         capture='cand-bcf-eb', needle='Saturday, October 9, 2027',
         venue_line='Sands Expo & Convention Centre Singapore', theme='blockchain'),
]

added = 0
for item in NEW:
    eid = 'sg-ev-' + hashlib.md5(('sg-event|' + item['name']).encode()).hexdigest()[:12]
    line_no, line_text = find_line(item['capture'] + '.txt', item['needle'])
    if not line_no:
        raise SystemExit('new event line not found: ' + item['name'])
    v_no, v_text = find_line(item['capture'] + '.txt', item['venue_line'])
    loc = 'line %d' % line_no
    evidence = {
        'claim_id': claim_id('new-evidence', eid, line_text[:40]),
        'inference': '',
        'observed_facts': 'Captured %s on 2026-11-26 prints: %s' % (item['title'], line_text),
        'run_id': RUN,
        'source_title': item['title'],
        'source_url': item['url'],
        'verified_at': TODAY,
    }
    fields = {}
    for field, value, quote, locator in (
            ('date_range', {'start': item['start'], 'end': item['end']}, line_text, loc),
            ('venue', item['venue'], v_text or item['venue'], 'line %d' % v_no if v_no else loc),
            ('status', 'confirmed', line_text, loc),
            ('kind', item['kind'], line_text, loc),
            ('relevance', item['relevance'], line_text, loc),
            ('conflict_severity', 'medium' if item['name'].startswith('Blockchain Festival') else 'low', line_text, loc)):
        fields[field] = ev_claim(eid, field, value, title=item['title'], url=item['url'],
                                 capture='captures/' + item['capture'] + '.txt',
                                 locator=locator, quote=quote)
    conflict_note = None
    if item['name'].startswith('Blockchain Festival'):
        conflict_note = ('The Eventbrite organiser page prints Saturday 9 October 2027; '
                         'confslist.com prints Saturday 27 March 2027 for the same FINEXPO series. '
                         'The organiser listing is stored and the conflict is recorded, not resolved.')
        fields['conflict_severity']['value'] = 'medium'
        fields['conflict_severity']['conditions'] = conflict_note
    STORE['events'][eid] = {
        'city_slug': 'singapore-sg',
        'event_id': eid,
        'evidence': [evidence],
        'fields': fields,
        'history': {},
        'name': item['name'],
        'names_seen': [item['name']],
        'needs_human_verify': bool(conflict_note),
        'verification_questions': ([conflict_note] if conflict_note else []),
        'theme': item['theme'],
    }
    added += 1

print('events refreshed', refreshed, 'added', added, 'total', len(STORE['events']))
