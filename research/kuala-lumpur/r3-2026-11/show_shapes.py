import json
from pathlib import Path
kl = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
print(json.dumps(kl['sources_consulted'][0], indent=1)[:900])
print('--- event full')
eid = 'kl-ev-424614cfd600'
print(json.dumps(kl['events'][eid], indent=1)[:3000])
print('--- runs')
print(json.dumps(kl['runs'], indent=1)[:900])
print('--- community first')
print(json.dumps(list(kl['communities'].values())[0], indent=1)[:900])
