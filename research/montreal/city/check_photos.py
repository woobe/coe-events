import json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
S=json.load(open(BASE+"/city.json"))
N=json.load(open(BASE+"/photo-records.json"))
for vid in sorted(set(S["photos"])|set(N)):
    a=len(S["photos"].get(vid,[])); b=len(N.get(vid,[]))
    c=sum(1 for r in S["photos"].get(vid,[]) if not r.get("withheld"))
    print(vid,"stored",a,"new-specs",b,"cleared",c)
print("total stored",sum(len(v) for v in S["photos"].values()),"specs",sum(len(v) for v in N.values()))
