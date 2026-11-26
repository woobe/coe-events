import json, hashlib
from pathlib import Path
from fetch_pages import PAGES

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
lines = ["# R3b sources consulted (2026-11-26)", ""]
for slug, url in PAGES:
    p = BASE / "pages" / (slug + ".html")
    if not p.exists():
        lines.append(f"- {url}  [not fetched]")
        continue
    blob = p.read_bytes()
    title = ""
    head = blob[:4000].decode("utf-8", "replace")
    import re
    m = re.search(r"<title[^>]*>(.*?)</title>", head, re.S | re.I)
    if m:
        title = re.sub(r"\s+", " ", m.group(1)).strip()[:90]
    lines.append(f"- {url}\n  saved {p.name} ({len(blob)} b, sha256 {hashlib.sha256(blob).hexdigest()[:16]}), title \"{title}\"")
pdf = BASE / "pdf" / "klcc-capacity-chart.pdf"
lines.append(f"- https://www.klccconventioncentre.com/clients/asset_1DC34A5E-8086-475D-9583-2A8A0CD6CFA6/contentms/img/pdf/klcc-capacity-chart-and-floor-plan.pdf"
             f"\n  saved klcc-capacity-chart.pdf ({pdf.stat().st_size} b, sha256 {hashlib.sha256(pdf.read_bytes()).hexdigest()[:16]})")
lines += ["", "## Blocked or dead", "",
          "- https://www.apwbangsar.com/ - DNS does not resolve (curl error 6)",
          "- https://www.sunwaypyramidconventioncentre.com/ - DNS does not resolve (curl error 6)",
          "- https://mecc.matrade.gov.my/ - returns a 44-byte stub",
          "- https://www.shangri-la.com/kualalumpur/shangrila/meetings-events/meeting-rooms/ - Cloudflare 403",
          "- https://www.shangri-la.com/kualalumpur/traders/meetings-events/meeting-rooms/ - Cloudflare 403",
          "- https://www.wework.com/en-MY/l/event-space/kuala-lumpur--MY - Cloudflare 403",
          "- https://www.matrade.gov.my/en/about-matrade/mecc - 404",
          "- https://www.mandarinoriental.com/en/kuala-lumpur/klcc/meetings-and-events - 404 (correct path is /petronas-towers/meet)",
          "- https://www.klccconventioncentre.com/venues/plenary-hall - 404 (and two other patterns)",
          "- http://web.archive.org/web/20261101233312/http://thebee.com.my/ - snapshot is a challenge page",
          ]
(BASE / "sources-r3b.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
