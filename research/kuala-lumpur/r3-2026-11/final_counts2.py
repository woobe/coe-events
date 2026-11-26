#!/usr/bin/env python3
"""Final counts for the handoff: pinless reconciliation, gaps, ids."""
import json
from pathlib import Path

base = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
store = json.loads((base / 'city/city.json').read_text())
pre = json.loads((base / 'city/city.pre-r3.json').read_text())


def f(v, k):
    return (v['fields'].get(k) or {}).get('value')


pre_pins = {vid for vid, v in pre['venues'].items()
            if isinstance(f(v, 'coordinates'), dict) and f(v, 'coordinates').get('latitude') is not None}
print('pre-image venues', len(pre['venues']), 'with pins', len(pre_pins), 'pinless', len(pre['venues']) - len(pre_pins))
tiers = {}
for vid, v in store['venues'].items():
    co = f(v, 'coordinates') or {}
    tiers[co.get('precision')] = tiers.get(co.get('precision'), 0) + 1
print('tiers all', tiers)
pinless_tiers = {}
for vid in pre['venues']:
    if vid in pre_pins:
        continue
    co = f(store['venues'][vid], 'coordinates') or {}
    pinless_tiers[co.get('precision')] = pinless_tiers.get(co.get('precision'), 0) + 1
print('pinless-39 tiers', pinless_tiers, 'unresolved',
      sum(1 for vid in pre['venues'] if vid not in pre_pins
          and not (f(store['venues'][vid], 'coordinates') or {}).get('precision')))
print('ids prefix ok', all(vid.startswith('kl-') for vid in store['venues']),
      'same id set', set(store['venues']) == set(pre['venues']))
print('refresh_revision', store.get('refresh_revision'), 'updated_at', store.get('updated_at'))
print('holidays', len(store['holidays']), 'coverage', len(store['coverage']),
      'events', len(store['events']), 'communities', len(store.get('communities') or []))
print('public', sum(1 for h in store['holidays'] if h['kind'] in ('public_holiday', 'municipal_holiday')),
      'school', sum(1 for h in store['holidays'] if h['kind'] == 'school_holiday'))
islam = [h for h in store['holidays'] if h['kind'] in ('public_holiday', 'municipal_holiday')
         and h.get('status') == 'derived']
print('islamic derived rows', len(islam),
      'subject_to_announcement', sum(1 for h in islam if h.get('subject_to_announcement')))
print('gaps', len(store['declared_gaps']))
for g in store['declared_gaps']:
    print('  -', g['kind'], '|', g['text'][:110])
print('alcohol yes', [vid for vid, v in store['venues'].items()
                      if (f(v, 'alcohol') or {}).get('state') == 'yes'] if False else 'n/a')
