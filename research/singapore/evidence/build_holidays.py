"""Holiday layers: MOM public 2027 + MOE school 2027."""
from datetime import date

MOM = 'Ministry of Manpower — Public holidays'
MOM_URL = 'https://www.mom.gov.sg/employment-practices/public-holidays'
MOM_CAP = 'captures/mom-public-holidays.txt'
MOM_ED = 'MOM Public Holidays page, 2027 table (page last updated 19 June 2026)'
MOE = 'Ministry of Education — School Terms and Holidays for 2027'
MOE_URL = 'https://www.moe.gov.sg/news/press-releases/20260714-school-terms-and-holidays-for-2027'
MOE_CAP = 'captures/moe-school-terms-2027.txt'
MOE_ED = 'MOE press release 14 July 2026, School Terms and Holidays for 2027'

PUBLIC = [
    ('New Year\'s Day', '2027-01-01', '2027-01-01', 'line 122',
     "New Year's Day 1 January 2027, Friday"),
    ('Chinese New Year', '2027-02-06', '2027-02-06', 'lines 126-127',
     'Chinese New Year 6 February 2027 - 7 February 2027, Saturday - Sunday Monday, 8 February 2027, will be a public holiday if your rest day falls on 7 February 2027.'),
    ('Chinese New Year', '2027-02-07', '2027-02-07', 'lines 126-127',
     'Chinese New Year 6 February 2027 - 7 February 2027, Saturday - Sunday Monday, 8 February 2027, will be a public holiday if your rest day falls on 7 February 2027.'),
    ('Chinese New Year (substitution day)', '2027-02-08', '2027-02-08', 'line 127',
     'Monday, 8 February 2027, will be a public holiday if your rest day falls on 7 February 2027.'),
    ('Hari Raya Puasa', '2027-03-10', '2027-03-10', 'line 130',
     'Hari Raya Puasa 10 March 2027, Wednesday'),
    ('Good Friday', '2027-03-26', '2027-03-26', 'line 133',
     'Good Friday 26 March 2027, Friday'),
    ('Labour Day', '2027-05-01', '2027-05-01', 'line 136',
     'Labour Day 1 May 2027, Saturday'),
    ('Hari Raya Haji', '2027-05-17', '2027-05-17', 'line 139',
     'Hari Raya Haji 17 May 2027, Monday'),
    ('Vesak Day', '2027-05-20', '2027-05-20', 'line 142',
     'Vesak Day 20 May 2027, Thursday'),
    ('National Day', '2027-08-09', '2027-08-09', 'line 145',
     'National Day 9 August 2027, Monday'),
    ('Deepavali', '2027-10-28', '2027-10-28', 'line 148',
     'Deepavali 28 October 2027, Thursday'),
    ('Christmas Day', '2027-12-25', '2027-12-25', 'line 151',
     'Christmas Day 25 December 2027, Saturday'),
]

SCHOOL = [
    ('School vacation between Terms I and II', '2027-03-13', '2027-03-21', 'lines 120-121',
     'Between Terms I & II Sat 13 Mar to Sun 21 Mar',
     'MOE Kindergarten, primary and secondary'),
    ('School vacation between Semesters I and II', '2027-05-29', '2027-06-27', 'lines 122-123',
     'Between Semesters I & II Sat 29 May to Sun 27 Jun',
     'MOE Kindergarten, primary and secondary'),
    ('School vacation between Terms III and IV', '2027-09-04', '2027-09-12', 'lines 124-125',
     'Between Terms III & IV Sat 4 Sep to Sun 12 Sep',
     'MOE Kindergarten, primary and secondary'),
    ('End-of-year school vacation', '2027-11-20', '2027-12-31', 'lines 126-127',
     'At End of School Year Sat 20 Nov to Fri 31 Dec',
     'MOE Kindergarten, primary and secondary; pre-university end-of-year vacation starts 27 November (JC Year 1, MI Year 1 and MI Year 2) per the same release'),
    ("Youth Day (observed school holiday)", '2027-07-05', '2027-07-05', 'lines 141-143',
     'Youth Day *Sun 4 Jul (The following Mon 5 Jul will be a school holiday)',
     'MOE schools'),
    ('Day after National Day', '2027-08-10', '2027-08-10', 'lines 144-145',
     'Day after National Day Tue 10 Aug',
     'MOE schools'),
    ("Teachers' Day", '2027-09-03', '2027-09-03', 'lines 146-147',
     "Teachers' Day Fri 3 Sep",
     'MOE schools'),
    ("Children's Day", '2027-10-08', '2027-10-08', 'lines 148-150',
     "Children's Day (for primary schools and primary sections of full schools only) Fri 8 Oct",
     'Primary schools and primary sections of full schools only'),
    ('Designated day off-in-lieu for schools', '2027-02-09', '2027-02-09', 'line 177',
     'Tuesday, 9 February will be a designated day off-in-lieu for schools (i.e. Schools, including the General Office, Student Care Centres and KCare Centres, will be closed).',
     'Schools, including the General Office, Student Care Centres and KCare Centres (closed)'),
    ('Designated day off-in-lieu for schools', '2027-05-03', '2027-05-03', 'line 178',
     'Monday, 3 May will be a designated day off-in-lieu for schools (i.e. Schools, including the General Office, Student Care Centres and KCare Centres, will be closed).',
     'Schools, including the General Office, Student Care Centres and KCare Centres (closed)'),
    ('Designated day off-in-lieu for schools', '2027-12-27', '2027-12-27', 'line 179',
     'Monday, 27 December will be a designated day off-in-lieu for schools (i.e. Schools, including the General Office, Student Care Centres and KCare Centres, will be closed).',
     'Schools, including the General Office, Student Care Centres and KCare Centres (closed)'),
]

holidays = []
for name, start, end, loc, quote in PUBLIC:
    wd = date.fromisoformat(start).strftime('%A')
    holidays.append({
        'accessed_on': CHECKED,
        'capture': MOM_CAP,
        'derived': False,
        'end_date': end,
        'evidence': {
            'observed_facts': '%s %s (%s).' % (name, start, wd),
            'weekday_basis': 'The weekday is computed from the recorded start date, not copied from the first day of a multi-day holiday.',
        },
        'holiday_name': name,
        'jurisdiction_id': 'SG',
        'kind': 'public_holiday',
        'name_en': name,
        'needs_human_verify': False,
        'observance': 'gazetted',
        'quote': quote,
        'source_edition': MOM_ED,
        'source_locator': loc,
        'source_title': MOM,
        'source_url': MOM_URL,
        'start_date': start,
        'verified': True,
        'weekday': wd,
        'weekday_source': 'computed from start_date',
    })

for name, start, end, loc, quote, scope in SCHOOL:
    wd = date.fromisoformat(start).strftime('%A')
    holidays.append({
        'accessed_on': CHECKED,
        'capture': MOE_CAP,
        'derived': False,
        'end_date': end,
        'evidence': {
            'observed_facts': '%s: %s to %s (%s to %s).' % (name, start, end, wd, date.fromisoformat(end).strftime('%A')),
            'weekday_basis': 'The weekday is computed from the recorded start date. The MOE release prints the weekday for single-day holidays and ranges; computed values agree.',
            'school_scope': scope,
        },
        'holiday_name': name,
        'jurisdiction_id': 'SG',
        'kind': 'school_holiday',
        'name_en': name,
        'needs_human_verify': False,
        'observance': 'school_calendar',
        'quote': quote,
        'school_scope': scope,
        'source_edition': MOE_ED,
        'source_locator': loc,
        'source_title': MOE,
        'source_url': MOE_URL,
        'start_date': start,
        'verified': True,
        'weekday': wd,
        'weekday_source': 'computed from start_date',
    })

for h in holidays:
    if h['start_date'] == '2027-02-08':
        h['observance'] = 'substitution'
        h['evidence']['observed_facts'] = (
            'MOM prints Monday 8 February 2027 as a public holiday where the rest day falls on '
            '7 February 2027; MOE footnote 3 (capture line 177) also treats it as a public holiday '
            'for schools. The public row is conditional and is labelled as a substitution day.')
        h['evidence']['scope_note'] = (
            'Applies where the weekly rest day falls on Sunday 7 February 2027; schools treat it '
            'as a public holiday per the MOE release.')
    if h['holiday_name'] == 'Designated day off-in-lieu for schools':
        h['observance'] = 'school_off_in_lieu'
        if h['start_date'] == '2027-12-27':
            h['evidence']['observed_facts'] += (
                ' Falls inside the end-of-year vacation row (2027-11-20 to 2027-12-31); stored as '
                'the separately printed designated closure, not as an extra vacation day.')
        else:
            h['evidence']['observed_facts'] += (
                ' Falls inside a school term, so it closes schools on a day they would otherwise be open.')

STORE['holidays'] = holidays
STORE['coverage'] = [
    {
        'accessed_on': CHECKED,
        'derived': False,
        'end_date': '2027-12-31',
        'evidence': {
            'observed_facts': 'The 2027 table lists ten public holidays plus the second Chinese New Year day; Monday 8 February 2027 is stored as a substitution row from the MOM sentence that makes it a public holiday where the rest day falls on 7 February 2027. MOE footnote 3 (same capture set) also treats 8 February as a public holiday for schools.',
            'source_role_note': 'Public layer only; school rows are a separate authority.',
        },
        'jurisdiction_id': 'SG',
        'kind': 'public_holiday_coverage',
        'needs_human_verify': False,
        'source_edition': MOM_ED,
        'source_locator': '2027 public holidays table, lines 120-151',
        'source_title': MOM,
        'source_url': MOM_URL,
        'start_date': '2027-01-01',
        'verification_questions': [],
        'verified': True,
    },
    {
        'accessed_on': CHECKED,
        'derived': False,
        'end_date': '2027-12-31',
        'evidence': {
            'observed_facts': 'Four school vacations are stored for MOE Kindergarten, primary and secondary schools, plus the four scheduled school holidays printed in the same release and the three designated days off-in-lieu for schools (9 February, 3 May and 27 December). The 27 December designation falls inside the end-of-year vacation and is recorded as a separately printed closure, not an extra vacation day. Pre-university end-of-year vacation differs: JC Year 1, MI Year 1 and MI Year 2 end on 27 November 2027; JC Year 2 and MI Year 3 end with the GCE A-Level examinations. Those differences are recorded here, not duplicated as overlapping rows.',
            'source_role_note': 'School layer covered: MOE Kindergarten, primary and secondary; pre-university dates differ and are noted, not stored as a second overlapping layer.',
        },
        'jurisdiction_id': 'SG',
        'kind': 'school_holiday_coverage',
        'needs_human_verify': False,
        'source_edition': MOE_ED,
        'source_locator': 'School Vacation 2027 and Scheduled School Holidays 2027, lines 117-179',
        'source_title': MOE,
        'source_url': MOE_URL,
        'start_date': '2027-01-01',
        'verification_questions': [],
        'verified': True,
    },
]

print('holidays', len(holidays), 'public', sum(1 for h in holidays if h['kind'] == 'public_holiday'),
      'school', sum(1 for h in holidays if h['kind'] == 'school_holiday'))
