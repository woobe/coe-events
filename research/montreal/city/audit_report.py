import json, hashlib, collections, datetime
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
A=json.load(open(BASE+"/city.pre-r2.json"))
S=json.load(open(BASE+"/city.json"))
def sha(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
print("STORE sha256",sha(BASE+"/city.json"),"bytes",len(open(BASE+"/city.json","rb").read()))
print("venue count pre/post",len(A["venues"]),len(S["venues"]))
tiers=collections.Counter((v["fields"]["coordinates"]["value"] or {}).get("precision") for v in S["venues"].values())
print("coord tiers",dict(tiers))
print("pins non-null",sum(1 for v in S["venues"].values() if (v["fields"]["coordinates"]["value"] or {}).get("latitude") is not None))
print("was pinless",[k for k,v in A["venues"].items() if not (v["fields"].get("coordinates") or {}).get("value") or (v["fields"]["coordinates"]["value"] or {}).get("latitude") is None])
print("now tiers",[(k,S["venues"][k]["fields"]["coordinates"]["value"]["precision"]) for k in [k for k,v in A["venues"].items() if not (v["fields"].get("coordinates") or {}).get("value") or (v["fields"]["coordinates"]["value"] or {}).get("latitude") is None]])
# photos
cleared=[r for vs in S["photos"].values() for r in vs if not r.get("withheld")]
wh=[r for vs in S["photos"].values() for r in vs if r.get("withheld")]
print("photos total",len(cleared)+len(wh),"cleared",len(cleared),"withheld",len(wh))
fallback=[r for r in cleared if r.get("view_kind") in ("exterior","lobby","render")]
room=[r for r in cleared if r.get("view_kind") in ("interior","layout","floor_plan","past_event")]
print("room-kind",len(room),"fallback",len(fallback))
one=four=none=0
for vid,v in S["venues"].items():
    c=[r for r in S["photos"].get(vid,[]) if not r.get("withheld")]
    if not c: none+=1
    else:
        one+=1
        if len(c)>=4: four+=1
print("venues 1+",one,"4+",four,"none",none)
print("view_kinds",dict(collections.Counter(r.get("view_kind") for r in cleared)))
# access
full=floor=short=unk=0
for v in S["venues"].values():
    w=v["fields"]["programme_windows"]["value"]
    a,b=w["8"]["state"],w["12"]["state"]
    if b=="yes": full+=1
    elif a=="yes" and b=="no": floor+=1
    elif a=="no" and b=="no": short+=1
    else: unk+=1
print("access full/floor/shorter/unknown",full,floor,short,unk)
# holidays
print("holidays",len(A["holidays"]),"->",len(S["holidays"]))
for r in S["holidays"]:
    d=r["start_date"]
    wd=datetime.date.fromisoformat(d).strftime("%a")
    print(" ",r["jurisdiction_id"],r["kind"],d,r.get("end_date"),wd,"|",r["holiday_name"],"| choice:",r.get("choice"))
print("coverage",len(A["coverage"]),"->",len(S["coverage"]))
# events
print("events",len(A["events"]),"->",len(S["events"]))
for e in S["events"].values():
    dr=e["fields"]["date_range"]["value"]
    print("  ",e["name"],dr)
print("sources",len(A["sources_consulted"]),"->",len(S["sources_consulted"]))
print("gaps",len(S["declared_gaps"]))
# duplicate photo urls within venue
for vid,vs in S["photos"].items():
    urls=[r["url"] for r in vs]
    if len(urls)!=len(set(urls)): print("DUP",vid)
# cleared record completeness
bad=[r["url"] for r in cleared if not r.get("rights") or not r.get("view_kind") or not r.get("verified") or r.get("hotlink_ok") is False or not r.get("thumb_note")]
print("bad cleared",len(bad),bad[:5])
