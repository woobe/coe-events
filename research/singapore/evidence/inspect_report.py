import json
r = json.load(open('research/singapore/evidence/venue-report.json'))
for row in r['venues']:
    if row['id'] in ('sg-1f9af9e53c6a', 'sg-31b594bd4607', 'sg-9d1a91764baf', 'sg-afe29d71b4e8'):
        print(json.dumps(row, indent=1))
print('--- no-photo venues')
for vid, c in r['photos'].items():
    if c['total'] == 0:
        print(vid, c)
print('--- rights mix')
import collections
rm = collections.Counter()
for vid, ps in json.load(open('research/singapore/city/city.json'))['photos'].items():
    for p in ps:
        if p.get('url') and not p.get('withheld'):
            rm[p.get('rights_basis')] += 1
print(rm)
