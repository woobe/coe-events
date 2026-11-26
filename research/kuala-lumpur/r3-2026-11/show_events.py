import json
from pathlib import Path
kl = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
print('EVENTS')
for eid, e in kl['events'].items():
    f = e['fields']
    dr = (f.get('date_range') or {}).get('value')
    print(eid, '|', e.get('name'), '|', dr, '|', (f.get('source_url') or {}).get('value'))
print('LANES')
for s in kl['sources_consulted']:
    print('%-28s %s pages=%s venues=%s events=%s | %s' % (
        s.get('lane'), (s.get('url') or '')[:70], s.get('pages_read'), s.get('venue_yield'),
        s.get('event_yield'), (s.get('note') or '')[:60]))
