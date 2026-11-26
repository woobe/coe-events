# Lisbon L1 — research log (2026-11-24, rev 2)

Store: `research/lisbon/city/city.json` — schema `city-store/1`, 51 records
(30 assessed rooms + 21 leads), 7 events, 12 communities, 14 holiday rows,
2 coverage rows, 78 photo rows. Run `run-20261124-lx-b1`, pinned
`2026-11-24T22:30:00Z`. SHA-256 `090a2a603e51bece4eb5d3cbac449a8d4640a7d5abbf6c37d6432f6f783ea9ab`
(rebuilt twice, byte-identical). `city_store.py --check` passes. All eight
2026-q4 records are dispositioned in `legacy-dispositions.json`.

Rev 2 applies the round-1 review: SBC Summit dropped for want of a source, the
event/platform lane ledger completed and reconciled, the price typo corrected,
Yorkseed's end-date line added, two lead capacities removed, five missing
geocode attempts recorded, and the counts in this log brought back in line with
the shipped archive.

## Method and evidence rule

Every venue claim carries a quote re-derived at build time from a text capture
in `captures/` and a line locator. `lx_build.py` refuses a build when the quote
range does not contain the claimed capacity figure, so a keyword match cannot
stand in for a locator. `capture-manifest.json` pins 113 captures with their
SHA-256; 63 returned content and the other 50 are recorded 403/404/refused/DNS
failures with a 0-byte body. The manifest has no separate render flag: seven
venue pages are JavaScript shells whose readable text came from the rendered
capture, and the capture itself is the record.

## Assessed rooms (30)

Seated basis 23, venue-claim maximum 6, standing-only 1. Five rows publish a
numeric rate (Heden, all inc. IVA); the other 25 carry a price blocker.

- Heden: King's Room 50 · €300/h; Classic Auditorium 50 · €175/h; Open
  Auditorium 75 seated · €300/h; Theatre Staircase 50 · €140/h; Full Floor 200 ·
  €300/h. Source `heden.co/event-spaces/`, lines 82 and 89–140.
- Lisbon Marriott: The Garage 700, New York 430, Broadway 180, Manhattan 180,
  Berlin 180, Berlin A 70, Berlin B 70, Geneva 70, Los Angeles 90 —
  theatre/banquet columns of the hotel's own capacity chart, lines 198–296.
- MAAT: Generator 160 seated, Condenser 80 seated, Boiler 100 standing.
  The Boiler is the only room with a printed access rule: after 19:00 and
  Tuesdays, so both programme windows are **no**.
- Convento do Beato: Cloister 1,000 seated, Dining Room 250, Library 280,
  Upper Foyer 240, Chapter Hall 90 (standing and audience columns also read).
- Pestana Palace: Belém 480 theatre, Belém I 220, Ajuda 200, Ajuda I 80, from
  the hotel booking engine's capacity table (the hotel's own meetings page
  prints no table).
- Gulbenkian: Sala 1 120 theatre, Sala 2 80 theatre (Portuguese page, glossed).
- Avila Spaces: Blue Ocean Auditorium 50 (venue claim), Avila Café 60 (claim).

Programme windows: 29 rooms **unknown** (no published 09:00–21:00 or 09:00–17:00
interval anywhere), 1 room **no**. There is no `yes` row: an hourly rate is not
a booked interval, and a museum's public visiting hours are not a private-event
licence. Numeric USD comparators exist for five rooms at eight billed hours
(€140–300/h × 8 × 1.0963 = $1,228–$2,631); no programme cost is claimed while
the window is unknown. No assessed room publishes a total above USD 5,000, so
no budget exception row exists — the unknown-priced 25 may of course exceed it.

Coordinates: 25 of 30 assessed rooms carry numeric latitude/longitude derived
from a verified street-address claim. The five Heden rooms do not: their
operator page prints only a district ("Rossio, Lisbon", "Santa Apolónia,
Lisbon", "Alvalade, Lisbon"). Those five failed/absent lookups are now recorded
in `geocode-log.json` with `match: "no_address"` — no pin is guessed.

## Platform lanes

- Peerspace: direct 403; provider search returned Berlin/Barcelona/Madrid only.
  **Empty lane**: no Lisbon inventory found, not a claim that none exists.
- Tagvenue: `/venues/lisbon` 404; provider search returned London inventory
  only. **Empty lane**.
- Eventective: Portugal path 404; all results were Lisbon, Ohio/Iowa/Maine.
  **Empty lane** (no Portugal inventory surfaced).
- The Venue Report: direct page 403 and **not captured**, so no result count is
  claimed. A provider read surfaced four Lisbon venue names (Heden Santa
  Apolónia, Garden of Heden Tent, UNOBVIOUS Lab, Cantina LX), kept as leads
  only; listing averages are not operator terms. The earlier "139 results"
  figure came from the provider summary and is withdrawn.
- Eventflare (308+ Lisbon venues per the page title) and Lisbon Venues
  (CCL/FIL operator group, home + `/espacos/`) were read as discovery indexes;
  neither is used as a claim source. Lisbon Venues names two venue groups at
  complex level only, so CCL and FIL stay leads.

Every platform lane has a `sources_consulted` row with `pages_read`, `hits`,
`dedupe` and `disposition`; an empty lane is shown as an empty search.

## Event lanes

Eleven event-lane rows are stored. Their `event_yield` sums to **7**, the number
of stored events: websummit.com 1, portugaltechweek.com 1, lisbonaisummit.com 1,
luma.com/devcon 1, buildingthefuture.pt 1, luma.com/lisbondelegation 1,
and eventbrite 1 (38 event cards read, of which one distinct 2027 event —
Tech Hiring, 4 March). The zero-yield rows and why:

- Luma city page (`luma.com/discover/lisbon/tech`): 13 cards, mostly 2026
  editions; it yields community rows and venue tags, not a stored 2027 event.
- Meetup Lisbon technology search: 11 result cards, all dated November–December
  2026 (two are Bucharest/Kraków, one event is listed twice by two organisers);
  no 2027-dated Lisbon event. Logged as empty for this purpose.
- Yogonet (SBC): read through the provider on 2026-11-24. No captured page
  prints 21–23 September 2027 and the `sbcnews.co.uk` organiser page returned
  404 (0 bytes), so **SBC Summit Lisbon 2027 was dropped** rather than stored
  without a locator. The earlier trade-press summary is withdrawn.

The five mandatory sources were read through their payloads on 2026-11-24.
MiraGather's three views are 47-byte JavaScript shells and yielded nothing;
AI Tinkerers lists 281 cities with a Lisbon chapter but no dated 2027 edition;
the Decentralized AI Days past tab is empty.

Portuguese circuit by name: Web Summit, Portugal Tech Week, SBC Summit (dropped,
see above), Building The Future, Devcon, Lisbon AI Summit, Yorkseed, Tech Hiring
Community Conference.

Seven 2027 events are stored, each with a capture that prints the dates:
Building The Future 25 Feb, Tech Hiring 4 Mar, Lisbon AI Summit 1 Jun (secondary
index, organiser inferred), Devcon 11–13 Oct, PTW 5–14 Nov, Web Summit 8–11 Nov,
Yorkseed 8–12 Nov. Two Luma listings (AI Builders 27 Jan, Fintech Pitch Party
10 Nov) were dropped because the captured page carries the day and month but
not the year; the Luma search snippet did, and a snippet is not a locator.

## Holidays

13 statutory days from Código do Trabalho art. 234.º n.º 1 (consolidated text,
updated 2026-10-13), with the 2027 dates derived (Easter 2027-03-28) and
cross-checked against a Portuguese calendar. Every row is marked `derived`.
One municipal row: 13 June 2027 (Sunday), Santo António, facultative under
art. 235.º; the Câmara Municipal de Lisboa page returned 403, so the date rests
on the secondary calendar plus the statutory rule, and that gap is recorded.
Two coverage rows (`PT`, `PT:lisbon`); the shared registry has no Portuguese
scope, so the rows live in a hashed supplement.

## Law

DL 10/2015 (comércio, serviços e restauração), read on PGDL:
- art. 23.º n.º 1 — alcohol sale/service must follow DL 50/2013; no permit is
  granted by this article.
- art. 26.º — public commercial information must be in Portuguese.
- art. 31.º — opening hours follow DL 48/96, so a 21:00 finish depends on the
  venue's licensed hours.
Each is stored with the Portuguese quote and a reviewed English gloss; each
stays `open_question` with the venue-level unknown named.

## Photos

9 venue records carry 4 verified Commons images each (MAAT 3 rooms, Pestana 4
rooms, Gulbenkian 2 rooms — 36 rows), all HTTP 200 with byte counts and
licence/attribution recorded. Licences: CC BY-SA 2.0 (25), CC BY-SA 4.0 (6),
CC BY 4.0 (3), CC BY 2.0 (2). 42 records are explicit withheld rows with a
reason: no Commons file depicts the Marriott, Convento do Beato, Heden or Avila
buildings, and no operator media-kit URL with a stated licence was extracted.
No placeholder, stock or look-alike image is used.

## Declared gaps

1. Programme windows: no Lisboa venue in scope publishes a 09:00–21:00 (or
   09:00–17:00) bookable interval. 29 of 30 rooms are unknown; this is the main
   evidence gap and the page must show it, not smooth it over.
2. Prices: 25 of 30 rooms publish no rate. Only Heden gives a numeric figure
   (hourly, inc. IVA). No all-in 8-hour or 12-hour total is evidenced anywhere.
3. Access and season: `transit_access`, `winter_access`, `alcohol_service` and
   `catering` are **unknown on 30/30 rooms**, and `access_window` is "Not
   published" on 30/30. No operator page states a metro/bus route, a 21:00
   service, summer heat exposure or a wet-weather plan. The page must present
   these as unknown rather than absent.
4. Pins: five Heden rooms have no coordinates because the operator publishes a
   district only; the five failed lookups are recorded with `match:
   "no_address"`. 25 of 30 assessed rooms have a numeric pin.
5. FIL, MEO Arena, CCL, LX Factory, Village Underground and Titanic could not be
   read (JS shell, connection reset/refused, DNS failure, parked domain). They
   are leads with the exact failure recorded, not silent omissions.
6. Corinthia publishes "16 meeting rooms / up to 1,400 delegates" in a PDF only;
   no room-level table was readable, so it stays a lead.
7. Hotels other than Marriott/Pestana (Four Seasons, InterContinental, EPIC SANA,
   Tivoli) returned 403/404/DNS failures and are not in this pass at all.
8. Universities: ISCTE, Católica, ULisboa and Nova SBE publish no external
   room-rental page that could be read, so none is assessed.
9. Lisbon's municipal holiday rests on a secondary calendar (CML 403).
10. Photos are building exteriors, not room interiors; every room gallery is the
    same building set for its venue. No operator room photo cleared rights.
11. Budget: no numeric total exists, so the over-budget shape is unused rather
    than populated with a guess.
12. SBC Summit 2027 was dropped: no capture prints its dates and the organiser
    page is a 404. It is not counted among the seven stored events.

## Ceiling measurement

The manager amended this card's ceiling to **1,100 changed lines** and asked for
the metric to be stated. The metric is **non-blank hand-written lines in the
build tooling**, measured over the eight tooling files under `build/`:
`lx_build.py` 553, `lx_fetch.py` 138, `lx_finalize_inputs.py` 64,
`lx_geocode.py` 87, `lx_links.py` 52, `lx_commons_search.py` 43,
`lx_photos.py` 77, `lx_photo_fix.py` 32 — **1,046 non-blank (1,154 raw)**.
Excluded as sourced data, not tooling: `lx_venues.py` (243) and `lx_other.py`
(223), which hold venue facts, event facts, quotes and the source ledger.
1,046 ≤ 1,100. The six one-off capture/geocode/photo utilities are deliberately
kept as separate scripts rather than folded into one: the amendment said not to
refactor for a number, and each utility documents one evidence pass.

## Revision 1 — R4 refresh (2026-11-26, `run-20261126-lx-rev1`)

Store: `research/lisbon/city/city.json` — `refresh_revision: 1`,
`updated_at 2026-11-26T12:00:00Z`, 2,000,360 bytes, SHA-256
`8a464a78e0771f93b47f90752caf98b97622c298e42ecb39075db3a75b310e21`.
`city_store.py --check` passes (51 venues). `build_ranking(store,
"2026-11-26")` returns 30 open rows (29 can host, 1 cannot), 20 leads and 1
closed row — 51 venues, no duplicate or missing id. `loss_check` against
`HEAD:research/lisbon/city/city.json` (`090a2a60…`) returns **none**. The
revision-1 strict render was written to a profile scratch path and deleted;
its SHA-256 was `eac869aaa1197752c316ac606bd74ef94d723647ad4f0969ab06f63e5cb7c3ba`
(1,685,892 bytes), 50 displayed rows (closed Musicbox not displayed), every
external anchor `target="_blank" rel="noopener noreferrer"`.

### Addresses and pins

All 51 records were re-read and geocoded afresh in 31 address groups. Provider:
Photon (OpenStreetMap data, komoot), one live query per group on 2026-11-26;
every failed query is retained in `geocode-log-rev1.json`. Coordinates are
JSON numbers; each claim carries provider, query, request URL, returned place,
match evidence, refused lookups and the address claim's capture/line.

Tier counts over 51: **exact_venue 9, building 32, street 10, area 0,
unresolved 0**. The 26 records that had no pair now resolve as:
**6 exact_venue** (MEO Arena, FIL, CCL, Coliseu, Museu do Oriente, Titanic),
**10 building** (Engineers Hub, The Block, Corinthia, IDEA, Village
Underground, Impact Hub, Musicbox, LX Factory, Heden King's Room, Heden Classic
Auditorium) and **10 street** (Nova SBE, Heden Full Floor and Theatre Staircase,
Lisbon Stage, Second Home, ULisboa, ISCTE, Católica, São Luiz, Heden Open
Auditorium).
No venue is pinned at a city centroid; street-tier `map_target` omits the
venue name.

Brand/branch decisions are recorded in `declared_gaps`: Heden's five rooms map
to Rossio, Santa Apolónia and Alvalade addresses from the operator FAQ; Impact
Hub is the Penha de França space, not Baixa Chiado; IDEA is the Saldanha space.
Postal conflicts are kept: CCL 1300-307 (OSM 1300-037), Impact Hub 1170-070
(OSM 1170-079), Musicbox three variants.

### Photos

Before: 9 venues with 1+ photos (9 with 4+), 42 with none; 36 live records,
all Commons building exteriors, no room view. After: **11 venues with 1+, 11
with 4+, 40 with none; 19 room-specific records across 7 venues** (MAAT ×3
rooms, Gulbenkian Sala 1 and Sala 2, Avila Blue Ocean and Avila Café) and 44
labelled fallback records (36 Commons exteriors, 8 shared venue images).
Twenty-seven records are operator gallery assets hotlinked with attribution;
the rest are the prior Commons licences (CC BY-SA 2.0 25, CC BY-SA 4.0 6,
CC BY 4.0 3, CC BY 2.0 2). Every live record has `view_kind`, dimensions,
rights, attribution, check date and placement proof; 27 operator images were
fetched and their dimensions re-checked on 2026-11-26. Commons records gained
distance where the file page publishes coordinates (144–249 m), and an explicit
“no camera coordinate, distance not asserted” note otherwise.

### Holidays

Public: 13 statutory rows (Código do Trabalho art. 234.º; dates derived with the
2027 computus, Easter 28 March 2027, cross-checked against the secondary 2027
table) and 1 municipal row (13 June 2027, Sunday; art. 235.º facultative).
CML's own page was blocked by a Cloudflare verification loop and DGERT's 2027
list returned a database error; both failures are dated gaps.

School: **3 rows from Despacho n.º 8368/2024 Anexo II only** — Carnival 8–10
February 2027 (Mon–Wed), Easter 22 March–2 April 2027 (Mon–Fri), Christmas
20–31 December 2027 (Mon–Fri). The Anexo II heading is quoted with each row.
Amendments checked: Despacho n.º 10430/2026 amended Anexo I only (21 September
2026 start for scientific-humanistic secondary). The earlier reference to
Despacho n.º 9989/2025 was dropped in round 2 because that text was not
captured; no uncaptured amendment is asserted. **Anexo IV** (private special education)
differs — Easter 25 March–2 April 2027, Christmas 20–24 December 2027 — and is
deliberately not applied to the public layer. Summer is not an Anexo II
interruption and is not invented. 2027 coverage is 1 January–31 December;
comparison-country rows: 0.

### Events

11 stored events, each with a capture printing 2027 dates and one ledger row
(`event_yield` sums to 11). New this revision: NFC Summit 27–29 May (Unicorn
Factory), DATA'27 23–24 March (Meliá Oriente), IDCC27 9–12 February (ISCTE),
SBC Summit 21–23 September (FIL, outside the six themes but retained as a major
dated venue event). **Devcon corrected**: the community Luma calendar printed
11–13 October; the organiser page `devcon.org/lisbon/` prints **12–14 October
2027 at CCL**, which now supersedes it. Yorkseed and PTW date quotes were
re-pinned to single capture lines.

The six-theme × nine-lane matrix is stored as 54 `event_matrix_cell` rows
(theme, lane, URL, pages read, hits, disposition). Luma city/alias pages were
JavaScript shells; Eventbrite theme pages produced NFC and IDCC27; Meetup showed
2026-dated events only; MiraGather and AI Tinkerers had no Lisbon 2027 entry.
Drops are recorded: AI-Lisbon-27 directory (HTTP 429), Mafra dinner (out of
locality), dōTERRA convention (out of theme), HiTech 2027 information session
(held December 2026), the online “AI Engineer in 2027” course (not a Lisbon
venue event).

### Access

Zero full 09:00–21:00 windows. 50 rows unknown after reading the operator
venue-hire page, FAQ and any bookable sub-page; 1 explicit **no** (MAAT Boiler
Room: after 19:00 only, closed Tuesdays); 1 closed row. No venue published a
noise curfew on the pages read, so no curfew is recorded as a cap. Office hours
and public museum hours were not treated as hire windows.

### Evidence and limits

`capture-manifest.json` now pins 244 captures (rev-1 pages included; DR pages
rendered with a 40 s virtual-time budget). `geocode-log-rev1.json`,
`photo-candidates-rev1.json`, `photo-enrichment-rev1.json` and
`holiday-supplement.json` are the sidecars; the supplement is city-relative and
re-hashed. Every address, event and school claim was re-checked to resolve to a
line carrying its value (`lx_verify2` pass, 0 numeric/locator errors). The 12
dated `declared_gaps` entries list the remaining limits, including the two
blocked holiday authorities, the ten street-tier groups, the photo shortfall,
and the parked Musicbox / DNS-failing Titanic operator sites.

## Round-2 corrections (2026-11-26)

Review round 1 accepted the store's structure, coordinates, ranker and render but
required six evidence fixes. All six are applied; the store digest moved from
`8a464a78…10e21` to `d9ab635a…dbae` (2,003,106 bytes).

1. **Public-holiday citation.** The 13 statutory rows and the public coverage row
   now cite the PGDL consolidated *Código do Trabalho* (Lei n.º 7/2009), art.
   234.º n.º 1, captured at `captures/rev1-pgdl-art234.txt` line 1371. The quote
   is the statute sentence itself, not the TogaAI footer; `derived: true` stays
   because the 2027 dates are computus-derived. Each row also carries `weekday`
   and `weekday_source`; the municipal row uses `captures/rev1-hol-municipal.txt`
   line 14 and adds art. 235.º n.º 1 (`rev1-pgdl-art235.txt` line 1366).
2. **Events re-sourced to organiser pages.** Lisbon AI Summit 2027 now cites
   `lisbonaisummit.com` (lines 2–3, 7, 11), where the organiser is AI Summits LTD
   UAB; Tech Hiring Community Conference 2027 now cites
   `landing.jobs/business-tech-hiring-community-conference-2027` (lines 45–47,
   footer line 249). The eventsindex and Eventbrite-directory ledger rows remain
   as history with `event_yield: 0`; two new organiser rows carry the credit, so
   the `kind: event` yield still sums to 11 for 11 events.
3. **Locators name their capture.** All 90 bare `line N` claims (180 field and
   history occurrences; 26 of them on URLs with more than one capture) now read
   `capture <slug> lines N`. Every rewritten locator was checked against the
   named capture: the quote sits on the named line. Zero bare locators remain.
4. **`source_edition` collapsed.** The 14 repeated `re-read 2026-11-26` strings
   are replaced by one dated statement per source.
5. **Statutory authority.** PGDL is cited in the rows and in the new
   `holiday-derivation` declared gap; no row cites TogaAI as the holiday
   authority. The two TogaAI law rows stay in `sources_consulted` only as the
   pages actually read on 2026-11-24, alongside the new PGDL rows.
6. **Despacho 9989/2025 dropped.** The uncaptured assertion was removed from
   the school rows and coverage; only the captured Despacho 10430/2026
   (Anexo I only) is asserted.

Access split reported correctly: 0 full / 0 floor-only / 0 shorter, 50 unknown
(including the 1 closed venue) and 1 explicit no (MAAT Boiler). `--check`
passes; `loss_check(pre, post)` is `{}`; `build_ranking(store, 2027-01-15)`
returns 30 open (29 can-host, 1 cannot-host) + 20 leads + 1 closed = 51 unique
IDs. Rendered once to a scratch path in revision-1 strict mode (1,688,147 bytes,
sha256 `7ffda028…44e8`, 50 venue rows, 371 external anchors all
`target="_blank"`), then deleted. No summary, home page, manifest or other city
store was written.
