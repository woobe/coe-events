import json
p = "/home/joe/repo_dev/coe-events/research/montreal/city/city.json"
s = json.load(open(p))
vids = list(s['venues'])
print("VENUE IDS:", vids)
v = s['venues'][vids[0]]
print("\nVENUE KEYS:", list(v))
print(json.dumps(v, indent=1, ensure_ascii=False)[:3500])
print("\nPHOTOS keys sample:", list(s['photos'])[:5])
k = list(s['photos'])[0]
print("PHOTO[%s]:" % k, json.dumps(s['photos'][k], indent=1, ensure_ascii=False)[:2500])
print("\nEVENTS:", json.dumps(s['events'], indent=1, ensure_ascii=False)[:2500])
print("\nCOVERAGE:", json.dumps(s['coverage'], indent=1, ensure_ascii=False)[:2000])
print("\nHOLIDAY_REGISTRY keys:", list(s['holiday_registry']))
print(json.dumps(s['holiday_registry'], indent=1, ensure_ascii=False)[:2500])
print("\nLOCAL_REQ:", json.dumps(s['local_requirements'], indent=1, ensure_ascii=False)[:1500])
print("\nSOURCES[0]:", json.dumps(s['sources_consulted'][0], indent=1, ensure_ascii=False)[:1500])
