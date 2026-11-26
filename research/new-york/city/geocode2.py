"""R9: second geocode pass with cleaned address strings (floor/suite/parenthetical
text removed) for records the first pass could not resolve."""
import json, subprocess, time, urllib.parse, re
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
GEO = CITY / 'geocode'
UA = 'nyc-city-refresh/1.0 (coe-events research)'
log = json.loads((CITY / 'geocode-log.json').read_text())


def clean(address):
    text = re.sub(r'\([^)]*\)', '', address)
    text = re.sub(r'\b(?:Ground|Mezzanine|\d{1,2}(?:st|nd|rd|th)|Floors?)\s+Floor\b', '', text, flags=re.I)
    text = re.sub(r'\bFloors?\s+[\d,\s&and]+', '', text, flags=re.I)
    text = re.sub(r'\bFLOOR\s+\d+\b', '', text, flags=re.I)
    text = re.sub(r'\bSuite\s+\d+\b', '', text, flags=re.I)
    text = re.sub(r'\bStudio\s+\d+\b', '', text, flags=re.I)
    text = re.sub(r'\b\d{1,2}th\s+floor\b', '', text, flags=re.I)
    text = re.sub(r'\b(?:2nd|3rd|1st)\s+Floor\b', '', text, flags=re.I)
    parts = [' '.join(p.split()) for p in text.split(',')]
    parts = [p for p in parts if p]
    return ', '.join(parts)


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
        time.sleep(3 + 3 * attempt)
    return None, last


def q_url(q):
    return ('https://nominatim.openstreetmap.org/search?format=jsonv2&addressdetails=1'
            '&extratags=1&limit=4&accept-language=en&q=' + urllib.parse.quote(q))


for vid, rec in log.items():
    hits = [v for v in rec['lookups'].values()
            if isinstance(v.get('response'), list) and v['response']]
    if hits:
        continue
    raw = rec['address']
    cleaned = clean(raw)
    rec.setdefault('lookups', {})
    data, err = fetch(q_url(cleaned))
    rec['lookups']['clean'] = {'query': cleaned, 'url': q_url(cleaned), 'response': data}
    if err:
        rec['lookups']['clean']['error'] = err
    print(vid, 'clean ->', len(data) if data else err, '|', cleaned, flush=True)
    time.sleep(2.5)
    if not data:
        street = cleaned.split(',')[0]
        data2, err2 = fetch(q_url(street + ', New York'))
        rec['lookups']['street'] = {'query': street + ', New York',
                                    'url': q_url(street + ', New York'),
                                    'response': data2}
        if err2:
            rec['lookups']['street']['error'] = err2
        print(vid, 'street ->', len(data2) if data2 else err2, flush=True)
        time.sleep(2.5)
    (GEO / ('%s.json' % vid)).write_text(json.dumps(rec, indent=1, ensure_ascii=False))

(CITY / 'geocode-log.json').write_text(json.dumps(log, indent=1, ensure_ascii=False))
print('with hits', sum(1 for r in log.values()
                       if any(isinstance(v.get('response'), list) and v['response']
                              for v in r['lookups'].values())), 'of', len(log))
