"""Which 10 claim objects account for the 750 -> 760 delta?"""
import json
from collections import Counter

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

before = json.load(open("research/singapore/evidence/city.rev1-before-round2.json"))
after = json.load(open("research/singapore/city/city.json"))
cb = Counter(x[3]["claim_id"] for x in claims(before))
ca = Counter(x[3]["claim_id"] for x in claims(after))
new = ca - cb
gone = cb - ca
print("new ids", len(new), "gone ids", len(gone))
idx = {x[3]["claim_id"]: x for x in claims(after)}
for cid, n in new.items():
    x = idx[cid]
    print("NEW", cid, x[0], x[1], x[2], "| unlocated",
          not x[3].get("source_locator") and not x[3].get("capture"),
          "| text", (x[3].get("text") or "")[:100])
for cid, n in gone.items():
    print("GONE", cid, n)
