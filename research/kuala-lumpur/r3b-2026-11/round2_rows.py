import json
CITY = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(CITY))
ph = d["photos"]
print("DOJO rows:", len(ph["kl-977b423768cd"]))
for r in ph["kl-977b423768cd"]:
    print(json.dumps(r, indent=1))

# a mixed venue: one with live rows and a withheld row
for vid, rows in ph.items():
    if len(rows) > 1 and any(r.get("withheld") for r in rows) and any(not r.get("withheld") for r in rows):
        print("MIXED VENUE", vid)
        for r in rows:
            print(json.dumps(r, indent=1)[:1500])
        break

# all keys used by rows
keys = {}
for rows in ph.values():
    for r in rows:
        for k in r:
            keys[k] = keys.get(k, 0) + 1
print("ROW KEYS:", sorted(keys.items(), key=lambda kv: -kv[1]))
