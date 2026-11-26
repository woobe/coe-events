"""R9: geocode every New York venue afresh (retry + fallback queries)."""
import json, subprocess, time, urllib.parse, re
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
GEO = CITY / 'geocode'
GEO.mkdir(exist_ok=True)
UA = 'nyc-city-refresh/1.0 (coe-events research)'
inv = json.loads((CITY / 'venue-inventory.json').read_text())

verified = {vid: (row['address'][0] or '') for vid, row in inv.items()}
verified.update({
    'nyc-646e1e5393b6': '87 Lafayette Street, New York, NY 10013',
    'nyc-aa32c5682549': '135 Madison Avenue, New York, NY 10016',
    'nyc-6d04b6ce2634': '60-47 Metropolitan Avenue, Ridgewood, NY 11385',
    'nyc-lead-advent-hope': '111 East 87th Street, New York, NY 10128',
    'nyc-lead-cuny-gc': '365 Fifth Avenue, New York, NY 10016',
    'nyc-lead-bpl-meeting-rooms': '10 Grand Army Plaza, Brooklyn, NY 11238',
})

def fetch(url, tries=3):
    last = ''
    for attempt in range(tries):
        proc = subprocess.run(['curl', '-sS', '-m', '40', '-A', UA, url],
                              capture_output=True, text=True)
        body = proc.stdout.strip()
        if body:
            try:
                data = json.loads(body)
            except Exception:
                last = 'bad-json: ' + body[:120]
            else:
                if isinstance(data, list):
                    return data, None
                last = 'error-object: ' + json.dumps(data)[:120]
        else:
            last = 'empty response (curl %s) %s' % (proc.returncode, proc.stderr[:80])
        time.sleep(2 + 3 * attempt)
    return None, last

def q_url(q):
    return ('https://nominatim.openstreetmap.org/search?format=jsonv2&addressdetails=1'
            '&extratags=1&limit=4&accept-language=en&q=' + urllib.parse.quote(q))

results = {}
for vid, address in verified.items():
    path = GEO / ('%s.json' % vid)
    old = json.loads(path.read_text()) if path.exists() else None
    if old and any(isinstance(v.get('response'), list) and v['response']
                   for v in old['lookups'].values()):
        results[vid] = old
        print('cached', vid)
        continue
    name = inv[vid]['name'] or ''
    short = re.split(r'\s+[—-]\s+', name)[0].strip()
    queries = [('address', address)]
    if address.count(',') >= 2:
        parts = [p.strip() for p in address.split(',')]
        queries.append(('address-short', ', '.join([parts[0], parts[1], 'NY'])))
    queries.append(('name', '%s, %s' % (short, address)))
    rows = {}
    for kind, q in queries:
        url = q_url(q)
        data, err = fetch(url)
        rows[kind] = {'query': q, 'url': url, 'response': data}
        if err:
            rows[kind]['error'] = err
        print(vid, kind, '->', len(data) if data else err, flush=True)
        time.sleep(2.0)
    results[vid] = {'name': name, 'address': address, 'lookups': rows}
    path.write_text(json.dumps(results[vid], indent=1, ensure_ascii=False))

(CITY / 'geocode-log.json').write_text(json.dumps(results, indent=1, ensure_ascii=False))
print('done', len(results),
      'with hits', sum(1 for r in results.values()
                       if any(isinstance(v.get('response'), list) and v['response']
                              for v in r['lookups'].values())))
