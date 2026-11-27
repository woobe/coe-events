"""Measure the usable photo URLs so the store can carry real dimensions."""
import io
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore')
store = json.load(open(BASE / 'city' / 'city.json'))
urls = []
for vid, recs in store['photos'].items():
    for r in recs:
        u = r.get('url')
        if u and not r.get('withheld') and u not in urls:
            urls.append(u)
print('unique usable urls', len(urls))


def probe(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (compatible; hermes-research/1.0)'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = resp.read(6_000_000)
                ct = resp.headers.get('Content-Type')
                status = resp.status
            im = Image.open(io.BytesIO(data))
            return u, {'width': im.width, 'height': im.height, 'format': im.format,
                       'content_type': ct, 'http_status': status, 'bytes_read': len(data)}
        except Exception as exc:
            err = '%s: %s' % (type(exc).__name__, exc)
    return u, {'error': err}


out = {}
with ThreadPoolExecutor(max_workers=8) as pool:
    for u, rec in pool.map(probe, urls):
        out[u] = rec
        print('ok' if 'error' not in rec else 'ERR', (rec.get('width'), rec.get('height')), u[:110])

Path(BASE / 'evidence' / 'photo-dimensions.json').write_text(
    json.dumps(out, indent=1, sort_keys=True) + '\n', encoding='utf-8')
ok = sum(1 for r in out.values() if 'error' not in r)
print('measured', ok, 'of', len(out))
