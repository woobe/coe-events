"""R9 gate: loss check, validation, ranking, counts, scratch render."""
import json, sys
from pathlib import Path

sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
import city_store, city_rank, city_page  # noqa: E402

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
before = json.loads((CITY / 'city.pre-r9.json').read_text())
after = json.loads((CITY / 'city.json').read_text())

print('== loss_check:', json.dumps(city_store.loss_check(before, after), sort_keys=True))
print('== validate:', city_store.validate_store(after) or 'OK')

rank = city_rank.build_ranking(after, str(after['updated_at'])[:10])
rows = rank.get('rows') or rank.get('venues') or []
print('== ranking keys:', list(rank.keys()))
print('== ranking counts:', rank.get('counts'), 'rows:', len(rows))
ids = [r.get('venue_id') or r.get('id') for r in rows]
print('== ranking unique ids:', len(set(ids)), 'missing:',
      sorted(set(after['venues']) - set(ids)))
print('== ranking order:')
for r in rows:
    print('  ', r.get('position'), r.get('venue_id'), r.get('group'), r.get('score'),
          (r.get('name') or '')[:40])

tiers = {}
for v in after['venues'].values():
    c = v['fields']['coordinates']['value']
    tiers[c['precision']] = tiers.get(c['precision'], 0) + 1
print('== tiers:', tiers, 'total', sum(tiers.values()))

def photo_count(store, vid):
    return len({p['url'] for p in store['photos'].get(vid, [])
                if p.get('url') and not p.get('withheld')})

for label, store in (('before', before), ('after', after)):
    counts = [photo_count(store, v) for v in store['venues']]
    print('== photos %s: 1+ %d  4+ %d  none %d  records %d' % (
        label, sum(1 for n in counts if n >= 1), sum(1 for n in counts if n >= 4),
        sum(1 for n in counts if n == 0), sum(len(a) for a in store['photos'].values())))

rights = {}
views = {}
for arr in after['photos'].values():
    for p in arr:
        if p.get('withheld'):
            continue
        key = 'CC' if 'CC ' in str(p.get('rights') or '') else 'operator'
        rights[key] = rights.get(key, 0) + 1
        views[p.get('view_kind')] = views.get(p.get('view_kind'), 0) + 1
print('== rights mix:', rights, 'views:', views)

for label, store in (('before', before), ('after', after)):
    h2027 = [h for h in store['holidays']
             if h['start_date'] <= '2027-12-31' and h['end_date'] >= '2027-01-01']
    by = {}
    for h in h2027:
        key = '%s/%s' % (h['jurisdiction_id'], h['kind'])
        by[key] = by.get(key, 0) + 1
    print('== holidays %s total %d 2027 %d %s' % (label, len(store['holidays']), len(h2027), by))

split = {'full': 0, 'floor_only': 0, 'shorter': 0, 'unknown': 0}
for v in after['venues'].values():
    if v['lifecycle'] != 'open':
        continue
    pw = (v['fields'].get('programme_windows') or {}).get('value') or {}
    s12 = (pw.get('12') or {}).get('state')
    s8 = (pw.get('8') or {}).get('state')
    if s12 == 'yes':
        split['full'] += 1
    elif s8 == 'yes':
        split['floor_only'] += 1
    elif s12 == 'no' or s8 == 'no':
        split['shorter'] += 1
    else:
        split['unknown'] += 1
print('== access split:', split)
print('== events 2027:', sum(1 for e in after['events'].values()
                            if str((e['fields']['date_range']['value'] or {}).get('end', '')) >= '2027-01-01'),
      'total', len(after['events']))
print('== sources', len(after['sources_consulted']),
      'yield', sum(int(r.get('event_yield') or 0) for r in after['sources_consulted']))
print('== gaps', len(after['declared_gaps']))

scratch = Path('/home/joe/.hermes/profiles/jnr-research/cache/scratch/nyc-r9-scratch.html')
scratch.parent.mkdir(parents=True, exist_ok=True)
page = city_page.render_page(after)
scratch.write_text(page, encoding='utf-8')
print('== rendered scratch', scratch.stat().st_size, 'bytes; maps:', 'maplibre' in page.lower())
scratch.unlink()
print('== scratch deleted:', not scratch.exists())
