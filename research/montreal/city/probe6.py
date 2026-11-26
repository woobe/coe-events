import json
p="/home/joe/repo_dev/coe-events/research/montreal/city/city.json"
s=json.load(open(p))
print("EVCONTEXT:", json.dumps(s["event_context"], indent=1, ensure_ascii=False))
print("\nCURRENCY:", s["currency"], s.get("currency_assumptions"))
for vid,v in sorted(s["venues"].items()):
    f=v["fields"]
    print("\n",vid,v["name"])
    for k in ("access_window","event_window_status","booking_hour_cap","closing_time","price_detail","price_basis"):
        e=f.get(k)
        if e is not None:
            print("   ",k,"=",json.dumps(e.get("value"),ensure_ascii=False)[:220],"| loc:",e.get("source_locator"))
