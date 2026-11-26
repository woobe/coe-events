"""R9: add the CUNY Graduate Center and Civic Hall room photos from the operators'
own space pages."""
import json, subprocess, time
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')
out = json.loads((CITY / 'photo-enrichment-rev1.json').read_text())


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


SPECS = {
    'nyc-lead-cuny-gc': {
        'brand': 'CUNY Graduate Center',
        'address': '365 Fifth Avenue, New York, NY 10016',
        'page': 'https://spacerentals.gc.cuny.edu/',
        'items': [
            ('https://spacerentals.gc.cuny.edu/files/2025/09/Proshansky4-1400-0925.webp',
             'interior', 'Proshansky Auditorium - Auditorium Rental in NYC. Comfortable audience seating.'),
            ('https://spacerentals.gc.cuny.edu/files/2025/09/Elebash4_1400_0925.webp',
             'layout', 'Elebash Recital Hall - Theater Rental in NYC. Front of auditorium - front row seating and stage.'),
            ('https://spacerentals.gc.cuny.edu/files/2025/09/Skylight1-1400-0925.webp',
             'interior', 'Kelly Skylight Room - Flexible Event Space in NYC. Tables set up for a corporate event - formal dinner.'),
            ('https://spacerentals.gc.cuny.edu/files/2025/09/dining-commons1-1400.webp',
             'interior', 'Dining Commons - Reception Space in NYC. Close up of dinner table set up for a formal dinner.'),
        ],
    },
    'nyc-4c6638c43df6': {
        'brand': 'Civic Hall',
        'address': '124 East 14th Street, New York, NY 10003',
        'page': 'https://civichall.org/our-spaces/',
        'items': [
            ('https://cdn.prod.website-files.com/65c43c2479e30f10b200c063/65f3556c3ae8ec71bda6774a_ch_conference.jpg',
             'interior', 'ch_conference'),
            ('https://cdn.prod.website-files.com/65c43c2479e30f10b200c063/65f35641f5b9c2015230d7bd_ch_panel_conference.jpg',
             'interior', 'ch_panel_conference'),
            ('https://cdn.prod.website-files.com/65c43c2479e30f10b200c063/65f358621cd8af53a3589256_ch_elevated_lounge.jpg',
             'interior', 'ch_elevated_lounge'),
            ('https://cdn.prod.website-files.com/65c43c2479e30f10b200c063/65f358622bddf9b4127a7415_ch_elevated_symposium.png',
             'interior', 'ch_elevated_symposium'),
        ],
    },
}
for vid, spec in SPECS.items():
    recs = []
    for url, kind, desc in spec['items']:
        status, ctype, size = head(url)
        recs.append({
            'url': url,
            'alt': desc,
            'alt_basis': 'operator page alt text or asset file name',
            'view_kind': kind,
            'view': desc,
            'source_page': spec['page'],
            'pages_checked': [spec['page']],
            'rights': ('Operator gallery asset; © %s; hotlinked from the operator\'s own page '
                       'with attribution. The page publishes no separate licence text.'
                       % spec['brand']),
            'attribution': spec['brand'],
            'hotlink_ok': status in (200, 206) and ctype.startswith('image/'),
            'verified': {'status': status, 'content_type': ctype, 'bytes': size,
                         'checked_on': '2026-11-26'},
            'checked_on': '2026-11-26',
            'placement_proof': ('Image served on %s, the operator page that prices the spaces at '
                                '%s.' % (spec['page'], spec['address'])),
            'distance_m': 0,
            'withheld': not (status in (200, 206) and ctype.startswith('image/')),
        })
        print(vid, status, ctype, size, url.rsplit('/', 1)[-1])
        time.sleep(0.3)
    out[vid] = recs
(CITY / 'photo-enrichment-rev1.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
print('venues', len(out), 'photos', sum(len(v) for v in out.values()))
