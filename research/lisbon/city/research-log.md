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
of stored events: websummit.com 1, portugaltechweek.com 1, eventsindex 1,
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
