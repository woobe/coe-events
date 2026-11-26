import json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
R=json.load(open(BASE+"/operator-fetch-report.json"))
want=["mtl-1125d1fcdf46","mtl-d0e27aa38d40","mtl-b1e93c63b00b","mtl-281cff0a7a6d","mtl-6f6753b2d241","mtl-eeca8449dbec","mtl-2729e116a7ed","mtl-583f8727f3f3","mtl-2fc617abde76","mtl-eb0452047e00","mtl-edf77b252f04","mtl-8ef00c25a80d","mtl-bfeec3cc37f4","mtl-a200486a6df1","mtl-3c2599f5b2b4"]
for k,r in R.items():
    vid=k.split(":")[0]
    if vid not in want: continue
    print("\n==",k,r.get("url"))
    seen=set()
    for u in r.get("imgs",[]):
        if u in seen or u.startswith("data:"): continue
        seen.add(u); print("  ",u)
