# R1 — San Francisco store refresh, revision 1 (research handoff, round 2)

Worker: jnr-research, card `t_f9db5e38`. Store: `research/san-francisco/city/city.json`.
Evidence root: `research/san-francisco/r1-2026-11/`. All reads on 2026-11-26 unless stated.
Round-2 fix log: `fix2/round2-log.json` and `fix2/gates.json`; state-holiday reconciliation
lives in `coverage[US-CA|public_holiday_coverage|2027-01-01]`.

## 1. Sourced facts (each line is a claim in the store with its own locator)

**Addresses.** All 16 rows re-read from the room-specific operator page and left unchanged:
80 Turk St (CounterPulse), 2781 24th St (Brava Lobby and Studio), 1345 Bush St (Alliance
Française), 4705 3rd St (Ruth Williams Opera House), 2665 Mission St (Gray Area), 1062 Valencia
St (Marsh Mainstage and Studio), 450 Florida St (Z Space Steindler and Lobby), 2948 16th St
(The Lab), 1131 Mission St (Root Division), 3543 18th St (Women's Building), 934 Brannan St
(SOMArts), 419 Tenth St (Four One Nine). Common Space's street and unit come from the owner's
visit record, not the Peerspace listing, which prints no street number.

**Coordinates.** One live Nominatim search per record, re-run for all 16 including those that
already carried a point. 4 `exact_venue` (CounterPulse, Bayview Opera House, The Lab, Women's
Building — each returned a POI named for the venue at the printed house number). 12 `building`
(house number matched, room entrance not proven). 0 street, 0 area, 0 unresolved. Fifteen
points are unchanged to seven decimals; Common Space moved 0.00011° north because the fresh
search resolved 3108 Fillmore to a named boutique at the same house number.

**Photos.** 49 URL-bearing assets re-checked (HTTP 206/200, type and pixel size recorded), then
45 cleared and 4 withheld as different rooms (two Gray Area main-room shots, SOMArts dance
studio and patio). 13 venues have 1+, 7 have 4+, 3 have none (Alliance Française, Marsh Studio,
Common Space). 43 of 45 are room views; the 2 fallbacks are Four One Nine's rooftop garden and
roof deck, both listed as included in the Middle Gallery package. Every asset is an operator
gallery image hotlinked with attribution; no venue publishes licence text.

**Holidays.** OPM's 2027 and 2028 tables print all 12 federal rows as stored. SFUSD's
board-approved calendars (approved 2026-01-27, announced 2026-02-07) print the seven school
rows now stored, including a Winter Recess 2026-12-21→2027-01-01 that the store was missing.
Local rows: 36 public, 7 school, 42 intersecting 2027 (43 local rows in all). The state
public layer holds 24 US-CA rows: the 18 statutory dates, each carrying its Government Code
6700 subdivision locator copied from the pinned registry (read 2026-11-20) because leginfo
returned HTTP 403 on 2026-11-26, plus six court-observance rows for the San Francisco
Superior Court's 2027 closures that have no exact statutory row (Farmworkers Day 9 April,
Juneteenth 18 June, Thanksgiving 25 November, Day After Thanksgiving 26 November, Christmas
24 December, New Year's Day 2028 on 31 December). The court list's 15 closures are reconciled
one by one in the coverage row: 9 match a stored statute row exactly, 6 are the court rows
above. 25 other US scopes and 294 foreign-country rows stay separate
(43 local + 25 other US + 294 foreign = 362).

**Events.** 54-cell theme × platform matrix: 48 cells read, 6 blocked (AI Tinkerers' national
roster returns 403 in every theme), 82 pages read. Four 2027-dated San Francisco events are
retained, each on its own organiser page: AI Engineer World's Fair (29 Jun–1 Jul 2027),
Data + AI Summit (21–24 Jun 2027), Funding the Commons Forum (13–14 Mar 2027), GDC
(1–4 Mar 2027). RSA Conference 2027 was dropped (organiser page 403).

**Access.** Three rooms publish an eight-hour band (Alliance Française Sunday 09:00–17:00,
Women's Building weekdays 09:00–17:00, SOMArts day-long 8 hours); two of those refuse twelve
hours in the same line. No room publishes an operator-stated 09:00–21:00 interval, so the city
still records zero full windows.

## 2. Inference (labelled in the store, not presented as sourced)

- Precision tiers are a judgement from the returned match, not an operator statement; the
  evidence string for each row says exactly what was matched.
- "Room view" for the Ruth Williams gallery is inferred from the rentals-page image group,
  because the filenames carry no room label.
- Summer Break is derived from the last and first instructional days of two calendars and is
  marked `derived`.
- The municipal 2027 layer is absent because no 2027 list is published, not because nothing
  applies; the gap says so.

## 3. Conflicts recorded, not resolved

- 1345 Bush Street: Nominatim returns postcode 94164, the operator prints 94109.
- 3108 Fillmore: the matched POI is a different business ("Fawn"); unit B exists only in the
  owner's record.
- State 2027: statute text blocked (HTTP 403), so the 18 dates were cross-checked against the
  San Francisco Superior Court 2027 closure list and each row carries its Government Code
  subdivision locator from the pinned registry. The court prints Farmworkers Day on 9 April
  rather than 31 March, Juneteenth on 18 June rather than 19 June, and Christmas/New Year on
  24/31 December rather than 25 December/1 January 2028; it prints no Lunar New Year, Genocide
  Remembrance, Admission Day or Columbus Day closure. All 15 court closures are reconciled
  row by row in the coverage entry, and the six without an exact statutory row are stored.
- DGS's own 2027 state list (OAH page, marked "tentative") carries 11 dates, including
  Thanksgiving 25 November and Day After Thanksgiving 26 November; the OHR page publishes the
  2026 schedule only. Both are recorded; neither is treated as the other.
- Two legacy access fields contradicted the operator pages (Alliance Française four-hour cap
  and `cannot_to_5`; Root Division's 5.5-hour "cap") and were corrected with locators.

## 4. Uncertainty and open items

- CounterPulse rate-limited the run (HTTP 429 on its calendar and photo page); its windows
  remain unknown and it keeps one verified room image.
- AI Tinkerers' national roster is 403; its SF chapter page was read and prints 2026 dates.
- The only 07:00–24:00 clock in the city is the Peerspace bookable-hours widget on Common
  Space; it is recorded and refused as an operator-published interval.
- No Luma organiser page printing 2027 dates was found for any of the six themes.

## 5. Gates

- `city_store.py --check` passes; `build_ranking(store, 2026-11-26)` returns 14 rows + 2 leads
  = 16 ids identical to the store; the store renders in strict revision-1 mode to
  `scratch-render.html` (not a published page).
- Whole-store loss check against the HEAD pre-image: no unexplained claim id. The 9 replaced
  event-evidence claim ids are retained under `events.<id>.history.evidence`; the 6 RSA claims
  and the withdrawn AFSF access blocker (`cl-a3f0b7215cf1`) are dispositioned in
  `runs[run-20261126-sf-r1-refresh].retired_claims`.
- Access blockers are derived from `fields.programme_windows.value["8"].state`, so a blocker
  only exists when the resolved field says an 8-hour programme cannot fit; no venue now
  qualifies, and the stale "4 hour cap" sentence is gone from the render.
- Counts and hashes: `report.json`; machine detail: `fix2/gates.json` and `fix2/round2-log.json`.
