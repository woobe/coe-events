import json, collections
p="/home/joe/repo_dev/coe-events/research/montreal/city/city.json"
s=json.load(open(p))
print("updated_at", s.get("updated_at"), "revision", s.get("refresh_revision"))
print("holidays", len(s["holidays"]), "coverage", len(s["coverage"]), "sources", len(s["sources_consulted"]))
print("photos venues with records:", len(s["photos"]))
tot = sum(len(v) for v in s["photos"].values())
wh = sum(1 for v in s["photos"].values() for r in v if r.get("withheld"))
print("photo records", tot, "withheld", wh)
rows=[]
for vid,v in s["venues"].items():
    f=v["fields"]
    addr=(f.get("address") or {}).get("value")
    co=(f.get("coordinates") or {}).get("value")
    pw=(f.get("programme_windows") or {}).get("value")
    src=(f.get("source_url") or {}).get("value")
    ph=s["photos"].get(vid,[])
    rows.append(dict(vid=vid,name=v["name"],life=v["lifecycle"],addr=addr,
        coord=(None if not co else (co.get("latitude"),co.get("longitude"),co.get("precision"))),
        pw=pw, nphoto=len(ph), nwh=sum(1 for r in ph if r.get("withheld")),
        src=src, fields=sorted(f.keys())))
for r in sorted(rows,key=lambda r:r["name"].lower()):
    print("\n==",r["vid"],"|",r["name"],"|",r["life"])
    print("  addr:",r["addr"])
    print("  coord:",r["coord"])
    print("  pw:",json.dumps(r["pw"],ensure_ascii=False) if r["pw"] else None)
    print("  photos:",r["nphoto"],"withheld",r["nwh"])
    print("  src:",r["src"])
print("\nMISSING COORD:", [r["vid"] for r in rows if not r["coord"] or r["coord"][0] is None])
print("NO PHOTOS:", [r["vid"] for r in rows if r["nphoto"]==0])
