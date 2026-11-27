import json
d = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/evidence/listing_parse.json'))
for vid in ['sg-1f9af9e53c6a', 'sg-42a07044079a', 'sg-42a16aa5a0df', 'sg-afe29d71b4e8', 'sg-6aaa43c58493']:
    print('=' * 80, vid)
    for im in d[vid]['images']:
        print(' ', im['alt'][:100], '|', im['url'].split(';')[-1][:80])
