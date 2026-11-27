# Bangkok BKK1 — research log (2026-11-25)

Store: `research/bangkok/city/city.json` — schema `city-store/1`, 44 records
(30 assessed rooms + 14 leads), 3 events, 6 communities, 20 holiday rows,
2 coverage rows, 75 photo rows (64 live: 58 on 29 assessed rooms and 6 shared by four leads; 11 explicit
withheld). Run `run-20261125-bkk-b1`, pinned `2026-11-25T05:00:00Z`.
SHA-256 `e36474bfa4d1ad6945da8cc488cda66945891b0b0e5420083db154443b84ebee`
(1,672,044 bytes, rebuilt twice, byte-identical). `city_store.py --check`
passes. There is no prior Bangkok research, so no legacy dispositions exist.

## Method and evidence rule

Every venue claim carries a quote re-derived at build time from a text capture
in `captures/` plus a line locator; `bkk_build.py` refuses the build when the
needle (capacity figure, price string, clock interval or address) is absent from
the cited lines. Where a capture can re-flow (the True Digital Park PDF), the
spec asks the builder to locate the line by the value itself (`lines="auto"`),
so a shifted text layer cannot silently point a citation at a line that does not
contain the value — that happened once during this run and the checker caught it.
`capture-manifest.json` pins all 88 captures with URL, status, HTTP title,
retrieval date and SHA-256. Nothing is fetched at build time, so a replay is
byte-stable.

Locator convention: line numbers are Python `str.splitlines()` indexes over the
stored text capture. On a PDF whose text layer contains form-feed page breaks,
`grep -n`/`awk` see a different offset (the True Digital Park PDF is 12 lines
adrift); the log and store always use the `splitlines()` convention so the
cited line contains the quoted value.

One extraction caveat: the Bank of Thailand PDF's text layer encodes the Thai
vowel mark U+0E4C as U+F70E in two words (`อาทิตย์`, `กุมภาพันธ์`). The stored
quotes carry that byte; the gloss gives the intended reading.

## Assessed rooms (30)

Capacity basis: **theatre** 20, **venue_max** 5, **seated** 4, **standing** 1.
No room is claimed as a confirmed seated 50 unless its basis is `seated`; every
theatre / venue_max / standing row carries a capacity blocker.

- **Bangkok Marriott Marquis Queen's Park** (`marriott.com/.../bkkqp/events`):
  feet and metre capacity charts, 39 rows each. Thai Chitlada 1 504 theatre /
  300 banquet; Thai Chakkraphat 1 80 / 60; Thai Boromphimarn 1+2 80 / 60;
  The Pavilion 1+2 100 / 80; Plum Blossom 120 theatre / 90 schoolroom.
- **Anantara Siam** (`anantara.com/en/siam-bangkok/meetings`): 17-room seating
  chart. Siam Ballroom 700 theatre / 320 classroom; Montathip 1 144 / 84;
  Pimarnman 220 / 120. The page's own counters conflict: "Max Capacity (Pax)
  700", the ballroom card's cocktail 700 and the body copy "up to 1,000 guests"
  / "over 800 delegates" — the chart figure is used and the copy is recorded as
  a conflict.
- **Mandarin Oriental Bangkok** (`mandarinoriental.com/.../meet`): eight space
  cards with "Up to N Guests" and no layout column. Royal Ballroom 800,
  Authors' Lounge 200, Sala Rim Naam 200, Regency Room 100 — every one is a
  `venue_max` basis.
- **QSNCC** (level 1 and level 2 tables): Plenary Hall 1 808 theatre / 570
  classroom; Ballroom 1 870 / 600; Ballroom 2 1,044 / 720; Meeting Room 204
  exactly 50 theatre / 33 classroom.
- **True Digital Park event space** (2025 rate sheet, 24 pages): Grand Hall
  476 theatre (650 with extra rows) / 320 banquet at THB 350,000; two halls
  330/320 at THB 280,000; one hall 146/136/132 at THB 200,000; Training Room 1
  88 theatre at THB 35,000; Training Room 3 170 at THB 46,000; Classroom 7 148
  at THB 46,000.
- **Lido Connect** (Thai rate card): Hall 1 140 seats at THB 40,000 per 4 hours;
  Hall 2 300 seats / 600 standing at THB 160,000 per 24 hours; Hall 3 250 / 450
  at the same 24-hour rate. Air-conditioning is printed as 8 hours.
- **River City Bangkok**: RCB Forum, 120 sq m, 100-seat auditorium.
- **BITEC**: SAMA Garden Event Space, 500 sq m, 300 standing.
- **IMPACT**: Banquet Halls 101-102 at 5,681 sq m with theatre 6,076 and, in the
  same page's introduction, "seat up to 3,600 attendees"; Phoenix Function Rooms
  1,126 sq m with a theatre range of 132-1,104.
- **Hyatt Regency Bangkok Sukhumvit**: the fact sheet prints 1,359 sq m of event
  space "accommodating up to 850 guests" and a pillarless ballroom, with no
  room-level chart — the 850 covers the whole floor.

Programme windows, stated only from a published clock:

- **12-hour yes (3)**: TDPK Grand Hall in all three configurations. The rate
  table prints `Rate: 350,000 THB / Day (09:00-21.00)` and `Event day operating
  hours: 8 AM - 9 PM. The room can be used at no additional cost during this
  period.`
- **12-hour no (4)**: TDPK Training Room 1, Training Room 3 and Classroom 7
  (their published full day ends at 18:00), and RCB Forum (the centre prints
  `OPEN DAILY 10.00 AM - 8.00 PM`, so neither a 09:00 start nor a 21:00 finish
  is available).
- **8-hour yes (6)**: the three Grand Hall configurations plus the three TDPK
  workshop rooms (full day 09:00-18:00 covers 09:00-17:00).
- **8-hour no (1)**: RCB Forum, for the same 10:00 opening.
- **Unknown (23 of 30 and 23 of 30)**: every hotel and convention room, and the
  three Lido halls, whose rate is sold as 4-hour or 24-hour hire with an 8-hour
  air-conditioning allowance but no published clock interval.

Costs (THB at the dated cross, USD 1 = THB 33.93 on 2026-11-24):

- Grand Hall 3 halls THB 350,000 → USD 10,315.36; 2 halls THB 280,000 →
  8,252.28; 1 hall THB 200,000 → 5,894.49; Training Room 1 THB 35,000 →
  1,031.54; Training Room 3 and Classroom 7 THB 46,000 → 1,355.73.
- Lido Hall 1 THB 40,000 per 4 hours → USD 1,178.90 (unit rate only; no window
  is established, so no programme cost is claimed); Halls 2 and 3 THB 160,000
  per 24 hours → USD 4,715.59.
- Twenty-one of 30 rooms publish no rate, so no programme cost is claimed for
  them. Every TDPK figure excludes 7% VAT as printed.
- Three budget exceptions use the New York shape, all True Digital Park: the
  three-hall Grand Hall at USD 10,315.36, the two-hall at 8,252.28 and the
  single hall at 5,894.49, each naming what the rate includes and that
  catering, staffing, cleaning and VAT are unknown extras. Only the three-hall
  rate prints an AV/facilities list (LED screen, microphones, camera, lighting
  and sound, stage, VIP and organiser rooms); the separate-hall table carries no
  AV row, so the two-hall and one-hall exceptions state that AV is unconfirmed
  for those configurations.

Coordinates: 25 of 30 assessed rooms carry numeric latitude/longitude derived
from a verified address claim, across eight buildings (Marriott, Anantara,
Mandarin Oriental, QSNCC, True Digital Park, River City, BITEC, Hyatt Regency).
Five rooms have no pin: the three Lido halls (Nominatim returned no match for
either the address or the venue-name query, recorded as `none`) and the two
IMPACT rooms (the only address the operator prints is the Bangkok Land office
tower at 47/569-576 Popular 3 Road, not the hall, so no address claim exists to
derive from). TruDigital Park and Mandarin Oriental resolve to a site polygon,
not a building; both are labelled `site`.

## Platform lanes

- **Peerspace**: `/venues/bangkok--th/` and `/venues/bangkok` both returned 403.
  **Blocked, not empty**; no count.
- **Tagvenue**: `/city/bangkok` and `/th/bangkok/` both 404; the site's own
  market list has no Thailand. **Empty by design**.
- **Eventective**: `/bangkok-thailand/` and `/thailand/bangkok/` both 404.
  **Empty** at both paths.
- **Venue Report**: `/venues/bangkok/` returned 403. **Blocked, no count**.
- **Spacebase** (extra lane): index prints `14 spaces in this area` and
  `Browse 14+ Meeting Rooms for hire in Bangkok`; no capacity or rate on the
  index, detail needs JavaScript → **count only, zero assessed**.
- **Event Banana** (extra lane): one HUBBA Sathorn listing read, no capacity or
  event rate → **one lead, zero assessed**.

## Event lanes and the 2027 list

The mandatory sources were **checked on 2026-11-25 but not all read through their
payloads**. MiraGather's three views returned HTTP 200 with 47-byte JavaScript
shells (0 pages read); the Luma Decentralized AI past tab is an 807-byte shell of
empty month bullets (0 pages read); AI Tinkerers lists Bangkok in its city
directory (line 378) but serves no dated 2027 chapter. The Luma **organiser**
pass adds `lu.ma/gaea` (read: three Bangkok cards — Before The Bell brunch, Good
Job! Bangkok job fair, Trading the AI Era — none prints a 2027 date),
`lu.ma/gaeaventures` (748-byte shell) and `lu.ma/money2020` (its only dated event
is 19-21 October 2027, Las Vegas). Luma's Bangkok city page shows undated cards
(three gave community leads); Eventbrite Bangkok is 2026 apart from a 2027
Thailand Tourism Forum card at The Athenee Hotel, which is excluded as not a
tech or AI event; Meetup's Bangkok AI results are November-December 2026.

Three 2027 events are stored, each with a capture that prints the dates:

1. **Money20/20 Asia 2027**, 27-29 April, Queen Sirikit National Convention
   Center — the organiser page's own header. Organiser is an **inference from the
   event brand**; the page prints no legal entity.
2. **Techsauce Global Summit 2027**, 25-27 August, QSNCC — the summit header
   prints the 2027 dates while the body still shows 2026 stages; the organiser
   line "Techsauce Media Co., Ltd." is printed on the same page (1 of 3 events has
   printed organiser evidence).
3. **SHE IS AI — AMPLIFY '27**, 23-25 September, Bangkok, venue unnamed —
   stored **provisional** because the page's own FAQ says dates and venue are
   still being confirmed; organiser is an inference from the brand.

Named-circuit dispositions: **Thailand Crypto Expo** — the domain did not resolve
on 2026-11-25 (0 pages read), so no edition, 2022 or 2027, is asserted from that
lane; **SEA Blockchain Week** — the domain did not resolve (0 pages read), so no
2027 Bangkok edition is claimed; **AI Summit Bangkok** — `aisummitbangkok.com`
returned HTTP 404 with a 107-byte body (0 pages read) and no 2027 Bangkok edition
is published under that name. The Malaysian circuit is carried by reference, not
re-derived: Malaysia Technology Expo 2027 (8-10 April), AIMY (24 March), InnoAI
Summit (22-23 April), CETA (28-29 April), DCCI (4-5 May) and AiSEAN (10-11 June)
are the Kuala Lumpur store's verified rows and are not restated as Bangkok
events.

## Holidays

Twenty rows in two layers, labelled for what the source actually is. Eighteen
come from the shared registry's Thai 2027 scope, read from Bank of Thailand
notice 37/2569 (Royal Gazette vol. 143, special part 202 Ngor, 25 August 2026):
New Year, Makha Bucha substitute (22 February), Chakri Day, **Songkran 13-15
April**, Labour Day substitute, Coronation Day, Visakha Bucha, Queen Suthida's
birthday, Asalha Puja substitute, King's birthday, Queen Sirikit's birthday,
King Bhumibol Memorial Day, Chulalongkorn Day substitute, National Day
substitute, Constitution Day and New Year's Eve. That notice is the
**financial-institution closure list** under the Financial Institution Business
Act, not the Cabinet public-holiday calendar; every row and both coverage rows
carry `authority_scope: financial_institution_closure` and an
`authority_label` saying so. `kind` stays `public_holiday` because that is the
store's calendar bucket (the page counts these closures); the authority fields,
not the bucket name, carry the scope.

The Cabinet's official 2027 public-holiday calendar is recorded as **pending,
not settled**: the Cabinet Secretariat page returned 403 to the research user
agent (0 pages read) and its indexed holiday page is the 2569 list, so no
Cabinet public-holiday date is stored. Two derived rows add the **actual lunar
observance days** (Makha Bucha 21 February and Asalha Puja 18 July) because the
notice only closes the substitute and names the actual day inside a
parenthetical; both are marked `subject_to_announcement`.

Coverage: `TH` (national) and `TH:bangkok` (host). Bangkok has no separate
public holiday, so the host row carries the national list rather than inventing
a city-specific one. **Royal Ploughing Ceremony** is `pending` in the supplement
— the Bank of Thailand list omits it because banks stay open, and no 2027 date
is published, so no date is stored. The notice's **Eid al-Fitr and Eid al-Adha**
closures apply only to the Islamic Bank of Thailand and to branches in
Narathiwat, Pattani, Yala, Satun and Songkhla, follow the Chularatchamontri
announcement and are recorded as `pending`, not as Bangkok-wide rows.

Note on the acceptance list: item 5 says "Malaysian holidays dated". This card's
own Bangkok instruction says to source **Thai** 2027 holidays, and a Malaysian
holiday layer would not apply to a Bangkok venue. The Thai authority was used;
the discrepancy is flagged rather than silently satisfied.

## Law

- **Alcohol:** Excise Department licence under the Liquor Act B.E. 2493, plus
  the Alcoholic Beverage Control Act 2008 (read through a law-firm summary; the
  statute text was not retrieved and the summary's sale-hour sentence is garbled
  in transcription, so no hour window is asserted). Per room: **unknown on all
  30**, each with the licence basis stated. The Marriott carry a note that its
  capacity chart includes ABar, a bar room, which proves alcohol is served on
  the premises and nothing about a closed 50-person event. No venue was
  contacted and no hotel licence is assumed to cover an external event.
- **Language:** Thai claims are quoted in the original script. All **six distinct
  Thai quotes** in the venue records now carry a `translation_review` — the
  Hall 1, 2 and 3 size/seat/rate blocks and the three separate rate lines — and
  the Thai hall names `ลิโด้ ฮอลล์ 1/2/3` are kept in each venue's `names_seen`.
  The 20 holiday rows and the `local_requirements.language` quote carry their own
  reviewed glosses. No statutory language duty is asserted for a private event;
  every `language_support` row is a checked unknown.
- **Food:** **not checked.** No Thai food-safety authority was retrieved; the
  `food` block records that state, and catering, food_service and
  delivery_allowed stay unknown on every room.

## Photos

Wikimedia Commons only; no operator gallery with a stated licence was
extracted. Twenty distinct files verified with a real GET (status 200, image
content type, byte count, SHA-256) and reused as building views across the rooms
in the same building: 58 live rows on 29 assessed rooms plus 6 on four leads. One assessed room
(Hyatt Regency) has **no** usable image and carries an explicit withheld row;
ten leads also carry withheld rows. The required split across the 30 assessed
rooms is **29 with 1+ live image, 0 with 4+, 1 with none** (Hyatt Regency); the
4-up target is missed at every assessed room and that is declared as an
exception, not smoothed over. Licence mix of the loaded rows: CC BY-SA 4.0
43, CC BY-SA 3.0 10, CC BY 4.0 9, CC BY 3.0 2. Rejected: nine Four Seasons
photographs of the same Ratchadamri compound (a different hotel identity), and
scanned books/PDFs that the Commons search returned as false hits. The single
Lido file is a 2007 photograph of the cinema building before its conversion and
is labelled as a building view, not a hall view.

## Conflicts and failures kept

- Anantara's own page prints three different capacity statements for the
  ballroom (700 max, 700 cocktail, "up to 1,000 guests").
- IMPACT prints "seat up to 3,600 attendees" and a 6,076 theatre row on the
  same page.
- The TDPK 2024 sheet prices the Grand Hall "9 am - 9 pm" where the 2025 sheet
  prices "09:00-21.00" and prints 8 AM - 9 PM operating hours; the 2025 edition
  is used and the difference is recorded.
- QSNCC MR 204 is exactly 50 theatre, so a seated 50 with a stage does not fit
  comfortably — carried as a capacity blocker and a question.
- Blocked or dead leads: Samyan Mitrtown Hall (no capacity captured), HUBBA
  Sathorn (no capacity), The Work Loft (max 30), River City Artery and Rooftop
  (no capacity), BITEC Live (7,000-10,000, far above brief), IMPACT Arena and
  the Exhibition Center halls (no capacity captured), Warehouse 30 (hours
  only), The Jam Factory (domain did not resolve), WeLearn (no venue), Lido
  outdoor space (no capacity), MO Embassy Room and Marriott Thai Boromphimarn 1
  (below/borderline the brief).

## Declared gaps

1. Programme windows: 23 of 30 rooms are unknown for both windows. Only TDPK
   publishes a priced clock, and only River City publishes hours that rule the
   brief out. This is the main gap.
2. Prices: 21 of 30 rooms publish no rate, and no all-in quote exists anywhere;
   tax, service charge, staffing and F&B are unquantified even on the priced
   rooms. Every TDPK figure excludes 7% VAT by its own line.
3. Seated capacity: only 4 rooms publish a seat count; 26 are theatre,
   venue_max or standing figures, so "plausibly serves 50" is not "confirmed
   seated 50".
4. Photos: one assessed room has no image and no assessed room reaches the 4-up
   target (29 at 1+, 0 at 4+, 1 at none); all cleared images are Commons
   building shots, and no operator room gallery cleared rights.
5. Access and climate: transit, monsoon/heat exposure, alcohol model, food
   service and delivery are unknown on 27-30 rooms. No 21:00 BTS/MRT service
   statement was found.
6. Food: no Thai food-safety authority was retrieved; the food block is
   explicitly `not_checked`.
7. Holidays: the layer is the Bank of Thailand financial-institution closure
   list; the Cabinet public-holiday calendar, Royal Ploughing Ceremony and the
   Islamic closures remain pending, and the two actual lunar observance rows
   are derived from a parenthetical.
8. Events: three 2027 events are stored, but only Techsauce prints a legal
   organiser (Money20/20 and SHE IS AI are brand inferences); the named circuit
   (Thailand Crypto Expo, SEA Blockchain Week, AI Summit Bangkok) has no 2027
   evidence, and the mandatory MiraGather and Decentralized AI lanes returned
   shells (0 pages read), so the event sweep is incomplete rather than
   exhaustive.
9. Communities: six listing-derived leads, no member counts except two Meetup
   attendee figures, no dated 2027 activity — below the page's 15-18 target.
10. No venue was contacted and no visit was made; `visits` stays empty.

## Suite result

`plan-event` suite, run at the end of this pass: **1,558 passed, 0 failed**
(`../.venv/bin/python -m pytest tests -q --basetemp=...`, 671.54 s). The three
stale-pin failures reported earlier (`test_home_page_facts`,
`test_summary_r2_entry::test_pinned_published_artifacts_still_match_baseline`,
`test_generate_luma_pack_cli::test_internal_notes_owner_only_and_public_files_0644`)
no longer reproduce: they were repaired by the separate card after the manager
waived AC8 for this one. AC8 was waived, but the live suite is green anyway.
The suite needs `--basetemp` here: without it every tmpdir fixture errors on this
container's scratch symlink.

## Ceiling measurement

The metric is non-blank hand-written tooling lines in `build/`: `bkk_build.py`
716, `bkk_fetch.py` 128, `bkk_geocode.py` 122, `bkk_photos.py` 85,
`bkk_photos_verify.py` 112, `audit.py` 35 — **1,198 non-blank**. Excluded as
sourced data, not tooling: `bkk_venues.py` and `bkk_other.py`, which hold the
facts, quotes, source ledger and holiday authority labels, plus every capture,
manifest, geocode and photo record. The manager amended the card ceiling to
**1,200** on 2026-11-25 (from 600), so the build is 2 lines under the amended
ceiling. `bkk_fetch.py` was written by the crashed first attempt and kept because
it is the hashing harness the captures are pinned with.

## R5 revision 1 (2026-11-26)

Store: `research/bangkok/city/city.json`, `refresh_revision: 1`, run
`run-20261126-bkk-r5`, pinned `2026-11-26T09:00:00Z`.
SHA-256 `0151c699312a619b53afa8d6d747920508a11e429239897f2c10a02a930123e9`
(1,705,056 bytes; rebuilt twice from `city.pre-r5.json`, byte-identical).
`city_store.py --check` passes (44 venues). The city-agnostic citation gate
(`kuala-lumpur/city/build/citation_gate.py`) reports **1,061 claims / 807
locators / 0 errors**. `build_ranking(store, "2026-11-26")` returns 30 open
rows + 14 leads = **44**, 29 `can_host` / 1 `cannot_host` (River City RCB Forum).
The revision-1 render to scratch produced 44 venue IDs and was then deleted.

### Addresses and coordinates (44/44 pinned)

Every address was re-read against its operator capture on 2026-11-26 and every
record was geocoded afresh through Nominatim (curl, browser UA; the Python UA
was refused 403). Tiers: **13 exact_venue, 23 building, 1 street, 7 area;
0 unresolved**. `exact_venue` marks only the venue's own mapped object (QSNCC,
BITEC, Lido Connect, Samyan Mitrtown Hall, Warehouse 30, IMPACT Arena), never a
room door. The 19 records that had no pin now carry: 8 exact_venue (Samyan,
BITEC Live, four Lido rooms, Warehouse 30, IMPACT Arena), 9 building (IMPACT
Phoenix, IMPACT Exhibition Center, three River City rooms, the Marriott lead,
IMPACT Banquet Halls, The Work Loft, The Jam Factory, MO Embassy Room), 1 area
(WeLearn) and 1 street (HUBBA Sathorn).

Failures kept: Nominatim has no `16 Phraya Phiren Alley` (WeLearn pinned to the
Thung Maha Mek khwaeng), no HUBBA building (street pin at 13.7165641,
100.5327225), no tower-level point for True Digital Park (six rooms on the
campus polygon), and no street number for the IMPACT halls (the operator prints
only the Bangkok Land Building head office). Address corrections: QSNCC
`60 Queen Sirikit National Convention Center` → `60 Ratchadaphisek Road`;
Lido kept in Thai with a reviewed English form; Jam Factory from a directory
page because the operator domain did not resolve.

### Photos (before → after)

Before: 75 rows, 64 live, 11 withheld; 33 venues 1+, **0 venues 4+**, 11 none;
rights CC BY-SA 4.0 43, CC BY-SA 3.0 10, CC BY 4.0 9, CC BY 3.0 2.
After: 114 rows, **108 live, 6 withheld; 38 venues 1+, 14 venues 4+, 6 none**;
rights CC BY-SA 4.0 65, CC BY-SA 3.0 21, CC BY 4.0 9, CC BY 3.0 8,
CC BY-SA 2.0 de 5. Split: **25 room/lobby views, 83 building/complex fallbacks**.
The cleared room views are Mandarin Oriental Royal Ballroom, Sala Rim Naam and
Authors' Lounge, plus River City's Artery and Auctions Room; every one is a
Commons file with a stated licence and a title/description placing it at the
venue (GPS distance recorded where a geotag exists). No operator room gallery
with a stated licence was found; the six venues with nothing carry an explicit
withheld record. The card's premise that eight venues already had 4+ was wrong:
the measured pre-refresh count was zero.

### Holidays (the Bank of Thailand layer is gone)

20 Bank of Thailand financial-institution rows removed. New store: **21
government public-holiday rows + 2 BMA school rows**, 3 coverage rows.
Government authority: HM Prime Minister's Office announcement B.E. 2562
(Royal Gazette vol. 136, special part 135 Ngor, 27 May 2019), the standing
19-day annual list. The Cabinet resolution acknowledging the B.E. 2570 overview
had **not been issued** as at 2026-11-26 (verified against Thai PBS, thaidata
and jobtopgun, all read on 2026-11-26), so:
- the 12 fixed-date rows are read from the standing announcement;
- the 4 lunar rows (Makha Bucha 21 Feb, Visakha Bucha 20 May, Asalha Bucha
  18 Jul, Khao Phansa 19 Jul) are rule-derived and flagged
  `subject_to_announcement: true`;
- the 3 substitute rows (22 Feb, 25 Oct, 6 Dec) are rule-derived,
  `verified: false`, and explicitly not read from a 2570 table;
- no Asalha substitute is stored: 18 July is a Sunday and 19 July is Khao
  Phansa, and Thai PBS prints three government substitutes for 2570, so the
  Asalha substitute stays unresolved (declared);
- Royal Ploughing Ceremony has no row (Royal Household Bureau sets it yearly);
- Islamic closures are not Bangkok-wide rows.
BMA local scope: the BMA portal returned a Cloudflare 403, so no municipal-only
2027 closure is stored; the host coverage row says the national list applies.
School: two 2027 term-break rows derived from the Ministry of Education
school-year regulation B.E. 2549 clauses 6-7 (summer break 2 Apr-16 May,
between-semester break 12-31 Oct). The BMA Department of Education order for
academic year 2569 was not retrievable (403); no private or international
school calendar was substituted. Weekdays are recomputed in code. Comparison
layers (US/UK/CA/DE/IE) are rendered separately from the registry and carry no
Bangkok rows. 2027 coverage is stated; 2028 is not attested.

### Events (54-cell matrix)

The matrix is `event-matrix-r5.json`: 6 themes × 9 lanes, each cell with URL,
pages read, hits and disposition. `sources_consulted` dedupes to one row per
(lane, URL) and sums to 6 yields. Six 2027 events retained: Money20/20 Asia
(27-29 Apr, QSNCC), Techsauce Global Summit (25-27 Aug, QSNCC), SHE IS AI
AMPLIFY '27 (23-25 Sep, Bangkok, provisional), Southeast Asia AI Data Center
Supply Chain Summit (14-15 Jan, Bangkok Phra Nakhon, venue TBD), TECHSPO Bangkok
(17 Aug, Bangkok Nana, venue not printed) and ICBDA 2027 (26-29 Apr, Bangkok).
Drops: ICMLAS 2027 is online; SEA Blockchain Week's domain is parked with dates
TBA; Thailand Crypto Expo did not resolve; WASET ICBC returned 403. MiraGather's
three views and the Decentralized AI lane returned shells (0 pages read);
Luma's Thai alias returned Page Not Found.

### Access

**3 full / 3 floor-only / 1 shorter / 37 unknown**. Full: the three True Digital
Park Grand Hall configurations, re-derived from the rate line
`Rate: 350,000 THB / Day (09:00-21.00)` and `Event day operating hours: 8 AM -
9 PM`. Floor-only: TDPK Training Room 1, Training Room 3 and Classroom 7,
published `8 AM - 6 PM`. Shorter: River City RCB Forum, `10.00-20.00`, which
does not fit the 09:00 start. Every unknown has a null locator and an
absence note; no hotel banqueting prose was promoted to a window.

### Declared gaps and handoff notes

`declared_gaps` carries nine dated entries (coordinates ×2, photos, holidays ×2,
events, access, addresses, contact). Handoff to G / P5:

1. `city_page.PAGE_PROFILES["bangkok-th"]["holiday_caveat"]` still appends the
   frozen sentence “These rows are the Bank of Thailand financial-institution
   closure list…” in revision 1, although `city_calendar.layers_for` receives
   `revision` and the store's rows are the new government layer. The caveat also
   names only two lunar rows where the store has four. This is shared code; the
   R card did not patch it. Revision 1 should pass no frozen caveat and derive
   the note from `store["holidays"]`/`coverage`.
2. `PAGE_PROFILES["bangkok-th"]["declared_gaps"]` (`BKK_GAPS`) is unused for
   revision 1 (`_declared_gaps_section` reads the store), but the `gaps_note`
   says “eleven” while the store declares nine; check whether the rendered note
   should be store-derived too.
3. The render was a scratch smoke only; no page, summary, manifest or other
   city store was written.

Tooling added: `build/bkk_refresh_r5.py` (788 lines), `bkk_geocode_r1.py`,
`bkk_photos_r5.py`, `quote_check.py`, `loss_audit_r5.py`, `verify_r5.py`;
sidecars `coordinate-tiers.json`, `geocode-log-r5.json`, `geocode/<id>.json`,
`event-matrix-r5.json`, `photo-verify-r5.json`, `photo-summary-r5.json`,
`holiday-supplement.json`, `city.pre-r5.json`.

## R5 revision 1 — round 2 (2026-11-26)

Round 2 answers the two blocking review findings (shared-pin tiers, gap
arithmetic) and the photo split. It supersedes the tier, photo-split and
WeLearn paragraphs above.

Store: `research/bangkok/city/city.json`, `refresh_revision: 1`, run
`run-20261126-bkk-r5`, 44 venues, **1,715,972 bytes**, SHA-256
`6a96d253897a7167f91c89e5f80bcf258bd4bd70c1e1f9ff59deeba2525e72e1`. Rebuilt
six times from `city.pre-r5.json`; the last three builds are byte-identical
(`cmp`). `city_store.py --check`: **OK (44 venues)**. Citation gate
(`build/citation_gate.py`, reproduced here): **1,061 claims / 807 capture
locators / 0 hard errors**, and 0 direct-value flags once derived, parsed and
URL claims are excluded. `build_ranking(store, "2026-11-26")`:
30 open + 14 leads = **44**, 29 `can_host` / 1 `cannot_host`. Loss audit:
44 → 44 ids, 76 fields changed, 0 removed, 80 added, 0 venue/field losses.

### Coordinates (round 2)

Tiers now **3 exact_venue, 33 building, 2 street, 6 area; 0 unresolved**; the
counts sum to 44 record ids. Ten records that shared three venue/complex points
were moved from `exact_venue` to `building`, because one shared point cannot
claim a verified room entrance (Kuala Lumpur and Lisbon label the same room
groups `building`):

- Lido Connect ×4 on OSM node 11139443935 (`amenity=music_venue`) at
  13.7451699, 100.5324766;
- QSNCC Ballroom 1/2, Plenary Hall 1 and Meeting Room 204 on OSM way 1085353819
  (`amenity=conference_centre`) at 13.7242403, 100.558736;
- BITEC Live and SAMA Garden on OSM way 25621160
  (`amenity=exhibition_centre`) at 13.669801, 100.6085436.

Each moved claim keeps its own quote and now carries a `tier_note` naming the
shared OSM object and the room count. The three single-record `exact_venue` rows
were re-checked against the raw Nominatim payload and keep the tier, each with a
new `matched_object`: Samyan Mitrtown Hall (node 11323335134,
`amenity=conference_centre`), Warehouse 30 (way 491885323, `amenity=arts_centre`),
IMPACT Arena (way 151982343, `leisure=stadium`). The eight shared building points
are listed in `coordinate-tiers.json["shared_building_points"]`; the three
`exact_venue` points are single-record and are not in that list.

The 19 formerly pinless records now carry: **14 building, 3 exact_venue, 2
street, 0 unresolved**.

WeLearn was re-geocoded, and its pin improved from `area` to `street`. The
printed 「16 Phraya Phiren Alley」 and the alley-name spelling return empty
Nominatim result lists (both stored now as failed lookups), but 「Soi Phraya
Phiren」 returns OSM way 53271857 (`highway=residential`) at 13.7216901,
100.5513486, whose own address is the same subdistrict and postcode (Thung Maha
Mek, Sathon 10120). The pin is that street; house number 16 stays unmatched. The
The two empty attempts are recorded in `geocode/bkk-971b52de876f.json` with status
`none` and reason `no OSM match`, so `failed_lookups` is no longer empty. The
round-1 khwaeng attempt, which did match the subdistrict, is kept but relabelled
as a coarser object superseded by the street lookup rather than a failed query;
successful lookups that returned some other business are labelled
`returned 「X」, not the venue or its building`.

### Photos (round 2)

108 live rows resolve to **38 distinct images**; 6 withheld records. Of the 108
live rows, 83 are exterior/complex fallbacks and 25 are room-side: **4 own-room,
11 another room in the same hotel/complex, 5 hotel lobby, 5 building
circulation/entrance interiors**. Each live row now stores `room_scope` so the
split is machine-readable. Of the 14 venues at 4+, **11 have no photo of their
own room**: the four QSNCC rooms (which each carry the same four building
images), the two BITEC rooms, Samyan Mitrtown Hall, Warehouse 30, IMPACT Arena,
Regency Room and Embassy Room. The review and manager notes said nine; the
extra two are Regency Room and Embassy Room, which carry other Mandarin Oriental
rooms and the lobby but never their own room. The five cleared room files are
reused across records in one building, so they do not map one-to-one to the 25
room-side rows. Counts and rights mix are
unchanged from round 1 (38/14/6 venues; CC BY-SA 4.0 65, CC BY-SA 3.0 21,
CC BY 4.0 9, CC BY 3.0 8, CC BY-SA 2.0 de 5).

### Holidays and access (round 2)

The 20 Bank of Thailand rows are still absent; the layer is 21 government rows
(PM's Office announcement B.E. 2562) + 2 BMA school rows (MoE regulation B.E.
2549) + 3 coverage rows. The four rule-derived lunar rows now carry
`verified: false` like the three substitutes, all seven still
`subject_to_announcement: true`; weekdays were recomputed and match code. The
TDPK Grand Hall 8-hour basis no longer quotes the rate line for an operating-
hours claim: it reads 09:00-21.00 and 8 AM - 9 PM, and the three Grand Hall
access claims now store a `supporting_quotes` entry with
`capture tdpk-event-2025 line 100` (`Event day operating hours: 8 AM - 9 PM…`).
Access split unchanged: 3 full / 3 floor-only / 1 shorter / 37 unknown.

### Declared gaps and citation fixes (round 2)

The coordinate gap is now generated from the store's tier counts, so it reads
3/33/2/6 and sums to 44 (round 1 printed 14/23/1/7 = 45). Photo refs point at
`build/photo-verify-r5.json` and `photo-summary-r5.json`; the event gap refs
`event-matrix-r5.json`; the contact gap refs the new
`build/contact-log-r5.json`. The addresses gap records the WeLearn street result.

One inherited claim failed the value-carried test: the record named
「Banquet Halls 101-102」 while no captured or live operator line prints a
101-102 suffix. The display name is now 「Banquet Halls (IMPACT Forum Hall 4)」
(cited `capture impact-banquet-halls lines 60-61`) and the record label
`IMPACT — Banquet Halls`; `names_seen` keeps the historical string.

Round-2 tooling: `build/tiers_r2.py`, `build/fetch_welearn_r2.py`,
`build/citation_gate.py`, `build/r2_summary.py`, `build/photo_buckets.py`,
`build/contact-log-r5.json`. Scratch render: 590,375 bytes, 44 venue ids, 23
holiday rows, tier words matching 33/6/3/2, then deleted. No page, summary,
manifest or other city store was written.

Still open for G / P5 (unchanged): `city_page.PAGE_PROFILES["bangkok-th"]
["holiday_caveat"]` injects the frozen Bank of Thailand sentence in revision 1;
the store's rows are the government layer, so the caveat must be removed or
store-derived. The scratch render shows it above the new rows.

