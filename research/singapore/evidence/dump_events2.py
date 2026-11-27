import json
s=json.load(open('research/singapore/city/city.json'))
ev=s['events']
print(type(ev), len(ev))
for k,v in ev.items():
    print('='*90)
    print(k)
    print(json.dumps(v, indent=1, ensure_ascii=False)[:2200])
