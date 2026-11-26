import json
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
S=json.load(open(BASE+"/city.json"))
bad=[k for k in S["venues"] if not k.startswith("mtl-")]
bad+=[k for k in S["events"] if not k.startswith("mtl-")]
bad+=[k for k in S["photos"] if not k.startswith("mtl-")]
print("bad ids",bad)
print("venue ids",len(S["venues"]),"event ids",len(S["events"]),"photo keys",len(S["photos"]))
print("refresh_revision",S["refresh_revision"],"updated_at",S["updated_at"])
print("declared gaps kinds",[g["kind"] for g in S["declared_gaps"]])
