import json, hashlib
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
raw = open(p, "rb").read()
d = json.loads(raw)
for indent in (1, 2):
    for nl in ("", "\n"):
        out = json.dumps(d, indent=indent, sort_keys=False, ensure_ascii=False) + nl
        b = out.encode()
        print(indent, repr(nl), "identical", b == raw, "len", len(b), len(raw),
              "sha", hashlib.sha256(b).hexdigest()[:12])
print("tail bytes", raw[-5:])
