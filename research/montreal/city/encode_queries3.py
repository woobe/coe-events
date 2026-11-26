import urllib.parse
lines=[l.rstrip("\n") for l in open("/home/joe/repo_dev/coe-events/research/montreal/city/geocode-queries3.txt") if l.strip()]
out=[]
for l in lines:
    vid,q=l.split("|",1)
    out.append(vid+"|"+q+"|"+urllib.parse.quote(q))
open("/home/joe/repo_dev/coe-events/research/montreal/city/geocode-queries3-enc.txt","w").write("\n".join(out)+"\n")
print(len(out))
