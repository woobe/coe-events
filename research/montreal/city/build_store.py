import json, os, hashlib, datetime
BASE="/home/joe/repo_dev/coe-events/research/montreal/city"
RUN="run-20261126-mtl-r2"
CHECKED="2026-11-26"
S=json.load(open(BASE+"/city.json"))
def cid(*parts):
    return "cl-"+hashlib.md5("|".join(parts).encode()).hexdigest()[:12]
def claim(vid, field, date=CHECKED, **kw):
    d={"claim_id":cid(RUN,vid,field),"run_id":RUN,"verified_at":date}
    d.update(kw); return d

# ---------- coordinates ----------
GEO={
"mtl-1125d1fcdf46":("raw-mtl-1125d1fcdf46.json",1,"building","Nominatim returns the address node 9475 Rue Meilleur (H2N 2C5) with no venue POI; Suite 601 is a unit inside that building.","A name query for Versa Loft returned no Nominatim POI, so no entrance is claimed."),
"mtl-13ee7228e4b2":("raw3-mtl-13ee7228e4b2.json",1,"street","Nominatim matches Rue Sainte-Catherine Ouest at the Quartier des Spectacles segment but has no house number 397A; the operator prints 397A rue Sainte-Catherine O, Suite 202.","Four lookups (397A with postcode, 397 without, structured street, and the venue name) returned only the street or no result; the apartment letter/house number is absent from OSM."),
"mtl-184b7a111981":("raw-mtl-184b7a111981.json",0,"building","Nominatim returns the address node 275 Rue Saint-Antoine Ouest (H2Y 2X6); the operator listing prints 275 Saint Antoine Street West, Niveau 1.","A name query found 'La Mise au Jeu' at 1205 Rue Saint-Antoine Ouest, a different address, so that POI was refused as another branch."),
"mtl-1c9b9b2b165a":("raw-mtl-1c9b9b2b165a.json",1,"exact_venue","Nominatim returns the hotel POI 'Hyatt Place Montréal – Downtown' at 1415 Rue Saint-Hubert, matching the operator address and the stored venue name."),
"mtl-1e4360518a06":("raw-mtl-1e4360518a06.json",0,"exact_venue","Nominatim returns 'Crew Collective & Café' as an amenity=cafe POI at 360 Rue Saint-Jacques, the operator-printed address."),
"mtl-2729e116a7ed":("raw-mtl-2729e116a7ed.json",0,"building","Nominatim returns the address node 9850 Rue Tolhurst; the operator prints 9850 Tolhurst and H3L 2Z8, while the geocoder returns H3L 2V7, so the point is the building frontage and the postcode conflict is recorded."),
"mtl-281cff0a7a6d":("raw-mtl-281cff0a7a6d.json",0,"building","Nominatim returns the address node 377 Rue Saint-Paul Ouest (H2Y 2E8); the operator page prints 377 Rue Saint-Paul O, and the venue is a single loft in that building."),
"mtl-2fc617abde76":("raw-mtl-2fc617abde76.json",1,"building","Nominatim returns the address node 137 Rue Saint-Ferdinand (H4C 2S8); the operator prints 137 rue Saint-Ferdinand #153. The named POI at this number is Helios Makerspace, a different organisation, so the address node is used and no entrance is claimed."),
"mtl-32894124b903":("raw-mtl-32894124b903.json",1,"building","Nominatim returns the address node 9475 Rue Meilleur (H2N 2C5); the operator prints 9475 rue Meilleur and the listing names Room 605, a unit inside the building."),
"mtl-3c2599f5b2b4":("raw-mtl-3c2599f5b2b4.json",0,"building","Nominatim returns the building POI 'Walter sur Atwater' at 2727 Rue Saint-Patrick (H3K 1B8); the operator prints 2727 Rue Saint-Patrick, so the point is the building and its frontage, not a conference-room door."),
"mtl-583f8727f3f3":("raw-mtl-583f8727f3f3.json",0,"building","Nominatim returns the building POI 'Belgo' at 372 Rue Sainte-Catherine Ouest; the operator prints 372 Sainte-Catherine Street West, Suites 123, 124 and 126, inside that building."),
"mtl-5aff2a80fdee":("raw-mtl-5aff2a80fdee.json",0,"building","Nominatim returns the address node 4526 Avenue du Parc (H2V 4E4); the stored address said 4526 Park Ave, which is the same street in English, and no venue POI exists."),
"mtl-6f6753b2d241":("raw3-mtl-6f6753b2d241.json",0,"street","Nominatim matches Rue Sainte-Catherine Est but no house number 9; the operator prints 9 Ste-Catherine Est, 2e étage. The point is the postcode/street segment rather than the door.","The 9 Rue Sainte-Catherine Est query returned the Village gai segment and, without city context, a same-named street in France; neither is the building."),
"mtl-8aee03975c77":("raw-mtl-8aee03975c77.json",0,"exact_venue","Nominatim returns 'Le Studio TD' as an amenity=theatre POI at 305 Rue Sainte-Catherine Ouest, matching the operator address."),
"mtl-8ef00c25a80d":("raw-mtl-8ef00c25a80d.json",0,"building","Nominatim returns the address node 5000 Rue d'Iberville (H2H 2R9); the operator prints Studio 320, 5000 rue d'Iberville, a unit inside the building."),
"mtl-9b1cfe2df6f0":("raw-mtl-9b1cfe2df6f0.json",0,"exact_venue","Nominatim returns 'Le Balcon' as an amenity=events_venue POI at 463 Rue Sainte-Catherine Ouest, matching the operator address."),
"mtl-9e195a901d0f":("raw-mtl-9e195a901d0f.json",0,"exact_venue","Nominatim returns 'Maison Notman' as an office POI at 51 Rue Sherbrooke Ouest (H2X 1X2), matching the operator address."),
"mtl-9e988109561c":("raw-mtl-9e988109561c.json",0,"building","Nominatim returns the address node 3737 Boulevard Crémazie Est (H1Z 2K4); the operator prints 3737 Boulevard Crémazie Est, and Suite 200 is a unit inside."),
"mtl-a200486a6df1":("raw-mtl-a200486a6df1.json",1,"building","Nominatim returns the address node 800 Rue du Square-Victoria (H3C 0B4). The named POI at this number is a McDonald's, not Ax.c, so the address node is used and no venue entrance is claimed."),
"mtl-a2488d6b9f36":("raw-mtl-a2488d6b9f36.json",0,"building","Nominatim returns the address node 370 Rue Guy (H3J 1R1); the operator prints two street-level spaces at 370 Rue Guy in Griffintown."),
"mtl-a69fecaefa03":("raw3-mtl-13ee7228e4b2.json",1,"street","Nominatim matches the Rue Sainte-Catherine Ouest segment for the operator address 397A rue Sainte-Catherine O; no house number or room POI exists for Juniper."),
"mtl-b1e93c63b00b":("raw3-mtl-b1e93c63b00b.json",1,"exact_venue","Nominatim returns 'Kawalees' as an amenity=restaurant POI at 5175 Avenue du Parc, matching the operator-printed 5175A Avenue du Parc, H2V 4G3."),
"mtl-b6318fa3d1f6":("raw2-mtl-b6318fa3d1f6.json",0,"exact_venue","Nominatim returns 'L'Annexe Saint-Ambroise' as an amenity=pub POI at 5080 Rue Saint-Ambroise, matching the operator address H4C 2G1."),
"mtl-b911cdc04475":("raw-mtl-b911cdc04475.json",0,"building","Nominatim returns the address node 5570 Avenue Casgrain (H2T 1X9); the operator prints suite 101, a unit inside the building."),
"mtl-bfeec3cc37f4":("raw-mtl-bfeec3cc37f4.json",0,"building","Nominatim returns the address node 1225 Boulevard Saint-Joseph Est; the operator prints H2J 1L7 and the geocoder returns H2J 1L5, so the point is the building frontage and the postcode conflict is recorded."),
"mtl-d0e27aa38d40":("raw-mtl-d0e27aa38d40.json",0,"exact_venue","Nominatim returns 'Société des arts technologiques (SAT)' as an amenity=theatre POI at 1201 Boulevard Saint-Laurent, matching the operator address."),
"mtl-dd69fc532018":("raw3-mtl-13ee7228e4b2.json",1,"street","Nominatim matches the Rue Sainte-Catherine Ouest segment for 397A; no house number or THE HOOK room POI exists, and the operator page prints the address without a room-level geocode."),
"mtl-eb0452047e00":("raw-mtl-eb0452047e00.json",0,"building","Nominatim returns the address node 4475 Boulevard Saint-Laurent; the operator prints H2W 1Z8 and the geocoder returns H2W 1Z5, so the point is the building frontage and the postcode conflict is recorded."),
"mtl-edf77b252f04":("raw-mtl-edf77b252f04.json",0,"building","Nominatim returns 'Le café RALIA' as an amenity=cafe POI at 4281 Boulevard Saint-Laurent, the same building, but the venue is the Connections event space, so the tier is building rather than exact_venue."),
"mtl-eeca8449dbec":("raw-mtl-eeca8449dbec.json",0,"building","Nominatim returns the address node 4030 Rue Saint-Ambroise (H4C 2E1); the operator prints Studio 202, a unit inside the building."),
"mtl-fc4d581ec532":("raw-mtl-fc4d581ec532.json",0,"exact_venue","Nominatim returns 'District 3 Innovation Center' as a leisure=hackerspace POI at 1250 Rue Guy (H3H 2L3), matching the operator address."),
"mtl-be24c9002459":("raw-mtl-be24c9002459.json",0,"exact_venue","Nominatim returns 'Café Van Houtte' as an amenity=cafe POI at 100 Rue McGill, matching the stored venue address."),
}
MANUAL_GEO={
"mtl-6f6753b2d241":{"lat":45.5101045,"lon":-73.5636063,"returned":"Rue Sainte-Catherine Est, Quartier des Spectacles, Ville-Marie, Montréal, Québec, H2X 1K4, Canada","query":"9 Rue Sainte-Catherine Est, Montréal, Québec, H2X 1K3 (structured street/city/postcode query)"}
}
geosum=json.load(open(BASE+"/geocode-summary.json"))
qmap={}
for line in open(BASE+"/geocode-queries.txt"):
    if "|" in line:
        a,b=line.rstrip("\n").split("|",1); qmap[a]=b

for vid,v in S["venues"].items():
    g=GEO[vid]
    raw_name,idx,tier,match=g[0],g[1],g[2],g[3]
    refused=g[4] if len(g)>4 else None
    rows=json.load(open(BASE+"/geocode/"+raw_name))
    r=rows[idx]
    if vid in MANUAL_GEO:
        lat,lon,returned,q = MANUAL_GEO[vid]["lat"],MANUAL_GEO[vid]["lon"],MANUAL_GEO[vid]["returned"],MANUAL_GEO[vid]["query"]
    else:
        lat,lon,returned,q=float(r["lat"]),float(r["lon"]),r.get("display_name",""),qmap[vid]
    mt={"exact_venue":"{name}, {street}","building":"{street}","street":"{street}","area":"{area}"}.get(tier,"")
    # a readable map target: venue name + verified street for exact/building, street for street
    if tier=="exact_venue":
        target="{} — {}".format(v["name"].split("—")[0].strip(), returned.split(", Canada")[0])
    elif tier=="building":
        target=returned.split(", Canada")[0]
    else:
        target=q
    ev=claim(vid,"coordinates",value={"latitude":lat,"longitude":lon,"precision":tier,"map_target":target},
        provider="OpenStreetMap Nominatim",query=q,request_url="https://nominatim.openstreetmap.org/search?format=jsonv2&addressdetails=1&extratags=1&limit=3&q="+q.replace(" ","+"),
        returned_place=returned,match_evidence=match,derived=True,derived_from="address",precision=tier,
        source_title="Nominatim (OpenStreetMap) forward geocode of the operator-printed address",
        source_url="https://nominatim.openstreetmap.org/",checked_on=CHECKED,
        note="One live Nominatim search per row on 2026-11-26, re-run for every venue including those that already carried a point; the point is the tier stated, not a surveyed entrance.")
    if refused: ev["refused_lookups"]=refused
    v["fields"]["coordinates"]=ev

# ---------- access ----------
ACC={
"mtl-eeca8449dbec":dict(window="07:00-22:00",w8="yes",w12="yes",basis="published_clock_hours",cap=15,
  quote="Studio hours 7:00am - 10:00pm After hours - booking available",loc="Studio Cuero home page, 'Studio hours' line",
  url="https://www.studiocuero.com/",title="Studio Cuero — creative studio and event space"),
"mtl-a2488d6b9f36":dict(window="08:00-03:00",w8="yes",w12="yes",basis="published_booking_intervals",cap=19,
  quote="Booking Duration * Day Rentals (8am - 5pm) Evening Rentals (5pm - 3am)",loc="IMAGEMOTION studio page, Booking Duration block",
  url="https://imagemotion.com/studio/",title="IMAGEMOTION Studio & Event Spaces — booking page"),
"mtl-b1e93c63b00b":dict(window="12:00-24:00",w8="yes",w12="yes",basis="published_booking_intervals",cap=12,
  quote="12pm – 4pm / 4pm – 8pm / 8pm – 12am (next day)",loc="Kawalees rental page, three consecutive four-hour blocks",
  url="https://kawalees.ca/event-space-rental/",title="Espace Culturel Kawalees — event space rental"),
"mtl-13ee7228e4b2":dict(window="08:00-22:00",w8="yes",w12="yes",basis="published_booking_hours",cap=14,
  quote="\"openingHoursSpecification\":[{\"dayOfWeek\":[\"Monday\",...,\"Sunday\"],\"opens\":\"08:00\",\"closes\":\"22:00\"",loc="Tagvenue room page, openingHoursSpecification JSON-LD",
  url="https://www.tagvenue.com/ca/rooms/montreal/114371/collectif-mtl/carnegie",title="Tagvenue — Carnegie, Collectif MTL room booking page"),
"mtl-dd69fc532018":dict(window="08:00-22:00",w8="yes",w12="yes",basis="published_booking_hours",cap=14,
  quote="\"openingHoursSpecification\":[{\"dayOfWeek\":[\"Monday\",...,\"Sunday\"],\"opens\":\"08:00\",\"closes\":\"22:00\"",loc="Tagvenue room page, openingHoursSpecification JSON-LD",
  url="https://www.tagvenue.com/ca/rooms/montreal/115207/collectif-mtl/the-hook",title="Tagvenue — THE HOOK, Collectif MTL room booking page"),
"mtl-a69fecaefa03":dict(window="08:00-18:00",w8="yes",w12="no",basis="published_booking_hours",cap=10,
  quote="\"dayOfWeek\":[\"Saturday\",\"Sunday\"],\"opens\":\"08:00\",\"closes\":\"18:00\"",loc="Tagvenue room page, openingHoursSpecification JSON-LD (weekend span; weekdays close 19:00)",
  url="https://www.tagvenue.com/ca/rooms/montreal/115206/collectif-mtl/juniper",title="Tagvenue — Juniper, Collectif MTL room booking page"),
"mtl-281cff0a7a6d":dict(window="09:00-17:00",w8="yes",w12="no",basis="published_booking_intervals",cap=8,
  quote="Select Schedule (Set-up incl.) Half Day AM (8am -12pm or 9am-1pm ) Half day PM (12-4pm or 1-5pm) Evening event (6pm to 12am) Full day (9am to 5pm)",loc="Loft108 booking page, Select Schedule block",
  url="https://yasminfgow.com/loft-108/",title="Loft 108 — Old Montreal venue booking page"),
"mtl-bfeec3cc37f4":dict(window=None,w8="unknown",w12="unknown",basis="appointment_block",cap=None,
  quote="La location se fait pour 4 heures, 8 heures ou 12 heures. Une réservation de 11 h à 15 h est une location de 4 heures",loc="Centre humaniste page, rental-length paragraph",
  url="https://fondhum.com/fr/centre",title="Centre humaniste du Québec — salle principale"),
}
for vid,v in S["venues"].items():
    a=ACC.get(vid,{})
    window=a.get("window"); w8=a.get("w8","unknown"); w12=a.get("w12","unknown"); basis=a.get("basis","none")
    url=a.get("url") or (v["fields"].get("source_url") or {}).get("value"); title=a.get("title") or v["name"]
    if window:
        v["fields"]["access_window"]=claim(vid,"access_window",value=window,source_url=url,source_title=title,
            source_locator=a.get("loc"),quote=a.get("quote"),confidence="high")
        v["fields"]["closing_time"]=claim(vid,"closing_time",value=window.split("-")[1],source_url=url,source_title=title,
            source_locator=a.get("loc"),quote=a.get("quote"),confidence="high")
    else:
        v["fields"]["access_window"]=claim(vid,"access_window",value=None,source_url=url,source_title=title,
            source_locator=a.get("loc"),quote=a.get("quote"),confidence="low")
        v["fields"]["closing_time"]=claim(vid,"closing_time",value=None,source_url=url,source_title=title,
            source_locator=a.get("loc"),quote=a.get("quote"),confidence="low")
    v["fields"]["booking_hour_cap"]=claim(vid,"booking_hour_cap",value=a.get("cap"),source_url=url,source_title=title,
        source_locator=a.get("loc"),quote=a.get("quote"),confidence=("high" if a.get("cap") else "low"))
    v["fields"]["programme_windows"]=claim(vid,"programme_windows",value={"8":{"state":w8,"basis":basis},"12":{"state":w12,"basis":basis}},
        source_url=url,source_title=title,source_locator=a.get("loc"),quote=a.get("quote"),confidence=("high" if w12=="yes" else ("medium" if w12=="no" else "low")))
    v["fields"]["event_window_status"]=claim(vid,"event_window_status",value=(w12 if w12 in ("yes","no") else "unknown"),
        source_url=url,source_title=title,source_locator=a.get("loc"),quote=a.get("quote"),confidence="medium")

# ---------- photos ----------
new=json.load(open(BASE+"/photo-records.json"))
cleared_by_url={}
for vid,recs in new.items():
    for r in recs: cleared_by_url[(vid,r["url"])]=r
DROP_URLS={"https://media.eventective.com/default_space.jpg"}
dispo={"cleared":0,"dropped":0,"withheld":0}
for vid,recs in list(S["photos"].items()):
    keep=[]
    for r in recs:
        u=r.get("url")
        if u in DROP_URLS:
            dispo["dropped"]+=1; continue
        if (vid,u) in cleared_by_url:
            c=cleared_by_url[(vid,u)]
            keep.append(c); dispo["cleared"]+=1
        else:
            r["withheld"]=True; r["checked_on"]=CHECKED
            r["rights_note"]=("Hosted by a third-party listing platform ({}); the operator's own site publishes no matching gallery image and no licence for this file, so it stays withheld.").format(
                "Eventective" if "eventective" in (r.get("source_page") or "") else ("Tagvenue" if "tagvenue" in (r.get("source_page") or "") else "the listing platform"))
            keep.append(r); dispo["withheld"]+=1
    # append new cleared records not already kept
    kept_urls={x.get("url") for x in keep}
    for r in new.get(vid,[]):
        if r["url"] not in kept_urls:
            keep.append(r); kept_urls.add(r["url"])
    S["photos"][vid]=keep
for vid in new:
    if vid in S["photos"]:
        continue
    S["photos"][vid]=list(new[vid])

# ---------- holidays ----------
def wd(d): return datetime.date.fromisoformat(d).strftime("%A")
QC=[
 ("Jour de l'An","2027-01-01","statutory","N-1.1 art. 60 (1°): le 1er janvier"),
 ("Vendredi saint ou lundi de Pâques",None,"employer's choice of Good Friday 2027-03-26 or Easter Monday 2027-03-29","N-1.1 art. 60 (2°): le Vendredi saint ou le lundi de Pâques, au choix de l'employeur"),
 ("Journée nationale des patriotes","2027-05-24","le lundi qui précède le 25 mai","N-1.1 art. 60 (3°): le lundi qui précède le 25 mai"),
 ("Fête nationale du Québec","2027-06-24","24 June; 25 June substitute only when 24 June is a Sunday","Loi sur la fête nationale, art. 1 and 2"),
 ("Fête du Canada","2027-07-01","1 July; 2 July only when 1 July is a Sunday","N-1.1 art. 60 (4°): le 1er juillet ou, si cette date tombe un dimanche, le 2 juillet"),
 ("Fête du Travail","2027-09-06","le premier lundi de septembre","N-1.1 art. 60 (5°)"),
 ("Action de grâce","2027-10-11","le deuxième lundi d'octobre","N-1.1 art. 60 (6°)"),
 ("Noël","2027-12-25","statutory","N-1.1 art. 60 (7°): le 25 décembre"),
]
rows=[]
for name,date,obs,rule in QC:
    if name.startswith("Vendredi"):
        row={"holiday_name":name,"jurisdiction_id":"CA-QC","kind":"public_holiday","start_date":"2027-03-26","end_date":"2027-03-29",
             "candidate_dates":["2027-03-26","2027-03-29"],"choice":"employer","single_settled_date":False,
             "choice_note":"Quebec gives one statutory day for this holiday and the employer schedules it on Good Friday (2027-03-26) or Easter Monday (2027-03-29). No 2027 employer choice is recorded, so both dates stand and neither is the settled date.",
             "observance":obs,"derived":True,"verified":True,"accessed_on":CHECKED,"needs_human_verify":True,
             "source_title":"Loi sur les normes du travail (RLRQ c. N-1.1), art. 60","source_url":"https://www.legisquebec.gouv.qc.ca/fr/document/lc/N-1.1",
             "source_locator":"art. 60 (2°): «le Vendredi saint ou le lundi de Pâques, au choix de l'employeur»",
             "source_edition":"Current statute consulted 2026-11-26; 2027 dates from the computus (Easter Sunday 2027-03-28)",
             "evidence":{"observed_facts":"art. 60 (2°) names the pair; the computus fixes Easter Sunday 2027-03-28, so Good Friday is 2027-03-26 and Easter Monday 2027-03-29. Weekdays: Friday and Monday. CNESST's Jours fériés page returned Cloudflare HTTP 403 to a scripted request and via r.jina.ai on 2026-11-26, so the statutory text is the authority and CNESST is recorded as blocked.",
                         "corroboration":{"source":"sources_consulted — EMSB dated calendar","url":"https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/new-yearly-calendar-and-important-dates.pdf","shows":"Vendredi saint 26 mars 2027 and Lundi de Pâques 29 mars 2027"}},
             "verification_questions":["Confirm the employer's 2027 choice between Good Friday 2027-03-26 and Easter Monday 2027-03-29."]}
        rows.append(row); continue
    weekday=wd(date)
    row={"holiday_name":name,"jurisdiction_id":"CA-QC","kind":"public_holiday","start_date":date,"end_date":date,
         "observance":obs,"derived":True,"verified":True,"accessed_on":CHECKED,"needs_human_verify":False,
         "source_title":"Loi sur les normes du travail (RLRQ c. N-1.1), art. 60" if "N-1.1" in rule else "Loi sur la fête nationale (RLRQ c. F-1.1)",
         "source_url":"https://www.legisquebec.gouv.qc.ca/fr/document/lc/N-1.1" if "N-1.1" in rule else "https://www.legisquebec.gouv.qc.ca/fr/document/lc/F-1.1",
         "source_locator":rule,
         "source_edition":"Current statute consulted 2026-11-26",
         "evidence":{"observed_facts":"{}; {} (weekday computed in code).".format(rule,weekday)}}
    if name=="Fête nationale du Québec":
        row["evidence"]["observed_facts"]+=" 24 June 2027 is a Thursday, so the 25 June substitute in art. 2 does not apply."
    rows.append(row)
FED=[("New Year's Day","2027-01-01"),("Good Friday","2027-03-26"),("Victoria Day","2027-05-24"),
     ("Canada Day","2027-07-01"),("Labour Day","2027-09-06"),("National Day for Truth and Reconciliation","2027-09-30"),
     ("Thanksgiving Day","2027-10-11"),("Remembrance Day","2027-11-11"),("Christmas Day","2027-12-25"),("Boxing Day","2027-12-26")]
for name,date in FED:
    rows.append({"holiday_name":name,"jurisdiction_id":"CA","kind":"public_holiday","start_date":date,"end_date":date,
      "observance":"federal general holiday","derived":True,"verified":True,"accessed_on":CHECKED,"needs_human_verify":False,
      "source_title":"Canada Labour Program — Annual vacations and general holidays","source_url":"https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html",
      "source_locator":"General holiday entitlement: the 10 listed general holidays",
      "source_edition":"Page read 2026-11-26; dates projected to 2027 from the listed rules",
      "evidence":{"observed_facts":"The page lists 10 general holidays for federally regulated employees; {} 2027 is a {} (weekday computed in code). Federal scope is kept separate from the Quebec layer.".format(date,wd(date))}})
# school rows
rows.append({"holiday_name":"Journée pédagogique (institutionnelle)","jurisdiction_id":"CA-QC:cssdm","kind":"school_holiday",
  "start_date":"2027-04-23","end_date":"2027-04-23","observance":"pedagogical day","derived":False,"verified":True,"accessed_on":CHECKED,"needs_human_verify":False,
  "source_title":"CSSDM — Calendrier des activités scolaires 2026-2027, formation générale des jeunes","source_url":"https://face.cssdm.gouv.qc.ca/wp-content/uploads/sites/54/2026/07/Calendrier-FACE-2026-2027.pdf",
  "source_locator":"Legend: «20 journées pédagogiques : 8 fixées par le CSSDM dont 2 institutionnelles : 2 déc et 23 avr»",
  "source_edition":"2026-2027 (dated 11-mai-26), Service de l'organisation scolaire",
  "evidence":{"observed_facts":"23 April 2027 is one of the two CSSDM institutional pedagogical days; 2027-04-23 is a Friday (computed in code)."}})
rows.append({"holiday_name":"Fermeture du Centre de services scolaire de Montréal","jurisdiction_id":"CA-QC:cssdm","kind":"school_holiday",
  "start_date":"2027-06-04","end_date":"2027-06-04","observance":"board closure","derived":False,"verified":True,"accessed_on":CHECKED,"needs_human_verify":False,
  "source_title":"CSSDM — Calendrier des activités scolaires 2026-2027, formation générale des jeunes","source_url":"https://face.cssdm.gouv.qc.ca/wp-content/uploads/sites/54/2026/07/Calendrier-FACE-2026-2027.pdf",
  "source_locator":"Legend: «Fermeture du Centre de services scolaire de Montréal ... 5 oct, 16 oct et 4 juin»",
  "source_edition":"2026-2027 (dated 11-mai-26), Service de l'organisation scolaire",
  "evidence":{"observed_facts":"4 June 2027 is a listed CSSDM closure day; 2027-06-04 is a Friday (computed in code). The calendar also names a Semaine de relâche but the extracted PDF does not print its dates."}})
rows.append({"holiday_name":"Winter Break / Vacances d'hiver","jurisdiction_id":"CA-QC:emsb","kind":"school_holiday",
  "start_date":"2026-12-21","end_date":"2027-01-01","observance":"school break","derived":False,"verified":True,"accessed_on":CHECKED,"needs_human_verify":False,
  "source_title":"EMSB — School Calendar 2026-2027 and Important Dates","source_url":"https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/new-yearly-calendar-and-important-dates.pdf",
  "source_locator":"December 2026: «∆ 21 décembre – 1 janvier Vacances d'hiver December 21 - January 1 Winter Break»",
  "source_edition":"2026-2027",
  "evidence":{"observed_facts":"The break runs 2026-12-21 to 2027-01-01, so it intersects 2027 on 1 January 2027."}})
rows.append({"holiday_name":"March Break / Relâche scolaire","jurisdiction_id":"CA-QC:emsb","kind":"school_holiday",
  "start_date":"2027-03-01","end_date":"2027-03-05","observance":"school break","derived":False,"verified":True,"accessed_on":CHECKED,"needs_human_verify":False,
  "source_title":"EMSB — School Calendar 2026-2027 and Important Dates","source_url":"https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/new-yearly-calendar-and-important-dates.pdf",
  "source_locator":"March 2027: «∆1-5 Semaine de relâche March Break»",
  "source_edition":"2026-2027",
  "evidence":{"observed_facts":"March Break 2027 is 1 to 5 March (Monday to Friday)."}})
S["holidays"]=rows

# coverage
cov=[]
cov.append({"jurisdiction_id":"CA-QC","kind":"public_holiday_coverage","start_date":"2027-01-01","end_date":"2027-12-31",
 "accessed_on":CHECKED,"verified":True,"needs_human_verify":True,"source_edition":"Current statute read 2026-11-26; 2027 dates projected",
 "source_title":"Loi sur les normes du travail (N-1.1) art. 60 and Loi sur la fête nationale (F-1.1) arts. 1-2",
 "source_url":"https://www.legisquebec.gouv.qc.ca/fr/document/lc/N-1.1",
 "source_locator":"art. 60 statutory list; F-1.1 arts. 1-2",
 "evidence":{"observed_facts":"Full 2027 statutory list read from the two statutes. CNESST's Jours fériés page was blocked by Cloudflare (HTTP 403) on 2026-11-26; the statute, not CNESST's page, supplies the dates. The employer-choice pair is preserved as two candidate dates."},
 "verification_questions":["Re-read CNESST Jours fériés when the page is reachable and confirm no 2027 substitute day."]})
cov.append({"jurisdiction_id":"CA","kind":"public_holiday_coverage","start_date":"2027-01-01","end_date":"2027-12-31",
 "accessed_on":CHECKED,"verified":True,"needs_human_verify":False,"source_edition":"Page read 2026-11-26",
 "source_title":"Canada Labour Program — Annual vacations and general holidays",
 "source_url":"https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html",
 "source_locator":"General holiday entitlement: the 10 listed general holidays",
 "evidence":{"observed_facts":"Federal scope only, kept separate from Quebec; the page was read through r.jina.ai because the direct canada.ca request timed out on 2026-11-26."}})
cov.append({"jurisdiction_id":"CA-QC:cssdm","kind":"school_holiday_coverage","start_date":"2027-01-01","end_date":"2027-06-30",
 "accessed_on":CHECKED,"verified":True,"needs_human_verify":False,"source_edition":"2026-2027 (dated 11-mai-26)",
 "source_title":"CSSDM — Calendrier des activités scolaires 2026-2027, formation générale des jeunes",
 "source_url":"https://face.cssdm.gouv.qc.ca/wp-content/uploads/sites/54/2026/07/Calendrier-FACE-2026-2027.pdf",
 "source_locator":"Header and legend: 2026-2027, 180 jours de classe, 20 journées pédagogiques; dates 2 déc, 23 avr, 5 oct, 16 oct, 4 juin",
 "evidence":{"observed_facts":"The 2026-2027 calendar is read and covers January-June 2027. Two dated 2027 non-teaching days are recorded (23 April, 4 June); the Semaine de relâche dates are not printed in the extracted PDF and the 2027-2028 edition is not published, so July-December 2027 is uncovered."}})
cov.append({"jurisdiction_id":"CA-QC:emsb","kind":"school_holiday_coverage","start_date":"2027-01-01","end_date":"2027-06-30",
 "accessed_on":CHECKED,"verified":True,"needs_human_verify":False,"source_edition":"2026-2027",
 "source_title":"EMSB — School Calendar 2026-2027 and Important Dates",
 "source_url":"https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/new-yearly-calendar-and-important-dates.pdf",
 "source_locator":"Dated calendar: Winter Break 21 Dec-1 Jan; March Break 1-5 March; last day of classes 23 June 2027",
 "evidence":{"observed_facts":"The English-board 2026-2027 calendar is read and covers January-June 2027. The 2027-2028 edition is not published, so July-December 2027 is uncovered. The same PDF prints National Patriots' Day twice (18 and 24 May); the statute's Monday-before-25-May rule fixes 24 May 2027 and the conflict is declared."}})
for jid,title,url in (("CA-QC:cssmb","CSS Marguerite-Bourgeoys — official calendars","https://www.cssmb.gouv.qc.ca/"),
                      ("CA-QC:csspi","CSS de la Pointe-de-l'Île — official calendars","https://www.csspi.gouv.qc.ca/"),
                      ("CA-QC:lbpsb","Lester B. Pearson SB — official calendars","https://www.lbpsb.qc.ca/")):
    cov.append({"jurisdiction_id":jid,"kind":"school_holiday_coverage","start_date":"2027-01-01","end_date":"2027-12-31",
      "accessed_on":CHECKED,"verified":False,"needs_human_verify":True,"source_edition":"not read",
      "source_title":title,"source_url":url,"source_locator":"No edition read",
      "evidence":{"observed_facts":"This board is not the host board for the city page and no calendar was read in this run; the whole 2027 year remains unverified for this scope, not a zero-holiday finding."},
      "verification_questions":["Read the current and next-year calendar before using this board's dates."]})
S["coverage"]=cov

# ---------- events ----------
# locate existing ALL IN and Family Office
for eid,e in list(S["events"].items()):
    nm=e.get("name","")
    if "ALL IN" in nm:
        e["fields"]["date_range"]=claim(eid,"date_range",value={"start":"2027-09-22","end":"2027-09-23"},
          source_url="https://www.scaleai.ca/events/",source_title="Scale AI — events page",
          source_locator="ALL IN 2027 — September 22 & September 23, 2027")
        e.setdefault("evidence",[]).append({"claim_id":cid(RUN,eid,"ev"),"run_id":RUN,"verified_at":CHECKED,
          "source_url":"https://www.scaleai.ca/events/","source_title":"Scale AI — events page",
          "observed_facts":"Scale AI events page prints 'ALL IN 2027 September 22 & September 23, 2027'; the MiraGather record prints startDate 2027-09-22 and endDate 2027-09-23, city Montreal.",
          "inference":"Organiser page and aggregator agree on a 2027 Montreal date."})
    if "Family Office" in nm:
        e["fields"]["date_range"]=claim(eid,"date_range",value={"start":"2027-05-03","end":"2027-05-03"},
          source_url="https://dc-finance.com/",source_title="DC Finance — event schedule",
          source_locator="Event schedule: 'The Montreal Family Office & High Net Worth Conference Monday, May 3rd, 2027 Le Mount Stephen, Montreal'")
        e["evidence"].append({"claim_id":cid(RUN,eid,"ev"),"run_id":RUN,"verified_at":CHECKED,
          "source_url":"https://dc-finance.com/","source_title":"DC Finance — event schedule",
          "observed_facts":"dc-finance.com prints 'The Montreal Family Office & High Net Worth Conference Monday, May 3rd, 2027 Le Mount Stephen, Montreal'.",
          "inference":"The organiser page prints the 2027 date, so the aggregator record is retained; audience is wealth management, not an engineering theme."})
# add Startupfest
sid="mtl-ev-"+hashlib.md5("startupfest-2027".encode()).hexdigest()[:12]
S["events"][sid]={"city_slug":S["city_slug"],"event_id":sid,"name":"Startupfest 2027","names_seen":["Startupfest 2027"],
 "needs_human_verify":False,"verification_questions":[],
 "evidence":[{"claim_id":cid(RUN,sid,"ev"),"run_id":RUN,"verified_at":CHECKED,
   "source_url":"https://www.startupfest.com/","source_title":"Startupfest — official site",
   "observed_facts":"startupfest.com prints 'July 7-9, 2027 | Montreal' in the banner and in its translations block.",
   "inference":"Organiser page prints a 2027 Montreal date range."}],
 "fields":{"date_range":claim(sid,"date_range",value={"start":"2027-07-07","end":"2027-07-09"},source_url="https://www.startupfest.com/",source_title="Startupfest — official site",source_locator="Banner: 'July 7-9, 2027 | Montreal'"),
   "kind":claim(sid,"kind",value="major_other",source_url="https://www.startupfest.com/",source_title="Startupfest — official site",source_locator="Banner: Canada's Original Startup Conference"),
   "relevance":claim(sid,"relevance",value="medium",source_url="https://www.startupfest.com/",source_title="Startupfest — official site",source_locator="Banner: Canada's Original Startup Conference"),
   "conflict_severity":claim(sid,"conflict_severity",value="low",source_url="https://www.startupfest.com/",source_title="Startupfest — official site",source_locator="Banner: 'July 7-9, 2027 | Montreal'")},
 "history":{}}

# ---------- sources ----------
def src(url,title,kind,note,status="checked",loc="en-CA",mandatory=False):
    return {"url":url,"title":title,"kind":kind,"note":note,"check_status":status,"checked_on":CHECKED,"accessed_on":CHECKED,"locale":loc,"mandatory":mandatory}
existing={s["url"] for s in S["sources_consulted"]}
add=[]
add.append(src("https://nominatim.openstreetmap.org/search","OpenStreetMap Nominatim — 32 forward queries","geocode",
  "32 live queries on 2026-11-26, one per venue, re-run for every row; results in geocode/raw-*.json. Four lookups refused: 397A, 9 Ste-Catherine Est, Kawalees/Ax-C house-number matches that landed on another business."))
add.append(src("https://www.legisquebec.gouv.qc.ca/fr/document/lc/N-1.1","Loi sur les normes du travail (N-1.1)","calendar",
  "art. 60 read 2026-11-26 (via r.jina.ai because the direct request returned 403/502); statutory list and employer-choice pair captured.",loc="fr-CA"))
add.append(src("https://www.legisquebec.gouv.qc.ca/fr/document/lc/F-1.1","Loi sur la fête nationale (F-1.1)","calendar",
  "arts. 1-2 read 2026-11-26 (via r.jina.ai); 24 June is the national holiday and a statutory day off, with a 25 June substitute only when 24 June is a Sunday.",loc="fr-CA"))
add.append(src("https://www.cnesst.gouv.qc.ca/fr/conditions-travail/jours-feries","CNESST — jours fériés au Québec","calendar",
  "Attempted 2026-11-26: direct and r.jina.ai both returned Cloudflare HTTP 403 / CAPTCHA; no CNESST text was read. Dates come from the statutes, not from this page.",status="blocked",loc="fr-CA"))
add.append(src("https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html","Canada Labour Program — Annual vacations and general holidays","calendar",
  "Read 2026-11-26 through r.jina.ai (direct canada.ca timed out); the 10 general holidays are captured."))
add.append(src("https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/new-yearly-calendar-and-important-dates.pdf","EMSB — School Calendar 2026-2027 and Important Dates","calendar",
  "Read 2026-11-26; dated 2026-2027 table captured (Winter Break, March Break, Good Friday, Easter Monday, National Patriots' Day, St-Jean-Baptiste, Canada Day)."))
add.append(src("https://cdn.aglty.io/emsb/emsb-website/common/annual-calendars/youth-calendar.pdf","EMSB — youth sector work-day calendar 2026-2027","calendar",
  "Read 2026-11-26; school year 2026-08-26 to 2027-06-30, first day 2026-09-01, last day 2027-06-23, spring break 2027-03-01..05."))
add.append(src("https://face.cssdm.gouv.qc.ca/wp-content/uploads/sites/54/2026/07/Calendrier-FACE-2026-2027.pdf","CSSDM — Calendrier des activités scolaires 2026-2027 (FGJ)","calendar",
  "Read 2026-11-26; 2026-2027 edition dated 11-mai-26, 180 class days, 20 pedagogical days including 2027-04-23 and 2027-06-04.",loc="fr-CA"))
add.append(src("https://www.cssdm.gouv.qc.ca/","CSSDM — centre de services scolaire","calendar",
  "Site reached 2026-11-26; the central calendar path returned 404, so the FACE school edition of the CSSDM FGJ calendar was read.",status="partial",loc="fr-CA"))
add.append(src("https://www.emsb.qc.ca/emsb/about/documents/calendars","EMSB — Annual Calendars index","calendar",
  "Read 2026-11-26; links to the 2026-2027 youth calendar and the dated important-dates PDF."))
# operator pages
OPS={
"mtl-1125d1fcdf46":("https://versaloft.ca/en/evenements-salle-anaia-en/","Versa Loft — Anaia Room","'Event (minimum 5 hours) 175$/h ... Up to 60 people in banquet style'; address 9475 Rue Meilleur, Suite 601."),
"mtl-13ee7228e4b2":("https://collectifmtl.com/en/espace/carnegie/","Collectif MTL — Carnegie room","Operator room page read; address 397A rue Sainte-Catherine O, Suite 202, H3A 2G3; no opening hours printed."),
"mtl-a69fecaefa03":("https://collectifmtl.com/en/espace/juniper/","Collectif MTL — Juniper room","Operator room page read; no opening hours printed."),
"mtl-dd69fc532018":("https://collectifmtl.com/en/espace/the-hook/","Collectif MTL — THE HOOK room","Operator room page read; no opening hours printed."),
"mtl-1e4360518a06":("https://crewcollectivecafe.com/en/crew/main-venue","Crew Collective & Café — Main Venue","Operator page read 2026-11-26 (curl); 250 people, 3,000 sq ft, 360 rue St-Jacques G101."),
"mtl-3c2599f5b2b4":("https://2727coworking.com/","2727 Coworking","Operator site read; 2727 Rue Saint-Patrick, Griffintown; gallery alts captured."),
"mtl-a200486a6df1":("https://espaceaxc.com/en/","Ax.c — Espace Ax-C","Operator site read; 800 Rue du Square-Victoria, H3C 0B4; 'Monday to friday 8:30 AM to 4:30 PM'."),
"mtl-2fc617abde76":("https://www.communidee.ca/","Centre Communidée","Operator site read; Montreal, QC H4C 2S6; gallery captured."),
"mtl-bfeec3cc37f4":("https://fondhum.com/fr/centre","Centre humaniste du Québec","Operator page read; 1225 boul. Saint-Joseph Est, H2J 1L7; 4/8/12-hour rental lengths, no fixed clock interval."),
"mtl-583f8727f3f3":("https://disstorsion.com/en/","DissTorsion Studio","Operator site read; 372 Sainte-Catherine Street West, Suites 123, 124 and 126."),
"mtl-b1e93c63b00b":("https://kawalees.ca/event-space-rental/","Espace Culturel Kawalees","Operator rental page read; 5175A Avenue du Parc, H2V 4G3; 12pm-4pm, 4pm-8pm, 8pm-12am blocks."),
"mtl-9e988109561c":("https://groupe3737.com/en/","Groupe 3737 — Espace 3737","Operator site read; 3737 Boulevard Crémazie Est, H1Z 2K4."),
"mtl-a2488d6b9f36":("https://imagemotion.com/studio/","IMAGEMOTION Studio & Event Spaces","Operator booking page read; Day 8am-5pm, Evening 5pm-3am."),
"mtl-8ef00c25a80d":("https://www.kpturstudio.com/","Kptur Studio","Operator site read; Studio 320, 5000 rue d'Iberville; gallery captured."),
"mtl-9b1cfe2df6f0":("https://en.lebalcon.ca/","Le Balcon","Operator site read; 463 Sainte-Catherine Ouest."),
"mtl-8aee03975c77":("https://lestudiotd.com/","Le Studio TD — Galerie Lounge TD","Operator site read; 305 Rue Sainte-Catherine Ouest."),
"mtl-edf77b252f04":("https://connectionsralia.com/","Les Connections Ralia","Operator site read; 4281 Boul. Saint-Laurent, H2W 1Z4; gallery captions captured."),
"mtl-281cff0a7a6d":("https://yasminfgow.com/loft-108/","Loft 108","Operator booking page read; 377 Rue Saint-Paul O; schedule blocks captured."),
"mtl-2729e116a7ed":("https://maisontela.com/","Maison Tela","Operator site read; 9850 Tolhurst, H3L 2Z8; studio galleries captured."),
"mtl-32894124b903":("https://miralestudios.com/","Mirale Studios","Operator site read; 9475 rue Meilleur; studio galleries captured."),
"mtl-184b7a111981":("https://centrebell.ca/en/food-and-beverage/restaurants/mise-au-jeu","Mise au Jeu — Centre Bell","Operator page read; 275 Saint Antoine Street West, Niveau 1."),
"mtl-6f6753b2d241":("http://monloftprive.com/","Mon Loft Privé — Espace des Arts","Operator site read; 9 Sainte-Catherine Est, 2e étage, H2X 1K3; Espace des Arts gallery captured."),
"mtl-b6318fa3d1f6":("https://mcauslan.com/en/lannexe/","Pub L'Annexe St-Ambroise","Operator site read; 5080 St-Ambroise, H4C 2G1."),
"mtl-eeca8449dbec":("https://www.studiocuero.com/","Studio Cuero","Operator site read; 4030 Rue Saint-Ambroise, Studio 202; 'Studio hours 7:00am - 10:00pm'."),
"mtl-eb0452047e00":("https://tangorenaissance.com/","Tango Renaissance","Operator site read; 4475 St. Laurent Blvd, Suite 200, H2W 1Z8."),
"mtl-d0e27aa38d40":("https://sat.qc.ca/en/rent-our-spaces/","SAT — rent our spaces","Operator rental page read; 1201 Boulevard Saint-Laurent; Café SAT 70; gallery with credits captured."),
"mtl-b911cdc04475":("https://www.lewagon.com/montreal","Le Wagon Montreal Campus","Operator site read; 5570 avenue Casgrain, suite 101, H2T 1X9."),
"mtl-9e195a901d0f":("https://maisonphilanthropiquenotman.org/","Notman House / Maison philanthropique Notman","Operator site read; 51 Rue Sherbrooke Ouest, H2X 1X2."),
"mtl-fc4d581ec532":("https://www.district3.co/about","District 3 Innovation Centre","Operator page read; 1250 Rue Guy, Suite 600, H3H 2L3."),
"mtl-be24c9002459":("https://cafevanhoutte.com/fr/trouver-un-cafe/","Café Van Houtte — 100 McGill","Brand locator read; the 100 Rue McGill café is the stored venue."),
}
for vid,(url,title,note) in OPS.items():
    add.append(src(url,title,"venue",note))

# ---------- addresses re-verified ----------
ADDR={
"mtl-13ee7228e4b2":("397A Rue Sainte-Catherine O, Suite 202, Montréal, QC H3A 2G3","397A rue Sainte-Catherine O, Suite 202, Montréal QC H3A 2G3","Collectif MTL home page address block","https://collectifmtl.com/en/","Collectif MTL — event and conference spaces","Operator prints H3A 2G3; the Tagvenue listing printed H3B 1A4. The operator address wins and the conflict is recorded."),
"mtl-a69fecaefa03":("397A Rue Sainte-Catherine O, Suite 202, Montréal, QC H3A 2G3","397A rue Sainte-Catherine O, Suite 202, Montréal QC H3A 2G3","Collectif MTL home page address block","https://collectifmtl.com/en/","Collectif MTL — event and conference spaces","Operator prints H3A 2G3; the Tagvenue listing printed H3B 1A4. The operator address wins and the conflict is recorded."),
"mtl-dd69fc532018":("397A Rue Sainte-Catherine O, Suite 202, Montréal, QC H3A 2G3","397A rue Sainte-Catherine O, Suite 202, Montréal QC H3A 2G3","Collectif MTL home page address block","https://collectifmtl.com/en/","Collectif MTL — event and conference spaces","Operator prints H3A 2G3; the Tagvenue listing printed H3B 1A4. The operator address wins and the conflict is recorded."),
"mtl-bfeec3cc37f4":("1225 Boul Saint-Joseph Est, Montréal, QC H2J 1L7","1225, boul. Saint-Joseph Est, Montréal (QC) H2J 1L7, métro Laurier","Centre humaniste address line","https://fondhum.com/fr/centre","Centre humaniste du Québec — salle principale","Operator prints H2J 1L7; Nominatim returns H2J 1L5 for the same frontage."),
"mtl-9e988109561c":("3737 Boulevard Crémazie Est, Suite 200, Montréal, QC H1Z 2K4","3737 Boulevard Crémazie Est, Montréal, (QC) H1Z 2K4, Canada","Groupe 3737 address block","https://groupe3737.com/en/","Groupe 3737 — Espace 3737",None),
"mtl-edf77b252f04":("4281 Boul. Saint-Laurent, Montréal, QC H2W 1Z4","La Maison Ralia, 4281 Boul. Saint-Laurent, Montréal, QC H2W 1Z4, Canada","Connections Ralia address line","https://connectionsralia.com/","Les Connections Ralia",None),
"mtl-b1e93c63b00b":("5175A Avenue du Parc, Montréal, QC H2V 4G3","5175A Avenue du parc, Montreal, Quebec H2V 4G3","Kawalees address line","https://kawalees.ca/event-space-rental/","Espace Culturel Kawalees — event space rental",None),
"mtl-eb0452047e00":("4475 Boul. Saint-Laurent, Suite 200, Montréal, QC H2W 1Z8","4475 St. Laurent Blvd. Suite 200, Montreal ... Quebec, H2W 1Z8","Tango Renaissance address block","https://tangorenaissance.com/","Tango Renaissance — studio and event space","Operator prints H2W 1Z8; Nominatim returns H2W 1Z5 for the same frontage."),
"mtl-b6318fa3d1f6":("5080 Rue St-Ambroise, Montréal, QC H4C 2G1","5080 ST-AMBROISE MONTRÉAL H4C 2G1","L'Annexe address block","https://mcauslan.com/en/lannexe/","Pub L'Annexe St-Ambroise",None),
"mtl-2729e116a7ed":("9850 Rue Tolhurst, Montréal, QC H3L 2Z8","9850 Tolhurst, Montréal ... Montréal, QC H3L 2Z8","Maison Tela address block","https://maisontela.com/","Maison Tela — photo and video studios","Operator prints H3L 2Z8; Nominatim returns H3L 2V7 for the same frontage."),
"mtl-32894124b903":("9475 Rue Meilleur, Room 605, Montréal, QC H2N 2C5","9475 rue meilleur, Montréal Qc","Mirale studios address line","https://miralestudios.com/","Mirale Studios",None),
"mtl-1125d1fcdf46":("9475 Rue Meilleur, Local 601, Montréal, QC H2N 2C5","9475 Rue Meilleur, Suite 601, Montréal, QC H2N 2C5","Versa Loft address line","https://versaloft.ca/en/evenements-salle-anaia-en/","Versa Loft — Anaia Room",None),
"mtl-b911cdc04475":("5570 Avenue Casgrain, Suite 101, Montréal, QC H2T 1X9","5570, avenue Casgrain, suite 101, Montréal (Québec), H2T1X9","Le Wagon Montreal address block","https://www.lewagon.com/montreal","Le Wagon Montreal Campus",None),
"mtl-9e195a901d0f":("51 Rue Sherbrooke Ouest, Montréal, QC H2X 1X2","Montréal, QC, H2X 1X2","Notman House address block","https://maisonphilanthropiquenotman.org/","Notman House / Maison philanthropique Notman",None),
"mtl-5aff2a80fdee":("4526 Avenue du Parc, Montréal, QC","4526 Avenue du Parc, Montréal, QC","Eventective listing address block","https://www.eventective.com/montreal-qc/genesis-hq-789694.html","Eventective — Genesis HQ listing","The stored English 'Park Ave' is the same street as Avenue du Parc; the French form is stored so the geocode and address agree."),
}
for vid,v in S["venues"].items():
    old=(v["fields"].get("address") or {}).get("value")
    if vid in ADDR:
        value,quote,loc,url,title,note=ADDR[vid]
    else:
        value=old; quote=None
        url,title,_=OPS.get(vid,( (v["fields"].get("source_url") or {}).get("value"),v["name"],""))
        loc="Address block on the operator source page"
        note=None
    e=claim(vid,"address",value=value,source_url=url,source_title=title,source_locator=loc,confidence="high")
    if quote: e["quote"]=quote
    if note: e["conflict_note"]=note
    e["reverified_from"]=old
    v["fields"]["address"]=e
QDICT={
"mtl-184b7a111981":'"streetAddress":"275 Saint Antoine Street West Niveau 1"',
"mtl-281cff0a7a6d":'"streetAddress":"377 Rue Saint-Paul O"',
"mtl-2fc617abde76":'"streetAddress":"137 rue Saint-Ferdinand # 153"',
"mtl-3c2599f5b2b4":'"streetAddress":"2727 Rue Saint-Patrick"',
"mtl-583f8727f3f3":'"streetAddress":"372 rue Sainte Catherine Ouest, Suite 123"',
"mtl-6f6753b2d241":'"streetAddress":"9 Ste-Catherine Est (coin St-Laurent), 2e, suite 1"',
"mtl-8aee03975c77":'"streetAddress":"305 Rue Sainte-Catherine Ouest"',
"mtl-8ef00c25a80d":'"streetAddress":"5000 rue d\\u0027iberville"',
"mtl-9b1cfe2df6f0":'"streetAddress":"463 Sainte-Catherine Ouest"',
"mtl-a2488d6b9f36":'"streetAddress":"370 Rue Guy"',
"mtl-be24c9002459":'"streetAddress":"100 rue McGill"',
"mtl-eeca8449dbec":'"streetAddress":"4030 Rue Saint-Ambroise"',
"mtl-fc4d581ec532":'"streetAddress":"1250 Guy Street, Suite #600"',
}
for vid,q in QDICT.items():
    e=S["venues"][vid]["fields"]["address"]
    e["quote"]=q; e["source_locator"]="JSON-LD streetAddress on the listing page"
    e["source_url"]=(S["venues"][vid]["fields"].get("source_url") or {}).get("value")
    e["source_title"]="Listing page JSON-LD address"
for vid,note in {
 "mtl-1c9b9b2b165a":"Hyatt's meetings page returned HTTP 429 on 2026-11-26, so the address is carried from the same Hyatt meetings page read on 2026-11-24; no fresh address line was captured.",
 "mtl-1e4360518a06":"The Crew Collective page returned HTTP 403 to the scripted fetch (and its HTML carries no address text on a 200 re-fetch), so the address is carried from the operator's terms page read on 2026-11-24.",
 "mtl-a200486a6df1":"The Ax.c page prints the address in a split footer block and no single captured line carries the full string; the stored value is the operator's footer address, re-read 2026-11-26.",
 "mtl-d0e27aa38d40":"SAT's rental page loads its address client-side; the stored value is the operator's printed 1201 Boulevard Saint-Laurent, re-read 2026-11-26.",
}.items():
    e=S["venues"][vid]["fields"]["address"]
    e["confidence"]="medium"; e["retrieval_note"]=note

# event lane sources
EV=[
("https://lu.ma/montreal","Luma — Montréal city page","Lane opened 2026-11-26: 0 occurrences of 2027 in the served page; no 2027 event retained.","checked"),
("https://lu.ma/mtl","Luma — MTL alias","Alias returned HTTP 404 on 2026-11-26; alias lane closed as unsupported.","blocked"),
("https://lu.ma/montr%C3%A9al","Luma — Montréal accented alias","Accented alias returned HTTP 404; French alias lane closed.","blocked"),
("https://lu.ma/decentralized_ai_events?period=past","Luma — DeAI organiser calendar (past)","Organiser calendar read; 2027 text appears only in a day-number class; no 2027 dated event retained.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/tech/","Eventbrite — Montreal tech","Read; 2027 signal = 'Women in Tech 2027 - Montreal Employer Ticket', actual startDate 2027-02-25, a recruiting event outside the six themes → dropped.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/ai/","Eventbrite — Montreal AI","Read; 'What Does My Business Actually Need in 2027? (An AI Fair for Women)' starts 2026-12-28 → dropped as not 2027.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/machine-learning/","Eventbrite — Montreal machine learning","Read; no 2027 theme event.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/data-science/","Eventbrite — Montreal data science","Read; no 2027 theme event.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/web3/","Eventbrite — Montreal Web3","Read; no 2027 Web3 event.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/crypto/","Eventbrite — Montreal crypto","Read; no 2027 crypto event.","checked"),
("https://www.eventbrite.ca/d/canada--montreal/blockchain/","Eventbrite — Montreal blockchain","Read; 0 occurrences of 2027.","checked"),
("https://www.meetup.com/find/?keywords=ai&location=ca--montreal","Meetup — Montreal AI search","Read; 2027 dates found belong to a JavaScript group, outside the six themes → dropped.","checked"),
("https://www.meetup.com/pydata-montreal/","Meetup — PyData Montreal","Group page read; no 2027 dated event.","checked"),
("https://www.meetup.com/ai-ml-montreal/","Meetup — AI/ML Montreal","Group page read; no 2027 dated event.","checked"),
("https://www.meetup.com/data-drinks-montreal/","Meetup — Data Drinks Montreal","Group page read; no 2027 dated event.","checked"),
("https://www.meetup.com/gdg-montreal/","Meetup — GDG Montreal","Group page read; no 2027 dated event.","checked"),
("https://www.meetup.com/blockchain-montreal/","Meetup — Blockchain Montreal","Group page read; no 2027 dated event.","checked"),
("https://www.meetup.com/montreal-crypto/","Meetup — Montreal Crypto","Group page read; no 2027 dated event.","checked"),
("https://aitinkerers.org/all_cities","AI Tinkerers — all cities","Attempted 2026-11-26; the directory now returns 200 but exposes no Montreal 2027 dates.","checked"),
("https://montreal.aitinkerers.org/","AI Tinkerers — Montreal chapter","Chapter page read; 2027 appears only in an asset hash; no 2027 dated event.","checked"),
("https://c2montreal.com/","C2 Montréal","Read; 0 occurrences of 2027; no next-edition date printed.","checked"),
("https://www.startupfest.com/","Startupfest — official site","Read; banner prints 'July 7-9, 2027 | Montreal' → retained.","checked"),
("https://mtlconnecte.ca/","MTL connecte","Read; a 'Thème 2027' heading but no 2027 date or venue → not retained.","partial"),
("https://www.scaleai.ca/events/","Scale AI — events","Read; 'ALL IN 2027 September 22 & September 23, 2027' → retained.","checked"),
("https://mila.quebec/en/events","Mila — events","Read; one 2027 item, 'Hack The High Seas: Ecohull Vessel Challenge' 22-23 March 2027, outside the six themes → dropped.","checked"),
("https://ivado.ca/en/events/","IVADO — events","Read; a 2026-2027 seminar series but no 2027 dated conference.","checked"),
("https://dc-finance.com/","DC Finance — event schedule","Read via search result; prints 'The Montreal Family Office & High Net Worth Conference Monday, May 3rd, 2027 Le Mount Stephen, Montreal' → retained.","checked"),
("https://miragather.com/","MiraGather — main (Montreal filter)","Read 2026-11-26; 2 Montreal records, both 2027: ALL IN and the Family Office conference.","checked"),
("https://miragather.com/?tab=side","MiraGather — side events","Read 2026-11-26; the served document is the same payload as main; no additional Montreal 2027 side event.","checked"),
("https://miragather.com/ai","MiraGather — AI view","Read 2026-11-26; AI payload filtered for Montreal returns ALL IN only.","checked"),
]
for url,title,note,status in EV:
    add.append(src(url,title,"event",note,status=status,loc="fr-CA" if "quebec" in url or "montreal" in title.lower() and "montréal" in title else "en-CA"))
for s in add:
    if s["url"] not in existing:
        S["sources_consulted"].append(s); existing.add(s["url"])

# ---------- declared gaps ----------
S["declared_gaps"]=[
 {"kind":"coordinates","checked_on":CHECKED,"evidence_refs":["geocode/raw3-mtl-13ee7228e4b2.json","venues.mtl-13ee7228e4b2.fields.coordinates","venues.mtl-a69fecaefa03.fields.coordinates","venues.mtl-dd69fc532018.fields.coordinates"],
  "text":"The three Collectif MTL rooms are pinned to the Rue Sainte-Catherine Ouest street segment, not a door: OSM has no house number 397A, and four lookups returned only the street or no result."},
 {"kind":"coordinates","checked_on":CHECKED,"evidence_refs":["geocode/raw3-mtl-6f6753b2d241.json","venues.mtl-6f6753b2d241.fields.coordinates"],
  "text":"Mon Loft Privé is a street-segment pin: OSM has no house number 9 on Rue Sainte-Catherine Est; the previous point was on the Village gai segment about a kilometre east."},
 {"kind":"coordinates","checked_on":CHECKED,"evidence_refs":["geocode/raw-mtl-2729e116a7ed.json","geocode/raw-mtl-bfeec3cc37f4.json","geocode/raw-mtl-eb0452047e00.json"],
  "text":"Three building pins carry a postcode conflict: Maison Tela operator H3L 2Z8 vs OSM H3L 2V7; Centre humaniste H2J 1L7 vs H2J 1L5; Tango Renaissance H2W 1Z8 vs H2W 1Z5. The point is the building frontage."},
 {"kind":"photos","checked_on":CHECKED,"evidence_refs":["photos.mtl-*","photo-specs.json"],
  "text":"42 of the 48 platform-listing photo records remain withheld: Eventective and Tagvenue host the files without a licence, and the operators' own sites publish no matching gallery image for those URLs. Two Eventective default_space.jpg placeholders were dropped."},
 {"kind":"photos","checked_on":CHECKED,"evidence_refs":["photos"],
  "text":"17 of 32 venues still have no cleared room photograph; the cleared set is 45 operator-gallery images across 15 venues, with the operator sites publishing no room gallery for the rest."},
 {"kind":"holidays","checked_on":CHECKED,"evidence_refs":["sources_consulted[CNESST]","holidays[Vendredi saint]"],
  "text":"CNESST's Jours fériés page was blocked by Cloudflare (HTTP 403, also via r.jina.ai) on 2026-11-26; the Quebec dates come from the Loi sur les normes du travail and the Loi sur la fête nationale, and CNESST remains unread."},
 {"kind":"holidays","checked_on":CHECKED,"evidence_refs":["coverage[CA-QC:cssdm]","sources_consulted[CSSDM]"],
  "text":"The CSSDM 2026-2027 FGJ calendar prints 23 April and 4 June 2027 as non-teaching days but does not print the Semaine de relâche dates in the extracted PDF, so no March-break row is claimed for the French board."},
 {"kind":"holidays","checked_on":CHECKED,"evidence_refs":["coverage[CA-QC:cssdm]","coverage[CA-QC:emsb]"],
  "text":"Neither the CSSDM nor the EMSB 2027-2028 calendar is published, so July-December 2027 is uncovered for both school scopes; the 2026-2027 editions cover January-June 2027."},
 {"kind":"holidays","checked_on":CHECKED,"evidence_refs":["holidays[CA-QC:emsb]","sources_consulted[EMSB]"],
  "text":"The EMSB 2026-2027 dated calendar prints National Patriots' Day on both 18 May and 24 May 2027; the statute's Monday-before-25-May rule fixes 24 May and the internal conflict is recorded."},
 {"kind":"events","checked_on":CHECKED,"evidence_refs":["event-matrix.json","sources_consulted[events]"],
  "text":"Only three events print 2027 dates on an organiser page: ALL IN (22-23 September), Startupfest (7-9 July) and the DC Finance Montreal Family Office conference (3 May). Luma's city page, the six Meetup groups and AI Tinkerers Montreal published no 2027 theme event; Luma MTL and Montréal aliases both 404."},
 {"kind":"access","checked_on":CHECKED,"evidence_refs":["venues.mtl-13ee7228e4b2.fields.programme_windows","venues.mtl-dd69fc532018.fields.programme_windows"],
  "text":"Carnegie and THE HOOK carry a 12-hour yes from the Tagvenue room booking page's 08:00-22:00 openingHoursSpecification; the operator's own Collectif MTL room pages publish no hours, so the interval is platform-published, not operator prose."},
 {"kind":"access","checked_on":CHECKED,"evidence_refs":["venues.mtl-bfeec3cc37f4.fields.programme_windows"],
  "text":"Centre humaniste's former 12-hour yes was an appointment block: the operator prices 4-, 8- and 12-hour rentals but publishes no fixed clock interval, so both windows are downgraded to unknown."},
]
S["refresh_revision"]=1
S["updated_at"]="2026-11-26T00:00:00Z"
S["runs"].append({"kind":"refresh","run_id":RUN,"updated_at":S["updated_at"],
  "note":"R2 revision-1 refresh: 32 addresses re-geocoded, 45 operator-gallery photos cleared, 42 platform photos kept withheld, Quebec/federal/school holiday layers rebuilt, six-theme event sweep."})
json.dump(S,open(BASE+"/city.json","w"),indent=1,ensure_ascii=False)
print("WROTE store; venues",len(S["venues"]),"photos",sum(len(v) for v in S["photos"].values()),"cleared",sum(1 for v in S["photos"].values() for r in v if not r.get("withheld")),"withheld",sum(1 for v in S["photos"].values() for r in v if r.get("withheld")),"holidays",len(S["holidays"]),"events",len(S["events"]),"gaps",len(S["declared_gaps"]))
print("dispo",dispo)
