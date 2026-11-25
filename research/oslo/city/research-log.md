# Oslo O1 — research log (2026-11-25)

Store: `research/oslo/city/city.json` — schema `city-store/1`, 45 records
(30 assessed rooms + 15 leads), 7 events, 8 communities, 12 holiday rows,
1 coverage row, 126 photo rows (114 live, 74 of them on assessed rooms;
12 explicit withheld venues). Run `run-20261125-osl-b1`, pinned
`2026-11-25T01:00:00Z`.
SHA-256 `30e2fc256268c165a66af947594f926f860aa5fd1cb354ec345d2632f21d6b59`
(1,670,616 bytes, rebuilt twice, byte-identical). `city_store.py --check`
passes; `plan-event` suite 1,550 passed / 0 failed. There is no prior Oslo
research: discovery is from zero, so no legacy dispositions exist.

## Method and evidence rule

Every venue claim carries a quote re-derived at build time from a text capture
in `captures/` plus a line locator. `os_build.py` refuses a build when the
needle (capacity figure, price string or address) is absent from the cited
lines; addresses are checked against their exact source line. `capture-manifest.json`
pins every capture with URL, status and SHA-256; 67 of 80 capture pages
returned content and the 13 failures (9 HTTP 404, 3 HTTP 403, 1 DNS failure)
are recorded with their status and a zero-byte body. Nothing is fetched at
build time, so a replay is byte-stable.

## Assessed rooms (30)

Seated basis 5 (Deichmansalen 150, Kinosalen 68, Munch Festsal 160 dinner,
Ingensteds 100 chairs, Vippa 300 at long tables); theatre basis 2 (Epicenter
Disruption Hall 230, Think Big 60); the other 23 are operator maximum or
unlabelled layout figures.

- Deichman Bjørvika: Deichmansalen 150 amphitheatre seats, full day 49,500 kr;
  Kinosalen 68 seats, full day 20,000 kr. Both ex VAT. Source
  `deichman.no/event-og-konferanse` and the 2026 price list.
- MUNCH: Festsal 160 at round tables (the same line prints 350 and 500 for
  other layouts); Toppsal 140. No rate printed.
- Mesh: Atrium 220; Workbar Youngstorget 250; Rooftop 150 (prose says 200,
  capacity field says 1-150); Workbar Nationaltheatret 100 (prose 100, field
  1-150). Both conflicts are stored with the lower figure and a blocker.
- Epicenter Oslo: Disruption Hall 290 sqm, 230 theatre / 300 mingle; Think Big
  60 theatre.
- Oslo Kongressenter: Sal A 200-690, Sal B 100-393, Sal C 70-242, Sal D 50-150,
  Møterom 1 26-100; published ranges kept as ranges.
- OsloMet: Festsalen 150, Studenthallen 200, Athene 1 og 2 192, S141 138,
  Store auditorium 440; term-window restrictions recorded.
- Thon Hotel Opera: Flagstadsalen 260 is the largest of six unlabelled layout
  figures (160/230/220/260/40/50); the seated figure is not labelled.
- Clarion Hotel The Hub: Kongressalen, 900 sqm, hotel maximum 1,110; the single
  hall's seated figure is not printed.
- NOVA Spektrum (Lillestrøm): Studio 2 300, Studio 3 190, Studio 4 230,
  Studio N 710; Green Room 150 is a lead (assessment cap).
- Sentralen: Marmorsalen up to 1,000, Hvelvet up to 200; the layout columns in
  the text capture are unlabelled, so no seated figure is claimed.
- Ingensteds: chairs for 100; day hire 10,500 kr, all-day 09:00-01:00 25,000 kr.
- Vippa: 300 seated at long tables, 800 standing; full-day private events
  Monday-Wednesday.

Programme windows, each stated from the line that publishes the interval:

- Deichmansalen 12-hour **yes** and 8-hour **yes**: `deichman-pris` 82-83
  publishes room bands 08:00-12:00, 12:00-17:00 and 17:00-21:00, and says a
  hire longer than one band is full-day (`heldagsleie`). The published room day
  is 08:00-21:00, so it covers both 09:00-17:00 and 09:00-21:00 at the full-day
  rate.
- Ingensteds 12-hour **yes** and 8-hour **yes**: `ingensteds` 34 publishes
  `Heldagsleie kl.09:00-01:00`.
- Kinosalen 8-hour **yes**: `deichman-event` 100 publishes `Salen leies
  hovedsakelig ut på hverdager fra 08-17` (mainly weekdays).
- Kinosalen 12-hour **unknown**: the room line says mainly 08:00-17:00 while the
  same operator's price list publishes a 17:00-21:00 room band; no line
  establishes this room's letting past 17:00, so the conflict is recorded and
  the window stays unknown rather than "no".

The other 27 rooms are **unknown** for both windows. Tally: 12-hour yes 2,
unknown 28, no 0; 8-hour yes 3, unknown 27.

Costs (NOK at the dated cross): Deichmansalen 49,500 → USD 5,055.13 for either
window; Ingensteds 25,000 → USD 2,553.10 for 8h and 12h; Kinosalen 20,000 →
USD 2,042.48 for the 8-hour window only. Twenty-seven rooms publish no rate, so
no programme cost is claimed. The one
over-budget row uses the New York `budget_exception` shape and names what the
rate buys (150 seats, 108 sqm stage, Bjørvika) and the unknown extras (25% VAT,
catering, technicians).

Coordinates: 25 of 30 assessed rooms carry numeric latitude/longitude derived
from a verified street-address claim. Five have no pin because the operator
prints no street number: Deichmansalen and Kinosalen (building described only
as 200 m from Oslo S), both Epicenter rooms (street name only), and Vippa
(no address). Those lookups are recorded as `no_address`, not guessed.

## Platform lanes

- Peerspace: locations page returned 403 on plain and rendered reads. **Blocked,
  not empty**; no count is claimed.
- Tagvenue: the operator's own about page lists the UK, Ireland, Australia,
  Singapore, Canada and the US as its markets; `/city/oslo` is 404. **Empty by
  design**, no Oslo inventory.
- Eventective: `/oslo-norway/` is 404. **Empty** (no Norway path).
- Venue Report: `/venues/oslo/` is 403, nothing captured. **Blocked, no count.**

Every lane has a `sources_consulted` row with `pages_read`, `venue_yield`,
`event_yield`, `hits` and `disposition`.

## Event lanes and the 2027 list

Mandatory sources were read through their payloads on 2026-11-25. MiraGather's
three views are 47-byte JavaScript shells; AI Tinkerers lists Oslo in its city
directory but serves no dated 2027 Oslo edition; the Luma Decentralized AI past
tab is a 577-byte shell. Luma's Oslo city page shows 12 cards, all 2026-dated;
Eventbrite Oslo shows 2026 cards only; Meetup's Oslo AI group prints 4,729
members and no 2027 listing. `allai.events` lists 25 Oslo cards with 8 in 2027,
used as discovery only: it gave three conflicting May 2027 dates for one
consortium conference, so only organiser pages were stored. `aiwhatson` lists
NLDL (Tromsø), ICMRE (Grimstad) and SCIA (Gjøvik) in 2027 — none in Oslo.

Seven 2027 events are stored, each with a capture that prints the dates:
Oslo Innovation Week 25-28 Oct; Nor-Shipping 7-11 Jun; SECTECH Norway 17-18 Mar;
Oslo Tech Show 12-13 May; Data Centre Expo 12-13 May; NDC Oslo 31 May-4 Jun;
IEEE QAI 7-9 Sep. Six organisers are now claim-backed by a cited line:
Nor-Shipping/NOVA Spektrum (`norshipping-home` 257), AR Media International AB
(`sectech-no` 75), Live Expo/Easyfairs twice (`oslotechshow` 205 and
`datacentreexpo` 191), NDC Conferences AS (`ndcoslo` 18), and the IEEE QAI
organising committee at OsloMet (`ieee-qai` 42-44). Oslo Innovation Week's
organiser (Oslo Business Region) is **not printed on the cited page**, so that
row is stored as an explicit inference the page may not print as sourced.

## Holidays

Twelve 2027 dates from two authorities: `helligdagsfredloven` §2 (the named
days) and the 1 and 17 May act §1. Every date is marked `derived: true`:
Easter Sunday 2027 is 28 March, so Maundy Thursday 25, Good Friday 26, Easter
Monday 29, Ascension 6 May, Whit Sunday 16 May and Whit Monday 17 May follow.
1 May and 17 May are fixed dates. Easter week 25-29 March contains five
holidays. 17 May 2027 is also Whit Monday, so the §4 ban on public events
06:00-13:00 applies that day through the Whit Monday rule; the 1 and 17 May act
expressly excludes those two dates from holiday peace. §3 is the holiday-peace
rule (00:00-24:00); the 06:00-13:00 event ban is §4 (`lovdata-helligdager`
127-128) and the coverage row quotes it. Oslo fixes no separate
municipal public holiday. One `NO` coverage row; the shared registry has no
Norwegian scope, so the rows live in a hashed supplement.

## Law

- Alcohol: alkoholloven §1-4a requires a licence for sale/serving; §4-2 ties it
  to a premises and allows a closed-party licence. A 09:00-21:00 event with beer
  needs a licence holder; no assessed venue publishes its model, so beer stays
  unknown on all 30 rooms.
- Food: matloven §4 defines a caterer as a food business and §5 puts the
  compliance duty on it. Which caterers a venue approves is unknown; many route
  catering through their own kitchen or an approved supplier.
- Language: språklova §1 states the purpose and §3 states the scope — the state,
  counties and municipalities and the entities named there. That scope clause,
  not the purpose clause, is why no duty is read onto a private event organiser.
  No statutory language duty was found; the page is English with Norwegian
  names and diacritics kept.
Each is stored with the Norwegian quote and a reviewed English gloss.

## Photos

Wikimedia Commons only, because no operator gallery with a stated licence was
extracted. 74 live rows on the 30 assessed rooms: 12 venues with 4 photos,
6 with 3, 4 with 2, 8 with none. The assessed licence mix is CC BY-SA 4.0 (53),
CC BY-SA 3.0 (9), CC BY-SA 3.0 no (5), CC BY 4.0 (4), CC BY-SA 2.0 (2),
CC BY 3.0 (1). Across all 114 live rows (assessed + leads) the mix also includes
Public domain (3), CC0 (1) and CC BY 2.0 (1). Every row carries the source page,
file URL, dimensions, attribution and licence URL; the 12 venues with no image
have an explicit withheld row with a reason. Each live `verified` value is the
`{"status", "bytes", "content_type"}` object from a real GET on 2026-11-25: all
51 chosen files returned HTTP 200 with their byte count and `image/jpeg`. The
earlier HEAD pass had been rate-limited (429) and stored an integer plus zero
bytes; the re-fetch replaced it. Photos show buildings and, where available, the
room (Gamle festsal, Sentralen, Oslo Spektrum seated layout, Deichman interior);
no placeholder, stock or look-alike is used. UiO — Informatikksalen carries no
photo: the UiO Commons files depict Gamle festsal, a different room, so that
lead's row is withheld rather than borrowing them.

## Conflicts and failures kept

- Mesh Rooftop 200 vs 150 and Workbar Nationaltheatret 100 vs 150: lower figure
  stored, conflict named on the row.
- Deichman: the room pages say Kinosalen is let mainly weekdays 08-17, while the
  price list publishes half-day bands 08-12, 12-17 and 17-21 for rooms and calls
  anything longer than a band a full day. Deichmansalen is assessed from the
  bands (12h yes, room day 08:00-21:00); Kinosalen's 12h stays unknown because no
  line says the 17-21 band applies to that room.
- Thon and Sentralen capacity columns are unlabelled in the text capture; the
  figures are stored as maxima with a seated unknown.
- Clarion's 1,110 is a hotel maximum, not a verified hall seated figure.
- Deichman's building has no street address; Epicenter prints a street only;
  Vippa prints none. No pin is invented.
- Blå's Nominatim match returned the street without house number 9c and a
  different postcode; it is a lead and carries no coordinates.
- dogA's former rental URL returns the site's 404 page; Radisson's meeting page
  returns 403; UiO states it normally does not let rooms to external events and
  forbids food in Gamle festsal; BI prints no named room table.

## Declared gaps

1. Programme windows: 28 of 30 rooms are unknown for the 12-hour window and 27
   of 30 for the 8-hour window; only Deichmansalen and Ingensteds publish a
   span that covers 09:00-21:00. This is the main evidence gap and the page must
   show it plainly.
2. Prices: 27 of 30 rooms publish no rate. No all-in quote exists anywhere, and
   VAT, staffing, security and catering are unquantified even on the three
   priced rooms.
3. Seated capacity: only 5 rooms publish a seated figure; 23 are maxima or
   unlabelled layout rows, so "plausibly serves 50" is not "confirmed seated 50".
4. Photos: all cleared images are Commons; no operator room gallery cleared
   rights, and 8 assessed venues have no usable image.
5. Access and season: transit, winter exposure, alcohol model, food service and
   delivery are unknown on 30/30 rooms. No 21:00 service statement was found.
6. University and institutional stock: UiO is not a normal external rental; BI
   publishes no room table; dogA has no rental page. None is assessed.
7. Oslo Spektrum is arena-scale (11,500) with no small-room offer; kept as a lead.
8. IEEE QAI's venue page was not read; the city is confirmed, the room is not.
9. No venue was contacted and no visit was made; visits stays empty.

## Ceiling measurement

The metric is non-blank hand-written lines in the build tooling:
`os_build.py` 577, `os_fetch.py` 109, `os_geocode.py` 77, `os_photos.py` 112 —
**875 non-blank (955 raw)**. Excluded as sourced data, not tooling:
`os_venues.py` (273) and `os_other.py` (234), which hold the facts, quotes and
source ledger, plus every capture, manifest, geocode and photo record.
The manager amended the card ceiling from 600 to 900 on 2026-11-25 and asked
for the acquisition utilities to be kept, so 875 sits under the amended limit;
nothing was deleted or refactored for the number.
