"""R8b item 4: reproduce the 750 -> 760 delta and the LLI claim-id split."""
import json, os
from collections import Counter

def load(p):
    return json.load(open(p))

def claims(store):
    out = []
    def walk(node, top, cid, path):
        if isinstance(node, dict):
            if "claim_id" in node:
                out.append((top, cid, path, node))
            for k, v in node.items():
                walk(v, top, cid, path + "/" + str(k))
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, top, cid, path + "/" + str(i))
    for cid, v in store["venues"].items():
        walk(v, "venue", cid, "venues/" + cid)
    for cid, e in store["events"].items():
        walk(e, "event", cid, "events/" + cid)
    return out

before = load("research/singapore/evidence/city.rev1-before-round2.json")
after = load("research/singapore/city/city.json")

for label, s in (("BEFORE(round2 pre-image)", before), ("AFTER", after)):
    c = claims(s)
    un = [x for x in c if not x[3].get("source_locator") and not x[3].get("capture")]
    by = Counter(x[0] for x in un)
    print(label, "all", len(c), "unlocated", len(un), dict(by))

print("delta", len([x for x in claims(after) if not x[3].get("source_locator") and not x[3].get("capture")])
      - len([x for x in claims(before) if not x[3].get("source_locator") and not x[3].get("capture")]))

# blocker records: after has 21 venue blockers; which are unlocated and how many were added?
def blockers(s):
    out = []
    for cid, v in s["venues"].items():
        b = v.get("blockers")
        if isinstance(b, dict) and "claim_id" in b:
            out.append((cid, b["claim_id"]))
        elif isinstance(b, list):
            for x in b:
                if isinstance(x, dict) and "claim_id" in x:
                    out.append((cid, x["claim_id"]))
    return out
print("blockers before", len(blockers(before)), "after", len(blockers(after)))

# LLI rows
lli = [k for k, v in after["venues"].items() if "Lifelong Learning" in (v.get("name") or "")]
print("\nLLI ids", lli)
for cid in lli:
    fb = before["venues"].get(cid, {}).get("fields", {})
    fa = after["venues"].get(cid, {}).get("fields", {})
    print("--", cid, after["venues"][cid]["name"])
    for f in sorted(set(fb) | set(fa)):
        cb = (fb.get(f) or {}).get("claim_id")
        ca = (fa.get(f) or {}).get("claim_id")
        vb = (fb.get(f) or {}).get("value")
        va = (fa.get(f) or {}).get("value")
        print("  ", f, "before", cb, "after", ca, "| id changed", cb != ca,
              "| value same", vb == va)

# field-level duplicates before/after
for label, s in (("before", before), ("after", after)):
    c = Counter()
    for coll in (s["venues"], s["events"]):
        for rec in coll.values():
            for f in (rec.get("fields") or {}).values():
                if isinstance(f, dict) and "claim_id" in f:
                    c[f["claim_id"]] += 1
    print(label, "field-level dup ids", {k: n for k, n in c.items() if n > 1})
