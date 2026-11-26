import json
from pathlib import Path
from collections import Counter
BASE = Path.home() / 'repo_dev/coe-events/research/montreal/city'
pre = json.loads((BASE / 'city.pre-r2.json').read_text(encoding='utf-8'))
post = json.loads((BASE / 'city.json').read_text(encoding='utf-8'))

def field(v, k):
    return (v['fields'].get(k) or {}).get('value')

report = {
    'schema_version': 'city-loss-report/1',
    'run_id': 'run-20261126-mtl-r2',
    'city_slug': post['city_slug'],
    'checked_on': '2026-11-26',
    'pre_store': 'research/montreal/city/city.pre-r2.json',
    'post_store': 'research/montreal/city/city.json',
}

# ---- venues: a join, not a count ----
pre_ids, post_ids = set(pre['venues']), set(post['venues'])
venue_rows, field_changes = [], []
for vid in sorted(pre_ids | post_ids):
    a, b = pre['venues'].get(vid), post['venues'].get(vid)
    if a and b:
        pa, pb = set(a['fields']), set(b['fields'])
        changed = []
        for k in sorted(pa & pb):
            if field(a, k) != field(b, k):
                changed.append({'field': k, 'pre': field(a, k), 'post': field(b, k)})
                field_changes.append({'venue_id': vid, 'field': k})
        grown = sorted(pb - pa)
        shrunk = sorted(pa - pb)
        venue_rows.append({
            'venue_id': vid,
            'legacy_slug': (a.get('legacy_slug') or a.get('slug') or vid),
            'disposition': 'retained',
            'fields_changed': len(changed),
            'fields_added': grown,
            'fields_lost': shrunk,
        })
        # keep the biggest changes for review, per venue
        for c in changed:
            c['venue_id'] = vid
        report.setdefault('venue_field_changes', []).extend(changed)
    elif a and not b:
        venue_rows.append({'venue_id': vid, 'disposition': 'dropped'})
    else:
        venue_rows.append({'venue_id': vid, 'disposition': 'added'})
report['venues'] = venue_rows
report['venue_counts'] = {
    'pre': len(pre_ids), 'post': len(post_ids),
    'retained': sum(r['disposition'] == 'retained' for r in venue_rows),
    'dropped': sum(r['disposition'] == 'dropped' for r in venue_rows),
    'added': sum(r['disposition'] == 'added' for r in venue_rows),
}

# ---- photos: the 48 inherited withheld URL records, venue -> url pairs ----
pre_photos = {}
for vid, recs in pre['photos'].items():
    for p in recs:
        if p.get('url') and p.get('withheld'):
            pre_photos.setdefault((vid, p['url']), p)
post_lookup = {}
for vid, recs in post['photos'].items():
    for p in recs:
        post_lookup.setdefault((vid, p.get('url')), []).append(p)
photo_rows = []
for (vid, url), p in pre_photos.items():
    hits = post_lookup.get((vid, url))
    if not hits:
        disp = 'dropped'
    elif any(not h.get('withheld') for h in hits):
        disp = 'cleared'
    else:
        disp = 'still_withheld'
    photo_rows.append({
        'venue_id': vid, 'url': url, 'disposition': disp,
        'reason': (hits[0].get('rights_note') if hits else
                   'platform placeholder default_space.jpg shows no venue; removed rather than carried'),
    })
report['inherited_withheld_photos'] = photo_rows
report['inherited_withheld_photo_counts'] = dict(Counter(r['disposition'] for r in photo_rows))
report['photo_counts'] = {
    'pre_withheld_url_records': len(pre_photos),
    'pre_venues_with_withheld': len({v for v, _ in pre_photos}),
    'post_records': sum(len(r) for r in post['photos'].values()),
    'post_withheld': sum(1 for r in post['photos'].values() for p in r if p.get('withheld')),
    'post_cleared': sum(1 for r in post['photos'].values() for p in r
                        if not p.get('withheld') and str(p.get('url') or '').startswith('http')),
}

# ---- events ----
pre_ev = set(pre['events']); post_ev = set(post['events'])
report['events'] = {
    'pre': sorted(pre_ev), 'post': sorted(post_ev),
    'retained': sorted(pre_ev & post_ev),
    'dropped': sorted(pre_ev - post_ev),
    'added': sorted(post_ev - pre_ev),
}

# ---- holidays ----
def hkey(h):
    return (h['jurisdiction_id'], h['kind'], h['start_date'], h['end_date'],
            h.get('holiday_name') or h.get('name') or '')
pre_h = Counter(hkey(h) for h in pre['holidays'])
post_h = Counter(hkey(h) for h in post['holidays'])
report['holidays'] = {
    'pre': len(pre['holidays']), 'post': len(post['holidays']),
    'retained': sum((pre_h & post_h).values()),
    'removed': [list(k) for k in (pre_h - post_h)],
    'added': [list(k) for k in (post_h - pre_h)],
}

# ---- everything else ----
report['top_level'] = {
    'declared_gaps': {'pre': len(pre.get('declared_gaps') or []), 'post': len(post.get('declared_gaps') or [])},
    'sources_consulted': {'pre': len(pre.get('sources_consulted') or []), 'post': len(post.get('sources_consulted') or [])},
    'coverage': {'pre': len(pre.get('coverage') or []), 'post': len(post.get('coverage') or [])},
    'communities': {'pre': len(pre.get('communities') or []), 'post': len(post.get('communities') or [])},
    'refresh_revision': {'pre': pre.get('refresh_revision'), 'post': post.get('refresh_revision')},
}
report['unexplained'] = [
    r for r in venue_rows if r['disposition'] == 'retained' and r['fields_lost']
]

(BASE / 'r2-loss-report.json').write_text(
    json.dumps(report, indent=1, ensure_ascii=False), encoding='utf-8')
print('venue_counts', report['venue_counts'])
print('venue fields changed total', len(report['venue_field_changes']))
print('inherited withheld', report['inherited_withheld_photo_counts'])
print('photo_counts', report['photo_counts'])
print('events', report['events'])
print('holidays', {k: v for k, v in report['holidays'].items() if k != 'added'})
print('holidays added', len(report['holidays']['added']))
print('unexplained field losses', len(report['unexplained']))
print('top_level', report['top_level'])
