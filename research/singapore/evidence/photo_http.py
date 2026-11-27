import json, urllib.request
s = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/city/city.json'))
urls = []
for vid, ps in s['photos'].items():
    for p in ps:
        if p.get('url') and not p.get('withheld'):
            urls.append((vid, p['url']))
print('total photo urls', len(urls))
bad = []
for vid, u in urls[:12]:
    try:
        req = urllib.request.Request(u, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            print(r.status, vid, u[:90])
    except Exception as e:
        bad.append((vid, u, repr(e)[:80]))
        print('ERR', vid, repr(e)[:80])
print('bad', len(bad))
