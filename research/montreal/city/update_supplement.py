import json, hashlib
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
S=json.load(open(BASE+"/city.json"))
D=json.load(open(BASE+"/holiday-supplement.json"))
D["coverage"]=S["coverage"]
D["coverage_rows"]=len(S["coverage"])
D["generated_on"]="2026-11-26"
D["holiday_rows"]=0
D["jurisdictions"]=[
 {"jurisdiction_id":"CA-QC","layer":"public","authority":"Loi sur les normes du travail (N-1.1) art. 60; Loi sur la fête nationale (F-1.1) arts. 1-2",
  "source_url":"https://www.legisquebec.gouv.qc.ca/fr/document/lc/N-1.1","checked_on":"2026-11-26","needs_human_verify":True,
  "attested":[{"start":"2027-01-01","end":"2027-12-31","note":"Statutory list read; employer-choice pair kept as two candidates. CNESST page blocked (Cloudflare 403)."}],"unknown":[]},
 {"jurisdiction_id":"CA-QC:cssdm","layer":"school","authority":"CSSDM — Calendrier des activités scolaires 2026-2027 (FGJ)",
  "source_url":"https://face.cssdm.gouv.qc.ca/wp-content/uploads/sites/54/2026/07/Calendrier-FACE-2026-2027.pdf","checked_on":"2026-11-26","needs_human_verify":False,
  "attested":[{"start":"2027-01-01","end":"2027-06-30","note":"2026-2027 edition read; 2027-04-23 and 2027-06-04 recorded."}],
  "unknown":[{"start":"2027-07-01","end":"2027-12-31","reason":"2027-2028 edition not published."}]},
 {"jurisdiction_id":"CA-QC:emsb","layer":"school","authority":"EMSB — School Calendar 2026-2027 and Important Dates",
  "source_url":"https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/new-yearly-calendar-and-important-dates.pdf","checked_on":"2026-11-26","needs_human_verify":False,
  "attested":[{"start":"2027-01-01","end":"2027-06-30","note":"2026-2027 dated calendar read; Winter Break, March Break and public holidays recorded."}],
  "unknown":[{"start":"2027-07-01","end":"2027-12-31","reason":"2027-2028 edition not published."}]},
 {"jurisdiction_id":"CA-QC:cssmb","layer":"school","authority":"CSS Marguerite-Bourgeoys — official calendars","source_url":"https://www.cssmb.gouv.qc.ca/","checked_on":"2026-11-26","needs_human_verify":True,"attested":[],"unknown":[{"start":"2027-01-01","end":"2027-12-31","reason":"No edition read; not the host board."}]},
 {"jurisdiction_id":"CA-QC:csspi","layer":"school","authority":"CSS de la Pointe-de-l'Île — official calendars","source_url":"https://www.csspi.gouv.qc.ca/","checked_on":"2026-11-26","needs_human_verify":True,"attested":[],"unknown":[{"start":"2027-01-01","end":"2027-12-31","reason":"No edition read; not the host board."}]},
 {"jurisdiction_id":"CA-QC:lbpsb","layer":"school","authority":"Lester B. Pearson SB — official calendars","source_url":"https://www.lbpsb.qc.ca/","checked_on":"2026-11-26","needs_human_verify":True,"attested":[],"unknown":[{"start":"2027-01-01","end":"2027-12-31","reason":"No edition read; not the host board."}]},
]
open(BASE+"/holiday-supplement.json","w").write(json.dumps(D,indent=1,ensure_ascii=False)+"\n")
sha=hashlib.sha256(open(BASE+"/holiday-supplement.json","rb").read()).hexdigest()
S["holiday_registry"]["supplement"]["sha256"]=sha
S["holiday_registry"]["supplement"]["coverage_rows"]=len(S["coverage"])
S["holiday_registry"]["supplement"]["note"]="Montreal-scoped layer: CA-QC public rows from the statutes (CNESST blocked) and dated CSSDM/EMSB 2026-2027 rows; next-year editions unpublished."
json.dump(S,open(BASE+"/city.json","w"),indent=1,ensure_ascii=False)
print("sha",sha)
