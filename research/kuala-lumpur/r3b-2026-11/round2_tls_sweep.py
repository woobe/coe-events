import json, subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CITY = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json")
store = json.loads(CITY.read_text())
urls = []
for vid, rows in store["photos"].items():
    for r in rows:
        if r.get("withheld"):
            continue
        u = r.get("url") or ""
        if u.startswith("http"):
            urls.append((vid, u))
uniq = sorted({u for _, u in urls})
print("live rows:", len(urls), "unique urls:", len(uniq))


def probe(u):
    cmd = ["curl", "-sS", "-o", "/dev/null", "--max-time", "40",
           "-w", "%{http_code} %{size_download}", u]
    p = subprocess.run(cmd, capture_output=True, text=True)
    return u, p.returncode, p.stdout.strip(), p.stderr.strip()[:160]


bad = []
with ThreadPoolExecutor(max_workers=8) as ex:
    for u, rc, out, err in ex.map(probe, uniq):
        status = out.split()[0] if out else ""
        if rc != 0 or not status.startswith("2"):
            bad.append((u, rc, status, err))
print("failures:", len(bad))
for b in bad:
    print("FAIL", b)
