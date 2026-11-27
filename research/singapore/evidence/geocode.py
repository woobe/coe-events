import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore')
OUT = BASE / 'city' / 'geocode-responses'
OUT.mkdir(exist_ok=True)
LOG = BASE / 'city' / 'geocode-log-rev1.json'
UA = 'coe-events-singapore-refresh/1.0 (address verification; one lookup per venue)'

def norm(s):
    s = str(s or '').lower()
    s = s.replace('&', ' and ')
    s = re.sub(r"['\u2019]", '', s)
    s = re.sub(r'\b(street|st)\b', 'st', s)
    s = re.sub(r'\b(road|rd)\b', 'rd', s)
    s = re.sub(r'\b(avenue|ave)\b', 'ave', s)
    s = re.sub(r'\b(boulevard|blvd)\b', 'blvd', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return ' '.join(s.split())

def get_json(url, tag):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read().decode('utf-8', 'replace')
    (OUT / (tag + '.json')).write_text(body, encoding='utf-8')
    return json.loads(body)

def photon(q, tag):
    url = 'https://photon.komoot.io/api/?' + urllib.parse.urlencode(
        {'q': q, 'limit': 5, 'lang': 'en', 'lat': 1.3521, 'lon': 103.8198})
    try:
        return url, get_json(url, tag + '-photon')
    except Exception as e:
        return url, {'error': repr(e)}

def nominatim(q, tag):
    url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode(
        {'q': q, 'format': 'json', 'limit': 5, 'addressdetails': 1, 'countrycodes': 'sg'})
    try:
        time.sleep(1.1)
        return url, get_json(url, tag + '-nominatim')
    except Exception as e:
        return url, {'error': repr(e)}

def ph_features(payload):
    out = []
    for f in (payload.get('features') or []):
        p = f.get('properties') or {}
        c = (f.get('geometry') or {}).get('coordinates') or [None, None]
        out.append({'name': p.get('name'), 'hn': p.get('housenumber'), 'street': p.get('street'),
                    'pc': p.get('postcode'), 'city': p.get('city'), 'district': p.get('district'),
                    'locality': p.get('locality'), 'lat': c[1], 'lon': c[0]})
    return out

def nom_results(payload):
    out = []
    for r in (payload if isinstance(payload, list) else []):
        a = r.get('address') or {}
        out.append({'name': r.get('name'), 'hn': a.get('house_number'), 'street': a.get('road'),
                    'pc': a.get('postcode'), 'city': a.get('city'), 'district': a.get('suburb'),
                    'locality': a.get('neighbourhood'), 'lat': float(r.get('lat')), 'lon': float(r.get('lon'))})
    return out

def match(job, r):
    score = 0
    notes = []
    street_ok = norm(r.get('street')) == norm(job['street']) or norm(job['street']) in norm(r.get('street')) or norm(r.get('street')) in norm(job['street'])
    pc_ok = str(r.get('pc') or '') == str(job['pc'])
    hn_ok = norm(r.get('hn')) == norm(job['hn']) or norm(job['hn']).rstrip('abcdefghijklmnopqrstuvwxyz') == norm(r.get('hn'))
    name_ok = False
    if r.get('name') and job.get('name'):
        a = set(norm(r['name']).split())
        b = set(norm(job['name']).split()) - {'at', 'the', 'singapore', 'event', 'hall', 'space'}
        name_ok = len(a & b) >= min(2, len(b)) and len(b) > 0
    if street_ok: score += 1
    if pc_ok: score += 2
    if hn_ok: score += 2
    if name_ok: score += 2
    notes = [k for k, v in (('street', street_ok), ('postcode', pc_ok), ('housenumber', hn_ok), ('name', name_ok)) if v]
    if hn_ok and (pc_ok or street_ok) and name_ok:
        tier = 'exact_venue'
    elif hn_ok and (pc_ok or street_ok):
        tier = 'building'
    elif street_ok and pc_ok:
        tier = 'street'
    elif street_ok:
        tier = 'street'
    else:
        tier = None
    return {'score': score, 'tier': tier, 'matched_on': notes, 'name_ok': name_ok,
            'hn_ok': hn_ok, 'pc_ok': pc_ok, 'street_ok': street_ok}

def main():
    jobs = json.load(open(sys.argv[1]))
    log = []
    for job in jobs:
        tag = job['id']
        url, payload = photon(job['q'], tag)
        cands = ph_features(payload) if isinstance(payload, dict) and 'features' in payload else []
        chosen = None
        for r in cands:
            m = match(job, r)
            r.update(m)
            if m['tier'] and (chosen is None or m['score'] > chosen['score']):
                chosen = r
        provider = 'Photon (OpenStreetMap data, komoot)'
        raw_url = url
        if chosen is None:
            url2, payload2 = nominatim(job['q'], tag)
            cands = nom_results(payload2) if isinstance(payload2, list) else []
            for r in cands:
                m = match(job, r)
                r.update(m)
                if m['tier'] and (chosen is None or m['score'] > chosen['score']):
                    chosen = r
            provider = 'OpenStreetMap Nominatim (Photon had no tier-matching result)'
            raw_url = url2
        entry = {'venue_id': job['id'], 'query': job['q'], 'checked_on': '2026-11-26',
                 'provider': provider, 'request_url': raw_url,
                 'expected': {'street': job['street'], 'housenumber': job['hn'], 'postcode': job['pc'],
                              'building': job.get('building')},
                 'candidates': cands[:5], 'chosen': chosen}
        log.append(entry)
        print(job['id'], '->', (chosen or {}).get('tier'), (chosen or {}).get('score'),
              (chosen or {}).get('street'), (chosen or {}).get('hn'), (chosen or {}).get('pc'),
              (chosen or {}).get('name'), (chosen or {}).get('lat'), (chosen or {}).get('lon'), flush=True)
    LOG.write_text(json.dumps(log, indent=1, ensure_ascii=False), encoding='utf-8')
    print('wrote', LOG)

if __name__ == '__main__':
    main()
