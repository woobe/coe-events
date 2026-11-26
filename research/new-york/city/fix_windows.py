"""R9 fix: programme_windows states belong inside the claim's `value`, not beside it."""
import json
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
s = json.loads(STORE.read_text())
fixed = 0
for vid, v in s['venues'].items():
    pw = v['fields'].get('programme_windows')
    if not isinstance(pw, dict):
        continue
    stray = {'8': pw.pop('8', None), '12': pw.pop('12', None)}
    if any(stray.values()):
        value = pw.setdefault('value', {})
        for key, row in stray.items():
            if row:
                value[key] = row
        fixed += 1
STORE.write_text(json.dumps(s, indent=1, ensure_ascii=False))
print('fixed', fixed)
for vid in ('nyc-cf2d116c0745', 'nyc-4f482327c22f', 'nyc-ca43f10af68d'):
    print(vid, json.dumps(s['venues'][vid]['fields']['programme_windows']['value'], indent=1)[:600])
