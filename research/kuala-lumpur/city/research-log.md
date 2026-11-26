# Kuala Lumpur KL1 — research log (2026-11-25)

Store: `research/kuala-lumpur/city/city.json` — schema `city-store/1`, 55 records
(30 assessed rooms + 25 leads), 11 events, 15 communities, 21 holiday rows,
2 coverage rows, 82 photo rows (43 live on assessed rooms, 39 explicit withheld).
Run `run-20261125-kl-b1`, pinned `2026-11-25T04:00:00Z`.
SHA-256 `1efed6adcc8887b54c69507104f13034ca37b11bf1f39cbf1173be4916d8570c`
(1,794,841 bytes; rebuilt twice in place and twice out of tree, each pair
byte-identical, the two trees differing only in 4 absolute-path leaves).
`city_store.py --check` passes (55 venues) and `build/citation_gate.py` reports
1,064 claims / 865 locators / 0 errors. The `plan-event` suite runs
**1,558 passed / 0 failed in 86.71 s** (`TMPDIR` on a 0700 directory under
`$HOME`). There is no prior Kuala Lumpur research, so no legacy dispositions
exist.

## Method and evidence rule

Every venue claim carries a quote re-derived at build time from a text capture
in `captures/` plus a line locator; `kl_build.py` refuses the build when the
needle (capacity figure, price string or address) is absent from the cited
lines. `capture-manifest.json` pins every capture with URL, status and SHA-256.
PDFs were parsed by `kl_pdf.py` (pypdf in a scratch venv), and the holiday and
law quotes come from those parsed texts. Nothing is fetched at build time, so a
replay is byte-stable.

## Citation provenance

Every claim's named page is the page its quote came from. `kl_build.py` stamps
`source_url` and `source_title` from the cited capture's own
`capture-manifest.json` entry (`source_of()`), so an alcohol claim whose text
lives on the dining page names the dining page even though the room's capacity
chart lives on the events page. Four claim groups needed that: 12
`alcohol_service` + 12 `beer_allowed` (W and St. Regis, dining capturers), 10
address claims (5 Colony via `colony-locations`, 4 MITEC via `mitec-address`, 1
WSPACE via `wspace-contact`), and WORQ's window claim, which now cites the
published 8 am–10 pm booking line (`worq-events` 105) instead of the RM950 price
block (88-92). Values did not move: the only diffs against the previous store
are 34 × (url + title), the WORQ window quote/locator, and one event title.

`build/citation_gate.py` is the gate. For every claim carrying a
`capture <slug>` locator it requires the slug to exist in the manifest, the
`source_url` to be that capture's requested or resolved URL, and the
`source_title` to identify that page (normalised substring of the page's own
`<title>`, so an honest short label passes and another page's title fails). It
is city-agnostic — point it at any city directory — and `kl_build.py` runs it
in-process, so a drifted citation fails the build. It is deliberately a
separate module rather than a change to `plan-event/scripts/city_store.py`:
that file carries another card's uncommitted edits right now, and the same
check against Oslo (19), Lisbon (280 title-only), Bangkok (4) and Budapest (71)
shows the drift class exists in published stores, so making `--check` strict
fleet-wide is a manager decision, not a side effect of K1.

## Assessed rooms (30)

Capacity basis: **theatre** 21, **seated** 3 (klpac's fixed, modular and
removable seat counts), **venue_max** 5 (Common Ground and WSPACE "up to N
pax"), **mixed** 1 (Colony The Lounge, existing 50 / theatre 70). No room is
claimed as a confirmed seated 50 unless its row says seated; every
theatre/venue_max row carries a capacity blocker.

- **Colony** (`colony.work/event-space`): Event Lounge KLCC, theatre 80 /
  banquet 40, from RM 4,800; Event Lounge KL Eco City, 100 / 80, from RM 4,800;
  The Glass Box (Mont Kiara), 400 / 300, from RM 17,000 unfurnished (RM 21,800
  furnished); Rooftop Terrace, 150 / 150, from RM 8,000; The Lounge, existing
  50 / theatre 70 / banquet 40, from RM 5,300. Sun Room (20) and Boardroom (26)
  are leads, below the brief.
- **W Kuala Lumpur** (`marriott.com/.../kulwh.../events`): capacity chart with
  theatre, schoolroom, reception and banquet columns — Great Room 700/630,
  Great Room 1 250/220, Great Room 2 350/220, Studio Room 180/120, Studio 1
  82/50. Studio 2 and Studio 3 print 48 theatre and are leads.
- **The St. Regis Kuala Lumpur**: Astor Room 1 130/120, Astor Room 2 130/120,
  Astor Room 3 150/120, Astor 1 & 2 260/240, The Astor Rooms 500/360, Ringgit
  Room 1 80/60, Ringgit Room 2 90/80.
- **Common Ground**: KLCC up to 80, Bukit Bintang up to 120, KL Eco City up to
  80 (event-space pax; layout unlabelled). Ampang is 68000 Ampang Jaya,
  Selangor and is a lead, not a city room.
- **WSPACE**: Event Space 50 (Mid Valley) up to 50 at RM 350/hour; Event Space
  80 (GTower) up to 80 at RM 900/hour. The 30-pax room is a lead.
- **WORQ**: event hall, theatre 80 / classroom 30 / cluster 25, RM 950 per
  four-hour session.
- **klpac**: Pentas 1, 504 fixed seats; Pentas 2, 210 modular seats; indicine,
  100 removable seats.
- **MITEC**: Level 3 halls 18,000 theatre / 6,700 banquet across three halls;
  Level 2 hall 4,000 / 1,500; Level 1A Novel 742 sqm, 700 / 350; The Gallery
  373 sqm, 500 / 200.

Programme windows, stated only from a published interval:

- WORQ **12-hour yes** and **8-hour yes**: the event-space FAQ publishes
  `available for booking from 8 am to 10 pm daily`, so 09:00–21:00 and
  09:00–17:00 both sit inside the bookable day; closing 22:00.
- The other 29 rooms are **unknown** for both windows. No operator page prints
  a 09:00–21:00 event interval, and a staff-hours line (Common Ground 9am-6pm
  weekdays) is not an event window. Tally: 12-hour yes 1, unknown 29, no 0;
  8-hour yes 1, unknown 29.

Costs (MYR at the dated cross, USD 1 = MYR 4.1155): Colony 4,800 → USD
1,166.32; 4,800 → 1,166.32; 17,000 → 4,130.73; 8,000 → 1,943.87; 5,300 →
1,287.81. WSPACE 350/hour → 85.04/hour; 900/hour → 218.69/hour. WORQ RM 950
per session → USD 230.83 per session, and USD 461.67 for 8 h / 692.50 for 12 h
by multiplying the published four-hour session (stated as a multiplication, not
a quote). Twenty-two rooms publish no rate, so no programme cost is claimed.
The one budget exception uses the New York shape: The Glass Box furnished rate
RM 21,800 → USD 5,297.05, above the USD 5,000 soft budget, with the unfurnished
RM 17,000 alternative and the unknown extras named.

Coordinates: 16 of 30 assessed rooms carry numeric latitude/longitude derived
from a verified address claim, across four buildings (Colony The MET, W Kuala
Lumpur, St. Regis, Common Ground Bukit Bintang). Nominatim returned no match for
Vipod Residences, Menara 2 KL Eco City, Menara Darussalam, Centrepoint North,
GTower, klpac and MITEC, so those rows have no pin; each lookup is recorded as
`none`. WORQ prints no outlet, so its lookup is recorded as `no_address`.

## Platform lanes

- Peerspace: homepage 200, but `/venues/kuala-lumpur--MY` and
  `/venues/kuala-lumpur` both returned 403. **Blocked, not empty**; no count.
- Tagvenue: `/my/kuala-lumpur/` is 404 and the site's own market list is
  Australia, Canada, Ireland, Singapore, UK and USA. **Empty by design**.
- Eventective: `/kuala-lumpur-malaysia/` is 404. **Empty** at that path.
- Venue Report: `/venues/kuala-lumpur/` returned 403. **Blocked, no count**.

Every lane has a `sources_consulted` row with `pages_read`, `venue_yield`,
`event_yield`, `hits` and `disposition`.

## Event lanes and the 2027 list

Mandatory sources were read on 2026-11-25. MiraGather's three views are 47-byte
JavaScript shells; the Luma Decentralized AI past tab is an 807-byte shell; AI
Tinkerers' all-cities directory lists Kuala Lumpur (line 384) and its chapter
page serves 31 dated past events but no 2027 edition. Luma's Kuala Lumpur city
page shows ten cards, all 2026-dated (three gave community leads); Eventbrite
Kuala Lumpur shows 2026 cards plus one 2027 hackathon; Meetup's Kuala Lumpur AI
results are November–December 2026. DMEXCO Asia 2027 is 7–8 April at Marina Bay
Sands, Singapore, so it is recorded and excluded; Selangor Techsphere returns to
KLCC in 2027 but prints "DATES TBC", so no dated row is stored.

Eleven 2027 events are stored from nine `event/organiser` source pages, each
with a capture that prints the dates:
Global Innovation Hackathon Malaysia 23–24 Jan (ReSkills EdTech, International
Youth Centre); AIMY / Asia AI Infrastructure Malaysia Summit 24 Mar (KL, venue
unnamed); MTE 8–10 Apr (Protemp, venue unnamed); Digital Transformation Summit
Malaysia 14 Apr (Exito Media Concepts); BFSI IT Summit 15 Apr (Exito); InnoAI
Summit 22–23 Apr (Yuktan Technologies, Concorde Hotel Ampang); CETA 28–29 Apr
(The C0_Lab, KLCC); DCCI 4–5 May (KLCC); AiSEAN Summit 10–11 Jun (Hilton KL
Sentral); Cyber Security Summit KL 22 Sep (Exito); Petrosains AI Summit 26–28
Nov (KLCC). Seven events carry a cited organiser line covering five distinct
claim-backed organisers (Exito Media Concepts on three events, plus ReSkills
EdTech, Protemp Group, Yuktan Technologies and The C0_Lab); AIMY, AiSEAN, DCCI
and Petrosains are stored as explicit brand inferences because their pages do
not print a legal organiser.

## Community lane

Opened as a lane of its own: 25 `community/*` rows in `sources_consulted`
(grouped `community/meetup` 7, `community/luma` 9, `community/chapter` 2,
`community/directory` 3, `community/student` 3, `community/web3` 1), each with
URL, title, status, pages read and a note naming its yield. Fifteen records
stand, every one on a page read today:

- **Meetup group pages (6 records, with held events and member counts):** AWS
  User Group AI/ML Kuala Lumpur 2,101 members, five held events Feb–Jun 2026
  with 142–187 attendees each, at The Access Group TRX, Xendit KL Sentral and
  Arvato GTower; Ethereum Malaysia (ETHKL) 4,052 members and 209 past events,
  including 25 Apr 2026 at Millerz Square and 4 Feb 2026 POP-X Kuala Lumpur;
  LFDT Kuala Lumpur and Cyberjaya 419 members, 83 past events; Kong/KUALA-LUMPUR
  185 members, 104 past events; Kuala Lumpur Web3 Meetup 64 members, two held
  events at Dome Cafe Suria KLCC with 3 attendees each; Kuala Lumpur AI Group 63
  members, one held online event with 27 attendees. The last four run online or
  very small editions — recorded plainly rather than counted as 50-person rooms.
- **Luma and chapter pages (5 records):** AISEA (AISEA WEEK 2.0, 13–21 Nov 2026,
  Kuala Lumpur, marked Past Event with 77 Went); Malaysian AI (weekly events,
  eight-week in-person residency at 500 Global, Bangunan AICB); The AI Collective
  Kuala Lumpur (28 Nov 2026, 17:00–22:00, KLCC area — an upcoming edition, so
  cadence is not claimed); SideQuest (biweekly coworking sessions); AI Tinkerers
  Kuala Lumpur (31 dated past events, 12 May 2024 to 19 Nov 2026). n8n Kuala
  Lumpur, Codex Community Kuala Lumpur and 4rthur.ai stay as city-page cards
  only — the n8n organiser page is a 91-byte shell, `luma.com/4rthur` is 404 and
  the community-run Codex calendar is marked deprecated.
- **Students (1 record + 2 named and dismissed):** APU Artificial Intelligence
  Club from APU Student Affairs (society, advisor, no dated public event, so no
  cadence or attendance claimed). Monash MUSA's club list and AI Hackerdorm's
  site print no AI-society event page, so they add no row.

Dispositions where the lane yielded nothing: `luma.com/codex-community` has no
Kuala Lumpur row among its visible past events; the Malaysian AI calendar
renders event titles but no dates; malaysia-ai.my is an organisation directory,
not a community calendar; the Malaysia Blockchain Association prints no event
calendar; `meetup.com/kl-cyber-security-for-controls-systems` was a guessed slug
that returned "Group not found" (the group is named only in the Meetup feed
capture); `myblockchainweek.com` is the MYBW **2026** edition, 29–30 July 2026 at
World Trade Centre Kuala Lumpur, with no 2027 dates, so it is recorded and
excluded. Codex's and 4rthur.ai's printed venues (Cyberjaya, Sunway) are in
Selangor and are labelled as outside the Federal Territory.

## Holidays

Twenty-one 2027 rows from `kalendar.ecentral.my/kalendar-2027`, which states
that its dates come from the JPM `Jadual Hari Kelepasian Am Persekutuan dan
Negeri 2027`. Two coverage rows: federal `MY` and `MY-14` (Kuala Lumpur). The
Kuala Lumpur layer adds Federal Territory Day on 1 February and the replacement
holidays on 8 February, 8 June and 16 August, and is named for New Year (1 Jan),
Thaipusam (22 Jan), Nuzul al-Quran (24 Feb) and Deepavali (28 Oct). Islamic
dates — Nuzul al-Quran 24 Feb, Hari Raya Aidilfitri 10–11 Mar, Hari Raya Haji
17 May, Awal Muharram 6 Jun and its replacement 8 Jun, Maulidur Rasul 15 Aug
and its replacement 16 Aug — are marked `derived: true`,
`subject_to_announcement: true` and `observance:
statutory_subject_to_announcement`. The primary JPM schedule PDF was not
retrieved; the table is a reproduction and is labelled as such.

## Law

- **Alcohol:** Excise Act 1976 s.32(1) — no retail sale of intoxicating liquor
  except under a licence and in a place specified in the licence; s.35(1) lists
  public house, beer house, retail shop and wholesale classes. Per room:
  **yes** on 1 room — WORQ, whose event-space FAQ asks "Can we serve alcohol?"
  and answers "We have no restrictions as long as everything is clean and tidy
  after the event." **unknown** on the other 29 rooms. W Kuala Lumpur's dining
  page calls WET DECK, an outdoor bar and restaurant, a spot for private events
  (`w-dining` 185), and The St. Regis page describes Astor Bar and Decanter with
  650 labels and a whisky bar (`stregis-dining` 136); neither line is the room's
  event terms or a licence for a private event, so both groups stay unknown, with
  the bar mention kept as context and a licence question on each room. A hotel
  bar licence and an event licence are separate questions. No licence holder is
  printed anywhere; no venue was contacted.
- **Food:** Food Act 1983 defines "food premises" and lists event/food caterers
  (MSIC 56210); the Act makes catering a licensed food activity but does not
  approve a caterer for a venue. catering/food_service/delivery stay unknown.
- **Language:** National Language Act 1963/67 s.2 requires the national
  language for official purposes; the scope clause does not name a private
  commercial event. Malay and Chinese text is kept with an English gloss and a
  review note (holiday names, `cuti ganti` as replacement holiday).

## Photos

Wikimedia Commons only; no operator gallery with a stated licence was
extracted. 43 live rows on 16 assessed rooms: klpac (three rooms, four images
each), MITEC (four halls, four each), Colony KL Eco City and Common Ground KL
Eco City share the four KL Eco City files, and seven St. Regis rooms share one
narrow tower image. Fourteen assessed rooms have none and carry an explicit
withheld row. Every chosen file was fetched with a real GET and records status
200, byte count and content type. Licence mix: CC BY-SA 4.0 (36), CC0 (4),
CC BY-SA 3.0 (3). No placeholder, look-alike or unlicensed copy is used;
"View from Vipod Residences" images were rejected because they do not depict
the building.

## AV and Wi-Fi

A room's `screen` and `wifi` is `confirmed` only where that room's own printed
block names the equipment. WSPACE is the one such case: the Event Space 50 card
prints "60-inch smart TV", "Projector", "Projector Screen", "HDMI Cable",
"Drinking Water", "Wifi Connection" and a flipchart (`captures/wspace.txt`
62-68); the Event Space 80 card prints the same list without the TV (74-80); and
the FAQ repeats "WIFI, projector or Smart TV" (line 90). Both rooms are
`confirmed` against the room card. Venue-level statements do not confirm a room:
W's "LCD screens ... Wi-Fi" applies to "our meeting venues" generally
(`w-events` 171), The St. Regis lists hotel AV services without naming a room
(`stregis-events` 1575-1579), and Colony's "Built-in AV Systems & Projector" is
a portfolio-wide plan inclusion (`colony-events` 109-110). Those 17 rooms (5 W,
7 St. Regis, 5 Colony) stay `unknown`, and the rule is recorded in every
`screen`/`wifi` condition.

## Conflicts and failures kept

- W Studio 2/3 and Colony Sun Room/Boardroom print capacities below 50 and are
  leads, not assessed rooms.
- Common Ground Ampang is Selangor by its own address line; excluded.
- MITEC Level 3 and W great-room figures are multi-hall/theatre maxima; each
  row keeps a capacity blocker.
- KLCC's capacity chart is an image-only PDF (3 pages, 43 extractable
  characters); numeric hall capacity could not be established.
- DOJO's TLS certificate had expired; its halls appear only in a search extract
  and are a lead, not a stored page.
- Mandarin Oriental, Shangri-La, Traders, Grand Hyatt, Venue Report and
  Peerspace city paths were blocked; Sunway Pyramid CC, APW and MITIC did not
  resolve; The Co. now serves an unrelated lottery page.

## Declared gaps

1. Programme windows: 29 of 30 rooms are unknown for both windows; only WORQ
   publishes a bookable day that covers 09:00–21:00. This is the main gap.
2. Prices: 22 of 30 rooms publish no rate, and no all-in quote exists anywhere;
   tax, service charge, staffing and F&B are unquantified even on the priced
   rooms. WORQ's 8 h and 12 h figures are multiplications, not quotes.
3. Seated capacity: only 3 rooms publish a seat count; 27 are theatre,
   venue-max or mixed figures (21 theatre, 5 venue-max, 1 mixed), so "plausibly
   serves 50" is not "confirmed seated 50".
4. Photos: 14 assessed rooms have no usable image and all cleared images are
   Commons building shots; no operator room gallery cleared rights.
5. Access and climate: transit, monsoon/heat exposure, alcohol model, food
   service and delivery are unknown on 27–30 rooms. No 21:00 rail-service
   statement was found.
6. Holidays: the JPM primary schedule was not retrieved; the reproduction is
   labelled, and Islamic dates remain subject to announcement.
7. Hotel and convention stock: only W and St. Regis published readable capacity
   charts; Mandarin Oriental, Shangri-La, Traders, Ruma, WTC and Connexion
   stayed leads. MITEC is assessed capacity-only.
8. Communities: fifteen records, but only six carry printed member counts and
   only six sit on dated physical Kuala Lumpur editions; four of the Meetup
   groups run online network events with no Kuala Lumpur room. No 2027 community
   calendar is stored: every dated edition found is 2024-2026. The student lane
   has one society row and no dated event.
9. Archive dispositions: 160 captures exist, 83 are discharged by a claim or a
   `sources_consulted` row, and 77 are read-and-rejected pages that carry no row
   of their own (blocked PeerSpace paths, Cloudflare hotel pages, superseded
   calendar reproductions). That ratio matches the peer stores (Oslo 27 of 80,
   Lisbon 80 of 113). The one page the review named — `myblockchainweek.com` —
   now has its own row.
10. No venue was contacted and no visit was made; `visits` stays empty.

## Ceiling measurement

The metric is non-blank hand-written tooling lines in `build/`: `kl_build.py`
630, `kl_fetch.py` 98, `kl_render.py` 78, `kl_photos.py` 99, `kl_geocode.py`
72, `kl_pdf.py` 45, `citation_gate.py` 75 — **1,097 non-blank (1,166 raw)**.
Excluded as sourced data, not tooling: `kl_venues.py` (397) and `kl_other.py`
(386), which hold the facts, quotes and source ledger, plus every capture,
manifest, geocode and photo record. The card ceiling is 600; the build script
alone is 630, and the acquisition utilities plus the citation gate are the
overage. The gate is the round-3 addition (+75) and the citation stamping added
25 lines to the build; nothing was deleted or refactored for the number. The
manager's amendment should therefore be ~1,100 rather than ~1,000 (the Lisbon
precedent was 1,100; Oslo was amended 600 → 900 on the same pattern).

## R3 revision-1 refresh (2026-11-26)

Store: `research/kuala-lumpur/city/city.json`, `refresh_revision: 1`,
`updated_at 2026-11-26T09:00:00Z`, run `run-20261126-kl-r3`. SHA-256
`a5d37975953b279b7edc1947045ee72a68baafb0eb7e918fa55d5c0bfa85b4b5`
(1,845,993 bytes). `city_store.py --check` passes (55 venues); `loss_check`
returns `{}` against `city.pre-r3.json`; the ranker returns 30 open rows plus 25
leads (55, one per venue); the page renders to scratch with
`--no-map-assets` at 609,307 bytes and 55 rows. City-scoped evidence is in
`research/kuala-lumpur/r3-2026-11/` (captures + manifest, geocode/, pdf/,
photo-records.json, event-matrix.json, coordinate-tiers.json, build and verify
scripts).

**Coordinates.** All 55 records geocoded afresh with one live Nominatim search
each (90 queries; every attempt kept in `geocode/<venue_id>.json`). The 39
pinless records each gained a tier: 30 building, 3 exact_venue, 3 street, 3
area, 0 unresolved. Store-wide: 3 exact_venue (APW Bangsar, MATRADE MECC,
Sunway Pyramid CC — the geocoder returns the venue itself), 46 building, 3
street (The Hive Bukit KL, The Co., Common Ground Ampang), 3 area (two KL Eco
City records, WSPACE Mid Valley). Branch conflicts checked one by one: Colony's
three KL sites, Common Ground's four, WSPACE's two and W vs St Regis all resolve
to different addresses. The Co.'s site now serves a lottery page, so its street
comes from a 2016 listing at The Row and is labelled as such.

**Photos.** 43 → 55 live rows. Venues with 1+ photo 16 → 23, with 4+ 9 → 9,
with none 39 → 32. Rights: 36 CC BY-SA 4.0, 4 CC0, 3 CC BY-SA 3.0 (Wikimedia,
unchanged) plus 12 operator assets hotlinked with attribution (MITEC 3, Marriott
2, Common Ground 2, klpac 2, Publika 1, The Hive 1, Connexion 1). Room-versus-
fallback: 12 venues carry a room-kind view (interior/layout/floor_plan), 11 only
a labelled fallback (exterior or lobby), 32 none. The WSPACE asset the page
serves returns 404 and is recorded as a failed lookup, not a photo.

**Holidays.** Local public unchanged at 21 rows in the Federal Territory
(column) shape, each re-weekdayed from code (0 mismatches); eight Islamic-date
rows keep `derived`/`subject_to_announcement`. New local school layer: 14
Kumpulan B rows (four term breaks plus ten KPM additional festival days) read
from the KPM *Kalendar Akademik Tahun 2027* PDF — which is image-only, so its
text came from OCR of all seven pages. The BKPP primary schedule PDF was
unreachable (three URL forms, all timed out), so the KL column rests on three
independent reproductions and is declared as such. Comparison countries: none
stored for this city.

**Events.** 11 → 13, with the 66-cell six-theme matrix in
`event-matrix.json` (11 lanes × 6 themes). Luma's Kuala Lumpur page has 150 KL
mentions and zero 2027 dates; the two alias pages and the Malaysia page carry
none; MiraGather's payloads (1.8–2.1 MB) name no Kuala Lumpur event; AI
Tinkerers' all-cities page returns 403 and its KL chapter ends in November 2026;
Meetup returns November–December 2026 editions. Two 2027 Kuala Lumpur events
were added from Eventbrite (GAICC 24 January at The Majestic; Business Growth AI
15 July, venue unnamed) and XR ASIA SUMMIT 2027 was excluded as Petaling Jaya.
Source yields sum to 13.

**Access.** 1 full window (WORQ, 8 am–10 pm daily, covers 09:00–21:00), 54
unknown, 0 no. Every unknown names the pages read and, where a clock exists, the
office- or mall-hours line that is not a hire interval (WTC 9.00 am–6.00 pm
Mon–Fri; WSPACE 9:00am–6:00pm weekdays; Publika 10:00am–10:00pm).


## R3 review round 2 (2026-11-26)

The review asked for three corrections; nothing else was rebuilt. Store now
`sha256 11972bfd3d5b3e746e7f0735e15f07d971eaab9719e6a337155f0edee4ef04cb`,
1,846,168 bytes, same run id and `refresh_revision: 1`; `--check` passes,
`loss_check` returns `{}`, the ranker returns 55 rows, 869 stored locators
resolve, and the scratch render is 598,103 bytes (the drop from 609,307 is the
20 building photographs removed from five galleries, see below).

1. **Photo labels.** `build_r3.py` applied `setdefault(view_kind, interior)`
   before the room rule, so 20 legacy Wikimedia records on MITEC Level 1A/2/3
   and klpac indicine/Pentas 2 were labelled `interior` while their own `room`
   is `building`. The rule now runs first and `interior` is never a default:
   `room == building` gives `exterior`, a named room gives `interior`, and a row
   with neither keeps no view. Those five panels now carry only the operator
   floor plan or room asset; the 11 venues whose only photographs are exteriors
   keep their `Exterior`/`Lobby` labels. Room-kind venues stay 12, fallback-only
   11, none 32.
2. **Per-fact event evidence.** GAICC and Business Growth no longer cite one
   date line for seven claims. Each page-printed fact carries its own line and
   quote (GAICC: date 134, kind 104, relevance 100, organiser 104, venue 96;
   Business Growth: date 95, kind 97, relevance 93, venue 121-122). Business
   Growth has no printed organiser and neither page prints a status word, so
   both values are null with an absence locator instead of a guessed value.
3. **Derived gap text.** The photos declared gap is now generated from the
   store: 43 of 55 records carry no room-kind view (32 none, 11 fallback-only),
   7 records gained a first photograph, 12 operator assets.
