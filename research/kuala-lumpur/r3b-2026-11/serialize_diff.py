import json
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/city/city.json"
raw = open(p, encoding="utf-8").read()
d = json.loads(raw)
out = json.dumps(d, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
for i, (a, b) in enumerate(zip(raw, out)):
    if a != b:
        print("first diff at", i)
        print("RAW:", repr(raw[max(0, i-120):i+160]))
        print("OUT:", repr(out[max(0, i-120):i+160]))
        break
else:
    print("prefix equal", len(raw), len(out))
