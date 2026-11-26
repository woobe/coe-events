import json, sys, collections
sys.path.insert(0,"/home/joe/repo_dev/hermes-skills/plan-event/scripts")
import city_rank
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
s=json.load(open(BASE+"/city.json"))
r=city_rank.build_ranking(s,"2026-11-26")
print("schema",r["schema_version"],"refresh",r["refresh_date"])
print("rows",len(r["rows"]),"leads",len(r["leads"]),"sequence",len(r["sequence"]),"counts",r["counts"])
print("groups",[(g["key"],g["count"]) for g in r["ordering"]["groups"]])
print("access windows on scored rows:",collections.Counter((row["access"]["windows"]["8"],row["access"]["windows"]["12"]) for row in r["rows"]))
print("adjudication flagged:",sum(1 for row in r["rows"] if row["access"].get("adjudication_required")))
print("row ids == sequence subset:",set(x["venue_id"] for x in r["rows"]+r["leads"])==set(r["sequence"]))
