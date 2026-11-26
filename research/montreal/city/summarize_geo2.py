import json, os
BASE="/home/joe/repo_dev/coe-events/research/montreal/city/geocode"
for tag in ("raw2","raw3"):
    print("\n#####",tag)
    for fn in sorted(os.listdir(BASE)):
        if not fn.startswith(tag+"-"): continue
        rows=json.load(open(os.path.join(BASE,fn)))
        print("\n==",fn)
        for r in rows[:3]:
            a=r.get("address") or {}
            print("   ",r.get("lat"),r.get("lon"),"|",r.get("category"),r.get("type"),"| name:",r.get("name"),
                  "| hn:",a.get("house_number"),"|",r.get("display_name","")[:130])
