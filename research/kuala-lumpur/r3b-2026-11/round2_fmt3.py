import json
from pathlib import Path
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city")
b = (BASE / "city.pre-r3b.json").read_bytes()
o = json.loads(b.decode("utf-8"))
s = (json.dumps(o, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
print(len(b), len(s))
for i, (x, y) in enumerate(zip(b, s)):
    if x != y:
        print("first diff at", i)
        print("file:", b[max(0, i - 120):i + 120])
        print("ours:", s[max(0, i - 120):i + 120])
        break
else:
    print("prefix equal; length diff", len(b) - len(s))
