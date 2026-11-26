#!/usr/bin/env python3
"""One live Nominatim search per query for every Kuala Lumpur record.

Writes geocode/<venue_id>.json with every attempt (query, URL, status, raw
candidates, chosen match, token evidence) and geocode-summary.json.
"""
import json
import subprocess
import time
from pathlib import Path
from urllib.parse import urlencode

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
OUT = BASE / 'r3-2026-11' / 'geocode'
UA = 'CoeEventsResearch/1.0'
CHECKED = '2026-11-26'


def query_url(q):
    return 'https://nominatim.openstreetmap.org/search?' + urlencode(
        {'q': q, 'format': 'jsonv2', 'limit': 4, 'addressdetails': 1,
         'accept-language': 'en'})


def run(q):
    url = query_url(q)
    proc = subprocess.run(['curl', '-sS', '-m', '40', '-A', UA, url],
                          capture_output=True, timeout=70)
    if proc.returncode != 0:
        raise OSError('curl exit %s: %s' % (proc.returncode,
                                            proc.stderr.decode()[:160]))
    body = proc.stdout.decode('utf-8', 'replace')
    if not body.strip():
        raise OSError('empty body')
    return url, json.loads(body)


def score(cand, tokens):
    text = (cand.get('display_name') or '').lower()
    addr = ' '.join(str(v) for v in (cand.get('address') or {}).values()).lower()
    hay = text + ' ' + addr
    hits = [t for t in tokens if t.lower() in hay]
    named = (cand.get('name') or '').lower()
    return len(hits), bool(named) and all(
        any(part in named for part in t.split()) for t in tokens), hits


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    store = json.loads((BASE / 'city/city.json').read_text())
    plan = json.loads((BASE / 'r3-2026-11' / 'address-plan.json').read_text())['venues']
    summary = {}
    for vid in store['venues']:
        entry = plan[vid]
        record = {'venue_id': vid, 'name': store['venues'][vid]['name'],
                  'checked_on': CHECKED, 'address': entry.get('address'),
                  'note': entry.get('note'), 'attempts': []}
        best = None
        for q in entry['queries']:
            attempt = {'query': q}
            try:
                url, data = run(q)
                attempt['url'] = url
                attempt['returned'] = len(data)
                attempt['candidates'] = data
                for cand in data:
                    hits, named, tokens = score(cand, entry['expect'])
                    cand['_score'] = {'hits': hits, 'all_tokens': hits == len(entry['expect']),
                                      'named_filter': named, 'tokens': tokens}
                    rank = (hits, named)
                    if best is None or rank > best[0]:
                        best = (rank, cand, q)
            except Exception as exc:  # noqa: BLE001
                attempt['error'] = str(exc)[:200]
            record['attempts'].append(attempt)
            time.sleep(1.2)
            if best and best[0][0] == len(entry['expect']):
                break
        if best:
            cand, q = best[1], best[2]
            record['chosen'] = {
                'query': q,
                'latitude': float(cand['lat']),
                'longitude': float(cand['lon']),
                'display_name': cand.get('display_name'),
                'name': cand.get('name'),
                'category': cand.get('category') or cand.get('class'),
                'type': cand.get('type'),
                'osm': '%s/%s' % (cand.get('osm_type'), cand.get('osm_id')),
                'tokens_matched': cand['_score']['tokens'],
                'all_tokens': cand['_score']['all_tokens'],
                'named_match': cand['_score']['named_filter'],
            }
        else:
            record['chosen'] = None
        (OUT / (vid + '.json')).write_text(
            json.dumps(record, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        chosen = record['chosen'] or {}
        print('%-16s %-42s %s %s' % (vid, record['name'][:42],
                                     'OK ' if record['chosen'] else 'FAIL',
                                     (chosen.get('display_name') or '')[:80]))
        summary[vid] = {k: record['chosen'][k] for k in
                        ('query', 'latitude', 'longitude', 'display_name', 'name',
                         'tokens_matched', 'all_tokens', 'named_match')} if record['chosen'] else None
    (BASE / 'r3-2026-11' / 'geocode-summary.json').write_text(
        json.dumps(summary, indent=1, ensure_ascii=False, sort_keys=True) + '\n',
        encoding='utf-8')
    ok = sum(1 for v in summary.values() if v)
    print('resolved', ok, 'of', len(summary))


if __name__ == '__main__':
    main()
