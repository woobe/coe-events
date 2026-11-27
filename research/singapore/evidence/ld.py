import json, re, sys
p = sys.argv[1]
html = open(p, encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S|re.I):
    body = m.group(1).strip()
    try:
        data = json.loads(body)
    except Exception:
        print('LD unparsed:', body[:300]); continue
    print(json.dumps(data, indent=1)[:3500])
