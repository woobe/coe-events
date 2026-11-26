import json
from pathlib import Path
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city")
b = (BASE / "city.pre-r3b.json").read_bytes()
o = json.loads(b.decode("utf-8"))
for indent in (1, 2):
    for sk in (False, True):
        for ea in (False, True):
            s = (json.dumps(o, indent=indent, sort_keys=sk, ensure_ascii=ea) + "\n").encode("utf-8")
            print("indent=%r sort=%r ascii=%r len=%d match=%s" % (indent, sk, ea, len(s), s == b))
