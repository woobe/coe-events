"""Capture K2 primary sources and an HTTP ledger (run from any directory)."""
import concurrent.futures
import json
import subprocess
from pathlib import Path

HOME = Path(__file__).resolve().parent
OUT = HOME.parent / '2027/captures/k2'
BASE = json.loads((HOME / 'preimage/city.json').read_text())
SCOPES = {'US-CA:sfusd', 'GB-SCT:edinburgh', 'CA-BC:vsb', 'DE-BE', 'IE'}
URLS = {
    'notices.html': 'https://www.city.kyoto.lg.jp/kyoiku/category/179-3-3-0-0-0-0-0-0-0.html',
    'instruction.html': 'https://www.city.kyoto.lg.jp/kyoiku/soshiki/29-2-9-0-0.html',
    'cms.html': 'https://cms.edu.city.kyoto.jp/kyoto',
    'area-schedule.html': 'https://cms.edu.city.kyoto.jp/kyoto/area_schedule',
    'directory.html': 'https://www.edu.city.kyoto.jp/hp/',
    'directory-http.html': 'http://www.edu.city.kyoto.jp/hp/',
    'city-hours.html': 'https://www.city.kyoto.lg.jp/bunshi/page/0000003123.html',
    'city-code-index.html': 'https://en3-jg.d1-law.com/kyoto/d1w_reiki/index_003.html',
    'city-code.html': 'https://en3-jg.d1-law.com/kyoto/d1w_reiki/H401901010005/H401901010005_j.html',
    'pref-office.html': 'https://www.pref.kyoto.jp/reiki/reiki_honbun/a300RG00000020.html',
    'pref-school.html': 'https://www.pref.kyoto.jp/reiki/reiki_honbun/a300RG00000836.html',
    'city-high.pdf': 'https://cms.edu.city.kyoto.jp/300308/download/document/17733251',
}
for scope in sorted(SCOPES):
    urls = sorted({r['source_url'] for r in BASE['holidays'] if (r['jurisdiction_id'], r['kind']) == (scope, 'school_holiday')})
    for i, url in enumerate(urls, 1):
        ext = 'ics' if url.endswith('.ics') else 'pdf' if url.endswith('.pdf') or '/downloads/file/' in url else 'html'
        URLS[f'{scope.replace(":", "-")}-{i}.{ext}'] = url


def fetch(item):
    name, url = item
    dest = OUT / name
    res = subprocess.run(['curl', '-fsSL', '--compressed', '--max-time', '25', '-o', str(dest), '-w', '%{http_code}\t%{url_effective}', url], capture_output=True, text=True)
    if res.returncode:
        dest.unlink(missing_ok=True)
    return f'{name}\t{url}\t{res.stdout}\t{res.returncode}'


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        output = '\n'.join(pool.map(fetch, URLS.items()))
    (OUT / 'http.tsv').write_text('capture\trequested_url\tstatus\teffective_url\tcurl_exit\n' + output + '\n')
    print(output)
