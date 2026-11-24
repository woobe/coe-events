#!/usr/bin/env python3
"""Build the Singapore `city-store/1` from the sourced records in `sg_data.py`.

Deterministic: the same inputs and the pinned stamp produce byte-identical
city.json and run-bundle.json.
"""

import hashlib
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sg_data as D  # noqa: E402

HERE = Path(__file__).resolve().parent
HERMES = Path("/home/joe/repo_dev/hermes-skills")
REGISTRY = HERMES / "plan-event/references/school_holidays.json"
CITIES = HERMES / "plan-event/references/cities.json"
SUPPLEMENT = HERE / "holiday-supplement.json"
ENUMERATION = HERE / "tagvenue-enumeration.json"
GEOCODE = HERE / "geocode-log.json"
PHOTOS = HERE / "photos.json"
CITY = HERE / "city.json"
BUNDLE = HERE / "run-bundle.json"
UPDATED_AT = "2026-11-24T19:47:00Z"
CITY_SLUG = "singapore-sg"
LANG = "en-SG"
TODAY = D.CHECKED
TAG_BASE = "https://www.tagvenue.com/sg/rooms/singapore/"
MOM = "https://www.mom.gov.sg/employment-practices/public-holidays"
MSS = "https://www.weather.gov.sg/climate-climate-of-singapore/"
COMMONS = "https://commons.wikimedia.org/w/api.php"

def sha_text(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()

def norm(text): return " ".join(str(text or "").casefold().split())

def vid(prefix, name, url): return prefix + sha_text(norm(name) + "\n" + (url or ""))[:12]

def cid(venue_id, field): return "cl-" + sha_text(venue_id + "|" + field + "|" + D.RUN_ID)[:12]

def usd(sgd): return None if sgd is None else int(round(sgd * D.FX["rate"]))

def weekday(stamp):
    """The weekday of a recorded date; the store never trusts a copied label."""
    return date.fromisoformat(str(stamp)).strftime("%A")

def claim(owner, field, value, url, title, locator=None, quote=None, confidence=None,
          note=None, derived_from=None, derived=None, derivation=None):
    row = {"claim_id": cid(owner, field), "value": value, "verified_at": TODAY,
           "source_url": url, "source_title": title, "run_id": D.RUN_ID, "language": LANG}
    for key, extra in (("source_locator", locator), ("quote", quote),
                       ("confidence", confidence), ("note", note),
                       ("derived_from", derived_from)):
        if extra:
            row[key] = extra
    if derived is not None:
        row["derived"] = derived
    if derivation:
        row["derivation"] = derivation
    return row

def tag_url(key):
    return TAG_BASE + "/".join(key.split("__"))

def evidence_line(key, override):
    f = FACTS[key]
    cap = ", ".join("%s %s" % (k.lower(), v) for k, v in (f["rows"] or {}).items())
    sat = f["days"]["Saturday"]["rows"] if f["days"].get("Saturday") else []
    price = "; ".join("%s %s %s%s" % (r["unit"].lower(), r["from"], r["to"],
                                      "" if r["sgd"] is None else " S$%s" % r["sgd"])
                      for r in sat) or "no Saturday price printed"
    bits = ["Tagvenue room page fetched %s: %s at %s, %s m from %s." % (
                TODAY, f["name"], f["addr"] or "an address the listing does not publish",
                f["mrt_m"], f["mrt"]), "Published capacity: %s." % (cap or "not printed"),
            "Saturday hours and price: %s." % price]
    if f["min"]:
        bits.append("Minimum booking %s." % f["min"])
    if f["ext"]:
        bits.append("External catering allowed.")
    if f["byo"]:
        bits.append("BYO alcohol allowed and no alcohol provided by the venue.")
    items = (("Wi-Fi", "wifi"), ("flatscreen TV", "tv"), ("projector", "projector"),
             ("PA system", "pa"))
    provided = [label for label, key in items if f.get(key)]
    missing = [label for label, key in items if f.get(key) is False]
    bits.append("Facilities listed as provided: %s." % (
        ", ".join(provided) if provided else "none of the listed AV items"))
    if missing:
        bits.append("Listed as unavailable: %s." % ", ".join(missing))
    return " ".join(bits)

def transit(venue, url, title, sourced):
    """Station pair and distance with the provenance the record can support.

    A Tagvenue page prints both figures, so its claim is not derived; operator pages
    and leads do not, and there the claim says it is a researcher estimate.
    """
    mrt, metres = venue.get("mrt"), venue.get("mrt_m")
    if not mrt:
        return {"state": "unknown", "checked_on": TODAY, "derived": False,
                "source_role": "none published",
                "note": "No station distance is published for this room.",
                "question": "Confirm the nearest station and the walk."}
    return {
        "state": "published_station_distance" if sourced else "estimated_station_distance",
        "derived": not sourced, "checked_on": TODAY,
        "station_pair_source": "listing" if sourced else "researcher estimate",
        "nearest_station": mrt, "walk_metres": metres,
        "method": ("The station pair and the metres are the listing's own published "
                   "line; no route was plotted and no walking time is claimed."
                   if sourced else
                   "The station pair and the metres are a researcher estimate; the "
                   "venue page read in this run does not publish them, and no route "
                   "was plotted."),
        "service_at_1700": "unknown", "service_at_2100": "unknown",
        "note": "No per-station last-train table was readable on 2026-11-24 (SMRT pages are "
                "client-rendered), so no service claim is made for a 21:00 finish; the "
                "last departure from this station still needs checking against the event "
                "date.",
        "question": "Confirm the last train from %s on the event's date and the step-free "
                    "route from this entrance." % mrt}

def climate(venue):
    rooftop = "rooftop" in venue["name"].lower()
    return {
        "state": "derived_indoor" if not rooftop else "derived_outdoor_exposure",
        "derived": True, "checked_on": TODAY, "season": "December–early March; June–September",
        "note": (("A rooftop or outdoor room: the Northeast Monsoon (December to early "
                  "March) and the Southwest Monsoon (June to September) can put the "
                  "outdoor area out of use, so an indoor fallback and a wet-weather "
                  "cancellation term need confirming.")
                 if rooftop else
                 ("An indoor room; monsoon rain affects arrival, not the programme. The "
                  "Northeast Monsoon runs December to early March and the Southwest "
                  "Monsoon June to September (Meteorological Service Singapore).")),
        "question": ("Is there an indoor fallback and a wet-weather term for the monsoon "
                     "months?" if rooftop else
                     "Is the arrival route covered, and is there an indoor queue?")}

def venue_record(rec, kind):
    if kind == "tag":
        url = tag_url(rec["key"])
        f = FACTS[rec["key"]]
        address = rec.get("address") or f["addr"]
        mrt, mrt_m, lat, lon = f["mrt"], f["mrt_m"], f["lat"], f["lon"]
        title = "%s — Tagvenue Singapore listing" % rec["name"]
        quote = rec["note"]
        observed = evidence_line(rec["key"], rec)
        screen = "confirmed" if (f.get("tv") or f.get("projector")) else (
            "no" if (f.get("tv") is False and f.get("projector") is False) else "unknown")
        wifi = "confirmed" if f.get("wifi") else ("no" if f.get("wifi") is False else "unknown")
    else:
        url, address, mrt, mrt_m = rec["url"], rec["address"], rec["mrt"], rec["mrt_m"]
        lat, lon = rec.get("lat"), rec.get("lon")
        title, quote = rec["src_title"], rec["quote"]
        observed = "Page fetched %s: %s" % (TODAY, rec["quote"])
        screen = wifi = "confirmed" if kind != "hotel" else "unknown"
    venue_id = vid("sg-", rec["name"], url)
    p12, p8 = rec["p12"], rec["p8"]
    if rec["w12"] == "yes" and p12 is not None:
        chosen, hours = p12, 12
    elif rec["w8"] == "yes" and p8 is not None:
        chosen, hours = p8, 8
    else:
        chosen, hours = None, None
    cost_usd = usd(chosen)

    fields = {}

    def put(name, value, locator=None, **kw):
        fields[name] = claim(venue_id, name, value, url, title, locator=locator, **kw)

    put("display_name", rec["display"], confidence="high")
    put("about", rec["about"], "About this space / capacity and rules blocks", confidence="medium")
    put("address", address, "address line", confidence="high" if kind == "tag" else "medium")
    put("capacity", rec["capacity"], "Capacity block", quote=quote, confidence="medium")
    put("capacity_basis", rec["basis"])
    put("screen", screen, "Facilities")
    put("wifi", wifi, "Facilities")
    put("recording", "unknown", "Facilities")
    put("catering", rec["catering"], "Catering and drinks")
    put("food_service", rec["food"], "Catering and drinks")
    put("alcohol_service", rec["alcohol"], "Catering and drinks")
    put("delivery_allowed", rec["delivery"], "Catering and drinks")
    put("beer_allowed", rec["beer"], "Catering and drinks")
    put("booking_url", url)
    put("source_url", url)
    put("lifecycle", "open")
    put("language_support", {"state": "en_published",
                             "note": "The operator publishes this room in English."})
    put("access_window", rec.get("access"), "Prices block", note=rec.get("access_note"))
    put("booking_hour_cap", rec.get("min_hours"), "Minimum booking duration")
    if rec.get("closing"):
        put("closing_time", rec["closing"], "Prices block — Saturday span end")
    put("event_window_status", rec["window_status"], "Prices block")
    put("programme_windows",
        {"8": {"state": rec["w8"], "basis": rec["wbasis"]},
         "12": {"state": rec["w12"], "basis": rec["wbasis"]}},
        "Prices block", quote=quote, confidence="medium")
    put("price", cost_usd, "Prices block", quote=quote,
        confidence="medium" if cost_usd else None)
    put("price_basis", None if cost_usd is None else ("published_rate" if rec.get("published_rate", True) else "estimated_from_rate"))
    put("price_detail",
        {"cost_local_amount": chosen, "cost_local_currency": "SGD",
         "cost_rate_unit": rec.get("unit", "programme"), "estimated_hours": hours,
         "windows": {"8": {"sgd": p8, "state": rec["w8"], "basis": rec["wbasis"]},
                     "12": {"sgd": p12, "state": rec["w12"], "basis": rec["wbasis"]}},
         "fx_pair": "SGD/USD", "fx_rate": D.FX["rate"], "fx_date": D.FX["date"],
         "fx_source": D.FX["source"], "note": rec["note"],
         "rounding": "nearest whole US dollar"}, "Prices block")
    put("programme_costs", {"8": usd(p8), "12": usd(p12)}, "Prices block")
    put("transit_access", transit({"mrt": mrt, "mrt_m": mrt_m}, url, title, kind == "tag"),
        "Location — nearest station")
    fields["climate_access"] = claim(venue_id, "climate_access", climate(rec), MSS,
                                     "Meteorological Service Singapore — Climate of Singapore",
                                     locator="Seasons")
    if lat is not None and address:
        put("coordinates",
            {"latitude": lat, "longitude": lon, "checked_on": TODAY, "derived": False,
             "provider": "listing map pin" if kind == "tag" else "operator/venue locality",
             "precision": "published listing pin, not a surveyed entrance",
             "match": "listing"}, "map pin" if kind == "tag" else "venue locality")
    elif address and GEO.get(address):
        point = GEO[address]
        put("coordinates",
            {"latitude": point["latitude"], "longitude": point["longitude"], "derived": True,
             "checked_on": TODAY, "provider": "OpenStreetMap Nominatim",
             "query": address, "match": "address_geocode", "result": point.get("display_name"),
             "precision": "geocoded from the published address, not a surveyed entrance"},
            "geocoded address", derived_from=fields["address"]["claim_id"],
            note="One Nominatim lookup of the published address; geocode-log.json keeps "
                 "the raw response.")
    if cost_usd is not None and cost_usd > 5000:
        base = p8 or p12 or 0
        h = base / (8 if p8 else 12)
        r = "S${:,.0f}".format(h) if float(h).is_integer() else "S${:,.2f}".format(h)
        put("budget_exception", {
            "reason": ("The documented %s-hour figure is USD %s, above the USD 5,000 soft budget. Published rate: %s. It buys %s-hour room hire at that published rate only; catering, service charges, staffing, cleaning and AV add-ons are not included. Ask for an all-in quote covering the room, the mixer catering and any AV." % (hours, "{:,.0f}".format(cost_usd), rec["note"].rstrip("."), hours)),
            "comparable_usd": cost_usd, "window_hours": hours,
            "included": "Room hire for the %s-hour window at the published %s/hour rate." % (hours, r),
            "unknown_extras": "Catering, service charge, staffing, cleaning and AV add-ons are not itemised in the published rate."},
            "Prices block — rate card against the soft budget", quote=quote, derived=True,
            derivation="Published hourly rate multiplied by the %s-hour window, converted to USD at the dated SGD/USD rate." % hours)

    blockers = []
    if chosen is None:
        blockers.append({"claim_id": cid(venue_id, "blocker-price"), "field": "price",
                         "text": "No 8 h or 12 h price can be published from this page; the "
                                 "hire cost is unknown, not zero.",
                         "source_url": url, "verified_at": TODAY})
    evidence_rows = [{"claim_id": cid(venue_id, "evidence"), "observed_facts": observed,
                      "inference": rec["note"], "source_url": url, "source_title": title,
                      "verified_at": TODAY, "run_id": D.RUN_ID}]
    if not address:
        evidence_rows.append({
            "claim_id": cid(venue_id, "evidence-pin"),
            "observed_facts": ("The listing publishes a map pin but masks the street "
                               "address; no address claim and no coordinate claim are "
                               "written for this room."),
            "inference": "A pin without a checked address would look precise without being "
                         "verifiable, so the row carries no point until the operator "
                         "confirms the address.",
            "source_url": url, "source_title": title, "verified_at": TODAY,
            "run_id": D.RUN_ID})
    return {"venue_id": venue_id, "name": rec["name"], "names_seen": [rec["name"]],
            "city_slug": CITY_SLUG, "lifecycle": "open", "needs_human_verify": True,
            "tier_reasons": [], "verification_questions": rec["q"], "legacy_flags": [],
            "verification_question_kinds": ["final_quote", "availability"],
            "legacy_score": {"value": None, "breakdown": None,
                             "note": "No legacy score is carried; the 2026-08 shortlist rows "
                                     "were used as leads only."},
            "fields": fields, "history": {k: [v] for k, v in fields.items()},
            "blockers": blockers, "evidence": evidence_rows}

def clock(value):
    """`9:00` -> `09:00`; anything else is returned untouched."""
    text = str(value or "")
    if ":" not in text:
        return text
    hh, mm = text.split(":", 1)
    return "%02d:%02d" % (int(hh), int(mm)) if hh.isdigit() and mm.isdigit() else text

def span_text(span):
    """One listing span as `HH:MM-HH:MM`, with a midnight close written 24:00.

    The end changes only when the whole token is midnight: a plain
    `replace("0:00", "24:00")` also rewrites `20:00` into `220:00`.
    """
    start, end = clock(span[0]), clock(span[1])
    return "%s-%s" % (start, "24:00" if end == "00:00" else end)

def access_text(rec):
    f = FACTS[rec["key"]] if rec.get("key") else None
    if not f:
        return rec.get("access")
    spans = {day: span_text(f["days"][day]["span"])
             if f["days"].get(day) and f["days"][day].get("span") else "closed"
             for day in ("Monday", "Saturday", "Sunday")}
    if spans["Monday"] == spans["Saturday"] == spans["Sunday"]:
        return "Daily %s" % spans["Saturday"]
    return "Mon %s; Sat %s; Sun %s" % (spans["Monday"], spans["Saturday"], spans["Sunday"])

def overnight_note(rec):
    """A printed span whose end clock is earlier than its start runs past midnight."""
    f = FACTS.get(rec.get("key"))
    if not f:
        return None
    for day in ("Monday", "Saturday", "Sunday"):
        row = f["days"].get(day)
        if not row or not row.get("span"):
            continue
        start, end = clock(row["span"][0]), clock(row["span"][1])
        if end != "00:00" and end < start:
            return ("The %s span runs past midnight: the listing prints %s, read here as "
                    "an overnight close at %s the next morning." % (
                        day, span_text(row["span"]), end))
    return None

def saturday_close(rec):
    """The printed Saturday span end as `HH:MM`, or None when no same-day clock is printed.

    A span that closes after midnight has no same-day closing time, so the field is
    omitted for it rather than written as an early-morning hour.
    """
    f = FACTS.get(rec.get("key"))
    row = f["days"].get("Saturday") if f else None
    if not row or not row.get("span"):
        return None
    start, end = clock(row["span"][0]), clock(row["span"][1])
    if end != "00:00" and end < start:
        return None
    return "24:00" if end == "00:00" else end

def window_status(rec):
    """The documented `event_window_status` enum, derived from the same window claims.

    `allows_to_6` is the enum's furthest close (18:00) for a room whose published hours
    cover the whole 09:00-21:00 programme; `allows_to_5` reaches 17:00 only;
    `cannot_to_5` is a sourced No; `unknown` otherwise.
    """
    if rec["w12"] == "yes":
        return "allows_to_6"
    if rec["w8"] == "yes":
        return "allows_to_5"
    return "cannot_to_5" if rec["w8"] == "no" else "unknown"


LEAD_DISPLAY = {
    "JustCo event space — Marina Square / UIC Building": "JustCo — Event Space",
    "The Working Capitol — 1 Keong Saik Road": "Working Capitol — Keong Saik",
    "Genting Hotel Jurong Ballroom 1 — Resorts World Sentosa": "Genting Jurong — Ballroom 1",
    "Lorong AI @ One-North (Vidacity Building, Level 3)": "Lorong AI @ One-North",
    "Aliwal Arts Centre — Multi-Purpose Hall": "Aliwal — Multi-Purpose Hall",
    "The Arts House — Screening Room": "Arts House — Screening Room",
}

def lead_record(rec):
    venue_id = vid("sg-", rec["name"], rec["url"])
    url, title = rec["url"], rec["title"]
    fields = {
        "display_name": claim(venue_id, "display_name",
                              LEAD_DISPLAY.get(rec["name"], rec["name"][:40]), url, title,
                              confidence="medium"),
        "about": claim(venue_id, "about", rec["about"], url, title, confidence="low"),
        "address": claim(venue_id, "address", rec["address"], url, title, confidence="medium"),
        "capacity": claim(venue_id, "capacity", rec["capacity"], url, title),
        "capacity_basis": claim(venue_id, "capacity_basis", rec["basis"], url, title),
        "lifecycle": claim(venue_id, "lifecycle", "lead", url, title),
        "source_url": claim(venue_id, "source_url", url, url, title),
        "booking_url": claim(venue_id, "booking_url", url, url, title),
        "programme_windows": claim(venue_id, "programme_windows",
                                   {"8": {"state": "unknown", "basis": "none"},
                                    "12": {"state": "unknown", "basis": "none"}}, url, title),
        "price": claim(venue_id, "price", None, url, title),
        "transit_access": claim(venue_id, "transit_access",
                                transit({"mrt": rec["mrt"], "mrt_m": rec["mrt_m"]}, url,
                                        title, False), url, title,
                                locator="Location — nearest station")}
    if rec.get("lat") is not None:
        fields["coordinates"] = claim(
            venue_id, "coordinates",
            {"latitude": rec["lat"], "longitude": rec["lon"], "checked_on": TODAY,
             "derived": False, "provider": "venue locality", "match": "listing",
             "precision": "locality point, not a surveyed entrance"}, url, title,
            locator="venue locality")
    return {
        "venue_id": venue_id, "name": rec["name"], "names_seen": [rec["name"]],
        "city_slug": CITY_SLUG, "lifecycle": "lead", "needs_human_verify": True,
        "tier_reasons": [rec["why"]], "verification_question_kinds": ["rental_terms"],
        "verification_questions": ["Obtain room-level capacity, hours and a hire rate from "
                                   "the operator before assessing this room."],
        "legacy_flags": [], "legacy_score": {"value": None, "breakdown": None,
                                            "note": "Lead: never scored."},
        "fields": fields, "history": {k: [v] for k, v in fields.items()},
        "blockers": [{"claim_id": cid(venue_id, "blocker-lead"), "field": "source_url",
                      "text": rec["why"], "source_url": url, "verified_at": TODAY}],
        "evidence": [{"claim_id": cid(venue_id, "evidence"), "observed_facts": rec["why"],
                      "inference": "", "source_url": url, "source_title": title,
                      "verified_at": TODAY, "run_id": D.RUN_ID}]}

def build_events():
    events = {}
    for ev in D.EVENTS:
        eid = vid("sg-ev-", ev["name"], ev["url"])
        fields = {
            "date_range": claim(eid, "date_range", {"start": ev["start"], "end": ev["end"]},
                                ev["url"], ev["title"], confidence="high"),
            "kind": claim(eid, "kind", ev["kind"], ev["url"], ev["title"]),
            "relevance": claim(eid, "relevance", ev["relevance"], ev["url"], ev["title"]),
            "status": claim(eid, "status", "confirmed", ev["url"], ev["title"]),
            "conflict_severity": claim(eid, "conflict_severity", "low", ev["url"], ev["title"])}
        if ev["venue"]:
            fields["venue"] = claim(eid, "venue", ev["venue"], ev["url"], ev["title"],
                                    confidence="high")
        events[eid] = {
            "event_id": eid, "name": ev["name"], "names_seen": [ev["name"]],
            "city_slug": CITY_SLUG, "fields": fields, "needs_human_verify": False,
            "history": {k: [v] for k, v in fields.items()}, "verification_questions": [],
            "evidence": [{"claim_id": cid(eid, "evidence"), "observed_facts": ev["facts"],
                          "inference": "", "source_url": ev["url"],
                          "source_title": ev["title"], "verified_at": TODAY,
                          "run_id": D.RUN_ID}]}
    return events

def build_communities():
    communities = {}
    for c in D.COMMUNITIES:
        cmid = vid("sg-com-", c["name"], c["url"])
        communities[cmid] = {
            "community_id": cmid, "name": c["name"], "city_slug": CITY_SLUG,
            "network": c["network"], "focus_tags": c["focus"], "cadence": c["cadence"],
            "activity_status": c["status"], "typical_venue": c["venue"],
            "member_size_public": c["members"], "contact_info": None, "cohost_open": False,
            "cohost_evidence_phrase": None, "verified_at": TODAY, "needs_human_verify": True,
            "source_url": c["url"], "source_title": c["title"],
            "verification_questions": ["Recheck the group's 2027 schedule and room."],
            "uncertainty_notes": ("Cadence is read from the dated events on the page, not "
                                  "from a stated schedule."),
            "evidence": [{"observed_facts": c["facts"], "inference": "",
                          "source_url": c["url"], "source_title": c["title"],
                          "verified_at": TODAY}]}
    return communities

def build_holidays():
    """2027 Singapore public holidays, weekdays computed from the recorded dates."""
    holidays, coverage = [], []
    base = {"jurisdiction_id": "SG", "source_url": MOM, "accessed_on": TODAY,
            "source_title": "Ministry of Manpower — Public holidays"}
    for name, start, day, end, note in D.HOLIDAYS:
        if weekday(start) != day:
            raise SystemExit("%s start %s is a %s, not the recorded %s"
                             % (name, start, weekday(start), day))
        for s, e in ([(start, start)] if not end else [(start, start), (end, end)]):
            holidays.append(dict(base, kind="public_holiday", holiday_name=name,
                start_date=s, end_date=e, observance="gazetted", derived=False, verified=True,
                needs_human_verify=False, source_locator="2027 public holidays table",
                source_edition="2027 table (page last updated 19 June 2026)",
                evidence={"observed_facts": ("%s %s (%s). %s" % (name, s, weekday(s), note)).strip(),
                          "weekday_basis": ("The weekday is computed from the recorded date, "
                                            "not copied from the first day of a multi-day "
                                            "holiday.")},
                verification_questions=[]))
    coverage.append(dict(base, kind="public_holiday_coverage", derived=False, start_date="2027-01-01",
        end_date="2027-12-31", verified=True, needs_human_verify=False, source_locator="2027 public holidays table",
        source_edition="2027 table (page last updated 19 June 2026)",
        evidence={"observed_facts": D.PUBLIC_COVERAGE_NOTE}, verification_questions=[]))
    coverage.append(dict(base, kind="school_holiday_coverage", derived=False, start_date="2027-01-01",
        end_date="2027-12-31", verified=False, needs_human_verify=True, source_edition="not read", source_locator="none",
        source_role=("gap record: the MOM page is cited only as the public-holiday authority already read, not as a school-holiday source; no MOE calendar was read"),
        evidence={"observed_facts": D.SCHOOL_COVERAGE_NOTE, "source_role_note": "This row records an absence of evidence, not a school closure or term date."},
        verification_questions=["Read the MOE 2027 school calendar before claiming any school-holiday span."]))
    return holidays, coverage

def build():
    venues = {}
    for kind, recs in (("tag", D.TAG_VENUES), ("op", D.OP_VENUES)):
        for rec in recs:
            rec = dict(rec)
            if kind == "tag":
                rec["access"] = access_text(rec)
                rec["access_note"] = overnight_note(rec)
                rec["closing"] = saturday_close(rec)
            else:
                for key in ("access", "access_note", "closing"):
                    rec.setdefault(key, None)
            rec["min_hours"] = None
            rec["window_status"] = window_status(rec)
            v = venue_record(rec, kind)
            venues[v["venue_id"]] = v
    for rec in D.LEADS:
        v = lead_record(rec)
        venues[v["venue_id"]] = v
    holidays, coverage = build_holidays()
    registry_sha = hashlib.sha256(REGISTRY.read_bytes()).hexdigest()
    supplement_sha = hashlib.sha256(SUPPLEMENT.read_bytes()).hexdigest()

    def requirement(kind, data, verify):
        return {"claim_id": cid("local", kind), "run_id": D.RUN_ID, "verified_at": TODAY, "language": LANG,
                "check_status": "checked", "needs_human_verify": verify, "source_url": data["source_url"],
                "source_title": data["source_title"], "source_locator": data["source_locator"],
                "quote": data["quote"], "value": data["value"]}

    mandatory = ("https://aitinkerers.org/all_cities", "https://luma.com/decentralized_ai_events?period=past")
    sources = [{"url": url, "title": title, "checked_on": TODAY, "check_status": status,
                "mandatory": url.startswith("https://miragather.com/") or url in mandatory,
                "note": note, "run_id": D.RUN_ID} for url, title, status, note in D.SOURCES]
    photos = PHOTO_DATA.get("venues", {}) if PHOTO_DATA else {}
    communities, events = build_communities(), build_events()
    inputs = {
        "records": {"path": "research/singapore/city/sg_data.py",
                    "sha256": hashlib.sha256((HERE / "sg_data.py").read_bytes()).hexdigest()},
        "tagvenue_facts": {"path": "research/singapore/city/tagvenue-facts.json",
                           "sha256": hashlib.sha256((HERE / "tagvenue-facts.json").read_bytes()).hexdigest()},
        "tagvenue_enumeration": {"path": "research/singapore/city/tagvenue-enumeration.json",
                                 "sha256": hashlib.sha256(ENUMERATION.read_bytes()).hexdigest()},
        "geocode_log": {"path": "research/singapore/city/geocode-log.json",
                        "sha256": hashlib.sha256(GEOCODE.read_bytes()).hexdigest()},
        "holiday_supplement": {"path": "research/singapore/city/holiday-supplement.json",
                               "sha256": supplement_sha}}
    if PHOTO_DATA:
        inputs["photos"] = {"path": "research/singapore/city/photos.json", "sha256": hashlib.sha256(PHOTOS.read_bytes()).hexdigest()}
    store = {
        "schema_version": "city-store/1", "city_slug": CITY_SLUG, "city_name": "Singapore",
        "country": "Singapore", "timezone": "Asia/Singapore", "currency": "SGD",
        "city_registry": {
            "path": str(CITIES), "sha256": hashlib.sha256(CITIES.read_bytes()).hexdigest(),
            "slug": CITY_SLUG, "registry_id": None, "note": D.CITY_REGISTRY_NOTE},
        "updated_at": UPDATED_AT,
        "event_context": {
            "attendance": 50, "budget_currency": "USD", "currency": "USD",
            "local_currency": "SGD", "soft_budget_usd": 5000.0, "duration_hours": 8,
            "preferred_duration_hours": 12, "start_local": "09:00",
            "fallback_end_local": "17:00", "preferred_end_local": "21:00"},
        "currency_assumptions": D.CURRENCY_ASSUMPTIONS,
        "venues": venues, "communities": communities, "events": events,
        "pending_event_matches": {}, "holidays": holidays, "coverage": coverage,
        "holiday_registry": {
            "path": str(REGISTRY), "sha256": registry_sha, "base_jurisdiction_ids": ["CA"],
            "base_holiday_rows": 354, "base_coverage_rows": 69, "jurisdiction_ids": ["SG"],
            "host_jurisdiction_id": "SG", "projection_year": 2027,
            "holiday_rows": len(holidays), "coverage_rows": len(coverage),
            "supplement": {
                "path": str(SUPPLEMENT), "sha256": supplement_sha,
                "jurisdiction_ids": ["SG"], "holiday_rows": len(holidays),
                "coverage_rows": len(coverage),
                "note": "Singapore public-holiday layer read from MOM on 2026-11-24; no school "
                        "calendar is included."}},
        "local_requirements": {
            "language": dict(requirement("language", D.LOCAL_LANGUAGE, False),
                             statutory_quote=D.LOCAL_LANGUAGE["statutory_quote"]),
            "alcohol": requirement("alcohol", D.LOCAL_ALCOHOL, True),
            "food": requirement("food", D.LOCAL_FOOD, True)},
        "visits": [], "photos": photos, "sources_consulted": sources,
        "runs": [
            {"run_id": D.RUN_ID, "kind": "refresh", "updated_at": UPDATED_AT},
            {"run_id": D.RUN_ID + "-inputs", "checked_on": TODAY, "inputs": inputs,
             "fx": {"pair": D.FX["pair"], "rate": D.FX["rate"],
                    "effective_date": D.FX["date"], "source": D.FX["source"]},
             "city_scope": {"slug": CITY_SLUG, "name": "Singapore", "country": "Singapore",
                            "timezone": "Asia/Singapore", "currency": "SGD"},
             "counts": {"venues": len(venues), "communities": len(communities),
                        "events": len(events), "holidays": len(holidays),
                        "coverage": len(coverage), "sources": len(sources)}}]}
    return store

def bundle_from(store):
    """The immutable run payload: the same facts, before merge into the store."""
    return {"schema_version": "city-run/1", "run_id": D.RUN_ID, "city_slug": CITY_SLUG,
            "checked_on": TODAY, "updated_at": UPDATED_AT,
            "venues": list(store["venues"].values()),
            "events": list(store["events"].values()),
            "communities": list(store["communities"].values()),
            "sources": [{"url": s["url"], "title": s["title"], "accessed_on": s["checked_on"]}
                        for s in store["sources_consulted"]]}

def main():
    global FACTS, GEO, PHOTO_DATA
    FACTS = json.loads((HERE / "tagvenue-facts.json").read_text(encoding="utf-8"))
    geocode = json.loads(GEOCODE.read_text(encoding="utf-8"))
    GEO = {row["address"]: row["result"] for row in geocode["lookups"]
           if row.get("status") == "matched" and row.get("result")}
    PHOTO_DATA = json.loads(PHOTOS.read_text(encoding="utf-8")) if PHOTOS.exists() else {}
    store = build()
    text = json.dumps(store, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    CITY.write_text(text, encoding="utf-8")
    bundle = json.dumps(bundle_from(store), indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    BUNDLE.write_text(bundle, encoding="utf-8")
    print("venues", len(store["venues"]), "communities", len(store["communities"]),
          "events", len(store["events"]), "holidays", len(store["holidays"]),
          "sources", len(store["sources_consulted"]))
    print("city sha256", hashlib.sha256(text.encode()).hexdigest())
    print("bundle sha256", hashlib.sha256(bundle.encode()).hexdigest())


FACTS, GEO, PHOTO_DATA = {}, {}, {}
if __name__ == "__main__":
    main()
