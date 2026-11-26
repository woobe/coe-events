import json, collections
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
A=json.load(open(BASE+"/city.pre-r2.json")); S=json.load(open(BASE+"/city.json"))
ch=[]
for vid,v in S["venues"].items():
    old=(A["venues"][vid]["fields"].get("address") or {}).get("value")
    new=v["fields"]["address"]["value"]
    if old!=new: ch.append((v["name"],old,new))
print("address changed",len(ch))
for n,o,x in ch: print(" -",n,"|",o,"=>",x)
print("address claims checked_on 2026-11-26:",sum(1 for v in S["venues"].values() if v["fields"]["address"]["verified_at"]=="2026-11-26"))
print("address claims with quote:",sum(1 for v in S["venues"].values() if v["fields"]["address"].get("quote")))
