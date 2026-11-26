import re, json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city/captures"
def read(p): return open(BASE+"/"+p,encoding="utf-8",errors="replace").read()
for theme in ("tech","ai","machine-learning","data-science","web3","crypto","blockchain"):
    t=read("ev-eb-"+("ml" if theme=="machine-learning" else "ds" if theme=="data-science" else theme)+".html")
    names=[]
    for m in re.finditer(r'aria-label="View ([^"]{5,160})"',t):
        n=re.sub(r"&amp;","&",m.group(1))
        if n not in names: names.append(n)
    print(theme,len(names))
    for n in names[:6]: print("   ",n[:90])
lu=read("ev-luma-montreal.html")
print("\nLUMA names count",len(set(re.findall(r'"name":"([^"]{3,80})"',lu))))
for n in list(dict.fromkeys(re.findall(r'"name":"([^"]{3,80})"',lu)))[:10]: print("  ",n)
