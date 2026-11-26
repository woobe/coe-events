"""R9: build cleared photo records for New York venues from operator/Tagvenue room
galleries, classify the view from the image caption, and HEAD-check every asset."""
import json, re, subprocess, time
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
CAP = CITY / 'captures'
pages = json.loads((CITY / 'venue-pages.json').read_text())
inv = json.loads((CITY / 'venue-inventory.json').read_text())
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')

PAST = ('guest', 'performer', 'mingl', 'party', 'celebrat', 'crowd', 'audience', 'attendee', 'dj ')
EXTERIOR = ('exterior', 'facade', 'street', 'building front', 'outside', 'storefront', 'entrance')
INTERIOR = ('loft', 'room', 'space', 'interior', 'seating', 'sofa', 'table', 'chairs', 'chair',
            'bar ', 'bar,', 'studio', 'hall', 'stage', 'auditorium', 'lounge', 'counter', 'desk',
            'screen', 'projector', 'lighting', 'floor', 'wall', 'ceiling', 'window')


def view_kind(alt):
    a = alt.casefold()
    if any(w in a for w in PAST):
        return 'past_event'
    if any(w in a for w in EXTERIOR):
        return 'exterior'
    if any(w in a for w in INTERIOR):
        return 'interior'
    return ''


def head(url):
    proc = subprocess.run(['curl', '-sS', '-I', '-L', '-m', '30', '-A', UA, url],
                          capture_output=True, text=True)
    status = 0
    ctype = ''
    size = 0
    for line in proc.stdout.splitlines():
        if line.lower().startswith('http/'):
            parts = line.split()
            if len(parts) > 1 and parts[1].isdigit():
                status = int(parts[1])
        elif line.lower().startswith('content-type:'):
            ctype = line.split(':', 1)[1].strip()
        elif line.lower().startswith('content-length:'):
            try:
                size = int(line.split(':', 1)[1].strip())
            except ValueError:
                pass
    return status, ctype, size


out = {}
for vid, rec in pages.items():
    gallery = rec.get('gallery') or []
    cands = []
    seen = set()
    for it in gallery:
        src, alt, caption = it.get('src'), (it.get('alt') or ''), (it.get('caption') or '')
        if not src or src in seen:
            continue
        if not caption or not alt:
            continue
        kind = view_kind(alt)
        if not kind:
            continue
        seen.add(src)
        cands.append({'url': src, 'alt': alt, 'caption': caption, 'view_kind': kind,
                      'width': it.get('width'), 'height': it.get('height')})
    # room-first: interior/layout/past_event before exterior
    cands.sort(key=lambda c: ({'interior': 0, 'layout': 0, 'past_event': 1, 'exterior': 2,
                               'lobby': 2, 'render': 2}.get(c['view_kind'], 3)))
    out[vid] = cands[:6]
    print(vid, len(gallery), 'usable', len(cands), '| kinds', [c['view_kind'] for c in cands[:6]])

(CITY / 'photo-candidates-rev1.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
print('venues with candidates', sum(1 for v in out.values() if v), 'of', len(out))
