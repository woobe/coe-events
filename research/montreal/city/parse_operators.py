import json, re, os, glob
from html.parser import HTMLParser
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
class T(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0; self.imgs=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag in ("script","style","noscript"): self.skip+=1
        if tag=="img":
            self.imgs.append({"src":d.get("src") or d.get("data-src") or "", "alt":d.get("alt") or "", "title":d.get("title") or ""})
        if tag in ("p","div","br","li","h1","h2","h3","h4","section","article","tr"): self.parts.append("\n")
    def handle_endtag(self,tag):
        if tag in ("script","style","noscript") and self.skip: self.skip-=1
    def handle_data(self,data):
        if not self.skip:
            t=" ".join(data.split())
            if t: self.parts.append(t+" ")
def text_of(path):
    raw=open(path,encoding="utf-8",errors="replace").read()
    p=T(); p.feed(raw)
    txt="".join(p.parts)
    txt=re.sub(r"[ \t]+"," ",txt)
    txt=re.sub(r"\n\s*\n+","\n",txt)
    return txt, p.imgs
KW=re.compile(r"(ouvert|open|heure|hour|h\b|am\b|pm\b|location|rental|louer|réserver|book|bureau|suite|adresse|address|Montréal|Québec|capacit|personnes|people|invit|guest|minute|minimum|jusqu|until|soir|evening|nuit|night)", re.I)
for path in sorted(glob.glob(BASE+"/captures/op-*.html")):
    txt,imgs=text_of(path)
    base=os.path.basename(path)
    open(BASE+"/captures/"+base.replace(".html",".txt"),"w").write(txt)
    print("\n\n########",base,"| chars",len(txt),"| imgs",len(imgs))
    # address-ish lines
    for line in txt.split("\n"):
        if re.search(r"Montr[eé]al|Qu[eé]bec|H\d[A-Z] ?\d[A-Z]\d|QC\b|Canada", line) and len(line)<220:
            print("  ADDR>",line.strip()[:200])
    # hours-ish lines
    n=0
    for line in txt.split("\n"):
        if re.search(r"\b\d{1,2}\s*(?:h|am|pm)\b", line, re.I) and len(line)<260:
            print("  TIME>",line.strip()[:240]); n+=1
            if n>=8: break
    for im in imgs[:12]:
        if im["src"]: print("  IMG>",im["src"][:120],"| alt:",im["alt"][:80],"| title:",im["title"][:60])
