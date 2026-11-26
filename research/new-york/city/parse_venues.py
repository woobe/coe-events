"""R9: parse the saved Tagvenue/operator pages for address, geo, hire-price intervals,
minimum booking and gallery items."""
import json, re, html
from pathlib import Path

CITY = Path('/home/joe/repo_dev/coe-events/research/new-york/city')
CAP = CITY / 'captures'
report = json.loads((CITY / 'venue-fetch-report.json').read_text())
DAYS = 'Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday'
out = {}

def text_of(path):
    return (CAP / path).read_text(errors='ignore')

for vid, entries in report.items():
    rec = {'pages': entries, 'gallery': [], 'price_rows': [], 'minimum': None,
           'jsonld': [], 'address_lines': []}
    for e in entries:
        if e['status'] != 200 or not e['bytes']:
            continue
        raw = text_of(e['capture'])
        # JSON-LD blocks
        for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', raw, re.S):
            body = m.group(1).strip()
            try:
                rec['jsonld'].append(json.loads(body))
            except Exception:
                pass
        # gallery items
        for m in re.finditer(r'data-gallery-items="([^"]+)"', raw):
            try:
                items = json.loads(html.unescape(m.group(1)))
            except Exception:
                continue
            for it in items:
                if it.get('src'):
                    rec['gallery'].append({k: it.get(k) for k in
                                           ('src', 'alt', 'caption', 'category', 'width', 'height')})
        txt = text_of(e['text'])
        for m in re.finditer(r'(%s)\s+(\d{1,2}:\d{2}\s*[ap]m)\s*[–-]\s*(\d{1,2}:\d{2}\s*[ap]m)[^A-Z]{0,40}?(?:from)?' % DAYS, txt):
            row = m.group(0)
            if row not in rec['price_rows']:
                rec['price_rows'].append(row)
        mm = re.search(r'Minimum booking duration:\s*(\d+)\s*(hour|hours|day|days)', txt)
        if mm:
            rec['minimum'] = mm.group(0)
        for line in txt.splitlines():
            if re.search(r'\b\d{1,4}[A-Z]?\s+(West|East|W|E)\s+\d{1,3}(st|nd|rd|th)\b', line) or \
               re.search(r'\b\d{2,4}-\d{2}\s+\w+\s+(Street|Avenue|Road)\b', line) or \
               re.search(r'\b\d{1,4}\s+(Broadway|Madison Avenue|Lafayette Street|Bogart Street|Times Square)\b', line):
                if len(line) < 200 and line not in rec['address_lines']:
                    rec['address_lines'].append(line)
    out[vid] = rec

(CITY / 'venue-pages.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
for vid, rec in out.items():
    addr = None
    for block in rec['jsonld']:
        blocks = block if isinstance(block, list) else [block]
        for b in blocks:
            if not isinstance(b, dict):
                continue
            a = b.get('address')
            if isinstance(a, dict) and a.get('streetAddress'):
                addr = a
                geo = b.get('geo') or {}
                name = b.get('name')
                hours = b.get('openingHoursSpecification')
                break
        if addr:
            break
    print(vid, '|', name if addr else 'NO-JSONLD')
    print('   addr:', addr)
    print('   geo:', geo if addr else None, '| hours:', json.dumps(hours)[:120] if addr else None)
    print('   price:', rec['price_rows'][:6], '| min:', rec['minimum'], '| gallery:', len(rec['gallery']))
    print('   addrlines:', rec['address_lines'][:3])
