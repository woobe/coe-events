import re
from pathlib import Path
c = Path('/home/joe/repo_dev/coe-events/research/singapore/city/captures')
n = 0
for p in c.glob('*.txt'):
    t = p.read_text(encoding='utf-8', errors='replace')
    # collapse the doubled line-number prefix produced by fetch.py over to_text.py
    t2 = re.sub(r'(?m)^(\s*\d+)\|\s*\d+\|\s?', r'\1| ', t)
    if t2 != t:
        p.write_text(t2, encoding='utf-8')
        n += 1
print('cleaned', n)
