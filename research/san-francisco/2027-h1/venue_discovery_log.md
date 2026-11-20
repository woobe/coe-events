# Venue discovery log — San Francisco, 2027 H1

Research date: 2026-11-20. Window: 2027-01-01 through 2027-06-30. Target: 50-125 people, Saturday, about 8 hours (09:00-17:00).
City: San Francisco, United States. Region: North America. Currency: USD (no conversion applied; every source publishes in USD). Timezone: America/Los_Angeles.
Output: `venues.raw.json` (16 records, 15 with coordinates, 1 withheld).

## Method

Discovery ran as a widening sweep rather than a single keyword search, because the last three city passes that searched only "event space" produced an all-lead shortlist:

1. Commercial/creative event spaces with published rate cards (Splacer, Peerspace, Eventective listings; SoMa and Mission lofts and galleries).
2. Non-profit and community arts venues that publish rental rates (Root Division, SOMArts, CounterPulse, The Lab, Brava, The Women's Building, Ruth Williams Opera House, Gray Area).
3. Theatres and black-box spaces with full-day weekend rates (The Marsh, Z Space, Alliance Française).
4. Institutional and campus venues (Mission Bay Conference Center at UCSF, USF McLaren, UC Law SF).
5. Platform coverage check before platform searching.

Each candidate was then opened on its own site and the rate table, capacity statement and access policy were read directly. Search-result snippets were used only to find the page, never as the final evidence.

## Platform coverage

`plan-event/references/venue_platforms.json` registers three active platforms — giggster, space-cloud and tagvenue — and `san-francisco` appears in none of their coverage lists (giggster: new-york-ny-us; space-cloud: seoul-kr; tagvenue: boston-ma-us, new-york-ny-us). No registered platform covers San Francisco, so every venue record is a plain web source (`source_type` omitted; no platform provenance claimed). Peerspace and Splacer surface San Francisco inventory but are not registered platforms, so they were treated as ordinary web sources and are noted as such.

## Sources that could not be read on 2026-11-20

- Mission Bay Conference Center at UCSF (campuslifeserviceshome.ucsf.edu): Cloudflare "Performing security verification" interstitial on both curl and headless render.
- Tides Converge (tides.org/converge): Cloudflare challenge.
- The Midway (themidwaysf.com/venue-rental): bot check ("Hold up while we check your connection").
- Noisebridge wiki (noisebridge.net): Anubis proof-of-work wall.
- Mission Cultural Center for Latino Arts (missionculturalcenter.org): the domain reports "Squarespace - Website Expired".
- Splacer (splacer.co venue pages): empty response body.
- Peerspace live listings: Cloudflare challenge on every attempt. The Common Space record was read through a Wayback Machine snapshot (web.archive.org/web/20260406005213) and is labelled as archived evidence.
- somarts.org and counterpulse.org rate-limited the first requests (HTTP 429); both were recovered with a delayed headless render.
- Mechanics' Institute (milibrary.org/venue-rental) and UC Law SF (uclawsf.edu/alumni-reception-center) returned 404/calendar pages rather than rental pages; neither was pursued further, so no rate is claimed for either.
- Public Works (publicsf.com) was read but publishes no rate and totals 1,000 people, so it was dropped rather than padded into the list.

These are recorded so the next pass does not re-burn time on the same walls, and so the reviewer can see which absences are access failures rather than "no such venue".

## Cost basis discipline

Every priced record states the exact tier used and what it excludes. No currency conversion was needed — every venue publishes in USD — so `cost_local_currency` is USD and the rate basis is "no conversion applied".

Two priced cost bases are in use, plus an explicit unknown state:

- `published_rate` (6 records): the venue publishes a package, event or day price. Not all six cover eight hours: SOMArts (day-long access) and The Marsh Mainstage and Studio (Friday-Sunday full-day) do, while Root Division's package is 5.5 hours, Alliance Française's is a four-hour daytime tier, and Ruth Williams publishes no defined rate unit.
- `estimated_from_rate` (4 records): the venue publishes an **hourly** rate and we multiply by eight hours. These carry `hourly_rate_usd`, `estimated_hours: 8`, `cost_rate_unit: "hour"` and a `rate_estimate_note` naming the source, the tier used and the exclusions. The arithmetic is `hourly_rate_usd × 8 = estimated_cost_usd`.
- `unknown` (6 records): no price is published anywhere on the venue's own site; these carry a `cost_unknown` question and null amounts. Null is never treated as free.

Per-venue basis, tier and exclusions:

- SOMArts — `published_rate`, USD 4,549 is the **Essentials package starting price** (100-150 guests), which includes day-long (8 hour) access, full audio and lighting package, audio technician and set-up/load-out labour. Excludes non-profit discounts, security (priced by anticipated attendance) and the refundable damage deposit.
- Root Division — `published_rate`, USD 1,800 is the **Front & Rear Galleries package** and covers 5.5 hours (4 hour event + 1.5 hour set/clean). Excludes extra hours (USD 150/hour), projector (USD 100), PA (USD 150), cleaning when food is served (USD 250), insurance.
- Four One Nine — `estimated_from_rate`, **USD 650/hour × 8 hours = USD 5,200** for Middle Gallery Extended (40-100 people), from a rate card titled "Jan 1-Dec 31, 2026" with a 4-hour minimum and "seasonal rate may apply". Excludes AV, staffing, cleaning, security and any seasonal uplift; 2027 pricing is unconfirmed.
- CounterPulse — `estimated_from_rate`, **USD 50/hour × 8 hours = USD 400** at the published "Main Stage Private Event" rate. Excludes staffing and insurance, which the page does not itemise.
- The Women's Building — `estimated_from_rate`, **USD 165/hour × 8 hours = USD 1,320** for the Audre Lorde Room, and that rate is printed as a weekday (Monday-Friday 9-5) rate with no Saturday rate published.
- The Marsh — `published_rate`, USD 2,500 (Mainstage) and USD 2,000 (Studio) are the published **Friday-Sunday full-day (>4 hour)** rates. Both exclude the required Marsh Arts Representative (USD 40/hour), security when over 100 people or alcohol is served (USD 40/hour), AV (USD 100 plus USD 40/hour technical director) and optional USD 100/hour set-up, break-down and cleaning.
- Ruth Williams Opera House — `published_rate`, USD 900 is the published **"Base Rate Main Theater"**, with a five-hour event minimum stated but no defined rate unit. Excludes a 3% service fee, a 25% admin fee, cleaning (USD 350 indoor), projection from USD 950, security at USD 50/hour per guard.
- Alliance Française — `published_rate`, USD 800 is the **private-event daytime base rate**, with front-desk staffing mandatory at USD 60/hour and a USD 200 catering surcharge if food is served.
- Common Space — `estimated_from_rate`, **USD 165/hour × 8 hours = USD 1,320** from the archived Peerspace listing, which also states a four-hour minimum and a USD 250 security deposit. Excludes the deposit, cleaning and platform fees.
- The Lab, Brava (Lobby and Studio), Z Space (Lobby and Steindler) and Gray Area publish no price at all: `cost_basis: unknown` with a `cost_unknown` question rather than an invented figure.

## Tier counts (scorer output, not hand counts)

Counts come from the repo's own scorer, run on this file on 2026-11-20. Command:

```
python3 plan-event/scripts/score_venues.py \
  research/san-francisco/2027-h1/venues.raw.json \
  --output <scratch>/sf_scored.json \
  --budget-usd 5000 --target-attendance 50 \
  --event-date 2027-03-06 --event-duration-hours 8
```

Output, verbatim:

```
eligible: 0
shortlist_ready: 14
lead: 2
top selectable: Alliance Francaise de San Francisco - Theater (score 0.7255, tier shortlist_ready)
```

So the shape is **0 eligible / 14 shortlist_ready / 2 lead**, of 16 records.

- `lead` 1 — CounterPulse. Its rate is published and cheap, but the seated capacity (108) exists only in third-party venue directories; CounterPulse's own rentals page publishes rates and spaces and no capacity figure. Capacity is a material field, so the honest tier is `lead` with a specific `capacity` question.
- `lead` 2 — Common Space. Its coordinates are null because Peerspace masks the street address, and a `location` verification question is a **material** kind under the schema, so the venue cannot be selectable until an address is obtained. This is the second lead and the reason the earlier "13 shortlist_ready / 1 lead" figure in this log was wrong.
- `shortlist_ready` (14) — every other record: a published price or an evidenced no-price state plus an evidenced capacity, with soft gaps only (Saturday availability, screen, Wi-Fi, access window, final quote, terms, room assignment).
- `eligible` — none. No venue evidences Saturday availability, a written all-in quote, a confirmed screen and Wi-Fi, and a window supporting 09:00-17:00 simultaneously.

The full scored order, for reference: Alliance Française 0.7255, Root Division 0.7105, The Marsh Studio 0.5950, The Marsh Mainstage 0.5750, The Women's Building 0.5547, The Lab 0.5450, Gray Area 0.5325, Brava Lobby 0.5075, Brava Studio 0.5075, Z Lobby 0.5075, Four One Nine 0.4075, Z Steindler 0.4000, Ruth Williams 0.3965, SOMArts 0.3705. Every record carries `stale_evidence` because research is 106 days before the 2027-03-06 scoring date; that is a freshness flag, not a quality finding.

Oversized rooms are carried, not eliminated. `score_venues.py` flags `oversized_capacity` only above `CAPACITY_PARTIAL_MAX = 160`, so on this file the flag lands on Ruth Williams Opera House (300) and Z Space Steindler (236) and on nothing else. The Lab (150 seated) and SOMArts (150) exceed the 125 comfort ceiling but are not flagged; all four remain visible evidence for Joe rather than being silently dropped.

## Community and non-profit versus commercial

Marked as community/non-profit or publicly-owned rather than commercial event venues. The basket is a rental-posture classification, not a verified 501(c)(3) register: it holds nine organisations across ten venue records (Brava has two rooms). Z Space is a non-profit arts centre with a commercial rental programme and no published rate table, so it appears in the commercial list below; counting it would make ten organisations and 12 of 16 records.

- SOMArts Cultural Center — non-profit arts organisation operating a city-owned building (the rental FAQ names the City and County of San Francisco as an additional insured because SOMArts operates in a city-owned building).
- Root Division — non-profit arts organisation.
- CounterPulse — "award-winning art and community facility" offering "below-market rates".
- The Women's Building — non-profit women's community building, explicitly inviting mission-aligned non-profits.
- Ruth Williams Opera House — 501(c)(3) community opera house.
- The Lab — non-profit experimental art and performance space.
- Brava Theater Center — performing-arts non-profit.
- Gray Area — art-and-technology non-profit in the Grand Theater.
- Alliance Française — cultural centre; its record evidences the daytime private-event rate (USD 800) and a separate daytime nonprofit tier (USD 550), neither of which verifies the organisation's own tax status.

Commercial or private event venues: Four One Nine, The Marsh, Z Space (non-profit arts centre with a commercial rental programme and no published rate table), Common Space (private Peerspace host).

## Coordinate provenance

15 of 16 records carry a latitude/longitude pair taken from an OpenStreetMap Nominatim lookup performed 2026-11-20, each with its `openstreetmap.org` object URL in `evidence.geo`. Nominatim results were matched against the venue's own published street address; all 15 matched the expected street and postcode.

Common Space is the exception and carries null coordinates by choice. Its Peerspace listing masks the exact address until booking and publishes only "Union Street, San Francisco Marina District, 900 sqft". A Marina-district centroid would have produced a plausible-looking pin that is not the venue, so the pair is null and a `location` question stands in its place. This is the only record without a map position, and it is why that record is a `lead`.

## Conflicts found while researching

- Root Division publishes two different price sheets on its own domain: the live rental page lists Front & Rear Galleries at USD 1,800 (Option 1 USD 750, Option 3 USD 2,250), while `rootdivision.org/sites/default/files/files/venuerental_faq_1131.pdf` lists the same galleries at USD 1,200 (Option 1 USD 500, Option 3 USD 1,500). The live page is treated as current; the difference is flagged in `evidence.observed_facts`.
- The Women's Building contradicts itself on weekend access: the Audre Lorde Room rate line reads "Monday to Friday reservations only between 9 am and 5 pm", while the same page states the latest event end is "10 PM Friday through Sunday". Both statements are recorded and the contradiction becomes the first verification question.
- GDC 2027 is March 1-4 on the Moscone Center's own page; one aggregator says March 1-5. The Moscone page is treated as authoritative and the discrepancy is noted.
- Four One Nine's rate card is explicitly a 2026 card; a 2027 rate cannot be assumed.

## What this pass could not verify

- No 2027 Saturday availability, hold, or written quote from any venue.
- Wi-Fi for 13 records and screen for 10. The two fields are recorded separately because they disagree: `wifi_status: confirmed` appears on three records only (The Lab, Common Space, Gray Area, the last on fiber internet), while `screen_status: confirmed` appears on six (Root Division, Ruth Williams Opera House, The Lab, Z Space Steindler, Alliance Française, Common Space).
- Whether any venue's 8-hour window comfortably contains set-up and load-out on a Saturday morning.
- Real all-in totals including staff, security, insurance and cleaning for every venue except where the page itemises those fees (The Marsh, Ruth Williams, Alliance Française, SOMArts, Root Division).
- The street address of Common Space, and therefore its map position.
