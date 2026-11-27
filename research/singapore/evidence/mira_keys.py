import json, re
from pathlib import Path
p = Path('research/singapore/city/captures/ev-mira-main.html')
html = p.read_text(encoding='utf-8', errors='replace')
m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
data = json.loads(m.group(1))
pp = data['props']['pageProps']
print('pageProps keys:', list(pp))
for k, v in pp.items():
    if isinstance(v, list):
        print(' ', k, 'list', len(v), 'first keys:', list(v[0])[:20] if v and isinstance(v[0], dict) else '')
    elif isinstance(v, dict):
        print(' ', k, 'dict', list(v)[:20])
    else:
        print(' ', k, type(v).__name__, str(v)[:80])
