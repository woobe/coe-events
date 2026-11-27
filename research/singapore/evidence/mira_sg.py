import json, re, sys
from pathlib import Path

def next_data(path):
    html = Path(path).read_text(encoding='utf-8', errors='replace')
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return None
    return json.loads(m.group(1))

for f in ['ev-mira-main.html', 'ev-mira-side.html', 'ev-mira-ai.html']:
    p = 'research/singapore/city/captures/' + f
    d = next_data(p)
    if not d:
        print(f, 'no next data'); continue
    evs = d['props']['pageProps'].get('allEvents') or []
    print('===', f, 'allEvents', len(evs))
    for e in evs:
        city = str(e.get('city') or '')
        country = str(e.get('country') or '')
        sd = str(e.get('startDate') or '')
        name = e.get('event') or ''
        if 'singapore' in (city + country).lower():
            print(' ', sd[:19], '|', name, '|', city, '|', e.get('link'), '|', e.get('organizer'))
