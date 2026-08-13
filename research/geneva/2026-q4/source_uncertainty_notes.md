# Geneva Run A (2026 Q4) — source uncertainty notes

Accessed/research date: 2026-08-13. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. This file is a local research artifact;
nothing here is a recommendation, elimination, or date commitment.

## 1. FX conversion basis

- All USD equivalents in this package use the ECB euro foreign exchange
  reference rate dated 2026-08-13 (EUR 1 = USD 1.1534; EUR 1 = CHF 0.9373),
  fetched 2026-08-13 from
  https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml.
  Derived rate: 1 CHF = 1.230556 USD (USD per CHF = 1.1534 / 0.9373).
- Converted amounts:
  - Impact Hub Geneva Grand Salon: CHF 950 / 4 hours published; modeled as
    CHF 237.50/hour -> USD 292.26/hour, 8h = CHF 1,900 -> USD 2,338.08.
  - Impact Hub Geneva Petit Salon: CHF 550 / 4 hours published; modeled as
    CHF 137.50/hour -> USD 169.20/hour, 8h = CHF 1,100 -> USD 1,353.61.
  - Salle communale de Plainpalais Salle des Assemblées: CHF 92/hour
    published (2024 municipal tarif), 8h = CHF 736 -> USD 905.69 (plus
    mandatory prep/cleanup ~CHF 102 -> ~USD 125.52; see venue record).
  - CERN Science Gateway: published daily fee range CHF 15,000-60,000; the
    minimum CHF 15,000 -> USD 18,458.34 is used as the cost figure (way over
    the USD 5,000 soft budget).
- NEVER invent a rate: any venue without a dated, published conversion basis
  keeps `estimated_cost_usd: null` with a confirm-cost question. This applies
  to Palexpo, Hotel N'vY, Warwick, Mövenpick, Decentral House (all
  inquiry-only pricing).
- Gap: the ECB 2026-08-13 reference is a dated published basis, not a live
  market rate and not a predictor of 2026 Q4; re-confirm at booking time.

## 2. Calendar uncertainty

- All calendar records were verified against official organizer pages
  (direct fetch on 2026-08-13): swiss-it-forums.tech + palexpo.ch (Swiss IT
  Forum(s)), ai-weeks.ch/events/geneva-hackathon (Geneva Hackathon),
  wto.org (WTO Public Forum 2026), ohchr.org (UN Human Rights Council 63rd
  session), palexpo.ch + aid-expo.com (AidEx 2026), bachatagenevafestival.com
  + palexpo.ch (Bachata Geneva Festival 2026), palexpo.ch (MEGALLOWEEN).
- ADJACENT CONTEXT ONLY (outside the 2026-09-15..2026-10-31 coverage window;
  never in-window assertions):
  - Fête de Genève is an August event — adjacent context only, never a claim
    that August is in research scope.
  - Geneva Digital Week / AI for Good Global Summit / WSIS Forum 2026 and the
    inaugural Global Dialogue on AI Governance ran 6-10 July 2026 (ITU,
    official) — major Geneva AI-governance activity but out of window.
  - ECCB 2026 / #GenevaLovesData (SIB, HUG, UNIGE) ran 31 Aug - 4 Sep 2026 at
    Geneva venues with the Datarium exhibition from 3 Aug at Parc des
    Bastions — out of window (adjacent early-September data-science activity).
  - Generali Genève Marathon 2026 was 9-10 May 2026 (official) — out of
    window (spring edition; no autumn marathon found).
  - Global Digital Collaboration Conference (GDC26), 1-3 Sep 2026 at Palexpo
    (official globaldigitalcollaboration.org) — before the coverage start.
  - IGF 2026 Second Open Consultations and MAG Meeting, 7-9 Sep 2026 at CICG
    (official intgovforum.org) — before the coverage start.
  - HPE Hackathon, 14 Sep 2026 at HPE Geneva Customer Innovation Center
    (ai-weeks.ch listing) — one day before the coverage start; not recorded.
  - Geneva AI Summit 2027 (Federal Council delegate Fabiola Gianotti
    appointed 2026-08-12, admin.ch) — 2027 event, referenced only as context;
    the Geneva Hackathon and Swiss AI Weeks pages note their own link to the
    2027 summit roadmap.
- Not recorded: digitalswitzerland forum 2026 (15 Sep 2026, Bernexpo BERN —
  not Geneva; the "Road to the Geneva AI Summit" branding refers to Geneva
  2027), Swiss Data Space Forum 2026 (28 Oct 2026, Prilly/Lausanne — Vaud,
  not Geneva), The Merge Film Festival (1-4 Oct 2026, Massagno/Ticino — not
  Geneva), Swiss AI Safety Days (7-8 Nov 2026 — outside window),
  TOKEN2049 Singapore / Blockchain Life Dubai (other cities).
- All calendar prose is date-neutral about Decentralized AI Day (v2.8/v2.9
  family): no scheduling-window, candidate-date, or preferred-date phrasing
  is stated anywhere in calendar records. Factual dates of the external
  events are preserved as evidence facts.

## 3. Venue uncertainty

- Impact Hub Geneva (ih-038): Tier-1 trusted resolver match (Up&Running,
  HUB, Geneva/CH/Europe). Unlike the Boston seed, the Geneva hub's own pages
  ARE current and claim-bearing (spaces page with Grand Salon CHF 950/4h and
  Petit Salon CHF 550/4h, Grand Salon room page with capacity/equipment,
  online booking system at geneva.impacthub.ch). Retained as a scored
  candidate (shortlist_ready) — but Saturday availability is UNCONFIRMED
  because the site footer states Monday-Friday 9h00-19h00 reception hours;
  the online calendar shows Mon-Sun days, so weekend booking must be
  confirmed via the event-space form (geneva.impacthub.ch/form/space-geneva).
  The 15% member discount and 6-month membership requirement for discounts
  may affect pricing for a non-member organizer.
- Salle communale de Plainpalais: the 2024 municipal tarif PDF is dated
  12.01.2024 — current 2026 rates need confirmation; screen/Wi-Fi inventory
  is not published; municipal booking conditions (association status,
  deposit, insurance per the municipal règlement) need confirmation. The
  grande salle (500 w/ tables) is oversized; only the Salle des Assemblées
  (100 w/ tables) is a fit. Prep/cleanup 1h before + 1h after at CHF 51/hr is
  mandatory per the tarif.
- Palexpo: rooms E/F/G (120 theatre each), K (230), L (108) on the mezzanine
  above rooms A/B/C with an 800 m² foyer; capacities and data sheets are
  published but no rates — quote-only. Rooms P-X and Alpha-Omega exist but
  were not examined in this pass.
- CERN Science Gateway (Meyrin): public venue-hire program evidenced by the
  January 2025 rate PDF (CHF 15,000-60,000/day; event days 08:00-24:00; AV +
  2 technicians included; catering not included). Retained conservatively as
  an over-budget lead per the plan's "CERN non-local unless evidenced as
  practically suitable" rule — the venue-hire program is practical-suitability
  evidence, but the price makes it impractical for the USD 5,000 budget.
  Meyrin is in the Canton of Geneva, ~20 minutes from the city centre.
- Hotels (N'vY, Warwick, Mövenpick): capacities/suites published, rates
  inquiry-only. N'vY Nolita (70 m², 50 pax) and Sausalito (2x65 m², up to 110)
  fit; Warwick Mont-Blanc max 105; Mövenpick has 19 rooms up to 800 but no
  per-room small-room capacity published. All remain leads pending quotes.
- Decentral House (Lancy-Pont-Rouge): Main Hall up to 120 guests theatre,
  4K projection, surround sound, live-streaming; rates inquiry-only; exact
  street address not published on the fetched pages (directory sources say
  Route des Jeunes area); also retained as a community hub record.
- coworkinggeneva.ch (event-space directory/platform: "Conferences &
  Seminars from CHF 950/day", "Workshops from CHF 450/day", Centre Ville
  Auditorium up to 200, Plainpalais Loft up to 120, Carouge Workshop Hall up
  to 80, Eaux-Vives Lakeside Room up to 60) is a PLATFORM, not the operating
  venue; per evidence policy its rates cannot support a venue record, so it
  is logged as a platform lead (unresolved) rather than retained.
- BFM (Salle Théodore Turrettini 1,000+ seats; Foyer up to 1,000) and CICG
  (up to 2,200 participants) are oversized for a 50-person event and are
  logged as rejected-oversized, not retained.
- Fongit (startup incubator at Campus Biotech B4 and Plan-les-Ouates HQ):
  hosts events (café-croissants, investor days, FONGIT-Life) but has no
  public venue-rental page or rates — logged as unresolved, not retained.
- La Muse Bouge (associative coworking, Rue Jean-Charles Amat 6, 1202 Genève,
  Mon-Fri 09-18): membership coworking only, no event-space rental page —
  logged as unresolved, not retained.
- Geneva Network of Innovators co-organized the AI Tinkerers Geneva inaugural
  meetup at SDG Solution Space (May 13, 2026) — a useful community venue
  signal for future Run B, noted in the community log.
- Geo coordinates: only Impact Hub Geneva carries a non-null pair (from the
  installed ih-038 record, evidence.geo = geneva.impacthub.net). All other
  retained venues keep null coordinates (map_location_unknown) because no
  sourced coordinate was captured in this pass.
- No Geneva records exist in past_venues.json; trusted_venues.json has no
  Geneva entry; ih-038 is the only Impact Hub Geneva record.

## 4. Community uncertainty

- activity_status labels are honest per the official own-page evidence:
  active (AI Tinkerers Geneva — inaugural meetup 2026-05-13; Decentral House
  — full events calendar; Open Geneva — 140+ hackathons since 2018;
  ge-ni — co-organized meetup 2026-05-13), intermittent (Geneva AI/Mindstone
  — Feb 2025 meetup evidenced, Nov event page "Unavailable", 2026 cadence
  unconfirmed; GDG Geneva — 55 members, no upcoming events at fetch).
- cohost_open is true ONLY for Geneva Network of Innovators (ge-ni), backed
  by its own page's explicit co-organization language ("The event is
  co-organised with the AI Tinkerers, Bengoo AI, and the Young AI leaders").
  All other records have cohost_open false with no negative claim. AI
  Tinkerers Geneva's /sponsors page returned HTTP 403 (WAF) to direct fetch,
  so the venue-partner language observed for Boston could not be verified for
  Geneva this pass.
- contact_info is null for every record: the only visible contact routes are
  email addresses (contact@decentral.house, nvy@manotel.com, etc.), forms,
  or organizer buttons, which are refused by policy. No contact route was
  inferred.
- member_size_public uses only the number displayed on the group's own page:
  Decentral House 100+ (stored 100), Open Geneva 6,000+ (stored 6000),
  GDG Geneva 55. Null where no public count exists (never estimated).
- Categories with honest evidence gaps (recorded as open questions in
  city_input.json, never as false absence): no PyData Geneva chapter (nearest
  is PyData Lausanne, ~60 km away); Genève R User Group Meetup page returned
  "Group not found" at fetch (an R-community index still lists a "Genève Data
  Analytics Group" with 481 members — unverifiable this pass); no standing
  Geneva quant community page surfaced; Crypto Valley (Zug) and swissAI
  (Swiss AI Association, German-first, Zürich-based) are Swiss-national
  adjacency, not Geneva-local records.
- SIB Swiss Institute of Bioinformatics (Geneva-headquartered) anchors the
  life-science data ecosystem (GenevaLovesData) but is an institute, not a
  community; logged as context only.
- AI Tinkerers Geneva subpages (events/sponsors) are WAF-blocked to direct
  fetch; the homepage and the ge-ni co-organizer page carry the evidence used.

## 5. Tooling / process notes

- web_extract is unavailable in this environment (search-only backend), so
  every page was fetched via curl with a browser user agent and parsed to
  text; WAF-blocked subpages (geneva.aitinkerers.org/events,
  /sponsors, hotelnvygeneva.com Seminars & Banquets 403) are recorded per
  record.
- All accessed_on values are 2026-08-13.
- ECB daily reference XML was fetched directly from ecb.europa.eu (200 OK,
  Cube time='2026-08-13').
