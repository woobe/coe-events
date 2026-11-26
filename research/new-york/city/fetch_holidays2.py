"""R9: capture DCAS PSB 440-2 (Paid Holidays) and NY General Construction Law §24."""
import subprocess, re, html, time
from pathlib import Path

CAP = Path('/home/joe/repo_dev/coe-events/research/new-york/city/captures')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')
TARGETS = [
    ('rev1-dcas-psb-440-2.pdf', 'https://www.nyc.gov/assets/dcas/downloads/pdf/reports/440_2.pdf'),
    ('rev1-gcl-24.html', 'https://www.nysenate.gov/legislation/laws/GCN/24'),
    ('rev1-nyc-dcas-psb-index.html', 'https://www.nyc.gov/site/dcas/reports/personnel-services-bulletins.page'),
]
for name, url in TARGETS:
    out = CAP / name
    proc = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-A', UA, '-o', str(out),
                           '-w', '%{http_code} %{size_download}', url],
                          capture_output=True, text=True)
    print(name, proc.stdout.strip(), flush=True)
    if name.endswith('.html') and out.exists():
        text = out.read_text(errors='ignore')
        text = re.sub(r'<script\b[^>]*>.*?</script>', ' ', text, flags=re.S | re.I)
        text = re.sub(r'<style\b[^>]*>.*?</style>', ' ', text, flags=re.S | re.I)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = html.unescape(text)
        lines = [' '.join(line.split()) for line in text.splitlines()]
        (CAP / (name.rsplit('.', 1)[0] + '.txt')).write_text(
            '\n'.join(line for line in lines if line), encoding='utf-8')
    time.sleep(1)
