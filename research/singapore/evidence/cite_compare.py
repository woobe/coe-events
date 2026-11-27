import json, collections
for city in ('lisbon', 'kuala-lumpur', 'oslo'):
    s = json.load(open('research/%s/city/city.json' % city))
    miss = 0; total = 0; byf = collections.Counter()
    for v in s['venues'].values():
        for f, e in v['fields'].items():
            total += 1
            if not e.get('quote') or not e.get('source_locator'):
                miss += 1; byf[f] += 1
    print(city, 'fields', total, 'missing', miss)
    print(' ', byf.most_common(8))
