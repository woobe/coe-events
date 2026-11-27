"""Before/after disposition ledger for the access and photo losses."""
import json
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore')
old = json.load(open(BASE / 'evidence' / 'city.pre-r8.json'))
new = json.load(open(BASE / 'city' / 'city.json'))


def f(v, k):
    return ((v.get('fields') or {}).get(k) or {}).get('value')


access = []
for vid in sorted(old['venues']):
    ov, nv = old['venues'][vid], new['venues'][vid]
    ow = (f(ov, 'programme_windows') or {})
    nw = (f(nv, 'programme_windows') or {})
    o12 = (ow.get('12') or {}).get('state')
    n12 = (nw.get('12') or {}).get('state')
    o8 = (ow.get('8') or {}).get('state')
    n8 = (nw.get('8') or {}).get('state')
    reason = None
    if o12 == 'yes' and n12 != 'yes':
        reason = ('The 2026-11-24 row treated the listing day span as a 12-hour window; '
                  'revision 1 keeps only a continuously published 09:00-21:00 hire block. '
                  'The captured page publishes a per-day hourly tariff, not that block.')
        if vid in ('sg-31b594bd4607',):
            reason = 'The operator publishes two weekend sessions with a 16:00-17:00 gap.'
        if vid == 'sg-9d1a91764baf':
            reason = 'The full-day session ends at 17:30; the evening is a separate 18:00-22:00 block.'
        if vid == 'sg-bea2d52eb16e':
            reason = 'The package is a 10-hour hire with 12 hours of access including setup and teardown, not a 09:00-21:00 event block.'
    access.append({'venue_id': vid, 'name': f(nv, 'display_name'),
                   'before': {'8': o8, '12': o12}, 'after': {'8': n8, '12': n12},
                   'window': f(nv, 'access_window'), 'loss_reason': reason})

photos = []
for vid in sorted(old['venues']):
    op = old.get('photos', {}).get(vid, [])
    np = new.get('photos', {}).get(vid, [])
    ocount = len({p.get('url') for p in op if p.get('url') and not p.get('withheld')})
    ncount = len({p.get('url') for p in np if p.get('url') and not p.get('withheld')})
    photos.append({'venue_id': vid, 'name': f(new['venues'][vid], 'display_name'),
                   'before': ocount, 'after': ncount,
                   'withheld_reason': (np[0].get('placement_proof') if np and np[0].get('withheld') else None),
                   'views': sorted({p.get('view_kind') for p in np if p.get('url') and not p.get('withheld')})})

json.dump({'access': access,
           'access_summary': {
               'before_12_yes': sum(1 for a in access if a['before']['12'] == 'yes'),
               'after_12_yes': sum(1 for a in access if a['after']['12'] == 'yes'),
               'after_full': sum(1 for a in access if a['after']['12'] == 'yes'),
               'after_floor_only': sum(1 for a in access if a['after']['8'] == 'yes' and a['after']['12'] != 'yes'),
               'after_shorter': sum(1 for a in access if a['after']['8'] == 'no' and a['after']['12'] == 'no'),
               'after_unknown': sum(1 for a in access if a['after']['8'] == 'unknown' and a['after']['12'] == 'unknown'),
           }},
          open(BASE / 'evidence' / 'access-dispositions.json', 'w'), indent=1)
json.dump({'photos': photos,
           'summary': {
               'before_1plus': sum(1 for p in photos if p['before'] >= 1),
               'before_4plus': sum(1 for p in photos if p['before'] >= 4),
               'before_none': sum(1 for p in photos if p['before'] == 0),
               'after_1plus': sum(1 for p in photos if p['after'] >= 1),
               'after_4plus': sum(1 for p in photos if p['after'] >= 4),
               'after_none': sum(1 for p in photos if p['after'] == 0),
               'after_room_views': sum(1 for recs in new['photos'].values()
                                      for r in recs if r.get('url') and not r.get('withheld')
                                      and r.get('room_specific')),
               'after_fallback_views': sum(1 for recs in new['photos'].values()
                                           for r in recs if r.get('url') and not r.get('withheld')
                                           and not r.get('room_specific')),
               'rights_after': dict(sorted({
                   basis: sum(1 for recs in new['photos'].values()
                              for r in recs if r.get('url') and not r.get('withheld')
                              and (r.get('rights_basis') or 'none') == basis)
                   for basis in {r.get('rights_basis') or 'none'
                                 for recs in new['photos'].values()
                                 for r in recs if r.get('url') and not r.get('withheld')}}.items())),
               'rights_before': dict(sorted({
                   basis: sum(1 for recs in old['photos'].values()
                              for r in recs if r.get('url') and not r.get('withheld')
                              and (r.get('rights_basis') or 'none') == basis)
                   for basis in {r.get('rights_basis') or 'none'
                                 for recs in old['photos'].values()
                                 for r in recs if r.get('url') and not r.get('withheld')}}.items())),
           }},
          open(BASE / 'evidence' / 'photo-dispositions.json', 'w'), indent=1)
print(json.dumps(json.load(open(BASE / 'evidence' / 'access-dispositions.json'))['access_summary'], indent=1))
print(json.dumps(json.load(open(BASE / 'evidence' / 'photo-dispositions.json'))['summary'], indent=1))
