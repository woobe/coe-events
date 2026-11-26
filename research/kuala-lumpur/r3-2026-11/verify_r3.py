#!/usr/bin/env python3
"""R3 verification: --check, ranker, loss check, counts and the scratch render."""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

SK = Path('/home/joe/repo_dev/hermes-skills')
sys.path.insert(0, str(SK / 'plan-event' / 'scripts'))
import city_rank  # noqa: E402
import city_store  # noqa: E402

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
STORE = BASE / 'city' / 'city.json'
store = json.loads(STORE.read_text())
before = json.loads((BASE / 'city' / 'city.pre-r3.json').read_text())

print('sha256', hashlib.sha256(STORE.read_bytes()).hexdigest(), 'bytes', STORE.stat().st_size)

errors = city_store.validate_store(store, str(SK / 'plan-event/references/school_holidays.json'),
                                   str(STORE.parent))
print('validate errors', len(errors))

ranking = city_rank.build_ranking(store, '2026-11-26')
rows = list(ranking.get('rows') or []) + list(ranking.get('leads') or [])
print('rank counts', json.dumps(ranking.get('counts')), 'rows', len(rows),
      'unique ids', len({r['venue_id'] for r in rows}))
print('rank keys', sorted(ranking)[:8])

loss = city_store.loss_check(before, store)
print('loss', json.dumps(loss)[:600])

# ---------------------------------------------------------------- counts
def field(v, key):
    return (v['fields'].get(key) or {}).get('value')

tiers = {}
for vid, v in store['venues'].items():
    co = field(v, 'coordinates') or {}
    tiers[co.get('precision')] = tiers.get(co.get('precision'), 0) + 1
print('tiers', tiers)

def photos(s, k):
    return len({p['url'] for p in s['photos'].get(k, []) if
                str(p.get('url') or '').startswith(('https://', 'http://'))
                and not p.get('withheld') and p.get('hotlink_ok', True)})

for label, s in (('before', before), ('after', store)):
    counts = [photos(s, k) for k in s['venues']]
    print('%s photos venues 1+ %d 4+ %d none %d; rows live %d withheld %d' % (
        label, sum(n >= 1 for n in counts), sum(n >= 4 for n in counts), counts.count(0),
        sum(1 for k in s['photos'] for p in s['photos'][k] if not p.get('withheld')),
        sum(1 for k in s['photos'] for p in s['photos'][k] if p.get('withheld'))))

rights = {}
for k, rows_ in store['photos'].items():
    for p in rows_:
        if p.get('withheld') or not p.get('url'):
            continue
        basis = 'wikimedia' if 'wikimedia' in str(p.get('rights_basis') or '') else 'operator'
        rights[basis] = rights.get(basis, 0) + 1
print('rights mix (after)', rights)
kinds = {}
for k, rows_ in store['photos'].items():
    for p in rows_:
        if p.get('withheld') or not p.get('url'):
            continue
        kinds[p.get('view_kind')] = kinds.get(p.get('view_kind'), 0) + 1
print('view kinds (after)', kinds)

local = {'MY', 'MY-14'}
def hcount(s, year_only=True):
    out = {}
    for h in s['holidays']:
        if year_only and not (h['start_date'] <= '2027-12-31' and h['end_date'] >= '2027-01-01'):
            continue
        scope = 'local' if h['jurisdiction_id'] in local else 'foreign'
        key = (scope, 'school' if h['kind'] == 'school_holiday' else 'public')
        out[key] = out.get(key, 0) + 1
    return out

print('holidays before', hcount(before), 'after', hcount(store))
bad = []
for h in store['holidays']:
    y, m, d = (int(x) for x in h['start_date'].split('-'))
    if h.get('weekday') != date(y, m, d).strftime('%A'):
        bad.append((h['start_date'], h.get('weekday')))
print('weekday mismatches', bad)

windows = {}
for vid, v in store['venues'].items():
    w = field(v, 'programme_windows') or {}
    state12 = (w.get('12') or {}).get('state')
    state8 = (w.get('8') or {}).get('state')
    windows[(state12, state8)] = windows.get((state12, state8), 0) + 1
print('window (12,8) states', windows)

events = store['events']
print('events', len(events), 'sources with yield', sum(1 for s in store['sources_consulted'] if s.get('event_yield')))
print('sources', len(store['sources_consulted']), 'gaps', len(store['declared_gaps']))
