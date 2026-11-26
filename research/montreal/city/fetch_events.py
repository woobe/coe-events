import json, os, re, ssl, time, urllib.request
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
OUT=BASE+"/captures"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36"
URLS=[
("ev-luma-montreal","https://lu.ma/montreal"),
("ev-luma-mtl","https://lu.ma/mtl"),
("ev-luma-montreal-fr","https://lu.ma/montr%C3%A9al"),
("ev-luma-deai-past","https://lu.ma/decentralized_ai_events?period=past"),
("ev-eb-tech","https://www.eventbrite.ca/d/canada--montreal/tech/"),
("ev-eb-ai","https://www.eventbrite.ca/d/canada--montreal/ai/"),
("ev-eb-blockchain","https://www.eventbrite.ca/d/canada--montreal/blockchain/"),
("ev-eb-crypto","https://www.eventbrite.ca/d/canada--montreal/crypto/"),
("ev-eb-web3","https://www.eventbrite.ca/d/canada--montreal/web3/"),
("ev-eb-ds","https://www.eventbrite.ca/d/canada--montreal/data-science/"),
("ev-eb-ml","https://www.eventbrite.ca/d/canada--montreal/machine-learning/"),
("ev-meetup-find","https://www.meetup.com/find/?keywords=ai&location=ca--montreal"),
("ev-meetup-pydata","https://www.meetup.com/pydata-montreal/"),
("ev-meetup-aiml","https://www.meetup.com/ai-ml-montreal/"),
("ev-meetup-datadrinks","https://www.meetup.com/data-drinks-montreal/"),
("ev-meetup-gdg","https://www.meetup.com/gdg-montreal/"),
("ev-meetup-blockchain","https://www.meetup.com/blockchain-montreal/"),
("ev-meetup-crypto","https://www.meetup.com/montreal-crypto/"),
("ev-miragather-main","https://miragather.com/"),
("ev-miragather-side","https://miragather.com/?tab=side"),
("ev-miragather-ai","https://miragather.com/ai"),
("ev-aitinkerers-all","https://aitinkerers.org/all_cities"),
("ev-aitinkerers-mtl","https://montreal.aitinkerers.org/"),
("ev-c2","https://c2montreal.com/"),
("ev-startupfest","https://www.startupfest.com/"),
("ev-mtlconnecte","https://mtlconnecte.ca/"),
("ev-scaleai","https://www.scaleai.ca/events/"),
("ev-mila","https://mila.quebec/en/events"),
("ev-ivado","https://ivado.ca/en/events/"),
("ev-allin","https://allin.ai/"),
]
rep={}
for slug,url in URLS:
    try:
        req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html","Accept-Language":"en-CA,en;q=0.9,fr;q=0.8"})
        with urllib.request.urlopen(req,timeout=45,context=ssl.create_default_context()) as r:
            st=r.status; ct=r.headers.get("content-type",""); data=r.read()
    except Exception as e:
        print(slug,"ERR",repr(e)[:100],flush=True); rep[slug]={"url":url,"error":repr(e)[:160]}; time.sleep(0.8); continue
    p=os.path.join(OUT,slug+".html"); open(p,"wb").write(data)
    txt=data.decode("utf-8","replace")
    hits=re.findall(r".{0,90}2027.{0,90}",txt)
    rep[slug]={"url":url,"status":st,"bytes":len(data),"file":p,"n2027":len(hits),"hits":hits[:12]}
    print(slug,st,len(data),"2027hits",len(hits),flush=True)
    time.sleep(0.8)
json.dump(rep,open(BASE+"/event-fetch-report.json","w"),indent=1,ensure_ascii=False)
print("done")
