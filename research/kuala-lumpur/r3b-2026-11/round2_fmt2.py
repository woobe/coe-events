import json
from pathlib import Path
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city")
b = (BASE / "city.pre-r3b.json").read_bytes()
o = json.loads(b.decode("utf-8"))
for indent in (1, 2, 4, None):
    for ea in (False, True):
        s = (json.dumps(o, indent=indent, sort_keys=True, ensure_ascii=ea) + "\n").encode("utf-8")
        if s == b:
            print("MATCH indent=%r ensure_ascii=%r len=%d" % (indent, ea, len(s)))
        else:
            print("no   indent=%r ensure_ascii=%r len=%d" % (indent, ea, len(s)))
