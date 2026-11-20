# Seoul 2027 H1 — raw evidence summary (research 2026-11-20; review round 2, 2026-11-20)

Scope: a free community Decentralized AI Day for 50-125 people on a Saturday, 09:00-17:00
(8 hours), date window 2027-01-01 through 2027-06-30. This is a **Run A raw evidence
package**. It contains no bundle, no rendered summary and no date recommendation. Owner
chooses the date.

## Files in this directory (seven)

1. `city_input.json` — 1 object. Slug `seoul-kr`, KRW, Asia/Seoul, window
   2027-01-01..2027-06-30, `target_date` 2027-04-17 (a Saturday, technical placeholder
   only), both recommendation fields null, `research_completed_on` 2026-11-20.
2. `venues.raw.json` — 13 venue records, 10 with latitude+longitude.
3. `communities.raw.json` — 16 community records (11 active with dated 2026 activity,
   3 intermittent, 2 dormant).
4. `calendar_conflicts.json` — 5 records (3 `related`, 2 `major_other`).
5. `calendar_context.raw.json` — exactly 4 keys, `adjacent_events` holding 3 rows.
6. `venue_discovery_log.md`, `community_discovery_log.md` — search and rejection logs.
7. `evidence_summary.md` — this file.

The previous round's extra `adjacent_events.raw.json` was deleted after the manager ruling
of 2026-11-20 16:47: the adjacency rows now live in `calendar_context.raw.json`
(`adjacent_events`), which is their raw home, so no file can disagree with another.

Schema checks run on this machine, plan-event 2.26 scripts:

- `validate_schema.py venue venues.raw.json` -> PASS
- `validate_schema.py local_community communities.raw.json` -> PASS
- `validate_schema.py calendar_conflict calendar_conflicts.json` -> PASS
- `validate_adjacent_events(calendar_context.raw.json.adjacent_events, 'seoul-kr',
  [('2027-01-01','2027-06-30')])` -> no errors

## Venue tiers — the numbers this package stands behind

The skill's own deterministic scorer is the tier of record. Command run 2026-11-20:

```
python3 plan-event/scripts/score_venues.py venues.raw.json --budget-usd 5000 \
  --target-attendance 50 --event-date 2027-04-17 --event-duration-hours 8
```

Result: **eligible 0 / shortlist_ready 6 / lead 7**.

- `shortlist_ready` (6): SETEC 세미나실 2 (0.5273), SETEC 세미나실 1 (0.5234),
  DDP 디자인홀 (0.4778), COEX 컨퍼런스룸 300호 (0.4500), 서울시 어울림플라자
  다목적강당 (0.3250), 노들섬 라이브하우스 (0.1708).
- `lead` (7): 그라운드옥탑 (Space Cloud), D.CAMP 마포 박병원홀, D.CAMP 선릉 이벤트홀,
  KT&G 상상마당 라이브홀, 문화비축기지 T6, 앙트레블 (Space Cloud), 연세대 백양누리
  그랜드볼룸 A.
- `eligible` (0). No venue has a confirmed 2027 date hold, so none can reach eligible.

The two D.CAMP rooms are **leads**, not shortlist_ready: both carry an `other_material`
verification question (theatre/scale fit) and `cost_basis: unknown`, and `schemas.md`
treats `other_material` as material.

Stricter card rule, stated separately as the card requires: if `shortlist_ready` demands
a current, claim-bearing price plus availability evidence, the count falls to **4 at most**
— SETEC 세미나실 1, SETEC 세미나실 2, DDP 디자인홀 and 노들섬 라이브하우스 all publish a
numeric current rate for an 8-hour/day or weekend slot. COEX 300호 and 어울림플라자 drop
out (no numeric price; 어울림's band has no published per-row unit). No Seoul venue
publishes a bookable 2027 Saturday calendar, so under the strictest reading of
"availability evidence" the count is 0. This package does not claim 8 under either rule.

Venues with coordinates (10): SETEC 37.4954477/127.0720963 (both SETEC rooms),
DDP 37.5670686/127.009899, 노들섬 37.5181487/126.9582184,
D.CAMP 선릉 37.507863/127.0452171, D.CAMP 마포 37.5453974/126.9525905,
COEX 37.5125275/127.0588489, 백양누리 37.5639034/126.9376219,
문화비축기지 37.5715903/126.8937769, 상상마당 37.5509886/126.9210678.
Each carries an `openstreetmap.org` object URL in `evidence.geo`.

Null coordinates (3): 어울림플라자 (no building object in OSM), 그라운드옥탑 and
앙트레블 — Space Cloud masks the street address until booking; a `location` question is
attached instead of a guessed coordinate.

## Prices confirmed (KRW + USD on one dated basis)

Conversion basis for every converted amount: ECB euro foreign exchange reference rate
dated 2026-11-20 — EUR 1 = USD 1.0990, EUR 1 = KRW 1472.04, so 1 KRW = USD 0.000746583
(1 USD = **1,339.44** KRW), fetched 2026-11-20 from
`https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` (Cube time='2026-11-20').
USD totals are rounded from the KRW total; hourly USD figures are rounded separately, so
hourly x 8 can differ by one cent (recorded note in both rate-derived records).

Six amounts, in two categories:

Published rate tables (4 venues):

- SETEC 세미나실 1 — KRW 890,000 for `8~17시(전일 8H)`, VAT excluded -> USD 664.46.
- SETEC 세미나실 2 — KRW 760,000 for the same slot, VAT excluded -> USD 567.40.
- DDP 디자인홀 — KRW 3,256,000 `1일 기준` (VAT not stated on the page) -> USD 2,430.87.
- 노들섬 라이브하우스 — KRW 6,000,000 `토,일,공휴일` 2회 rate (a 3-hour performance is
  billed as 2회), VAT excluded -> USD 4,479.50.
- 서울시 어울림플라자 — rate table publishes `350,000 ~ 540,000원` but not the per-row
  unit, so **no number is claimed**; the cost field stays null. Counted here as a
  published table without a usable figure.

Rate-derived estimates, not quotes (2 venues, both Space Cloud listings):

- 그라운드옥탑 — KRW 200,000/hour weekend rate x 8h = KRW 1,600,000, VAT excluded ->
  USD 1,194.53 (hourly USD 149.3166; 149.3166 x 8 = 1,194.53).
- 앙트레블 — KRW 88,000/hour x 8h = KRW 704,000, no weekend differential published ->
  USD 525.59 (hourly USD 65.6993; 65.6993 x 8 = 525.59).

## Prices NOT confirmed (no figure claimed)

- **서울시 어울림플라자 다목적강당** — band only, unit per row unstated (above).
- **D.CAMP 선릉 / D.CAMP 마포** — no price published; TaapSPACE application plus 대관 심사,
  then a quote. Both records carry `cost_basis: unknown`.
- **COEX 컨퍼런스룸 300호** — room specs and an `임대관련자료` board exist; no public rate
  for this room.
- **연세대 백양누리 그랜드볼룸 A** — only the LED screen fee is published (KRW 1,320,000)
  plus the rule `4만원 이상 메뉴 식사시 기본대관료 3시간 무료`; the base rate sits in the
  `백양누리_요금표` attachment, which was not machine-readable.
- **문화비축기지 T6** — indoor tanks moved to a 사용수익허가 operator
  (㈜더문엔터테인먼트, 02-508-2205); no indoor rate published. Only the outdoor 문화마당
  rate is public (T0 `141,613원(1시간)`).
- **KT&G 상상마당 라이브홀** — procedure, address and contact only; no base rate.

## Venue claims that remain unverified

- **Saturday availability for every venue.** No venue exposes a bookable 2027 calendar to
  an anonymous fetch. Nodeul Island and 어울림플라자 price Saturday use, D.CAMP publishes
  `토요일 09:00 ~ 18:00`, but no specific 2027 date is confirmed anywhere.
- **Attendee Wi-Fi at every venue except 그라운드옥탑 and 앙트레블** (both listing-confirmed).
- **Screens**: confirmed only at DDP 디자인홀 (LED 6.4m x 4m), D.CAMP 선릉
  (`LED 디스플레이`, 60인치 TV 2대), D.CAMP 마포 (98인치 TV 2대, 빔프로젝트),
  COEX 300호 (LED 6.5m x 2.5m), 백양누리 (LED, fee KRW 1,320,000), 그라운드옥탑
  (150인치 빔), 앙트레블 (4K LED 5m x 3m). SETEC, 노들섬, 어울림플라자, 문화비축기지,
  상상마당 are unknown.
- **VAT treatment.** SETEC and Nodeul state `부가가치세 별도`. DDP's rendered table does
  not state VAT; neither does 어울림플라자's.
- **Room capacities.** SETEC 세미나실 1 (100석) and 세미나실 2 (80석) come from the SETEC
  listing on Space Cloud, not from the rate page (which publishes area only); 백양누리
  60-120석 comes from the Yonsei page but the building-level figure for 그랜드볼룸
  elsewhere on the site is 380석 — unresolved.
- **백양누리 layout.** The official page sells banquet catering; a venue-platform FAQ
  states round tables only and that a lecture layout needs an outside setup vendor. That
  is platform-sourced, flagged, and material (it is why the record is a lead).
- **D.CAMP booking ceiling.** `신청일 기준 최대 7일 이후 60일 이전 행사만 신청 가능합니다`
  — a 2027 date cannot be applied for today; D.CAMP cannot be secured before 60 days out.
- **Coordinate accuracy.** D.CAMP 선릉's OSM match is an address node occupied by a shop in
  the building; 문화비축기지's node is the T2 stage on the same site as T6. Both are the
  published site address, not a door-level survey.
- **어울림플라자 has no coordinate** — Nominatim returned only road-level features for
  공항대로 489 / 등촌동 645-11. Null instead of a road centroid.

## Communities — honest counts

16 records, each with a URL and `accessed_on: 2026-11-20`. **11 are active with a dated
2026 in-person fact**, so the card's 10+ bar is met without relabelling anything:

1. AI Tinkerers Seoul — next event 2026-11-24; past 2026-07-02 and 2026-08-20.
2. AWSKRUG — sessions 2026-11-04, 2026-11-24, 2026-11-26.
3. PyLadies Seoul — book clubs/workshops on 2026-02-07, 03-04, 03-21, 04-01, 04-25,
   05-06, 05-30, 06-03, 07-26, 09-05; PyLadies Asia Conference 2026 announced for 11-29.
   (The conference is still upcoming at check time; the past events carry the activity
   claim.)
4. 모두의연구소 (Modulabs) — in-person seminars 2026-11-10 / 11-26 / 11-27 at 강남캠퍼스.
5. Bridge34 — 2026-04-14, 2026-05-07, KBW2026 side events 2026-09-28..10-02.
6. KISA 블록체인 밋업데이 (BCMD) — 31st session 2026-11-14, Sat, 10:00-18:00.
7. AI Seoul (Meetup group) — bi-weekly AI Adoption Talk through 2026-06-06 .. 12-12;
   326 members.
8. Superteam Korea — Solana Ecosystem Day 2026-09-28, Solana Summit Korea 2026-09-30,
   SANC Nine 2026-10-01 (official KBW events page).
9. openKcloud 커뮤니티 (ETRI) — DevDay 2026-11-10, ST Center 중회의실3.
10. Ethereum Collective Korea (ECK) — research digests through 2026-11-19; co-hosted
    Ethereum Korea One Genesis builder day 2026-09-29.
11. Builderbase Hackathons — DIGITAL AF Seoul hackathon 2026-10-01, Yeongdong-daero.

Intermittent (3): 파이토치 한국 사용자회 (blog 2026-10 + a site report of a 2026-09-30
meetup, no own calendar), 한국 R 사용자회 (서울 R Meetup subpage 404 this pass, no dated
2026 meetup observed), GDG Seoul (organizer page renders with no upcoming event; the
May 2026 Build with AI event survives only in a search index).

Dormant (2): Seoul Ethereum Meetup (last event 2022-12-15, 3,983 members), Ethereum Seoul
Community (2024-era notices).

Honest caveats on the activity bar: two of the eleven (Superteam Korea, openKcloud) are
evidenced by an organiser listing or a public-sector programme rather than a community
calendar; BuilderBase is an international hackathon operator with one 2026 Seoul event
rather than a Seoul membership group; ECK's attendance figures are self-reported. Member
counts are published for only two records (AI Seoul 326, Seoul Ethereum Meetup 3,983);
every other count is null rather than estimated. Co-host willingness is published only by
Bridge34; all other `cohost_open` values are false with a specific question.

## Calendar — 2027 H1 Seoul

`calendar_conflicts.json` (5 rows, schema-valid, no `opportunity_kind`/`status` — the
validator rejects those keys there):

- **AI EXPO KOREA 2027** — 2027-04-14..16, COEX Hall A, `related` / `ai` / `medium`.
  Official site (`전시회 개요`): `2027년 4월 14일(수) ~ 16일(금), 3일간`, `서울 COEX 1층
  Hall A`, 50,000 target visitors.
- **월드IT쇼 2027 (WIS)** — 2027-04-21..23, COEX Hall A/B1/C, `related` / `ai` / `medium`.
  COEX BUSINESS page `2027.04.21 - 2027.04.23`; 한국경제 2026-09-16 reports the same dates.
- **서울메타위크 2027 (Seoul Meta Week)** — 2027-04-29..30, COEX Grand Ballroom,
  `related` / `ai` / `low`. Official site: `2027. 04. 29 - 30 Coex, Grand Ballroom`.
- **AW 2027 (Automation World)** — 2027-03-03..05, COEX 전체 홀, `major_other` / `other` /
  `none`. Official page: `2027. 3. 3(수) – 3. 5(금)` with `500개 업체 / 2,300부스 /
  80,000명 참관`. Manufacturing automation audience, so logistics/venue demand only.
- **서울마라톤 2027** — 2027-03-21, `major_other` / `other` / `none`. 동아일보 2026-11-20:
  `제97회 서울마라톤 겸 동아마라톤은 2027년 3월 21일 열린다`.

`calendar_context.raw.json` `adjacent_events` (3 rows, all `related`, `status: confirmed`,
`opportunity_kind: ai`, same city so no `rail`): AI EXPO KOREA 2027, WIS 2027,
서울메타위크 2027. This is the raw home the manager designated on 2026-11-20 16:47.

Not recorded, because no official 2027 date is published: **NextRise 2027** (nextrise.co.kr
shows no 2027 dates), **Korea Blockchain Week 2027** (koreablockchainweek.com is KBW2027-
branded but publishes no dates; historically early September, outside H1), **SK AI SUMMIT**
(reported to move to H1 2027, no official date), **AI Summit Seoul & Expo 2027**
(officially 2027-08-11..13, outside H1).

### Saturday sweep — all 26 Saturdays of 2027-01-01..2027-06-30

Registry rows used: `KR` public holidays for 2027 from
`references/school_holidays.json`, edition `2027년 월력요항 (우주항공청공고 제2026-0078호)`.
The registry carries no `KR:seoul` holiday rows and no `KR:seoul` coverage row, so the host
jurisdiction resolves to its parent `KR`; that is why `host_holidays` and `host_coverage`
stay empty in this raw file and the curated rows are read from the registry later.

Saturdays that collide with a holiday or form a long weekend:

- **2027-01-02** — Saturday of the New Year weekend (신정 2027-01-01, Friday).
- **2027-02-06** — 설날 연휴 day 1 (holiday Saturday; 연휴 runs 02-06..08 with substitute
  2027-02-09).
- **2027-02-27** — Saturday before 3·1절 on Monday 2027-03-01: a three-day long weekend.
  (Missing from round 1; added on review.)
- **2027-05-01** — 노동절, a holiday Saturday, and the substitute holiday is Monday
  2027-05-03, so the Saturday-Monday span is a long weekend.
- **2027-06-05** — Saturday before 현충일 on Sunday 2027-06-06.

Saturdays in the same week as a mid-week holiday (no day-level collision):

- **2027-05-08** — week of 어린이날 (Wednesday 2027-05-05).
- **2027-05-15** — week of 부처님 오신 날 (Thursday 2027-05-13).

Saturdays adjacent to a recorded city event (not holidays):

- **2027-03-06** — day after AW 2027 closes (2027-03-05); COEX fully occupied that week.
- **2027-03-20** — day before 서울마라톤 2027 (Sunday 2027-03-21).
- **2027-04-17** — between AI EXPO KOREA (ends 2027-04-16) and WIS (starts 2027-04-21);
  the target_date placeholder happens to sit inside this dense AI fortnight.
- **2027-04-24** — between WIS (ends 2027-04-23) and 서울메타위크 (starts 2027-04-29).

Saturdays with no KR holiday adjacency and no recorded city event:
2027-01-09, 01-16, 01-23, 01-30, 02-13, 02-20, 03-13, 03-27, 04-03, 04-10, 05-22, 05-29,
06-12, 06-19, 06-26. Note 2027-04-03: the 2027 월력요항 also lists three *local* holidays
(4·3희생자 추념일, 동학농민혁명 기념일, 5·18민주화운동 기념일); those are regional, not
Seoul, and were not imported as rows, so 2027-04-03 is a normal Seoul Saturday here.

No date is recommended; these are awareness flags only.

## Deviations and open items

1. **Adjacency home resolved.** Per the manager ruling, `calendar_context.raw.json` keeps
   four keys and a **non-empty** `adjacent_events`; `adjacent_events.raw.json` was deleted
   so the package cannot self-contradict. The six-key context block described in
   `schemas.md` is the assembler's job later; nothing was fabricated here.
2. **`opportunity_kind` / `status` remain absent from `calendar_conflicts.json`** because
   `validate_calendar_conflict` rejects unknown keys and `schemas.md` confines those fields
   to `calendar_context.adjacent_events`. The three related rows therefore carry topic and
   severity in the conflicts file and the adjacency fields in the context file.
3. **`research_completed_on` = 2026-11-20** while `target_date` is 2027-04-17; every
   `accessed_on` is 2026-11-20, so all evidence predates the window by construction and
   every record keeps `needs_human_verify: true`.
4. **No price is dated to 2027.** All rates are 2026 tables; SETEC already runs a 2027
   rental recruitment with its own notice, so 2027 rates may differ.
5. **Community evidence quality varies** (organiser listings, self-reported attendance,
   one international operator) — see the caveats above; no dormant group was relabelled.

## What would change confidence

- A Saturday date hold at any venue and a written KRW quote including VAT.
- SETEC's per-room AV list and a confirmation that 09:00-17:00 is bookable on a 2027
  Saturday.
- Fresh 2027 dates from NextRise and Korea Blockchain Week.
- A rendered or logged-in check of the Korean pages that returned 404 to curl
  (gdg.community.dev events, parks.seoul.go.kr deep links).
