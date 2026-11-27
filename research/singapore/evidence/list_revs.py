import json, os, glob
root='research'
for p in sorted(glob.glob(root+'/*/city/city.json')):
    try:
        s=json.load(open(p))
    except Exception as e:
        print(p,'ERR',e); continue
    print(p, 'rev=',s.get('refresh_revision'), 'venues=',len(s.get('venues',{})), 'events=',len(s.get('events',{})), 'holidays=',len(s.get('holidays',[])), 'gaps=',len(s.get('declared_gaps') or []))
