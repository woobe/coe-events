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
