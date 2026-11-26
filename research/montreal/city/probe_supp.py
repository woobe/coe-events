import json
p="/home/joe/repo_dev/coe-events/research/montreal/city/holiday-supplement.json"
d=json.load(open(p))
print(list(d))
for k,v in d.items():
    print(k,type(v).__name__,len(v) if hasattr(v,"__len__") else v)
print(json.dumps({k:v for k,v in d.items() if k not in ("coverage","holidays","holiday_rows")},indent=1,ensure_ascii=False)[:1200])
