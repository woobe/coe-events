import json, re
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
R=json.load(open(BASE+"/venue-fetch-report.json"))
S=json.load(open(BASE+"/city.json"))
SKIP=re.compile(r"eventective|tagvenue|google|facebook|twitter|instagram|pinterest|youtube|linkedin|tiktok|schema\.org|w3\.org|gstatic|cloudflare|jquery|fonts|doubleclick|googletag|cdnjs|jsdelivr|bootstrap|getterms|mixpanel|rollbar|wix|squarespace|shopify|stripe|gmpg", re.I)
want=["mtl-bfeec3cc37f4","mtl-eeca8449dbec","mtl-eb0452047e00","mtl-edf77b252f04","mtl-be24c9002459","mtl-5aff2a80fdee","mtl-d0e27aa38d40","mtl-9e195a901d0f"]
for vid in want:
    r=R.get(vid,{})
    print("\n==",vid,S["venues"][vid]["name"],r.get("status"))
    for u in r.get("links",[]):
        if not SKIP.search(u):
            print("  ",u[:140])
