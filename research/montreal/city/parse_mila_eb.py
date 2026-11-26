import re
BASE="/home/joe/repo_dev/coe-events/research/montreal/city/captures"
def read(p): return open(BASE+"/"+p,encoding="utf-8",errors="replace").read()
mi=read("ev-mila.html")
i=mi.find("March 22")
print("MILA CTX:", re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",mi[max(0,i-1500):i+300]))[-1400:])
print("\nMILA links near:")
for m in re.finditer(r'href="([^"]*events[^"]*)"', mi):
    print(" ",m.group(1)[:140])
print("\n\nEB AIFAIR dates:")
eb=read("ev-eb-ai.html")
i=eb.find("2005037372756")
print(re.sub(r"\s+"," ",eb[max(0,i-800):i+2500])[:2500])
