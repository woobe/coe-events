import re, json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city/captures"
mg=open(BASE+"/ev-miragather-main.html",encoding="utf-8",errors="replace").read()
print("Montreal 2027 records:")
seen=set()
for m in re.finditer(r'"startDate":"2027-\d\d-\d\d"', mg):
    w=mg[max(0,m.start()-900):m.start()+400]
    city=re.search(r'"city":\[(.*?)\]', w)
    ev=re.findall(r'"event":"([^"]{3,160})"', w)
    sd=re.search(r'"startDate":"(2027-\d\d-\d\d)"', w).group(1)
    ed=re.search(r'"endDate":"([^"]*)"', w)
    org=re.findall(r'"organizer":\{?"?([^",]{2,80})', w)
    if city and "Montreal" in city.group(1):
        key=(ev[-1] if ev else "?", sd)
        if key in seen: continue
        seen.add(key)
        print(" ", sd, "|", ev[-1] if ev else "?", "| org:", org[-1] if org else "?")
print("count",len(seen))

print("\nAll Montreal records any year:")
seen2=set()
for m in re.finditer(r'"city":\["Montreal"\]', mg):
    w=mg[max(0,m.start()-600):m.start()+500]
    ev=re.findall(r'"event":"([^"]{3,160})"', w)
    sd=re.findall(r'"startDate":"(\d{4}-\d\d-\d\d)"', w)
    if ev and sd:
        k=(ev[-1],sd[-1])
        if k in seen2: continue
        seen2.add(k); print(" ",sd[-1],"|",ev[-1])
print("count",len(seen2))
