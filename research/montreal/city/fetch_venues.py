import json, os, re, ssl, sys, time, urllib.request, urllib.parse, hashlib
BASE = "/home/joe/repo_dev/coe-events/research/montreal/city"
S = json.load(open(BASE + "/city.json"))
OUT = BASE + "/captures"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-CA,en;q=0.9,fr;q=0.8",
    })
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        data = r.read()
        return r.status, r.headers.get("content-type", ""), data

report = {}
for vid, v in sorted(S["venues"].items()):
    u = (v["fields"].get("source_url") or {}).get("value")
    if not u:
        report[vid] = {"error": "no source_url"}
        continue
    try:
        st, ct, data = fetch(u)
    except Exception as e:
        report[vid] = {"url": u, "error": repr(e)[:200]}
        print(vid, "ERR", u, repr(e)[:120], flush=True)
        continue
    name = re.sub(r"[^a-z0-9]+", "-", v["name"].lower())[:40].strip("-")
    path = os.path.join(OUT, vid + "-" + name + ".html")
    open(path, "wb").write(data)
    text = data.decode("utf-8", "replace")
    links = sorted(set(re.findall(r'href="(https?://[^"]+)"', text)))
    imgs = sorted(set(re.findall(r'(?:src|data-src|content)="(https?://[^"]+\.(?:jpe?g|png|webp)[^"]*)"', text, re.I)))
    addr = sorted(set(re.findall(r'[^<>]{0,60}(?:Montr[eé]al|Qu[eé]bec)[^<>]{0,40}', text)))
    report[vid] = {"url": u, "status": st, "ctype": ct, "bytes": len(data), "file": path,
                   "links": links, "images": imgs[:40], "addr_hits": addr[:6]}
    print(vid, st, len(data), u, flush=True)
    time.sleep(0.5)

json.dump(report, open(BASE + "/venue-fetch-report.json", "w"), indent=1, ensure_ascii=False)
print("WROTE", BASE + "/venue-fetch-report.json")
