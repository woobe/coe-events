import json, re
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
R=json.load(open(BASE+"/venue-fetch-report.json"))
S=json.load(open(BASE+"/city.json"))
SKIP=re.compile(r"eventective|tagvenue|peerspace|google|facebook|twitter|instagram|pinterest|youtube|linkedin|tiktok|schema\.org|w3\.org|gstatic|cloudflare|jquery|fonts|doubleclick|googletag|cdnjs|jsdelivr|bootstrap|getterms|apple\.com|wa\.me|maps\.", re.I)
for vid,r in sorted(R.items()):
    name=S["venues"][vid]["name"]
    print("\n==",vid,"|",name,"|",r.get("status"),r.get("bytes"))
    if r.get("error"): print("  ERR",r["error"]); continue
    ext=[u for u in r.get("links",[]) if not SKIP.search(u)]
    # keep likely venue domains
    seen=[]
    for u in ext:
        d=re.sub(r"^https?://(www\.)?","",u).split("/")[0]
        if d not in seen:
            seen.append(d); print("  LINK",u[:120])
    print("  imgs",len(r.get("images",[])), "| addr:", (r.get("addr_hits") or [None])[0])
