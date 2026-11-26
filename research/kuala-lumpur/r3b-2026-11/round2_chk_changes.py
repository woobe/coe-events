import json
p = "/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11/photo-changes.json"
d = json.load(open(p))
for e in d:
    if e["venue_id"] == "kl-977b423768cd":
        print(json.dumps(e, indent=1, ensure_ascii=False))
