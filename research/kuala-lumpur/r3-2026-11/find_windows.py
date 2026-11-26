import json
import re
from pathlib import Path

CAPS = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11/captures')
PAT = re.compile(r'(\b\d{1,2}(?::\d{2})?\s*(?:am|pm|a\.m\.|p\.m\.)\b[^.\n]{0,60}'
                 r'|\b(?:opening|operating|operation|business|office|staff)\s+hours?\b[^.\n]{0,80}'
                 r'|\b\d{1,2}(?:\.\d{2})?\s*(?:am|pm)\s*(?:-|to|until)\s*\d{1,2}(?:\.\d{2})?\s*(?:am|pm)\b)',
                 re.I)
for path in sorted(CAPS.glob('*.txt')):
    text = path.read_text(encoding='utf-8', errors='replace').splitlines()
    hits = []
    for i, line in enumerate(text, 1):
        if len(line) > 400:
            continue
        if PAT.search(line) and re.search(r'\b(am|pm|hours?)\b', line, re.I):
            hits.append((i, line.strip()[:180]))
    if hits:
        print('==', path.stem)
        for i, line in hits[:6]:
            print('   %d: %s' % (i, line))
