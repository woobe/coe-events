import json
p="/home/joe/repo_dev/coe-events/research/san-francisco/city/city.json"
s=json.load(open(p))
print("TOP", list(s))
for k in ("refresh_revision","declared_gaps","updated_at","schema_version"):
    print(k, "=>", json.dumps(s.get(k), ensure_ascii=False)[:1200])
vids=list(s['venues'])
print("nvenues",len(vids),"nevents",len(s.get('events',{})),"nphotos",len(s.get('photos',{})))
v=s['venues'][vids[0]]
print("fields:", list(v['fields'].keys()))
print("coordinates:", json.dumps(v['fields'].get('coordinates'),indent=1,ensure_ascii=False)[:1800])
print("photos:", json.dumps(s['photos'][vids[0]],indent=1,ensure_ascii=False)[:1200])
print("coverage n:", len(s.get('coverage',[])))
for c in s.get('coverage',[])[:3]: print(json.dumps(c,ensure_ascii=False)[:400])
