#!/usr/bin/env python3
"""Extract one venue panel (figure/gallery block) from a rendered page."""
import re
import sys

path, vid = sys.argv[1], sys.argv[2]
html = open(path, encoding='utf-8').read()
# each venue panel carries id="venue-<vid>" or data-record="<vid>"; find the anchor
m = re.search(r'id="[^"]*%s[^"]*"' % re.escape(vid), html)
print('anchor', m.group(0) if m else None, 'at', m.start() if m else None)
if m:
    start = max(0, m.start() - 200)
    chunk = html[start:m.start() + 6000]
    for line in chunk.splitlines():
        if any(k in line for k in ('img', 'Exterior', 'Lobby', 'Render', 'gallery', 'figure', 'photo')):
            print(line[:400])
