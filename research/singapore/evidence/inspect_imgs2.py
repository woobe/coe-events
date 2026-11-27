import json, re
L = json.load(open('research/singapore/evidence/listing_parse.json'))
for vid in ('sg-83af406debab', 'sg-47e22cc263a7', 'sg-5be91e319a02', 'sg-a5d5d094bf2e', 'sg-b5dffa99af1f'):
    print('==', vid, 'imgs', len(L[vid]['images']))
    for im in L[vid]['images'][:6]:
        print('  ', im['alt'][:110], '|', im['url'][-60:])
print('--- addresses')
s = json.load(open('research/singapore/city/city.json'))
for vid, v in s['venues'].items():
    a = v['fields']['address']['value']
    if re.search(r'(Street|Road|Avenue|Boulevard), \d', a) or a.startswith('Bain'):
        print(vid, a)
