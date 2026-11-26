"""R9: save the CUNY Graduate Center retry lookup into the geocode log."""
import json, subprocess, time, urllib.parse
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
UA = 'nyc-city-refresh/1.0 (coe-events research)'
q = 'CUNY Graduate Center, New York'
url = ('https://nominatim.openstreetmap.org/search?format=jsonv2&addressdetails=1'
       '&extratags=1&limit=4&accept-language=en&q=' + urllib.parse.quote(q))
proc = subprocess.run(['curl', '-sS', '-m', '40', '-A', UA, url], capture_output=True, text=True)
data = json.loads(proc.stdout)
log = json.loads((CITY / 'geocode-log.json').read_text())
log['nyc-lead-cuny-gc']['lookups']['name-city'] = {'query': q, 'url': url, 'response': data}
(CITY / 'geocode-log.json').write_text(json.dumps(log, indent=1, ensure_ascii=False))
(CITY / 'geocode' / 'nyc-lead-cuny-gc.json').write_text(
    json.dumps(log['nyc-lead-cuny-gc'], indent=1, ensure_ascii=False))
print(len(data), data[0]['lat'], data[0]['lon'], data[0]['display_name'][:90])
