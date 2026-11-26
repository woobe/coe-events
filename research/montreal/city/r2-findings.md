# R2 Montreal store refresh — evidence and findings

Run: `run-20261126-mtl-r2` · checked 2026-11-26 · revision 1
Store: `research/montreal/city/city.json`
SHA-256: `47d7f1052fc2f3c2518dc8a9bdc46d60f3bfd550c68a3177a25f02689601fdc4`
Size: 1,195,102 bytes

## Verdict

The staged Montreal store now passes `city_store.py --check`, projects all 32 venues through `build_ranking`, carries a proven coordinate tier for every venue, 45 cleared operator-gallery photographs, a dated Quebec/federal/school holiday layer with the employer-choice pair intact, three 2027 events with organiser pages, and 13 dated declared gaps. No page was published, no summary HTML was written, and no other city subtree was touched.

## 1. Coordinates

Attempted: 32 of 32. One live Nominatim query per venue, re-run for every row including the 28 that already had a point.

Tiers: exact_venue 10, building 18, street 4, area 0, unresolved 0. Pins: 32 of 32 non-null.

Exact venue: Hyatt Place, Crew Collective, Le Studio TD, Le Balcon, Notman House, Café Van Houtte, SAT, Kawalees, Pub L'Annexe, District 3.

The four previously pinless venues:
- `mtl-1c9b9b2b165a` Hyatt Place — exact_venue (hotel POI at 1415 Rue Saint-Hubert).
- `mtl-9e195a901d0f` Notman House — exact_venue (Maison Notman POI at 51 Rue Sherbrooke Ouest).
- `mtl-b911cdc04475` Le Wagon — building (address node, Suite 101 inside).
- `mtl-d0e27aa38d40` SAT — exact_venue (Société des arts technologiques POI at 1201 Boulevard Saint-Laurent).

Street tier: the three Collectif MTL rooms (397A Rue Sainte-Catherine Ouest) and Mon Loft Privé (9 Rue Sainte-Catherine Est). OSM has no house number at either address; four lookups returned only the street or no result. These are honest street pins, not doors.

Postcode conflicts recorded: Maison Tela H3L 2Z8 vs OSM H3L 2V7; Centre humaniste H2J 1L7 vs H2J 1L5; Tango Renaissance H2W 1Z8 vs H2W 1Z5. Each point is the building frontage.

Refused lookups: “La Mise au Jeu” name query returned 1205 Rue Saint-Antoine Ouest, a different branch; Ax.c’s 800 Square-Victoria lookup returned a McDonald’s; Centre Communidée’s 137 Saint-Ferdinand returned Helios Makerspace. In each case the address node was used, not the unrelated business.

## 2. Addresses

All 32 address claims re-read and re-stamped 2026-11-26. 14 values were corrected:
- Collectif MTL ×3: operator prints 397A Rue Sainte-Catherine O, Suite 202, H3A 2G3; the Tagvenue listing had H3B 1A4.
- Maison Tela: 9850 Rue Tolhurst, H3L 2Z8.
- Mirale Studios: added H2N 2C5.
- Genesis HQ: “4526 Park Ave” normalised to Avenue du Parc.
- Notman House: added H2X 1X2.
- Groupe 3737: full French street form and H1Z 2K4.
- Kawalees: H2V 4G3.
- Pub L'Annexe: 5080 Rue St-Ambroise, H4C 2G1.
- Le Wagon: H2T 1X9.
- Centre humaniste: H2J 1L7.
- Tango Renaissance: H2W 1Z8.
- Les Connections Ralia: 4281 Boul. Saint-Laurent, H2W 1Z4.

15 address claims carry a verbatim line (operator address block or JSON-LD `streetAddress`). Four (Hyatt 429, Crew 403/no address text, Ax.c split footer, SAT client-side) carry a locator plus a retrieval note and `confidence: medium`.

## 3. Photos

Records: 87 total. Cleared 45. Withheld 42. The 48 inherited withheld records resolved as:
- Cleared 4: two Versa Loft files and two SAT files, both operator-hosted galleries.
- Dropped 2: `media.eventective.com/default_space.jpg` at Mirale and Genesis, platform placeholders that show no venue.
- Still withheld 42: Eventective/Tagvenue listings with no licence and no matching operator gallery image.

New cleared records: 41 operator-gallery images across 13 further venues (45 unique cleared URLs total).

Venues with 1+ cleared photo: 15. With 4+: 6 (Kawalees 6, SAT 6, Loft108 4, Studio Cuero 4, Maison Tela 4, Kptur 4). With none cleared: 17.

Room/fallback split: 40 room-kind (interior 36, past_event 3, floor_plan 1) and 5 fallback (lobby 2, exterior 3). Ax.c is the only venue whose cleared set is fallback-only (one building exterior).

View kinds: interior 36, past_event 3, exterior 3, lobby 2, floor_plan 1. No render, no stock, no placeholder.

Every cleared record has `view_kind`, `source_page`, `rights`, `attribution`, `checked_on`, `dimensions`, `thumb_note`, `placement_proof`, `verified` (HTTP 200 + content type + bytes) and `hotlink_ok: true`.

## 4. Holidays

Public, Quebec (`CA-QC`), 2027, from the statutes:
- 2027-01-01 Fri — Jour de l'An (N-1.1 art. 60 (1°))
- 2027-03-26 Fri or 2027-03-29 Mon — Vendredi saint **or** lundi de Pâques, employer's choice (art. 60 (2°)); both candidate dates stored, `choice: employer`, `single_settled_date: false`
- 2027-05-24 Mon — Journée nationale des patriotes (art. 60 (3°))
- 2027-06-24 Thu — Fête nationale du Québec (F-1.1 arts. 1–2; no Sunday substitute in 2027)
- 2027-07-01 Thu — Fête du Canada (art. 60 (4°); not a Sunday, so no 2 July)
- 2027-09-06 Mon — Fête du Travail (art. 60 (5°))
- 2027-10-11 Mon — Action de grâce (art. 60 (6°))
- 2027-12-25 Sat — Noël (art. 60 (7°))

Public, federal (`CA`), 2027, from the Canada Labour Program page: New Year's Day 1 Jan, Good Friday 26 Mar, Victoria Day 24 May, Canada Day 1 Jul, Labour Day 6 Sep, National Day for Truth and Reconciliation 30 Sep, Thanksgiving 11 Oct, Remembrance Day 11 Nov, Christmas 25 Dec, Boxing Day 26 Dec. Federal scope is separate from the Quebec layer.

School, French board (`CA-QC:cssdm`): CSSDM *Calendrier des activités scolaires 2026-2027*, formation générale des jeunes, dated 11-mai-26. Dated 2027 rows: 2027-04-23 Fri institutional pedagogical day; 2027-06-04 Fri CSSDM closure day. Coverage 2027-01-01 to 2027-06-30.

School, English board (`CA-QC:emsb`): EMSB *School Calendar 2026-2027 and Important Dates*. Dated rows: Winter Break 2026-12-21 to 2027-01-01; March Break 2027-03-01 to 2027-03-05. Coverage 2027-01-01 to 2027-06-30.

Weekdays recomputed in code for every row and now stored as an explicit `weekday` field (plus `end_weekday` on ranges and `candidate_weekdays` on the choice pair), not only in prose. Easter from the computus (Easter Sunday 2027-03-28). Comparison countries are not mixed into either local layer.

Noel 2027 falls on a Saturday. Article 60 prints the seven statutory days and no substitute date, so none is stored; the compensatory-day practice CNESST would confirm is recorded as a declared gap because CNESST could not be read.

CNESST was attempted and is recorded as blocked: the *Jours fériés* page returned Cloudflare HTTP 403 directly and through r.jina.ai on 2026-11-26. The statutory text is the authority used.

## 5. Events

Matrix: 6 themes × 9 lanes = 54 cells attempted. 48 opened, 6 blocked (Luma `mtl` and `montréal` aliases both 404). Evidence: `event-matrix.json`.

Retained from the lanes: 1 unique event, ALL IN 2027-09-22/23 (Scale AI organiser page prints the dates; MiraGather main, side and AI captures duplicate it).
Retained from direct flagship checks: Startupfest 2027-07-07/09 (startupfest.com banner); Montreal Family Office & High Net Worth Conference 2027-05-03 (dc-finance.com schedule). Total stored: 3.

Drops explained:
- Luma city page: 194 names in the payload, 0 occurrences of 2027.
- Meetup: six group pages and the directory opened; the only 2027 dates found belong to a JavaScript group, outside the six themes.
- Eventbrite: broad theme card sets (AI 16, ML 20, DS 19, Web3 20, crypto 19, blockchain 19) but no 2027 theme event. “What Does My Business Actually Need in 2027?” starts 2026-12-28; “Women in Tech 2027” starts 2027-02-25 and is a recruiting event.
- AI Tinkerers: all-cities directory and Montreal chapter opened; no 2027 dated event.
- Mila: one 2027 item, “Hack The High Seas: Ecohull Vessel Challenge”, 22–23 March 2027, outside the six themes.
- MTL connecte: a “Thème 2027” heading but no 2027 date or venue.
- C2 Montréal and IVADO: no 2027 dated event.

French-language lanes were opened: Collectif MTL, Centre humaniste, Mon Loft Privé, Maison Tela, Kawalees, Ralia, CSSDM and the Quebec statutes.

## 6. Access

Full (12 h yes): 5 — Studio Cuero 07:00–22:00; IMAGEMOTION 08:00–03:00; Kawalees 12:00–24:00; Carnegie 08:00–22:00; THE HOOK 08:00–22:00.
Floor only (8 h yes, 12 h no): 2 — Juniper 08:00–18:00 weekend (10 h cap); Loft108 full day 09:00–17:00 (8 h cap).
Shorter: 0. Unknown: 25.

Every full yes cites a captured published interval: Studio Cuero’s “Studio hours 7:00am - 10:00pm”; IMAGEMOTION’s “Day Rentals (8am - 5pm) Evening Rentals (5pm - 3am)”; Kawalees’ three consecutive four-hour blocks 12–4, 4–8, 8–12; Carnegie and THE HOOK’s Tagvenue `openingHoursSpecification` 08:00–22:00.

Centre humaniste’s former 12-hour yes was an appointment block: the operator prices 4-, 8- and 12-hour rentals but publishes no fixed clock interval, so both windows are downgraded to unknown. No other venue gained a yes from opening hours or prose.

## 7. Facts, inference and uncertainty

Sourced facts: addresses and portraits, coordinate tiers, photo rights/placement, statutory holiday names and dates, school-board dates, event dates — each stored with a source URL, locator and check date.

Inference (labelled in the store): coordinate tier assignment from the returned place; event relevance/kind; access state where the interval is a booking platform’s rather than the operator’s prose.

Uncertainty: CNESST unread; CSSDM break dates not printed in the extracted PDF; 2027-28 school editions unpublished; four address claims without a verbatim line; Carnegie/THE HOOK intervals platform-published; 17 venues without a cleared room photo; only three 2027 events exist on organiser pages.

## 8. Verification

- `city_store.py --check` → `OK: ... (schema city-store/1, 32 venues)`.
- `build_ranking(store, "2026-11-26")` → `city-ranking/1`; 25 scored rows + 7 lead rows = 32; `sequence` 32; `counts` open 25, leads 7, closed 0; 0 adjudication flags.
- Render: `city_page.py --store ... --out ~/.hermes/profiles/jnr-research/cache/scratch/mtl-r2/montreal-r2.html` → 1,569,679 bytes, exit 0, 32 `data-venue-id` rows, declared-gaps section present.
- Loss: `r2-loss-report.json` is a join, not a count — 32/32 venues retained (0 dropped, 0 added), 84 field-level changes, 0 unexplained field losses; the 48 inherited withheld photo URLs disposed 4 cleared / 42 still withheld / 2 dropped with venue→URL pairs; 2 pre events retained, 1 added, 0 dropped; 18 holiday rows retained, 4 added, 0 removed.
- Source yield: every `sources_consulted` row carries `yield_count`; the sum is 3, equal to the stored event count; duplicate lanes keep `preserved_event_links` without double-crediting.
- Claims: 876 claim IDs, 0 duplicated; all 32 coordinate claims carry provider, query, checked_on, returned_place, match_evidence and request_url; all 7 access-yes rows carry a published quote.
- IDs: every venue, event and photo key keeps the `mtl-` prefix; no duplicate photo URL within a venue.
- Scope: no file outside `research/montreal/` changed by this run; no summary HTML, home page or manifest written.

## 9. Artifacts

- `research/montreal/city/city.json` — candidate revision-1 store.
- `research/montreal/city/r2-loss-report.json` — pre→post loss disposition (join).
- `research/montreal/city/holiday-supplement.json` — dated Montreal-side holiday layer.
- `research/montreal/city/geocode/` — 32 raw Nominatim responses plus refused-lookup variants.
- `research/montreal/city/captures/` — operator pages, event lanes, holiday PDFs and texts.
- `research/montreal/city/photo-specs.json`, `photo-records.json` — photo provenance.
- `research/montreal/city/event-matrix.json` — 54-cell event matrix.
- `research/montreal/city/r2-loss-report.json` — pre/post loss disposition.
- `research/montreal/city/build_store.py` and companion scripts — reproducible build.

## 10. Memory note

Per the card, `memory_bank.md`, `memory_archive.md` and `.hermes.md` were not written. Manager action: record the R2 result in the project bank if this run changes project state.
