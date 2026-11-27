import json, re, sys
from pathlib import Path

def walk(node, path=''):
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from walk(v, path + '/' + str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, path + '/%d' % i)

def load_json_scripts(html):
    out = []
    for m in re.finditer(r'(?is)<script[^>]*>(.*?)</script>', html):
        body = m.group(1).strip()
        if not body or len(body) < 20:
            continue
        if body[0] not in '[{':
            # look for a JSON object inside js assignment
            mm = re.search(r'(\{.*\})', body, re.S)
            if not mm:
                continue
            body = mm.group(1)
        try:
            out.append(json.loads(body))
        except Exception:
            continue
    return out

p = Path(sys.argv[1])
html = p.read_text(encoding='utf-8', errors='replace')
blobs = load_json_scripts(html)
print(p.name, 'json blobs:', len(blobs))
seen = set()
for blob in blobs:
    for path, node in walk(blob):
        s = json.dumps(node, ensure_ascii=False)[:4000]
        if '2027' not in s:
            continue
        keys = set(node)
        looks = keys & {'name', 'title', 'event_name', 'start_date', 'startDate', 'date', 'dates',
                        'start_at', 'startAt', 'location', 'city', 'venue'}
        if len(looks) < 2:
            continue
        name = node.get('name') or node.get('title') or node.get('event_name')
        if not name:
            continue
        key = (str(name), path[:120])
        if key in seen:
            continue
        seen.add(key)
        print('---', path[:160])
        print(json.dumps({k: node.get(k) for k in list(node)[:18]}, ensure_ascii=False)[:1200])
