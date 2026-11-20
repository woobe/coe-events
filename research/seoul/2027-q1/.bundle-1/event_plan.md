# Event Plan: Seoul (seoul-kr) — Run A: Venue & Date

- Schema version: 2.4
- Phase: venue
- City: Seoul (seoul-kr), South Korea
- Target date: 2027-03-06
- Date window: 2027-01-01 through 2027-03-31
- Target attendance: 50
- Currency: KRW (Budget/scoring currency is USD; venue-local costs are recorded in KRW (cost_local_amount/cost_local_currency KRW).; USD equivalent at the ECB euro foreign exchange reference rate dated 2026-11-20 (EUR 1 = USD 1.0990; EUR 1 = KRW 1472.04), fetched 2026-11-20 from https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml (Cube time='2026-11-20'); derived 1 KRW = USD 0.000746583 (1.0990 / 1472.04), i.e. 1 USD = 1339.44 KRW. Every converted KRW amount in venues.raw.json records this dated basis; where no dated conversion basis applies the USD equivalent stays null with a question. No FX rate is invented.; KRW amounts quoted from official rate tables that state '부가가치세 별도' (VAT excluded) are converted as published; VAT and any 부대비용 remain open verification questions, not assumptions.)
- Soft budget: USD 5000 (over-budget venues stay selectable with Joe's approval)
- Event duration: 8 hours (requested local window 09:00-17:00)
- Generated: 2026-11-20T00:00:00Z

## Executive Summary

- Top selectable venue: SETEC 컨벤션센터 — 세미나실 2 (166㎡, 80석) (score 0.5273) — tier shortlist_ready
- Eligible venues: 0; shortlist-ready: 6; leads: 7
- Speaker candidates: deferred to Run B after venue selection
- Calendar awareness: 5 record(s) — 3 related-event opportunity/relevance, 2 major-city logistics — informational, never eliminations
- Open questions: 112
- Recommendation: none selected yet

## Calendar flags for Joe — informational, not eliminations

Calendar awareness has two categories in schema 2.4: related-event opportunity/relevance and major-city logistics. Neither category scores, tiers, selects, or rejects a venue; these flags are awareness only.

- AW 2027 (Automation World / 스마트공장·자동화 전시회) — 2027-03-03 to 2027-03-05 (major-city logistics) — [전시회 개요 — AW 2027](https://www.automationworld.co.kr/overview-exhibition?hl=ko). This is a logistics awareness flag for Joe's decision; it never removes the date automatically.
- 서울마라톤 2027 (제97회 동아마라톤 겸 서울마라톤) — 2027-03-21 to 2027-03-21 (major-city logistics) — [서울마라톤, 8년째 세계 최고 '플래티넘' 인증 (동아일보, 2026-11-20)](https://www.donga.com/news/article/all/20261120/135057511/2). This is a logistics awareness flag for Joe's decision; it never removes the date automatically.
- AI EXPO KOREA 2027 (국제인공지능대전) — 2027-04-14 to 2027-04-16 (related-event opportunity, relevance: ai) — [전시회 개요 — AI EXPO KOREA 2027](https://aiexpo.co.kr/%EC%A0%84%EC%8B%9C%ED%9A%8C-%EA%B0%9C%EC%9A%94). This is an awareness flag for Joe's decision; it never removes the date automatically.
- 월드IT쇼 2027 (World IT Show 2027, WIS) — 2027-04-21 to 2027-04-23 (related-event opportunity, relevance: ai) — [월드IT쇼 (WIS) | 코엑스 BUSINESS](https://business.coex.co.kr/post-exhibitions/%EC%9B%94%EB%93%9Cit%EC%87%BCwis/). This is an awareness flag for Joe's decision; it never removes the date automatically.
- 서울메타위크 2027 (Seoul Meta Week 2027) — 2027-04-29 to 2027-04-30 (related-event opportunity, relevance: ai) — [서울메타위크 2027 | 대한민국을 대표하는 AI 컨퍼런스](http://seoulmetaweek.com/ko). This is an awareness flag for Joe's decision; it never removes the date automatically.

## Venue Shortlist (eligible, ranked)

- No fully evidenced eligible venues.

## Shortlist-Ready Venues (manual checks remain; selectable by Joe)

1. SETEC 컨벤션센터 — 세미나실 2 (166㎡, 80석) (tier shortlist_ready, score 0.5273) — capacity 80 (venue_claim), screen unknown, wifi unknown, cost USD 567.4 / 760000 KRW (published_rate), catering unknown
   - Flags: screen_unknown, wifi_unknown, availability_unconfirmed, final_quote_required, stale_evidence
   - Cost rate unit: day
   - Event window: allows_to_5 (closing 21:00) (opening 08:00-21:00 (대관 시간대 08~12 / 13~17 / 18~21))
   - Source: [컨벤션센터 대관 — 사용료 (official SETEC page): 세미나실2 166㎡, 8~17시(전일 8H) 760,000원, 부가가치세 별도](https://www.setec.or.kr/front/rent/rent05.do)
   - Booking: [https://www.setec.or.kr/front/rent/rent01.do](https://www.setec.or.kr/front/rent/rent01.do)
   - Unresolved: Confirm Saturday availability for a 09:00-17:00 event in 세미나실 2 on the specific date (the official page publishes no weekday/weekend band).
   - Unresolved: Confirm screen/projection in 세미나실 2 (the official rate page publishes only 면적 and 사용료; the room equipment list is published per room elsewhere).
   - Unresolved: Confirm attendee Wi-Fi in 세미나실 2 (not stated on the official rental pages).
   - Unresolved: Confirm the all-in price: KRW 760,000 for 8~17시, 부가가치세 별도; confirm VAT and any 장비/부대시설 charges.
   - Unresolved: Confirm booking terms and the operator's acceptance of a free community tech event under the standard 컨벤션센터 대관 procedure.
2. SETEC 컨벤션센터 — 세미나실 1 (189㎡, 100석) (tier shortlist_ready, score 0.5234) — capacity 100 (venue_claim), screen unknown, wifi unknown, cost USD 664.46 / 890000 KRW (published_rate), catering unknown
   - Flags: screen_unknown, wifi_unknown, availability_unconfirmed, final_quote_required, stale_evidence
   - Cost rate unit: day
   - Event window: allows_to_5 (closing 21:00) (opening 08:00-21:00 (대관 시간대 08~12 / 13~17 / 18~21))
   - Source: [컨벤션센터 대관 — 사용료 (official SETEC page, setec.or.kr): 시간대별 사용료, 세미나실1 189㎡, 8~17시(전일 8H) 890,000원, 부가가치세 별도](https://www.setec.or.kr/front/rent/rent05.do)
   - Booking: [https://www.setec.or.kr/front/rent/rent01.do](https://www.setec.or.kr/front/rent/rent01.do)
   - Unresolved: Confirm Saturday availability for a 09:00-17:00 event on the specific date: the official rate table publishes time slots (08~12 / 13~17 / 18~21) but states no weekday/weekend band, and the online booking system (컨벤션센터 온라인 예약) is the only availability source.
   - Unresolved: Confirm screen/projection in 세미나실 1: the official rate page lists 면적 and 사용료 only; the room equipment list is published per room elsewhere and a projector/screen is not confirmed for this room.
   - Unresolved: Confirm attendee Wi-Fi in 세미나실 1 (not stated on the official rental pages).
   - Unresolved: Confirm the all-in price for an 8-hour Saturday event: KRW 890,000 is the published 8~17시 rate, 부가가치세 별도 (VAT excluded); confirm VAT, 시간외 (110,000/hour), and any 부대시설 or 장비 charges.
   - Unresolved: Confirm booking terms: 사업자등록증 and 행사계획서 are required for the application, and payment must be settled within 3 days of 대관 허가.
3. DDP — 디자인홀 (Design Lab 3F, 627.6㎡, 약 110명) (tier shortlist_ready, score 0.4778) — capacity 110 (venue_claim), screen confirmed, wifi unknown, cost USD 2430.87 / 3.256e+06 KRW (published_rate), catering unknown
   - Flags: wifi_unknown, availability_unconfirmed, final_quote_required, stale_evidence
   - Cost rate unit: day
   - Event window: allows_to_5 (closing 20:00) (opening 08:00-20:00 (컨벤션 기준시간 12시간))
   - Source: [디자인홀 — 공간안내 (official DDP page): 디자인랩 지상 3층, 수용인원 약 110명, 627.6㎡, 디자인랩 대관료 디자인홀 시간당 296,000 / 3시간 888,000 / 1일 3,256,000, LED 디스플레이 6.4m X 4m](https://www.ddp.or.kr/?menuno=714)
   - Booking: [https://www.ddp.or.kr/?menuno=714](https://www.ddp.or.kr/?menuno=714)
   - Unresolved: Confirm Saturday availability for 09:00-17:00 on the specific date (DDP rentals run through an application + 대관심의 committee; the published window is a daily basis time, not an availability calendar).
   - Unresolved: Confirm attendee Wi-Fi in 디자인홀 (the official page lists display, audio, power and furniture but no attendee Wi-Fi).
   - Unresolved: Confirm whether the published 1일 기준 KRW 3,256,000 includes VAT and whether the 8-hour 09:00-17:00 use is billed as 1일 기준 (the table gives 시간당 296,000 / 3시간 888,000 / 1일 3,256,000 with no VAT statement on the rendered page).
   - Unresolved: Confirm booking terms for a free community event (DDP requires 대관 신청 and committee review; approval lead time and deposit terms are not published).
4. COEX — 컨퍼런스룸 300호 (264㎡, 강의식 114석) (tier shortlist_ready, score 0.4500) — capacity 114 (seated), screen confirmed, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering unknown
   - Flags: cost_unknown, wifi_unknown, availability_unconfirmed, duration_unconfirmed, stale_evidence
   - Event window: unknown
   - Source: [컨퍼런스룸 (남) 3F — 회의실 안내 (official COEX BUSINESS page): 300호 264㎡, 강의식 114석 / 극장식 225석 / 연회식 90석, LED 6.5m x 2.5m](https://business.coex.co.kr/meeting-room/conference-room-3f/)
   - Booking: [https://business.coex.co.kr/meeting-room/conference-room-3f/](https://business.coex.co.kr/meeting-room/conference-room-3f/)
   - Unresolved: Confirm the rental fee for 300호: COEX publishes room specs and an 임대관련자료 board, but no rate for this room is exposed on the public pages, so a written quote is required.
   - Unresolved: Confirm the usable daily window and whether a 09:00-17:00 eight-hour Saturday block is bookable (COEX publishes no meeting-room hours on this page).
   - Unresolved: Confirm Saturday availability (the COEX exhibition calendar shows weekend exhibitions, which is not evidence of meeting-room availability).
   - Unresolved: Confirm attendee Wi-Fi in 300호 (the page lists A/V, fixed projector, interpretation booth and stage for rooms ≥207㎡, but not Wi-Fi).
   - Unresolved: Confirm booking terms and whether a free community event is accepted (COEX runs 대관 공고 notices and a separate business rental channel).
5. 서울시 어울림플라자 — 다목적강당 (70~100명) (tier shortlist_ready, score 0.3250) — capacity 100 (venue_claim), screen unknown, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering unknown
   - Flags: cost_unknown, screen_unknown, wifi_unknown, availability_unconfirmed, duration_unconfirmed, map_location_unknown, stale_evidence
   - Event window: unknown (closing 22:00) (opening 대관 시간대 10:00-14:00 / 14:00-18:00 / 18:00-22:00 (공연장 기준 표기))
   - Source: [대관 안내 (official 서울시 어울림플라자 page): 다목적강당 수용인원 70~100명, 시설 대관료 다목적강당 350,000~540,000원, 토·일·공휴일 20% 가산 조항](https://seouleoullim.or.kr/site/reserve/info)
   - Unresolved: Confirm the 다목적강당 rental fee and its unit: the official '어울림플라자 시설 대관료' table lists 다목적강당 350,000 ~ 540,000원 but the per-row 내용 column (which states '1회(4시간) 단가' for 공연장 and '시간당 단가' for 문화센터 1,2) is not repeated for 다목적강당, so the unit for this row is not published.
   - Unresolved: Confirm Saturday availability and the 20% 토·일·공휴일 surcharge that the table applies to 문화센터/문화교실/연수객실 rows ('토, 일, 공휴일은 기존금액의 100분의 20을 가산함') — whether it applies to 다목적강당 as well.
   - Unresolved: Confirm screen/projection: the 시설별 대여가능장비 list for 다목적강당 is '음향, 조명, 거울' with no screen or projector (세미나실 rows do list 빔프로젝터).
   - Unresolved: Confirm attendee Wi-Fi (not stated on the official rental page).
   - Unresolved: Confirm the usable daily window: the published slot table is written for 공연장 (10:00-14:00 / 14:00-18:00 / 18:00-22:00); confirm that a 다목적강당 event can run 09:00-17:00 or 10:00-18:00 for eight hours.
   - Unresolved: Confirm booking terms: 온라인 신청 at least 7 days before use, 내부 심사 and 승인 통보, then payment; 취소 refunds are 100% at 10+ days and 80% under 10 days.
6. 노들섬 라이브하우스 (Nodeul Island Livehouse, 1F, 1,320㎡) (tier shortlist_ready, score 0.1708) — capacity 456 (venue_claim), screen unknown, wifi unknown, cost USD 4479.5 / 6e+06 KRW (published_rate), catering unknown
   - Flags: oversized_capacity, screen_unknown, wifi_unknown, availability_unconfirmed, final_quote_required, stale_evidence
   - Cost rate unit: event
   - Event window: allows_to_5 (closing 23:00) (opening 공연대관 10:00-23:00; 준비·철수대관 10:00-22:00)
   - Source: [라이브하우스 대관 — 대관료 안내 (official Nodeul Island page): 토,일,공휴일 공연 1회 4,000,000원 / 2회 6,000,000원 (VAT 별도), 공연 대관 시간 10시~23시](https://nodeul.org/rent/rent-livehouse/)
   - Booking: [https://nodeul.org/rent/rent-livehouse/](https://nodeul.org/rent/rent-livehouse/)
   - Unresolved: Confirm Saturday availability for the specific date: the official rent calendar (nodeul.org/rent-calendar/?calendar_type=rent-livehouse) shows per-day availability and the hall runs an active concert schedule.
   - Unresolved: Confirm whether an 09:00 start is possible: the official performance window is 10:00-23:00, so an 09:00-17:00 window is not covered by published hours (a 10:00-18:00 window is).
   - Unresolved: Confirm screen/projection: the facility page lists sound, lighting and instrument equipment, a house manager and four ushers, but no presentation screen or projector.
   - Unresolved: Confirm attendee Wi-Fi (not stated on the facility page).
   - Unresolved: Confirm the all-in price for an 8-hour Saturday event: 토,일,공휴일 2회 rate KRW 6,000,000 applies because a single performance over 3 hours is billed as 2회 (VAT excluded); 준비·철수 대관 is a separate KRW 1,067,000 per slot on weekends.
   - Unresolved: Confirm that a non-concert community/tech event is accepted at the performance-rental rate and terms (대관 공고 → 신청 → 심의 → 계약).

## Venue Leads (not selectable until re-evidenced)

- [그라운드옥탑] 강남역 100인 세미나·강의장 (Space Cloud listing 68421) (tier lead, score unknown) — capacity 100 (venue_claim), screen confirmed, wifi confirmed, cost USD 1194.53 / 1.6e+06 KRW (estimated_from_rate), catering unknown
   - Flags: availability_unconfirmed, final_quote_required, map_location_unknown, stale_evidence
   - Tier notes: material verification question(s): location
   - Rate estimate: USD 149.317 per hour x 8 hour(s) — Weekend/holiday hourly rate KRW 200,000 (VAT excluded per the listing) x 8 hours = KRW 1,600,000. USD equivalent at the ECB euro foreign exchange reference rate dated 2026-11-20 (EUR 1 = USD 1.0990; EUR 1 = KRW 1472.04), fetched 2026-11-20 from https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml (Cube time='2026-11-20'); derived 1 KRW = USD 0.000746583, 1 USD = 1339.44 KRW.
   - Local rate: 200000 KRW per hour
   - Cost rate unit: hour
   - Event window: allows_to_5 (closing 22:00) (opening 09:00-22:00 (이용시간 평일/주말/공휴일 09~22시))
   - Source: [[그라운드옥탑] 강남역 100인 — 스페이스클라우드: 수용인원 최대 110명(100명 기준), 주말 및 공휴일 시간당 200,000원, 150인치 빔스크린, 와이파이](https://www.spacecloud.kr/space/68421)
   - Booking: [https://www.spacecloud.kr/space/68421](https://www.spacecloud.kr/space/68421)
   - Unresolved: Confirm the exact street address and building access before shortlisting: Space Cloud masks it ('자세한 주소는 예약 확정 후 예약 내역에서 확인할 수 있습니다') and only states 서울 역삼동 / 강남역 도보 5분, so no coordinate can be recorded honestly yet.
   - Unresolved: Confirm Saturday availability for the specific date on the platform calendar.
   - Unresolved: Confirm the all-in cost: KRW 200,000/시간 for 주말 및 공휴일, VAT 별도, 최소 3시간; the listing also states 100명 초과 시 1인 1만원 추가 요금 (max 120) and a 30-minute grace before entry, so an 8-hour booking plus setup may exceed 8 paid hours.
   - Unresolved: Confirm booking terms: 호스트 승인 후 예약확정 (average wait 1분 at fetch), 취소/환불 rules (이용일 기준 8일 전부터 변경·취소 환불 불가 per the listing).
- D.CAMP 마포 — 5층 박병원홀 (322㎡, 200인) (tier lead, score unknown) — capacity 200 (venue_claim), screen confirmed, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering unknown
   - Flags: oversized_capacity, cost_unknown, wifi_unknown, availability_unconfirmed, stale_evidence
   - Tier notes: material verification question(s): other_material
   - Event window: allows_to_5 (closing 18:00) (opening 평일 09:00-21:00; 토요일 09:00-18:00 (법정 공휴일 휴무))
   - Source: [space — 대관 가능 공간 (official D.CAMP page): 마포 5층 박병원홀 322㎡, 정원 200인, 장비 98인치 TV 2대·빔프로젝터·무선마이크 3대, 의자 190개](https://dcamp.kr/program/space)
   - Booking: [https://dcamp.kr/program/space](https://dcamp.kr/program/space)
   - Unresolved: Confirm the rental fee for 박병원홀 (no price is published; TaapSPACE application + 대관 심사, then quote).
   - Unresolved: Confirm Saturday availability for the specific date within the 7-day/60-day application window.
   - Unresolved: Confirm attendee Wi-Fi (not in the published equipment list).
   - Unresolved: Confirm whether a 200-seat hall can be scaled down to a 50-125 person community event comfortably (published furniture: 98인치 TV 2대, 강연대 1개, 무선마이크 3대, 유선마이크 1대, 빔프로젝트, 2인 테이블 2개, 의자 190개).
   - Unresolved: Confirm the 심사 criteria for a free community AI event and whether marketing/sponsor content is treated as '영리 목적'.
- D.CAMP 선릉 — 6층 이벤트홀 (201.48㎡, 130인) (tier lead, score unknown) — capacity 130 (venue_claim), screen confirmed, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering unknown
   - Flags: cost_unknown, wifi_unknown, availability_unconfirmed, stale_evidence
   - Tier notes: material verification question(s): other_material
   - Event window: allows_to_5 (closing 18:00) (opening 평일 09:00-21:00; 토요일 09:00-18:00 (법정 공휴일 휴무))
   - Source: [space — 대관 가능 공간 (official D.CAMP page): 선릉 6층 이벤트홀 201.48㎡, 정원 130인, 장비 60인치 TV 2대·LED 디스플레이·외부 디스플레이·무선마이크 4대, 의자 130개](https://dcamp.kr/program/space)
   - Booking: [https://dcamp.kr/program/space](https://dcamp.kr/program/space)
   - Unresolved: Confirm the rental fee: no price is published. Applications run through TaapSPACE (taapspace.kr) after 대관 심사, so a written quote is needed before any cost claim.
   - Unresolved: Confirm Saturday availability for the specific date, and note the published booking window: '신청일 기준 최대 7일 이후 60일 이전 행사만 신청 가능합니다' — a 2027 date cannot be applied for more than ~60 days ahead.
   - Unresolved: Confirm attendee Wi-Fi in the event hall (the equipment list covers displays, mics and furniture but not Wi-Fi).
   - Unresolved: Confirm the 심사 criteria applied to a free community AI event: the FAQ excludes '단순 친목 중심 모임' and '영리 목적' events, and one 기업(단체) may apply at most 5 times per month.
   - Unresolved: Confirm whether the 201.48㎡ hall can be laid out theatre-style for 50-125 people with the published furniture (2인 테이블 5개, 의자 130개).
- KT&G 상상마당 홍대 — 라이브홀 (tier lead, score unknown) — capacity 0 (unknown), screen unknown, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering unknown
   - Flags: cost_unknown, screen_unknown, wifi_unknown, availability_unconfirmed, duration_unconfirmed, stale_evidence
   - Tier notes: material verification question(s): capacity; capacity_comfortable 0 below minimum 40
   - Event window: unknown
   - Source: [대관안내 (official KT&G 상상마당 page): 예약문의 → 신청 → 계약 절차, 홍대 주소 서울시 마포구 어울마당로 65, 라이브홀 대관 문의 livehall@ssmadang.co.kr](https://www.sangsangmadang.com/rental/list)
   - Booking: [https://www.sangsangmadang.com/rental/list](https://www.sangsangmadang.com/rental/list)
   - Unresolved: Confirm the 라이브홀 capacity and layout (standing vs seated) for a 50-125 person event: the official 대관안내 page describes the procedure but publishes no capacity for the Hongdae live hall.
   - Unresolved: Confirm the rental fee: the official 대관안내 and 다회대관 할인 프로모션 pages describe discounts (e.g. 6회 이상 대관 시 평일 30%/주말 20% 할인 in the 2025 promotion) but no base rate is published; a written quote is required.
   - Unresolved: Confirm Saturday availability for a 09:00-17:00 event.
   - Unresolved: Confirm the usable window for an eight-hour daytime event (the hall is a working concert venue).
   - Unresolved: Confirm screen/projection in the live hall (a concert hall typically carries stage lighting and PA, not a conference screen — this must be verified, not assumed).
   - Unresolved: Confirm attendee Wi-Fi (not stated on the official rental page).
   - Unresolved: Confirm booking terms: 예약문의 → 대관신청서 이메일 접수 (livehall@ssmadang.co.kr, 02-2014-2024) and whether a non-concert community event is accepted.
- 문화비축기지 — T6 커뮤니티센터 (원형회의실/강의실) (tier lead, score unknown) — capacity 0 (unknown), screen unknown, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering unknown
   - Flags: cost_unknown, screen_unknown, wifi_unknown, availability_unconfirmed, duration_unconfirmed, stale_evidence
   - Tier notes: material verification question(s): capacity; capacity_comfortable 0 below minimum 40
   - Event window: unknown
   - Source: [문화비축기지 — 장소사용 안내 (official 서울의 공원 page): T6 커뮤니티센터, T1~T6 대관문의 02-508-2205 ㈜더문엔터테인먼트, 탱크 내부 사용수익허가 전환](https://parks.seoul.go.kr/template/sub/culturetank.do)
   - Booking: [https://parks.seoul.go.kr/template/sub/culturetank.do](https://parks.seoul.go.kr/template/sub/culturetank.do)
   - Unresolved: Confirm the seated capacity of the T6 원형회의실 and 강의실 for a 50-125 person event: the official park page describes the rooms (원형회의실 164㎡) but publishes no capacity, and the space is now operated under a 사용수익허가 by ㈜더문엔터테인먼트 (02-508-2205) rather than by the park office.
   - Unresolved: Confirm the rental fee: the official page publishes only 문화마당 rates (T0 141,613원/시간, 나무데크 18,324원/시간); T1~T6 rates are set by the operator and are not published.
   - Unresolved: Confirm Saturday availability and the approval route for T6 (T1~T6 문의 02-508-2205; 문화마당/산책로 02-2133-0425).
   - Unresolved: Confirm the usable event window for an eight-hour 09:00-17:00 Saturday event.
   - Unresolved: Confirm screen/projection in T6 (the park page lists the rooms and the café but no AV).
   - Unresolved: Confirm attendee Wi-Fi in T6 (not stated on the park page).
- 앙트레블 (신논현역·강남역) — 100인 컨퍼런스 공간 (Space Cloud listing 29372) (tier lead, score unknown) — capacity 100 (venue_claim), screen confirmed, wifi confirmed, cost USD 525.59 / 704000 KRW (estimated_from_rate), catering unknown
   - Flags: availability_unconfirmed, final_quote_required, map_location_unknown, stale_evidence
   - Tier notes: material verification question(s): location
   - Rate estimate: USD 65.6993 per hour x 8 hour(s) — Published hourly rate KRW 88,000 x 8 hours = KRW 704,000. The listing states a minimum 2-hour booking and a 2-hour base rental; no weekend differential is published. USD equivalent at the ECB euro foreign exchange reference rate dated 2026-11-20 (EUR 1 = USD 1.0990; EUR 1 = KRW 1472.04), fetched 2026-11-20 from https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml (Cube time='2026-11-20'); derived 1 KRW = USD 0.000746583, 1 USD = 1339.44 KRW.
   - Local rate: 88000 KRW per hour
   - Cost rate unit: hour
   - Event window: allows_to_5 (closing 23:59) (opening 0~24시 (영업시간 0~24시, 휴무일 없음))
   - Source: [앙트레블(신논현역, 강남역) 대관 — 스페이스클라우드: 수용인원 최대 100명, 시간당 88,000원, 4K LED 스크린 5m x 3m, 무료 wifi](https://www.spacecloud.kr/space/29372)
   - Booking: [https://www.spacecloud.kr/space/29372](https://www.spacecloud.kr/space/29372)
   - Unresolved: Confirm the exact street address and building access: Space Cloud masks the address ('자세한 주소는 예약 확정 후 예약 내역에서 확인할 수 있습니다'; only 서울 역삼동 인근 is shown), so no coordinate can be recorded honestly yet.
   - Unresolved: Confirm Saturday availability for the specific date (the host answers by phone 0507-1443-1417, weekdays 10:00-18:00).
   - Unresolved: Confirm the all-in cost: KRW 88,000/시간 with a 2-hour minimum and no published weekend differential; confirm whether VAT, cleaning and any 10-minute overrun charge (30분 단위 추가금) apply to an 8-hour booking.
   - Unresolved: Confirm booking terms and the room fit: 호스트 승인 후 예약확정; seating is 73석 with tables up to 100 with floor cushions, and 케이터링 이용 시 수용 인원 50명으로 제한.
- 연세대 백양누리 — 그랜드볼룸 A (60~120석) (tier lead, score unknown) — capacity 120 (venue_claim), screen confirmed, wifi unknown, cost unknown (unknown) — confirm cost with venue, catering in_house_only
   - Flags: cost_unknown, wifi_unknown, availability_unconfirmed, duration_unconfirmed, stale_evidence
   - Tier notes: material verification question(s): other_material
   - Event window: unknown
   - Source: [연세대학교 백양누리 | 대관서비스 | 그랜드볼룸A,B | 공간안내: 그랜드볼룸 A 또는 B 60석~120석, LED스크린 사용료 1,320,000원, 4만원 이상 메뉴 식사시 기본대관료 3시간 무료](https://gsis.yonsei.ac.kr/commons/space/grandBallroom.do)
   - Booking: [https://gsis.yonsei.ac.kr/commons/space/grandBallroom.do](https://gsis.yonsei.ac.kr/commons/space/grandBallroom.do)
   - Unresolved: Confirm the basic 대관료 for 그랜드볼룸 A: the official page publishes only the LED screen usage fee (KRW 1,320,000) and the rule '4만원 이상 메뉴 식사시 기본대관료 3시간 무료'; the base room rate sits in the 백양누리_요금표 attachment and must be quoted.
   - Unresolved: Confirm the usable daily window for a 09:00-17:00 Saturday event (no hours are published on the space page).
   - Unresolved: Confirm Saturday availability and whether external (non-Yonsei) organizations can book a weekend date.
   - Unresolved: Confirm booking terms: 신청서 submission to the CJ프레시웨이 reservations team (02-2123-8052, ys.thelounge@cj.net), deposit and cancellation terms, and the 교내/동문 discount eligibility for an outside community group.
   - Unresolved: Confirm attendee Wi-Fi in 그랜드볼룸 A (not stated on the official space page).
   - Unresolved: Confirm the seating fit: the venue holds round tables for banquet-style seating only, and the platform FAQ states a theatre/lecture layout requires an outside setup vendor — confirm whether a lecture-style 50-125 person layout is permitted and who supplies it.

## Trusted Venue Seeds (discovery provenance only)

- No matching trusted-venue seeds for this city. A seed is a head-start for research, never proof of current availability, capacity, screen, Wi-Fi, or cost.

## Speaker Candidates

- Speaker candidates: deferred to Run B after venue selection. No speaker candidates research is performed in Run A.

## Local Communities

- AI Seoul (Meetup group) (independent (Meetup)) — activity: active — focus: ai, machine_learning — members: 326 — cadence: Bi-weekly 'AI Adoption Talk - Learning & Talking on AI' with a 2026 series: 2026-06-06 (Robotics & Tech Stocks), 2026-06-20, 2026-07-04, 2026-07-18, 2026-09-05, 2026-09-19, 2026-10-03, 2026-10-17, 2026-10-31, 2026-11-14, 2026-11-28; next listed 2026-12-12 — typical venue: unknown venue
  - Verify: Confirm the group's organiser team and whether they would co-host a DeAI Day or provide an audience channel (the page lists no collaboration language).
  - Verify: Confirm the typical venue and headcount of the bi-weekly AI Adoption Talk (not stated on the events list).
  - Source: [AI Seoul | Meetup — events](https://www.meetup.com/ai-seoul-public/events/)
  - Observed: Rendered Meetup group and events pages (meetup.com/ai-seoul-public/, fetched 2026-11-20) return 'AI Seoul 4.9 • 18 ratings Seoul, KR 326 members'; the events list shows repeated '✨ AI Adoption Talk - Learning & Talking on AI' entries with dates 2026-06-06, 2026-06-20, 2026-07-04, 2026-07-18, 2026-09-05, 2026-09-19, 2026-10-03, 2026-10-17, 2026-10-31, 2026-11-14, 2026-11-28 and 2026-12-12 (one dated 2026-06-06 is titled '✨ AI Adoption Talk - Robotics & Tech Stocks'). The about text: 'Our group is focused on learning and networking within the realm of artificial intelligence and robotics.' The about section links a Kakao open chat ('Kakao Group: https://open.kakao.com/o/pV7r9rii'), recorded here because contact_info must be a structured object or null.
  - Inference (displayable uncertainty, not proof): A regular, reasonably sized Seoul AI audience with a predictable bi-weekly slot; good audience signal, co-host openness unknown.
  - Uncertainty: Member count (326) and rating (4.9, 18 ratings) are public on the group page. The event list shows dates and titles but not venues or headcounts. Sixteen dated 2026 entries appear on the rendered events page, counting both past and upcoming.
- AI Tinkerers Seoul (AI Tinkerers) — activity: active — focus: ai, machine_learning — members: unknown — cadence: Irregular builder demo nights; the chapter page shows 'Next event: Tuesday, November 24, 2026' with past events on July 2, 2026 and August 20, 2026 — typical venue: unknown venue
  - Verify: Confirm the chapter's current organizer roster and whether a co-hosted DeAI Day is something the Seoul organizers would consider (the page lists organizers and a past event 'sponsored by CROO', but carries no Seoul-specific open call).
  - Verify: Confirm the typical venue and headcount of the 2026 Seoul demo nights (not stated on the chapter page).
  - Source: [AI Tinkerers Seoul - AI Meetups, Events, and Builder Demos 2026](https://seoul.aitinkerers.org/)
  - Observed: Official AI Tinkerers Seoul page (seoul.aitinkerers.org, fetched 2026-11-20): title 'AI Tinkerers Seoul - AI Meetups, Events, and Builder Demos 2026'; 'Next event: Tuesday, November 24, 2026'; past-event entries include 'The Prompt That Worked in Isolation and Died in Production ... (July 2, 2026)' and an August 20, 2026 talk; one past outing is described as 'a technical demo night for AI builders, featuring live demos and networking, sponsored by CROO'; the page lists organisers by first name only and was 'Last updated: November 2026'.
  - Inference (displayable uncertainty, not proof): The most credible Seoul AI-builder audience in this set (recent, dated, in-person demo nights).
  - Uncertainty: Own-page evidence is strong for activity (dated 2026 events), but the chapter posts no venue, no public member count and no collaboration or sponsorship invitation, so co-host openness is intentionally false rather than a negative claim.
- AWSKRUG (AWS 한국사용자모임) (AWS User Group Community) — activity: active — focus: ai, mixed — members: unknown — cadence: Multiple sub-meetups per month: '2026년 11월 24일 19:00 KST' session, '2026년 11월 26일 19:00 KST' AWSKRUG Connect at 스파크플러스 강남 4호점 IR룸 11B, '2026년 11월 04일' Kiro 한국 사용자 모임 — typical venue: unknown venue
  - Verify: Confirm current membership size and whether the group co-hosts community events with non-AWS organisers (no co-hosting language appears on the Meetup page).
  - Verify: Confirm whether an AI/DeAI topic fits the group's 2027 programme and who approves topics.
  - Source: [AWSKRUG (AWS 한국사용자모임) | Meetup](https://www.meetup.com/ko-kr/awskrug/)
  - Observed: Official AWSKRUG Meetup page (meetup.com/ko-kr/awskrug, fetched 2026-11-20) lists upcoming sessions dated '2026년 11월 24일 19:00 KST', '2026년 11월 26일 19:00 KST' ('AWSKRUG Connect' at 스파크플러스 강남 4호점 IR룸 11B) and '2026년 11월 04일', with registration deadlines such as '신청 마감 : 2026년 11월 20일 (금) 23:59'.
  - Inference (displayable uncertainty, not proof): Large, regularly meeting cloud/AI engineering audience in Seoul; a strong audience signal even without co-host language.
  - Uncertainty: Meetup organiser page with dated 2026 sessions; member count was not captured on the fetched page, so it stays null rather than estimated.
- Bridge34 (independent) — activity: active — focus: web3, mixed — members: unknown — cadence: Event-agency cadence: 2026 Seoul events listed on 2026-04-14 (Agentic by Eigen | Seoul Edition), 2026-05-07 (MEGA ARCADE - SEOUL), and a KBW2026 side-event run 2026-09-28 to 2026-10-02 — typical venue: unknown venue
  - Open to co-hosting: "'From intimate KOL dinners to summit-scale conferences, Bridge34 plans, hosts and runs off-line events for global Web3 projects in Korea.'" — own-page phrase; manual assessment required, never a confirmed commitment
  - Verify: Confirm whether Bridge34 is open to co-organising a free community DeAI Day (their page states they plan/host/run events for global Web3 projects, which is a commercial engagement model, not a stated community partnership).
  - Verify: Confirm the commercial terms and lead time for a Seoul venue-plus-production engagement.
  - Source: [Bridge34 Off-Line Events — Where Web3 Meets Seoul](https://bridge34.com/events)
  - Observed: Bridge34 events page (bridge34.com/events, fetched 2026-11-20): heading 'Where Web3 Meets Seoul'; 'From intimate KOL dinners to summit-scale conferences, Bridge34 plans, hosts and runs off-line events for global Web3 projects in Korea.'; listed Seoul events include 'Apr 14, 2026 · Seoul Agentic by Eigen | Seoul Edition', 'May 7, 2026 · Seoul MEGA ARCADE - SEOUL', and KBW2026 side events dated Sep 28 - Oct 2, 2026.
  - Inference (displayable uncertainty, not proof): A production partner that could solve venue, AV and side-event logistics for a Seoul run, at commercial cost.
  - Uncertainty: The own-page language proves they run events in Seoul, not that they will partner for free; cohost_open is recorded as an invitation to assess, per the schema rule.
- Builderbase Hackathons (BuilderBase) (Builderbase) — activity: active — focus: web3, ai, mixed — members: unknown — cadence: Hackathon series visiting Seoul: 'DIGITAL AF Seoul — Hackathon' 2026-10-01 14:00-18:00 KST (4-hour build session inside DIGITAL AF Seoul, Yeongdong-daero/Seoul) — typical venue: DIGITAL AF Seoul venue, 14-15 Yangjae-dong, Seocho-gu, Seoul (per the DIGITAL AF calendar listing)
  - Verify: Confirm whether BuilderBase would co-run a Seoul DeAI hackathon or demo track in 2027 H1 (the page describes a single 2026 Seoul event and its tech partners, not a standing partnership offer).
  - Verify: Confirm typical participant numbers and the Seoul operating team.
  - Source: [DIGITAL AF Seoul Hackathon | 4-Hour Build Session — Builderbase](https://builderbase.com/event/digital-af-seoul-hackathon)
  - Observed: builderbase.com/event/digital-af-seoul-hackathon (fetched 2026-11-20): 'DIGITAL AF Seoul — Hackathon', 'Oct 1, 2026 · Yeongdong-daero, KR', 'Hosted by Builderbase Hackathons', "The Seoul Build Session drops builders into the middle of a five day art, gaming and tech festival during Korea Blockchain Week... judged the same night.", tech partners lovable.dev and elevenlabs.io; embedded schema.org JSON-LD: "startDate":"2026-10-01T05:00:00+00:00", "endDate":"2026-10-01T09:00:00+00:00", "price":0. The DIGITAL AF calendar (luma.com/DigitalAF2026) lists 'Sep 30 ... DIGITAL AF Seoul: Hackathon - In person Builderbase Hackathons'.
  - Inference (displayable uncertainty, not proof): A working hackathon operator with a Seoul 2026 footprint; relevant if the run wants a build track, at commercial/partnership cost.
  - Uncertainty: The event is confirmed by BuilderBase's own event page (schema.org Event with startDate 2026-10-01T05:00Z, price 0) and by the DIGITAL AF Seoul calendar. BuilderBase is an international hackathon operator, not a Seoul membership community, so it is recorded as a hackathon-capability signal. focus_tags cannot carry a hackathon value in schema 2.4, so the hackathon role is recorded in cadence and this note.
- Ethereum Collective Korea (ECK) (independent Korean Ethereum public-goods collective) — activity: active — focus: web3 — members: unknown — cadence: Weekly Korean-language Ethereum research digests (ACDE #249 2026-11-19, ACDC #191 2026-11-12, ACDT #103 2026-11-16) plus co-hosted Seoul events such as 'Ethereum Korea One Genesis' (2026-09-28/29) — typical venue: 성수 (Seongsu) multi-floor venue for Ethereum Korea One Genesis Day 2, per the collective's own notice
  - Verify: Confirm the collective's current organisers and whether it would co-host or promote a DeAI Day (the site describes public-goods work, not event partnerships).
  - Verify: Confirm the exact attendance and venue for Ethereum Korea One Genesis (registered/approved figures are from the collective's own notice).
  - Source: [ECK — Ethereum Collective Korea](https://ethcollective.xyz/)
  - Observed: ethcollective.xyz (fetched 2026-11-20): 'Ethereum Collective Korea (ECK) 한국 이더리움 생태계를 위한 공공재를 만드는 비영리 콜렉티브입니다. 리서치, 뉴스, 주간 리포트, 커뮤니티 이니셔티브를 한국어로 제공합니다.' Recent posts include 'ACDE #249 · 11월 19일', 'ACDT #103 · 11월 16일', 'ACDC #191 · 11월 12일', '월간 EIP - 2026년 10월'. A notice dated '2026.09.29' reads: '[공지] Ethereum Korea One Genesis · Day 2 Builder Day, 오늘 성수에서 열립니다 ... 800명이 넘는 분들이 등록해 주셨고, 그중 500명 정도를 승인했습니다.'
  - Inference (displayable uncertainty, not proof): An active Korean Ethereum research and builder community with recent Seoul event organisation; relevant as an audience signal for a Web3/DeAI track.
  - Uncertainty: Activity evidence is the collective's own site: dated research posts through 2026-11-19 and a notice dated 2026.09.29 describing the Ethereum Korea One Genesis builder day. Attendance figures (800 registered, ~500 approved) are self-reported in that notice.
- openKcloud 커뮤니티 (OpenKcloud community, ETRI-operated) (ETRI / K-cloud programme (KACI partners)) — activity: active — focus: ai, machine_learning — members: unknown — cadence: Annual DevDay plus programme work: 'openKcloud DevDay 2026' held 2026-11-10 13:30-18:00 at ST Center (과학기술회관) 중회의실3, Seoul — typical venue: ST Center (과학기술회관) 중회의실3, 서울 강남구 테헤란로7길 22
  - Verify: Confirm the community's 2027 programme and whether it co-hosts with non-ETRI organisers (the event channel is a public-sector programme, not a membership community).
  - Verify: Confirm typical headcount; the event registration page did not show a capacity figure on the fetched HTML.
  - Source: [openKcloud DevDay 2026 「모두를 위한 AI, 관측에서 서비스까지 AI로 연결되는 클라우드」 — 이벤터스 (hosted by openkcloud 커뮤니티)](https://event-us.kr/openkcloud/event/137324)
  - Observed: 전자신문 (etnews.com/20261030000252, published 2026-10-30): "한국인공지능클라우드산업협회(KACI)는 오픈클라우드(openKcloud) 커뮤니티가 주관하는 'openKcloud DevDay 2026' 컨퍼런스가 오는 11월 10일 서울 ST센터 중회의실3에서 열린다" and quotes '최현화 openKcloud 커뮤니티 리더'. 디지털데일리 (2026-11-02): "오픈케이클라우드(openKcloud) 커뮤니티는 오는 11월10일 오후 1시30분 서울 ST센터 중회의실3에서 '오픈케이클라우드 데브데이 2026'을 개최한다". Event registration page (event-us.kr/openkcloud/event/137324, fetched 2026-11-20): 'openKcloud DevDay 2026 ... 일시 11월 10일(화) 13:30 ~ 18:00 ... 장소 서울 강남구 테헤란로7길 22 ST Center(과학기술회관) 중회의실3 ... 비용 무료 ... 주최 OpenKcloud 커뮤니티'.
  - Inference (displayable uncertainty, not proof): A live Seoul AI-infrastructure audience with public-sector and NPU-industry reach; a topic signal (AI infra/observability) rather than a consumer AI audience.
  - Uncertainty: The event date and venue are corroborated by three independent outlets (전자신문 2026-10-30, 디지털데일리 2026-11-02, 아이티데일리 2026-10-30) and by the event registration page; the event-us page renders its schedule client-side, so the quoted date comes from the press notice plus the aggregator listing. Operated by ETRI under the K-cloud programme with KETI, Innogrid, Orchestro, Mobilint, Kyung Hee, Yonsei and KACI.
- PyLadies Seoul (PyLadies) — activity: active — focus: data_science, ai — members: unknown — cadence: Monthly book club plus workshops and seminars: 2026-02-07 seminar, 2026-03-04 book club, 2026-03-21 Git workshop, 2026-04-01 book club, 2026-04-25 Django open-source workshop, 2026-05-06 book club, 2026-05-30 career seminar, 2026-06-03 book club, 2026-07-26 Git workshop (2nd), 2026-09-05 Upstage team-lead seminar; PyLadies Asia Conference 2026 announced for 2026-11-29 (upcoming at check time) — typical venue: unknown venue
  - Verify: Confirm the group's 2027 calendar and whether it would co-host or partner on a DeAI Day audience track (the page states PyLadies Seoul hosts the Asia Conference but no collaboration call).
  - Verify: Confirm current public member count (not captured on the fetched page).
  - Source: [PyLadies Seoul | Meetup](https://www.meetup.com/seoul-pyladies-meetup/)
  - Observed: Rendered Meetup events page (meetup.com/seoul-pyladies-meetup/events/, fetched 2026-11-20) lists dated events '2026-02-07 AI 시대, 해외 취업 시장은 어떻게 다를까? ... 세미나', '2026-03-04 2026년 3월 PyLadies Seoul 월간 북클럽', '2026-03-21 Pyladies seoul: 깃 튜토리얼 워크샵', '2026-04-01 2026년 4월 PyLadies Seoul 월간 북클럽', '2026-04-25 [PyLadies Seoul] Django 오픈소스 기여 워크샵(Beginner Friendly)', '2026-05-06 2026년 5월 PyLadies Seoul 월간 북클럽', '2026-05-30 정답 대신 나만의 리듬으로 ... 세미나', '2026-06-03 2026년 6월 PyLadies Seoul 월간 북클럽', '2026-07-26 PyLadies Seoul Git 튜토리얼 워크샵 (2회차)', '2026-09-05 생물학도에서 개발팀 리더로 ... (Upstage Team Lead 문수영님 세미나)', and the upcoming '2026-11-29 PyLadies Asia Conference 2026'. Member count not shown on the fetched page.
  - Inference (displayable uncertainty, not proof): Active Seoul Python/data community with a steady 2026 in-person cadence and women-in-tech reach; a plausible outreach partner for an inclusive audience.
  - Uncertainty: Past 2026 events are now cited alongside the announced 2026-11-29 conference, so activity no longer rests on a future date. Member count is still not published on the fetched pages.
- Superteam Korea (Superteam (Solana ecosystem)) — activity: active — focus: web3 — members: unknown — cadence: Ran dated Seoul events during Korea Blockchain Week 2026: 'Solana Ecosystem Day' 2026-09-28 14:00-18:00 (Cafe en Travel, Gangnam, hosted by Metaplex x Superteam Korea), 'Solana Summit Korea' 2026-09-30 09:30-17:00 (Yeouido, hosted by Superteam Korea, Four Pillars, Solana Foundation) and 'SANC Nine' 2026-10-01 14:00-18:00 (localhost:web3, hosted by Sanctum x Superteam Korea) — typical venue: unknown venue
  - Verify: Confirm Superteam Korea's current Seoul leads and whether a DeAI Day could be co-hosted or promoted through the Korea channel (the KBW listing proves event organisation, not a partnership offer).
  - Verify: Confirm the community's own event calendar for 2027 H1 (the earn/bounty page and the KBW listing are the only sources observed).
  - Source: [Welcome to Superteam Earn South Korea | Discover Bounties and Grants](https://superteam.fun/earn/regions/korea)
  - Observed: Official KBW events page (koreablockchainweek.com/events, fetched 2026-11-20) lists: 'NETWORKING Solana Ecosystem Day Sep 28 2:00 PM - 6:00 PM Cafe en Travel 45 Gangnam-daero 102-gil, Gangnam District, Seoul, South Korea Hosted by Metaplex x Superteam Korea'; 'conference Solana Summit Korea September 30 9:30 AM - 5:00 PM Yeouido, Seoul (Accepted guests only) Hosted by: Superteam Korea, Four Pillars, Solana Foundation'; 'NETWORKING SANC Nine October 1 2:00 PM - 6:00 PM localhost:web3 로컬호스트Web3 609-1 Yeoksam-dong, Gangnam District, Seoul Hosted by: Sanctum · Superteam Korea'. The Superteam Earn Korea page (superteam.fun/earn/regions/korea) remains a bounty/grant platform with no dates.
  - Inference (displayable uncertainty, not proof): A Solana-ecosystem builder community that demonstrably organises or co-hosts in-person Seoul events during KBW; useful as an audience signal and a plausible co-host for a Web3/DeAI track.
  - Uncertainty: Upgraded from intermittent to active on 2026-11-20 review: three dated in-person Seoul events in Sept-Oct 2026 are listed on the official Korea Blockchain Week events page. The evidence is an organiser listing rather than Superteam Korea's own site, so co-host openness remains false and unverified.
- 모두의연구소 (Modulabs) (Modulabs) — activity: active — focus: ai, machine_learning, data_science — members: unknown — cadence: Recurring in-person seminars (e.g. '11월 10일(화) 10:00 - 12:00' with status 모집완료; '11월 26일(목)' and '11월 27일(금)' sessions 모집중) plus 모두모임 study groups and the annual 모두콘 conference ('모두콘 2026 - Deeper in AI') — typical venue: 역삼디오슈페리움 2층 모두의연구소 강남캠퍼스
  - Verify: Confirm the date, venue and expected headcount of 모두콘 2026 (the conference is named on the site but no date was visible on the fetched pages).
  - Verify: Confirm whether Modulabs would co-host or lend its community channel for a Seoul DeAI Day.
  - Source: [행사/세미나 | 모두의연구소 (Modulabs event listing)](https://biz.modulabs.co.kr/event?page=1)
  - Observed: Modulabs event listing (biz.modulabs.co.kr/event?page=1, rendered 2026-11-20) shows '변화근육, AI에게 대체되지 않는 나를 만드는 힘 — 11월 10일(화) 10:00 - 12:00 | 역삼디오슈페리움 2층 모두의연구소 강남캠퍼스' (모집완료), 'Notion 당신의 생각을 현실로만드는 공간 (입문편) — 11월 26일(목) 10:00 - 12:00 | 대전테크노파크 ... 모두의연구소' (모집중) and 'Notion ... (응용편) — 11월 27일(금) 05:00 - 09:00' (모집중). The main community page (modulabs.co.kr/community/momos) lists '모두모임 - 함께 성장하는 즐거움', '모두콘 2026 - Deeper in AI' and '모두팝 - AI/SW 세미나'.
  - Inference (displayable uncertainty, not proof): A large Seoul AI-education community with live in-person seminars at its 강남 campus and an annual conference; both an audience signal and a plausible co-host.
  - Uncertainty: The event listing prints day-month and weekday without a year; the weekday/day pairs match 2026 (2026-11-10 is a Tuesday, 2026-11-26 a Thursday, 2026-11-27 a Friday), so the sessions are read as 2026 dates.
- 블록체인 밋업데이 (Blockchain Meetup Day, BCMD) — 한국인터넷진흥원(KISA) (KISA (Korea Internet & Security Agency)) — activity: active — focus: web3 — members: unknown — cadence: Recurring education meetup; the 31st session was held 2026-11-14 (Sat) 10:00-18:00 at KISA 서울청사 10층 기업성장허브 — typical venue: 한국인터넷진흥원 서울청사 10층 기업성장허브 (서울시 송파구 중대로 135, 가락동 IT벤처타워)
  - Verify: Confirm the 2027 BCMD schedule and whether KISA would co-promote a DeAI Day to its blockchain audience (the page is an education-recruitment notice, not a partnership channel).
  - Verify: Confirm typical headcount (the notice caps confirmed attendees at 35 per session).
  - Source: [「2026 블록체인 밋업데이(BCMD)」 31회차 교육생 모집(~11.13)](https://kisa.or.kr/401/form?lang_type=KO&postSeq=3787)
  - Observed: KISA notice (kisa.or.kr/401/form?lang_type=KO&postSeq=3787, fetched 2026-11-20), 등록일 2026-10-21: '「2026 블록체인 밋업데이(BCMD)」 31회차 교육생 모집'; '2026년 11월 14일(토), 2026 블록체인 밋업데이(BCMD)가 개최됩니다. -토큰증권 제도화와 스마트 컨트랙트-'; '■ 일시 : 2026.11.14.(토) 10:00~18:00'; '■ 장소 : 한국인터넷진흥원 서울청사 10층 기업성장허브 (서울시 송파구 중대로 135 (가락동) IT벤처타워)'; '선착순 35명'.
  - Inference (displayable uncertainty, not proof): Shows a live Seoul Web3 education audience meeting on Saturdays, which is useful for week-day/time fit but not for scale.
  - Uncertainty: A public-agency programme rather than a member community; recorded as an audience and topic signal, not as a co-host candidate.
- GDG Seoul (Google Developer Groups Seoul) (Google Developer Groups (GDG)) — activity: intermittent — focus: ai, mixed — members: unknown — cadence: Seasonal large events; the organizer page rendered on 2026-11-20 shows an 'Upcoming Events' section with no event listed, and a search index still carries 'Build with AI Seoul 2026 with Google DeepMind | May 2, 2026' — typical venue: unknown venue
  - Verify: Confirm the current GDG Seoul event calendar: the organizer page rendered on 2026-11-20 shows 'Upcoming Events' with no upcoming event listed, while a search index still carries the May 2, 2026 'Build with AI Seoul 2026 with Google DeepMind' event.
  - Verify: Confirm whether GDG Seoul co-hosts with external community organisers.
  - Source: [Google Developer Groups GDG Seoul](https://gdg.community.dev/gdg-seoul/)
  - Observed: Headless-rendered fetch of https://gdg.community.dev/gdg-seoul/ on 2026-11-20 returned the GDG Seoul organizer shell with an 'Upcoming Events' section and no listed event, plus footer '© 2026'. A plain HTTP fetch of the same URL returned 404. A web search on the same date returned the organizer page title 'Google Developer Groups GDG Seoul' and the event 'Build with AI Seoul 2026 with Google DeepMind | May 2, 2026' at gdg.community.dev/events/details/google-gdg-seoul-presents-build-with-ai-seoul-2026-with-google-deepmind/.
  - Inference (displayable uncertainty, not proof): Likely a seasonal Google-dev community between event cycles; the 2026 May flagship suggests real reach but no current cadence is observable.
  - Uncertainty: The organizer page was reachable only through headless rendering (a direct HTTP fetch returned 404) and listed no upcoming events at fetch time; activity is therefore recorded as intermittent with an explicit question rather than as verified active.
- 파이토치 한국 사용자 모임 (PyTorch Korea) (PyTorch Korea) — activity: intermittent — focus: machine_learning, ai — members: unknown — cadence: Digital-first: Korean tutorial/blog posts through 2026-10-28, plus a reported in-person 'KVCache Meetup Korea' on 2026-09-30 at 드림플러스 강남 — typical venue: unknown venue
  - Verify: Confirm whether the group still runs its own in-person Seoul meetups (the fetched site shows blog activity and a report of a September 2026 meetup, but no own events calendar).
  - Verify: Confirm who the current organisers are and whether they would co-host a DeAI Day session.
  - Source: [파이토치 한국 사용자 모임 (pytorch.kr)](https://pytorch.kr/)
  - Observed: pytorch.kr (fetched 2026-11-20) shows blog entries dated '2026-10-28', '2026-10-23' and '2026-10-20', and a post describing '지난 2026년 9월 30일 저녁, 서울 강남 드림플러스에서 KVCache Meetup Korea 행사가 진행되었습니다'.
  - Inference (displayable uncertainty, not proof): A translation/tutorial community with ML reach; in-person cadence unknown.
  - Uncertainty: Evidence is digital-first plus a third-party meetup reported on the site; that is not the same as an own-organised in-person series, hence intermittent rather than active.
- 한국 R 사용자회 (Korea R User Group) — 서울 R Meetup (R User Groups (R Consortium)) — activity: intermittent — focus: data_science, machine_learning — members: unknown — cadence: The organisation runs the 서울 R Meetup and the annual 한국 R 컨퍼런스 per its site navigation; no 2026 meetup date was readable this pass — typical venue: unknown venue
  - Verify: Confirm the 2026/2027 서울 R Meetup dates: the site's '서울 R Meetup' subpage returned HTTP 404 at fetch time and only the navigation label was observable.
  - Verify: Confirm whether the group would co-host a data-science track at a Seoul DeAI Day.
  - Source: [한국 R 사용자회 (r2bit.com)](https://r2bit.com/)
  - Observed: r2bit.com (fetched 2026-11-20): '공익법인 한국 R 사용자회는 2022년에 설립되어 ...' with navigation entries '한국 R 컨퍼런스', '서울 R Meetup', '서울 R Meetup Archive', '글로벌 R Meetup'; footer '© 2026 BitStat'. The direct subpage r2bit.com/seoul-r-meetup/ returned 'Page not found · GitHub Pages 404'.
  - Inference (displayable uncertainty, not proof): An established Korean R/data-science non-profit with a Seoul meetup brand; current cadence unverified this pass.
  - Uncertainty: The 2026 Q4 run recorded a monthly Seoul R Meetup cadence from this site; this pass could not re-observe a dated 2026 meetup, so the status is downgraded to intermittent and the old cadence is not restated as fact.
- Ethereum Seoul Community (Ethereum Seoul Community) — activity: dormant — focus: web3 — members: unknown — cadence: Site describes bi-weekly meetups plus Civic Hackers' Club, Open Research Club and Ethcon Korea, but the newest notices shown are 2024-era — typical venue: Ethaewon Hacker House (EHH), 용산구 회나무로 60-1 — as printed in the 2024 meetup notices
  - Verify: Confirm whether the community is still running: the site's newest announcements are the '6월 이더리움 서울 bi-weekly meetup' and '이드콘한국 2024 운영위원회' notices, with no 2025 or 2026 schedule visible.
  - Source: [Ethereum Seoul Community | A hub for Ethereum Punks in Seoul](https://ethereum-seoul.community/)
  - Observed: ethereum-seoul.community: 'A hub for Ethereum Punks in Seoul. Participate in bi-weekly meetups, Open Research Club, Civic Hack Club, and the annual Ethcon conference.'; '이더리움 서울 커뮤니티는 월 2회 소규모 밋업을 가지며...'; the listed notices are '6월 이더리움 서울 bi-weekly meetup 안내' and '5월 이더리움 서울 bi-weekly meetup 안내' with agendas referencing '이드콘한국 2024 운영위원회 회의'.
  - Inference (displayable uncertainty, not proof): The Ethcon Korea-organising scene appears to have moved on; do not treat this site as a current 2027 partner without a fresh check.
  - Uncertainty: Dormant on own-page evidence (2024-era notices last). The venue line is quoted from those 2024 notices and is historical, not current.
- Seoul Ethereum Meetup (Seoul Ethereum Meetup) — activity: dormant — focus: web3 — members: 3983 — cadence: No event after December 2022 on the group's own Past events list — typical venue: unknown venue
  - Verify: Confirm whether the group has any post-2022 activity: the own page's 'Past events' list begins with 'Thu, Dec 15, 2022' and shows 46 past events with no later date.
  - Source: [Seoul Ethereum Meetup | Meetup](https://www.meetup.com/seoul-ethereum-meetup/)
  - Observed: meetup.com/seoul-ethereum-meetup: '4.5 • 422 ratings', 'Seoul, KR', '3,983 members'; 'Past events 46 See all' with the most recent entry 'Thu, Dec 15, 2022 · 6:00 PM KST — <비탈릭 부테린-지분증명> 과 머지이후 이더리움 확장성 확보 전략'.
  - Inference (displayable uncertainty, not proof): A large but inactive membership pool; any Seoul Ethereum audience in 2027 would have to be re-activated through a different organiser.
  - Uncertainty: Dormant on own-page evidence (no event since 2022-12-15) despite 3,983 members; retained only as historical context for the Seoul Ethereum audience.

## Trusted Network

- Trusted-network research: deferred to Run B after venue selection. No trusted-network research research is performed in Run A.

## Co-Host Candidates

- Co-host research: deferred to Run B after venue selection. No co-host research research is performed in Run A.

## Open Questions

- Assess whether a side event or co-located session during the show would reach the same AI/ICT builder audience, or whether the show mainly draws enterprise buyers.
- Blocked/unusable sources this pass: aT Center (WAF challenge), 한국과학기술회관 stcenter.or.kr (connection timeout), wework.com (403), front1.co.kr (NXDOMAIN), sparkplus.co.kr (empty response), ddp.or.kr (curl 0 bytes; needed headless render), parks.seoul.go.kr deep links (404; content read through the search-indexed page text). aiexpo.co.kr rejects plain curl but renders correctly under headless Chromium, which is how the 2027 dates were read.
- Calendar research on 2026-11-20 found three confirmed 2027 H1 Seoul AI events and one industrial trade show: WIS 2027 (2027-04-21..23, COEX), AI EXPO KOREA 2027 (2027-04-14..16, COEX Hall A) and 서울메타위크 2027 (2027-04-29..30, COEX Grand Ballroom) are recorded as related rows with opportunity_kind ai and status confirmed; their April dates fall outside the Q1 window, so they are carried in this quarter's calendar_conflicts as context and are not adjacent_events; AW 2027 (2027-03-03..05, COEX 전체 홀) is recorded as major_other for logistics. AI Summit Seoul & Expo 2027 is 2027-08-11..13 (outside H1). NextRise 2027 and Korea Blockchain Week 2027 still publish no 2027 dates and stay as leads.
- Candidate Saturdays are operational input only (all 13 Saturdays of the window); they are not a recommendation, an elimination set, or a date selection; Joe alone decides the date.
- Confirm attendee Wi-Fi (not in the published equipment list).
- Confirm attendee Wi-Fi (not stated on the facility page).
- Confirm attendee Wi-Fi (not stated on the official rental page).
- Confirm attendee Wi-Fi in 300호 (the page lists A/V, fixed projector, interpretation booth and stage for rooms ≥207㎡, but not Wi-Fi).
- Confirm attendee Wi-Fi in T6 (not stated on the park page).
- Confirm attendee Wi-Fi in the event hall (the equipment list covers displays, mics and furniture but not Wi-Fi).
- Confirm attendee Wi-Fi in 그랜드볼룸 A (not stated on the official space page).
- Confirm attendee Wi-Fi in 디자인홀 (the official page lists display, audio, power and furniture but no attendee Wi-Fi).
- Confirm attendee Wi-Fi in 세미나실 1 (not stated on the official rental pages).
- Confirm attendee Wi-Fi in 세미나실 2 (not stated on the official rental pages).
- Confirm booking terms and the operator's acceptance of a free community tech event under the standard 컨벤션센터 대관 procedure.
- Confirm booking terms and the room fit: 호스트 승인 후 예약확정; seating is 73석 with tables up to 100 with floor cushions, and 케이터링 이용 시 수용 인원 50명으로 제한.
- Confirm booking terms and whether a free community event is accepted (COEX runs 대관 공고 notices and a separate business rental channel).
- Confirm booking terms for a free community event (DDP requires 대관 신청 and committee review; approval lead time and deposit terms are not published).
- Confirm booking terms: 사업자등록증 and 행사계획서 are required for the application, and payment must be settled within 3 days of 대관 허가.
- Confirm booking terms: 신청서 submission to the CJ프레시웨이 reservations team (02-2123-8052, ys.thelounge@cj.net), deposit and cancellation terms, and the 교내/동문 discount eligibility for an outside community group.
- Confirm booking terms: 예약문의 → 대관신청서 이메일 접수 (livehall@ssmadang.co.kr, 02-2014-2024) and whether a non-concert community event is accepted.
- Confirm booking terms: 온라인 신청 at least 7 days before use, 내부 심사 and 승인 통보, then payment; 취소 refunds are 100% at 10+ days and 80% under 10 days.
- Confirm booking terms: 호스트 승인 후 예약확정 (average wait 1분 at fetch), 취소/환불 rules (이용일 기준 8일 전부터 변경·취소 환불 불가 per the listing).
- Confirm current membership size and whether the group co-hosts community events with non-AWS organisers (no co-hosting language appears on the Meetup page).
- Confirm current public member count (not captured on the fetched page).
- Confirm Saturday availability (the COEX exhibition calendar shows weekend exhibitions, which is not evidence of meeting-room availability).
- Confirm Saturday availability and the 20% 토·일·공휴일 surcharge that the table applies to 문화센터/문화교실/연수객실 rows ('토, 일, 공휴일은 기존금액의 100분의 20을 가산함') — whether it applies to 다목적강당 as well.
- Confirm Saturday availability and the approval route for T6 (T1~T6 문의 02-508-2205; 문화마당/산책로 02-2133-0425).
- Confirm Saturday availability and whether external (non-Yonsei) organizations can book a weekend date.
- Confirm Saturday availability for 09:00-17:00 on the specific date (DDP rentals run through an application + 대관심의 committee; the published window is a daily basis time, not an availability calendar).
- Confirm Saturday availability for a 09:00-17:00 event in 세미나실 2 on the specific date (the official page publishes no weekday/weekend band).
- Confirm Saturday availability for a 09:00-17:00 event on the specific date: the official rate table publishes time slots (08~12 / 13~17 / 18~21) but states no weekday/weekend band, and the online booking system (컨벤션센터 온라인 예약) is the only availability source.
- Confirm Saturday availability for a 09:00-17:00 event.
- Confirm Saturday availability for the specific date (the host answers by phone 0507-1443-1417, weekdays 10:00-18:00).
- Confirm Saturday availability for the specific date on the platform calendar.
- Confirm Saturday availability for the specific date within the 7-day/60-day application window.
- Confirm Saturday availability for the specific date, and note the published booking window: '신청일 기준 최대 7일 이후 60일 이전 행사만 신청 가능합니다' — a 2027 date cannot be applied for more than ~60 days ahead.
- Confirm Saturday availability for the specific date: the official rent calendar (nodeul.org/rent-calendar/?calendar_type=rent-livehouse) shows per-day availability and the hall runs an active concert schedule.
- Confirm screen/projection in T6 (the park page lists the rooms and the café but no AV).
- Confirm screen/projection in the live hall (a concert hall typically carries stage lighting and PA, not a conference screen — this must be verified, not assumed).
- Confirm screen/projection in 세미나실 1: the official rate page lists 면적 and 사용료 only; the room equipment list is published per room elsewhere and a projector/screen is not confirmed for this room.
- Confirm screen/projection in 세미나실 2 (the official rate page publishes only 면적 and 사용료; the room equipment list is published per room elsewhere).
- Confirm screen/projection: the facility page lists sound, lighting and instrument equipment, a house manager and four ushers, but no presentation screen or projector.
- Confirm screen/projection: the 시설별 대여가능장비 list for 다목적강당 is '음향, 조명, 거울' with no screen or projector (세미나실 rows do list 빔프로젝터).
- Confirm Superteam Korea's current Seoul leads and whether a DeAI Day could be co-hosted or promoted through the Korea channel (the KBW listing proves event organisation, not a partnership offer).
- Confirm that a non-concert community/tech event is accepted at the performance-rental rate and terms (대관 공고 → 신청 → 심의 → 계약).
- Confirm the 2026/2027 서울 R Meetup dates: the site's '서울 R Meetup' subpage returned HTTP 404 at fetch time and only the navigation label was observable.
- Confirm the 2027 BCMD schedule and whether KISA would co-promote a DeAI Day to its blockchain audience (the page is an education-recruitment notice, not a partnership channel).
- Confirm the 2027-04-29..30 dates and COEX Grand Ballroom booking, and whether the programme accepts community side sessions.
- Confirm the all-in cost: KRW 200,000/시간 for 주말 및 공휴일, VAT 별도, 최소 3시간; the listing also states 100명 초과 시 1인 1만원 추가 요금 (max 120) and a 30-minute grace before entry, so an 8-hour booking plus setup may exceed 8 paid hours.
- Confirm the all-in cost: KRW 88,000/시간 with a 2-hour minimum and no published weekend differential; confirm whether VAT, cleaning and any 10-minute overrun charge (30분 단위 추가금) apply to an 8-hour booking.
- Confirm the all-in price for an 8-hour Saturday event: KRW 890,000 is the published 8~17시 rate, 부가가치세 별도 (VAT excluded); confirm VAT, 시간외 (110,000/hour), and any 부대시설 or 장비 charges.
- Confirm the all-in price for an 8-hour Saturday event: 토,일,공휴일 2회 rate KRW 6,000,000 applies because a single performance over 3 hours is billed as 2회 (VAT excluded); 준비·철수 대관 is a separate KRW 1,067,000 per slot on weekends.
- Confirm the all-in price: KRW 760,000 for 8~17시, 부가가치세 별도; confirm VAT and any 장비/부대시설 charges.
- Confirm the basic 대관료 for 그랜드볼룸 A: the official page publishes only the LED screen usage fee (KRW 1,320,000) and the rule '4만원 이상 메뉴 식사시 기본대관료 3시간 무료'; the base room rate sits in the 백양누리_요금표 attachment and must be quoted.
- Confirm the chapter's current organizer roster and whether a co-hosted DeAI Day is something the Seoul organizers would consider (the page lists organizers and a past event 'sponsored by CROO', but carries no Seoul-specific open call).
- Confirm the COEX hall footprint and expected 80,000 visitors for 2027-03-03..05, and assess hotel/transport demand and venue competition for a Seoul event on the following weekend.
- Confirm the collective's current organisers and whether it would co-host or promote a DeAI Day (the site describes public-goods work, not event partnerships).
- Confirm the commercial terms and lead time for a Seoul venue-plus-production engagement.
- Confirm the community's 2027 programme and whether it co-hosts with non-ETRI organisers (the event channel is a public-sector programme, not a membership community).
- Confirm the community's own event calendar for 2027 H1 (the earn/bounty page and the KBW listing are the only sources observed).
- Confirm the current GDG Seoul event calendar: the organizer page rendered on 2026-11-20 shows 'Upcoming Events' with no upcoming event listed, while a search index still carries the May 2, 2026 'Build with AI Seoul 2026 with Google DeepMind' event.
- Confirm the date, venue and expected headcount of 모두콘 2026 (the conference is named on the site but no date was visible on the fetched pages).
- Confirm the dates and Public Day audience on the organiser site nearer the show, and assess whether a Saturday in the same week gains or loses from the exhibition crowd.
- Confirm the exact attendance and venue for Ethereum Korea One Genesis (registered/approved figures are from the collective's own notice).
- Confirm the exact street address and building access before shortlisting: Space Cloud masks it ('자세한 주소는 예약 확정 후 예약 내역에서 확인할 수 있습니다') and only states 서울 역삼동 / 강남역 도보 5분, so no coordinate can be recorded honestly yet.
- Confirm the exact street address and building access: Space Cloud masks the address ('자세한 주소는 예약 확정 후 예약 내역에서 확인할 수 있습니다'; only 서울 역삼동 인근 is shown), so no coordinate can be recorded honestly yet.
- Confirm the group's 2027 calendar and whether it would co-host or partner on a DeAI Day audience track (the page states PyLadies Seoul hosts the Asia Conference but no collaboration call).
- Confirm the group's organiser team and whether they would co-host a DeAI Day or provide an audience channel (the page lists no collaboration language).
- Confirm the published dates and hall allocation on the organiser's own site before the dates are used for any planning, and assess audience overlap with a Seoul Decentralized AI Day.
- Confirm the race date on the organiser site (seoul-marathon.com) and assess logistics impact on the city centre: road closures, route access, hotel demand, transport disruption and crowding for a Seoul event on a nearby weekend.
- Confirm the rental fee for 300호: COEX publishes room specs and an 임대관련자료 board, but no rate for this room is exposed on the public pages, so a written quote is required.
- Confirm the rental fee for 박병원홀 (no price is published; TaapSPACE application + 대관 심사, then quote).
- Confirm the rental fee: no price is published. Applications run through TaapSPACE (taapspace.kr) after 대관 심사, so a written quote is needed before any cost claim.
- Confirm the rental fee: the official page publishes only 문화마당 rates (T0 141,613원/시간, 나무데크 18,324원/시간); T1~T6 rates are set by the operator and are not published.
- Confirm the rental fee: the official 대관안내 and 다회대관 할인 프로모션 pages describe discounts (e.g. 6회 이상 대관 시 평일 30%/주말 20% 할인 in the 2025 promotion) but no base rate is published; a written quote is required.
- Confirm the seated capacity of the T6 원형회의실 and 강의실 for a 50-125 person event: the official park page describes the rooms (원형회의실 164㎡) but publishes no capacity, and the space is now operated under a 사용수익허가 by ㈜더문엔터테인먼트 (02-508-2205) rather than by the park office.
- Confirm the seating fit: the venue holds round tables for banquet-style seating only, and the platform FAQ states a theatre/lecture layout requires an outside setup vendor — confirm whether a lecture-style 50-125 person layout is permitted and who supplies it.
- Confirm the typical venue and headcount of the 2026 Seoul demo nights (not stated on the chapter page).
- Confirm the typical venue and headcount of the bi-weekly AI Adoption Talk (not stated on the events list).
- Confirm the usable daily window and whether a 09:00-17:00 eight-hour Saturday block is bookable (COEX publishes no meeting-room hours on this page).
- Confirm the usable daily window for a 09:00-17:00 Saturday event (no hours are published on the space page).
- Confirm the usable daily window: the published slot table is written for 공연장 (10:00-14:00 / 14:00-18:00 / 18:00-22:00); confirm that a 다목적강당 event can run 09:00-17:00 or 10:00-18:00 for eight hours.
- Confirm the usable event window for an eight-hour 09:00-17:00 Saturday event.
- Confirm the usable window for an eight-hour daytime event (the hall is a working concert venue).
- Confirm the 다목적강당 rental fee and its unit: the official '어울림플라자 시설 대관료' table lists 다목적강당 350,000 ~ 540,000원 but the per-row 내용 column (which states '1회(4시간) 단가' for 공연장 and '시간당 단가' for 문화센터 1,2) is not repeated for 다목적강당, so the unit for this row is not published.
- Confirm the 라이브홀 capacity and layout (standing vs seated) for a 50-125 person event: the official 대관안내 page describes the procedure but publishes no capacity for the Hongdae live hall.
- Confirm the 심사 criteria applied to a free community AI event: the FAQ excludes '단순 친목 중심 모임' and '영리 목적' events, and one 기업(단체) may apply at most 5 times per month.
- Confirm the 심사 criteria for a free community AI event and whether marketing/sponsor content is treated as '영리 목적'.
- Confirm typical headcount (the notice caps confirmed attendees at 35 per session).
- Confirm typical headcount; the event registration page did not show a capacity figure on the fetched HTML.
- Confirm typical participant numbers and the Seoul operating team.
- Confirm whether a 200-seat hall can be scaled down to a 50-125 person community event comfortably (published furniture: 98인치 TV 2대, 강연대 1개, 무선마이크 3대, 유선마이크 1대, 빔프로젝트, 2인 테이블 2개, 의자 190개).
- Confirm whether an 09:00 start is possible: the official performance window is 10:00-23:00, so an 09:00-17:00 window is not covered by published hours (a 10:00-18:00 window is).
- Confirm whether an AI/DeAI topic fits the group's 2027 programme and who approves topics.
- Confirm whether Bridge34 is open to co-organising a free community DeAI Day (their page states they plan/host/run events for global Web3 projects, which is a commercial engagement model, not a stated community partnership).
- Confirm whether BuilderBase would co-run a Seoul DeAI hackathon or demo track in 2027 H1 (the page describes a single 2026 Seoul event and its tech partners, not a standing partnership offer).
- Confirm whether GDG Seoul co-hosts with external community organisers.
- Confirm whether Modulabs would co-host or lend its community channel for a Seoul DeAI Day.
- Confirm whether the 201.48㎡ hall can be laid out theatre-style for 50-125 people with the published furniture (2인 테이블 5개, 의자 130개).
- Confirm whether the community is still running: the site's newest announcements are the '6월 이더리움 서울 bi-weekly meetup' and '이드콘한국 2024 운영위원회' notices, with no 2025 or 2026 schedule visible.
- Confirm whether the group has any post-2022 activity: the own page's 'Past events' list begins with 'Thu, Dec 15, 2022' and shows 46 past events with no later date.
- Confirm whether the group still runs its own in-person Seoul meetups (the fetched site shows blog activity and a report of a September 2026 meetup, but no own events calendar).
- Confirm whether the group would co-host a data-science track at a Seoul DeAI Day.
- Confirm whether the published 1일 기준 KRW 3,256,000 includes VAT and whether the 8-hour 09:00-17:00 use is billed as 1일 기준 (the table gives 시간당 296,000 / 3시간 888,000 / 1일 3,256,000 with no VAT statement on the rendered page).
- Confirm who the current organisers are and whether they would co-host a DeAI Day session.
- Coordinate provenance: every non-null coordinate pair in venues.raw.json comes from an OpenStreetMap Nominatim lookup performed 2026-11-20 and is recorded with its openstreetmap.org object URL in evidence.geo. Two platform-listed venues (Space Cloud) mask the street address until booking and therefore carry null coordinates plus a location question.
- Event window assessed as 09:00-17:00 (8 hours) per the locked plan; venue windows that only start at 10:00 (Nodeul Island) or gate on a Saturday closing time carry a specific question.
- Impact Hub has no Seoul location (no Seoul/Korea record in the installed impact_hub_locations.json and none on impacthub.net/locations); Seoul venue discovery proceeded without a hub seed, consistent with the 2026 Q4 pass.
- KR public-holiday rows for 2027 come from the plan-event registry (references/school_holidays.json, jurisdiction KR and KR:seoul, edition '2027년 월력요항 (우주항공청공고 제2026-0078호)'); this package does not duplicate them. All 13 Saturdays of the Q1 window were swept against those rows on 2026-11-20. Direct Saturday collisions: 2027-02-06 (설날 연휴 day 1, with substitute 2027-02-09). Long-weekend Saturdays (a Sunday or Monday neighbour is a holiday): 2027-01-02 (신정 on Friday 2027-01-01) and 2027-02-27 (3·1절 on Monday 2027-03-01). No same-week mid-week holiday falls inside the Q1 window.
- Research window is 2027-01-01 through 2027-03-31. target_date 2027-03-06 is a neutral technical placeholder required by score/bundle/summary integrity; it is never a recommendation and no output may present it as one.
- Venue open question: most Seoul venues are inquiry-only. This pass found published rate tables at four venues: SETEC (시간대별 사용료 table), DDP 디자인홀 (디자인랩 대관료 table), Nodeul Island Livehouse (2026 대관료 table) and 서울시 어울림플라자 (시설 대관료 table, row unit not stated so no number is claimed). Two Space Cloud listings publish hourly weekend rates (그라운드옥탑 200,000원/h, 앙트레블 88,000원/h) from which an 8-hour estimate is derived and labelled estimated_from_rate. D.CAMP, COEX, 백양누리, 문화비축기지 and KT&G 상상마당 are inquiry/quote-only.

Full source list: see sources.md
