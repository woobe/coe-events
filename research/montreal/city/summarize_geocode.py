import json, glob, os, re, unicodedata
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
S=json.load(open(BASE+"/city.json"))
def norm(s):
    s=unicodedata.normalize("NFKD",s or "").encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+"," ",s).strip()
def tokens(name):
    n=norm(name.split("—")[0])
    stop={"the","and","de","du","des","la","le","les","montreal","studio","espace","space","centre","center","loft","salle","rooms","room","venue","main","cafe","atelier"}
    return {t for t in n.split() if len(t)>2 and t not in stop}
for vid,v in sorted(S["venues"].items()):
    raw=json.load(open(os.path.join(BASE,"geocode","raw-"+vid+".json")))
    qt=open(os.path.join(BASE,"geocode-queries.txt")).read()
    q=[l.split("|",1)[1] for l in qt.splitlines() if l.startswith(vid)][0]
    hn=re.match(r"(\d+[A-Za-z]?)",q)
    hn=hn.group(1) if hn else ""
    nt=tokens(v["name"])
    print("\n==",vid,"|",v["name"],"| q:",q,"| wantHN:",hn,"| nameTokens:",sorted(nt))
    for r in raw[:3]:
        a=r.get("address") or {}
        nm=r.get("name") or ""
        nmn=norm(nm)
        nmatch=any(t in nmn for t in nt) if nm else False
        hnm=norm(a.get("house_number"))==norm(hn)
        print("   -",r.get("lat"),r.get("lon"),"| cat/type:",r.get("category"),r.get("type"),
              "| name:",nm,"| nameMatch:",nmatch,"| hn:",a.get("house_number"),"hnMatch:",hnm)
        print("     dn:",r.get("display_name","")[:150])
