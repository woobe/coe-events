import json
from pathlib import Path
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur")
pre = json.loads((BASE / "city" / "city.pre-r3b.json").read_text())
post = json.loads((BASE / "city" / "city.json").read_text())
changes = []
for vid in post["photos"]:
    a = pre["photos"][vid]
    b = post["photos"][vid]
    removed = [r for r in a if r not in b]
    added = [r for r in b if r not in a]
    if not removed and not added:
        continue
    changes.append({
        "venue_id": vid,
        "venue": post["venues"][vid]["name"],
        "removed": [{"view_kind": r.get("view_kind"), "alt": r.get("alt"), "withheld": r.get("withheld")}
                    for r in removed],
        "added": [{"view_kind": r.get("view_kind"), "alt": r.get("alt"), "url": r.get("url"),
                   "withheld": r.get("withheld"), "source_page": r.get("source_page"),
                   "rights": (r.get("rights") or "")[:80]} for r in added],
    })
out = BASE / "r3b-2026-11" / "photo-changes.json"
out.write_text(json.dumps(changes, indent=1, ensure_ascii=False))
print("changed groups", len(changes), "->", out)
for c in changes:
    print(c["venue"], "removed", len(c["removed"]), "added", len(c["added"]))
