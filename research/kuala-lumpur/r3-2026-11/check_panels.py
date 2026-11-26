#!/usr/bin/env python3
"""Check the five repaired panels and the labelled-fallback venues in the render."""
import json
import re
from pathlib import Path

STORE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json')
R2 = Path('/home/joe/.hermes/profiles/jnr-research/cache/scratch/kl-r3-render-r2.html')
R1 = Path('/home/joe/.hermes/profiles/jnr-research/cache/scratch/kl-r3-render-r1-repro.html')
store = json.loads(STORE.read_text())
ROOM = ('interior', 'layout', 'floor_plan', 'past_event')

FIVE = ['kl-13ee3afff10b', 'kl-a2b2e1986ea5', 'kl-d86dffabc235',
        'kl-73ee37f91926', 'kl-ade0334f2820']


def panel(html, vid):
    i = html.find('id="panel-%s"' % vid)
    if i < 0:
        return ''
    return html[i:html.find('</details>', i)]


def imgs(chunk):
    out = []
    for m in re.finditer(r'<img[^>]*>', chunk):
        tag = m.group(0)
        alt = re.search(r'alt="([^"]*)"', tag)
        out.append(alt.group(1) if alt else '')
    return out


r1 = R1.read_text(encoding='utf-8')
r2 = R2.read_text(encoding='utf-8')
print('render bytes  r1 %d  r2 %d' % (len(r1.encode()), len(r2.encode())))
print('Exterior labels r1 %d  r2 %d' % (r1.count('>Exterior<'), r2.count('>Exterior<')))
print()
for vid in FIVE:
    rows = [p for p in store['photos'][vid] if not p.get('withheld')]
    print('==', vid, store['venues'][vid]['name'])
    print('   stored kinds', [(p.get('view_kind'), (p.get('alt') or '')[:40]) for p in rows])
    print('   r1 gallery', imgs(panel(r1, vid)))
    print('   r2 gallery', imgs(panel(r2, vid)))
    chunk = panel(r2, vid)
    bad = [alt for alt in imgs(chunk) if 'building' in alt.lower()
           or 'exterior' in alt.lower() or 'night' in alt.lower()]
    print('   r2 unlabelled building shots in panel:', bad)

print()
print('fallback-only venues (no room kind) and their row labels in r2:')
shown = 0
for vid in store['venues']:
    live = [p for p in store['photos'].get(vid, [])
            if not p.get('withheld') and str(p.get('url')).startswith('http')]
    if not live or any(p.get('view_kind') in ROOM for p in live):
        continue
    row = re.search(r'data-venue-id="%s".{0,4000}?</th>' % vid, r2)
    label = 'Exterior' if row and '>Exterior<' in row.group(0) else ('Lobby' if row and '>Lobby<' in row.group(0) else None)
    shown += 1
    print('  ', vid, store['venues'][vid]['name'], '->', label)
print('fallback-only venues', shown)
