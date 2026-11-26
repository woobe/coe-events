import json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
s=json.load(open(BASE+"/city.json"))
print("RUNS:",json.dumps(s["runs"],indent=1,ensure_ascii=False)[:1200])
print("\nEVENT:")
k=list(s["events"])[0]
print(json.dumps(s["events"][k],indent=1,ensure_ascii=False))
print("\nHOLIDAY0:",json.dumps(s["holidays"][1],indent=1,ensure_ascii=False))
print("\nCOVERAGE:")
print(json.dumps(s["coverage"],indent=1,ensure_ascii=False))
print("\nSUPPLEMENT:")
print(open(BASE+"/holiday-supplement.json").read()[:3000])
