#!/usr/bin/env python3
"""Prove the R3b diff: photos only, and every venue has a recorded outcome."""
import json, hashlib, collections
from pathlib import Path

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city")
pre = json.loads((BASE / "city.pre-r3b.json").read_text(encoding="utf-8"))
post = json.loads((BASE / "city.json").read_text(encoding="utf-8"))
VIEW = ("interior", "layout", "floor_plan", "past_event", "exterior", "lobby", "render")
ROOM = {"interior", "layout", "floor_plan", "past_event"}

def h(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

print("top keys identical:", set(pre) == set(post), len(pre), len(post))
changed = [k for k in pre if k != "photos" and h(pre[k]) != h(post[k])]
print("non-photos keys changed:", changed)
print("photos key present both:", "photos" in pre and "photos" in post)
print("refresh_revision:", pre.get("refresh_revision"), "->", post.get("refresh_revision"))
print("venue ids identical:", set(pre["venues"]) == set(post["venues"]))
print("photo groups identical:", set(pre["photos"]) == set(post["photos"]))
# byte stability
raw = (BASE / "city.json").read_bytes()
print("round-trip byte identical:",
      (json.dumps(post, indent=1, sort_keys=False, ensure_ascii=False) + "\n").encode() == raw)
print("sha256:", hashlib.sha256(raw).hexdigest(), "bytes", len(raw))

def dist(store):
    live = collections.Counter()
    wh = 0
    for rows in store["photos"].values():
        for r in rows:
            if r.get("withheld"):
                wh += 1
            else:
                live[r.get("view_kind")] += 1
    return dict(sorted(live.items())), wh

print("before live/withheld:", dist(pre))
print("after  live/withheld:", dist(post))

# new rows = live rows whose url is not in pre
preurls = {r.get("url") for rows in pre["photos"].values() for r in rows}
new = [r for rows in post["photos"].values() for r in rows
       if not r.get("withheld") and r.get("url") not in preurls]
print("new live rows:", len(new))
bad = []
for r in new:
    if r.get("view_kind") not in VIEW: bad.append(("kind", r.get("url")))
    if not r.get("rights") or r["rights"].strip().lower() in {"unknown", "unverified", "not cleared", "none", "all rights reserved"}: bad.append(("rights", r.get("url")))
    if not r.get("placement_proof"): bad.append(("placement", r.get("url")))
    v = r.get("verified") or {}
    if not str(v.get("status")).startswith("2"): bad.append(("verified", r.get("url")))
    d = r.get("dimensions") or {}
    if not d.get("width") or not d.get("height"): bad.append(("dims", r.get("url")))
    if not r.get("source_page"): bad.append(("page", r.get("url")))
    if r.get("hotlink_ok") is not True: bad.append(("hotlink", r.get("url")))
print("bad new rows:", bad)

# outcomes per venue
out = collections.Counter()
room_venues, ext_only, none_venues = [], [], []
for vid, rows in post["photos"].items():
    live = [r for r in rows if not r.get("withheld")]
    kinds = {r.get("view_kind") for r in live}
    if kinds & ROOM:
        out["room-level"] += 1
        room_venues.append(vid)
    elif live:
        out["exterior-only"] += 1
        ext_only.append(vid)
    else:
        out["no image"] += 1
        none_venues.append(vid)
print("outcomes:", dict(out), "total", sum(out.values()))
print("exterior-only venues:", [(post["venues"][v]["name"], sorted({r.get("view_kind") for r in post["photos"][v] if not r.get('withheld')})) for v in ext_only])
print("no-image venues:", [post["venues"][v]["name"] for v in none_venues])
print("no-image venues with a route note:",
      sum(1 for v in none_venues if any("R3b (2026-11-26)" in (r.get("rights_note") or "")
                                        for r in post["photos"][v])))
