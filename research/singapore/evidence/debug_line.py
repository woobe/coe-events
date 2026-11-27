from pathlib import Path
import re
CAP = Path('/home/joe/repo_dev/coe-events/research/singapore/city/captures')
p = CAP / 're-2027-govware.txt'
print(p.exists(), p)
text = p.read_text(encoding='utf-8', errors='replace')
for line in text.splitlines():
    m = re.match(r'^\s*(\d+)\|\s?(.*)$', line)
    if m and '25 - 27 October 2027' in m.group(2):
        print('MATCH', m.group(1), repr(m.group(2)[:100]))
print([l for l in text.splitlines() if 'October 2027' in l][:3])
