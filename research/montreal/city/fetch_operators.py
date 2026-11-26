import json, os, re, ssl, time, urllib.request
BASE = "/home/joe/repo_dev/coe-events/research/montreal/city"
OUT = BASE + "/captures"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
URLS = [
 ("mtl-3c2599f5b2b4","home","https://2727coworking.com/"),
 ("mtl-3c2599f5b2b4","meeting","https://2727coworking.com/en/meeting-rooms/"),
 ("mtl-a200486a6df1","rental","https://espaceaxc.com/en/"),
 ("mtl-13ee7228e4b2","rooms","https://collectifmtl.com/en/"),
 ("mtl-2fc617abde76","home","https://www.communidee.ca/"),
 ("mtl-bfeec3cc37f4","centre","https://fondhum.com/fr/centre"),
 ("mtl-583f8727f3f3","home","https://disstorsion.com/en/"),
 ("mtl-b1e93c63b00b","rental","https://kawalees.ca/event-space-rental/"),
 ("mtl-9e988109561c","home","https://groupe3737.com/en/"),
 ("mtl-a2488d6b9f36","studio","https://imagemotion.com/studio/"),
 ("mtl-8ef00c25a80d","home","https://www.kpturstudio.com/"),
 ("mtl-9b1cfe2df6f0","home","https://en.lebalcon.ca/"),
 ("mtl-8aee03975c77","home","https://lestudiotd.com/"),
 ("mtl-edf77b252f04","home","https://connectionsralia.com/"),
 ("mtl-281cff0a7a6d","home","https://yasminfgow.com/loft-108/"),
 ("mtl-2729e116a7ed","home","https://maisontela.com/"),
 ("mtl-32894124b903","home","https://miralestudios.com/"),
 ("mtl-184b7a111981","home","https://centrebell.ca/en/food-and-beverage/restaurants/mise-au-jeu"),
 ("mtl-6f6753b2d241","home","http://monloftprive.com/"),
 ("mtl-b6318fa3d1f6","home","https://mcauslan.com/en/lannexe/"),
 ("mtl-eeca8449dbec","home","https://www.studiocuero.com/"),
 ("mtl-eb0452047e00","home","https://tangorenaissance.com/"),
 ("mtl-d0e27aa38d40","rental","https://sat.qc.ca/fr/louer-la-sat"),
 ("mtl-9e195a901d0f","home","https://maisonphilanthropiquenotman.org/"),
 ("mtl-5aff2a80fdee","home","https://genesishq.ca/"),
]
def fetch(url, timeout=35):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
        "Accept":"text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"en-CA,en;q=0.9,fr;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as r:
        return r.status, r.headers.get("content-type",""), r.read()
rep={}
for vid, tag, url in URLS:
    try:
        st, ct, data = fetch(url)
    except Exception as e:
        print(vid, tag, "ERR", repr(e)[:110], url, flush=True); rep[vid+":"+tag]={"url":url,"error":repr(e)[:200]}; continue
    name = re.sub(r"[^a-z0-9]+","-",url.split("//",1)[-1])[:55].strip("-")
    p=os.path.join(OUT,"op-"+vid+"-"+tag+"-"+name+".html")
    open(p,"wb").write(data)
    txt=data.decode("utf-8","replace")
    rep[vid+":"+tag]={"url":url,"status":st,"bytes":len(data),"file":p,
        "imgs":re.findall(r'(?:src|data-src|content)="(https?://[^"]+\.(?:jpe?g|png|webp)[^"]*)"',txt)[:30],
        "pdfs":re.findall(r'href="(https?://[^"]+\.pdf)"',txt)[:10]}
    print(vid, tag, st, len(data), url, flush=True)
    time.sleep(0.4)
json.dump(rep,open(BASE+"/operator-fetch-report.json","w"),indent=1,ensure_ascii=False)
print("done")
