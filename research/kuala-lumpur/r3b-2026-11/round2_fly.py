import hashlib, urllib.request, os, json
from PIL import Image

base = "https://media.flyspaces.com/venue-photo/venue-photo/final-malaysia/kuala-lumpur/dojo-kl-menara-amplewest/dojo-kl-menara-amplewest-%d.jpg"
outdir = "/tmp/dojo_fly"
os.makedirs(outdir, exist_ok=True)

our = "/tmp/dojo.jpg"
our_h = hashlib.sha256(open(our, "rb").read()).hexdigest()
im = Image.open(our)
print("OUR", im.size, im.mode, os.path.getsize(our), our_h[:16])

for i in range(1, 9):
    url = base % i
    p = os.path.join(outdir, "f%d.jpg" % i)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        open(p, "wb").write(data)
        im = Image.open(p)
        h = hashlib.sha256(data).hexdigest()
        print(i, r.status, im.size, im.mode, len(data), h[:16], "SAME_BYTES" if h == our_h else "")
    except Exception as e:
        print(i, "ERR", type(e).__name__, e)
