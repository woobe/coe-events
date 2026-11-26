import hashlib, io, json, urllib.request
from PIL import Image

URLS = {
 "W-Studio3": "https://cache.marriott.com/content/dam/marriott-renditions/KULWH/kulwh-meeting-facilities-3802-hor-clsc.jpg?output-quality=70&interpolation=progressive-bilinear&downsize=1920px:*",
 "StR-Astor": "https://cache.marriott.com/content/dam/marriott-renditions/KULXR/kulxr-astor-room-5291-hor-wide.jpg?output-quality=70&interpolation=progressive-bilinear&downsize=2880px:*",
}
for name, url in URLS.items():
    print("==", name)
    for i in range(3):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            im = Image.open(io.BytesIO(data))
            print("  try%d status=%s bytes=%d dims=%s sha=%s" % (
                i + 1, r.status, len(data), im.size, hashlib.sha256(data).hexdigest()[:16]))
        except Exception as e:
            print("  try%d ERR %s %s" % (i + 1, type(e).__name__, e))
