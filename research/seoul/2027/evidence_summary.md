# Seoul 2027 — evidence summary (deep refresh, Run A)

Prepared by: jnr-research (Kanban t_fadad6d5)
Research date: **2026-11-28**
Work root: `/home/joe/repo_dev/coe-events/research/seoul/2027/`
Prior bundles: `research/seoul/2026-q4/`, `2027-h1/`, `2027-q1/`, `2027-q2/` — read as a lead list only, never edited, never cited as evidence.

## 1. What is in this package

- `city_input.json` — city research input, 1 record, no date window, no `target_date`
- `venues.raw.json` — venue (schema 2.4), **16 records**
- `venues.shortlist.json` — scorer output, 16 records, byte-identical on re-run
- `calendar_conflicts.json` — calendar_conflict, **7 records** (bare array)
- `communities.raw.json` — local_community, **14 records**
- `captures/` + `INDEX.md` — **74 captured files**, all 74 named in the index, 0 orphans (63 from the first pass plus 1 DDP 운영시간 page and 10 failed geocoding responses during the review fix round)
- `fx_evidence_2026-11-28.md`, `source_uncertainty_notes.md`, `venue_discovery_log.md`, `community_discovery_log.md`

Validator exit codes (whole file and per record):

```
$ python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py venue research/seoul/2027/venues.raw.json
PASS: research/seoul/2027/venues.raw.json is valid [venue]                       # exit 0
$ python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py calendar_conflict research/seoul/2027/calendar_conflicts.json
PASS: research/seoul/2027/calendar_conflicts.json is valid [calendar_conflict]    # exit 0
$ python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py local_community research/seoul/2027/communities.raw.json
PASS: research/seoul/2027/communities.raw.json is valid [local_community]         # exit 0
per-record venue validation:       16 / 16 passed
per-record calendar validation:     7 / 7 passed
per-record community validation:   14 / 14 passed
```

## 2. Scorer output — tiers and top five

```
$ python3 ~/.hermes/skills/plan-event/scripts/score_venues.py research/seoul/2027/venues.raw.json \
    --output research/seoul/2027/venues.shortlist.json --budget-usd 5000 --target-attendance 50
eligible: 0
shortlist_ready: 12
lead: 4
top selectable: DDP 동대문디자인플라자 — 서울-온 화상스튜디오 (Seoul-On Studio, Design Lab 2F) (score 0.8506, tier shortlist_ready)
```

Byte identity and hash:

```
$ cmp research/seoul/2027/venues.shortlist.json /tmp/sl_fix1.json && echo "shortlist byte-identical"
shortlist byte-identical
$ sha256sum research/seoul/2027/venues.shortlist.json
03b8330536dfb55dfb6dbbcae3ed49f59357ee01bc8b97c81149e96c7c34d583
```

The hash differs from the first-pass `5425f9e5…` only because the review fix round changed one coordinate pair and the DDP/성공 스페이스 evidence text; every score and tier is identical to the first pass.

Top five (from `venues.shortlist.json`):

```
0.8506  DDP 서울-온 화상스튜디오 (80)                    USD 1,985.92  shortlist_ready
0.8453  한국컨퍼런스센터 컨퍼런스룸 A (54)               USD 1,054.76  shortlist_ready
0.7746  판교 경기창조경제혁신센터 대회의실 (68)          USD   197.77  shortlist_ready
0.7649  DDP 디자인랩 디자인홀 (110)                     USD 2,439.13  shortlist_ready
0.6750  COEX 스튜디오 159 (100)                         cost unpublished  shortlist_ready
```

Full tier breakdown:

- **shortlist_ready (12):** DDP 서울-온 (0.8506), COCOC 컨퍼런스룸 A (0.8453), 판교 대회의실 (0.7746), DDP 디자인홀 (0.7649), COEX Studio 159 (0.6750), 마로니에공원 다목적홀 (0.6464), COCOC 대강당 (0.6150), DDP 잔디사랑방 (0.5855), 스페이스쉐어 컨퍼런스 B룸 (0.5500), 성공 스페이스 (0.5250), 판교 국제회의장 (0.5034), 노들섬 라이브하우스 (0.4126).
- **lead (4):** COEX 컨퍼런스룸 300 (material capacity question), KT&G 상상마당 라이브홀 (capacity and cost unknown), 노들섬 노들라운지 (no published headcount), 몽상가들 서브 세미나룸 (room/capacity and cost ambiguity).
- **eligible (0):** expected — every record carries at least one soft verification question, and the scorer reserves `eligible` for fully evidenced venues with no questions.

Tier counts differ from what the raw price list suggests because the scorer treats a material question (capacity, cost basis, location) as a lead even when the price is published: that is why COEX 300, 노들라운지 and 몽상가들 sit in `lead` despite having a published rate.

## 3. Coordinates audit

```
venues: 16
numeric coordinate pairs: 16 / 16
records with evidence.geo URL: 16 / 16
latitude range: 37.400339 .. 37.5805083
longitude range: 126.8856839 .. 127.1048351
distinct coordinate pairs: 10
```

Ten points carry sixteen records because DDP has three rooms, COEX two, COCOC two, 노들섬 two and 판교 two. Every pair is a JSON number, never a string, and every pair equals the value in its captured Nominatim response. Fourteen records resolve to a building or POI (DDP ×3, COEX ×2, 판교 ×2, 마로니에공원, 노들섬 ×2, 상상마당, 대화빌딩); two are street-level — COCOC (both rooms) on 강남대로53길, and 성공 스페이스, the one road-segment point (37.5600451, 127.0364011), labelled as such in the record's `evidence.geo_note`, in `captures/INDEX.md` and in `source_uncertainty_notes.md` §2. The ten failed building-level lookups for that address are kept as captures so the label is auditable.

## 4. FX basis and three hand recomputations

Basis (see `fx_evidence_2026-11-28.md`): ECB `eurofxref-daily.xml`, fetched 2026-11-28, reference date printed 2026-11-27 — EUR 1 = USD 1.0957, EUR 1 = KRW 1462.65 → USD 1 = KRW 1334.9001, 1 KRW = USD 0.00074912.

1. DDP 디자인홀, KRW 3,256,000 × 0.00074912 = 2,439.1347 → **USD 2,439.13** (reverse: 2,439.13 / 0.00074912 = 3,255,994 KRW, within 6 KRW).
2. 판교 대회의실, KRW 264,000 × 0.00074912 = 197.7677 → **USD 197.77** (reverse: 263,999 KRW).
3. 노들섬 라이브하우스, KRW 4,000,000 × 0.00074912 = 2,996.48 → **USD 2,996.48**.
4. (rate-estimate cross-check) COCOC 컨퍼런스룸 A, KRW 176,000 = USD 131.84512/h × 8 = 1,054.76096 → **USD 1,054.76**.

All eleven priced records reproduce at two decimals from that single rate; there is no cent-level exception in this bundle.

## 5. Calendar disposition

- **7 rows, all inside calendar year 2027** (2027-04-14 through 2027-10-15). `related` 6, `major_other` 1.
- `related`: AI EXPO KOREA 2027 (04-14..16, COEX Hall A, `ai`, medium), World IT Show 2027 (04-21..23, COEX, `ai`, medium), Seoul Meta Week 2027 (04-29..30, COEX Grand Ballroom, `ai`, high), AI Summit Seoul & Expo 2027 (08-11..13, COEX, `ai`, high), Physical AI EXPO KOREA 2027 (09-09..11, Songdo Convensia, Incheon, `ai`, low), KES 2027 COEX leg (10-12..15, COEX, `ai`, low).
- `major_other`: 코리아빌드위크 하반기 (08-04..07, COEX, `other`, `none`) — four-day construction expo at COEX; logistics vocabulary (hotel, transport, venue availability) is in `evidence.observed_facts` and the question is logistics-framed.
- **Unknown-date notes** (no row, because no organiser page prints a 2027 date): Korea Blockchain Week 2027 (applications open, no dates), UDC / Upbit D Conference 2027 (2026 devoted to a pause, no 2027 edition), Korea Fintech Week 2027, Seoul Fintech Week 2027, Seoul Fashion Week 2027 F/W (the "2027 S/S" edition ran in September 2026), ETH Seoul 2025/2026/2027, and the hackathon lane (only aggregator-dated 2027 listings, no organiser page).
- **Holidays** come only from the KR registry rows (설날 2027-02-06..08 + substitute 02-09; 추석 2027-09-14..16; 20 rows, edition 2027년 월력요항, 우주항공청공고 제2026-0078호). They inform date context; no calendar row cites a holiday.
- **Seoul school lane: declared unknown.** `KR:seoul` exists as an ID with no holiday rows and no coverage rows, so no Seoul school-break date is asserted anywhere.

## 6. Community disposition

- **14 records:** 4 `active`, 5 `intermittent`, 5 `dormant`.
- Active — a dated in-person activity on the group's own page, either in the past 12 months or announced for the near term: 모두의연구소 (MODUCON 2026 printed as '12월 12일(토) 10:00 - 18:00 / 이화여대 ECC'; the same page carries a study session marked 모집완료, '[2회차 마감] RL과 VLA로 만나는 Physical AI - 로봇 프로그래밍 | (11.21)'), PyTorchKR (KVCache Meetup Korea 2026-09-30 at 드림플러스 강남; DeepDive 2026-11-22 at 스페이스쉐어 하모니홀), AI Tinkerers Seoul (next event 2026-12-31), GDG on Campus Dongguk University (2026-05-08).
- Intermittent: GDG Korea WebTech (1,163 members, no dated 2026 event rendered), 서울 AI 허브, AI Network, 디센터, Hashed.
- Dormant: GDG Campus Korea (727, newest event 2020), Seoul AI Meetup (318, newest 2025-03-20), SeoulWeb3 (534, newest 2023-04-27), 한국블록체인협회 (2023 notices), ETH Seoul (2024 edition).
- **No co-host badge anywhere:** `cohost_open` is false on all 14 because no group's own page carries quotable co-host solicitation language. Every record has a public HTTPS contact route; no email address or phone number appears in `contact_info`.

## 7. Which old-run (2026-q4) fields changed after re-verification

The August 2026 bundle is untouched. These are the fields today's live pages contradict, cannot support, or fill in:

1. **DDP — Design Hall cost.** Old: `null` with `cost_basis: unknown`. Today: 3,256,000 KRW per 11-hour day = USD 2,439.13, published in the rental page's 디자인랩 대관료 table; the 10:00-21:00 Design Lab window is printed on the separate DDP 대관정보서비스 facility page (`deep.ddp.or.kr/introduce/c003.do`, captured this round), not on the rental-fee page. This is the single largest evidence gain in the package.
2. **DDP — Conference Hall (414 m²) dropped.** Old: capacity 0, USD 2,768.66. Today the DDP rooms that can be evidenced at 50-person scale are the Design Hall, the Jandi-sarangbang and the Seoul-On studio; the old "Conference Hall" row has no matching room page in the captured table and was not carried.
3. **COEX — Conference Room 300 capacity conflict.** Old: 114 persons. Today: the official page gives a 20-300 person range across the 남 3F block and no per-room figure, so the record uses 300 with a `capacity` question naming the old 114; it is a `lead`, not a shortlist row. Old cost `null` is unchanged.
4. **Nodeul Island — Livehouse price and basis.** Old: USD 4,251.48 from a 2026-08-15 page. Today: KRW 4,000,000 weekend one-performance rate, VAT excluded = USD 2,996.48; the fee table and its `VAT 별도` note are now captured, and the 2026 open-call limit (to 2026-10-31) plus the Art Island project are recorded as an availability question.
5. **Mongsang Space — tier and cost basis.** Old: `shortlist_ready`, 50 persons, USD 561.20 from a main-hall rate estimate. Today: the main hall is quote-only; the only published rate is the 서브 세미나룸 (55,000 KRW/h weekend), the '최대 70인' line is not tied to a room, and the record is a `lead` at USD 329.61 with material capacity and cost questions.
6. **KT&G SangSangMadang — unchanged status, sharper evidence.** Old and new are both `lead` with no capacity and no cost; the new record adds the four-step application process, the seven-day review and the absence of any published rate or headroom.
7. **Calendar — 7 rows to 7 rows, different set.** Old bundle carried 7 Q4-2026 rows; this run carries 7 verified 2027 rows plus six unknown-date notes. Only AI EXPO KOREA and COEX-based events survive in recognisable form, and the whole set is now organiser-dated.
8. **Communities — 10 records to 14.** Old: 10 Seoul records. New: 14, each with a dated own-page activity claim or an explicit dormant label, and 5 dormant groups are labelled rather than left implied-active.
9. **Coordinates — added.** Old bundle had `null` latitude/longitude on all six venues (`map_location_unknown`); this run has 16/16 numeric pairs inside the Seoul/Pangyo envelope, each with a captured geocoder response. Fifteen records are building/POI or street-level matches and one, 성공 스페이스, is a captured road-segment point labelled as such rather than presented as door-precise.
10. **FX basis — moved forward.** Old: ECB 2026-08-15. New: ECB 2026-11-27 (1 KRW = USD 0.00074912), which moves every USD figure independently of price changes.
11. **New venues not in the old set (11):** DDP 잔디사랑방, DDP 서울-온 화상스튜디오, COCOC 대강당, COCOC 컨퍼런스룸 A, COEX Studio 159, 판교 대회의실, 판교 국제회의장, 마로니에공원 다목적홀, 노들섬 노들라운지, 스페이스쉐어 삼성 컨퍼런스 B룸, 성공 스페이스.
12. **Old-set venues not carried (1):** DDP Conference Hall (414 m²) — no matching room-level page in the captured table.

## 8. Zero date commitments

Grepped across everything except `captures/`, for the five phrases the card names (written here in hyphenated form so this audit block is not itself a match):

```
$ for p in recommended-date preferred-date candidate-Saturday target-date we-recommend; do
    printf '%s: ' "$p"; grep -rIo --exclude-dir=captures -i "${p//-/ }" . | wc -l; done
recommended-date: 0
preferred-date: 0
candidate-Saturday: 0
target-date: 0
we-recommend: 0
```

Before this pass the same five phrases appeared verbatim inside this section, so the grep matched its own audit block; the hyphenated form makes the count a real zero.

`city_input.json` carries `target_date: null` and `date_window: null`; `score_venues.py` was run without `--event-date`; `score_dates.py` was not run. The only "recommend" strings in the bundle are the disclaimers that no date is recommended.

## 9. Evidence discipline notes for the reviewer

- **Facts vs inference** are separated inside every record: `evidence.observed_facts` is page content with the fetch date, `evidence.inference` is my reading. Nothing in `inference` is presented as a source claim.
- **Rate arithmetic** that is not a printed package is labelled in the record (`estimated_from_rate` with `estimated_hours: 8`, `rate_estimate_note`, and a `final_quote` question): COCOC 컨퍼런스룸 A, 몽상가들 서브 세미나룸, 마로니에공원 다목적홀.
- **Alcohol** is treated as a licensing question on all 16 records; 몽상가들's "food and alcohol require separate consultation" is recorded as a consultation requirement, not permission.
- **Korean venue sites are often inquiry-only** and that is recorded rather than guessed: 5 of 16 records have no cost, 2 have no capacity, and 1 has an ambiguous room/price mapping.
- **Review round 1 fixes (this revision):** 성공 스페이스 coordinates replaced with the captured road-segment point and labelled in three places (record `evidence.geo_note`, `captures/INDEX.md`, `source_uncertainty_notes.md` §2), with all ten failed building lookups kept as captures; the DDP 10:00-21:00 window re-cited to the captured DDP 대관정보서비스 Design Lab page that prints it, and the fee-only rental page no longer cited for hours; the station count in `venue_discovery_log.md` corrected to 6 stated / 10 not stated; the Modulabs over-claim replaced with the activity its captured page prints. Venue count, tiers and scores are unchanged by the fix round.
- **No store, page, publish or git work was done.** No `city.json`, no `index.html`, no `published-cities.json`, no commit, no sentinel; `research/seoul/2026-q4/`, `2027-h1/`, `2027-q1/` and `2027-q2/` were not modified.

## 10. Open questions for Joe / the reviewer

1. Five venues cannot be priced from their own pages (COEX x2, 상상마당, 스페이스쉐어, 성공 스페이스). Do you want inquiry emails sent now, or should the priced twelve be narrowed first?
2. DDP and 노들섬 open at 10:00 and 판교 closes at 17:00 — none of the three supports the 09:00-21:00 window in full. Is the 10:00-21:00 or 09:00-17:00 compromise acceptable for those venues?
3. COEX 컨퍼런스룸 300 carries an unresolved capacity conflict (114 in the old bundle vs a 20-300 range today). Should the office confirm the room before it is considered at all?
4. The active community set is small (4 active of 14; 5 dormant). The dormant groups are large (727 / 534 / 318 members) but have not published an event in 12+ months — is a reactivation outreach worth trying, or should the 2027 plan rely on Modulabs, PyTorchKR, AI Tinkerers and the GDG campus chapter?
5. KBW2027, UDC, Korea/Seoul Fintech Week, Seoul Fashion Week F/W and ETH Seoul are all unannounced. Should a spring-2027 calendar re-sweep be scheduled as a follow-up card?
6. The Seoul school lane is unknown by registry design. Should a Seoul school-authority row be added in the next registry card, or is the school lane out of scope for Seoul?
