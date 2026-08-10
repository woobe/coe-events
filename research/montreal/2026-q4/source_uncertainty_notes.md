# Source Uncertainty Notes — Montreal Run A v2 (2026-montreal-v2)

Prepared 2026-08-09 by the Run A v2 research card (evidence-bound venue + calendar
research only; no scoring, no assembly, no speakers/communities/outreach).
Output directory: /home/joe/repo_dev/coe-events/2026-montreal-v2

## Fix Round 1 (2026-08-09) — evidence-integrity corrections

- P1-A remediation: every cited material source page was re-fetched as a full page
  on 2026-08-09 (curl with browser UA; Wayback Machine fallback with snapshot date
  for the two live-403 sources). Claims below are retained only where directly
  visible on the fetched source; unsupported values were nulled with matching
  verification questions.
- P1-B remediation: the currency attached to each Eventective amount was checked
  against the actual listing page. Every Eventective page embeds schema.org
  structured data (JSON-LD) declaring `priceCurrency: "CAD"` for the listed rates,
  so the CAD local amounts and the documented 0.72 conversion are retained with
  page-level source evidence. Versa Loft's own page renders only "175$/h" with no
  CAD declaration, so its cost fields were nulled (cost_basis unknown) and a
  cost_unknown question added; no conversion was applied without established source
  currency.
- Calendar sources (ALL IN, UCI Montréal 2026, MTL connect) were also re-fetched
  full-page and re-verified on 2026-08-09.

## Trusted-venue match result

- references/trusted_venues.json has 12 seed records across 9 city slugs:
  bangkok-th, budapest-hu, frankfurt-de, prague-cz, san-francisco-ca-us,
  seattle-wa-us, tokyo-jp, toronto-ca, vienna-at.
- montreal-qc-ca match: NONE (zero matches). Reported honestly as a provenance
  result, not a research failure. No trusted-venue seed was used as evidence for
  any Montreal venue.
- Note: trusted_venues.json contains toronto-ca (tv-09, Startuptive). That is a
  Toronto record, NOT a Montreal match, and was not substituted for Montreal.
- past_venues.json has 15 archive records; NONE is Montreal. No Montreal past
  venue seed existed, so all venue discovery was fresh this pass.

## Currency assumptions (CAD -> USD)

- Documented planning assumption used for every estimated_cost_usd in this
  package: CAD 1.00 = USD 0.72 (research-time manual conversion estimate).
  Recorded in city_input.json currency_assumptions and applied consistently.
- Every priced venue preserves the original local amount and currency
  (cost_local_amount + cost_local_currency "CAD").
- Eventective listing prices (e.g. "$480-$560 per event", "$200/hr") are
  Canadian-dollar listings on eventective.com. Currency evidence: each fetched
  Eventective page embeds schema.org JSON-LD structured data with
  `priceCurrency: "CAD"` attached to the exact listed rates (verified on all 14
  records on 2026-08-09). The visible text renders "$", but the page's own
  structured data declares CAD, so CAD is directly established by the source page
  rather than assumed. Each such record still carries a final_quote verification
  question asking Joe/venue staff to confirm the exact all-in total.
- Versa Loft's own page (versaloft.ca) lists "175$/h" with no CAD/C$ marker and no
  structured-data currency declaration, so its cost fields were nulled
  (cost_local_amount/currency null, estimated_cost_usd null, cost_basis "unknown")
  and a cost_unknown + final_quote verification question was added. The 0.72
  conversion was NOT applied without directly established source currency.
- Rate-derived estimates (cost_basis estimated_from_rate) document the math in
  rate_estimate_note: hourly rate x estimated hours, converted at 0.72.
  Examples: Kptur C$110/hr x 6h = C$660 = USD 475.20 (page JSON-LD declares CAD);
  Tango Studio Theater C$200/hr x 6h = C$1,200 = USD 864 (page JSON-LD declares
  CAD). These are planning estimates, NOT written quotes, and require a
  final_quote verification question by schema.
- No automatic live FX rate was fetched; the 0.72 figure is the same research-time
  planning assumption used in the v1 Montreal package for consistency.

## Observed source facts (full-page fetches, all accessed 2026-08-09)

### Calendar (6 conflict records, all informational flags for Joe)

- ALL IN 2026 (official allinevent.ai full-page fetch): September 16-17, 2026,
  Palais des congrès de Montréal, 6,500+ attendees, Canada's largest AI event;
  co-organized with SCALE AI and Mila. Ends two days before candidate Saturday
  09-19. Severity: medium adjacency. FLAG only.
- 2026 UCI Road World Championships (official montreal2026.org full-page fetch):
  September 20-27, 2026; the Elite Women and Men road races are on September 26
  AND 27, so candidate Saturday 09-26 is a race day with downtown street closures
  very likely. Severity: medium. FLAG only.
- MTL connect 2026 (official mtlconnecte.ca full-page fetch): October 13-16, 2026,
  8th edition. Adjacent to candidate Saturdays 10-10 and 10-17. Severity: medium.
  FLAG only.
- The Techfair (10times listing): September 30 - October 1, 2026, Mount Royal
  Center. Adjacent to candidate Saturday 10-03. Severity: low.
- ICBC 2026 (aggregator listings): the official IEEE ICBC 2026 is in Brisbane,
  Australia on June 2-4, 2026 — NOT Montreal and outside the window. The
  Montreal-titled "International Conference on Blockchain and Cryptocurrencies"
  remains an academic conference-index artifact with conflicting aggregator dates
  (Oct 28-29 conferenceindex.org vs Oct 26-27 waset.org). Severity: low, dates
  unconfirmed. FLAG only.
- Women in Tech Montreal 2026 (Eventbrite, carried from v1): October 29, 2026,
  6:00 PM; re-verification on 2026-08-09 surfaced only the general womenhack
  Montreal hub, not a live copy of the specific listing. Severity: low.
- AI Salon Montreal (Luma pages for September and October 2026 editions exist):
  recurring monthly AI founder/builders community salon; exact edition dates are
  NOT published in accessible search snippets, so it is documented here as a
  recurring community signal rather than a dated calendar_conflicts record (no
  fabricated date). Side-event/cross-promotion potential with a DeAI Day.
- Startupfest 2026 is July 8-10, 2026 (outside the window) and is not recorded
  as a flag.
- Absence of a found same-day flag for 10-03, 10-10, 10-17, 10-24, 10-31 in this
  pass is not proof those Saturdays are clean; local calendars are still filling.

### Venues (27 records in venues.raw.json) — verified-page evidence

All claims below were verified against the fetched source page on 2026-08-09.
Unsupported claims were nulled with matching verification questions.

- Tagvenue room pages (full-page fetches, direct): JUNIPER (50 seats theatre,
  C$690/day Saturday incl. tax, Wi-Fi + projector + flatscreen TV, kitchenette
  with JURA, external catering), THE HOOK (70 seats / 80 standing, C$1,500/day
  Saturday incl. tax, Wi-Fi + projector + flatscreen + PA, 13-foot bar), CARNEGIE
  (150 seats / 200 standing, C$2,600/day Saturday incl. tax, high-speed Wi-Fi +
  projector + flatscreen + PA, two bars, kitchen, 98x25 ft, 120 seated
  conferences). All at 397A Rue Ste Catherine Ouest (Quartier des Spectacles).
  These are the strongest candidates and the v1 eligible trio.
- Versa Loft Anaia Room (direct venue site fetch): 175$/h, min 5h, $100 cleaning,
  60 banquet / 80 cocktail, Bluetooth sound, weekend parking, NO screen
  documented, NO Wi-Fi documented, NO catering policy documented, and NO currency
  declaration — cost nulled to unknown (see Currency assumptions).
- Eventective listings (full-page fetches; page JSON-LD declares priceCurrency
  CAD): DissTorsion (90 cap header / 80 comfortably, $480-$560/event + $120-$140/hr,
  Wi-Fi + Bluetooth/AUX sound, kitchenette, outside catering), Kptur Studio (55 cap
  header, corporate $110/hr up to 50, retroprojector + black-out curtains, Wi-Fi),
  Studio Cuero (100 cap, $540/event or $135/hr, Sonos soundbar, kitchen, Wi-Fi),
  Le Balcon (250 cap theater, $900-$1,600 for 50 guests, menu $18-$32/person,
  Wi-Fi, full bar, kitchen), Van Houtte 100 McGill (50 cap, $1,000-$2,000/event,
  no AV/Wi-Fi details), Tango Renaissance Studio Theater (100 cap header, $200/hr
  Studio Theater, $800-$2,000/event, Wi-Fi, outside catering, liability insurance
  note), Groupe 3737 Coworking Space (150 cap, $35-$1,500/meeting range, Wi-Fi
  amenity confirmed on page, ground-floor conference room has TV), Maison Tela
  (250 cap across 5 studios, $275-$900/event, Wi-Fi), Les Connections Ralia
  (100 cap restaurant, $840-$1,700/event or $210-$425/hr, no Wi-Fi listed),
  Mon Loft Privé Espace des Arts (200 cap per Event Spaces section, $1,080/event,
  Wi-Fi, full bar, DJ equipment; page pricing block labels capacities
  inconsistently — room_assignment question added), Le Studio TD Galerie Lounge TD
  (240 cap, from $1,500/event, Salle Stevie Wonder 100 cap, on-site catering, no
  Wi-Fi listed), IMAGEMOTION Space B (200 max, $750-$2,500, projector + screens +
  Wi-Fi + Sonos + cyclorama confirmed), Espace Culturel Kawalees (99 cap theater,
  $100 Sun-Thu / $150 Fri-Sat, stage 12'x13', Wi-Fi, full bar/kitchen),
  Centre Communidée (75 cap, $600/event, Wi-Fi amenity confirmed on page, kitchen,
  stage, non-profit seeking partner), Pub L'Annexe St-Ambroise (80 cap,
  $700/event or $175/hr, Wi-Fi amenity confirmed on page, outside catering).
- Eventective page 2727 Coworking (full-page fetch): 8 cap conference rooms,
  $300/meeting full-day, projector + screen + Wi-Fi listed, gigabit internet
  (lead — capacity far below 50).
- Inquiry-only / no published rate or capacity (leads, all page-fetched):
  Hyatt Place Montreal Downtown (Wayback snapshot 2025-08-01: 557 sq m flexible
  venue space, 16 event spaces, largest Metropole A+B 222 sq m / 350 guests,
  address 1415 rue Saint-Hubert; rates inquiry-only — now shortlist_ready with
  oversized_capacity + cost_unknown), Notman House (official coming-soon page:
  rentals/events on hold during renovation; no address/Wi-Fi/capacity/rate on
  page — address nulled + location question), Ax.c Espace Ax-C (Place Victoria,
  former trading floor, two event spaces; no rates/capacities/Wi-Fi on page),
  District 3 Innovation Centre Concordia (1250 Guy Street Suite #600, bookable
  conference rooms + event venues, weekdays 9AM-5PM; no rates/capacities/Wi-Fi),
  Le Wagon Montreal Campus (5570 Avenue Casgrain suite 101 per page; community
  events; no rates/capacities/Wi-Fi), Crew Collective & Café (Wayback snapshot
  2026-05-10 of coolsevents.com article: former Royal Bank HQ, Old Port event
  space; no street address/capacity/rate/Wi-Fi on source — address nulled +
  location question), SAT Société des arts technologiques (mtl.org page: nonprofit
  since 1996, Satosphère, privatisable spaces; no rates/capacities/Wi-Fi on page).

## Inference vs observed fact

- All estimated_cost_usd values with cost_basis "published_rate" are directly
  sourced published prices converted at the documented 0.72 planning rate.
  With cost_basis "estimated_from_rate" they are analyst estimates: published
  hourly rate x estimated hours, documented in rate_estimate_note, and require
  a final_quote/booking_terms verification question by schema. They are NOT
  quotes.
- Eventective "$X/event" prices are CAD as declared by the page's own structured
  data (JSON-LD priceCurrency CAD, verified per record on 2026-08-09); the
  currency confirmation is still included as a final_quote verification question.
- "Capacity_comfortable" is the best supported published figure; capacity basis
  is recorded (seated/standing/venue_claim/unknown). Venues with unknown
  capacity (0 + basis unknown) are leads by schema, not selectable.
- Calendar severity is analyst judgment from dates/audience; no deterministic
  script uses it. All seven Saturdays remain in consideration (flags, not
  eliminations).
- The UCI road-race schedule (Sep 26-27) is the most consequential new calendar
  fact this pass: candidate Saturday 09-26 is likely to have downtown street
  closures and crowd pressure.

## Evidence gaps / why needs_human_verify is true on every venue record

- No venue has a written quote or confirmed live Saturday availability for any
  of the seven Saturdays; every record is an evidence-bound shortlist/lead input.
- Fix Round 1 completed full-page fetches for every cited material source
  (2026-08-09). Two live sources returned 403 and were retrieved via Wayback
  Machine with snapshot dates recorded: Hyatt Place meetings page (snapshot
  2025-08-01) and coolsevents.com Crew Collective article (snapshot 2026-05-10).
  Those snapshot dates are older than the research date and are flagged for
  freshness; live re-checks remain manual steps.
- Eventective prices may be ranges; the low end was used for
  estimated_cost_usd and the range is recorded in evidence/verification
  questions.
- Screen status is confirmed for only 4 of 27 records (JUNIPER, THE HOOK,
  CARNEGIE, IMAGEMOTION Space B); 23 are unknown. Under v2 this is a soft flag
  (screen_unknown), not an exclusion — Joe may supply equipment or accept a
  workaround.
- Wi-Fi is confirmed for 16 of 27; 11 unknown (Versa Loft, Van Houtte,
  Les Connections Ralia, Le Studio TD, Hyatt, Notman, Ax.c, District 3,
  Le Wagon, Crew, SAT). The Eventective amenity lists confirmed Wi-Fi for
  Groupe 3737, Centre Communidée, and Pub L'Annexe on 2026-08-09; the
  non-Eventective leads (Hyatt, Notman, Ax.c, District 3, Le Wagon, Crew, SAT)
  were set to unknown where their cited pages do not mention Wi-Fi.
- Montreal public calendars for Sep-Oct 2026 are still filling; absence of a
  flag is not proof of a clean date.

## Expected tier picture (analyst expectation, NOT scoring output)

- eligible (fully evidenced, no questions): none expected from this raw pass —
  every record carries verification questions, which is honest for
  research-only evidence. The later deterministic pipeline (score_venues.py)
  owns the final tier/score.
- shortlist_ready (plausible, manual checks remain): JUNIPER, THE HOOK,
  CARNEGIE, Kptur Studio, Tango Renaissance, Espace Culturel Kawalees,
  DissTorsion, IMAGEMOTION Space B, Pub L'Annexe, Mon Loft Privé, Les
  Connections Ralia, Studio Cuero, Centre Communidée, Le Balcon, Versa Loft
  (cost_unknown now), Van Houtte, Hyatt Place (capacity now page-supported),
  Le Studio TD, Groupe 3737, Maison Tela — 20 venues per the 2026-08-09 scorer.
- lead (material gap): 2727 Coworking (capacity ~8), Ax.c (no capacity/rate),
  Notman House (rentals on hold), District 3 (no capacity/rate), Le Wagon
  (no capacity/rate), Crew Collective (no capacity/rate/address on source),
  SAT (no capacity/rate) — 7 venues per the 2026-08-09 scorer.
- Under v2 relaxed rules this is a much broader shortlist than v1's eligible-3
  outcome; the difference is flags (screen/wifi unknown, cost_unknown,
  oversized_capacity, availability) instead of hard gates. Zero eligible in the
  raw package is acceptable per the plan; eligibility requires confirmed screen
  + Wi-Fi + sourced cost + no questions, which no research-only record can
  honestly claim.

## Next manual actions (for Joe / the assembly card)

1. Run the deterministic pipeline commands exactly as in
   local/runA-v2-2026-nyc-montreal-plan-v1.md (Phase 3) once the raw package is
   accepted — do NOT hand-edit tier/score fields.
2. Contact-verify the top shortlist candidates for the preferred Saturday:
   COLLECTIF MTL (JUNIPER / THE HOOK — both screen+Wi-Fi confirmed, priced,
   Quartier des Spectacles), Kptur Studio (retroprojector question), IMAGEMOTION
   Space B (screen+Wi-Fi confirmed, rate range), Versa Loft (confirm currency
   and exact rate — page does not declare CAD).
3. Confirm UCI road-race street closures for 09-26 before recommending that
   Saturday (race day per montreal2026.org); confirm ALL IN/MTL connect side
   programming if Joe wants side-event synergy on 09-19/10-10/10-17.
4. Confirm the AI Salon Montreal October 2026 date from its Luma page for
   cross-promotion potential.
5. Confirm the CAD->USD 0.72 planning assumption with a current FX rate before
   any cost comparison is finalized.
6. No outreach, booking, RSVP, or payment is authorized by this research pass.

## v2.2 data pass log (2026-08-09, data-only card)

- Added per-venue WGS84 latitude/longitude (~6dp) to all 27 records. 16
  Eventective-listed venues use the venue listing page's own embedded
  schema.org GeoCoordinates (authoritative; verified full-page 2026-08-09);
  the remaining venues were geocoded from their street address via
  OpenStreetMap Nominatim with evidence.geo set to the venue's own page.
  Notman House and Crew Collective have null coordinates because their
  records carry no street address on the cited source (map_location_unknown
  flag expected).
- Added v2.2 venue window fields per memo v3/v4: opening_hours,
  closing_time, max_booking_hours, event_window_status, event_window_evidence.
- event_window_status findings (8-hour default = 09:00-17:00):
  - allows_to_6: JUNIPER (Sat 8am-6pm), THE HOOK (Sat 8am-10pm), CARNEGIE
    (Sat 8am-10pm), 2727 Coworking (venue site advertises 24/7 access).
  - cannot_to_5: Ax.c (venue site: Mon-Fri 8:30am-4:30pm, Sat-Sun CLOSED)
    and District 3 (site states weekdays 9AM-5PM only; Saturday availability
    is a question -> status kept unknown with event_window question).
  - unknown (no claim-bearing window source; event_window verification
    question added): Versa Loft, DissTorsion, Kptur, Studio Cuero, Le Balcon,
    Van Houtte, Tango Renaissance, Groupe 3737, Maison Tela, Les Connections
    Ralia, Mon Loft Privé, Le Studio TD, IMAGEMOTION, Espace Kawalees,
    Centre Communidée, Pub L'Annexe, Hyatt Place, Notman, Le Wagon, Crew, SAT.
- Unknown-window venues got a soft "event_window" verification question and
  retain needs_human_verify true.
- cost_rate_unit added to all records per cost_basis (hour/day/event/unknown).
- Regenerated estimated_from_rate records from 6h to the 8h default:
  Kptur C$110/hr x 8h = C$880 = USD 633.60; Tango Studio Theater
  C$200/hr x 8h = C$1,600 = USD 1,152.00 (0.72 planning rate retained).
  Rate estimates are still planning estimates, not written quotes.
- Re-validation: venues.raw.json PASS exit 0; venues.shortlist.json
  re-scored (scorer-owned) 0 eligible / 20 shortlist_ready / 7 lead (top
  JUNIPER 0.8710); all shortlist tier collections schema-valid when scored
  fields are allowed. city_input.json now carries event_duration_hours 8 and
  validates clean.
- city_bundle validation against the CURRENT .bundle-4 event_plan.json
  FAILS as expected (219 errors): the published bundle is still schema 2.0
  (missing v2.2 fields + event_duration_hours). Republish is a later card;
  this card is data-only.
