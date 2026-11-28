# Venue discovery log — Seoul 2027 deep refresh, 2026-11-28

Method: 37 English and Korean searches in total across the bundle (this log's own venue/district list is 23; the other 14 are the calendar and community searches listed in `community_discovery_log.md`). Each surviving venue's own page was then fetched and captured; aggregators were discovery-only. A venue is only recorded when its own page (or the operating institution's own record) could be captured today.

## Queries — venue and district sweep (23)

1. 서울 이벤트 스페이스 대관 50명 세미나실
2. 서울 회의실 대여 시간당 가격 강남 세미나실 대관
3. 성수동 공간 대관 행사 스페이스 50명
4. 서울 스타트업 이벤트 공간 대관 커뮤니티
5. 스페이스클라우드 서울 강남 세미나실 50명 가격
6. Seoul event space rental 50 people hourly price Gangnam
7. 코엑스 회의실 대관 요금 컨퍼런스룸 300
8. DDP 동대문디자인플라자 대관 요금 디자인랩 신청
9. 스페이스쉐어 강의장 회의실 가격 시간당 대관
10. 한국컨퍼런스센터 강남 대관 요금 세미나실 정원
11. 코엑스 컨퍼런스룸 대관료 1일 사용료 홈페이지
12. SETEC 세텍 전시장 컨벤션홀 대관료 요금
13. 마포구 공공시설 대관 회의실 세미나실 신청 요금
14. 성동구 시설 대관 다목적실 회의실 요금 신청 성수
15. KT&G 상상마당 홍대 라이브홀 대관 요금 수용인원
16. 노들섬 공간 대관 라이브하우스 다목적홀 요금
17. 프론트원 Front One 마포 서울창업 공간 대관 요금
18. 경기창조경제혁신센터 판교 대관 회의실 요금 신청
19. site:eshare.go.kr 서울 강당 다목적실 50명 이용요금
20. 몽상공간 문래 대관 요금 수용인원
21. 전경련회관 컨퍼런스센터 여의도 대관 요금 회의실
22. 서울창업허브 공덕 대관 강의장 요금 신청
23. 시민청 대관 신청 공간 요금 수용인원 서울시청 지하

## District sweep

- **Jung-gu / Euljiro** — queries 8, 23 → DDP Design Lab (3 rooms recorded), 시민청 (30-person rooms, below brief), 을지로 district halls (no operator rate page)
- **Gangnam** — queries 1, 2, 7, 9, 10, 11 → COEX meeting rooms (2 recorded), COCOC (2 recorded), SpaceShare Samsung (1 recorded), Gangnam district 유휴공간 (fee table image-only, excluded)
- **Seocho / Gangnam station** — query 2 → COCOC
- **Seongsu** — queries 3, 14 → 성동구 자치회관 halls (weekday-only rentals, excluded), 성공 스페이스 (recorded, no fee published), 성수한옥 (site unreachable)
- **Hongdae / Mapo** — queries 15, 17, 22 → KT&G 상상마당 (recorded), 서울창업허브 공덕 (client-rendered list, no capture), 프론트원 (DNS failure — front1.kr now redirects to D.CAMP)
- **Jongno / Daehak-ro** — query 19 → 마로니에공원 다목적홀 (recorded)
- **Yeouido** — query 21 → FKI Tower conference centre (no public rate page; page captured as a redirect shell only, nothing carried)
- **Jamsil** — covered by the general Seoul queries; no Jamsil operator rate page surfaced (롯데월드타워 event spaces are inquiry-only)
- **Mullae** — query 20 → 몽상가들 스페이스 (recorded; only the sub-room rate is published)
- **Pangyo (Bundang)** — query 18 → 경기창조경제혁신센터 (2 rooms recorded)
- **Itaewon / Yongsan** — queries 16, 23 → 노들섬 (2 rooms recorded); Itaewon itself returned only aggregator listings
- **Gwanak** — query 19 → 관악청년청 다목적강당 (50 persons, 30,000 KRW) reviewed and dropped: no geocoder returned a building-level point, so the coordinate would have been wrong-district

## Platform lane (registered platform, opened and closed)

- **Space Cloud (space-cloud, active in `references/venue_platforms.json`)** — opened with four listing captures (`spacecloud_48685.html`, `sc_82926.html`, `sc_56454.html`, `sc_78369.html`). Disposition: **closed, nothing carried**. The platform publishes capacity, price and amenities, but withholds the exact address until booking ("자세한 주소는 예약 확정 후 예약 내역에서 확인할 수 있습니다"), so no platform-only record can carry a real address or a geocoded coordinate pair.
- Aggregators seen and not used as evidence: shareit.kr, spacecloud listings via search, naver blogs, junkangworld, platformdodam, chrisandpartners, event-us.

## Retained — 16 records in `venues.raw.json`

- 1. DDP 디자인홀 (110) — 3,256,000 KRW/day — USD 2,439.13
- 2. DDP 잔디사랑방 (150) — 2,988,000 KRW/day — USD 2,238.37
- 3. DDP 서울-온 화상스튜디오 (80) — 2,651,000 KRW/day — USD 1,985.92
- 4. 한국컨퍼런스센터 대강당 (170) — 2,420,000 KRW/9h package — USD 1,812.87
- 5. 한국컨퍼런스센터 컨퍼런스룸 A (54) — 176,000 KRW/h × 8 — USD 1,054.76
- 6. COEX 컨퍼런스룸 300 (300) — unpublished — null
- 7. COEX Studio 159 (100) — unpublished — null
- 8. 경기창조경제혁신센터 대회의실 (68) — 264,000 KRW/day — USD 197.77
- 9. 경기창조경제혁신센터 국제회의장 (540) — 2,640,000 KRW/day — USD 1,977.68
- 10. 마로니에공원 다목적홀 (100) — 30,000 KRW/2h → 8h estimate — USD 89.89
- 11. 몽상가들 스페이스 서브 세미나룸 (70) — 55,000 KRW/h × 8 — USD 329.61
- 12. 노들섬 라이브하우스 (456) — 4,000,000 KRW/weekend — USD 2,996.48
- 13. 노들섬 노들라운지 (capacity unpublished) — 1,346,000 KRW/weekend — USD 1,008.32
- 14. KT&G 상상마당 홍대 라이브홀 (capacity unpublished) — unpublished — null
- 15. 스페이스쉐어 삼성역센터 컨퍼런스 B룸 (60) — unpublished — null
- 16. 성공 스페이스 (110) — unpublished — null

(The scorer's output is the authority; this list mirrors `venues.shortlist.json`.)

## Reviewed and excluded (with reason)

- **성동구 자치회관 다목적실 (성수1가제1동 30, 성수2가제1동 50, 용답동 50)** — the 용답동 record states weekend and public-holiday rentals are not accepted; the same 자치회관 pattern applied to the other two, so a Saturday event cannot be booked. Excluded rather than recorded as shortlist-ready.
- **관악청년청 다목적강당 (50, 30,000 KRW, 120-240 minutes)** — right size and price, but no geocoder returned a building-level point for 남부순환로 1759 (Nominatim returned a street centroid in a different district, and Overpass answered HTTP 400 on the name search).
- **마포구청 시청각실 (80)** — the 구청 page's fee table is not rendered in the captured HTML, and the only figures found came from a public-data aggregator, which is not acceptable final evidence.
- **서울창업허브 공덕 대강당 (200)** — the rental list is client-rendered; the room rows (including the 200-person 대강당) are not in the HTML and therefore not capturable.
- **SETEC 컨벤션홀 / 세미나실 1-3 (362 / 189 m²)** — the facility pages give areas but the fee table and capacities are rendered by script; no rate or headcount could be captured, and the venue is a convention-scale hall.
- **시민청 (서울시청 지하)** — rooms cap at about 30 persons, below the brief.
- **FKI 타워 컨퍼런스센터 (여의도)** — no public rate page; the site answered a JavaScript shell.
- **프론트원 / D.CAMP 마포** — front1.kr no longer resolves and redirects to D.CAMP; no rental rate published.
- **성수한옥** — TLS connection failed on two host forms; no capture, so nothing carried.
- **강남구 유휴공간 다목적강당 (80석, 143,000원/2시간)** — the list page carries the address and the fee only outside the rendered HTML (fee rows are images).
- **SpaceShare 서울중부센터 토파즈홀 (70) / 을지로입구 넥서스홀 (120)** — the centre's fee tables are published only on a Naver blog and in date-selected booking widgets, not on a static page.

## Open items carried to the reviewer

1. Five records have no published price (COEX x2, 상상마당, 스페이스쉐어, 성공 스페이스); each carries a `cost_unknown` question, and none has been estimated.
2. Two records have no published headcount (노들라운지, 상상마당) and one has an ambiguous headcount (몽상가들); all three are leads.
3. Station access is stated on six records only, from captured operator pages (COCOC 대강당 and 컨퍼런스룸 A: Gangnam exit 5, two minutes; 판교 대회의실: Pangyo exit 4, about seventeen minutes; 상상마당: Hongik University exit 9 / Hapjeong exit 3; 스페이스쉐어: Samsung exit 8, two minutes; 몽상가들: five minutes from a station, name not published). The other ten records do not state a station (DDP ×3, COEX ×2, 판교 국제회의장, 마로니에공원, 노들섬 ×2, 성공 스페이스); their station is left unasserted — those records do **not** carry a location question kind, and no station name has been guessed.
4. DDP and 노들섬 both publish 10:00 openings, so neither can serve a 09:00 start; this is recorded as an availability question, not smoothed over.
