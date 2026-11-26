import re, json, html
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11/pages/mo-meet.html"
raw = open(p, errors="replace").read()
seen = set()
for m in re.finditer(r"media-data=\"([^\"]+)\"", raw):
    blob = html.unescape(m.group(1))
    try:
        data = json.loads(blob)
    except Exception as exc:
        print("parse fail", exc)
        continue
    for a in data.get("Assets", []):
        key = a.get("ImageSrc")
        if key in seen:
            continue
        seen.add(key)
        print(json.dumps({"title": a.get("Title"), "src": key}, ensure_ascii=False))
print("total", len(seen))
print("PDF links:")
for m in re.finditer(r"https?://[^\"' ]+\.pdf", raw):
    print(" ", m.group(0)[:160])
