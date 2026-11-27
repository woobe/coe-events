import json
s=json.load(open('research/singapore/city/city.json'))
def f(v,k): return (v.get('fields',{}).get(k) or {}).get('value')
for vid,v in s['venues'].items():
    print('='*100)
    print(vid, '|', f(v,'display_name'))
    print('SOURCE:', f(v,'source_url'))
    print('BOOK  :', f(v,'booking_url'))
    print('ADDR  :', f(v,'address'))
    print('ABOUT :', str(f(v,'about'))[:400])
    print('TRANSIT:', str(f(v,'transit_access'))[:200])
