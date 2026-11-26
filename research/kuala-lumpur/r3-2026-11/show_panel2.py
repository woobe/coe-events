#!/usr/bin/env python3
"""Extract a venue panel's gallery from a rendered page and print image rows + labels."""
import re
import sys

path, vid = sys.argv[1], sys.argv[2]
html = open(path, encoding='utf-8').read()
marker = 'id="panel-%s"' % vid
i = html.find(marker)
if i < 0:
    print('panel not found')
    sys.exit(1)
end = html.find('</details>', i)
chunk = html[i:end]
print('panel bytes', len(chunk))
for m in re.finditer(r'<img[^>]*>', chunk):
    tag = m.group(0)
    src = re.search(r'src="([^"]*)"', tag)
    alt = re.search(r'alt="([^"]*)"', tag)
    print('IMG alt=%r src=...%s' % (alt.group(1)[:60] if alt else None, (src.group(1) or '')[-55:]))
for label in ('Exterior', 'Lobby', 'Render (not a room photo)'):
    print('label %-24s x%d' % (label, chunk.count('>' + label + '<')))
print('figure count', chunk.count('<figure'))
