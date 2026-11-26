"""R9: rebuild the New York holiday layers from the captured authorities, recompute
weekdays in code, and keep federal, state, city and school scopes separate."""
import json, hashlib, datetime
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
STORE = CITY / 'city.json'
SUPP = CITY / 'holiday-supplement.json'
RUN = 'run-20261126-nyc-r9'
CHECKED = '2026-11-26'
store = json.loads(STORE.read_text())
supp = json.loads(SUPP.read_text())

OPA = 'https://www.nyc.gov/assets/opa/downloads/pdf/three-year-calendar-25-26-27.pdf'
PSB = 'https://www.nyc.gov/assets/dcas/downloads/pdf/reports/440_2.pdf'
NYS = 'https://cs.ny.gov/attendance_leave/2027_legal_holidays.cfm'
OPM = 'https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/'
NYCPS = 'https://www.schools.nyc.gov/calendar/2026-2027-school-year-calendar'
GCL = 'https://newyork.public.law/laws/n.y._general_construction_law_section_24'

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def weekday_of(datestr):
    y, m, d = (int(x) for x in datestr.split('-'))
    return WEEKDAYS[datetime.date(y, m, d).weekday()]


def norm(row):
    row['start_date'] = str(row['start_date'])
    row['end_date'] = str(row['end_date'])
    row['weekday'] = weekday_of(row['start_date'])
    row['weekday_source'] = 'computed in code from start_date (2026-11-26)'
    return row


def add(rows, row):
    for existing in rows:
        if (existing.get('jurisdiction_id') == row['jurisdiction_id']
                and existing.get('kind') == row['kind']
                and existing.get('start_date') == row['start_date']
                and existing.get('end_date') == row['end_date']):
            return False
    rows.append(row)
    return True


holidays = store['holidays']
for h in holidays:
    norm(h)

# --- city scope: Lincoln's Birthday is the 13th paid holiday and a floating day ---
city_lincoln = {
    'accessed_on': CHECKED, 'capture': 'captures/rev1-nyc-opa-three-year.pdf',
    'end_date': '2027-02-12', 'start_date': '2027-02-12',
    'evidence': {'observed_facts': (
        'OPA 2025-2027 payroll calendar, 2027 list: "Feb. 12 Lincoln\u2019s Birthday*"; DCAS PSB '
        '440-2 lists Lincoln\u2019s Birthday as February 12 "(Floating Holiday)" and limits it to '
        'employees hired before 7/1/2004, with the day taken at the employee\u2019s discretion.')},
    'holiday_name': "Lincoln's Birthday", 'jurisdiction_id': 'US-NY:nyc',
    'kind': 'public_holiday', 'needs_human_verify': True,
    'observance': 'floating', 'eligible_only': True,
    'note': ('Floating city holiday, not a universal office closure: eligible employees choose the '
             'day; facilities normally closed on Lincoln\u2019s Birthday observe 12 February.'),
    'source_edition': '2025-2027 Holiday and Pay Calendar (FISA/OPA)',
    'source_locator': '2027 Payroll Holiday list: "Feb. 12 Lincoln\u2019s Birthday*"',
    'source_title': 'NYC Office of Payroll Administration \u2014 2025-2027 Holiday and Pay Calendar',
    'source_url': OPA, 'verified': True,
}
add(holidays, city_lincoln)

# city rows now cite OPA + PSB 440-2
for h in holidays:
    if h.get('jurisdiction_id') == 'US-NY:nyc':
        h['source_url'] = OPA
        h['source_edition'] = '2025-2027 Holiday and Pay Calendar (FISA/OPA)'
        h['source_title'] = ('NYC Office of Payroll Administration \u2014 2025-2027 Holiday and Pay '
                             'Calendar')
        h['needs_human_verify'] = False
        h['verified'] = True
        h['accessed_on'] = CHECKED
        h['capture'] = 'captures/rev1-nyc-opa-three-year.pdf'
        h['source_locator'] = '2027 Payroll Holiday list row for ' + h['holiday_name']
        h['evidence'] = {'observed_facts': (
            'OPA 2027 Payroll Holiday list prints "%s"; DCAS PSB 440-2 fixes the observance rule '
            '(Saturday to the preceding Friday, Sunday to the following Monday).'
            % h['holiday_name'])}

# --- state scope: re-read on 2026-11-26, page verified ---
for h in holidays:
    if h.get('jurisdiction_id') == 'US-NY':
        h['accessed_on'] = CHECKED
        h['verified'] = True
        h['needs_human_verify'] = False
        h['source_url'] = NYS
        h['capture'] = 'captures/rev1-nys-civil-service-2027.txt'
        h['source_locator'] = '2027 Legal Holidays table row: ' + h['holiday_name']

# --- school scope: NYCPS 2026-2027 calendar ---
school = [
    ('2027-01-18', '2027-01-18', 'Rev. Dr. Martin Luther King Jr. Day',
     'January 18 Monday Rev. Dr. Martin Luther King Jr. Day, schools closed'),
    ('2027-03-09', '2027-03-09', 'Eid al-Fitr',
     'March 9 Tuesday Eid al-Fitr, schools closed'),
    ('2027-03-26', '2027-03-26', 'Good Friday',
     'March 26 Friday Good Friday, schools closed'),
    ('2027-05-17', '2027-05-17', 'Eid al-Adha',
     'May 17 Monday Eid al-Adha, schools closed'),
    ('2027-05-31', '2027-05-31', 'Memorial Day',
     'May 31 Monday Memorial Day, schools closed'),
    ('2027-06-10', '2027-06-10', "Anniversary Day/Chancellor's Conference Day",
     'June 10 Thursday Anniversary Day/Chancellor\u2019s Conference Day for staff development; students do not attend school'),
]
for start, end, name, line in school:
    add(holidays, {
        'accessed_on': CHECKED, 'capture': 'captures/rev1-nycps-2026-2027.txt',
        'end_date': end, 'start_date': start,
        'evidence': {'observed_facts': '2026-2027 School Year Calendar, 2027 row: ' + line},
        'holiday_name': name, 'jurisdiction_id': 'US-NY:nycps', 'kind': 'school_holiday',
        'needs_human_verify': False, 'observance': 'actual',
        'source_edition': '2026-2027 School Year Calendar (NYCPS)',
        'source_locator': '2026-2027 School Year Calendar: ' + line,
        'source_title': 'NYC Public Schools \u2014 2026-2027 School Year Calendar',
        'source_url': NYCPS, 'verified': True})

holidays.sort(key=lambda h: (h['start_date'], h['jurisdiction_id']))
store['holidays'] = [norm(h) for h in holidays]

# --- coverage ---
coverage = []
for row in store['coverage']:
    jid = row['jurisdiction_id']
    if jid == 'US':
        row.update({'accessed_on': CHECKED, 'verified': True, 'capture': 'captures/rev1-opm-2027.txt',
                    'source_url': OPM})
    elif jid == 'US-NY':
        row.update({'accessed_on': CHECKED, 'verified': True, 'needs_human_verify': False,
                    'capture': 'captures/rev1-nys-civil-service-2027.txt',
                    'source_url': NYS,
                    'evidence': {'observed_facts': (
                        'State table re-read 2026-11-26 in full; General Construction Law \u00a724 '
                        'read at newyork.public.law for the statutory list (it includes Flag Day, '
                        'which is not a closure). State scope only: not every employer closes.')}})
    elif jid == 'US-NY:nyc':
        row.update({'accessed_on': CHECKED, 'verified': True, 'needs_human_verify': False,
                    'capture': 'captures/rev1-nyc-opa-three-year.pdf',
                    'source_edition': '2025-2027 Holiday and Pay Calendar (FISA/OPA)',
                    'source_title': 'NYC Office of Payroll Administration \u2014 2025-2027 Holiday and Pay Calendar',
                    'source_url': OPA,
                    'source_locator': '2027 Payroll Holiday list, 14 rows',
                    'evidence': {'observed_facts': (
                        'The OPA three-year calendar prints 14 city holiday rows for 2027 '
                        '(including the floating Lincoln\u2019s Birthday). DCAS PSB 440-2 governs '
                        'eligibility and the Saturday/Sunday shift. City-employee scope, not a '
                        'mayoral proclamation of every office closure.')}})
    elif jid == 'US-NY:nycps':
        row.update({'accessed_on': CHECKED, 'verified': True,
                    'capture': 'captures/rev1-nycps-2026-2027.txt',
                    'evidence': {'observed_facts': (
                        'Official 2026-2027 calendar re-read 2026-11-26: eight 2027 closure rows '
                        'from 18 January to 28 June, which is the last day of school. The 2027-2028 '
                        'edition is not published: schools.nyc.gov/calendar/2027-2028-school-year-calendar '
                        'returned HTTP 404 on 2026-11-26, so 2027-06-29 onward is uncovered.')}})
    coverage.append(row)
store['coverage'] = coverage

# --- registry counts ---
reg = store['holiday_registry']
reg['holiday_rows'] = len(store['holidays'])
reg['coverage_rows'] = len(store['coverage'])
reg['projection_year'] = 2027

# --- supplement: city rows and counts kept in step, digest refreshed ---
supp_rows = supp['holidays']
for h in supp_rows:
    norm(h)
for h in supp_rows:
    if h.get('jurisdiction_id') == 'US-NY:nyc':
        h['source_url'] = OPA
        h['source_edition'] = '2025-2027 Holiday and Pay Calendar (FISA/OPA)'
        h['source_title'] = 'NYC Office of Payroll Administration \u2014 2025-2027 Holiday and Pay Calendar'
        h['needs_human_verify'] = False
        h['verified'] = True
        h['accessed_on'] = CHECKED
        h['capture'] = 'captures/rev1-nyc-opa-three-year.pdf'
add(supp_rows, dict(city_lincoln))
supp_rows.sort(key=lambda h: (h['start_date'], h['jurisdiction_id']))
supp['checked_on'] = CHECKED
supp['run_id'] = RUN
supp['coverage'] = [r for r in store['coverage'] if r['jurisdiction_id'] in ('US-NY', 'US-NY:nyc')]
SUPP.write_text(json.dumps(supp, indent=1, ensure_ascii=False))
digest = hashlib.sha256(SUPP.read_bytes()).hexdigest()
reg['supplement']['sha256'] = digest
reg['supplement']['holiday_rows'] = len(supp_rows)
reg['supplement']['coverage_rows'] = len(supp['coverage'])
reg['supplement']['note'] = ('New York State and New York City public-holiday scopes, both re-read '
                             '2026-11-26. State rows from the Civil Service 2027 table; city rows from '
                             'the OPA 2025-2027 payroll calendar with DCAS PSB 440-2, including the '
                             'floating Lincoln\u2019s Birthday row.')

STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False))
print('holiday rows', len(store['holidays']), 'coverage', len(store['coverage']),
      'supplement rows', len(supp_rows), 'digest', digest[:12])
for h in store['holidays']:
    if h['start_date'] >= '2027-01-01' and h['end_date'] <= '2027-12-31':
        print(h['jurisdiction_id'], h['kind'], h['start_date'], h['end_date'], h['weekday'], h['holiday_name'])
