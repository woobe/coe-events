import json
s=json.load(open('research/singapore/city/city.json'))
for e in s['events']:
    print('='*90)
    print(json.dumps(e, indent=1, ensure_ascii=False)[:2500])
print('=== sources_consulted count', len(s['sources_consulted']))
for src in s['sources_consulted']:
    print(src.get('lane'), '|', src.get('title'), '|', src.get('url'), '|', src.get('disposition'), '| yield', src.get('event_yield'), '| pages', src.get('pages_read'))
