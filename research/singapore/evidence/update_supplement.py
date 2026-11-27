"""Keep holiday-supplement.json in step with the store's holiday rows."""
import hashlib
import json
from datetime import date
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore/city')
rows = []
for h in STORE['holidays']:
    row = {
        'holiday_name': h['holiday_name'],
        'start_date': h['start_date'],
        'end_date': h['end_date'],
        'day': date.fromisoformat(h['start_date']).strftime('%A'),
        'kind': h['kind'],
        'jurisdiction_id': h['jurisdiction_id'],
        'source_title': h['source_title'],
        'source_url': h['source_url'],
        'source_locator': h['source_locator'],
    }
    if h.get('school_scope'):
        row['note'] = 'Scope: %s.' % h['school_scope']
    rows.append(row)

supp = {
    'jurisdiction_ids': ['SG'],
    'note': ('Singapore holiday layer for the 2027 projection. Public rows from the Ministry of Manpower '
             '2027 table; school rows from the Ministry of Education School Terms and Holidays for 2027 '
             'release of 14 July 2026. Every row is dated by the authority; no row is rule-derived.'),
    'source': {
        'url': 'https://www.mom.gov.sg/employment-practices/public-holidays',
        'title': 'Ministry of Manpower — Public holidays; Ministry of Education — School Terms and Holidays for 2027',
        'edition': 'MOM 2027 table (updated 19 June 2026); MOE release 14 July 2026',
        'accessed_on': CHECKED,
    },
    'holidays': rows,
    'coverage': [
        {'kind': 'public_holiday_coverage', 'jurisdiction_id': 'SG',
         'start_date': '2027-01-01', 'end_date': '2027-12-31', 'verified': True,
         'note': 'Full-year 2027 span; the twelve public rows are the eleven MOM date rows including both Chinese New Year days, plus the 8 February substitution day printed in the MOM sentence and treated as a school public holiday in MOE footnote 3.'},
        {'kind': 'school_holiday_coverage', 'jurisdiction_id': 'SG',
         'start_date': '2027-01-01', 'end_date': '2027-12-31', 'verified': True,
         'note': 'MOE Kindergarten, primary and secondary: four vacations, four scheduled school holidays and three designated days off-in-lieu for schools (9 February, 3 May, 27 December). The 27 December designation falls inside the end-of-year vacation. Pre-university end-of-year vacation differs and is noted on the end-of-year row.'},
    ],
}
p = BASE / 'holiday-supplement.json'
p.write_text(json.dumps(supp, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
sha = hashlib.sha256(p.read_bytes()).hexdigest()
reg = STORE['holiday_registry']
reg['coverage_rows'] = 2
reg['holiday_rows'] = len(rows)
reg['jurisdiction_ids'] = ['SG']
reg['supplement'] = {
    'coverage_rows': 2,
    'holiday_rows': len(rows),
    'jurisdiction_ids': ['SG'],
    'note': 'MOM 2027 public layer plus MOE 2027 school layer; both read on 2026-11-26.',
    'path': p.name,
    'sha256': sha,
}
p2 = BASE / 'city.json'
p2.write_text(json.dumps(STORE, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('supplement', len(rows), 'rows sha', sha[:12], 'store', p2.stat().st_size)
