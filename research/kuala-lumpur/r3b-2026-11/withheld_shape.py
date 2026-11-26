import json, collections
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(p))
print(collections.Counter(r.get("alt") for rows in d["photos"].values() for r in rows if r.get("withheld")))
for vid, rows in d["photos"].items():
    if any(r.get("withheld") for r in rows) and len(rows) > 1:
        print("mixed group:", vid, d["venues"][vid]["name"], [r.get("view_kind") for r in rows])
