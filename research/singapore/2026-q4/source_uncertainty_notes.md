# Source Uncertainty Notes — Singapore Run A v2.5 (singapore-sg)

Prepared 2026-08-10 by the Run A v2.5 research card (evidence-bound venue + calendar
research only; no bundle/summary generation here beyond the deterministic scorer
run, no speakers/communities/outreach, no comparison).

## Currency handling (documented rate)

- SGD-to-USD: European Central Bank euro foreign exchange reference rates,
  retrieved 2026-08-10 from the ECB daily feed
  (https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml): EUR 1 = USD
  1.1555 and EUR 1 = SGD 1.4785. Computed USD 1 = SGD 1.27953 (1.4785 / 1.1555),
  i.e. 1 SGD = USD 0.78153534. This is a date-stamped planning conversion, not a
  bank or venue quote. The same feed/date was used for the Budapest (HUF) and
  Hong Kong (HKD) passes.
- All local amounts are preserved in their published currency and code (SGD).
  USD estimates are analyst conversions labeled in evidence.inference and
  rate_estimate_note, and carry final_quote questions.
- GST treatment: Tagvenue room pages state 'All prices include GST'; the LLI
  rates PDF publishes both base and w/GST columns (the w/GST value was used for
  estimates). WeWork Tagvenue listings additionally note a cleaning fee and
  Event Management Fee starting at S$500 before GST, which are NOT included in
  the estimates and are carried as final_quote/booking_terms questions.
- Venues with no published price keep cost null + cost_unknown question (CALI,
  National Gallery rooms, TEC The Exchange, JustCo, The Arts House, Aliwal,
  Zion) per the plan's no-price-ceiling rule.

## Trusted-venue match result

- references/trusted_venues.json contains NO singapore-sg seed (12 records:
  san-francisco-ca-us x2, budapest-hu x2, vienna-at, seattle-wa-us,
  frankfurt-de, tokyo-jp x2, toronto-ca, prague-cz, bangkok-th).
- Expected and observed trusted-venue match for Singapore: ZERO. This is a
  provenance result (no seed exists for this city), NOT a suitability
  conclusion, and no other-city seed was substituted (same honest outcome as
  Hong Kong in this run).

## Calendar flags (7 records, all informational for Joe)

- TOKEN2049 Singapore 2026 (official token2049.com/singapore): Oct 7-8, 2026,
  Marina Bay Sands. World's largest crypto event; official press describes
  1,000+ side events across the week. Severity: high (Web3 audience in town;
  candidate Saturdays 10-03 and 10-10 adjacent). The literal phrase
  'side-event opportunity' is used in this record's evidence.inference because
  TOKEN2049's own positioning (1,000+ side events) genuinely supports a DeAI
  Day side-event designation that week; it is paired with a verification
  question.
- Formula 1 Singapore Airlines Singapore Grand Prix 2026 (official
  formula1.com/en/racing/2026/singapore + singaporegp.sg + tickets.formula1.com
  '09 - 11 Oct'): Oct 9-11, 2026. Candidate Saturday 2026-10-10 falls INSIDE
  the race weekend; citywide Marina Bay road closures, MRT crowding and
  elevated hotel/venue demand expected. Severity: high logistics awareness;
  FLAG only, never an elimination.
- Tech Week Singapore 2026 (official singaporetechnologyweek.com): Sep 29-30,
  2026, Sands Expo Convention Centre; five co-located shows incl Big Data & AI
  World Asia and Cloud & AI Infrastructure Asia. Severity: medium (AI cluster
  before 10-03).
- Tech in Asia Conference 2026 (official conference.techinasia.com): Sep 15-16,
  2026, Sands Expo; positioned as 'APAC's only enterprise-first AI conference'
  (1,500+ enterprise leaders). Starts on the first day of the 09-15..12-15
  coverage window. Severity: medium (before 09-19).
- Milken Institute Asia Summit 2026 (official milkeninstitute.org/events): Oct
  7-9, 2026, Singapore. Severity: low.
- Singapore FinTech Festival 2026 (official fintechfestival.sg): Nov 18-20,
  2026, Singapore Expo. Informational November awareness only.
- STACK Conference 2026 (official tech.gov.sg/events/stack-conference-2026/):
  Nov 4-5, 2026. GovTech's biennial flagship; the cited official page returned
  404 on 2026-08-10 fetch (indexed copy dated 10 July 2026), so the record
  carries a date-verification question. Informational November awareness only.
- Out-of-window discoveries (NOT stored as records): The AI Summit Singapore
  2026 (May 20-22, Singapore Expo, part of ATxEnterprise/Asia Tech x Singapore
  — official asiatechxsg.com FAQ), AI Everything Asia at GITEX Asia (April
  9-10, 2026 — official gitexasia.com), SuperAI (June 2026 edition; 2027 dates
  Sep 8-9 at MBS — official superai.com), and Tech in Asia/AI-Everything
  clusters outside the window.
- Undated/recurring signals (NOT stored as dated records): Singapore Future AI
  Summit 2026 (sfais.org confirms a 2026 'first annual' edition but publishes
  no dates or venue), ETHGlobal Singapore 2026 (no 2026 dates published on
  ethglobal.com at fetch time), NVIDIA AI Summit Singapore 2026 (no in-window
  2026 dates found). Reported as evidence gaps / recurring signals, never as
  fabricated dates.
- No claim is made that no other events exist in the coverage window; this is a
  search-coverage statement, and the discovery themes (Token2049-type Web3,
  SFF, Tech Week, AI/ML, startup) were actively hunted per the plan.

## Venues (18 records in venues.raw.json)

### Direct official venue pages / official documents (fetched live 2026-08-10, HTTP 200 unless noted)

- Lifelong Learning Institute (LLSG) — official Pay-Per-Use Schedule of Rates
  PDF (lli.sg, effective 1 September 2025): Training Room 1-1 (50 seminar /
  30 classroom, ~100 sqm) 8am-5pm block S$621.30 w/GST; Event Hall 2-1
  (120-140 seminar / 48-50 cluster, ~215 sqm) 8am-5pm block S$1,264.40 w/GST;
  all rates include projector and air-conditioning; Mon-Sun & PH 0800-2200.
  Two records; projector confirmed, Wi-Fi NOT stated on the PDF (unknown +
  question). STRONGEST budget fits in this city pass.
- National Gallery Singapore (nationalgallery.sg/venue-rental): Glass Room
  (standing 140), Ngee Ann Kongsi Auditorium & Foyer (seating 212 + 2
  wheelchair), Seminar Rooms (15-28), Rooftop Studios (23-28). Quote-based; no
  prices/AV/hours published. Four records (2 shortlist_ready, 2 leads).
- The Executive Centre — The Exchange (executivecentre.com/en-sg/event-space-venue/):
  Singapore Land Tower Level 4-5, 'versatile event spaces for 24 to 250 pax',
  function rooms 20-220 pax, quote-based. Recorded as a lead (capacity for a
  50-person room not published). The Tagvenue 'The Lounge' record at the same
  building is the scored counterpart.
- JustCo Marina Square (justcoglobal.com/en-sg/centre/justco-marina-square/):
  centre confirmed at 6 Raffles Boulevard #03-308; no public capacity/rates →
  lead with capacity + cost questions.
- Aliwal Arts Centre — Multi-Purpose Hall (aliwalartscentre.sg/venue-hire/ +
  Venuexplorer listing): up to 120 theatre / 150 standing, 'from SGD 1,000'
  (rate basis/session unclear → cost null + cost_unknown); address 28 Aliwal
  Street per NAC documentation (one directory lists 32 Aliwal Street —
  documented discrepancy, not a stored material question).
- The Arts House at the Old Parliament — Screening Room (theartshouse.sg/
  venue-hire/ via Wayback Machine 2024 snapshot because the live page is
  script-rendered; live page HTTP 200): official description 'This 75-seater
  film theatrette'; quote-based rental rates by category (Arts/General,
  Corporate/Private, Non-profit). Cost null + cost_unknown.

### Booking-platform records (Tagvenue.com/sg, fetched live 2026-08-10)

- Industrious at One George Street — Studio (formerly The Great Room; venue
  rebrand noted): 30 seats/30 standing → lead; S$1,875/day Mon-Fri, S$4,578/day
  Sat-Sun incl GST; 'No promoted and ticketed events allowed' rule is
  compatible with a free RSVP event.
- The Work Project Asia Square Tower 2 — Boardroom: 14 seats/24 standing →
  lead; S$321/hour Mon-Fri 9:00-18:00; Saturday/Sunday CLOSED (candidate
  Saturdays not bookable); official theworkproject.com confirms the Asia
  Square location.
- WeWork 21 Collyer Quay — Level 1 Auditorium: 55 seats theatre; S$963/hour
  Mon-Fri day, S$1,192/hour Sat & evenings incl GST; +cleaning/event-mgmt fee
  from S$500. Saturday 8h ≈ USD 7,452.72 → over soft budget.
- WeWork 21 Collyer Quay — Level 2 Business Centre: 120 seats/150 standing;
  S$1,399/hour day, S$1,759/hour Sat & evenings. Saturday 8h ≈ USD 10,997.77 →
  over soft budget.
- WeWork Suntec Tower 5 — Level 17 Common Area: 60 seats/100 standing;
  S$1,290/hour incl GST (weekends 9:00-23:00, weekdays 18:00-23:00 only);
  semi-private area. Saturday 8h ≈ USD 8,065.44 → over soft budget.
- The Executive Centre — The Lounge at Singapore Land Tower (The Exchange):
  50 seats/100 standing; S$818/hour Mon-Fri, S$1,227/hour Sat-Sun incl GST;
  day rate S$6,132 Sat. Saturday 8h ≈ USD 7,671.55 → over soft budget.
- CALI at Ascott Raffles Place — Raffles Place Function Room: 80 seats/70
  standing; session pricing only (afternoon from S$750, evening from S$950,
  min spend from S$1,000/session, S$48/person catering) → cost null +
  cost_unknown + final_quote.
- Meeting Room Rental Singapore (Zion Global Marketing) — Seminar Room 1:
  36 seats → lead; 'from S$60 hire fee' (rate unit unstated); Wi-Fi available,
  projector listed unavailable.

### Discovery gaps (not fabricated)

- *SCAPE (scape.com.sg): site unreachable from this environment (connection
  failures on repeated fetches; no Wayback snapshot found) — logged as a
  discovery gap, not recorded.
- The Projector: official site states the cinema closed in August 2025
  (theprojector.sg 'Page not found' notice: 'The Projector was Singapore's
  beloved independent cinema... until its closure in August 2025') — NOT
  recorded as a venue.
- The Substation (45 Armenian Street): closed for redevelopment since 2021;
  redevelopment 'will be completed in 2026' per The Straits Times (2026) —
  NOT recorded as a hireable venue until reopening is confirmed.
- Regus Singapore (regus.com.sg): bot-protected (Incapsula) — not recorded.
- Spaces / WeWork other centres, Distrii (distrii.com /sg/ 404), Found8
  (found8.co DNS failure), Trehaus (trehaus.co JS-redirect): no fetchable
  public capacity/rate evidence — not recorded.
- Hotels (Grand Hyatt Singapore hyatt.com blocked 403; The Fullerton Hotel
  quote-based meetings page; Swissôtel The Stamford 34 meeting rooms at
  Raffles City Convention Centre): no public 50-person room capacity/rate
  evidence was obtainable in this pass — logged as a hotel-sector evidence
  gap, not recorded. Not a claim that hotels are unsuitable.
- SMU / NUS / polytechnic function rooms: no public venue-hire page with
  capacity/rates found in this pass — not recorded.

## Inference vs observed fact

- All estimated_cost_usd values are analyst conversions from page-published
  rates using the documented ECB 2026-08-10 rate, labeled in evidence.inference
  and rate_estimate_note; they are NOT quotes and carry final_quote questions.
- cost_basis "estimated_from_rate" is used only for published hourly rates
  (WeWork Collyer L1/L2, WeWork Suntec, The Lounge) with 8-hour estimates
  matching the selected event duration; "published_rate" is used for published
  day/block rates (Industrious Saturday day, LLI 8am-5pm blocks).
- cost_basis "unknown" with null cost is used for quote-based venues (CALI,
  National Gallery rooms, TEC The Exchange, JustCo, Arts House, Aliwal, Zion).
- capacity_comfortable 0 with capacity_basis unknown marks unknown-capacity
  records (TEC The Exchange, JustCo) — they are leads, never candidates.
- Coordinates are Nominatim (OpenStreetMap) geocodes of the published
  addresses, recorded as source-supported map evidence (evidence.geo points at
  the venue page); they are planning aids, not venue-verified points.
- capacity_basis is venue_claim for all published capacities (no record in
  this pass published a seated-vs-standing split as a 'seated' claim).

## Scorer run (deterministic, no hand edits)

- Command: scripts/score_venues.py venues.raw.json --output
  venues.shortlist.json --budget-usd 5000 --target-attendance 50
  --event-date 2026-10-03 --event-duration-hours 8. (2026-10-03 is the plan's
  illustrative candidate date; Joe's actual date will be used at
  assembly/scoring time.)
- Result: eligible 0 / shortlist_ready 11 / lead 7. Top selectable: CALI at
  Ascott Raffles Place — Raffles Place Function Room (score 0.6650), then
  Lifelong Learning Institute (LLSG) — Training Room 1-1 (0.6156), The
  Executive Centre — The Lounge at Singapore Land Tower (0.6100), LLI Event
  Hall 2-1 (0.5955), WeWork 21 Collyer Quay Level 1 Auditorium / Level 2
  Business Centre / WeWork Suntec Level 17 Common Area (0.5650 each).
- Byte-identical on re-run (SHA-256 of venues.shortlist.json:
  77c287638ee0200483dd1518e25aeb8c921a1ee0). The shortlist file is
  scorer-owned; no hand edits were made to it.
- Expected tier summary stated honestly: 0 eligible (every record carries at
  least one soft verification question), 11 shortlist_ready, 7 lead —
  matching the actual scorer output.
