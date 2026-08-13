# Kyoto Run A (2027 Q2) — source uncertainty notes

Accessed/research date: 2026-08-13. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. This file is a local research artifact;
nothing here is a recommendation, elimination, or date commitment. `target_date`
2027-04-03 is a neutral technical placeholder for pipeline integrity; Joe
decides the date.

## 1. Calendar uncertainty

- Calendar-awareness coverage is 2027-03-15 through 2027-06-30, informational
  only. All six retained records are `major_other` logistics flags (Golden Week,
  cherry-blossom peak, Aoi Matsuri, BitSummit, World Masters Games 2027 KANSAI,
  June rainy season). No `related` record was retained because, as of
  2026-08-13, no 2027 Q2 Kyoto/Kansai AI/ML/data/web3/fintech/quant/DeAI/agent
  event has an official organizer page with published in-window dates. This is
  an honest evidence gap, not a false absence — see open question in
  city_input.json and re-check closer to Q2 2027.
- Golden Week 2027: official Cabinet Office holiday list (2027-04-29 Showa Day,
  05-03 Constitution Memorial Day, 05-04 Greenery Day, 05-05 Children's Day).
- Cherry blossom: the official Kyoto City Travel Guide calendar confirms the
  late-March-to-early-April hanami season (2026 updates ended April 10); the
  official 2027 forecast (Japan Meteorological Corporation et al.) is not yet
  published — the record uses the typical window with a verification question.
- Aoi Matsuri: Kamigamo Shrine official annual calendar lists May 15; 2027 date
  is May 15, 2027.
- BitSummit 2027: official bitsummit.org announces May 21-23, 2027 at Miyako
  Messe; 2026 edition attendance/scale from the official announcement and
  corroborating coverage.
- World Masters Games 2027 KANSAI: official wmg2027.jp/games/ states May 14-30,
  2027 (17 days); Kyoto City official page confirms Kyoto hosts the opening
  ceremony and athletics; organizing-committee athletics guide (2025-12-09)
  lists track & field at Takebishi Stadium Kyoto May 18-25, 2027.
- Rainy season: JMA official baiu page (early June to late July across most of
  Japan); the portion beyond June 30 is adjacent-Q3 context only.
- Adjacent-Q3 context (NOT records, per plan): Gion Matsuri (July 17 and 24,
  2027 — never an assertion July is in scope), ACL 2027 (August 17-22, Kyoto —
  the June 1-5 ACL date found in the ACL member-portal joint workshop call
  belongs to NAACL 2027 San Francisco; the ACL 2027 line says physically held in
  Japan August 17-22), IVS 2027 (recent editions early July in Kyoto; 2027 not
  yet announced), ETHTokyo (2026 edition September), PyCon JP / PyCon Kansai
  (later in the year), Kyoto Marathon 2027 (February 21, before the coverage
  window), MLPR 2026 (December 4-6, 2026, before the window; not recorded).
- All calendar prose is date-neutral about Decentralized AI Day (v2.8/v2.9
  family): no candidate-window, candidate-Saturday, coverage-window-range, or
  preferred-date phrasing appears in any record's evidence fields; verified by a
  family scan on 2026-08-13 (CLEAN). Factual dates of the external events are
  preserved as evidence facts.

## 2. FX conversion basis (stated, dated)

- All USD-equivalent amounts in this package use ONE stated, dated conversion
  basis: ECB euro foreign exchange reference rate dated 2026-08-12
  (EUR 1 = USD 1.1545; EUR 1 = JPY 183.67), fetched 2026-08-13 from
  https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml.
  Derived: USD 1 = JPY 159.0905; 1 JPY = USD 0.00628573.
- Every venue with a USD equivalent records its original JPY amount and this
  dated basis in `evidence.observed_facts` (and in `rate_estimate_note` for the
  one rate-derived estimate, FabCafe Kyoto). No FX rate is invented.
- Known gap: the ECB 2026-08-12 rate is a point-in-time published reference,
  not a live market rate and not a forecast for 2027 Q2; the conversion basis
  must be re-confirmed at booking time (recorded as an open question in
  city_input.json).
- Tax treatment: published venue rates are recorded as published. Where the
  venue explicitly states tax-inclusive (Kyoto University, Hearton Hotel Kyoto,
  Kyoto Terrsa, Campus Plaza Kyoto, KRP, FabCafe), the USD equivalent reflects
  that. Where the rate is tax-exclusive (Impact Hub Kyoto) or tax status is not
  stated (kokoka), the USD equivalent is computed from the published figure and
  the tax question is a verification question.

## 3. Venue uncertainty

- Impact Hub Kyoto (ih-052): treated as a DISCOVERY SEED per plan; its own
  current page (kyoto.impacthub.net/useourspace/) now carries claim-bearing
  capacity/pricing/AV/window evidence, so it is retained as a scored candidate
  (shortlist_ready, top score 0.7069), not a lead-only seed. Still needs
  availability, tax-inclusive total, and Wi-Fi confirmation.
- Kyoto University Clock Tower Centennial Hall: official fee pages publish
  per-hour holiday rates and capacities; external (non-university) booking
  eligibility is a manual check (the facility is a university building, not a
  general public venue). Retained shortlist_ready with soft availability/
  booking-terms questions.
- Hearton Hotel Kyoto: published hall fee table (tax-included, 7-8h brackets);
  AV inventory and Wi-Fi not published; availability via hotel inquiry.
- Kyoto Terrsa: official fee PDF (2026-04-01) with room rates; free Wi-Fi
  confirmed for all rooms; projector rental is a separate equipment fee;
  reservations via the Kyoto prefecture/municipality public-facility system.
- Campus Plaza Kyoto: official general-fee PDF (2025-07-01) with Hall and
  Conference Room 1 rates, tax-included; AV/Wi-Fi inventory not on the fee page.
- Kyoto Research Park (KRP): official fee page with full-day weekend rates
  (tax-included); A/B/C Conference Rooms school capacity 42 is below 50 (lead),
  Room 2 school 96 fits (shortlist_ready); AV/Wi-Fi per-room to confirm.
- kokoka (Kyoto International Community House): official fee page with Event
  Hall (theater 221 / school 130) and Conference Rooms 1 & 2 (34 each, joint
  use = 68); LAN in rooms; Wi-Fi documented only in the Interaction Lobby;
  tax status not stated on the fee page.
- ICC Kyoto: national-level conference center with a fee-table PDF (2026-07
  revision); no room-level capacity/rate extracted in this pass — retained as a
  lead (capacity, cost, window all unknown) until current claim-bearing
  evidence supports its material fields.
- THE TERMINAL KYOTO: machiya rental space; inquiry-only pricing and no
  published capacity/AV — lead.
- FabCafe Kyoto: 2F meeting space (14 tatami, about 23 m2) at JPY 5,500/hour
  (tax-included) — the only cost evidence is this hourly rate; capacity for 50,
  AV, Wi-Fi, and window unsubstantiated — lead (rate-derived 8h estimate
  recorded at JPY 44,000 / USD 276.57 for transparency, not a quote).
- Geo coordinates: all retained venues carry null lat/long this pass because no
  claim-bearing coordinate was captured from the cited source pages
  (map_location_unknown is informational, no tier/score effect). Coordinates
  can be added later from a sourced address/geo evidence.
- Hotels with conference rooms beyond Hearton (e.g., Granvia Kyoto, Rihga
  Royal, ANA Crowne Plaza) were considered but not retained because no official
  page with a published 50-person room + rate was captured in this pass; listed
  in the discovery log as unresolved, not as a false absence.

## 4. Community uncertainty

- activity_status labels are honest per the official own-page evidence: active
  (GDG Kyoto — Google I/O Extended 2026-06-27 at kokoka on its own event blog;
  Kyoto University Blockchain Research Center — 2025 conference edition + BCK26
  Dec 2026 announced), intermittent (Kashima-Takeuchi Lab — own-page news last
  dated 2024, no current public seminar scheduled; Learning Machines Group — no
  dated public events on own page), dormant (PyData Osaka — own Meetup page last
  visible event Oct 2022 and returned "Group not found" on direct fetch; HN
  Kansai — last visible Meetup event Jan 2020, own site 2020 copyright).
- cohost_open true ONLY for GDG Kyoto, backed by its own official page's
  explicit venue-provider solicitation language (quoted verbatim in the record);
  needs_human_verify true + verification question. All other records
  cohost_open false with no negative claim.
- contact_info is null for every record: the only visible contact routes are
  email addresses, Slack invites, or SNS links (refused by policy). No contact
  route was inferred.
- member_size_public: 266 for PyData Osaka (search-indexed count on its own
  Meetup page — flagged as needing verification because the live page returned
  "Group not found"); null elsewhere (never estimated).
- Honest empty search, recorded as explicit community-research open questions
  in city_input.json: AI Tinkerers has no Kyoto/Osaka chapter (only Tokyo in
  the official all_cities list); no standing Kansai quant community page and no
  public Kyoto University student AI/ML club page with observed activity were
  found; the Kyoto/Kansai web3 landscape beyond BCK is thin on own-page activity
  evidence. These are evidence gaps, never absence claims and never deferred to
  Run B.

## 5. Tooling / process notes

- web_extract was unavailable in this environment (search-only backend), so
  pages were fetched via curl with a browser user agent and parsed to text;
  Meetup pages returned "Group not found" on direct fetch for PyData Osaka and
  HN Kansai (bot-blocking or inactive groups) — search-indexed content was used
  as corroboration and the fetch outcome is recorded per record.
- All accessed_on values are 2026-08-13.
- No invented FX, price, capacity, contact, or availability values; unsupported
  material fields are null with precise verification questions.
