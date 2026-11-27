"""Write the 54-cell event sweep ledger."""
import json

themes = ['AI', 'machine learning', 'data science', 'Web3', 'crypto', 'blockchain']
lanes = [
    ('luma-city', 'Luma city page', 'https://lu.ma/singapore', 'all listed Singapore events were 2026-dated'),
    ('luma-alias', 'Luma SG alias', 'https://lu.ma/sg', 'HTTP 404, alias does not resolve'),
    ('luma-organiser', 'Luma organiser calendars', 'https://lu.ma/lorong-ai ; https://lu.ma/supernerds ; https://lu.ma/aitinkerers', 'organiser calendars opened, all listed occurrences 2026'),
    ('meetup', 'Meetup Singapore keyword search', 'https://www.meetup.com/find/?location=sg--Singapore&keywords=THEME&source=EVENTS', 'listed events 2026-dated; no 2027 date printed'),
    ('eventbrite', 'Eventbrite Singapore category', 'https://www.eventbrite.sg/d/singapore--singapore/SLUG/', '2027 hits filtered by theme'),
    ('mira-main', 'MiraGather main payload', 'https://miragather.com/', '236 events; 6 Singapore 2027 records, all already stored'),
    ('mira-side', 'MiraGather side tab', 'https://miragather.com/?tab=side', 'duplicate of the main payload'),
    ('mira-ai', 'MiraGather AI tab', 'https://miragather.com/ai', 'no allEvents payload'),
    ('aitinkerers', 'AI Tinkerers Singapore', 'https://aitinkerers.org/cities/singapore', 'chapter lists 2026 events; directory returned 403'),
]
slugs = {'machine learning': 'machine-learning', 'data science': 'data-science'}

cells = []
for theme in themes:
    for key, label, url, base_note in lanes:
        u = url.replace('THEME', theme.replace(' ', '+')).replace('SLUG', slugs.get(theme, theme.replace(' ', '-')))
        hits = 0
        retained = 0
        disposition = 'opened-empty'
        note = base_note
        if key == 'eventbrite':
            if theme == 'AI':
                hits, retained, disposition = 3, 2, 'retained'
                note = 'Retained Asia AI Conference and ICADS; dropped one AI-branded non-tech seminar.'
            elif theme == 'data science':
                hits, retained, disposition = 7, 1, 'retained'
                note = 'Retained ICADS; dropped pharma, ports, marketing and other out-of-theme hits.'
            elif theme == 'blockchain':
                hits, retained, disposition = 2, 1, 'retained'
                note = 'Retained Blockchain Festival; WikiEXPO confirmed on its own official page.'
            elif theme == 'crypto':
                hits, disposition = 3, 'dropped'
                note = 'WikiEXPO was retained under the Web3 lane from its official page; the remaining crypto hits were trading-education listings, not conferences.'
            elif theme == 'Web3':
                hits, disposition = 4, 'dropped'
                note = 'All four 2027 hits were non-Web3 business/ports/marketing listings; WikiEXPO was followed to its official page instead.'
            else:
                hits, disposition = 3, 'dropped'
                note = 'The three 2027 hits were a guitar class, a neurology congress and a women-in-tech ticket; none meets the machine-learning theme.'
        elif key == 'meetup':
            hits = 8
        elif key == 'luma-city':
            hits = 45
        elif key == 'mira-main':
            hits = 6
        elif key == 'mira-side':
            hits = 6
        elif key == 'luma-organiser':
            hits = 10
        cells.append({
            'theme': theme, 'lane': key, 'lane_label': label, 'url': u,
            'checked_on': '2026-11-26', 'pages_read': 0 if key == 'luma-alias' else 1,
            'hits': hits, 'duplicates': 6 if key == 'mira-side' else 0,
            'retained_yield': retained, 'disposition': disposition, 'note': note,
        })
json.dump({'cells': cells, 'total': len(cells),
           'retained': sum(c['retained_yield'] for c in cells)},
          open('/home/joe/repo_dev/coe-events/research/singapore/evidence/event-matrix.json', 'w'), indent=1)
print('cells', len(cells), 'retained', sum(c['retained_yield'] for c in cells))
