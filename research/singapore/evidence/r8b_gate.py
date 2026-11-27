"""R8b gate: ranker aggregates + coordinate/photo edge detail. Read-only."""
import json, sys
from collections import Counter
sys.path.insert(0, "/home/joe/repo_dev/hermes-skills/plan-event/scripts")
from city_rank import build_ranking
from city_store import loss_check

S = "research/singapore/city/city.json"
store = json.load(open(S))
r = build_ranking(store, "2026-11-26")
rows = r["rows"]; leads = r["leads"]; seq = r["sequence"]
ids = [x["venue_id"] for x in rows] + [x["venue_id"] for x in leads]
print("rows", len(rows), "leads", len(leads), "sequence", len(seq))
print("counts", r["counts"])
print("ids unique", len(set(ids)), "of", len(ids))
print("sequence unique", len(set(seq)), "of", len(seq))
print("id set == store venues", set(ids) == set(store["venues"]))
print("sequence set == store venues", set(seq) == set(store["venues"]))
print("tiers rows", dict(Counter((x.get("tier") or {}).get("label") for x in rows)))
print("tiers leads", dict(Counter((x.get("tier") or {}).get("label") for x in leads)))

print("\n-- coordinate provider x failed_lookups --")
tab = Counter()
for vid, v in store["venues"].items():
    e = v["fields"]["coordinates"]
    p = e["provider"].split(" (")[0]
    fl = e.get("failed_lookups", "")
    if fl == "none":
        tab[(p, "none")] += 1
    else:
        first = fl.split(".")[0][:70]
        tab[(p, "recorded: " + first)] += 1
for k, n in sorted(tab.items()):
    print(n, "|", k[0], "|", k[1])

print("\n-- match_evidence prefixes --")
print(dict(Counter(v["fields"]["coordinates"].get("match_evidence", "")[:60]
                   for v in store["venues"].values())))

print("\n-- loss check vs pre-r8 --")
old = json.load(open("research/singapore/evidence/city.pre-r8.json"))
loss = loss_check(old, store)
print("keys", {k: len(v) for k, v in loss.items()})
print("non-sources keys", [k for k in loss if k != "sources_consulted"])
