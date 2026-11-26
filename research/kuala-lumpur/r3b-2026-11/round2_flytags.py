import re
html = open("/tmp/flyspaces_dojo.html", encoding="utf-8", errors="replace").read()
# print img tags with alt, in order
for m in re.finditer(r"<img[^>]+>", html):
    tag = m.group(0)
    if "dojo-kl-menara-amplewest" in tag:
        print(tag[:500])
        print("---")
# text near images
idx = html.find("dojo-kl-menara-amplewest-1.jpg")
print("CONTEXT1:", re.sub(r"<[^>]+>", " ", html[max(0, idx-1200):idx+400]).split())
