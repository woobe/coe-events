import json, re, glob, os
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
S=json.load(open(BASE+"/city.json"))
def text_of(path):
    raw=open(path,encoding="utf-8",errors="replace").read()
    raw=re.sub(r"<script.*?</script>"," ",raw,flags=re.S|re.I)
    raw=re.sub(r"<style.*?</style>"," ",raw,flags=re.S|re.I)
    t=re.sub(r"<[^>]+>","\n",raw)
    t=re.sub(r"&amp;","&",t); t=re.sub(r"&#0?39;|&apos;","'",t); t=re.sub(r"&nbsp;"," ",t)
    return "\n".join(" ".join(l.split()) for l in t.splitlines() if l.strip())
for vid,v in S["venues"].items():
    e=v["fields"]["address"]
    if e.get("quote"): continue
    val=e["value"]
    m=re.match(r"(\d+[A-Za-z]?)",val); hn=m.group(1) if m else ""
    cands=sorted(glob.glob(BASE+"/captures/op-"+vid+"-*.txt"))+sorted(glob.glob(BASE+"/captures/"+vid+"-*.html"))
    found=[]
    for p in cands:
        t=text_of(p)
        for line in t.splitlines():
            if hn and hn in line and ("Montr" in line or "QC" in line or "Quebec" in line or "Qc" in line) and 8<len(line)<160:
                found.append((os.path.basename(p),line))
    print("\n==",vid,v["name"],"|",val)
    for f,l in found[:3]: print("   ",f,"|",l)
