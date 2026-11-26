import re, json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city/captures"
def read(p): return open(p,encoding="utf-8",errors="replace").read()

mg=read(BASE+"/ev-miragather-main.html")
print("MIRAGATHER len",len(mg))
for m in re.finditer(r'.{200}Montreal.{300}', mg):
    s=m.group(0)
    if "2027" in s:
        print("---",s[:500].replace("\n"," "))
        break
# event-ish keys
for key in ("startDate","eventName","organizerName","city"):
    idx=mg.find('"'+key+'"')
    print(key,"first idx",idx, mg[idx:idx+160] if idx>0 else "")

print("\n\nEB AI cards")
eb=read(BASE+"/ev-eb-ai.html")
for m in re.finditer(r'aria-label="View ([^"]{5,140})"', eb):
    print(" ",m.group(1)[:120])
print("\nEB AI date json")
for m in re.finditer(r'"(?:startDate|start_date|dateTime)"\s*:\s*"([^"]+)"', eb):
    print(" ",m.group(1)); 
    break
print("count date keys", len(re.findall(r'"(?:startDate|start_date|dateTime)"', eb)))

print("\n\nLUMA deai names")
lu=read(BASE+"/ev-luma-deai-past.html")
for m in re.finditer(r'"name":"([^"]{3,80})"', lu):
    n=m.group(1)
    if any(w in n.lower() for w in ("ai","crypto","web3","blockchain","machine","data")):
        print(" ",n)
print("count",len(re.findall(r'"name":"',lu)))

print("\n\nMILA around March 22")
mi=read(BASE+"/ev-mila.html")
i=mi.find("March 22")
print(re.sub(r"<[^>]+>"," ",mi[max(0,i-1200):i+400])[:1200])
