import json
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(p))
for vid in ("kl-e67bf1a8718b", "kl-1fb682196274", "kl-1501b357e078"):
    print("=" * 70, d["venues"][vid]["name"])
    for r in d["photos"][vid]:
        print(json.dumps(r, indent=1, ensure_ascii=False)[:1200])
