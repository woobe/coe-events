"""R8b independent re-verification of the four round-1 defects.

Read-only over research/singapore/city/city.json.
Run from the coe-events repo root:  python3 research/singapore/evidence/verify_r8b.py
"""
import json, os, re
from collections import Counter, defaultdict

BASE = "research/singapore/city"
STORE = os.path.join(BASE, "city.json")
s = json.load(open(STORE))

print("STORE", STORE)
print("refresh_revision", s.get("refresh_revision"), "updated_at", s.get("updated_at"))

# ---------- item 4 helper: every dict carrying a claim_id, at any depth ----------
claims = []  # (top, collection_id, path, claim_obj)

def walk(node, top, cid, path):
    if isinstance(node, dict):
        if "claim_id" in node:
            claims.append((top, cid, path, node))
        for k, v in node.items():
            walk(v, top, cid, path + "/" + str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, top, cid, path + "/" + str(i))

for cid, v in s["venues"].items():
    walk(v, "venue", cid, "venues/" + cid)
for cid, e in s["events"].items():
    walk(e, "event", cid, "events/" + cid)

print("\n=== ITEM 4: claim objects ===")
print("total claim objects", len(claims))
by_top = Counter(t for t, _, _, _ in claims)
print("by collection", dict(by_top))
unloc = [c for c in claims if not c[3].get("source_locator") and not c[3].get("capture")]
unloc_top = Counter(t for t, _, _, _ in unloc)
print("unlocated total", len(unloc), dict(unloc_top))

# where do the unlocated ones live (top-level container under the collection record)?
def container(path):
    parts = path.split("/")
    if len(parts) > 3:
        return parts[3]
    return "?"
print("unlocated by container", dict(Counter(container(p) for _, _, p, _ in unloc)))

# fields-only count (the naive definition)
fields_only = []
for top, coll in (("venue", s["venues"]), ("event", s["events"])):
    for cid, rec in coll.items():
        for fname, f in (rec.get("fields") or {}).items():
            if isinstance(f, dict) and "claim_id" in f:
                if not f.get("source_locator") and not f.get("capture"):
                    fields_only.append((top, cid, fname))
print("unlocated fields-only", len(fields_only), dict(Counter(t for t, _, _ in fields_only)))

# duplicate ids
id_counts = Counter(c[3]["claim_id"] for c in claims)
dups = {k: n for k, n in id_counts.items() if n > 1}
print("claim ids appearing more than once (any depth)", len(dups), list(dups.items())[:10])
field_id_counts = Counter()
for top, coll in (("venue", s["venues"]), ("event", s["events"])):
    for cid, rec in coll.items():
        for fname, f in (rec.get("fields") or {}).items():
            if isinstance(f, dict) and "claim_id" in f:
                field_id_counts[f["claim_id"]] += 1
print("field-level duplicate ids", {k: n for k, n in field_id_counts.items() if n > 1})
print("cl-5452575c6d1b occurrences in store text", open(STORE).read().count("cl-5452575c6d1b"))

gap = [g for g in s["declared_gaps"] if g["kind"] == "legacy-claims"][0]["text"]
print("gap text claims 760:", "760" in gap, "| 608:", "608" in gap, "| 152:", "152" in gap)
print("gap text matches computed?",
      f"{len(unloc)} claim objects" in gap and f"{unloc_top.get('venue',0)} venue" in gap
      and f"{unloc_top.get('event',0)} event" in gap)

# ---------- item 1: holidays ----------
print("\n=== ITEM 1: holidays ===")
print("rows", len(s["holidays"]))
want = {"2027-02-08": ("public_holiday", "mom-public-holidays.txt"),
        "2027-02-09": ("school_holiday", "moe-school-terms-2027.txt"),
        "2027-05-03": ("school_holiday", "moe-school-terms-2027.txt"),
        "2027-12-27": ("school_holiday", "moe-school-terms-2027.txt")}
for d, (kind, cap) in want.items():
    rows = [h for h in s["holidays"] if h.get("start_date") == d]
    if not rows:
        print("MISSING", d); continue
    h = rows[0]
    print(d, h["kind"], h.get("observance"), "|", h["source_locator"], "|", h["capture"],
          "| match", h["kind"] == kind and h["capture"].endswith(cap), "| quote_ok", bool(h.get("quote")))
# quote really on the cited line?
def line_of(capture, locator):
    nums = re.findall(r"\d+", locator or "")
    if not nums: return None
    p = os.path.join(BASE, capture)
    lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
    return lines[int(nums[-1]) - 1] if int(nums[-1]) <= len(lines) else None

for d in want:
    h = [x for x in s["holidays"] if x.get("start_date") == d][0]
    line = line_of(h["capture"], h["source_locator"])
    q = h.get("quote", "")
    print("line check", d, "line carries quote:", bool(line and q and q.split("(")[0].strip()[:40] in line))

g6 = [g for g in s["declared_gaps"] if g["kind"] == "holidays"][0]["text"]
print("gap[6] mentions 9 Feb overlap:", "overlap" in g6.lower())
print("gap[6] text:", g6)

# ---------- item 2: coordinates ----------
print("\n=== ITEM 2: coordinates ===")
prov = Counter(); resp_missing = []; retry_missing = []
none_rows = []; nom_bad = []; fail_rows = 0; both_fail = 0
for vid, v in s["venues"].items():
    e = v["fields"]["coordinates"]
    p = os.path.join(BASE, e["geocode_response"])
    if not os.path.exists(p): resp_missing.append((vid, e["geocode_response"]))
    if e.get("retry_response") and not os.path.exists(os.path.join(BASE, e["retry_response"])):
        retry_missing.append((vid, e["retry_response"]))
    prov[e["provider"].split(" (")[0]] += 1
    fl = e.get("failed_lookups", "")
    if fl == "none": none_rows.append(vid)
    else: fail_rows += 1
    if "both" in fl.lower() or ("photon" in fl.lower() and "nominatim" in fl.lower()):
        both_fail += 1
    if e["provider"].startswith("OpenStreetMap Nominatim"):
        if "Nominatim" not in e.get("match_evidence", "") or "Independent Photon lookup" in e.get("match_evidence", ""):
            nom_bad.append(vid)
print("providers", dict(prov))
print("geocode_response missing", len(resp_missing), resp_missing)
print("retry_response missing", len(retry_missing), retry_missing)
print("failed_lookups == none", len(none_rows))
print("failed_lookups recorded", fail_rows, "| both geocoders named", both_fail)
print("Nominatim rows not naming Nominatim / still Photon boilerplate", len(nom_bad), nom_bad)

# ---------- item 3: photos ----------
print("\n=== ITEM 3: photos ===")
usable = []  # (vid, room, room_specific, room_text, url)
for vid, recs in s["photos"].items():
    for r in recs:
        if r.get("url") and not r.get("withheld"):
            usable.append((vid, r.get("room"), r.get("room_specific"), (r.get("placement_proof") or "")[:80], r.get("url")))
print("usable", len(usable), "room_specific true", sum(1 for u in usable if u[2] is True),
      "false", sum(1 for u in usable if u[2] is False))
print("venues 1+", sum(1 for r in s["photos"].values() if any(x.get("url") and not x.get("withheld") for x in r)),
      "4+", sum(1 for r in s["photos"].values() if sum(1 for x in r if x.get("url") and not x.get("withheld")) >= 4),
      "none", sum(1 for r in s["photos"].values() if not any(x.get("url") and not x.get("withheld") for x in r)))
print("null dimensions", sum(1 for vid, recs in s["photos"].items() for r in recs
                            if r.get("url") and not r.get("withheld")
                            and not (r.get("dimensions") or {}).get("width")))
print("-- self-described fallbacks still true --")
for u in usable:
    text = (u[3] + " " + str(u[1])).lower()
    if u[2] is True and ("not the listed event space" in text or "not a hire room" in text):
        print("FAIL", u[0], u[1], "|", u[3])
print("-- all 9 fallbacks --")
for u in usable:
    if u[2] is False:
        print("fb", u[0], "|", u[1], "|", u[3])
g3 = [g for g in s["declared_gaps"] if g["kind"] == "photos"][0]["text"]
print("gap[3] says 113/9:", "113" in g3 and "9 are labelled" in g3, "| says 30/20/6:",
      "30 venues" in g3 and "20 carry four" in g3 and "6 carry none" in g3)

# ---------- guards ----------
print("\n=== GUARDS ===")
print("venue ids with sg- prefix", sum(1 for k in s["venues"] if k.startswith("sg-")), "/", len(s["venues"]))
print("event ids with sg- prefix", sum(1 for k in s["events"] if k.startswith("sg-")), "/", len(s["events"]))
print("venue_id field == key", all(v.get("venue_id") == k for k, v in s["venues"].items()))
print("event_id field == key", all(v.get("event_id") == k for k, v in s["events"].items()))
