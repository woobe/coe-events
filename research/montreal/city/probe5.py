import json
p="/home/joe/repo_dev/coe-events/research/montreal/city/city.json"
s=json.load(open(p))
for vid, recs in sorted(s["photos"].items()):
    print("\n==",vid,"|",s["venues"][vid]["name"])
    for r in recs:
        print(" ", json.dumps({k:r.get(k) for k in ("url","source_page","room","alt","index","withheld","rights_basis","checked_on")},ensure_ascii=False))
print("\n\n=== SOURCES_CONSULTED ===")
for i,x in enumerate(s["sources_consulted"]):
    print(i, x.get("kind"), "|", x.get("title"), "|", x.get("url"), "|", x.get("check_status"), x.get("checked_on"), "|", str(x.get("note"))[:160])
print("\n=== HOLIDAY ROWS ===")
for h in s["holidays"]:
    print(json.dumps(h,ensure_ascii=False)[:500])
