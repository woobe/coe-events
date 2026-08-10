# Montreal Run A v2 — Fix Round 1 resolution report (2026-08-09)

Task: t_2e5f01ce — Fix R1: Montreal Run A v2 (snippet provenance + CAD assumption P1s)
Review: local/runA-v2-research-review-v1.md (Montreal NEEDS REVISION, two P1s)
Scope: 2026-montreal-v2 only. 2026-nyc-v2 untouched.

## Method

Every cited material source URL was re-fetched as a full page on 2026-08-09 via
curl with a browser user agent. Two live sources returned HTTP 403 and were
retrieved from the Wayback Machine with the snapshot date recorded:

- Hyatt Place meetings page -> web.archive.org/web/20250801193940 (2025-08-01)
- coolsevents.com Crew Collective article -> web.archive.org/web/20260510145718 (2026-05-10)

Calendar sources (allinevent.ai, montreal2026.org, mtlconnecte.ca) were also
re-fetched full-page and re-verified.

## P1-A resolution — snippet provenance (per-record)

Retained claims are only those directly visible on the fetched source page.
Anything not page-supported was nulled and a matching verification question added
(material kinds for cost/capacity/location; soft for screen/wifi/availability).

Verified-page records (claims confirmed on the fetched page):

- JUNIPER — COLLECTIF MTL (Tagvenue full page): 50 seats, C$690/day Sat incl.
  tax, Wi-Fi + projector + flatscreen, kitchenette with JURA, external catering,
  397A Rue Ste Catherine Ouest. KEPT.
- THE HOOK — COLLECTIF MTL (Tagvenue): 70 seats / 80 standing, C$1,500/day Sat
  incl. tax, Wi-Fi + projector + flatscreen + PA, 13-foot bar, external catering.
  KEPT.
- CARNEGIE — COLLECTIF MTL (Tagvenue): 150 seats / 200 standing, C$2,600/day Sat
  incl. tax, high-speed Wi-Fi + projector + flatscreen + PA, two bars, kitchen,
  98x25 ft, 120 seated conferences. KEPT.
- Versa Loft — Anaia Room (versaloft.ca full page): 175$/h, min 5h, $100
  cleaning, 60 banquet / 80 cocktail, Bluetooth sound, weekend parking. The page
  does NOT declare CAD (no CAD/C$ marker, no structured data), does NOT mention
  Wi-Fi, and does NOT publish a catering policy. COST NULLED (cost_basis unknown)
  + cost_unknown question; wifi -> unknown + wifi question; catering -> unknown.
  No 0.72 conversion applied.
- 14 Eventective records (full pages): price, capacity, address, Wi-Fi, screen
  claims verified against each listing page. See P1-B section for the currency
  resolution. All material claims retained were page-visible; capacities with
  page-internal conflicts got room_assignment questions (Kptur 55 vs 40; Mon
  Loft Privé 200 vs 350 label).
- 2727 Coworking (Eventective full page): 8 cap, $300/meeting, projector+screen,
  Wi-Fi. Lead retained (capacity far below 50).

Leads nulled/adjusted (material fields unsupported by their cited pages):

- Hyatt Place Montreal Downtown: live page 403; Wayback 2025-08-01 confirms
  557 sq m, 16 event spaces, largest Metropole A+B 222 sq m / 350 guests,
  address 1415 rue Saint-Hubert; no numeric rates, no Wi-Fi on page. Capacity
  set to 350 (venue_claim, page-supported) -> moves from lead to
  shortlist_ready with oversized_capacity + cost_unknown + screen/wifi/avail
  questions.
- Notman House: official coming-soon page confirms rentals/events on hold;
  does not state address/Wi-Fi/capacity/rates. Address nulled + location
  question; wifi -> unknown + wifi question.
- Ax.c — Espace Ax-C: page confirms Place Victoria / former trading floor / two
  event spaces; no rates/capacities/Wi-Fi on page. wifi -> unknown + question;
  removed the unsupported "100,000 sq ft" claim from observed_facts.
- District 3 Innovation Centre: page confirms 1250 Guy Street Suite #600,
  bookable conference rooms + event venues, weekdays 9AM-5PM; no
  rates/capacities/Wi-Fi. wifi -> unknown + question; address corrected to page
  form.
- Le Wagon Montreal Campus: page shows 5570 Avenue Casgrain suite 101 (not the
  previously recorded 5333); no rates/capacities/Wi-Fi. Address corrected;
  wifi -> unknown + question.
- Crew Collective & Café: Wayback 2026-05-10 coolsevents article describes the
  venue (former Royal Bank HQ, Old Port, blank-canvas event space) but no street
  address / capacity / rate / Wi-Fi. Address nulled + location question;
  wifi -> unknown + question.
- SAT — Société des arts technologiques: mtl.org page confirms nonprofit since
  1996, Satosphère, privatisable spaces; no rates/capacities/Wi-Fi on page.
  wifi -> unknown + question.

Wi-Fi status corrections from page amenity evidence:

- Groupe 3737, Centre Communidée, Pub L'Annexe: Eventective amenity lists
  include Wireless Internet/Wi-Fi on the fetched page -> wifi_status confirmed,
  wifi question removed (and Groupe 3737 question-kind array realigned).
- Van Houtte, Les Connections Ralia, Le Studio TD, Versa Loft: pages do NOT
  list Wi-Fi -> wifi_status unknown with wifi question (unchanged for the first
  three; changed for Versa Loft).

## P1-B resolution — CAD currency (per-record)

The review asserted Eventective amounts were "assumed" CAD without page proof.
Resolution: each of the 14 Eventective listing pages was fetched in full and
each page embeds schema.org structured data (JSON-LD) declaring
"priceCurrency": "CAD" for the exact listed rates (verified per record
2026-08-09). That is page-level currency establishment, not a city-level
convention, so the CAD local amounts and the documented 0.72 conversion are
retained WITH source evidence. Each record still carries a final_quote
verification question.

Per-record cost evidence after the fix:

- DissTorsion Studio: $480-$560/event (CAD, page JSON-LD) -> 480 CAD = 345.60 USD. KEPT.
- Kptur Studio: corporate $110/hr (CAD, page JSON-LD) x6h = 660 CAD = 475.20 USD. KEPT.
- Studio Cuero: $540/event or $135/hr (CAD, page JSON-LD) -> 540 CAD = 388.80 USD. KEPT.
- Le Balcon: $900-$1,600 for 50 guests (CAD, page JSON-LD) -> 900 CAD = 648.00 USD. KEPT.
- Van Houtte (100 McGill): $1,000-$2,000/event (CAD, page JSON-LD) -> 1,000 CAD = 720.00 USD. KEPT.
- Tango Renaissance Studio Theater: $200/hr (CAD, page JSON-LD) x6h = 1,200 CAD = 864.00 USD. KEPT.
- Maison Tela: $275-$900/event (CAD, page JSON-LD) -> 275 CAD = 198.00 USD. KEPT.
- Les Connections Ralia: $840-$1,700/event (CAD, page JSON-LD) -> 840 CAD = 604.80 USD. KEPT.
- Mon Loft Privé Espace des Arts: $1,080/event (CAD, page JSON-LD) -> 1,080 CAD = 777.60 USD. KEPT.
- Le Studio TD Galerie Lounge TD: from $1,500/event (CAD, page JSON-LD) -> 1,500 CAD = 1,080.00 USD. KEPT.
- IMAGEMOTION Space B: $750-$2,500 (CAD, page JSON-LD) -> 750 CAD = 540.00 USD. KEPT.
- Espace Culturel Kawalees: $150 Fri/Sat (CAD, page JSON-LD) -> 150 CAD = 108.00 USD. KEPT.
- Centre Communidée: $600/event (CAD, page JSON-LD) -> 600 CAD = 432.00 USD. KEPT.
- Pub L'Annexe St-Ambroise: $700/event (CAD, page JSON-LD) -> 700 CAD = 504.00 USD. KEPT.

Nulled (page does not establish currency):

- Versa Loft — Anaia Room: page renders "175$/h" with no CAD/C$/structured-data
  declaration. cost_local_amount/currency + estimated_cost_usd -> null,
  cost_basis "unknown", cost_unknown + final_quote question added. The 0.72
  conversion was NOT applied.

## Deterministic pipeline evidence

Commands (from ~/repo_dev/hermes-skills/plan-event):

  python3 scripts/validate_schema.py venue 2026-montreal-v2/venues.raw.json
    -> PASS [venue], exit 0
  python3 scripts/validate_schema.py calendar_conflict 2026-montreal-v2/calendar_conflicts.json
    -> PASS [calendar_conflict], exit 0
  python3 scripts/score_venues.py 2026-montreal-v2/venues.raw.json \
      --budget-usd 5000 --target-attendance 50 --event-date 2026-10-03 \
      --output 2026-montreal-v2/venues.shortlist.json
    -> eligible 0, shortlist_ready 20, lead 7, top JUNIPER (0.8660), exit 0

Tier counts after the fix (vs review's independent exercise 19 shortlist-ready /
8 leads): Hyatt moved lead -> shortlist_ready because its Wayback snapshot
publishes room capacity (350 guests), so the capacity gate is now satisfied with
a room_assignment question. Versa Loft remained shortlist_ready (cost_unknown is
a soft flag). No tier/score fields were hand-edited; all tier/score/flags are
scorer-owned output.

## Changed files (2026-montreal-v2)

- venues.raw.json — per-record evidence corrections (P1-A + P1-B)
- venues.shortlist.json — regenerated by score_venues.py (scorer-owned)
- calendar_conflicts.json — observed_facts updated to full-page-verification
  language for ALL IN / UCI / MTL connect
- source_uncertainty_notes.md — rewritten to distinguish verified-page evidence
  from unavailable-source leads; CAD currency now documented with page JSON-LD
  evidence; Versa Loft cost-unknown documented
- city_input.json — currency_assumptions + open_questions updated to state the
  page-level CAD evidence and the Versa Loft exception

## Remaining risk (unchanged in kind)

- Live price, availability, taxes/fees, AV inclusions, room configuration remain
  manual confirmation items; no booking readiness is claimed.
- Wayback snapshot dates (2025-08-01 Hyatt, 2026-05-10 Crew) predate the event
  and are flagged for freshness; live re-checks are manual steps.
- Calendar listings remain awareness flags, never date eliminations.
