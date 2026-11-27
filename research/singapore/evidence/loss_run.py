import json, sys
sys.path.insert(0, '/home/joe/repo_dev/hermes-skills/plan-event/scripts')
from city_store import loss_check
old = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/evidence/city.pre-r8.json'))
new = json.load(open('/home/joe/repo_dev/coe-events/research/singapore/city/city.json'))
losses = loss_check(old, new)
print(json.dumps(losses, indent=1)[:4000])
