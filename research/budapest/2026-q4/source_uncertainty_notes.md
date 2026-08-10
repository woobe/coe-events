# Source Uncertainty Notes — Budapest Run A v2.5 (budapest-hu)

Prepared 2026-08-10 by the Run A v2.5 research card (evidence-bound venue + calendar
research only; no scoring/assembly here beyond the deterministic scorer run, no
speakers/communities/outreach, no bundle or summary generation).

## Currency handling (documented rate)

- HUF-to-USD: European Central Bank euro foreign exchange reference rates,
  retrieved 2026-08-10 from the ECB daily feed
  (https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml): EUR 1 = USD
  1.1555 and EUR 1 = HUF 363.65. Computed USD 1 = HUF 314.71 (363.65 / 1.1555),
  i.e. 1 HUF = USD 0.00317751. This is a date-stamped planning conversion, not a
  bank or venue quote.
- EUR-to-USD for the two venues that publish euro rates (KAPTÁR Coworking, New
  York Palace): EUR 1 = USD 1.1555 from the same ECB feed.
- All local amounts are preserved in their published currency and code (HUF or
  EUR). USD estimates are analyst conversions labeled in evidence.inference and
  rate_estimate_note, and carry final_quote questions. +VAT and weekend
  surcharges remain verification questions where the page does not show them
  included (Hungarian VAT is 27%, but no venue page in this pass stated its VAT
  inclusion on the specific published rate, so nothing was assumed).

## Trusted-venue match result

- references/trusted_venues.json contains two budapest-hu seeds:
  - tv-02 Impact Hub Budapest (Community & Event space 20-50, Great Hall
    100-150, Grund 20-40; Babér utca 1-5) — RE-VERIFIED from the current
    official booking page (budapest.impacthub.net/book-your-event-space/,
    HTTP 200, 2026-08-10). Included as two candidate records (Community &
    Event space, Great Hall), status stays unknown; not marked used.
  - tv-03 Loffice Budapest (Maxi Event Room 50-60 at 18,000 HUF/hr +VAT, 'A'
    event space up to 50 at 21,500 HUF/hr +VAT; Paulay Ede st. 55) —
    RE-VERIFIED from the current official event-spaces page
    (loffice.hu/budapest/en/event-spaces/index.php, HTTP 200, 2026-08-10).
    Included as two candidate records (Maxi Event Room, 'A' event space),
    status stays unknown; not marked used.
- Both seeds now have current claim-bearing evidence, so they are scored
  candidates like any other record (not treated as trusted/used).

## Calendar flags (6 records, all informational for Joe)

- SPAR Budapest Marathon 2026 (official marathon.runinbudapest.com): Oct 10-11,
  2026. Candidate Saturday 2026-10-10 falls inside the festival weekend. Severity:
  high logistics awareness; FLAG only, never an elimination.
- IEEE Tech Summit: Ethical AI 2026 (official techsummit.ieee.org/ethical-ai-2026/):
  Oct 1-2, 2026, Budapest. Severity: medium AI-ecosystem cluster before 10-03.
- ScaleupFest 2026 (official thescaleupfest.com): Sep 16-17, 2026, Budapest.
  Severity: low, before 09-19.
- AI Forward '26 (official techforward.hu): Oct 21, 2026, MVM Dome. Severity: low.
- EMNLP 2026 (official 2026.emnlp.org): Oct 24-29, 2026, Budapest. Candidate
  Saturday 10-24 falls inside; FinNLP-2026 workshop day Oct 28
  (sigfintech.github.io/finnlp2026). Severity: medium.
- MeOut Summit 2026 (official meoutsummit.com): Nov 25-26, 2026, Budapest
  (Akvárium Klub per listings). Informational November awareness only.
- Out-of-window discovery (NOT stored as a record): AI Summit Budapest 2026 is
  Sept 7-8 (official aisummitbudapest.hu embeds 2026-09-07/08 and 'szeptember
  7-8.'), before the 09-15..12-15 coverage window; noted here as an
  early-September signal, not a candidate-date conflict.
- Budapest Fintech Week 2026: official Luma page (luma.com/wjxqell7) confirms the
  event returns in 2026 but publishes no dates yet (program TBA); 2025 edition was
  Dec 4-5. Recorded as a recurring Nov/Dec signal, not a dated conflict.

## Venues (21 records in venues.raw.json)

### Direct official venue pages (fetched live 2026-08-10, HTTP 200 unless noted)

- Impact Hub Budapest (budapest.impacthub.net/book-your-event-space/): Community &
  Event space 20-50 with weekend exclusive hire; Great Hall 100-150 with built-in
  projector and 2 free mics + speaker; Grund 20-40 with 75" smart TV
  videoconference kit. WiFi confirmed explicitly only for Grund; Community/Great
  Hall WiFi recorded unknown with questions. No numeric prices published
  (cost_unknown). Address 1131 Budapest, Babér utca 1-5.
- Loffice Budapest (loffice.hu/budapest/en/event-spaces/index.php): Maxi Event
  Room 18,000 HUF/hr +VAT up to 50-60; 'A' event space 21,500 HUF/hr +VAT up to
  50; Mini 7,500; Midi 9,500; B/C 8,500; D/E/F 10,500. Secure WiFi listed; Full AV
  equipment at bespoke price (screen recorded unknown for Maxi/'A' with
  questions). Address Paulay Ede st. 55, 1061.
- KAPTÁR Coworking (kaptarbudapest.hu/en/meeting-rooms/): Event space 25-50,
  available after 6pm weekdays or weekends; weekend full day (8h) 360 EUR +VAT
  (= 415.98 USD at ECB rate), half day 210 EUR +VAT, workday 2h min 175 EUR +VAT;
  WS1 10-24 / WS2 10-30 with projector + electric canvas. Enterprise WiFi
  confirmed. Prices in EUR (documented). Address 4. Révay köz, 1065.
- bee@work ANKER (bee-at-work.hu/en/meeting-room-rental): Conference Room up to
  50 (lower ground) HUF 12,000/hr / HUF 72,000/day gross (= 228.78 USD at ECB
  rate); meeting rooms for 2-60 people; AV + reception included; office hours
  Mon-Fri 9-17, weekend availability unstated (event_window question). Address
  Anker köz 2-4, 1061.
- Eco Office (eco-office.hu/en/meeting-rooms/): Large Meeting Room 2-14 at
  6,000-8,000 HUF/hr, projector + projection screen, Gigabit WiFi, 24/7, no max
  booking time. Room alone seats max 14 (lead with combination question). Address
  Izabella utca 68/b, Budapest.
- Danubius Hotel Hungaria City Center (danubiushotels.com meetings page): 12
  event rooms, capacities 60-500 (largest room 455 m2). No prices/AV/WiFi on the
  page (cost/screen/wifi questions). Address Rákóczi út 90, 1074.
- Millenáris (2023.millenaris.hu/en/venue-rental/ + Budapest Party Service page):
  Great Hall (B) ~1,200-1,500, Glass Hall (D) ~600-800 (1,680 m2), National Dance
  Theatre; open daily 06:00-23:00; quote-based, no price/AV/WiFi published.
  Oversized for 50; lead/awareness.
- Budapest Music Center (bmc.hu/en/about-us): Corner Hall 61 m2 (40 theatre / 30
  rectangle), Rooftop Hall 112 m2 (60 theatre / 40 rectangle), Concert Hall 285 m2
  (295 theatre), built-in sound/projection/lighting. No prices published
  (rendezveny@bmc.hu). Address Mátyás utca 8, 1093.
- Winehub (winehub.hu/venue-rental/): former Goldberger factory, capacity
  200-250, in-house kitchen/bistro/fine dining catering, quote-based, no
  price/AV/WiFi. Oversized; lead/awareness. Óbuda, Budapest.
- Akvárium Klub (akvariumklub.hu/en/event-venue/): Aranyhall Conference Center
  (Main Hall + Glass Hall, each 100 seats, partitionable, separate wing), event
  capacities 50-1,000; total venue 2,100; bistro; personalized offers within 24h;
  no price/AV/WiFi published. Erzsébet tér 12.
- New York Palace (newyorkcafe.hu/en/event-meeting/): 12 rooms up to 600 guests;
  FULL-DAY CONFERENCE PACKAGE EUR 115/person/day (= 6,644.13 USD for 50 at ECB
  rate, OVER the USD 5,000 soft budget) incl. room, coffee breaks, business
  lunch, built-in LCD projector and screen, flipchart; min 15 guests. Address
  Erzsébet körút 9-11.
- Brody House (brody.house/events): boutique hotel/gallery with private-event and
  space rental (events@brody.house); no capacity/price/screen/WiFi published
  (lead). Bródy Sándor utca 10, 1088.
- Várkert Bazaar (Budapest Party Service venue page): Multifunctional Event Hall
  900 m2 (500-800), Screening Room 130 m2 (80-120), Foyer 880 m2, Foundry
  Courtyard outdoor 200-500; exclusive catering partner; quote-based, no
  price/AV/WiFi. Ybl Miklós tér 2-6.
- KUBIK Coworking (kubik.hu/en/): meeting rooms bookable by hour/day; high-speed
  WiFi; reception weekdays 9-18; 24/7 member access; no capacity/price/screen
  published on the reviewed page (lead). Jászai Mari tér 5-6, 1137.
- Create.26 (create26.hu/en/event-space/): Event Space 10-150; Full House 90
  theatre, South 50 theatre, North 25 theatre; 1 multimedia projector, sound
  system, streaming/live/video-recording support; 'Based on a unique offer' (no
  numeric price). Nagymező utca 26, 1065.
- Pesti Vigadó (vir.vigado.hu/web/en/135): Ceremonial Hall (second floor) for
  concerts, conferences, receptions, galas; also Makovecz Hall, Northern/Southern
  Halls, Sinkovits Imre Chamber Theatre; no capacity/price/AV/WiFi on the
  reviewed pages (lead). Vigadó tér 2.
- A38 Ship (a38.hu/en/event-organizing): Bistro standing 110/seated 90;
  Schweppes Terrace standing 80/seated 50; Concert Hall 192 m2 standing 400/seated
  180-200; plus smaller halls; hot/cold catering, built-in sound/lighting, AV
  equipment; open Mon-Sun 8-22; quote-based, no price published. Petőfi bridge,
  Buda side.

### Booking-platform records (workin.space, fetched live 2026-08-10)

- Signature Budapest — MR 01 (Szervita square 8, 1052): listed in the 21+
  conference category; HUF 19,900/hr, HUF 111,173/day excl. VAT (= 353.25 USD at
  ECB rate); Wi-Fi/Screen/Reception amenities shown. Exact capacity NOT published
  on the listing (lead with capacity question).
- Regus Budapest First Site — Frankfurt room (Kossuth Lajos utca 7-9, 1053):
  listed in the 11-20 training category; HUF 10,900/hr, HUF 60,894/day excl. VAT
  (= 193.49 USD); Wi-Fi/Screen/Reception shown. Exact capacity NOT published
  (lead with capacity question).
- Both are corporate-center rooms likely below the 50-person target; kept as
  evidence-bound leads rather than deleted (no-padding rule honored).

### Discovery gaps (not fabricated)

- Mosaik coworking: coworkbooking.com lists it as permanently closed; excluded.
- MOM Kulturális Központ and Bálna Budapest: official pages were unreachable in
  this pass (TLS/connect failures); Hungarian-only pages out of the English-only
  scope anyway; logged as discovery gaps, not translated evidence.
- CEU / Corvinus university spaces: no public venue-hire page found in this pass;
  not recorded.
- Szent István terem (St Stephen's Hall, Buda Castle): reviewed as a museum
  tour/historic-hall page; no event-hire facts published on the English page;
  not recorded.

## Inference vs observed fact

- All estimated_cost_usd values are analyst conversions from page-published
  rates using the documented ECB 2026-08-10 rate, labeled in evidence.inference
  and rate_estimate_note; they are NOT quotes and carry final_quote questions.
- cost_basis "published_rate" is used only for page-published day/package rates
  (KAPTÁR weekend day, bee@work day, New York Palace per-person package,
  Signature/Regus day); "estimated_from_rate" is used only for hourly HUF rates
  (Loffice Maxi/'A', Eco Office) with 8-hour estimates matching the selected
  event duration.
- Venues with no published price keep cost null + cost_unknown question
  (Impact Hub, BMC, Winehub, Akvárium, Create.26, A38, Danubius, Millenáris,
  Várkert, Brody, KUBIK, Pesti Vigadó) — Joe's amendment 1: no price keeps a
  venue in consideration.
- Capacity_comfortable is the best published figure; capacity_basis records
  seated/venue_claim/unknown. Venues with null capacity are recorded as 0 with
  capacity_basis unknown (schema requires an integer), making them leads.
- Coordinates are Nominatim (OpenStreetMap) geocodes of the published addresses,
  recorded as source-supported map evidence (evidence.geo points at the venue
  page); they are planning aids, not venue-verified points.

## Scorer run (deterministic, no hand edits)

- Command: scripts/score_venues.py venues.raw.json --output venues.shortlist.json
  --budget-usd 5000 --target-attendance 50 --event-date 2026-10-03
  --event-duration-hours 8. (2026-10-03 is the plan's illustrative candidate
  date; Joe's actual date will be used at assembly/scoring time.)
- Result: eligible 0 / shortlist_ready 15 / lead 6. Top selectable: Loffice
  Budapest — Maxi Event Room (score 0.7792). Byte-identical on re-run.
- The shortlist file is scorer-owned; no hand edits were made to it.
