import json, re, glob, os
from pathlib import Path
BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city/captures')

def ld_objs(html):
    out = []
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S|re.I):
        body = m.group(1).strip()
        try:
            d = json.loads(body)
        except Exception:
            continue
        if isinstance(d, list):
            out.extend(d)
        else:
            out.append(d)
    return out

rows = []
for p in sorted(BASE.glob('src-sg-*.html')):
    vid = p.name[4:-5]
    html = p.read_text(encoding='utf-8', errors='replace')
    rec = {'id': vid}
    venue = None
    for d in ld_objs(html):
        types = d.get('@type')
        if isinstance(types, str):
            types = [types]
        if types and any(t in ('EventVenue', 'LocalBusiness', 'Organization', 'Product') for t in types):
            if d.get('address') or d.get('geo'):
                venue = d
                break
    if venue:
        addr = venue.get('address') or {}
        if not isinstance(addr, dict):
            addr = {}
        geo = venue.get('geo') or {}
        if not isinstance(geo, dict):
            geo = {}
        rec.update({
            'name': venue.get('name'),
            'street': addr.get('streetAddress'),
            'postcode': addr.get('postalCode'),
            'locality': addr.get('addressLocality'),
            'lat': geo.get('latitude'),
            'lon': geo.get('longitude'),
            'capacity': venue.get('maximumAttendeeCapacity'),
            'price': venue.get('priceRange'),
            'hours': venue.get('openingHoursSpecification'),
            'image': venue.get('image'),
            'hasMap': venue.get('hasMap'),
        })
    # text signals
    text = p.with_suffix('.txt').read_text(encoding='utf-8', errors='replace')
    for pat in ['Minimum hire', 'min. hire', 'Hire fee', 'Opening hours', 'Mon', 'Sat', 'Sun']:
        hits = [l.strip() for l in text.splitlines() if pat.lower() in l.lower()]
        if hits:
            rec.setdefault('signals', {})[pat] = hits[:4]
    rows.append(rec)

for r in rows:
    print('=' * 90)
    for k, v in r.items():
        if k == 'signals':
            print('  signals:')
            for kk, vv in v.items():
                print('   ', kk, '::', ' || '.join(x[:180] for x in vv))
        else:
            print(' ', k, ':', json.dumps(v, ensure_ascii=False)[:400])
json.dump(rows, open(BASE.parent.parent / 'evidence' / 'tagvenue-ld.json', 'w'), indent=1)
