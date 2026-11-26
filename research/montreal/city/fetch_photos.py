import json, io, hashlib, ssl, time, urllib.request
from PIL import Image
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
specs=json.load(open(BASE+"/photo-specs.json"))
cache={}
out={}
for i,s in enumerate(specs):
    url=s["url"]
    if url in cache:
        meta=cache[url]
    else:
        meta={"status":None,"content_type":None,"bytes":None,"w":None,"h":None,"err":None}
        try:
            req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"image/avif,image/webp,image/*,*/*;q=0.8","Referer":s["source_page"]})
            with urllib.request.urlopen(req,timeout=40,context=ssl.create_default_context()) as r:
                data=r.read()
                meta["status"]=r.status; meta["content_type"]=r.headers.get("content-type")
                meta["bytes"]=len(data)
                try:
                    im=Image.open(io.BytesIO(data)); meta["w"],meta["h"]=im.size
                except Exception as e:
                    meta["err"]="dims:"+repr(e)[:60]
        except Exception as e:
            meta["err"]=repr(e)[:120]
        cache[url]=meta
        time.sleep(0.25)
    rec={
      "url":url,"alt":s["alt"],"alt_basis":"operator page caption or file name",
      "view_kind":s["view_kind"],"room":s["room"],"source_page":s["source_page"],
      "rights":"Operator gallery asset; © {}. Hotlinked from the operator's own page with attribution; the page publishes no separate licence text.".format(s["attribution"]),
      "attribution":s["attribution"],"checked_on":"2026-11-26",
      "placement_proof":s["placement"],"hotlink_ok":bool(meta["status"]==200),
      "verified":{"status":meta["status"],"content_type":meta["content_type"],"bytes":meta["bytes"]},
      "withheld":False}
    if meta["w"]:
        rec["dimensions"]={"width":meta["w"],"height":meta["h"]}
        rec["thumb_note"]="{}x{} original".format(meta["w"],meta["h"])
    if meta["err"]: rec["fetch_note"]=meta["err"]
    out.setdefault(s["vid"],[]).append(rec)
    print(i,s["vid"],meta["status"],meta["w"],meta["h"],meta["bytes"],url[:90],flush=True)
json.dump(out,open(BASE+"/photo-records.json","w"),indent=1,ensure_ascii=False)
print("records",sum(len(v) for v in out.values()))
