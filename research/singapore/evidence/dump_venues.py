import json
s=json.load(open('research/singapore/city/city.json'))

def f(v,k):
    return (v.get('fields',{}).get(k) or {}).get('value')

for vid,v in s['venues'].items():
    c=f(v,'coordinates')
    pw=f(v,'programme_windows') or {}
    print('|'.join([
        vid,
        str(f(v,'display_name')),
        str(f(v,'address')),
        str(f(v,'lifecycle')),
        (('%s,%s' % (c.get('latitude'),c.get('longitude'))) if isinstance(c,dict) else 'NONE'),
        str(f(v,'capacity')),
        str(f(v,'access_window')),
        '8='+str((pw.get('8') or {}).get('state')),
        '12='+str((pw.get('12') or {}).get('state')),
        str(f(v,'price')),
    ]))
