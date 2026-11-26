#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/photo-records.json')
recs = json.loads(p.read_text())
for vid, rows in recs.items():
    for r in rows:
        print(vid, repr(r.get('view_kind')), repr(r.get('room')), str(r.get('url'))[-45:],
              (r.get('verified') or {}).get('status'))
