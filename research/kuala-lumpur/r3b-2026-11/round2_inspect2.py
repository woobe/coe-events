import json

CITY = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(CITY))
ph = d["photos"]
print("photos type:", type(ph).__name__)
if isinstance(ph, dict):
    print("photos keys:", list(ph.keys())[:20])
    for k, v in ph.items():
        print(" ", k, "->", type(v).__name__, (len(v) if hasattr(v, "__len__") else ""))
        print("   sample:", json.dumps(v, indent=1)[:800])
        break
elif isinstance(ph, list):
    print("n groups:", len(ph))
    print(json.dumps(ph[0], indent=1)[:1200])

# find dojo
def scan(obj, path=""):
    res = []
    if isinstance(obj, dict):
        blob = json.dumps(obj)
        if "dojo" in blob.lower() and ("images" in obj or "photos" in obj or "url" in obj):
            res.append((path, obj))
        for k, v in obj.items():
            res += scan(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            res += scan(v, path + "/" + str(i))
    return res

hits = scan(ph)
print("dojo hits:", len(hits))
for p, o in hits[:6]:
    print("PATH", p)
    print(json.dumps(o, indent=1)[:2500])
