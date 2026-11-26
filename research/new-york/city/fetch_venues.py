"""R9: fetch every New York venue's operator/listing page, save the raw HTML and a
plain-text rendering, and record status in a fetch report."""
import json, re, subprocess, sys, time, html
from pathlib import Path

ROOT = Path('/home/joe/repo_dev/coe-events')
CITY = ROOT / 'research/new-york/city'
CAP = CITY / 'captures'
CAP.mkdir(exist_ok=True)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0 Safari/537.36")

inv = json.loads((CITY / 'venue-inventory.json').read_text())
sources = {}
for vid, row in inv.items():
    src = (row['source_url'][0] or row['address'][1] or row['coordinates'][1])
    sources[vid] = src
extra = {
    'nyc-12c98ff34e33': ['https://www.nyu.edu/life/campus-resources/kimmel-center/reservable-spaces.html'],
    'nyc-4c6638c43df6': ['https://civichall.org/our-spaces/'],
    'nyc-75c0f7334372': ['https://www.peerspace.com/pages/listings/5c5377f8961209000e6834b0'],
    'nyc-b07f42f9c9bc': ['https://www.peerspace.com/pages/listings/6420fda9464ca6000e043452',
                          'https://www.tagvenue.com/us/rooms/new-york/90459/jay-conference-bryant-park/the-tel-aviv-room'],
    'nyc-ca43f10af68d': ['https://nycseminarcenter.com/Seminar_Room_a/',
                          'https://nycseminarcenter.com/pricing/', 'https://nycseminarcenter.com/terms/'],
    'nyc-lead-advent-hope': ['https://www.adventhope.org/rent'],
    'nyc-lead-bpl-meeting-rooms': ['https://www.bklynlibrary.org/use-the-library/meeting-rooms'],
    'nyc-lead-cuny-gc': ['https://spacerentals.gc.cuny.edu/'],
}
report = {}
for vid, src in sources.items():
    urls = [src] + [u for u in extra.get(vid, []) if u != src]
    for i, url in enumerate(urls):
        slug = vid + ('' if i == 0 else '-%d' % i)
        html_path = CAP / ('venue-%s.html' % slug)
        txt_path = CAP / ('venue-%s.txt' % slug)
        tmp = CAP / ('venue-%s.tmp' % slug)
        proc = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-A', UA,
                               '-o', str(tmp), '-w', '%{http_code} %{size_download}',
                               url], capture_output=True, text=True)
        code, _, size = (proc.stdout.strip() + ' 0').split()[:3]
        raw = tmp.read_bytes() if tmp.exists() else b''
        html_path.write_bytes(raw)
        tmp.unlink(missing_ok=True)
        text = raw.decode('utf-8', 'replace')
        text = re.sub(r'<script\b[^>]*>.*?</script>', ' ', text, flags=re.S | re.I)
        text = re.sub(r'<style\b[^>]*>.*?</style>', ' ', text, flags=re.S | re.I)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = html.unescape(text)
        lines = [' '.join(line.split()) for line in text.splitlines()]
        txt_path.write_text('\n'.join(line for line in lines if line), encoding='utf-8')
        report.setdefault(vid, []).append({'url': url, 'status': int(code),
                                           'bytes': len(raw), 'capture': html_path.name,
                                           'text': txt_path.name})
        print(vid, i, code, len(raw), url, flush=True)
        time.sleep(0.8)
(CITY / 'venue-fetch-report.json').write_text(json.dumps(report, indent=1))
print('done', sum(len(v) for v in report.values()))
