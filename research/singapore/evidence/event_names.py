import json
s=json.load(open('research/singapore/city/city.json'))
for k,e in s['events'].items():
    f=e['fields']
    def val(x): return (f.get(x) or {}).get('value')
    print(k, '|', e.get('name'), '|', val('date_range'), '|', val('venue'), '|', val('kind'), '|', val('relevance'), '|', e.get('source_url') or (f.get('source_url') or {}).get('value'))
print('event keys', list(next(iter(s['events'].values())).keys()))
print('field keys', list(next(iter(s['events'].values()))['fields']))
