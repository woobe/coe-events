# New York — revision-1 refresh (R9)

Run `run-20261126-nyc-r9`, checked 2026-11-26. Scope: `research/new-york/city` only.
Store: `city.json` (revision 1), sidecars and captures beside it.

## Captures

- 189 files under `captures/`, hashed in `capture-manifest.json`.
- Operator/listing pages: 30 Tagvenue room pages plus NYU, Civic Hall, Peerspace,
  NYC Seminar Center, Advent Hope, Brooklyn Public Library and CUNY Graduate Center.
- Authorities: OPM 2027/2028 schedule, NYS Civil Service 2027 legal holidays, NYC OPA
  2025–2027 payroll calendar PDF, DCAS PSB 440-2 PDF, General Construction Law §24,
  NYCPS 2026–2027 calendar (the 2027–2028 URL returned HTTP 404).
- Event lanes: Luma city/alias/organiser pages, Meetup six theme searches, Eventbrite six
  theme browses, MiraGather main/side/`/ai`, AI Tinkerers directory, 22 organiser pages and
  three new 2027 candidates.

## Addresses and pins

Every row was re-read from its operator or listing page and geocoded afresh with one live
Nominatim lookup per address (raw responses in `geocode/`, log in `geocode-log.json`).
Tiers: exact_venue 10, building 23, street 0, area 0, unresolved 0 (33 total).

- Civic Hall was stored at 28 East 28th Street; the operator prints 124 East 14th Street,
  New York, NY 10003 (Zero Irving). Corrected and re-geocoded to the named Civic Hall POI.
- The Monroe Room had a point east of Fifth Avenue for a West 38th Street address. Two OSM
  nodes exist for 15 West 38th; the west-side office node is used and both are recorded.
- Ridgewood Hall's house number matches but OSM places it in Middle Village 11378 while the
  operator prints Ridgewood 11385; declared as a conflict.
- The three pinless leads gained addresses from their own pages (Advent Hope 111 East 87th
  Street; CUNY 365 Fifth Avenue) and, for Brooklyn Public Library, the LPC LP-1963 report,
  because the BPL meeting-rooms page returned HTTP 403. All three now carry a tier.

## Photos

Before: 4 venues with one or more, none with four, 29 with none, 31 records.
After: 29 venues with one or more, 28 with four, 4 with none, 117 records.
Rights: 108 operator-gallery assets hotlinked with attribution, 5 CC-licensed Commons files.
Views: 108 interior, 1 layout, 4 exterior. Each record carries `view_kind`, rights, source
page, placement proof, HTTP verification and a withheld flag where nothing is placeable.

## Holidays

50 rows (49 intersect 2027): US 12, US-NY 14, US-NY:nyc 14, US-NY:nycps 9 (2027).
Every row now carries a computed `weekday` and the capture it came from. Overlapping
observances are separate rows by scope and are not double-counted inside a scope.

- US: OPM 2027 schedule, including the 31 December 2027 observance of New Year's Day 2028.
- US-NY: Civil Service 2027 table, cross-checked against GCL §24 (which also lists Flag Day,
  not observed as a closure).
- US-NY:nyc: OPA 2027 payroll list with DCAS PSB 440-2. The floating Lincoln's Birthday
  (12 February, eligible employees only) is added as its own row.
- US-NY:nycps: 2026–2027 calendar. Added MLK Day, Eid al-Fitr, Good Friday, Eid al-Adha,
  Memorial Day and Anniversary Day; the 2027–2028 edition is not published (HTTP 404).

## Events

25 stored events (22 retained, 3 added), 54 matrix cells attempted. Retained events cite a
live organiser page printing 2027 dates (19 live reads, 3 flags). Added: ETHConf 2027
(14–16 June), DAOS CON 7 (7 March), Blockchain Tech Summit (28 September). Meetup and Luma
returned near-term 2026 listings only; AI Tinkerers returned HTTP 403. Three retained events
carry dated gaps: PE4KS (month-only page), Tech Week (HTTP 429) and Chainalysis Links
(HTTP 403), the last two corroborated by the MiraGather 2027 listings.

## Access

Full 12-hour window 7, 8-hour floor only 9, shorter 5, unknown 9. The five rooms that printed
"Open 24 hours" on the Saturday price row fell from yes to unknown because that is an opening
line, not a hire interval; two per-session rooms and Seminar Room A also stay unknown for 12h.

## Conflicts and open items

- This card's acceptance criterion 4 names Lovdata and Utdanningsetaten (Oslo). The body and
  named-sources section direct New York to OPM, NYS Civil Service, OPA/DCAS and NYCPS; those
  were read.
- BPL, NYU, Peerspace and NYC Seminar Center blocked or rate-limited their galleries; those
  venues are withheld, not filled with look-alikes.
- The Tagvenue-hosted operator galleries publish no separate licence text; every record says so.

## Round 2 remediation (review round 1 changes requested)

Checked 2026-11-26, run `run-20261126-nyc-r9-r2`. All ids preserved; no record re-keyed.

### Quote audit

- 390 venue claims carried a quote; 123 were not a contiguous line of the capture stored
  for that record. Every one was fixed: 108 re-quoted verbatim from the capture (50
  catering blocks, 48 "Up to N seats" lines, 5 "Open 24 hours" cells, 5 price/access rows),
  and 15 had the quote and locator withdrawn where the page is blocked or the sentence
  could not be reproduced.
- Final audit: 338 quotes resolve to a line in a capture file for their record; 4 address
  quotes resolve to the stored Nominatim response in `geocode/` (see blocked pages below);
  33 coordinate quotes resolve to the geocode responses; 0 unresolved.

### Blocking findings

1. Seminar Room A (`nyc-ca43f10af68d`): the 24 November quote is gone. `access_window`
   now cites "Daily Rates (Monday through Sunday, 8:00am - 5:00pm)" from
   `captures/venue-nyc-ca43f10af68d.txt`; the 8-hour state is yes because the daily block
   contains 09:00-17:00, and 12-hour stays unknown because the page publishes no
   09:00-21:00 interval (the four-hour rule is a booking minimum). Catering, food service,
   screen and wifi lose their citations (the sentences are not in the capture; the room
   page returned HTTP 429) and are marked carried, low confidence.
2. Civic Hall (`nyc-4c6638c43df6`): address re-quoted from the contact capture; transit
   re-derived at 124 East 14th Street (14 St-Union Square 165 m, 3 Av 171 m, Astor Pl
   478 m); all four photo proofs and distances now reference the corrected address.
3. Blocked pages: BPL meeting rooms (Cloudflare 403), NYU Kimmel (HTTP 202, empty body),
   Monroe Room and Tel Aviv Room (Peerspace 502/403). Addresses now cite the Nominatim
   returned place in `geocode/` with a note that the operator page was not readable; the
   other page-derived facts carry an explicit carried-basis derivation. Four dated
   `declared_gaps` entries record this.
4. CUNY photos: proof text, attribution and rooms fixed (Proshansky Auditorium, Elebash
   Recital Hall, Kelly Skylight Room, Dining Commons); real dimensions and byte counts
   recorded.
5. Event matrix: every cell now carries `retained` and `retained_ids`; `ai/meetup` records
   the three Wall Street Meets AI events from the followed organiser calendar. Stored
   event -> lane mapping is in `event-lane-map.json` (11 in keyword cells, 14 read from
   the global conference calendar).

### Folded-in fixes

- 13 records gained a `dimensions` object; the 5 Commons records gained `placement_proof`
  and `distance_m` from the Commons imageinfo capture (`captures/commons-imageinfo.json`).
- Photo split now: 78 records with a room, 4 exterior building fallbacks, 31 interior
  records without a room label, 4 withheld. Before: 31 records, 26 withheld, 5 with no
  rights value.
