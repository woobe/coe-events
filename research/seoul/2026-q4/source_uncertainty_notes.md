# Seoul Run A (2026 Q4) — source uncertainty notes

Accessed/research date: 2026-08-15. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. This file is a local research artifact;
nothing here is a recommendation, elimination, or date commitment.

## 1. FX conversion basis

- All USD equivalents in this package use the ECB euro foreign exchange
  reference rate dated 2026-08-14 (EUR 1 = USD 1.1567; EUR 1 = KRW 1632.42),
  fetched 2026-08-15 from
  https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml
  (Cube time='2026-08-14', the last ECB working-day reference before the
  fetch date). Derived rate: 1 KRW = 0.0007085799 USD (1.1567 / 1632.42);
  equivalently 1 USD = 1411.2735 KRW.
- Converted amounts (see also fx_evidence_2026-08-15.md):
  - Nodeul Island Livehouse: KRW 6,000,000 (Sat 2-performance rate, VAT
    excluded) -> USD 4,251.48.
  - DDP Conference Hall: KRW 3,907,330 (Sep/Oct high-season daily rate, VAT
    included) -> USD 2,768.66.
  - Mongsang Space: KRW 99,000/h weekend x 8h = KRW 792,000 base -> USD
    561.20 (plus per-person surcharge and setup fee; quote required).
- NEVER invent a rate: any venue without a dated, published conversion basis
  keeps `estimated_cost_usd: null` with a confirm-cost question. This applies
  to DDP Design Hall, COEX Conference Room 300, and KT&G SangSangMadang (all
  inquiry-only pricing).
- Gap: the ECB 2026-08-14 reference is a dated published basis, not a live
  market rate and not a predictor of 2026 Q4; re-confirm at booking time.

## 2. Calendar uncertainty

- All calendar records were verified against official organizer pages where
  possible (direct fetch on 2026-08-15): koreablockchainweek.com (KBW2026),
  gwdc.net (GWDC 2026 Korea), english.visitkorea.or.kr (Korea public
  holidays 2026: Chuseok Sep 24-26, National Foundation Day Oct 3 observed
  Oct 5, Hangeul Day Oct 9), fsc.go.kr press-release PDF (Korea Fintech Week
  Nov 25-27, 2026 at aT Center), comeup.org + third-party factual dates
  (COMEUP 2026 Dec 9-11 at COEX).
- COMEUP 2026: the official comeup.org site is JS-rendered and does not
  expose 2026 dates in static HTML; the December 9-11, 2026 dates at COEX
  come from Korean business press (mhnet.kr) and trade-show calendars
  (ntradeshows.com, neventum.com) — stored as third-party factual dates with
  a verification question, per plan policy.
- Korea Fintech Week: the official fintechweek.or.kr site returned HTTP 000
  to direct fetch from this environment; the FSC (Financial Services
  Commission) official press release PDF (fsc.go.kr, dated 2026-07-29) was
  fetched and confirms November 25-27, 2026 at aT Center (Yangjae-dong),
  Seoul, and the search-indexed fintechweek.or.kr snippet shows the same
  window at aT센터 제1/2전시장.
- ADJACENT CONTEXT ONLY (outside the 2026-09-15..2026-12-15 coverage window;
  never in-window assertions):
  - World Knowledge Forum 2026 (Sep 8-10, Jangchung Arena / The Shilla
    Seoul, official wkforum.org) — before the coverage start.
  - Try Everything 2026 (Sep 9-10, DDP, Seoul city startup festival,
    official tryeverything.or.kr + third-party dates) — before the coverage
    start.
  - Seoul International Fireworks Festival (Sep 5, 2026, Yeouido Hangang
    Park; Hanwha-hosted; multiple third-party Korean sources confirm Sep 5,
    2026 — a major crowd event but outside the coverage window).
  - AI Summit Seoul & Expo (Aug 19-21, 2026, COEX Grand Ballroom; official
    aisummitseoul.com) — outside the coverage window.
  - Bitcoin Seoul 2026 (Jun 4-5, FKI Tower; official bitcoin-seoul.kr) —
    outside the coverage window.
  - 2026 Blockchain Meetup Conference (Mar 12, 2026, 섬유센터 텍스파홀;
    MSIT/KISA-hosted, wiki1.kr) — past event, context only.
- Not recorded: AI Seoul 2026 (Jan 30, COEX Grand Ballroom; Seoul city +
    Seoul AI Hub) and Seoul AI Policy Conference (Jun 16-17, The Plaza) —
    past events outside the window; WAIC/NeurIPS/WebSummit/RareEvo — other
    cities.
- All calendar prose is date-neutral about Decentralized AI Day: no
  scheduling-window, candidate-date, or preferred-date phrasing is stated
  anywhere in calendar records. Factual dates of the external events are
  preserved as evidence facts.

## 3. Venue uncertainty

- Impact Hub Seoul DOES NOT EXIST (verified from the installed
  impact_hub_locations.json — 150 records, 0 Seoul/KR — and the live
  impacthub.net/locations page). No hub seed; no fabricated resolver match.
- aT Center (Yangjae): conference-room rates and specs are on atcenter.or.kr
  but the site blocks non-browser fetches (JavaScript CUPID challenge; HTTP
  000/403; Wayback 503 at fetch). GWDC 2026 Korea will run there Sep 29-30,
  2026 (official gwdc.net), so the venue is real and active, but no
  claim-bearing page could be captured this pass — logged unresolved.
- ST Center (Korea Science and Technology Center, Gangnam): official site
  stcenter.or.kr is unreachable from this environment (connection timeout);
  search-indexed pages describe a reservation system and a 2023 rate
  adjustment for the international conference room. Verify via a
  browser-capable fetch; logged unresolved.
- COEX Conference Room 300: capacity/screen confirmed from the official
  business.coex.co.kr page; the rental fee is inquiry-only, the window is
  unconfirmed, and Wi-Fi is not itemized per room.
- DDP: Design Hall (110 pax, 08:00-20:00 convention) has no published fee;
  Conference Hall (414 m²) has a published 2026 daily rate but no published
  capacity; Art Hall 1/2 are over budget and oversized. DDP rental requires
  application + committee review (deep.ddp.or.kr). The 2026 notice is the
  regular-rental announcement (posted 2025-10-21); the September/October
  high-season multiplier 1.1 is used for the Conference Hall estimate.
- Nodeul Island: the official site notes the '노들 글로벌 예술섬' construction
  project may change facility conditions, and the 2026 second-half rolling
  rental notice is open; the Livehouse is oversized (456-708) and its
  published performance start is 10:00 (the assessed 09:00-17:00 window's
  start is a verification question). The Nodeul Lounge page returned 404 for
  several URL guesses this pass and was not captured.
- KT&G SangSangMadang Hongdae: rental guide exists but no capacity/rate is
  published on the fetched pages; the Live Hall is performance-oriented.
- Mongsang Space: published rates are clear, but the all-in cost for 50
  people includes a KRW 10,000/person surcharge over the base 6 and a setup
  fee (KRW 100,000 over 20 people); screen/Wi-Fi/window are unconfirmed.
- Hotels (Grand Hyatt Seoul, Lotte Hotel Seoul): hyatt.com/lottehotel.com
  returned 403/JS-only to direct fetch; Lotte's Executive Tower conference
  rooms are too small (max 18 pax). Grand Hyatt NamSan rooms (20-240 pax)
  logged unresolved pending a browser-capable fetch.
- WeWork Seoul, Fastfive, SparkPlus: rates live inside booking flows or the
  sites block direct fetch; no official static rate pages captured.
- Geo coordinates: no retained venue carries a sourced latitude/longitude
  pair this pass (official pages fetched did not publish coordinates); all
  pairs are null with the informational map_location_unknown flag.
- No Seoul records exist in past_venues.json; trusted_venues.json has no
  Seoul entry; no Impact Hub Seoul record exists anywhere (see above).

## 4. Community uncertainty

- activity_status labels are honest per the official own-page evidence:
  active (AI Tinkerers Seoul — Jul 2 + Aug 20, 2026; GDG Seoul — Build with
  AI Seoul May 2, 2026; AWSKRUG — multiple Aug 2026 meetups; Modulabs —
  2025/2026 Seoul offline events; PyLadies Seoul — 2026 monthly bookclubs +
  upcoming Jul 26, 2026 workshop; Korea R User Group — monthly meetup claim),
  intermittent (Seoul Ethereum Meetup — no upcoming event at fetch; Ethereum
  Seoul Community — latest dated notices 2024-era; Superteam Korea —
  digital-first bounties; PyTorch Korea — digital-first).
- Korea's Web3 market is a DISCOVERY HYPOTHESIS: this pass retained only
  own-page-evidenced Seoul web3 groups (Seoul Ethereum Meetup, Ethereum
  Seoul Community, Superteam Korea), all honestly labeled; no claim of a
  'strong Web3 market' is made.
- cohost_open is true ONLY for three records with same-page language:
  AI Tinkerers Seoul ('sponsored by PostHog and DanaIX'), AWSKRUG (sponsor/
  venue-sponsor section), Korea R User Group (donation/sponsorship language,
  flagged conservatively). All other records cohost_open false with no
  negative claim.
- contact_info is set only for AWSKRUG (awskr.org, visibly referenced on the
  same official page); all other records null (email addresses like
  etherKorea@gmail.com / info@ethereum-seoul.community / admin@r2bit.com and
  forms are refused by policy; no route is inferred).
- member_size_public uses only the number displayed on the group's own page;
  null elsewhere (never estimated).
- Honest empty search recorded as community-research open questions in
  city_input.json (no standing Seoul quant community page; no Startup Grind
  Seoul chapter page with observed activity; WAI Korea is a company in
  Ansan, not a Seoul community).

## 5. Tooling / process notes

- web_extract is unavailable in this environment (search-only backend), so
  every page was fetched via curl with a browser user agent and parsed to
  text; WAF/JS-blocked pages (atcenter.or.kr, wework.com, hyatt.com,
  fintechweek.or.kr direct fetch, comeup.org static HTML) are recorded per
  record.
- All accessed_on values are 2026-08-15.
- ECB daily reference XML was fetched directly from ecb.europa.eu (HTTP 200,
  Cube time='2026-08-14'); the local XML copy was preserved at research time.
- Korean-language pages (nodeul.org, ddp.or.kr, culture.seoul.go.kr,
  mongsang-space.com, sangsangmadang.com, modulabs.co.kr, r2bit.com,
  pyladies.kr) are valid claim sources; only facts directly supported by the
  fetched page text are recorded (no translation-derived claims beyond
  plain-language descriptions of what the page states).
