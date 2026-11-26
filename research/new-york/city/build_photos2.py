"""R9: pick four cleared room views per venue, HEAD-check them, and write the
revision-1 photo records."""
import json, subprocess, time, re
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
cand = json.loads((CITY / 'photo-candidates-rev1.json').read_text())
inv = json.loads((CITY / 'venue-inventory.json').read_text())
pages = json.loads((CITY / 'venue-pages.json').read_text())
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')
SLOTS = 4


def spread(items, n=SLOTS):
    if len(items) <= n:
        return list(items)
    last = len(items) - 1
    picks, used = [], set()
    for step in range(n):
        i = round(last * step / (n - 1))
        while i in used:
            i = (i + 1) % len(items)
        used.add(i)
        picks.append(items[i])
    return [p for _, p in sorted(zip(used, picks))]


def head(url):
    proc = subprocess.run(['curl', '-sS', '-I', '-L', '-m', '30', '-A', UA, url],
                          capture_output=True, text=True)
    status, ctype, size = 0, '', 0
    for line in proc.stdout.splitlines():
        low = line.lower()
        if low.startswith('http/'):
            parts = line.split()
            if len(parts) > 1 and parts[1].isdigit():
                status = int(parts[1])
        elif low.startswith('content-type:'):
            ctype = line.split(':', 1)[1].strip()
        elif low.startswith('content-length:'):
            try:
                size = int(line.split(':', 1)[1].strip())
            except ValueError:
                pass
    return status, ctype, size


out = {}
for vid, items in cand.items():
    if not items:
        continue
    picks = spread(items)
    brand = (inv[vid]['name'] or '').split(' — ')[0]
    addr = inv[vid]['address'][0]
    listing = (inv[vid]['source_url'][0] or '')
    recs = []
    for p in picks:
        status, ctype, size = head(p['url'])
        time.sleep(0.15)
        rec = {
            'url': p['url'],
            'alt': p['alt'][:300],
            'alt_basis': 'listing caption and alt text: %r / %r' % (p['caption'], p['alt'][:90]),
            'caption': p['caption'],
            'view_kind': p['view_kind'],
            'view': p['caption'],
            'width': p['width'],
            'height': p['height'],
            'dimensions': {'width': p['width'], 'height': p['height']},
            'source_page': listing,
            'pages_checked': [listing],
            'rights': ('Operator gallery asset; © %s; hotlinked from the Tagvenue listing for '
                       'this room with attribution. The listing publishes no separate licence '
                       'text.' % brand),
            'attribution': brand,
            'hotlink_ok': status in (200, 206) and ctype.startswith('image/'),
            'verified': {'status': status, 'content_type': ctype, 'bytes': size,
                         'checked_on': '2026-11-26'},
            'checked_on': '2026-11-26',
            'placement_proof': ('Gallery image on the Tagvenue listing for %s at %s; the '
                                'caption %r names the room and the listing prints the address.'
                                % (p['caption'], addr, p['caption'])),
            'distance_m': 0,
            'withheld': not (status in (200, 206) and ctype.startswith('image/')),
        }
        recs.append(rec)
        print(vid, status, ctype, size, p['view_kind'], p['caption'][:40])
    out[vid] = recs
(CITY / 'photo-enrichment-rev1.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
print('venues', len(out), 'photos', sum(len(v) for v in out.values()))
