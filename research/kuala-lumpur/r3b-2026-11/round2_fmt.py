import json, hashlib
from pathlib import Path
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/city")
for name in ["city.pre-r3b.json", "city.pre-r3b-round2.json", "city.json"]:
    b = (BASE / name).read_bytes()
    o = json.loads(b.decode("utf-8"))
    for ea in (False, True):
        s = (json.dumps(o, indent=2, sort_keys=True, ensure_ascii=ea) + "\n").encode("utf-8")
        print(name, "ensure_ascii=%s" % ea, "same=%s" % (s == b), "len=%d" % len(s), "file=%d" % len(b))
    print("  first 200:", b[:200])
