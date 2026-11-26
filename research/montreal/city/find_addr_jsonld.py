import json, re, glob
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
S=json.load(open(BASE+"/city.json"))
for vid,v in S["venues"].items():
    if v["fields"]["address"].get("quote"): continue
    print("\n==",vid,v["name"])
    for p in sorted(glob.glob(BASE+"/captures/"+vid+"-*.html")):
        raw=open(p,encoding="utf-8",errors="replace").read()
        for m in re.finditer(r'"(?:streetAddress|street_address)"\s*:\s*"([^"]{5,120})"',raw):
            print("   JSONLD",m.group(1))
        for m in re.finditer(r'(?:itemprop="streetAddress"[^>]*>)([^<]{5,120})',raw):
            print("   ITEMPROP",m.group(1))
        break
