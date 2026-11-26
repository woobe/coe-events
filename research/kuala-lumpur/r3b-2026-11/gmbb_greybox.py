import lxml.html, re
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11/pages/gmbb-shared-space.html"
doc = lxml.html.fromstring(open(p, errors="replace").read())
for h in doc.iter("h2"):
    name = " ".join(h.text_content().split())
    if "GREY" not in name.upper():
        continue
    block = h.getparent()
    print("H2:", name, "| parent tag/class:", block.tag, block.get("class"))
    for img in block.iter("img"):
        print("   img:", img.get("src"), "| alt:", img.get("alt"), "| class:", img.get("class"))
    # parent of parent too
    up = block.getparent()
    print("  grandparent:", up.tag, up.get("class"))
    for img in up.iter("img"):
        print("   up img:", img.get("src"), "| alt:", img.get("alt"))
