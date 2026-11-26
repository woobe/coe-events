import json
CITY = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(CITY))
for vid in ("kl-977b423768cd", "kl-5206ba734e80", "kl-d05389364eb2"):
    rows = d["photos"][vid]
    print("==", vid, d["venues"][vid]["name"])
    for r in rows:
        print(json.dumps({k: r.get(k) for k in ("index", "view_kind", "withheld", "hotlink_ok",
                                               "url", "verified", "rights")},
                         indent=1, ensure_ascii=False))
