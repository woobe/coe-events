import json, collections
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(p))
print("_photo values:", collections.Counter(repr(v.get("_photo"))[:60] for v in d["venues"].values()))
# how many withheld rows total and their field sets
wh = [r for rows in d["photos"].values() for r in rows if r.get("withheld")]
print("withheld rows", len(wh))
print("withheld field sets:")
for fs, n in collections.Counter(tuple(sorted(r)) for r in wh).most_common():
    print(" ", n, fs)
print("live row field sets:")
lv = [r for rows in d["photos"].values() for r in rows if not r.get("withheld")]
for fs, n in collections.Counter(tuple(sorted(r)) for r in lv).most_common():
    print(" ", n, fs)
print("max index per group sample:", [(v, max(r.get("index", -1) for r in rows)) for v, rows in list(d["photos"].items())[:3]])
