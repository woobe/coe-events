"""Round 2 verification: prove only `photos` changed and record the row diffs."""
import hashlib, json
from collections import Counter
from pathlib import Path

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur")
CITY = BASE / "city" / "city.json"
PRE2 = BASE / "city" / "city.pre-r3b-round2.json"
PRE1 = BASE / "city" / "city.pre-r3b.json"

now = json.loads(CITY.read_text())
pre2 = json.loads(PRE2.read_text())
pre1 = json.loads(PRE1.read_text())


def h(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


changed2 = [k for k in now if h(now[k]) != h(pre2[k])]
changed1 = [k for k in now if h(now[k]) != h(pre1[k])]
rt = json.dumps(now, indent=1, ensure_ascii=False) + "\n"
print("sha before:", hashlib.sha256(PRE2.read_bytes()).hexdigest(), len(PRE2.read_bytes()))
print("sha after :", hashlib.sha256(CITY.read_bytes()).hexdigest(), len(CITY.read_bytes()))
print("round-trip byte identical:", rt.encode() == CITY.read_bytes())
print("top-level keys changed vs pre-round-2:", changed2)
print("top-level keys changed vs pre-r3b   :", changed1)
print("refresh_revision:", pre2["refresh_revision"], "->", now["refresh_revision"])
print("key count:", len(pre2), len(now))

rowdiff = []
for vid in now["photos"]:
    a, b = pre2["photos"][vid], now["photos"][vid]
    for i, (ra, rb) in enumerate(zip(a, b)):
        if ra == rb:
            continue
        fields = {}
        for key in sorted(set(ra) | set(rb)):
            if ra.get(key) != rb.get(key):
                fields[key] = {"before": ra.get(key), "after": rb.get(key)}
        rowdiff.append({"venue_id": vid, "venue": now["venues"][vid]["name"],
                        "index": i, "url": rb.get("url"), "changed": fields})
print("rows changed:", len(rowdiff), [d["venue_id"] for d in rowdiff])

live = Counter()
withheld = 0
renderable = Counter()
for vid, rows in now["photos"].items():
    for r in rows:
        if r.get("withheld"):
            withheld += 1
            continue
        live[r.get("view_kind")] += 1
        rights = " ".join(str(r.get("rights") or r.get("rights_note") or "").split()).casefold()
        ok = (r.get("hotlink_ok") is not False
              and str((r.get("verified") or {}).get("status") or "").startswith("2")
              and rights)
        if ok:
            renderable[r.get("view_kind")] += 1
print("live rows by view_kind:", dict(sorted(live.items())))
print("renderable (hotlink gate) by view_kind:", dict(sorted(renderable.items())))
print("withheld rows:", withheld, "groups:", len(now["photos"]))

# venue outcomes
no_image, exterior_only, room_level = [], [], []
for vid, rows in now["photos"].items():
    shown = [r for r in rows if not r.get("withheld")]
    if not shown:
        no_image.append(vid)
    elif not any(r.get("view_kind") in ("interior", "layout", "floor_plan", "past_event") for r in shown):
        exterior_only.append(vid)
    else:
        room_level.append(vid)
print("outcomes: no image %d, exterior/lobby-only %d, room-level %d, total %d"
      % (len(no_image), len(exterior_only), len(room_level),
         len(no_image) + len(exterior_only) + len(room_level)))
print("venue ids covered:", len(set(now["photos"])))

out = {
    "sha256_before": hashlib.sha256(PRE2.read_bytes()).hexdigest(),
    "sha256_after": hashlib.sha256(CITY.read_bytes()).hexdigest(),
    "bytes_before": len(PRE2.read_bytes()),
    "bytes_after": len(CITY.read_bytes()),
    "top_level_changed_vs_pre_round2": changed2,
    "top_level_changed_vs_pre_r3b": changed1,
    "refresh_revision": now["refresh_revision"],
    "row_changes": rowdiff,
    "distribution": {"live_by_view_kind": dict(live), "renderable_by_view_kind": dict(renderable),
                     "withheld": withheld, "photo_groups": len(now["photos"])},
    "outcomes": {"no_image": len(no_image), "exterior_only": len(exterior_only),
                 "room_level": len(room_level), "venues": len(now["photos"])},
}
(BASE / "r3b-2026-11" / "round2-diff.json").write_text(
    json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("wrote round2-diff.json")
