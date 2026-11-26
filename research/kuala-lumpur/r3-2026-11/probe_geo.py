import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlencode

UA = 'CoeEventsResearch/1.0'
OUT = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/geocode-probe.json')


def run(q):
    url = 'https://nominatim.openstreetmap.org/search?' + urlencode(
        {'q': q, 'format': 'jsonv2', 'limit': 5, 'addressdetails': 1,
         'accept-language': 'en'})
    proc = subprocess.run(['curl', '-sS', '-m', '40', '-A', UA, url],
                          capture_output=True, timeout=70)
    body = proc.stdout.decode('utf-8', 'replace')
    return url, (json.loads(body) if body.strip().startswith('[') else [])


def main(queries):
    state = json.loads(OUT.read_text()) if OUT.exists() else {}
    for q in queries:
        if q in state:
            data = state[q]['candidates']
            url = state[q]['url']
        else:
            url, data = run(q)
            state[q] = {'url': url, 'checked_on': '2026-11-26', 'candidates': data}
            OUT.write_text(json.dumps(state, indent=1, ensure_ascii=False) + '\n',
                           encoding='utf-8')
            time.sleep(1.2)
        print('== %s' % q)
        for c in data[:5]:
            print('   %.6f,%.6f  %s | name=%s' % (float(c['lat']), float(c['lon']),
                                                  (c.get('display_name') or '')[:120],
                                                  c.get('name')))


if __name__ == '__main__':
    main(sys.argv[1:])
