import json
from pathlib import Path
kl = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
for s in kl['sources_consulted']:
    if s.get('event_yield'):
        print(s['event_yield'], s['url'][:90], '|', (s.get('note') or '')[:60])
print('sum', sum(int(s.get('event_yield') or 0) for s in kl['sources_consulted']))
print('events', len(kl['events']))
