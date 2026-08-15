# Seoul Run A (2026 Q4) — venue discovery and disposition log

Research date: 2026-08-15. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. All HTTP fetches used a browser user
agent; web_extract is unavailable in this environment (search-only backend),
so every page was fetched via curl and parsed to text. Korean-language pages
are valid claim sources; only facts directly supported by the fetched page
text are recorded (no translation-derived claims).

Disposition convention: RETAINED (schema-valid record in venues.raw.json),
REJECTED (examined, does not fit scope/evidence), UNRESOLVED (lead not
retained because evidence is incomplete or inaccessible this pass).

## Seed check: Impact Hub Seoul

- Installed skill reference `references/impact_hub_locations.json` (150
  records): 0 hits for Seoul/Korea/KR (`country_code == "KR"` count 0; no
  'seoul'/'korea' substring in any record). Verified directly from the
  installed JSON.
- Live global locations page impacthub.net/locations/ (fetched 2026-08-15):
  no Seoul/Korea/South Korea entry.
- CONCLUSION: Impact Hub Seoul does not exist in the installed snapshot or on
  the live global locations page. It cannot be a trusted resolver match or a
  seeded venue candidate. No fabricated hub assertion is made. Seoul venue
  discovery proceeds without a hub seed; this is an explicit open question
  only if a Seoul hub opens later.

## Retained (6 records)

1. Nodeul Island — Livehouse (Nodeul Island 1F, Yongsan-gu)
   - Evidence: nodeul.org/facility/livehouse/ (official, fetched 2026-08-15):
     1,320 m², 456 seated / 708 standing, performance rental Sat/Sun/holiday
     KRW 4,000,000 (1회) / 6,000,000 (2회, if runtime > 3h) VAT excluded,
     hours 10:00-23:00, prep/teardown KRW 1,067,000/slot Sat.
   - Cost: KRW 6,000,000 (2-performance Saturday rate for an 8h event) ->
     USD 4,251.48 (ECB 2026-08-14 basis). Tier: shortlist_ready (0.2599).
   - Start-time (10:00 vs 09:00), screen, Wi-Fi, availability open.
   - Source URL: https://nodeul.org/facility/livehouse/ (accessed 2026-08-15).
2. DDP — Design Hall (Design Lab 3F, Jung-gu)
   - Evidence: ddp.or.kr/?menuno=714 (official, fetched 2026-08-15): 627.6 m²,
     about 110 pax, lectures/presentations/forums, convention 08:00-20:00.
   - Cost: not published (application via deep.ddp.or.kr). Tier:
     shortlist_ready (0.53) with cost_unknown.
   - Source URL: http://www.ddp.or.kr/?menuno=714 (accessed 2026-08-15).
3. DDP — Conference Hall (414 m²)
   - Evidence: culture.seoul.go.kr 2026 DDP regular-rental notice
     (nttId=15313, fetched 2026-08-15): Conference Hall 414 m², 2026 daily
     rate high season (1.1, Sep/Oct) KRW 3,907,330 VAT included; capacity
     not published in the notice.
   - Cost: KRW 3,907,330 -> USD 2,768.66 (ECB 2026-08-14). Tier: lead
     (capacity material gap; capacity 0 placeholder).
   - Source URL: https://culture.seoul.go.kr/culture/bbs/B0000000/view.do?nttId=15313
     (accessed 2026-08-15).
4. COEX — Conference Room 300 (Conference Rooms 3F, Gangnam-gu)
   - Evidence: business.coex.co.kr/meeting-room/conference/ (official,
     fetched 2026-08-15): 29 rooms on 3F, 20-300 pax; Room 300: 264 m²,
     114 classroom / 225 theatre; screen 3.6x2.7 (180"), 6,200 ANSI projector.
   - Cost: not published (inquiry). Tier: shortlist_ready (0.53) with
     cost_unknown.
   - Source URL: https://business.coex.co.kr/meeting-room/conference/
     (accessed 2026-08-15).
5. Mongsang Space (Mullae) — Main Hall (Yeongdeungpo-gu)
   - Evidence: mongsang-space.com/pricing (official, fetched 2026-08-15):
     KRW 88,000/h weekday, KRW 99,000/h weekend (Fri/holidays incl.); max 50
     pax with prior inquiry; setup fee KRW 50,000/100,000; catering from
     KRW 10,000/person; address 서울 영등포구 문래북로8 에이스NS타워 B102호.
   - Cost: 8h x KRW 99,000 = KRW 792,000 base -> USD 561.20 (ECB 2026-08-14);
     all-in for 50 pax includes per-person surcharge and setup fee (quote).
   - Tier: shortlist_ready (0.6876) — top selectable in this pass.
   - Source URL: https://www.mongsang-space.com/pricing (accessed 2026-08-15).
6. KT&G SangSangMadang Hongdae — Live Hall (Mapo-gu)
   - Evidence: sangsangmadang.com/rental/list (official, fetched 2026-08-15):
     rental available for each space; STEP 1 reservation inquiry; Live Hall
     is B2F music performance hall; no capacity/rate published on fetched
     pages.
   - Cost: not published. Tier: lead (capacity + location material gaps;
     capacity 0 placeholder).
   - Source URL: https://www.sangsangmadang.com/rental/list (accessed
     2026-08-15).

## Rejected (examined, not retained)

- COEX Auditorium (3F): 2,104 m², 1,080 theatre seats, LED screen 20x6 m —
  massively oversized for a 50-person event; the COEX Conference Room 300
  record covers the appropriate mid-size option (business.coex.co.kr
  /meeting-room/auditorium/, fetched 2026-08-15).
- DDP Art Hall 1 (2,992 m²) and Art Hall 2 (1,547 m²): published 2026 daily
  rates KRW 17,969,950-28,238,490 (Art Hall 1) and 9,291,280-14,600,580
  (Art Hall 2) — far over the USD 5,000 soft budget; oversized for 50 pax.
  The Conference Hall record covers the DDP mid-size priced option
  (culture.seoul.go.kr notice, fetched 2026-08-15).
- Lotte Hotel Seoul Executive Tower conference rooms: 4 small rooms up to 18
  pax — below the 50-person target (lottehotel.com page, fetched 2026-08-15).
- ST Center (Korea Science and Technology Center, Gangnam): official site
  stcenter.or.kr publishes a reservation system and rate-adjustment notice
  (search-indexed), but the site is unreachable from this environment
  (connection timeout on 2026-08-15); no claim-bearing page could be
  captured — logged UNRESOLVED, not retained.

## Unresolved (lead not retained this pass)

- aT Center (Yangjae, Gangnam): conference rooms exist (GWDC 2026 Korea is
  booked there Sep 29-30, 2026 per gwdc.net) but atcenter.or.kr returns a
  JavaScript CUPID challenge to direct fetch (HTTP 000/403) and Wayback
  snapshots were 503 at fetch time — no claim-bearing page captured. Verify
  via a browser-capable fetch or the aT Center sales desk.
- WeWork Seoul (multiple Gangnam locations): wework.com returns HTTP 403 to
  direct fetch; the SEO-snippet shows Seolleung II from KRW 374,000/month
  coworking (not a per-event room rate). Verify via WeWork's booking flow.
- Grand Hyatt Seoul NamSan meeting rooms (Yongsan): hyatt.com returns HTTP
  403 to direct fetch; search snippet states 5 rooms, 63-358 m², 20-240 pax.
  Verify via a browser-capable fetch.
- Fastfive (meeting-room booking via app; 60+ branches): rates live inside
  the app/booking flow, not on a fetchable static page; no official rate
  page captured.
- SparkPlus (space-rental page is JS-rendered): seminar-room rates are shown
  inside the booking flow; a third-party blog cites Euljiro seminar room at
  KRW 200,000/h weekday / 240,000/h weekend, but no official static rate page
  was captured — directory/blog rates cannot support a venue record.
- Seoul Startup Hub Scale-up Center (Gangnam, Teheran-ro 7-gil 22): official
  site scaleupcenter.startup-plus.kr has a 장소대관 (space rental) menu, but
  the page is JS-rendered with no static room/rate data; verify via the
  rental portal.
- Mongsang Studio seminar room (mongsangstudio.com): separate small seminar
  room max 24 seated — below target; the main Mongsang Space record covers
  the fit.
- D.CAMP (Seoul Startup Hub network, dcamp.kr): space/rental page returned
  404 at fetch; homepage describes 'space 입주 대관' but no static rates.

## Platform / directory leads (discovery only, not venue evidence)

- Space Cloud (spacecloud.kr): Seoul meeting-room/event-space platform with
  per-space rates; used as discovery index only, never as venue evidence
  (per evidence policy the operating venue's own page is required).
- Tipping Korea (tippingkorea.co.kr): classroom/event-space rental directory;
  discovery only.
- Roovook (roovook.com): venue network with COEX conference-room listings;
  discovery only.
- Surf Office / Coworker / instantoffices Seoul listings: coworking
  directories; discovery only (monthly membership figures, not per-event
  room rates).
- Seoul City public-facility reservation (yeyak.seoul.go.kr): city platform
  for public venue reservation; discovery only — individual facility pages
  would be needed for venue evidence.

## Notes

- Geo coordinates: no retained venue carries a sourced latitude/longitude
  pair this pass (official pages fetched did not publish coordinates), so
  all pairs are null with the informational map_location_unknown flag.
- Event-window evaluation: every retained venue was assessed for the
  09:00-17:00 8-hour window; only DDP Design Hall (08:00-20:00 convention)
  has a sourced window that covers it; Nodeul's published start is 10:00 and
  all other venues have unconfirmed windows (soft questions, never assumed).
- The 09:00-17:00 window is a research evaluation, not an availability
  commitment; Saturday availability is a verification question for every
  retained venue.
