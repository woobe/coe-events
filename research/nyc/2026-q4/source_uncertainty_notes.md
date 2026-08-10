# Source Uncertainty Notes — NYC Run A v2 (2026-nyc-v2)

Prepared 2026-08-09 by the Run A v2 research card (evidence-bound venue + calendar
research only; no scoring, no assembly, no speakers/communities/outreach).

## Trusted-venue match result

- references/trusted_venues.json has 12 seed records across 9 city slugs:
  bangkok-th, budapest-hu, frankfurt-de, prague-cz, san-francisco-ca-us,
  seattle-wa-us, tokyo-jp, toronto-ca, vienna-at.
- new-york-ny-us match: NONE (zero matches). Reported honestly as a provenance
  result, not a research failure. No trusted-venue seed was used as evidence for
  any NYC venue.
- The historical past-venue seed (references/past_venues.json meetup-02: Numerai
  Community NYC Meetup 2022-09-24 at NYC Seminar and Conference Center) was used
  as a discovery head-start only; current suitability was verified from the
  official pricing page (Wayback snapshot because the live site returned HTTP
  429 on 2026-08-09).

## Observed source facts (from claim-bearing pages, all accessed 2026-08-09)

### Calendar (7 conflict records, all informational flags for Joe)

- UN Blockchain Week 2026 (official unblockchainweek.com/events page): Sept
  10-19, NYC, UNGA + NYFW, 10 days, 100+ experiences, explicitly includes an
  "AI × Blockchain Summit" (autonomous agents, on-chain intelligence) theme and
  a Sept 18 Washington Elite Gala at Times Square. Final day = candidate
  Saturday 09-19. Severity: high as a same-day awareness signal; FLAG only.
- Messari Mainnet 2026: dates UNCONFIRMED. blockchainacademics.com lists Oct
  6-8, 2026; webmobi lists "Sep 2026 | NYC" TBA; official messari.io/mainnet
  blocked by a Vercel security checkpoint on 2026-08-09; Pier 36 venue page
  still documents the 2025 edition (Sept 21, 2025). Severity: medium adjacency
  to 10-03/10-10.
- AI Week New York (Fall Edition) (pulse.nyc/ai-week + reenbit.com): Oct 5-11,
  2026, citywide community-led festival. Candidate Saturday 10-10 falls inside.
  Severity: medium.
- AI Engineer NYC 2026 (official ai.engineer/nyc/2026 page fetched live): Oct
  12-14, 2026, Sheraton New York Times Square, 1,000+ in-person. Adjacent to
  10-10 and 10-17. Severity: medium.
- Ripple Swell 2026 (official swell.ripple.com page fetched live): Oct 27-29,
  2026, The Shed (545 W 30th St), 1,500+ attendees, AI & Agentic Finance topic.
  Adjacent to 10-24/10-31. Severity: low (institutional audience).
- The Bridge Conference 2026 (coinpedia aggregator only): Oct 27, 2026, NYC.
  Severity: low.
- ONUG AI Networking Summit NYC Fall 2026 (official onug.net): Oct 28-29, 2026.
  Severity: low (enterprise audience).
- No same-day AI/Web3/crypto flags found for candidate Saturdays 09-26, 10-17,
  or 10-24 in this research pass; absence of a found flag is not proof of a
  clean calendar.

### Venues (20 records in venues.raw.json)

- Tagvenue room pages fetched live and claim-bearing: Nomadworks Times Square
  Innovation Hub (50 standing, from $300/hr, Sat 9am-4pm), Event Loft 1505
  Studio 1505 (175 seats/200 standing; tier pricing 26-50 people $250/hr, $99
  setup, 3h min), Large Flex Event Loft Studio Entire Space (60 seats/60
  standing, from $175/hr), Times Square Jay Suites Meeting Room I (52 seats,
  Sat-Sun from $400/hr or $2,800/day, tax included), LOFT39 3rd Floor Speakeasy
  (75 seated/125 standing, Wi-Fi + PA, corporate mixer from $2,500 min spend,
  no hourly rate captured), Love Studios Midtown Loft 23B (40 seats/50
  standing, conference offer from $895 min spend), Well& by Durst Astoria
  (70 seats/75 standing, from $10,000/session, in-house catering only), Jay
  Suites Chelsea Meeting Room C (14 seats, from $75/hr promo), Coalition Space
  Penn Station (12 seats, from $50/hr, no projector), Cre8ive NYC (13 spaces,
  up to 40 seats venue-wide, from $35/hr).
- Tagvenue hub listing pages fetched live: Exposed Brick Multi-Use Event Space
  Entire Venue (74 guests, from $160/hr, Bowery), Ideal Glass Studios Atrium
  (500 guests, from $1,250/hr, Greenwich Village), VOLUME - The Club (225
  guests, from $375/hr, Garment District), Jay Conference Bryant Park The Dubai
  Room (150 guests, from $3,000/hr), Bogart House Main Floor (300 guests, from
  $2,000/day, Williamsburg). These records carry only hub-level evidence; the
  specific room pages were not fetched for them (source_url points to the hub).
- Direct venue sites fetched live: Civic Hall (Union Square/Zero Irving; event
  rooms up to 75 attendees with A/V; community-event option and special
  nonprofit/community rates; no numeric rates published), CUNY Graduate Center
  (365 Fifth Ave; 10-400 guest spaces; high speed WiFi; livestreaming; no
  numeric rates published), The Farm SoHo SoHo 2nd Fl Loft Venue specific room
  page (447 Broadway; Main Venue option data-option-capacity "Up to 50 people",
  1,154 sq ft; price options Mon-Thu $350/h * $2,380/day, Fri-Sun $500/h *
  $3,400/day; FAQ: "The Farm Soho Event Venue can host 50 seated (theater
  style) or 75 standing, when additional rooms are booked"; rental includes
  WIFI, furniture, A/V with projector + large screen + TV + 2 wireless mics +
  speakers; 1h setup + 30min breakdown; 30-day full-refund cancellation).
- Official pricing via Wayback Machine (live site rate-limited HTTP 429 on
  2026-08-09): NYC Seminar and Conference Center (day rate $1,150 for up to 65
  attendees at 800sf including projector/screen, wireless Internet, whiteboard;
  also $975/30ppl, $1,075/45ppl; 2nd Floor Conference Hall $7,500/day). This is
  the past meetup-02 venue.
- Brooklyn Public Library meeting-rooms program confirmed via Wayback snapshot
  (live page Cloudflare-protected); policy details carried from same-day prior
  research and remain unverified (lead tier).

## Inference vs observed fact

- All estimated_cost_usd values with cost_basis "estimated_from_rate" are
  analyst estimates: published hourly rate × 6 estimated hours, documented in
  rate_estimate_note, and they require a final_quote/booking_terms verification
  question by schema. They are NOT quotes.
- Published day/session rates (NYC Seminar Center $1,150/day; Jay Suites
  Meeting Room I $2,800/day Sat; Well& by Durst $10,000/session; Bogart House
  $2,000/day) use cost_basis "published_rate" — directly sourced but still
  subject to final all-in confirmation (taxes already stated included on
  Tagvenue; other fees unknown).
- "Capacity_comfortable" is the best supported published figure; capacity basis
  is recorded (seated/standing/venue_claim/unknown). Standing-only venues
  (Nomadworks Innovation Hub 50 standing) carry a room_assignment question
  about seated configuration for a talk format.
- The Farm SoHo capacity was corrected on 2026-08-09 (Fix R1, refined by Fix
  R2): the specific SoHo 2nd Fl Loft Venue page
  (thefarmsoho.com/event-venues/the-farm-soho/) directly publishes "Up to 50
  people" for the Main Venue option (data-option-capacity, 1,154 sq ft).
  Capacity 50 is therefore retained and cited to that page with
  capacity_basis "venue_claim"; the earlier record carried a venue-claim 50
  from a prior research pass without a citation, which the v2 evidence
  contract does not allow. The page does NOT establish that the Main Venue
  alone seats 50 theater-style: its FAQ states the venue "can host 50 seated
  (theater style) or 75 standing, when additional rooms are booked", so the
  50-seat theater configuration is conditioned on additional rooms. Fix R2
  therefore changed capacity_basis from "seated" to "venue_claim" and routes
  seating/room composition to the room_assignment verification question.
  Saturday (Fri-Sun) pricing is $500/h * $3,400/day, so the 6-hour Saturday
  estimate was corrected from $2,100 to $3,000 (the $350/h figure is the
  Mon-Thu rate). Screen and Wi-Fi are confirmed by the page's
  included-amenities FAQ (projector + large screen + TV + mics + speakers +
  WIFI).
- Calendar severity is analyst judgment from dates/audience; no deterministic
  script uses it. All seven Saturdays remain in consideration.

## Evidence gaps / why needs_human_verify is true on every record

- No venue has a written quote or live availability confirmation for any of the
  seven Saturdays; every record is an evidence-bound lead/shortlist input.
- Peerspace NYC listings were Cloudflare-blocked (JS challenge) on 2026-08-09;
  no Peerspace record was entered this pass (the prior v1 pass had Tokyo Room
  and 5th & Mad as leads; v2 raw captures only claim-bearing pages fetched this
  run).
- NYC Seminar Center live pricing page returned HTTP 429 on 2026-08-09; a
  Wayback snapshot was used and live-rate confirmation is a manual step.
- NYU Kimmel Center / conference-event services page returned no renderable
  content (empty/JS-gated) on 2026-08-09; it is NOT in venues.raw.json because
  no claim-bearing content could be captured this pass.
- Brooklyn Public Library live page was Cloudflare-protected; only the Wayback
  snapshot (program existence) is cited, policy specifics are unverified.
- Messari Mainnet 2026 dates remain unconfirmed (conflicting third-party dates;
  official page blocked).
- Currency: all NYC prices are USD, so no conversion assumption is needed
  (currency_assumptions empty in city_input.json).

## Expected tier picture (analyst expectation, NOT scoring output)

- shortlist_ready (plausible, manual checks remain): Civic Hall (community
  rate question), CUNY Graduate Center, NYC Seminar Center, Nomadworks
  Innovation Hub, Event Loft 1505, Large Flex Event Loft Studio, Jay Suites
  Meeting Room I, Exposed Brick, VOLUME, Bogart House, The Farm SoHo (capacity
  50 now directly evidenced on the specific room page), LOFT39,
  Love Studios 23B, Cre8ive NYC, Well& by Durst (over_soft_budget),
  Ideal Glass Atrium (over_soft_budget), Jay Conference Dubai Room
  (over_soft_budget).
- lead (material gap): Coalition Space (capacity 12), Jay Suites Chelsea
  Meeting Room C (capacity 14), Brooklyn Public Library (capacity/fee/screen/
  Wi-Fi unknown).
- eligible (fully evidenced, no questions): none expected from this raw pass —
  every record carries verification questions, which is honest for
  research-only evidence. The later deterministic pipeline (score_venues.py)
  owns the final tier/score; these expectations are informational only.
- Zero eligible in the raw package is acceptable per the plan: eligibility
  requires confirmed screen + Wi-Fi + sourced cost + no questions, which no
  research-only record can honestly claim.

## Next manual actions (for Joe / the assembly card)

1. Run the deterministic pipeline commands exactly as in
   local/runA-v2-2026-nyc-montreal-plan-v1.md (Phase 3) once the raw package is
   accepted — do NOT hand-edit tier/score fields.
2. Contact-verify the top shortlist candidates for the preferred Saturday:
   Civic Hall (community-event rate for a free public DeAI Day), NYC Seminar
   Center (live rate + Seminar Room A availability), Nomadworks Innovation Hub
   (Saturday availability + seated config), Event Loft 1505 (26-50 tier quote),
   Jay Suites Meeting Room I (Saturday day rate + 50-seat comfort).
3. Confirm Messari Mainnet 2026 dates once the official page is reachable;
   confirm AI Week NY fall schedule for 10-10 side-event potential.
4. No outreach, booking, RSVP, or payment is authorized by this research pass.

## Fix R1 log (2026-08-09, review-driven)

- P1 (NYC): The Farm SoHo record was corrected per the v2 evidence contract.
  Before: capacity_comfortable 50 with capacity_basis "venue_claim" carried
  from a prior research pass with no citation and no capacity verification
  question. After: capacity 50 retained because the specific SoHo 2nd Fl Loft
  Venue page directly publishes "Up to 50 people" (Main Venue option,
  data-option-capacity) and the FAQ states the venue can host 50 seated
  (theater style) or 75 standing with additional rooms; capacity_basis
  "seated"; source_url/source_title updated to that specific room page;
  verification questions now availability + final_quote + room_assignment
  (soft only). Saturday (Fri-Sun) rate $500/h * $3,400/day corrected the
  6-hour estimate from $2,100 to $3,000 (the $350/h figure is Mon-Thu only);
  screen and Wi-Fi confirmed from the page's included-amenities FAQ.
- Re-ran raw validation (exit 0) and the deterministic scorer
  (exit 0): 0 eligible, 17 shortlist_ready, 3 lead — The Farm SoHo is
  shortlist_ready (score 0.52) with no material-gap reason, consistent with
  the remediation rule (it must be lead unless 40+ capacity is actually
  evidenced on the page; 50 is evidenced).
- Scanned all 20 NYC records for the same defect (a material capacity/cost/
  screen/Wi-Fi claim admitted as carried/assumed with no verification
  question): no other record has it. Tagvenue hub-only records (Exposed Brick,
  Ideal Glass, VOLUME, Dubai, Bogart) carry capacity figures directly on their
  cited hub pages; BPL already uses the evidence-safe unknown-capacity pattern
  (capacity_basis "unknown" + material capacity question, lead).
- No other NYC record was modified in this pass. Montreal files untouched
  (separate card).

## Fix R2 log (2026-08-09, review-driven)

- P2 (NYC): The Farm SoHo record's capacity basis and evidence prose now match
  the page exactly. Before: capacity_basis "seated" with inference prose
  claiming the 50-seat theater-style configuration is directly claim-bearing
  for the specific Main Venue. After: capacity_basis "venue_claim" (the
  page's own data-option-capacity "Up to 50 people" for the Main Venue
  option, 1,154 sq ft); inference prose now states the page does NOT
  establish that the Main Venue alone seats 50 theater-style — the FAQ's "50
  seated (theater style) or 75 standing" is explicitly conditioned on
  additional rooms being booked, so seating/room composition for a 50-person
  talk event is routed to the room_assignment question.
- The room_assignment verification question now explicitly asks whether the
  50 seated theater-style configuration requires additional rooms beyond the
  Main Venue, and what the all-in cost of the chosen room configuration is
  (kinds availability + final_quote + room_assignment unchanged; all soft).
- source_title updated to quote the FAQ's full conditional wording.
- Fresh HTTP re-fetch 2026-08-09 (curl browser-UA; "?nonitro=1" used to
  bypass the NitroPack lazy-load): page returned HTTP 200 and contains
  data-option-capacity "Up to 50 people" (Main Venue, 1,154 sq ft), price
  options Mon-Thu $350/h * $2,380/day and Fri-Sun $500/h * $3,400/day, and
  the FAQ sentence verbatim: "The Farm Soho Event Venue can host 50 seated
  (theater style) or 75 standing, when additional rooms are booked."
- Re-ran raw venue validation (exit 0 PASS) and the deterministic scorer
  (exit 0) at the exact card commands; tier/score are script-owned and
  unchanged by a basis-label correction (capacity_comfortable 50, >= 40).
  Final NYC tier counts: 0 eligible / 17 shortlist_ready / 3 lead — The Farm
  SoHo stays shortlist_ready (score 0.52, flags availability_unconfirmed +
  final_quote_required + stale_evidence, no material-gap reasons).
- No other NYC record was modified in this pass. Montreal files untouched
  (separate card; PASS in review).

## v2.2 data pass log (2026-08-09, data-only card)

- Added per-venue WGS84 latitude/longitude (~6dp) to all 20 records, geocoded
  from the venue's street address via OpenStreetMap Nominatim (accessed
  2026-08-09), with evidence.geo set to the venue's own page or a reliable
  geocoding source URL. Coordinates are NOT fabricated: venues with a
  street-level address were geocoded to that address; venue pages that embed
  their own schema.org GeoCoordinates (Eventective listings for Montreal)
  were used as the authoritative source where available.
- Added v2.2 venue window fields per memo v3/v4: opening_hours,
  closing_time, max_booking_hours, event_window_status, event_window_evidence.
- event_window_status findings (8-hour default = 09:00-17:00):
  - allows_to_6 (supports 18:00): Event Loft 1505, Large Flex, Times Square
    Jay Suites MR I, Exposed Brick, VOLUME, Well& by Durst, Bogart House,
    LOFT39, Love Studios, Cre8ive NYC, The Farm SoHo (operating hours
    Monday-Sunday 24/7 per venue page), Jay Suites Chelsea MR C.
  - allows_to_5 (supports 17:00 only): NYC Seminar Center (day rates
    Mon-Sun 8am-5pm).
  - cannot_to_5: Nomadworks Innovation Hub (Tagvenue lists Saturday
    9:00am-4:00pm, so an event ending 17:00 is NOT supported) and Coalition
    Space Penn Station (Tagvenue lists Saturday Closed).
  - unknown (no claim-bearing window source; event_window verification
    question added): Ideal Glass Atrium, Jay Conference Dubai Room (hub
    listing only), Civic Hall, CUNY Graduate Center, Brooklyn Public Library.
- Unknown-window venues got a soft "event_window" verification question and
  retain needs_human_verify true.
- cost_rate_unit added to all records per cost_basis (hour/day/event/unknown).
- Regenerated all estimated_from_rate records from 6h to the 8h default
  (event_duration_hours 8): Nomadworks $2,400, Event Loft 1505 $2,000, Large
  Flex $1,400, Exposed Brick $1,280, Ideal Glass $10,000, VOLUME $3,000,
  Jay Conference Dubai $24,000, Farm SoHo $4,000 (Fri-Sun rate), Coalition
  $400, Jay Chelsea $600. Rate estimates are still planning estimates, not
  written quotes.
- Address refinements from reliable sources (all claim-bearing):
  Exposed Brick -> 91 East 3rd Street, NY 10003 (Tagvenue room page);
  Ideal Glass -> 9 West 8th Street, NY 10011 (venue site);
  VOLUME -> 265 West 37th Street, NY 10018 (Tagvenue room page);
  Jay Conference Bryant Park -> 109 West 39th Street, 2nd Floor, NY 10018
  (Eventective);
  Bogart House -> 230 Bogart Street, Brooklyn, NY 11206 (Tagvenue venue page);
  Civic Hall -> 28 East 28th Street (Zero Irving), NY 10016 (public record;
  venue page says Zero Irving).
- Re-validation: venues.raw.json PASS exit 0; venues.shortlist.json
  re-scored (scorer-owned) 0 eligible / 17 shortlist_ready / 3 lead; all
  shortlist tier collections schema-valid when scored fields are allowed.
  city_input.json now carries event_duration_hours 8 and validates clean.
- city_bundle validation against the CURRENT .bundle-4 event_plan.json
  FAILS as expected (163 errors): the published bundle is still schema 2.0
  (missing v2.2 fields + event_duration_hours). Republish is a later card;
  this card is data-only.
- Known scorer artifact (documented, not a data error): Nomadworks carries a
  duplicated "duration_window_not_supported" flag because both the
  cannot_to_5 status and max_booking_hours (7 < 8) independently append the
  flag in score_venues.py. Skill code is not modified per card constraints.
