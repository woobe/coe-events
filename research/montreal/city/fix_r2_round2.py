"""R2 round-2 corrections for the Montreal store.

Three reviewer findings, nothing else:
  1. access windows: marketplace opening-hours / appointment blocks are not
     hire intervals (rule 3, plan 4.5); downgrade and keep the quote as reason;
  2. holiday_registry.supplement.path -> city-relative;
  3. the 19 catering claims: cite a carrying line, or downgrade to unknown
     with a note and list the lost citation.
Run with the fleet venv:  .venv/bin/python fix_r2_round2.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/home/joe/repo_dev/hermes-skills/plan-event/scripts")
import city_store  # noqa: E402

STORE = Path("/home/joe/repo_dev/coe-events/research/montreal/city/city.json")
CAPTURES = STORE.parent / "captures"
RUN = "run-20261126-mtl-r2"
ON = "2026-11-26"

store = json.loads(STORE.read_text(encoding="utf-8"))


def set_claim(venue, field, value, url, title, locator, quote, note=None,
              extra=None, confidence=None):
    """Replace one field claim, keeping the previous claim in `history`."""
    old = venue["fields"].get(field, {})
    entry = {
        "claim_id": city_store._claim(venue["venue_id"], field, value, ON, url or ""),
        "run_id": RUN,
        "verified_at": ON,
        "value": value,
        "source_url": url,
        "source_title": title,
        "source_locator": locator,
        "quote": quote,
    }
    if note:
        entry["note"] = note
    if confidence or old.get("confidence"):
        entry["confidence"] = confidence or old.get("confidence")
    if old.get("language"):
        entry["language"] = old["language"]
    for key, item in (extra or {}).items():
        entry[key] = item
    history = venue.setdefault("history", {}).setdefault(field, [])
    if old and old != entry and (not history or history[-1] != old):
        history.append(old)
    venue["fields"][field] = entry
    return entry


# --- 1. access ------------------------------------------------------------
COL_QUOTE = ("Opening hours \u2014 By appointment from 10 a.m. to 5 p.m. weekdays; "
             "By appointment weekends")
COL_LOC = "Operator room page, footer 'Opening hours' block"

collectif = {
    "mtl-13ee7228e4b2": ("carnegie", "Collectif MTL \u2014 Carnegie room",
                          "A 200-standing hall in COLLECTIF MTL with theatre seating "
                          "for 150 and a fitted prep kitchen. The operator publishes "
                          "only an appointment window, not a hire interval, and "
                          "external catering is allowed."),
    "mtl-a69fecaefa03": ("juniper", "Collectif MTL \u2014 Juniper room",
                          "A private meeting room in COLLECTIF MTL with theatre seating "
                          "for 50 and a kitchenette. The operator publishes only an "
                          "appointment window, so no hire interval is published."),
    "mtl-dd69fc532018": ("the-hook", "Collectif MTL \u2014 THE HOOK room",
                          "An open-floor studio in COLLECTIF MTL seating up to 70 in "
                          "theatre layout, with BYO alcohol and external catering "
                          "allowed. The operator publishes only an appointment window, "
                          "not a hire interval."),
}
for vid, (slug, title, about) in collectif.items():
    v = store["venues"][vid]
    url = "https://collectifmtl.com/en/espace/{}/".format(slug)
    basis = ("The operator's own room page publishes only 'By appointment from 10 a.m. "
             "to 5 p.m. weekdays; By appointment weekends', an appointment block with no "
             "hire interval; the Tagvenue 08:00-22:00 openingHoursSpecification is a "
             "marketplace opening-hours widget (refused, rule 3).")
    set_claim(v, "programme_windows",
              {"8": {"state": "unknown", "basis": basis},
               "12": {"state": "unknown", "basis": basis}},
              url, title, COL_LOC, COL_QUOTE,
              note="Neither an eight- nor a twelve-hour window is published.",
              confidence="medium")
    set_claim(v, "access_window", None, url, title, COL_LOC, COL_QUOTE,
              note="Opening hours are appointment-only; no hire interval is published.",
              confidence="low")
    set_claim(v, "closing_time", None, url, title, COL_LOC, COL_QUOTE,
              note="No published closing time for hire; the Tagvenue span is not a "
                   "hire interval.", confidence="low")
    set_claim(v, "booking_hour_cap", None, url, title, COL_LOC, COL_QUOTE,
              note="No published booking cap; the Tagvenue span is not a hire interval.",
              confidence="low")
    set_claim(v, "event_window_status", "unknown", url, title, COL_LOC, COL_QUOTE,
              note="No operator-published hire interval.", confidence="low")
    old_about = v["fields"]["about"]
    set_claim(v, "about", about, old_about.get("source_url"), old_about.get("source_title"),
              "Operator room page footer 'Opening hours' block; Tagvenue listing "
              "'Catering and drinks' block", None,
              note="Rewritten after the access downgrade; no clock claim remains.",
              confidence="medium")

# Studio Cuero: "Studio hours" is opening hours, not a hire interval.
v = store["venues"]["mtl-eeca8449dbec"]
CUERO_Q = "Studio hours 7:00am - 10:00pm After hours - booking available"
CUERO_LOC = "Studio Cuero home page, 'Studio hours' line"
CUERO_URL = "https://www.studiocuero.com/"
CUERO_T = "Studio Cuero \u2014 creative studio and event space"
cuero_basis = ("The only clock text is 'Studio hours 7:00am - 10:00pm', which is opening "
               "hours rather than a hire interval; 'After hours - booking available' "
               "publishes no fixed interval, so neither window is confirmed (rule 3).")
set_claim(v, "programme_windows",
          {"8": {"state": "unknown", "basis": cuero_basis},
           "12": {"state": "unknown", "basis": cuero_basis}},
          CUERO_URL, CUERO_T, CUERO_LOC, CUERO_Q, confidence="medium")
set_claim(v, "access_window", None, CUERO_URL, CUERO_T, CUERO_LOC, CUERO_Q,
          note="Opening hours only; no hire interval published.", confidence="low")
set_claim(v, "closing_time", None, CUERO_URL, CUERO_T, CUERO_LOC, CUERO_Q,
          note="'10:00pm' is an opening-hours close, not a hire end.", confidence="low")
set_claim(v, "booking_hour_cap", None, CUERO_URL, CUERO_T, CUERO_LOC, CUERO_Q,
          note="No published booking cap.", confidence="low")
set_claim(v, "event_window_status", "unknown", CUERO_URL, CUERO_T, CUERO_LOC, CUERO_Q,
          confidence="low")

# IMAGEMOTION: two separately sold blocks; eight hours fits the day block only.
v = store["venues"]["mtl-a2488d6b9f36"]
IM_Q = "Booking Duration * Day Rentals (8am - 5pm) Evening Rentals (5pm - 3am)"
IM_LOC = "IMAGEMOTION studio page, Booking Duration block"
IM_URL = "https://imagemotion.com/studio/"
IM_T = "IMAGEMOTION Studio & Event Spaces \u2014 booking page"
set_claim(v, "programme_windows",
          {"8": {"state": "yes",
                 "basis": "'Day Rentals (8am - 5pm)' is a nine-hour operator-published "
                          "block that covers 09:00-17:00."},
           "12": {"state": "no",
                  "basis": "The page sells day rentals (8am-5pm, nine hours) and "
                           "evening rentals (5pm-3am, ten hours) as separate blocks; "
                           "neither is twelve hours and their union is not continuous "
                           "hire (plan 4.5), so twelve hours is refused."}},
          IM_URL, IM_T, IM_LOC, IM_Q, confidence="high")
set_claim(v, "access_window", "08:00-17:00", IM_URL, IM_T, IM_LOC, IM_Q,
          note="Day rentals only; evening rentals 17:00-03:00 are sold separately.",
          confidence="high")
set_claim(v, "closing_time", None, IM_URL, IM_T, IM_LOC, IM_Q,
          note="Two separate blocks close at 17:00 and 03:00; no single hire close.",
          confidence="low")
set_claim(v, "booking_hour_cap", 10, IM_URL, IM_T, IM_LOC, IM_Q,
          note="Longest single block is the ten-hour evening rental.", confidence="high")
set_claim(v, "event_window_status", "yes", IM_URL, IM_T, IM_LOC, IM_Q,
          confidence="medium")

# Kawalees: contiguous 12:00-24:00, which does not contain 09:00-21:00.
v = store["venues"]["mtl-b1e93c63b00b"]
KA_Q = "12pm \u2013 4pm / 4pm \u2013 8pm / 8pm \u2013 12am (next day)"
KA_LOC = "Kawalees rental page, three consecutive four-hour blocks"
KA_URL = "https://kawalees.ca/event-space-rental/"
KA_T = "Espace Culturel Kawalees \u2014 event space rental"
set_claim(v, "programme_windows",
          {"8": {"state": "unknown",
                 "basis": "The rental page sells three consecutive four-hour blocks "
                          "from 12:00, so the earliest hire starts at 12:00; no interval "
                          "covering 09:00-17:00 is published."},
           "12": {"state": "unknown",
                  "basis": "The blocks total 12:00-24:00, contiguous but starting at "
                           "12:00; the published schedule does not contain the "
                           "09:00-21:00 window, so twelve hours inside it is not "
                           "published."}},
          KA_URL, KA_T, KA_LOC, KA_Q, confidence="medium")
set_claim(v, "event_window_status", "unknown", KA_URL, KA_T, KA_LOC, KA_Q,
          note="Published blocks start at 12:00; the 09:00 start is not published.",
          confidence="low")

# --- 2. relative supplement path -----------------------------------------
supp = store["holiday_registry"]["supplement"]
assert supp["path"].endswith("holiday-supplement.json"), supp["path"]
supp["path"] = "holiday-supplement.json"

# --- 3. catering citations ------------------------------------------------
EE_LOC = "Eventective listing JSON-LD, LocationFeatureSpecification list"
EE_Q = '{{"@type":"LocationFeatureSpecification","name":"{}","value":true}}'
TV_LOC = "Tagvenue listing, venue feature label 'External catering allowed'"
TV_Q = "External catering allowed"

cite = {
    "mtl-13ee7228e4b2": ("tagvenue", TV_Q),
    "mtl-a69fecaefa03": ("tagvenue", TV_Q),
    "mtl-dd69fc532018": ("tagvenue", TV_Q),
    "mtl-281cff0a7a6d": ("eventective", "Outside Catering Allowed"),
    "mtl-2fc617abde76": ("eventective", "Outside Catering Allowed"),
    "mtl-583f8727f3f3": ("eventective", "Outside Catering Allowed"),
    "mtl-5aff2a80fdee": ("eventective", "Outside Catering Allowed"),
    "mtl-6f6753b2d241": ("eventective", "Outside Catering Allowed"),
    "mtl-8ef00c25a80d": ("eventective", "Outside Catering Allowed"),
    "mtl-a2488d6b9f36": ("eventective", "Outside Catering Allowed"),
    "mtl-b6318fa3d1f6": ("eventective", "Outside Catering Allowed"),
    "mtl-eb0452047e00": ("eventective", "Outside Catering Allowed"),
    "mtl-8aee03975c77": ("eventective", "On-Site Catering Service"),
    "mtl-b1e93c63b00b": ("eventective", "On-Site Catering Service"),
}

bad = []
for vid, (kind, feature) in cite.items():
    v = store["venues"][vid]
    claim = v["fields"]["catering"]
    if kind == "tagvenue":
        quote, locator = TV_Q, TV_LOC
    else:
        quote = EE_Q.format(feature)
        locator = EE_LOC
    files = sorted(CAPTURES.glob(vid + "-*.html"))
    if not files:
        bad.append((vid, "no capture"))
        continue
    text = files[0].read_text(encoding="utf-8", errors="replace")
    if quote not in text:
        bad.append((vid, quote[:60]))
        continue
    claim["source_locator"] = locator
    claim["quote"] = quote
    claim["citation_checked_on"] = ON
if bad:
    raise SystemExit("uncited carrying line missing: {}".format(bad))

lost = {
    "mtl-184b7a111981": ("in_house_only",
        "The listing prints 'On-Site Catering Service' but states nothing about "
        "outside catering, so in-house-only was not supported."),
    "mtl-9b1cfe2df6f0": ("in_house_only",
        "The listing prints 'Fully Equipped Kitchen' only; no catering-policy line."),
    "mtl-be24c9002459": ("in_house_only",
        "The captured listing carries no catering line at all."),
    "mtl-bfeec3cc37f4": ("outside_allowed",
        "The listing prints pricing and house rules but no catering-policy line."),
    "mtl-edf77b252f04": ("in_house_available",
        "The captured listing carries no catering line at all."),
}
lost_ids = []
for vid, (old_value, why) in lost.items():
    v = store["venues"][vid]
    claim = v["fields"]["catering"]
    lost_ids.append({"venue_id": vid, "field": "catering", "previous_value": old_value,
                     "previous_claim_id": claim["claim_id"]})
    set_claim(v, "catering", "unknown", claim["source_url"], claim["source_title"],
              None, None,
              note="Citation lost: {}. The earlier '{}' value had no source_locator or "
                   "quote, so it is downgraded to unknown.".format(why, old_value),
              extra={"citation_lost": True}, confidence="low")

# --- 4. declared gaps -----------------------------------------------------
gaps = store["declared_gaps"]
access_gap = next(i for i, g in enumerate(gaps) if g["kind"] == "access")
gaps[access_gap] = {
    "kind": "access",
    "checked_on": ON,
    "text": ("Seven access claims carry no hire interval. CARNEGIE, JUNIPER and THE "
             "HOOK publish only an appointment window ('By appointment from 10 a.m. to "
             "5 p.m. weekdays; By appointment weekends') and a Tagvenue "
             "openingHoursSpecification; Studio Cuero publishes only 'Studio hours "
             "7:00am - 10:00pm'; IMAGEMOTION sells day (8am-5pm) and evening (5pm-3am) "
             "blocks separately, so twelve hours is refused; Kawalees publishes "
             "12:00-24:00, which does not contain 09:00-21:00; Centre humaniste prices "
             "4-, 8- and 12-hour rentals but publishes only an appointment block. No "
             "Montreal venue now carries a twelve-hour yes."),
    "evidence_refs": [
        "venues.mtl-13ee7228e4b2.fields.programme_windows",
        "venues.mtl-a69fecaefa03.fields.programme_windows",
        "venues.mtl-dd69fc532018.fields.programme_windows",
        "venues.mtl-eeca8449dbec.fields.programme_windows",
        "venues.mtl-a2488d6b9f36.fields.programme_windows",
        "venues.mtl-b1e93c63b00b.fields.programme_windows",
        "venues.mtl-bfeec3cc37f4.fields.programme_windows",
        "captures/op-collectif-carnegie.html",
        "captures/mtl-a2488d6b9f36-imagemotion-studio-event-spaces-space-b.html",
    ],
}
# The appointment-block entry is now covered by the six-row access gap above,
# so keep one access gap rather than two overlapping ones.
appointment_gap = next((i for i, g in enumerate(gaps)
                        if g["kind"] == "access" and i != access_gap), None)
if appointment_gap is not None:
    gaps.pop(appointment_gap)

gaps.append({
    "kind": "claims",
    "checked_on": ON,
    "text": ("Five catering values had no locator or quote and are downgraded to "
             "unknown: Mise au Jeu, Le Balcon, Van Houtte, Centre humaniste and Les "
             "Connections Ralia. The captured listings print no catering-policy line "
             "(Mise au Jeu prints only 'On-Site Catering Service', which does not "
             "establish in-house-only). The other fourteen of the nineteen catering "
             "claims are now cited to a line that carries the value."),
    "evidence_refs": [
        "venues.{}.fields.catering".format(item["venue_id"]) for item in lost_ids
    ] + ["captures/mtl-184b7a111981-mise-au-jeu.html"],
})
audit = {
    "store": "research/montreal/city/city.json",
    "run_id": RUN,
    "checked_on": ON,
    "audited": 19,
    "cited": len(cite),
    "downgraded": len(lost),
    "lost": lost_ids,
    "cited_claims": [
        {"venue_id": vid, "field": "catering",
         "quote": (TV_Q if kind == "tagvenue" else EE_Q.format(feature)),
         "source_locator": (TV_LOC if kind == "tagvenue" else EE_LOC)}
        for vid, (kind, feature) in sorted(cite.items())
    ],
}
(STORE.parent / "r2-round2-catering.json").write_text(
    city_store.dump_json(audit), encoding="utf-8")


def dump(value):
    """The store's own on-disk shape: one-space indent, ASCII-escaped, no final newline."""
    return json.dumps(value, indent=1, sort_keys=True, ensure_ascii=True)


STORE.write_text(dump(store), encoding="utf-8")
print("wrote", STORE)
print("catering cited", len(cite), "downgraded", len(lost))
