"""R9: capture the holiday authorities (federal, state, city, school)."""
import subprocess, re, html, time
from pathlib import Path

CAP = Path('/home/joe/repo_dev/coe-events/research/new-york/city/captures')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')
TARGETS = [
    ('rev1-opm-2027.html', 'https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/'),
    ('rev1-nys-civil-service-2027.html', 'https://cs.ny.gov/attendance_leave/2027_legal_holidays.cfm'),
    ('rev1-nyc-opa-holiday-pay.html', 'https://www.nyc.gov/site/opa/my-pay/holiday-pay-calendar.page'),
    ('rev1-nycps-2026-2027.html', 'https://www.schools.nyc.gov/calendar/2026-2027-school-year-calendar'),
    ('rev1-nycps-2027-2028.html', 'https://www.schools.nyc.gov/calendar/2027-2028-school-year-calendar'),
    ('rev1-civic-hall-contact.html', 'https://civichall.org/contact-us'),
]
for name, url in TARGETS:
    out = CAP / name
    proc = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-A', UA, '-o', str(out),
                           '-w', '%{http_code} %{size_download}', url],
                          capture_output=True, text=True)
    print(name, proc.stdout.strip(), url, flush=True)
    raw = out.read_bytes() if out.exists() else b''
    text = raw.decode('utf-8', 'replace')
    text = re.sub(r'<script\b[^>]*>.*?</script>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'<style\b[^>]*>.*?</style>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    lines = [' '.join(line.split()) for line in text.splitlines()]
    (CAP / (name.rsplit('.', 1)[0] + '.txt')).write_text(
        '\n'.join(line for line in lines if line), encoding='utf-8')
    time.sleep(1)
