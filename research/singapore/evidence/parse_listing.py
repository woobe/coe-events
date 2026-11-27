import json, re, sys
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city/captures')
store = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/city/city.json'))
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
out = {}

for vid, v in store['venues'].items():
    p = BASE / ('src-' + vid + '.html')
    if not p.exists():
        continue
    html = p.read_text(encoding='utf-8', errors='replace')
    text = (BASE / ('src-' + vid + '.txt')).read_text(encoding='utf-8', errors='replace')
    plain = '\n'.join(re.sub(r'^\s*\d+\|\s?', '', l) for l in text.splitlines())
    src = v['fields']['source_url']['value']
    m = re.search(r'/rooms/singapore/(\d+)/', src)
    lid = m.group(1) if m else None
    rec = {'id': vid, 'listing_id': lid, 'src': src}
    # pricing spans
    spans = {}
    for day in DAYS:
        mm = re.search(day + r'\s*\n\s*(\d{1,2}:\d{2})\s*[–-]\s*\n?\s*(\d{1,2}:\d{2})', plain)
        if mm:
            spans[day] = mm.group(1) + '-' + mm.group(2)
        else:
            mm = re.search(day + r'\s+(\d{1,2}:\d{2})\s*[–-]\s*(\d{1,2}:\d{2})', plain)
            if mm:
                spans[day] = mm.group(1) + '-' + mm.group(2)
    rec['spans'] = spans
    mm = re.search(r'Minimum booking duration:\s*\n?\s*(\d+)\s*hours?', plain)
    rec['min_hours'] = mm.group(1) if mm else None
    # package lines
    pkg = []
    for line in plain.splitlines():
        if re.search(r'(PACKAGE|WEEKDAY|WEEKEND|Starting from|hours:|Mon to|Sat to|Fri &|Morning \(|Afternoon \(|Evening \()', line, re.I):
            pkg.append(line.strip())
    rec['package'] = pkg[:12]
    # images filtered to listing id or venue name
    imgs = []
    for im in re.finditer(r'<img[^>]+>', html):
        tag = im.group(0)
        srcm = re.search(r'src="([^"]+)"', tag)
        altm = re.search(r'alt="([^"]*)"', tag)
        if not srcm:
            continue
        u = srcm.group(1)
        a = altm.group(1) if altm else ''
        if 'tagvenue.com/resize' not in u:
            continue
        if lid and (lid + '-' in u):
            imgs.append((u, a))
        elif a and ('at ' in a) and ('Trehaus' in a or 'room' in a.lower()):
            pass
    seen = set(); ded = []
    for u, a in imgs:
        key = re.sub(r'^https://www.tagvenue.com/resize/[^;]+;', '', u)
        if key in seen:
            continue
        seen.add(key); ded.append({'url': u, 'alt': a})
    rec['images'] = ded
    out[vid] = rec

json.dump(out, open('/home/joe/repo_dev/coe-events/research/singapore/evidence/listing_parse.json', 'w'), indent=1)
for vid, r in out.items():
    if r['listing_id']:
        print(vid, r['listing_id'], 'min', r['min_hours'], 'spans', r['spans'], 'imgs', len(r['images']))
        if r['package']:
            print('   pkg:', ' || '.join(r['package'][:6]))
