#!/usr/bin/env python3
import json
import sys
from pathlib import Path

SK = Path('/home/joe/repo_dev/hermes-skills')
sys.path.insert(0, str(SK / 'plan-event' / 'scripts'))
import city_rank

STORE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json')
store = json.loads(STORE.read_text())
ranking = city_rank.build_ranking(store, '2026-11-26')
print('keys', sorted(ranking))
print('counts', json.dumps(ranking.get('counts'), indent=1)[:800])
print('leads', len(ranking.get('leads') or []))
for k, v in ranking.items():
    if isinstance(v, list):
        print('list key', k, len(v))
    elif isinstance(v, dict):
        print('dict key', k, sorted(v)[:10])
