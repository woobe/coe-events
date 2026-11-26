import json
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11/photo-changes.json"
d = json.load(open(p))
print(type(d).__name__, (list(d.keys()) if isinstance(d, dict) else len(d)))
def walk(o, path=""):
    if isinstance(o, dict):
        blob = json.dumps(o)
        if ("dojo" in blob.lower() or "3802-hor" in blob or "5291-hor" in blob) and len(blob) < 6000:
            print("HIT", path, blob[:1500])
        for k, v in o.items():
            walk(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, path + "/" + str(i))
if isinstance(d, dict):
    for k in d:
        print("KEY", k, type(d[k]).__name__, len(d[k]) if hasattr(d[k], "__len__") else "")
        print("  first:", json.dumps(d[k])[:400])
walk(d)
