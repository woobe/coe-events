import json
s = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/city/city.json'))
jobs = []
for vid, v in s['venues'].items():
    f = v['fields']
    jobs.append({'id': vid, 'url': f['source_url']['value'],
                 'capture': 'src-' + vid})
json.dump(jobs, open('/home/joe/repo_dev/coe-events/research/singapore/evidence/venues_fetch.json', 'w'), indent=1)
print(len(jobs))
