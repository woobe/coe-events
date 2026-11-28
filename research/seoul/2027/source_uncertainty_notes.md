# Source uncertainty notes — Seoul 2027 (seoul-kr), 2026-11-28

One entry per unresolved thing, written so a reviewer can check it against `captures/` and the JSON. Nothing here is an estimate dressed as a fact.

## 1. FX basis

- The ECB daily file is a dated reference rate (reference date 2026-11-27), not a 2027 rate and not a booking rate. Every USD figure is reproducible from `1 KRW = USD 0.00074912`; no figure has been re-based on a bank rate.
- VAT treatment differs by venue: 판교 states VAT included, DDP prints rates without a tax statement, 노들섬 and 마로니에 state VAT excluded, COCOC does not state it. Tax-excluded USD figures therefore understate the cash cost, and each such record carries a `final_quote` question.

## 2. Coordinates

- Ten distinct geocodes carry sixteen records; all sixteen records hold numeric `latitude`/`longitude`, and every pair is byte-for-byte the value in the captured Nominatim response named in `captures/INDEX.md`.
- **DDP** resolved to the plaza itself (37.5670686, 127.0098990, '281, 을지로, 을지로7가, 광희동, 04566'), **판교** to the innovation-centre building, **마로니에공원**, **노들섬 라이브하우스**, **KT&G 상상마당 빌딩** and **대화빌딩** all to their named points, and **COEX** to 513 영동대로 — these are building/POI matches.
- **Street-level matches (two records):** 한국컨퍼런스센터 (강남대로53길 8) and 성공 스페이스 (왕십리로 135) returned the street, not the building, and both disclose it inside the record.
- **성공 스페이스 is a road-segment point, not a building point (37.5600451, 127.0364011).** The pair is exactly what `captures/geo_seonggong.json` returns: display name '왕십리로, 행당동, 행당1동, 성동구, 04751', i.e. the 왕십리로 way itself. Seven Nominatim calls (the original address query plus six variants) and four Overpass queries all failed to return the 상가동 building; every response is stored in `captures/` and mapped in `INDEX.md` under '성공 스페이스 building-level lookups'. The record's `evidence.geo_note` says the same, so the coordinate is reproducible and honestly labelled — it locates the street, not the entrance. Confirming the actual pin and entrance is part of the venue inquiry, not a claim made here.
- **Rejected geocodes:** 남부순환로 1759 (관악청년청) returned a centroid in 구로구 and Overpass answered HTTP 400 on the name search, so that venue was dropped rather than recorded with a wrong-district point.

## 3. Prices withheld or unreadable

- **No published price (5 records):** COEX 컨퍼런스룸 300, COEX Studio 159, KT&G 상상마당 라이브홀, 스페이스쉐어 컨퍼런스 B룸, 성공 스페이스. All carry `estimated_cost_usd: null` with `cost_basis: unknown` and a `cost_unknown` question. None has been estimated.
- **Inquiry-only pages:** COEX routes conference-room pricing through an inquiry form; 스페이스쉐어 renders its fee table only after a date is selected; 성공 스페이스 is '유료' with the amount handled by phone; KT&G requires email application and review. Korean venue sites are frequently inquiry-only and these are recorded as such rather than inferred.
- **Client-rendered tables not captured:** SETEC (fee table), 서울창업허브 공덕 (room rows), 마포구청 (fee table), 강남구 유휴공간 (fee images). Those venues are excluded, not estimated.

## 4. Capacity gaps

- **No published headcount (2 records):** 노들섬 노들라운지 states '수용인원 행사 운영에 따라 상이' (varies by event); KT&G 상상마당 publishes no capacity for the live hall. Both are `lead` with `capacity_comfortable: 0` and a `capacity` question.
- **Ambiguous headcount (1 record):** 몽상가들 prints '최대 70인 이용 가능' under a general use note while the only published rate is for the 서브 세미나룸, so the room the 70 applies to is unconfirmed; the record is a `lead` with `capacity` and `cost` questions.
- **Stated range (2 records):** DDP 잔디사랑방 is '약 150~200명' (150 recorded as the conservative end); 마로니에공원 is '최대 50명(권장)~100명 이내' (100 recorded).
- **Conflict with the earlier bundle:** COEX 컨퍼런스룸 300 was recorded as 114 persons in `research/seoul/2026-q4/`; today's official page gives a 20-300 range across the 남 3F rooms and no per-room figure. The new record uses 300 with `capacity_basis: venue_claim` and a `capacity` question naming the conflict; the old figure is not adopted because it cannot be re-verified.

## 5. Calendar unknowns

- **KBW2027 (Korea Blockchain Week):** the organiser site presents KBW2027 participation applications but prints no 2027 dates; the 2026 edition ran 2026-09-29..10-01 at Walkerhill. Recorded as an unknown-date note, not a row, and the historical September pattern is explicitly not used as a prediction.
- **UDC (Upbit D Conference):** the UDC site states 2026 is devoted to "reflection, renewal, and preparation", and no 2027 edition is announced. Unknown-date note; no row.
- **Korea Fintech Week 2027 / Seoul Fintech Week 2027 / Seoul Fashion Week 2027 F/W:** only 2026 editions are published (Korea Fintech Week 2026 ran 2026-11-25..27 at aT센터; Seoul Fashion Week's "2027 S/S" edition ran in September 2026, which is outside the 2027 calendar year). Unknown-date notes; no rows.
- **ETH Seoul:** the newest edition found is 2024-03-29..31; no 2025, 2026 or 2027 page was located. Unknown-date note plus a dormant community record.
- **Hackathons:** the only 2027 Seoul hackathon seen was listed by an aggregator (koreahackathons.com shows 'OOO Seed 04' on 2027-01-24 and two AI hackathons on 2026-12-11 and 2026-12-12); no organiser page with a 2027 date could be captured, so no hackathon row is recorded. The aggregator listing is not acceptable final evidence.
- **Physical AI EXPO KOREA 2027** is dated but held in Songdo (Incheon); **World Smart City Expo 2027** is dated but held in Busan. Only the Incheon event is recorded (low severity), because Busan is outside the Seoul metro audience.
- **KR public holidays:** taken only from the registry edition 2027년 월력요항 (설날 2027-02-06..08 + substitute 02-09; 추석 2027-09-14..16; 20 rows in total). The captured KASA page (`captures/kasa_2027_calendar.html`) does not render the holiday table, so no calendar row cites it; the dates are used for context only.

## 6. School lane — declared unknown

- `KR:seoul` exists as a jurisdiction ID in `references/school_holidays.json` but carries **no holiday rows and no coverage rows**. The Seoul office of education publishes no city-wide academic calendar (its 2027학년도 guidance prints the 학사일정 only as an example), so each school sets its own 방학·개학 dates.
- Consequently **no Seoul school-break date is asserted anywhere in this package**, and there is no school row in `calendar_conflicts.json`.

## 7. Platform lane

- The registered platform for Korea is **space-cloud** (active). The lane was opened with four listing captures and closed with **nothing carried**: listings publish price, capacity and amenities but withhold the exact address until booking, which makes the coordinate requirement unsatisfiable from the listing alone.
- Aggregators (shareit.kr, naver blogs, public-data mirrors such as junkangworld and platformdodam) were used for discovery only; no record cites one as its source.

## 8. Alcohol

- No venue page in this set publishes an alcohol permission for a rented hall. Every one of the sixteen records carries an explicit licence question (permitted? which event liquor licence? who holds it?), including DDP, COCOC, COEX, 판교 and 노들섬.
- 몽상가들 is the only venue that mentions alcohol at all: '음식물 및 주류 반입시 별도 협의 필수' (food and alcohol brought in require separate consultation) — recorded as a consultation requirement, not as permission, and the licence holder is still asked.

## 9. Station access

- Stated from a captured page: COCOC (Gangnam exit 5, 2 minutes), 판교 (Pangyo exit 4, about 17 minutes), 상상마당 (Hongik University exit 9 / Hapjeong exit 3), 스페이스쉐어 삼성 (Samsung exit 8, 2 minutes), 몽상가들 (five minutes from a station; the station name is not published).
- Not published on any captured page: DDP (the site's directions pages answered 404 today), COEX (no text route on the captured pages), 노들섬 (rental pages carry the address only), 마로니에공원, 성공 스페이스. These are recorded as unknown with an availability question rather than a guessed station name.

## 10. Opening windows

- DDP Design Lab and 노들섬 both open at 10:00, so the brief's 09:00-21:00 window cannot be met there; the records state the printed 10:00 window and carry an availability question. They do support an evening finish.
- COCOC states 24-hour operation; 스페이스쉐어's standard bands end at 18:00 with a separate 19:00-22:00 night band; 판교 closes at 17:00. None of these is presented as a confirmed booking.
