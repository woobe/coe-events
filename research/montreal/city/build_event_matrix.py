import json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
CHECK="2026-11-26"
themes=["ai","machine_learning","data_science","web3","crypto","blockchain"]
lanes=[
 dict(key="luma_city",url="https://lu.ma/montreal",pages=1,state="opened",hits=0,ret=0,disp="opened-empty-for-2027"),
 dict(key="luma_alias",url="https://lu.ma/mtl ; https://lu.ma/montr%C3%A9al",pages=2,state="blocked",hits=0,ret=0,disp="blocked-404"),
 dict(key="luma_organiser",url="https://lu.ma/decentralized_ai_events?period=past",pages=1,state="opened",hits=0,ret=0,disp="opened-no-2027-occurrence"),
 dict(key="meetup",url="https://www.meetup.com/find/?keywords=ai&location=ca--montreal (+6 group pages)",pages=7,state="opened",hits=0,ret=0,disp="opened-no-2027-theme-event"),
 dict(key="eventbrite",url=None,pages=1,state="opened",hits=None,ret=0,disp="opened-no-2027-theme-event"),
 dict(key="miragather_main",url="https://miragather.com/",pages=1,state="opened",hits=None,ret=None,disp=None),
 dict(key="miragather_side",url="https://miragather.com/?tab=side",pages=1,state="opened",hits=None,ret=0,disp="duplicate-of-main-payload"),
 dict(key="miragather_ai",url="https://miragather.com/ai",pages=1,state="opened",hits=None,ret=None,disp=None),
 dict(key="aitinkerers",url="https://aitinkerers.org/all_cities ; https://montreal.aitinkerers.org/",pages=2,state="opened",hits=0,ret=0,disp="opened-empty-for-2027"),
]
EB={"ai":"https://www.eventbrite.ca/d/canada--montreal/ai/","machine_learning":"https://www.eventbrite.ca/d/canada--montreal/machine-learning/","data_science":"https://www.eventbrite.ca/d/canada--montreal/data-science/","web3":"https://www.eventbrite.ca/d/canada--montreal/web3/","crypto":"https://www.eventbrite.ca/d/canada--montreal/crypto/","blockchain":"https://www.eventbrite.ca/d/canada--montreal/blockchain/"}
EBHITS={"ai":16,"machine_learning":20,"data_science":19,"web3":20,"crypto":19,"blockchain":19}
cells=[]
for t in themes:
    for l in lanes:
        cell=dict(theme=t,lane=l["key"],url=l["url"] or EB[t],checked_on=CHECK,pages_read=l["pages"],state=l["state"],
                  raw_hits=l["hits"],retained=l["ret"],disposition=l["disp"])
        if l["key"]=="eventbrite":
            cell["raw_hits"]=EBHITS[t]; cell["note"]="All cards on the theme landing page; no card prints a 2027 date in the six themes. 'What Does My Business Actually Need in 2027?' starts 2026-12-28; 'Women in Tech 2027' starts 2027-02-25 and is a recruiting event, outside the six themes."
        if l["key"] in ("miragather_main","miragather_ai"):
            if t=="ai":
                cell["raw_hits"]=1; cell["retained"]=1; cell["disposition"]="retained (ALL IN 2027-09-22/23)"
                cell["note"]="MiraGather serves 2 Montreal records in total; only ALL IN is an AI-theme event."
            else:
                cell["raw_hits"]=0; cell["retained"]=0; cell["disposition"]="opened-empty"
        if l["key"]=="miragather_side" and t=="ai":
            cell["raw_hits"]=1; cell["note"]="Side tab serves the same payload as main; the ALL IN hit is a duplicate of the main-lane capture, not a second event."
        if l["key"]=="luma_city":
            cell["note"]="194 names in the served Luma city payload; 0 occurrences of 2027."
        if l["key"]=="meetup":
            cell["note"]="2027 dates found only on a JavaScript group (12 Jan, 9 Feb, 9 Mar, 13 Apr 2027), outside the six themes."
        cells.append(cell)
summary={"schema":"mtl-event-matrix/1","checked_on":CHECK,"themes":themes,
 "lanes":[l["key"] for l in lanes],"cells":len(cells),
 "attempted":len(cells),"blocked":sum(1 for c in cells if c["state"]=="blocked"),
 "opened":sum(1 for c in cells if c["state"]=="opened"),
 "retained_unique":1,"retained_duplicates":1,
 "direct_flagship_checks":[
   {"name":"Startupfest 2027","url":"https://www.startupfest.com/","date":"2027-07-07/09","result":"retained"},
   {"name":"Montreal Family Office & High Net Worth Conference","url":"https://dc-finance.com/","date":"2027-05-03","result":"retained"},
 ],
 "totals_note":"54 cells attempted; 6 alias cells blocked (both Luma aliases 404); 48 opened; one unique 2027 theme event retained from the lanes (ALL IN, duplicated by main/side/AI captures); two further 2027 events retained from direct flagship organiser pages (Startupfest, DC Finance). Eventbrite yields broad theme cards but no 2027 theme event."}
json.dump({"summary":summary,"cells":cells},open(BASE+"/event-matrix.json","w"),indent=1,ensure_ascii=False)
print(json.dumps(summary,indent=1))
