import json, time, urllib.parse, urllib.request
from pathlib import Path
UA = 'coe-events-singapore-refresh/1.0'
queries = {
 'pico': 'Pico Creative Centre, 20 Kallang Avenue, Singapore',
 'enclosed': '41 Beach Road, Singapore 189680',
 'isca': 'ISCA House, 60 Cecil Street, Singapore 049709',
 'highfive': '40 Sam Leong Road, Singapore 207930',
 'wework21': '21 Collyer Quay, Singapore 049320',
 'aliwal': 'Aliwal Arts Centre, 28 Aliwal Street, Singapore 199918',
 'vidacity': 'Vidacity, 69 Ayer Rajah Crescent, Singapore 139961',
 'brasbasah': 'Bras Basah Complex, 231 Bain Street, Singapore 180231',
}
for tag, q in queries.items():
    url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode(
        {'q': q, 'format': 'json', 'limit': 4, 'addressdetails': 1, 'countrycodes': 'sg'})
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    print('===', tag, q)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        for d in data:
            a = d.get('address') or {}
            print('  ', d.get('lat'), d.get('lon'), '|', d.get('name'), '|', a.get('house_number'), a.get('road'), a.get('postcode'), '|', d.get('display_name')[:140])
        Path('/home/joe/repo_dev/coe-events/research/singapore/city/geocode-responses/retry-%s.json' % tag).write_text(json.dumps(data, indent=1))
    except Exception as e:
        print('  ERR', e)
    time.sleep(1.2)
