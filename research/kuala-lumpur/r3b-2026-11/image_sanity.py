#!/usr/bin/env python3
"""Image-level sanity check for every new row: decode, measure, and flag a
line-art image that was labelled as a photo (or vice versa)."""
import json
from pathlib import Path
from PIL import Image, ImageStat

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
store = json.loads(Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json").read_text())
pre = json.loads(Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.pre-r3b.json").read_text())
preurls = {r.get("url") for rows in pre["photos"].values() for r in rows}
new = [(vid, r) for vid, rows in store["photos"].items() for r in rows
       if not r.get("withheld") and r.get("url") not in preurls]
byurl = {}
for p in BASE.glob("*probe.json"):
    for row in json.loads(p.read_text()):
        byurl[row["url"]] = row.get("file")

print(len(new), "new rows")
problems = []
for vid, r in new:
    path = byurl.get(r["url"])
    if not path or not Path(path).exists():
        problems.append(("missing file", r["url"]))
        continue
    im = Image.open(path); im.load()
    w, h = im.size
    rgb = im.convert("RGB")
    small = rgb.resize((160, max(1, int(160 * h / w))))
    px = list(small.getdata())
    n = len(px)
    white = sum(1 for a, b, c in px if a > 235 and b > 235 and c > 235) / n
    sat = ImageStat.Stat(rgb.convert("HSV").resize((160, max(1, int(160 * h / w))))).mean[1]
    kind = r["view_kind"]
    flag = ""
    if kind in ("interior", "layout", "past_event") and white > 0.55 and sat < 60:
        flag = "PHOTO LABELLED BUT LINE-ART-LIKE"
    if kind == "floor_plan" and not (white > 0.5):
        flag = "PLAN LABELLED BUT NOT LINE-ART-LIKE"
    if (w, h) != (r["dimensions"]["width"], r["dimensions"]["height"]):
        flag += " DIM MISMATCH"
    if flag:
        problems.append((flag.strip(), r["url"]))
    print(f"{kind:10s} {w}x{h} white={white:.2f} sat={sat:5.1f} {flag:32s} {r['alt'][:60]}")
print("problems:", problems)
