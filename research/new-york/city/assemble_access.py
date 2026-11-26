"""R9: re-derive every New York access window from the operator's published price
table / hire page (opening hours alone are not a hire interval)."""
import json, re
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
RUN = 'run-20261126-nyc-r9'
CHECKED = '2026-11-26'
store = json.loads(STORE.read_text())
access = json.loads((CITY / 'access-blocks.json').read_text())
inv = json.loads((CITY / 'venue-inventory.json').read_text())


def to_min(text):
    m = re.match(r'(\d{1,2}):(\d{2})\s*([ap]m)', text.strip(), re.I)
    if not m:
        return None
    h, mm, ap = int(m.group(1)), int(m.group(2)), m.group(3).lower()
    if ap == 'pm' and h != 12:
        h += 12
    if ap == 'am' and h == 12:
        h = 0
    return h * 60 + mm


def fmt(mins):
    mins %= 24 * 60
    return '%02d:%02d' % (mins // 60, mins % 60)


def covers(start, end, a, b):
    """True when [a,b] lies inside the same-day-or-wrapping span [start,end]."""
    if start is None or end is None:
        return None
    span_end = end if end > start else end + 24 * 60
    return start <= a and b <= span_end


summary = {}
for vid, venue in store['venues'].items():
    if venue['lifecycle'] != 'open':
        continue
    fields = venue['fields']
    rec = access.get(vid) or {}
    block = rec.get('saturday_block')
    row = (fields.get('access_window') or {})
    if block and len(block) >= 5:
        day, s, e, _from, price, unit = block[0], block[1], block[2], block[3], block[4], block[5] if len(block) > 5 else ''
        if s.strip().lower().startswith('open'):
            quote = '%s Open 24 hours from %s %s' % (day, price, unit)
            win = 'Open 24 hours (Saturday)'
            s8 = s12 = 'unknown'
            basis8 = basis12 = (
                'Saturday is printed as "Open 24 hours" with an hourly hire fee. That is an '
                'availability/opening line, not a published hire interval, so neither a '
                '09:00-17:00 nor a 09:00-21:00 booking is evidenced.')
        else:
            quote = '%s %s %s from %s %s' % (day, s.strip(), e.strip(), price, unit)
            smin, emin = to_min(s), to_min(e)
            win = '%s-%s (Saturday)' % (fmt(smin), fmt(emin))
            if 'min. spend' in unit or 'hire fee per session' in unit or 'Per session' in block:
                ok8 = covers(smin, emin, 9 * 60, 17 * 60)
                ok12 = covers(smin, emin, 9 * 60, 21 * 60)
                s8 = 'yes' if ok8 else 'no'
                s12 = 'yes' if ok12 else 'no'
                if ok8 or ok12:
                    s8 = s12 = 'unknown'
                    basis8 = basis12 = (
                        'The Saturday price row is a per-session minimum spend (%s) with no session '
                        'length published, so a continuous 09:00-17:00 or 09:00-21:00 booking is not '
                        'evidenced.' % quote)
                else:
                    basis8 = basis12 = (
                        'The Saturday price row publishes "%s"; the session starts after 09:00 or '
                        'ends before 17:00, so the window is not bookable.' % quote)
            else:
                ok8 = covers(smin, emin, 9 * 60, 17 * 60)
                ok12 = covers(smin, emin, 9 * 60, 21 * 60)
                s8 = 'yes' if ok8 else 'no'
                s12 = 'yes' if ok12 else 'no'
                basis8 = ('The Saturday price table publishes "%s" at an hourly hire fee, which '
                          '%s 09:00-17:00; no maximum booking length is published.'
                          % (quote, 'contains' if ok8 else 'does not contain'))
                basis12 = ('The Saturday price table publishes "%s" at an hourly hire fee, which '
                           '%s 09:00-21:00; no maximum booking length is published.'
                           % (quote, 'contains' if ok12 else 'does not contain'))
        row.update({'value': win, 'quote': quote, 'verified_at': CHECKED, 'run_id': RUN,
                    'source_url': rec.get('source'), 'source_locator':
                    'Pricing details -> Saturday (published hire rate row)',
                    'source_title': (inv[vid]['name'] or '') + ' — operator listing'})
        fields['access_window'] = row
        pw = fields.get('programme_windows') or {}
        pw['8'] = {'state': s8, 'basis': basis8}
        pw['12'] = {'state': s12, 'basis': basis12}
        fields['programme_windows'] = pw
        summary[vid] = (win, s8, s12)

# Seminar Room A: the operator publishes a full-day 09:00-17:00 rate; no 12-hour interval.
vid = 'nyc-ca43f10af68d'
venue = store['venues'][vid]
pw = venue['fields']['programme_windows']
pw['8'] = {'state': 'yes',
           'basis': ('The room page publishes "Full-day 09:00-17:00; evening 18:00-22:00" as its '
                     'bookable rates, so an 09:00-17:00 booking is published.')}
pw['12'] = {'state': 'unknown',
            'basis': ('Full-day (09:00-17:00) and evening (18:00-22:00) are the published rates; '
                      'the pricing page allows bookings of at least four consecutive hours between '
                      '8:00am and 9:00pm but no 12-hour interval is published.')}
summary[vid] = ('Full-day 09:00-17:00 / evening 18:00-22:00', 'yes', 'unknown')

STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
for vid, v in summary.items():
    print(vid, v)
print('12h yes', sum(1 for v in summary.values() if v[2] == 'yes'),
      '8h yes', sum(1 for v in summary.values() if v[1] == 'yes'))
