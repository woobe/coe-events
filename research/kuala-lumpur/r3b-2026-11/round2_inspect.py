import json, hashlib, sys

CITY = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
d = json.load(open(CITY))
print("top-level keys:", len(d), sorted(d.keys()))
print("refresh_revision:", d.get("refresh_revision"))

def find_photo_rows(obj, path=""):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            out += find_photo_rows(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out += find_photo_rows(v, path + "/" + str(i))
    return out

# locate DOJO venue
for v in d["venues"]:
    blob = json.dumps(v)
    if "dojo" in blob.lower():
        print("VENUE:", v.get("id"), "|", v.get("name"), "|", v.get("slug"))
        for g in v.get("photos") or []:
            print("  group:", g.get("id"), "|", g.get("label"))
            for row in g.get("images") or []:
                print("    row:", json.dumps(row, indent=2)[:1200])
        break
