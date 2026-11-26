import json, re
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
R=json.load(open(BASE+"/event-fetch-report.json"))
for slug in ["ev-luma-deai-past","ev-eb-tech","ev-eb-ai","ev-eb-crypto","ev-eb-web3","ev-eb-ds","ev-eb-ml","ev-meetup-find","ev-startupfest","ev-mtlconnecte","ev-scaleai","ev-mila","ev-ivado","ev-aitinkerers-mtl","ev-aitinkerers-all"]:
    r=R.get(slug,{})
    print("\n#####",slug,r.get("url"),r.get("n2027"))
    for h in (r.get("hits") or [])[:8]:
        print("   ",re.sub(r"<[^>]+>"," ",h)[:180].replace("\\n"," "))
