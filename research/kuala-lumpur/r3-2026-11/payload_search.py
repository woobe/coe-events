import json
import re
import subprocess
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11')
OUT = BASE / 'captures' / 'events'
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/158.0.0.0 Safari/537.36')


def raw(url):
    proc = subprocess.run(['curl', '-sS', '-L', '--compressed', '-m', '60', '-A', UA,
                           url], capture_output=True, timeout=100)
    body = proc.stdout
    if body[:2] == b'\x1f\x8b':
        import gzip
        try:
            body = gzip.decompress(body)
        except Exception:  # noqa: BLE001
            pass
    return body.decode('utf-8', 'replace')


for name, url in (('miragather-main', 'https://miragather.com/'),
                  ('miragather-side', 'https://miragather.com/?tab=side'),
                  ('miragather-ai', 'https://miragather.com/ai'),
                  ('luma-kl', 'https://lu.ma/kuala-lumpur'),
                  ('aitinkerers-all', 'https://aitinkerers.org/all_cities')):
    text = raw(url)
    (OUT / (name + '-raw.txt')).write_text(text, encoding='utf-8')
    print('== %s %s bytes=%d' % (name, url, len(text)))
    kl = [m.start() for m in re.finditer(r'Kuala Lumpur', text)]
    print('   Kuala Lumpur mentions:', len(kl))
    y27 = [m.start() for m in re.finditer(r'2027', text)]
    print('   2027 mentions:', len(y27))
    for pos in kl[:3]:
        print('   ...%s...' % re.sub(r'\s+', ' ', text[max(0, pos - 300):pos + 300])[:560])
