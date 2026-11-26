import json
CITY = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(CITY))
for vid, rows in d["photos"].items():
    for r in rows:
        u = r.get("url") or ""
        if "kulwh-meeting-facilities-3802" in u or "kulxr-astor-room-5291" in u:
            print(vid)
            print(json.dumps(r, indent=1))
            print("=====")
