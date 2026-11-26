"""R9: re-fetch every stored New York event's organiser page."""
import json, re, subprocess, time, html
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
CAP = CITY / 'captures'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')
rows = json.loads((CITY / 'event-inventory.json').read_text())
report = {}
for row in rows:
    url = row['urls'][0]
    slug = row['event_id']
    out = CAP / ('event-%s.html' % slug)
    proc = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-A', UA, '-o', str(out),
                           '-w', '%{http_code} %{size_download}', url],
                          capture_output=True, text=True)
    code = proc.stdout.split()[0] if proc.stdout.strip() else '000'
    size = int(proc.stdout.split()[1]) if len(proc.stdout.split()) > 1 else 0
    raw = out.read_text(errors='ignore') if out.exists() else ''
    text = re.sub(r'<script\b[^>]*>.*?</script>', ' ', raw, flags=re.S | re.I)
    text = re.sub(r'<style\b[^>]*>.*?</style>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    flat = ' '.join(text.split())
    (CAP / ('event-%s.txt' % slug)).write_text(flat, encoding='utf-8')
    dates = sorted(set(re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}(?:[–-]\d{1,2})?,?\s+2027', flat)))
    iso = sorted(set(re.findall(r'2027-\d{2}-\d{2}', raw)))
    report[slug] = {'url': url, 'status': int(code), 'bytes': size, 'title': row['name'],
                    'printed_2027': dates[:8], 'iso_2027': iso[:8],
                    'has_2027': '2027' in flat}
    print(slug, code, size, '| dates:', dates[:4], '| iso:', iso[:4], '| 2027:', '2027' in flat, flush=True)
    time.sleep(0.6)
(CITY / 'event-fetch-report.json').write_text(json.dumps(report, indent=1))
