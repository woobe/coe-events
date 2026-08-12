# Boston Run A (2026 Q4) — source uncertainty notes

Accessed/research date: 2026-08-12. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. This file is a local research artifact;
nothing here is a recommendation, elimination, or date commitment.

## 1. Calendar uncertainty

- All calendar records were verified against official organizer pages where
  possible. Sources that were verified by direct fetch on 2026-08-12:
  aiweek.boston (Boston AI Week 2026 + Summit), bostonfintechweek.org (Boston
  Fintech Week 2026), technologyreview.com/all-events (EmTech Future + MIT
  Future Fest), massrobotics.org (RoboBoston 2026), 2026.dahshu.org (DahShu
  Data Science Symposium 2026), world.aiacceleratorinstitute.com/location/boston
  (Generative AI Summit Boston), nxtai-conference.com (Nxt AI-2026),
  hocr.org (Head of the Charles), bostonbookfest.org (Boston Book Festival,
  confirmed via official-site search snippet + Brattle Book Shop + IPNE
  corroboration because the site returned HTTP 403 to direct fetch),
  baa.org (B.A.A. Boston Half), harvardsquare.com (Harvard Square Oktoberfest).
- RoboBoston 2026: the massrobotics.org news page and the separate Boston AI
  Week schedule entry both confirm Sep 26, 2026; the MassRobotics `/roboboston/`
  landing page still describes the block party generally. The Robotics & AI
  Technical Career Fair is Sep 25, 2026 (official MassRobotics announcement).
- EmTech Future 2026 (Sep 29-Oct 1) is listed on the official MIT Technology
  Review All Events page; the separate EmTech AI editions (Apr 2026 past,
  May 2027 future) are distinct events and are not recorded here.
- MIT Future Fest 2026 (Sep 30-Oct 4) is an MIT Museum-launched campus-wide
  festival; recorded as a major_other logistics flag (city crowding, campus
  access) with topic-adjacent AI/tech programming, not as a related-event
  recommendation.
- Boston Blockchain Week 2026 (Sep 8-10, Quincy Center) was observed from
  official bostonblockchainweek.com and QUBIC Labs pages but is NOT recorded in
  calendar_conflicts.json because its dates fall before the 2026-09-15
  calendar-awareness coverage start; it is an explicitly noted adjacent event
  for Joe's awareness, never an elimination.
- ODSC AI East 2026 (Apr 28-30, Hynes) and other spring events (EmTech AI Apr,
  Data Summit May, Leaders In AI Summit May, IEEE ICAD Jun, JSM Aug 1-6) fall
  outside the declared 09-15..12-15 research coverage period and are not
  recorded.
- ETHBoston (boston.ethglobal.co) shows Sep 6-8, 2019 on its own page — stale,
  not a 2026 event; no 2026 edition was found.
- All calendar prose is date-neutral about Decentralized AI Day (v2.8/v2.9
  family): no scheduling-window, candidate-date, or preferred-date phrasing
  is stated anywhere in calendar records. Factual dates of the external
  events are preserved as evidence facts.

## 2. Venue uncertainty

- Impact Hub Boston (ih-019): the official boston.impacthub.net page says
  "Coming Soon" / "New location coming soon!" and provides no address,
  capacity, pricing, screen, Wi-Fi, or booking path. It is retained as a
  discovery seed/lead only; it cannot be scored above lead until a current
  claim-bearing page supports its material fields (Budapest tv-02 precedent).
- MIT Samberg Conference Center: official use-fees PDF provides day rates and
  capacities, but screen/Wi-Fi inventory is not in the PDF; external (non-MIT)
  access requires an MIT DLC sponsor; weekend events require a $3,500 F&B
  minimum. Conference I (7th floor) was selected as the modeled room (125
  rounds / 150 theater, $725 external day); other rooms (DR3&4 combined, DR5)
  are alternatives with different rates.
- The Foundry (Cambridge): official page publishes capacities, projector
  confirmation, and small-event rates ($300/hr business hours, $600/hr after
  closing) with sliding scale; business-hours/closing definition and Wi-Fi are
  unconfirmed. Red Multi (50 seated) and Performance Space (115 seated) are
  both retained as distinct records.
- WPI Seaport Events Center (District Hall Boston): 6,400 sq ft, event request
  form only; no capacity or price published. Note: the old districthall.com
  domain redirects to a GoDaddy for-sale page and districthallboston.org's
  homepage currently serves unrelated/redirect content; the WPI events page is
  the operative official booking surface.
- CIC Cambridge: multiple 150-capacity spaces (Venture Café, Mosaic, rooftop)
  with basic AV + free Wi-Fi included, but all pricing is inquiry-only.
- Workbar: official page states 20-100 person event spaces from $250/hr across
  Greater Boston locations; per-location room capacity, AV, Wi-Fi, and
  Saturday availability are unconfirmed. Address left null because no single
  location/room is evidenced.
- Artisan's Asylum: official rentals page confirms event rentals at the
  Allston campus but publishes no capacities, rates, screen, or Wi-Fi.
- Harvard Innovation Labs (i-lab): public entry requires an i-lab affiliate
  invitation or a public event; lecture hall capacity and external pricing are
  unconfirmed.
- MassRobotics: active robotics/AI hub; no external venue-rental page, rate,
  capacity, or AV inventory published.
- Emmanuel Episcopal Church Parish Hall: platform listings conflict ($49/hr per
  Tagvenue city page vs $2,000/day per space-pal), so cost is unsubstantiated;
  the venue's own page and booking terms are required. Retained as a lead.
- Geo coordinates for retained venues with a non-null pair are approximate and
  sourced from the venue's own page (evidence.geo); venues without a confirmed
  address keep null coordinates (map_location_unknown).
- No Boston records exist in past_venues.json or trusted_venues.json; no such
  seeds were created.

## 3. Community uncertainty

- activity_status labels are honest per the official own-page evidence:
  active (AI Tinkerers Boston, PyData Boston, Boston FinTech, CryptoMondays
  Boston, MIT Sloan AI & ML Club, HDSI, Boston Python), intermittent (ODSC AI
  Boston — events tab empty at fetch, annual conference evidence only;
  LangChain Boston — single observed event), dormant (Boston Blockchain
  Association — no visible events since Mar 2025; official site 403).
- cohost_open is true ONLY for AI Tinkerers Boston, backed by the chapter's own
  sponsors page ("Venue Sponsor / Host ... Acknowledgment as official venue
  partner"). All other records have cohost_open false with no negative claim.
- contact_info is null for every record: the only visible contact routes are
  email addresses or forms, which are refused by policy. No contact route was
  inferred.
- member_size_public uses only the number displayed on the group's own page
  (Meetup counts for PyData 3,433, Boston FinTech 4,220, CryptoMondays 204,
  ODSC AI Boston 5,314, Boston Blockchain Association 3,770); null where no
  public count exists (never estimated).
- AI Salon Boston: no active Boston chapter page was found in this pass;
  recorded as an explicit community-research open question in city_input.json,
  not as a false absence.
- Northeastern University / BU student AI/data communities: no public
  student-group page with observed activity was retained in this pass; recorded
  as an explicit community-research open question in city_input.json.
- LangChain Boston contact email (community@langchain.dev) is visible on the
  event page but is not recorded per contact policy.

## 4. Tooling / process notes

- web_extract was unavailable in this environment (search-only backend), so
  every page was fetched via curl with a browser user agent and parsed to text;
  fetch failures are recorded per record (e.g. bostonbookfest.org 403,
  bostonblockchain.org 403, greentownlabs.com Cloudflare block).
- All accessed_on values are 2026-08-12.
