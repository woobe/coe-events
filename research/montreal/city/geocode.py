import json, os, re, ssl, time, urllib.request, urllib.parse
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
OUT=BASE+"/geocode"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
Q={
"mtl-1125d1fcdf46":"9475 Rue Meilleur, Montréal, QC H2N 2C5",
"mtl-13ee7228e4b2":"397A Rue Sainte-Catherine Ouest, Montréal, QC H3A 2G3",
"mtl-184b7a111981":"275 Rue Saint-Antoine Ouest, Montréal, QC",
"mtl-1c9b9b2b165a":"1415 Rue Saint-Hubert, Montréal, QC",
"mtl-1e4360518a06":"360 Rue Saint-Jacques, Montréal, QC H2Y 1P5",
"mtl-2729e116a7ed":"9850 Rue Tolhurst, Montréal, QC H3L 2Z8",
"mtl-281cff0a7a6d":"377 Rue Saint-Paul Ouest, Montréal, QC",
"mtl-2fc617abde76":"137 Rue Saint-Ferdinand, Montréal, QC H4C 2S6",
"mtl-32894124b903":"9475 Rue Meilleur, Montréal, QC H2N 2C5",
"mtl-3c2599f5b2b4":"2727 Rue Saint-Patrick, Montréal, QC",
"mtl-583f8727f3f3":"372 Rue Sainte-Catherine Ouest, Montréal, QC",
"mtl-5aff2a80fdee":"4526 Avenue du Parc, Montréal, QC",
"mtl-6f6753b2d241":"9 Rue Sainte-Catherine Est, Montréal, QC H2X 1K3",
"mtl-8aee03975c77":"305 Rue Sainte-Catherine Ouest, Montréal, QC",
"mtl-8ef00c25a80d":"5000 Rue d'Iberville, Montréal, QC",
"mtl-9b1cfe2df6f0":"463 Rue Sainte-Catherine Ouest, Montréal, QC",
"mtl-9e195a901d0f":"51 Rue Sherbrooke Ouest, Montréal, QC H2X 1X2",
"mtl-9e988109561c":"3737 Boulevard Crémazie Est, Montréal, QC H1Z 2K4",
"mtl-a200486a6df1":"800 Rue du Square-Victoria, Montréal, QC H3C 0B4",
"mtl-a2488d6b9f36":"370 Rue Guy, Montréal, QC",
"mtl-a69fecaefa03":"397A Rue Sainte-Catherine Ouest, Montréal, QC H3A 2G3",
"mtl-b1e93c63b00b":"5175A Avenue du Parc, Montréal, QC H2V 4G3",
"mtl-b6318fa3d1f6":"5080 Rue Saint-Ambroise, Montréal, QC H4C 2G1",
"mtl-b911cdc04475":"5570 Avenue Casgrain, Montréal, QC H2T 1X9",
"mtl-bfeec3cc37f4":"1225 Boulevard Saint-Joseph Est, Montréal, QC H2J 1L7",
"mtl-d0e27aa38d40":"1201 Boulevard Saint-Laurent, Montréal, QC H2X 2S6",
"mtl-dd69fc532018":"397A Rue Sainte-Catherine Ouest, Montréal, QC H3A 2G3",
"mtl-eb0452047e00":"4475 Boulevard Saint-Laurent, Montréal, QC H2W 1Z8",
"mtl-edf77b252f04":"4281 Boulevard Saint-Laurent, Montréal, QC H2W 1Z4",
"mtl-eeca8449dbec":"4030 Rue Saint-Ambroise, Montréal, QC",
"mtl-fc4d581ec532":"1250 Rue Guy, Montréal, QC H3H 2L3",
"mtl-be24c9002459":"100 Rue McGill, Montréal, QC",
}
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"application/json"})
    with urllib.request.urlopen(req,timeout=30,context=ssl.create_default_context()) as r:
        return r.status, r.read()
summ={}
for vid,q in Q.items():
    url=("https://nominatim.openstreetmap.org/search?q="+urllib.parse.quote(q)+
         "&format=jsonv2&limit=3&addressdetails=1&extratags=1")
    try:
        st,data=get(url)
        rows=json.loads(data)
    except Exception as e:
        rows=[]; st=repr(e)[:120]
    rec={"venue_id":vid,"query":q,"checked_on":"2026-11-26","provider":"OpenStreetMap Nominatim",
         "request_url":url,"http_status":st,"returned":rows}
    json.dump(rec,open(os.path.join(OUT,vid+".json"),"w"),indent=1,ensure_ascii=False)
    top=rows[0] if rows else None
    summ[vid]={"q":q,"n":len(rows),"name":(top or {}).get("name"),"dn":(top or {}).get("display_name"),
               "lat":(top or {}).get("lat"),"lon":(top or {}).get("lon"),
               "type":(top or {}).get("type"),"cls":(top or {}).get("category"),
               "house":((top or {}).get("address") or {}).get("house_number")}
    print(vid,"|",len(rows),"|",(top or {}).get("name"),"|",(top or {}).get("display_name","")[:110],flush=True)
    time.sleep(1.3)
json.dump(summ,open(BASE+"/geocode-summary.json","w"),indent=1,ensure_ascii=False)
print("done")
