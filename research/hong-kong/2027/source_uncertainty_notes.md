# Source uncertainty notes — Hong Kong 2027 research run (accessed 2026-11-28)

This file records what could not be read, what conflicting sources said, and what stays unknown. It is the companion to `evidence_summary.md` (what was found) and `captures/INDEX.md` (what was saved).

## 1. Platform lanes

- **Peerspace** — `https://www.peerspace.com/s/hong-kong` returns HTTP 403 to curl and a Cloudflare "Just a moment…" challenge to headless Chromium. Capture: `lane_peerspace_hong-kong_blocked_cloudflare.html`. Disposition: blocked; no Hong Kong count obtainable.
- **Tagvenue** — the site opens (HTTP 200) but has no Hong Kong city page: `https://www.tagvenue.com/hk` and `https://www.tagvenue.com/hk/hong-kong` both return HTTP 404, and the home page names no Hong Kong coverage. Capture: `lane_tagvenue_home_no_hk.html`. Disposition: nothing there (0 Hong Kong results).
- **Eventective** — the root opens (HTTP 200) with no Hong Kong inventory; `https://www.eventective.com/hong-kong/`, `/asia/` and `/search/?q=Hong+Kong` all return HTTP 404. Capture: `lane_eventective_root_no_hk.html`. Disposition: nothing there (0 Hong Kong results).
- **Venue Report** — `/venues/hong-kong/` returns HTTP 403 to curl; headless Chromium lands on the Venue Report home page with zero mentions of Hong Kong. Capture: `lane_venuereport_hong-kong_redirect_home.html`. Disposition: nothing there (no Hong Kong section).

## 2. Bot walls, dead URLs and unreadable prices

- **Cyberport** — `https://www.cyberport.hk/en/facilities/conference_exhibition_centre/` and `/en/event-venue-space/` both return HTTP 403 to curl and to headless Chromium (Cloudflare). Captures saved. Cyberport therefore has **no venue record** in this run; the August 2026 record cited a third-party page (`hkmice-venue.weebly.com`), which is not the operator's own page.
- **Hong Kong Science Park price card** — the MICE charges are published only as a PDF (`hkstp_mice-rate-card.pdf`); this environment has no PDF text extractor (`pdftotext` absent), so no HKSTP figure is recorded. HKSTP is a `lead` with a cost_unknown question and a note that the rate card is a PDF.
- **HKTDC event calendar** — `https://event.hktdc.com/en?eventFormat=Exhibition&location=hk` returns HTTP 403 to curl and an empty document to headless Chromium. Individual HKTDC fair pages (`hktdc.com/event/hkbookfair`, `/innoex`, `/hkelectronicsfairse`, `/hktoyfair`) open but print no 2027 dates in their text. **No HKTDC 2027 dates are asserted anywhere in this package**, even though third-party sources list them.
- **Dream Impact** — plain HTTP requests to `dreamimpacthk.com` return HTTP 502; the page renders correctly in headless Chromium and the rendered DOM is the capture.
- **ebspace.hk** — the search result URL `https://ebspace.hk/pages/meeting-room` returns HTTP 404; the venue was not pursued further.
- **The Hive Kennedy Town** — a search-engine snippet quotes "Studio: $1200 per hour"; the live page publishes no event-space rate (only meeting-room and day-pass rates). The snippet is **not** used as evidence.
- **AMO** — the operator's own page publishes capacities but no price. An indicative rate (about HK$1,100/hour for Room A+B at weekends) exists only on its Common Room listing, so the cost is null and the figure appears inside a verification question, not in a cost field.
- **Good Lab** — the page prints a bare `$` and its Webflow currency setting declares USD; the rate is not converted.
- **Dream Impact** — the rate table prints `$2,140 / $2,415 / $2,675` with no currency marker; recorded as HKD with a confirm-currency question.

## 3. Conflicting sources

- **Consensus Hong Kong 2027** — the organiser FAQ says "Feb 2-3, 2027"; several third-party listings say 1-3 February 2027. The record uses the organiser's dates (2027-02-02 to 2027-02-03) and carries a question about 1 February.
- **AI Tinkerers Hong Kong network size** — the captured chapter page says "281-city global network with 148,000+ members" in one block and the search snippet of the same site said "147,000+ members" elsewhere. Only the captured figure is used, and it is a global figure, not Hong Kong membership.
- **Art Basel Hong Kong venue** — the Art Basel landing page prints the dates but not the venue; Art Central's own page places Art Basel at HKCEC. The record says so explicitly rather than asserting the venue from the landing page.
- **Hong Kong Sevens venue name** — hksevens.com calls it "Kai Tak Stadium, Kai Tak Sports Park"; third-party copy sometimes says "Kai Tak Sports Park" as the venue. The record quotes the organiser.
- **Clockenflap 2027** — sources disagree (a festival listing says 4-6 December 2027; a TST calendar page says "early December 2027 — dates not yet confirmed"; a Facebook post mixes 4-6 and 5-7 December). No record is written.

## 4. 2027 editions with no organiser date (explicit unknown-date notes — never guessed)

These are real Hong Kong events whose 2027 editions are not yet dated on any organiser page captured today. They are **not** in `calendar_conflicts.json`, because that collection requires an ISO start date.

- **Hong Kong FinTech Week x StartmeupHK 2027** — `fintechweek.hk` shows only the 2026 edition (2-6 November 2026) plus a "Ready for 2027? Pre-Register" call with no dates; InvestHK's fintech portal is inviting an Expression of Interest for the **2027-2029 event organisation**, with submissions due 10 December 2026. Unknown date.
- **Hong Kong AI Week 2027** — `aiweek.hk` (rendered with headless Chromium) says "APRIL 2027 HONG KONG" with a countdown and "5 Locations 5000+ Attendees 50+ Countries/Economies 6 Tracks", but publishes no dates. Unknown date, April 2027 window only.
- **Digital Economy Summit 2027** — no 2027 edition found on an organiser page; the 2024 edition was held in April at HKCEC. Unknown date.
- **HKTDC 2027 fair calendar** (Book Fair, Food Expo, Electronics Fair spring/autumn, InnoEX, Watch & Clock Fair, Lighting Fair) — the HKTDC event calendar is bot-walled (HTTP 403) and the fair pages print no 2027 dates. Unknown dates.
- **Hong Kong Wine & Dine Festival 2027** — third-party pages publish "expected 28-31 October 2027" and explicitly say the Tourism Board has not announced it. Unknown date; not recorded.
- **Clockenflap 2027** — conflicting third-party dates; no organiser date. Unknown date; not recorded.
- **ETH Hong Kong 2027** — the event site still shows the 2023 edition (22-24 October 2023, Cyberport). Unknown date; not recorded.
- **AWS Summit Hong Kong 2027** — an AWS sponsorship prospectus preview (PDF) lists "Hong Kong May 26" for 2027 but says final dates are released on 8 December 2026; the public AWS Summit page still shows the 2026 edition (17 June 2026). The PDF could not be read here, so the date is not recorded.
- **Hong Kong Techathon+ 11th Edition Finale** — the organiser page dates the finale **28-31 January 2027**, but the organiser page does not state the AI topic that would justify a `related` classification, so it is noted here rather than recorded.

## 5. Venue facts that stay unknown

- **Saturday availability** — no Hong Kong venue in this sweep publishes a live 2027 calendar. Every record carries an availability question. TreeholeHK is the only one whose page states it is open Monday to Sunday including public holidays.
- **09:00-21:00 windows** — only Igather Central (24-hour opening) and AMO (24-hour opening) publish an access window that certainly covers a 12-hour day. Every other venue leaves the end time unknown.
- **Alcohol** — none of the sixteen venues states a licensing position. Each record carries a booking_terms question about serving alcohol; no hotel bar is treated as a yes, and no venue is recorded as alcohol-permitted.
- **Tax** — most published rates do not say whether tax or service charge is included; `final_quote` questions carry that.
- **Recording** — recording suitability is `likely_good` where a projector/screen and sound are described, and `unknown` where the page lists no AV at all (Dream Impact, PMQ).
- **Capacities** — several are venue claims rather than tested layouts: Igather (60-100), Dream Impact (200), The Hive Wan Chai (50-100 guests), The Wave (500), Good Lab (max 50 persons), Sheung Wan Civic Centre (150 seats), Ngau Chi Wan (30-70 seats). Only Garage Society (70 seated / 100 standing), TreeholeHK (50 seats), The Hive Kennedy Town (50 seated / 80 standing) and Banyan (20 seated / 60 standing) publish a layout-specific number.

## 6. Coordinate lookups

- Coordinates come from Nominatim (OpenStreetMap) address search, one saved JSON per venue, with the query URL recorded in each venue's `evidence.geo`.
- The two venue captures that were saved empty in the first pass (`geocode_treehole_wanchai.json`, `geocode_thewave.json`) were re-fetched on 2026-11-28 from their recorded query URLs and now hold the raw response: Treehole 22.2778363 / 114.1768740, The Wave 22.3092741 / 114.2251595, matching the stored coordinates.
- **Nearest MTR station and walking time.** Ten records carry an `evidence.nearest_mtr` line in this pass: the nine the review listed, plus Dream Impact, which the first pass had also left without a station. Three rest on the operator's own words: The Wave ("4 Hing Yip Street, Kwun Tong, Hong Kong (MTR Exit B1)" and "Short walk from MTR station"), Good Lab ("just 2-min walk from MTR station" in Lai Chi Kok) and Dream Impact (image alt/title "距離荔枝角地鐵站僅 3 分鐘路程", 3 minutes' walk from Lai Chi Kok MTR). The other seven are estimates: the station was resolved by a separate Nominatim lookup saved as `geocode_mtr_<station>.json`, and the walk time is `1.3 x straight-line distance / 80 m per min`, rounded. These are labelled as coordinate estimates in the record, not operator claims. Nine station lookups were saved in total: **Wan Chai, Central, Kwun Tong, Choi Hung, Kennedy Town, Sheung Wan and University** supply the seven estimates, while **Lai Chi Kok** (the Good Lab and Dream Impact distance checks) and **HKU** (The Hive Kennedy Town's secondary station, ~620 m) are cross-checks rather than estimate bases.
- Two operator claims are not corroborated by the stored coordinates: Good Lab's "2-min walk" measures ~710 m straight-line from Lai Chi Kok Station (~11-12 minutes on the formula above), and Dream Impact's "3 分鐘" measures ~688 m (~11 minutes). Both are recorded as operator claims needing confirmation, not as measured walk times.
- Hong Kong Science Park has no walkable station: University Station (East Rail) is ~1.5 km straight-line and the operator's own "Transportation" section names no station or shuttle time, so the record carries a distance only and leaves access to confirmation.
- Eight lookups resolved to a building (星光行 Star House for AMO, Tower 535 for Garage Society Causeway Bay, 23 Luard Road for The Hive Wan Chai, Hong Kong Science Park for HKSTP, Hip Shing Hong Centre for Igather Central, Ngau Chi Wan Municipal Services Building for the civic centre, Glimpse PMQ for PMQ, Sheung Wan Civic Centre for SWCC); the other eight resolved to the street or the block (Smithfield Road for The Hive Kennedy Town, Hing Yip Street for The Wave, Johnston Road for TreeholeHK, Lockhart Road for Garage Society Wan Chai, Castle Peak Road for Good Lab, Cheung Sha Wan Road for Dream Impact, Hoi Chak Street for Banyan, Hoi Yuen Road for Igather Kwun Tong). Those are street-level fixes, accurate to roughly a block, and are labelled as such here rather than presented as rooftop coordinates.
- The Wave's coordinate is the Hing Yip Street carriageway; the building sits on the same block.
- No coordinate was estimated by eye and no lookup failure was silently filled in.

## 7. Community uncertainty

- Meetup hides the year on events in the current year. Where a date appears without a year ("Wed, Nov 25"), the year is established by the weekday-day pair matching 2026; that reasoning is written into each record's `uncertainty_notes`.
- Four records are `intermittent` rather than `active` for evidence reasons: Open Source Hong Kong (newest listed meetup 2025-12-09, no 2026 entry), Women in Web3 HK (one past event dated 14 June with no year), Bitcoin Association of Hong Kong (one past event with no date at all) and StartmeupHK (a government programme and events calendar rather than a membership group).
- No group is marked `dormant`: the August 2026 run's dormant records (AISHK, 852Web3, HKDSS) were not re-verified today and are therefore **not carried forward**, rather than being re-asserted.
- Three records carry `cohost_open: true`, each on its own-page language: HKML (own-page call for speakers and sponsors), Prompt in Progress (own-page partner list and the statement that AI Tinkerers Hong Kong is "our focused technical community") and OSHK (its own "OSHK x HKPUG" joint-event listings). No co-host relationship is claimed for any group.
