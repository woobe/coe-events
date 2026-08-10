# Source Uncertainty Notes — Hong Kong Run A v2.5 (hong-kong-hk)

Prepared 2026-08-10 by the Run A v2.5 research card (evidence-bound venue + calendar
research only; no speakers/communities/outreach, no bundle or summary generation).

## Currency handling (documented rate)

- HKD-to-USD: European Central Bank euro foreign exchange reference rates,
  retrieved 2026-08-10 from the ECB daily feed
  (https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml): EUR 1 = USD
  1.1555 and EUR 1 = HKD 9.0653. Computed USD 1 = HKD 7.845348 (9.0653 / 1.1555),
  i.e. 1 HKD = USD 0.1274640663. This is a date-stamped planning conversion, not
  a bank or venue quote.
- All local amounts are preserved in their published currency and code (HKD).
  USD estimates are analyst conversions labeled in evidence.inference and
  rate_estimate_note, and carry final_quote questions. Taxes/fees and AV add-ons
  remain verification questions where the page does not show them included.
- Rate-derived estimates use the selected 8 hours and `cost_rate_unit: hour`
  (Banyan HK$888/hr, Garage HKD 3,000/hr, the Hive Wan Chai HK$2,500/hr and
  HK$1,250/hr), each with a visible calculation note.
- Good Lab's published '$900-$1,200' hourly figures carry no HKD marker and the
  page's Webflow currency setting declares USD; per the Run A currency rule the
  HKD amount is not page-visible, so its cost is null with a confirm-currency
  question instead of an assumed conversion (same treatment as the Budapest
  Versa Loft precedent).
- The Wave homepage advertises an event-space Flash Sale 'From $1,200/Hour'
  without a currency marker; the official event-space page is quote-based, so
  cost stays null with a confirm-cost question.

## Trusted-venue match result

- references/trusted_venues.json contains NO hong-kong-hk seed (the 12-record
  reference covers San Francisco, Budapest, Vienna, Seattle, Frankfurt, Tokyo x2,
  Toronto, Prague and Bangkok).
- Expected and actual trusted-venue match: ZERO for hong-kong-hk. This is a
  provenance result, not a suitability conclusion. No seed from another city was
  substituted, and no HK venue was marked as a trusted/used seed.

## Calendar flags (5 records, all informational for Joe)

- Hong Kong FinTech Week x StartmeupHK Festival 2026 (official fintechweek.hk,
  corroborated by hkengage.gov.hk): Nov 2-6, 2026, HKCEC. Severity: medium.
  Largest fintech/AI/Web3 event in HK; after the last candidate Saturday (10-31).
- Sun Hung Kai Properties Hong Kong Cyclothon 2026 (UCI official listing
  uci.org/competition-details/2026/ROA/78464 + Discover Hong Kong/HKTB event
  page; direct fetch Cloudflare-blocked): Sunday Oct 11, 2026. Severity: high
  logistics awareness for the 10-10 weekend; race-day road closures historically
  affect 155 bus routes and 15 green minibus routes (The Standard).
- Hong Kong Wine & Dine Festival 2026 (official DiscoverHK page Cloudflare-
  blocked; 2026 dates per consistent secondary sources dailypeter.com,
  foodwithkidappeal.com, hungrytimes.com, gowheretoday.com): Oct 29 - Nov 1,
  2026, Central Harbourfront. Severity: medium. Candidate Saturday 10-31 falls
  inside; official HKTB confirmation is a verification question.
- Clockenflap Music & Arts Festival 2026 (official clockenflap.com, JS-rendered;
  dates corroborated by lifestyleasia.hk and littlestepsasia.com): Dec 4-6, 2026,
  Central Harbourfront. Severity: low; December awareness only.
- Business of Design Week (BODW) 2026 Summit (official 2026.bodw.com/en): Nov
  18-20, 2026, HKCEC. Severity: low; November awareness only.
- Out-of-window / non-dated signals (NOT stored as records):
  - Hong Kong Web3 Festival 2026 ran April 20-23 (official web3festival.org) —
    before the 09-15..12-15 coverage window.
  - WAIC UP! Global Summit ran January 16, 2026 at Hong Kong Science Park
    (official hkstp.org) — out of window.
  - AWS Summit Hong Kong 2026 ran June 17 at HKCEC (official aws.amazon.com) —
    out of window.
  - HKICC 2026 (Hong Kong International Computer Conference): official HKCS
    site (hkcs.org.hk / hkicc.hkcs.org.hk) was rate-limited in this pass and no
    2026 dates are published on reachable pages; the 2025 edition ran Nov 17-18
    at HKCEC. Recorded as a recurring November signal, not a dated conflict.

## Venues (21 records in venues.raw.json)

### Direct official venue pages (fetched live 2026-08-10, HTTP 200 unless noted)

- Blueprint (blueprint.swireproperties.com/en/event-venues/venues-up-to-50-persons/):
  Auditorium tiered seating for 50, 2 ceiling-mounted projectors + drop-down
  projection screens, 2 handheld + 2 clip mics, built-in speakers. WiFi not
  stated (question). No numeric price published (cost_unknown). 3/F Two Taikoo
  Place, Quarry Bay (Swire Properties).
- Banyan Workspace (banyanworkspace.com/corporate-events/): Event Spaces from
  HK$888/hour for 2,500 sq ft, 20 seated / 60 standing, screen/projector/mics/
  sound, catering, 24/7 access. 8h estimate 905.50 USD. WiFi not stated
  (question). Suite 1204, Eastern Harbour Centre, Quarry Bay.
- The Wave (thewave.com.hk/event-space/): 520-6,000 sq ft, capacity 40-500
  seats, high-speed Wi-Fi, projectors, printers, audio, LED screen option,
  24-hour access, partitionable. Quote-based page (cost_unknown); homepage Flash
  Sale 'From $1,200/Hour' without currency marker. 4 Hing Yip Street, Kwun Tong.
- Garage Society (thegaragesociety.com/service/event-space): Event Space from
  HKD 3,000/hour for up to 100 people at Tower 535 (Causeway Bay) and Beverly
  House (Wan Chai); AV systems + WiFi confirmed; screen not named (question).
  8h estimate 3,059.14 USD.
- Good Lab (goodlab.hk/service/venue-hiring): The Future Workshop Training
  Space approx. 720 sq ft, max 50 persons, AV system / table x12 / whiteboard
  and flipchart; office-hour $1,000 / non-office-hour $1,200 (standard), NGO/SE
  discounts; page currency setting declares USD with no HKD marker, so cost is
  null with a confirm-currency question. Lai Chi Kok, 2-min walk from MTR.
- the Hive Wan Chai (thehive.com.hk/events-venue-hire/): 21F Indoor Space
  HK$2,500/hour (40 seated / 60 standing, high-speed WiFi, sound system,
  projector & flip chart) — 8h estimate 2,549.28 USD; 21F Rooftop Terrace
  HK$1,250/hour (40 seated / 80 standing, sound system, outdoor furniture) —
  8h estimate 1,274.64 USD. 21/F Phoenix Building, 23 Luard Road, Wan Chai.
- PMQ (pmq.org.hk/the-site/event-venue-rental/): QUBE multi-purpose hall
  approx. 500 m² / 5 m headroom / 450 participants; Courtyard & Marketplace
  450; Taste Library ~30. No price/AV/WiFi published (questions). 35 Aberdeen
  Street, Central.
- The Mills (themills.com.hk/en/shopfloor/venue_rental/): Fabrica Atrium
  2,404 sq ft 'fully equipped for conferences', The Hall (glass skylight),
  M4 Atrium. No price/AV/WiFi published (questions). 45 Pak Tin Par Street,
  Tsuen Wan.
- Fringe Club (hkfringeclub.com/en/venues/2-Fringe+Dairy.html,
  .../6-The+Vault.html): Fringe Dairy seats ~80 / 150 standing, baby grand
  piano + drum kit, end bar; The Vault up to ~40 guests (below 50 -> lead).
  No price/screen/WiFi published (questions). 2 Lower Albert Road, Central.
- Eaton HK (eatonworkshop.com/en-us/hong-kong/meetings-events/): Anita 8'8"
  690 sq ft (theatre 45 / classroom 50 / boardroom 4), Michelle 2,570 sq ft
  (theatre 250), Maggie 2,100 sq ft (theatre 250), Kino & Kino Lounge 2,040
  sq ft (theatre 80 / classroom 40). No price/screen/WiFi published
  (questions). 380 Nathan Road, Jordan.
- Hong Kong Arts Centre (hkac.org.hk/en/venue/): Shouson Theatre 394 seats,
  Louis Koo Cinema 119 seats, McAulay Studio 73 seats. No price/screen/WiFi
  published (questions). 2 Harbour Road, Wan Chai.
- The Executive Centre (executivecentre.com/locations/hong-kong/event-spaces-
  in-hong-kong/): Function Rooms seating up to 20-220 pax across 28 Stanley
  Street, Three Garden Road, Two Chinachem Central, Prosperity Tower, Two
  Pacific Place, One Island East; high-speed Wi-Fi confirmed; no numeric price,
  no explicit screen name (questions).
- HKSTP Golden Egg (hkstp.org/en/rental/space/mice-venue/hong-kong-science-park-
  mice-venues): MICE venue with fibre-optic + WiFi, high-resolution screens and
  projectors, Meeting Rooms, Conference Halls, Grand Hall, Amphitheatre; price
  list PDF linked but numeric rates not visible in fetched text (cost_unknown
  question). 2 Science Park East Avenue, Sha Tin.
- The Langham Hong Kong Grand Ballroom (langhamhotels.com/.../grand-ballroom/):
  490 m² / theatre 450 / classroom 180 / reception 500; no numeric price
  published on fetched page (likely over budget — oversized/awareness lead like
  the Budapest New York Palace precedent). 8 Peking Road, Tsim Sha Tsui.
- HKCEC (hkcec.com/en/venue-introduction): meeting rooms S421-S430, S221-S230,
  N201-N212, N101-N112, theatres, Convention Hall, Grand Hall, Bauhinia Room,
  Chancellor Room; per-room capacities and prices not visible in fetched text
  (lead with capacity/cost questions). 1 Expo Drive, Wan Chai.
- theDesk (thedesk.com.hk/): coworking + events-space service across Wan Chai,
  Sheung Wan, Kwun Tong, Hung Hom, Tsim Sha Tsui; no capacity/price/AV/WiFi on
  fetched pages (lead). Registered address 29F Dah Sing Financial Centre,
  248 Queens Road East, Wan Chai.

### Discovery gaps (not fabricated)

- JCCAC (Jockey Club Creative Arts Centre) venue rental: the official pages are
  Chinese-first; the English venue-rental URL returns 404 and the Chinese page
  is out of the English-only scope. Logged as a discovery gap, not translated
  evidence.
- CoCoon (hkcocoon.org) is a JS login page with no public venue-hire content in
  this pass; logged as a gap.
- Campfire (campfire.hk) served a JS-only Hack Club landing page; Wong Chuk
  Hang location facts were only visible via secondary sources (incubator.hk
  blog), which are not claim-bearing for stored venue facts; logged as a gap.
- Ooosh (ooosh.hk), WeWork HK, Regus HK, Spaces HK, Compass Offices HK were
  JS-only, Incapsula-blocked, or Cloudflare-blocked in this pass; not recorded.
- Tagvenue has no Hong Kong section (404); Venuerific, Spacebase, Cvent and
  VenueHub pages were Cloudflare/JS-blocked or empty in this pass; co-working
  .com.hk is a directory with JS-rendered listings and was not used as a
  claim-bearing source.
- Hotel ICON (hotelicon.com) served a Houston hotel page in this pass; The
  Murray (themurray.com.hk) did not resolve; not recorded.

## Inference vs observed fact

- All estimated_cost_usd values are analyst conversions from page-published
  HKD rates using the documented ECB 2026-08-10 rate, labeled in
  evidence.inference and rate_estimate_note; they are NOT quotes and carry
  final_quote questions.
- cost_basis "estimated_from_rate" is used only for hourly HKD rates with
  8-hour estimates matching the selected event duration (Banyan, Garage, the
  Hive x2). No venue in this pass published a usable day/package price.
- Venues with no published price keep cost null + cost_unknown question
  (Blueprint, The Wave, Good Lab, PMQ, The Mills, Fringe Club x2, Eaton x2,
  HKAC x3, TEC, HKSTP, Langham, HKCEC, theDesk) — Joe's amendment 1: no price
  keeps a venue in consideration.
- Capacity_comfortable is the best published figure; capacity_basis records
  seated/standing/venue_claim/unknown. Venues with null capacity are recorded
  as 0 with capacity_basis unknown (schema requires an integer), making them
  leads (theDesk).
- Fringe Club The Vault (~40) and theDesk (0/unknown) are leads; all other
  records have capacity >= 50 or a 40-49 configuration with questions.
- Coordinates are Nominatim (OpenStreetMap) geocodes of the published
  addresses, recorded as source-supported map evidence (evidence.geo points at
  the venue page); they are planning aids, not venue-verified points.
- The Wave capacity is recorded as 250 (homepage 'Capacity up to 250 persons'
  and the 40-500 range on the event page) with a room_assignment question for
  the specific 50-person partition.

## Scorer run (deterministic, no hand edits)

- Command: scripts/score_venues.py venues.raw.json --output venues.shortlist.json
  --budget-usd 5000 --target-attendance 50 --event-date 2026-10-03
  --event-duration-hours 8. (2026-10-03 is the plan's illustrative candidate
  date; Joe's actual date will be used at assembly/scoring time.)
- Expected tiers: eligible 0 (no venue has all material facts evidenced AND
  confirmed screen+WiFi AND a sourced numeric cost AND zero questions);
  shortlist_ready ~15-17 (all 50+ capacity or 40-49 with confirmed screen/
  WiFi/published cost records); lead ~4-6 (Fringe Vault ~40, theDesk no
  capacity, Langham/HKCEC oversized or unproven capacity).
- The shortlist file is scorer-owned; no hand edits will be made to it.
