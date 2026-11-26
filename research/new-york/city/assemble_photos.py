"""R9: write revision-1 photo collections (room-first, rights recorded, withheld otherwise)."""
import json, re
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
store = json.loads(STORE.read_text())
enrich = json.loads((CITY / 'photo-enrichment-rev1.json').read_text())
inv = json.loads((CITY / 'venue-inventory.json').read_text())
old = store['photos']

WITHHELD = {
    'nyc-12c98ff34e33': ('The NYU Kimmel reservable-spaces page returned HTTP 202 with an empty body on '
                         '2026-11-26 and no operator gallery could be read; nothing is shown rather '
                         'than a look-alike.', 'https://www.nyu.edu/life/campus-resources/kimmel-center/reservable-spaces.html'),
    'nyc-75c0f7334372': ('The Peerspace listing returned HTTP 403 (bot challenge) on 2026-11-26; no '
                         'operator gallery or licence could be read.', 'https://www.peerspace.com/pages/listings/5c5377f8961209000e6834b0'),
    'nyc-ca43f10af68d': ('The NYC Seminar & Conference Center room page returned HTTP 429 on 2026-11-26 '
                         'and its gallery could not be read; no licence or room caption was proven.',
                         'https://nycseminarcenter.com/Seminar_Room_a/'),
    'nyc-lead-bpl-meeting-rooms': ('The Brooklyn Public Library meeting-rooms page returned HTTP 403 '
                                   '(Cloudflare challenge) on 2026-11-26; no gallery could be read.',
                                   'https://www.bklynlibrary.org/locations/central/meeting-rooms'),
    'nyc-lead-advent-hope': ('The operator page carries one uncaptioned hero image; no room gallery, '
                             'floor plan or licence was found, so no image is placeable at a room.',
                             'https://www.adventhope.org/rent'),
}

counts = {'1+': 0, '4+': 0, 'none': 0}
for vid, venue in store['venues'].items():
    kept = []
    for p in old.get(vid, []):
        if p.get('withheld') or not str(p.get('url') or '').startswith('http'):
            continue
        p = dict(p)
        p.setdefault('view_kind', 'interior' if 'Interior' in (p.get('alt') or '') else 'exterior')
        p.setdefault('rights', p.get('licence') or p.get('rights_basis'))
        p.setdefault('view', p.get('alt'))
        p['checked_on'] = '2026-11-26'
        kept.append(p)
    fresh = []
    for p in enrich.get(vid, []):
        p = dict(p)
        caption = p.get('caption') or ''
        roomish = bool(re.search(r'\b(room|loft|hall|studio|theatre|theater|space|auditorium|atrium|garden|venue|floor)\b', caption, re.I))
        p['room'] = caption if roomish else None
        p['placement_proof'] = (
            'Gallery image on the operator/Tagvenue listing for %s at %s; the listing page names the '
            'room and prints the address, and the gallery caption is %r.'
            % (inv[vid]['name'], inv[vid]['address'][0], caption))
        fresh.append(p)
    merged = kept + fresh
    seen, picks = set(), []
    for p in merged:
        if p['url'] in seen:
            continue
        seen.add(p['url'])
        picks.append(p)
        if len(picks) == 4:
            break
    if picks:
        store['photos'][vid] = picks
        if len(picks) >= 4:
            counts['4+'] += 1
        counts['1+'] += 1
    else:
        url = WITHHELD.get(vid, ('No placeable image was proven.', ''))[1]
        reason = WITHHELD.get(vid, ('No placeable image was proven.', ''))[0]
        store['photos'][vid] = [{
            'alt': 'No verifiable photo of the venue', 'alt_basis': 'none',
            'checked_on': '2026-11-26', 'dimensions': {'height': None, 'width': None},
            'placement_proof': 'Withheld: ' + reason, 'source_page': url,
            'pages_checked': [url], 'rights': 'none', 'rights_basis': 'none',
            'view_kind': None, 'room': None, 'withheld': True, 'url': None, 'verified': None,
        }]
        counts['none'] += 1

store['photos'] = {vid: store['photos'].get(vid, []) for vid in store['venues']}
STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
print(counts, 'venues with photos', sum(1 for v in store['photos'].values() if v and not v[0].get('withheld')))
rights = {}
for vid, arr in store['photos'].items():
    for p in arr:
        if p.get('withheld'):
            continue
        key = 'CC' if 'CC ' in str(p.get('rights') or '') else 'operator'
        rights[key] = rights.get(key, 0) + 1
print('rights mix', rights)
