#!/usr/bin/env python3
import json
from pathlib import Path

store = json.loads(Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json').read_text())
pub = [h for h in store['holidays'] if h['kind'] in ('public_holiday', 'municipal_holiday')]
for h in pub[:3]:
    print(sorted(h.keys()))
print('---')
for h in pub:
    if str(h.get('basis') or h.get('date_basis') or '').startswith('derived') or h.get('subject_to_announcement'):
        print(h['holiday_name'], '|', h.get('basis'), '|', h.get('date_basis'),
              '|', h.get('subject_to_announcement'), '|', h.get('needs_human_verify'))
