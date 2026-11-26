import json, hashlib, os, time
from pathlib import Path

ROOT = Path('/home/joe/repo_dev/coe-events')
CITY = ROOT / 'research/new-york/city'
raw = (CITY / 'city.json').read_bytes()
after = json.loads(raw)
before = json.loads((CITY / 'city.pre-r9.json').read_text())

print('store bytes', len(raw), 'sha256', hashlib.sha256(raw).hexdigest())
print('refresh_revision', after.get('refresh_revision'), 'updated_at', after['updated_at'])

# event evidence urls vs sources
src = {r['url'] for r in after['sources_consulted']}
missing = []
for e in after['events'].values():
    for ev in e['evidence']:
        u = ev.get('source_url')
        if u and u not in src:
            missing.append((e['event_id'], u))
print('event evidence urls missing from sources:', missing)

# 12h changes
print('\n12h state changes (open venues):')
for vid, v in after['venues'].items():
    if v['lifecycle'] != 'open':
        continue
    old = ((before['venues'][vid]['fields'].get('programme_windows') or {}).get('12') or {}).get('state')
    new = ((v['fields'].get('programme_windows') or {}).get('12') or {}).get('state')
    if old != new:
        print(' ', vid, old, '->', new, '|', (v['fields'].get('access_window') or {}).get('value'))

print('\nphoto collections under 4:',
      [vid for vid, arr in after['photos'].items()
       if len({p['url'] for p in arr if p.get('url') and not p.get('withheld')}) < 4])

print('\ncity store mtimes:')
for p in sorted((ROOT / 'research').glob('*/city/city.json')):
    print(' ', p.parent.parent.name, time.strftime('%Y-%m-%d %H:%M', time.localtime(p.stat().st_mtime)))

for p in (ROOT / 'summary' / 'new-york-summary.html', ROOT / 'index.html'):
    print(p.name, time.strftime('%Y-%m-%d %H:%M', time.localtime(p.stat().st_mtime)), p.stat().st_size)
