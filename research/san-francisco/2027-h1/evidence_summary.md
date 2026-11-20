# Evidence summary — San Francisco, 2027 H1

Raw Run A evidence for San Francisco, 2027-01-01 through 2027-06-30 (Q1+Q2 as one period).
Research completed 2026-11-20. Revised 2026-11-20 through several review passes. Earlier passes fixed the capacity distribution, the oversized-capacity flag threshold, the non-profit count unit, one future-dated community fact, the Wi-Fi and screen counts, the access-window wording, the stale "no active SF Web3 meetup" sentence in `city_input.json`, the derived-price wording, the provenance exceptions, the community date scope and the unsourced Z Space rate claim. This pass adds the Funding the Commons Forum 2027 calendar row and its in-window adjacent row, corrects the claim that every `published_rate` figure covers eight hours, and updates the calendar counts.
No bundle, no summary render, no date recommendation, no skill edit.

## Files and counts

- `city_input.json` — 1 record. Validated against `validate_city_input`: 0 errors.
- `venues.raw.json` — 16 venues. 15 carry latitude/longitude with an OpenStreetMap provenance URL; 1 (Common Space) is deliberately null because the platform masks the street address. `validate_venue`: 16/16 clean.
- `communities.raw.json` — 17 groups: 12 active with a past-dated 2026 in-person event, 3 intermittent, 2 dormant. `validate_local_community`: 17/17 clean.
- `calendar_conflicts.json` — 5 events, all inside San Francisco. `validate_calendar_conflict`: 5/5 clean.
- `calendar_context.raw.json` — 4 keys as specified; `host_holidays` and `host_coverage` empty; 2 adjacent events inside candidate weeks. `validate_adjacent_events` against all 26 candidate Saturday windows: 0 errors.
- `venue_discovery_log.md`, `community_discovery_log.md`, this file.

The JSON files carry no `score`, `venue_tier`, `tier_reasons`, `venue_flags` or `score_breakdown` — those are script-owned and belong to the scoring card, not to research.

## What changed in this revision

1. Four venue records were reclassified from `published_rate` to `estimated_from_rate`. CounterPulse, The Women's Building, Four One Nine and Common Space each multiplied a published **hourly** rate by eight hours while declaring `cost_basis: published_rate` with null rate operands, which read as a claim that the venue publishes USD 400 / 1,320 / 5,200 / 1,320 **per hour**. The real published rates are USD 50, 165, 650 and 165 per hour. All four now carry `cost_basis: estimated_from_rate`, `hourly_rate_usd` (50 / 165 / 650 / 165), `estimated_hours: 8`, `cost_rate_unit: "hour"`, and a `rate_estimate_note` naming the source, the tier used and the exclusions. `estimated_cost_usd` still equals `hourly_rate_usd × 8`.
2. The venue log's tier statement was recomputed from the scorer's own output rather than by hand. It now reads 0 eligible / 14 shortlist_ready / 2 lead, names Common Space as the second lead, and quotes the command and its verbatim output.
3. Two community records that were labelled `active` on future-only dates were fixed at the source. AI Tinkerers SF now cites its past offline editions of 2026-11-08 (AGI House SF, 170 Saint Germain Avenue) and 2026-09-12; Bay Area AI War Room now cites its past SF edition of 2026-10-17 (JOE & THE JUICE, 525 Market St, 25 attending, status PAST). Both keep `active`, now on a fact dated before the 2026-11-20 access date.
4. Four active community records were added, including the Web3 flank that was missing: SF Bitcoin Devs, Funding the Commons, ClawCamp San Francisco and the Decentralized AI Builders Meetup. The two sources the reviewer named were attempted once each first; the result of those attempts is recorded in `community_discovery_log.md`.
5. The NVIDIA GTC 2027 exclusion is retained but made auditable: the exact Caltrain URLs attempted, the two timetable editions that could be read and why they were rejected as stale, and the outcome of the June San Jose developer-event sweep are recorded below.
6. Round-2 documentation corrections, recomputed rather than hand-edited: the capacity distribution now reports 12 of 16 records inside the card's 50-125 band and 11 inside the tighter 70-125 band (4 above, 1 below); the venue log now states that `oversized_capacity` fires only above `CAPACITY_PARTIAL_MAX = 160`, which on this file means Ruth Williams and Z Space Steindler; the non-profit basket states its unit (nine organisations, ten records) and why Z Space sits in the commercial list; and the San Francisco AI Code and Coffee record now cites 2026-10-25 as its activity fact, with 2026-11-22 recorded as future scheduling only and carrying no attendance figure.

## Venue facts and tiers

Ten venues carry a price; six publish none and carry `cost_basis: unknown` with a `cost_unknown` question rather than an invented figure. Of the ten priced records, 6 are `published_rate` (a package, event or day price) and 4 are `estimated_from_rate` (published hourly rate × 8 hours). The six `published_rate` records do not all cover eight hours: SOMArts (day-long access) and The Marsh Mainstage and Studio (Friday-Sunday full-day) do; Root Division's USD 1,800 package covers 5.5 hours and an eight-hour booking is about USD 2,175 at its published USD 150/hour extra-hour rate; Alliance Française's USD 800 is a four-hour daytime tier priced for private events, and its published Saturday daytime window closes at 14:00 (with a separate 1-5pm additional fee tier), so it cannot support 09:00-17:00; and Ruth Williams' USD 900 is a "Base Rate Main Theater" with a five-hour event minimum and no defined rate unit.

- Among the records that do cover eight hours, figures span USD 400 to USD 5,200, and both endpoints are hourly-rate products, not published eight-hour prices: CounterPulse at USD 50/hour × 8 and Four One Nine at USD 650/hour × 8. Nine of the ten priced records sit at or below the USD 5,000 soft budget; only Four One Nine (USD 5,200) exceeds it, and it carries `over_soft_budget`.
- Cheapest: CounterPulse Main Stage, USD 400 (USD 50/hour private-event rate × 8).
- Most expensive: Four One Nine Middle Gallery Extended, USD 5,200 (USD 650/hour × 8, 2026 rate card).
- Largest package whose published attendance band overlaps the 50-125 target: SOMArts Essentials, USD 4,549 for 100-150 guests including day-long (8 hour) access and an in-house audio and lighting package with technician.
- Seated theatre options with a published weekend full-day rate: The Marsh Mainstage (105 seats, USD 2,500 Fri-Sun) and Studio (60-90 seats, USD 2,000 Fri-Sun).
- Non-profit or publicly-owned basket: nine organisations across ten venue records — SOMArts, Root Division, CounterPulse, The Women's Building, Ruth Williams Opera House, The Lab, Brava (two rooms, so two records), Gray Area and Alliance Française. On a record count that is 10 of the 16 records. Z Space is also a non-profit arts centre, but it runs a commercial rental programme and publishes no rate table (`cost_basis: unknown`), so it is listed in the commercial basket; counting it would give ten organisations and 12 of 16 records. This is a rental-posture classification (community or below-market versus commercial rental programme), not a verified 501(c)(3) register.
- Capacity spread: 60 (Brava Studio) to 300 (Ruth Williams Opera House). Against the card's 50-125 target band, 12 of 16 records sit inside it, 4 are above (SOMArts 150, The Lab 150, Z Space Steindler 236, Ruth Williams 300) and none is below. Against a tighter 70-125 band, 11 sit inside, the same 4 are above and 1 is below (Brava Studio 60); Alliance Française at 74 is inside the band, not below it.
- Connectivity is recorded as two separate fields because the two do not agree. `wifi_status: confirmed` appears on 3 records: The Lab (Wi-Fi), Common Space (Wi-Fi, 65-inch smart TV) and Gray Area (fiber internet). `screen_status: confirmed` appears on 6 records: Root Division, Ruth Williams Opera House, The Lab, Z Space Steindler, Alliance Française and Common Space. Whichever field a venue does not confirm stays `unknown` — 13 records carry `wifi_status: unknown` and 10 carry `screen_status: unknown`.
- Two records carry `event_window_status: allows_to_6`, on different kinds of evidence. SOMArts is live-page evidence: the Essentials package includes day-long eight-hour access, which covers 09:00-17:00. Common Space is archived evidence: its 07:00-24:00 daily hours come from the 2026-04-06 Wayback snapshot of the Peerspace listing, not from the live listing, so the window is published but second-hand. Alliance Française publishes a daytime Saturday window ending at 14:00 (with a separate 1-5pm additional fee tier), which is evidenced non-support for a 09:00-17:00 programme (`cannot_to_5`). The remaining thirteen records publish no clock window and stay `unknown`.

Tier counts, from the scorer (not hand-counted). Command:

```
python3 plan-event/scripts/score_venues.py \
  research/san-francisco/2027-h1/venues.raw.json \
  --output <scratch>/sf_scored.json \
  --budget-usd 5000 --target-attendance 50 \
  --event-date 2027-03-06 --event-duration-hours 8
```

Verbatim output:

```
eligible: 0
shortlist_ready: 14
lead: 2
top selectable: Alliance Francaise de San Francisco - Theater (score 0.7255, tier shortlist_ready)
```

- 2 leads: CounterPulse (a `capacity` question — its 108 seated figure exists only in third-party listings) and Common Space (a `location` question, which is a material kind, because the Peerspace address is masked and the coordinates are therefore null).
- 14 shortlist_ready: every other record, each with a price or an evidenced no-price state plus an evidenced capacity and soft gaps only.
- 0 eligible: no venue evidences Saturday availability, a written all-in quote, a confirmed screen and Wi-Fi, and an 8-hour window simultaneously. Claiming otherwise would require inventing an availability fact.

## Community facts

Twelve groups have a past-dated 2026 in-person San Francisco fact on their own page (all dated before the 2026-11-20 access date):

- AI Tinkerers SF — 2026-11-08 SF × MIT Hack Day at AGI House SF (45 capacity, offline) and 2026-09-12 Agents Everywhere global hackathon in San Francisco.
- SF AI — 2026-11-12 (AWS Builder Loft, 525 Market St), 2026-11-18 (50 Beale St); 16,434 members.
- San Francisco AI Code and Coffee — 2026-10-25 at Salesforce Park (35 attendees); 2,839 members. The 2026-11-22 edition shown on the page is future-dated relative to the 2026-11-20 access date, so it is noted as upcoming only and carries no attendance figure.
- AI Builders and Learners SF — in-person "Own Your AI" hack night on 2026-11-03; 3,709 members.
- SF Python — 2026-06-17, 2026-07-29, 2026-09-09, PyBay 2026-10-03; 13,223 members.
- AGI House SF — Voice AI Hackathon 2026-09-19; 80+ hackathons hosted.
- Hedge West SF — 2026-06-02, 2026-09-01; 267 members, 44-48 attendees per edition.
- Bay Area AI War Room — 2026-10-17 SF Edition at 525 Market St (25 attending, status PAST); monthly 1st/3rd Saturday series.
- SF Bitcoin Devs — 2026-10-01 Seminar 74 at DG717, 717 Market St (20 going) and 2026-09-03 Seminar 73 at Presidio Bitcoin, 38 Keyes Ave (12 going).
- Funding the Commons — 2026-03-14/15 SF forum and hackathon at Frontier Tower, 150-200 selected builders, offline format.
- ClawCamp San Francisco — 2026-11-18 build night, 2026-11-02 "Sovereign AI" Campfire at Tenki SF, 2026-10-25/26 hackathon.
- Decentralized AI Builders Meetup (BitsLab) — 2026-03-04 at AWS Builder Loft, 525 Market St, AI-x-crypto agenda.

Three are intermittent and two dormant, and the dormant labels matter: SF Ethereum's newest listed event is 2022-12-13 and CryptoMondays SF's is 2025-09-22.

The Web3 flank is better evidenced than in the previous revision but still uneven. SF Bitcoin Devs is a genuine monthly San Francisco group. Funding the Commons and the Decentralized AI Builders Meetup supply the DeAI/Web3 overlap. What remains missing is a general-purpose Ethereum or crypto social meetup with 2026 city activity: both tracked Ethereum-side groups are dormant, ETHGlobal's 2027 stops are Cannes (Apr 14-16), New York (Jun 14-16), Tokyo (Aug 23-25) and Lisbon (Oct 13-15), and Solana Breakpoint's first US edition is at Pier 48 on 2027-09-08..10 — outside H1.

## Calendar facts — what sits inside the window

In-window adjacent events (inside the Mon-Sun week of a candidate Saturday): **2**.

- Data + AI Summit 2027 (Databricks), 2027-06-21 through 2027-06-24, San Francisco. Its Thursday close leaves candidate Saturday 2027-06-26 in the same week (`2027-06-21` to `2027-06-27`). `opportunity_kind: ai`, `status: confirmed`. Same city, so no `rail` field.
- Funding the Commons Forum 2027, 2027-03-13 through 2027-03-14, San Francisco. It sits on candidate Saturday 2027-03-13 itself, inside the week `2027-03-08` to `2027-03-14`. `opportunity_kind: ai`, `status: confirmed` on the organiser page's live ticket call. Same city, so no `rail` field. The page names no venue.

Calendar conflicts (awareness only, never an automatic elimination):

- Funding the Commons Forum 2027 — `related`, ai, medium. 2027-03-13 through 2027-03-14, San Francisco. Same day as candidate Saturday 2027-03-13, so it is both a same-day competitor and the closest audience match in the window; the organiser page does not name the venue.
- Data + AI Summit 2027 — `related`, ai, medium. Both a side-event opportunity and same-week competition for venue and hotel capacity.
- AI Engineer World's Fair 2027 — `related`, ai, medium. Moscone West, 2027-06-29 through 2027-07-01, targeting 10,000. The date spills past the window edge: it starts inside H1 and ends on 1 July. In a bundle this produces one R2 `calendar_outside_date_window` warning on `end_date`; the real dates were kept rather than truncated.
- GDC Festival of Gaming 2027 — `major_other`, other, none. Moscone Center, 2027-03-01 through 2027-03-04, the same week as candidate Saturday 2027-03-06.
- RSA Conference 2027 — `major_other`, other, none. Moscone Center, 2027-04-05 through 2027-04-08, the same week as candidate Saturday 2027-04-10.

### NVIDIA GTC 2027 — in-window, different city, deliberately excluded, with the audit trail

GTC 2027 runs 2027-03-15 through 2027-03-18 in **San Jose** (nvidia.com/gtc, fetched 2026-11-20: "GTC 2027 March 15-18", "San Jose 2027 is coming March 15-18"). Its week contains candidate Saturday 2027-03-20, so it is genuinely in-window. An adjacent row for a different city requires a `rail` object carrying a **published direct main-station itinerary with a minute count**, and that is the one thing that could not be sourced:

- `https://www.caltrain.com/schedules/weekday-timetable` — HTTP 200, 739,981 bytes, but a JavaScript application shell: the extracted text is navigation and station names, no timetable grid.
- `https://www.caltrain.com/schedules` — HTTP 200, identical 739,981-byte app shell, same result.
- `https://www.caltrain.com/media/22286/download` — HTTP 200, PDF, readable. Titled "Printer-Friendly Caltrain Schedule", stamped **"EFFECTIVE September 12, 2022"**.
- `https://www.caltrain.com/media/31557/download?inline` — HTTP 200, PDF, readable. Same document family, stamped **"EFFECTIVE September 25, 2023"**.

Both readable editions predate Caltrain's 2024 electrification and the service recast that came with it, so any minute count taken from them would be a stale number presented as a current itinerary. Publishing it would violate the "no flights, published direct main-station itinerary only" rule in spirit while satisfying it in form. GTC is therefore recorded here as context and left out of machine-readable adjacency, per the review's second option. To add it legitimately, someone needs the current Caltrain timetable in a readable form (Caltrain Go, 511.org, or a printed current-edition PDF).

### June San Jose / South Bay developer-event sweep

Swept on 2026-11-20 as the review asked:

- Apple WWDC 2027 — `https://developer.apple.com/wwdc/` still serves "WWDC26" with no 2027 dates. No dates published, so no adjacency row is possible.
- Google I/O 2027 — `https://io.google/` still serves "Google I/O 2026". No dates published.
- Result: neither can be recorded as an adjacent row today. Both are the usual early-June South Bay anchors and should be re-checked when the organisers announce 2027 dates.

Also outside H1 and therefore not recorded as rows: Solana Breakpoint 2027 (2027-09-08..10, Pier 48), Salesforce Dreamforce season, and everything else in the autumn.

## Holiday and school-break sweep

The card's `host_holidays` and `host_coverage` are empty by instruction, so the sweep result lives here. All 26 Saturdays in the window were checked against the installed registry (`plan-event/references/school_holidays.json`), covering the US federal OPM 2027 schedule, California Government Code 6700, and the SFUSD 2026-27 district calendar.

Candidate Saturdays that land on a public holiday:

- 2027-02-06 — California Lunar New Year (actual). A Saturday collision, and the single most consequential one in San Francisco: this is the city's largest civic festival.
- 2027-04-24 — California Genocide Remembrance Day (actual).
- 2027-06-19 — California Juneteenth (actual), with the federal Juneteenth observed on Friday 2027-06-18, making a long weekend.

Long-weekend Saturdays (a holiday sits on the Friday, Sunday or Monday next to them):

- 2027-01-02 — New Year's Day is Friday 2027-01-01.
- 2027-02-13 — Lincoln Day is Friday 2027-02-12 and Third Monday in February is 2027-02-15.
- 2027-05-29 — Memorial Day is Monday 2027-05-31.

SFUSD break that empties the city:

- SFUSD Spring Recess runs 2027-03-26 through 2027-04-02. Candidate Saturday 2027-03-27 sits inside the break, and 2027-04-03 is the weekend immediately before school resumes on Monday 2027-04-05. Both are family-travel weekends.

No SFUSD break overlaps any other candidate Saturday in the window; the district calendar's next break is outside H1.

## Facts, inference, uncertainty

Facts (sourced, quoted on the page):

- Prices, fees and holiday dates are quoted from the venue's or registry's own page or file, with the URL and access date recorded, with two stated exceptions. CounterPulse's 108/149 seated capacity exists only in third-party listings (Cvent, Eventective and The Vendry) and those URLs are not stored in the record. Common Space's rate and 07:00-24:00 window come from a 2026-04-06 Wayback snapshot of a Peerspace listing, not from the live page. The venue log and the CounterPulse and Common Space bullets above say the same.
- The five calendar event dates are confirmed on the organisers' own pages (Moscone for GDC and RSA, Databricks for Data + AI Summit, AI Engineer for World's Fair, Funding the Commons for its 2027 forum). GTC's 2027 dates are confirmed on nvidia.com/gtc.
- Every community fact used to justify an `active` label names a dated event inside the preceding 12 months of 2026-11-20. The two `dormant` records deliberately sit outside that window: SF Ethereum's newest event is 2022-12-13 and CryptoMondays SF's is 2025-09-22.
- The three holiday collisions and the SFUSD recess come from the installed registry, which is itself sourced to OPM, the California Government Code and the district calendar.

Inference (labelled as such, not proof):

- That an eight-hour rate can be derived by multiplying a published hourly rate by eight (Four One Nine, CounterPulse, The Women's Building, Common Space). Each is described in `rate_estimate_note` and carries a `final_quote` or `booking_terms` question.
- That GDC and RSA will materially raise hotel and venue demand. The convention sizes are not published on the Moscone pages, so no attendance number is quoted.
- That the small remaining Web3 gap reflects platform visibility rather than the absence of a scene: SF Bitcoin Devs is healthy while the two Ethereum-side groups are dormant.

Uncertainty, stated rather than smoothed over:

- No venue has confirmed 2027 Saturday availability, a hold, or a written quote. Every venue is `needs_human_verify: true`.
- No venue except The Marsh, Ruth Williams, Alliance Française, SOMArts and Root Division itemises its staff, security, cleaning and insurance add-ons, so the published headline is not the all-in cost anywhere.
- The Women's Building page contradicts itself on weekend bookings; that contradiction is the first verification question on the record.
- Four One Nine's rate card is a 2026 card, so the 2027 price is genuinely unknown.
- Common Space can never reach a selectable tier until an address is obtained; its price also comes from an archived snapshot, not the live listing.
- The AI Collective's SF chapter could not be read (see below), so its absence from the community set is an access failure, not a finding.
- The Decentralized AI Builders Meetup rests on a single published edition page; `cadence` is null because none was observed.

## Contradictions and conflicts recorded

- Root Division publishes USD 1,800 for Front & Rear Galleries on the live site and USD 1,200 for the same galleries in a PDF FAQ on the same domain. Live page treated as current; both cited.
- The Women's Building: weekday-only rate line versus a Friday-Sunday 10 PM end time on the same page.
- GDC 2027: March 1-4 on the Moscone page, March 1-5 on one aggregator. Moscone treated as authoritative.
- AI Engineer World's Fair: dates confirmed as 2027-06-29..07-01, which straddles the end of the H1 window.
- Caltrain: the only readable published timetables carry 2022 and 2023 effective dates, which conflict with the current service; neither was used for a journey time.

## Deviations from the card, for reviewer attention

1. `region` and `timezone` are **not** in `city_input.json`. `validate_city_input` uses a closed key set (city_slug, city_name, country, target_date, date_window, target_attendance, currency, currency_assumptions, workflow_phase, budget_usd, event_duration_hours, decision_note, research_completed_on, open_questions, recommendation) and rejects unknown keys, so a `region` or `timezone` field would fail assembly. Both values are stated in the header of `venue_discovery_log.md` (added in review round 3) and in the registry stub (`plan-event/references/cities.json` carries region "North America" and timezone "America/Los_Angeles"). If the owner wants them inside `city_input.json`, the schema needs an explicit change.
2. `city_slug` is `san-francisco`, as the card specifies. Historical rows in `past_venues.json` and `trusted_venues.json` use `san-francisco-ca-us`; this package is internally consistent at `san-francisco` and does not modify those files.
3. Common Space has null coordinates by choice — the platform masks the address. 15 of 16 venues have coordinates, and the null pair is why it is a `lead`.
4. NVIDIA GTC 2027 is documented here with its attempted-source trail but is not in the machine-readable adjacency, for the rail-evidence reason above.
5. The card's `verify_command` uses `python3 -c`, which this environment refuses. The equivalent check was run by script: 8 files present, `venues 16 coords 15`.

## Follow-up that would materially improve this package

1. Call or email the top four priced venues (SOMArts, Root Division, The Marsh, The Women's Building) for a 2027 Saturday hold and an all-in eight-hour quote.
2. Obtain the current Caltrain timetable in readable form and add GTC 2027 as a rail-qualified adjacent event; re-check WWDC 2027 and Google I/O 2027 dates when announced.
3. Read the AI Collective SF Bay Area chapter through a browser that executes its client-side app, or ask the operator for the chapter's event feed.
4. Confirm the four Mission/SOMArts rates against 2027 rate cards where the venue publishes annually (Four One Nine is explicit that its card is a 2026 one).
