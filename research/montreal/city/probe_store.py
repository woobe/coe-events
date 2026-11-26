import json, collections, sys
p = "/home/joe/repo_dev/coe-events/research/montreal/city/city.json"
s = json.load(open(p))
print("TOP KEYS:", list(s))
for k, v in s.items():
    if isinstance(v, (list, dict)):
        print(f"  {k}: {type(v).__name__} len={len(v)}")
    else:
        print(f"  {k}: {v!r}")
print("\nVENUES type/len:", type(s.get('venues')).__name__, len(s.get('venues', [])))
v0 = s['venues'][0] if isinstance(s.get('venues'), list) else None
print("\nVENUE0 KEYS:", list(v0) if v0 else None)
print(json.dumps(v0, indent=1, ensure_ascii=False)[:4000])
