import json
from pathlib import Path
kl = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
for vid in ['kl-73ee37f91926', 'kl-06d6f98467c0', 'kl-d86dffabc235']:
    print('==', vid, len(kl['photos'].get(vid) or []))
    print(json.dumps((kl['photos'].get(vid) or [])[:2], indent=1, ensure_ascii=False)[:1800])
print('photo counts per venue:')
for vid, rows in kl['photos'].items():
    live = [r for r in rows if not r.get('withheld')]
    print(vid, len(rows), 'live', len(live))
