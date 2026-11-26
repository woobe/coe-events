"""R9: event sweep lanes (Luma, Meetup, Eventbrite, MiraGather, AI Tinkerers)."""
import subprocess, re, html, time, json
from pathlib import Path

CAP = Path('/home/joe/repo_dev/coe-events/research/new-york/city/captures')
CAP.mkdir(exist_ok=True)
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
      '(KHTML, like Gecko) Version/17.0 Safari/605.1.15')

LANES = [
    ('lane-luma-nyc', 'https://lu.ma/nyc'),
    ('lane-luma-newyork', 'https://lu.ma/new-york'),
    ('lane-luma-nyc-alias', 'https://luma.com/new-york-city'),
    ('lane-luma-genai', 'https://luma.com/genai-ny'),
    ('lane-luma-aisalon', 'https://luma.com/AI-Salon-NewYork'),
    ('lane-luma-creativeai', 'https://luma.com/nyc-creative-ai'),
    ('lane-meetup-ai', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=ai'),
    ('lane-meetup-ml', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=machine%20learning'),
    ('lane-meetup-ds', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=data%20science'),
    ('lane-meetup-web3', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=web3'),
    ('lane-meetup-crypto', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=crypto'),
    ('lane-meetup-blockchain', 'https://www.meetup.com/find/?location=us--ny--New%20York&keywords=blockchain'),
    ('lane-eventbrite-ai', 'https://www.eventbrite.com/d/ny--new-york/ai/'),
    ('lane-eventbrite-ml', 'https://www.eventbrite.com/d/ny--new-york/machine-learning/'),
    ('lane-eventbrite-ds', 'https://www.eventbrite.com/d/ny--new-york/data-science/'),
    ('lane-eventbrite-web3', 'https://www.eventbrite.com/d/ny--new-york/web3/'),
    ('lane-eventbrite-crypto', 'https://www.eventbrite.com/d/ny--new-york/crypto/'),
    ('lane-eventbrite-blockchain', 'https://www.eventbrite.com/d/ny--new-york/blockchain/'),
    ('lane-miragather-main', 'https://miragather.com/'),
    ('lane-miragather-side', 'https://miragather.com/?tab=side'),
    ('lane-miragather-ai', 'https://miragather.com/ai'),
    ('lane-aitinkerers', 'https://aitinkerers.org/all_cities'),
    ('lane-chainalysis-ical', 'https://events.chainalysis.com/Links-2027?calendar-iCal&u=677a5829ece36522'),
]
out = {}
for name, url in LANES:
    p = CAP / (name + '.html')
    proc = subprocess.run(['curl', '-sS', '-L', '-m', '60', '-A', UA, '-o', str(p),
                           '-w', '%{http_code} %{size_download}', url],
                          capture_output=True, text=True)
    bits = (proc.stdout.strip() + ' 0').split()
    raw = p.read_text(errors='ignore') if p.exists() else ''
    text = re.sub(r'<script\b[^>]*>.*?</script>', ' ', raw, flags=re.S | re.I)
    text = re.sub(r'<style\b[^>]*>.*?</style>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    flat = ' '.join(text.split())
    (CAP / (name + '.txt')).write_text(flat, encoding='utf-8')
    n2027 = len(re.findall(r'2027', flat))
    out[name] = {'url': url, 'status': int(bits[0]), 'bytes': int(bits[1]),
                 'text_chars': len(flat), 'mentions_2027': n2027}
    print(name, bits[0], bits[1], 'text', len(flat), '2027x', n2027, flush=True)
    time.sleep(1.2)
(CITY := Path('/home/joe/repo_dev/coe-events/research/new-york/city')) / 'lane-report.json'
(CITY / 'lane-report.json').write_text(json.dumps(out, indent=1))
