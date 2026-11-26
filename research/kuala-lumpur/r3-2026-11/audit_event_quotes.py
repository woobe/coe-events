#!/usr/bin/env python3
"""Resolve every locator on the two net-new events against its capture."""
import json
import re
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
store = json.loads((BASE / 'city/city.json').read_text())
R3 = BASE / 'r3-2026-11/captures'

for eid in ('kl-ev-0f2a91c4d7b3', 'kl-ev-7c41b0e2a9d5'):
    ev = store['events'][eid]
    print('==', eid, ev['name'])
    for field, row in ev['fields'].items():
        loc = str(row.get('source_locator') or '')
        m = re.match(r'capture ([a-z0-9-]+) lines? (\d+)(?:-(\d+))?$', loc)
        if not m:
            print('  %-18s value=%-60r locator=%s (no line check)' % (
                field, row.get('value'), loc[:90]))
            continue
        slug, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        text = [ln.rstrip('\n') for ln in (R3 / (slug + '.txt')).read_text(
            encoding='utf-8', errors='replace').splitlines()]
        window = '\n'.join(text[a - 1:b])
        quote = str(row.get('quote') or '').strip()
        ok = bool(quote) and quote in window
        print('  %-18s lines %-8s quote-in-window=%s value=%r' % (
            field, '%d-%d' % (a, b), ok, row.get('value')))
        if not ok:
            print('      quote %r' % quote[:120])
            print('      window %r' % window[:120])
    print('  evidence url', ev['evidence'][0]['source_url'])
