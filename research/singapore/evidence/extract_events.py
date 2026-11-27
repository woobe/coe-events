import json, re, sys
from pathlib import Path

def json_blobs(html):
    out = []
    for m in re.finditer(r'(?is)<script[^>]*>(.*?)</script>', html):
        body = m.group(1).strip()
        if not body:
            continue
        if body[0] not in '[{':
            mm = re.search(r'(\{.*\}|\[.*\])', body, re.S)
            if not mm:
                continue
            body = mm.group(1)
        try:
            out.append(json.loads(body))
        except Exception:
            pass
    return out

def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)

f = sys.argv[1]
html = Path(f).read_text(encoding='utf-8', errors='replace')
seen = set()
for blob in json_blobs(html):
    for node in walk(blob):
        keys = set(node)
        date_keys = keys & {'start_at', 'startAt', 'start_date', 'startDate', 'start', 'datetime', 'date'}
        name_keys = keys & {'name', 'title', 'event_name', 'summary'}
        if not date_keys or not name_keys:
            continue
        name = node.get('name') or node.get('title') or node.get('event_name') or node.get('summary')
        if not isinstance(name, str):
            continue
        vals = ' '.join(str(node.get(k)) for k in date_keys)
        loc = json.dumps(node.get('location') or node.get('city') or node.get('geo_address_info') or {}, ensure_ascii=False)
        key = (name, vals[:30])
        if key in seen:
            continue
        seen.add(key)
        flag = '2027' if '2027' in vals else ''
        print(flag, '|', vals[:40], '|', name[:90], '|', loc[:120])
