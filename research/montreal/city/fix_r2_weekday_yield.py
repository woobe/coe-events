import json, datetime
from pathlib import Path
BASE = Path.home() / 'repo_dev/coe-events/research/montreal/city'
p = BASE / 'city.json'
S = json.loads(p.read_text(encoding='utf-8'))

# --- 1. explicit weekday on every holiday row (rule 15), recomputed in code ---
for h in S['holidays']:
    d = datetime.date.fromisoformat(h['start_date'])
    e = datetime.date.fromisoformat(h['end_date'])
    h['weekday'] = d.strftime('%A')
    h['weekday_source'] = 'computed from start_date/end_date in code'
    if e != d:
        h['end_weekday'] = e.strftime('%A')
    for cand in h.get('candidate_dates') or []:
        cd = datetime.date.fromisoformat(cand)
        h.setdefault('candidate_weekdays', {})[cand] = cd.strftime('%A')

# --- 2. structured event yield per source row (rule 12) ---
CREDIT = {
    'https://miragather.com/': ['mtl-ev-fbf3a925b2e0'],
    'https://www.startupfest.com/': ['mtl-ev-00c7888ab163'],
    'https://dc-finance.com/': ['mtl-ev-79cca7bc8e03'],
}
LINKONLY = {
    'https://miragather.com/?tab=side': ['mtl-ev-fbf3a925b2e0'],
    'https://miragather.com/ai': ['mtl-ev-fbf3a925b2e0'],
    'https://www.scaleai.ca/events/': ['mtl-ev-fbf3a925b2e0'],
}
for row in S['sources_consulted']:
    u = row.get('url')
    ids = CREDIT.get(u)
    if ids:
        row['yield_count'] = len(ids)
        row['retained_event_ids'] = ids
    else:
        row['yield_count'] = 0
        if u in LINKONLY:
            row['preserved_event_links'] = LINKONLY[u]
            row['note'] = (row.get('note') or '') + ' Duplicate lane: the occurrence is credited to its primary capture, link preserved here.'

total = sum(r['yield_count'] for r in S['sources_consulted'])
assert total == len(S['events']), (total, len(S['events']))

# --- 3. the missing substitute/observed-date gap ---
S['declared_gaps'].append({
    'kind': 'holidays',
    'checked_on': '2026-11-26',
    'evidence_refs': ['holidays[CA-QC:2027-12-25]', 'captures/legis-n-1-1.txt',
                      'sources_consulted[CNESST]'],
    'text': ("Noel 2027 falls on a Saturday. Article 60 of the Loi sur les normes du travail "
             "prints the seven statutory days and no substitute date for a holiday landing on a "
             "non-working day, so none is stored. The compensatory-day practice CNESST would "
             "confirm could not be read: cnesst.gouv.qc.ca returned a Cloudflare challenge "
             "(HTTP 403, also via r.jina.ai) on 2026-11-26. Treat the 25 December row as the "
             "statutory date only, not a settled observed closure."),
})

p.write_text(json.dumps(S, indent=1, ensure_ascii=False), encoding='utf-8')
print('written', p, p.stat().st_size)
print('holiday rows with weekday', sum('weekday' in h for h in S['holidays']), 'of', len(S['holidays']))
print('yield total', total, 'events', len(S['events']))
print('gaps', len(S['declared_gaps']))
