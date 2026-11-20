# Venue discovery log — Seoul, 2027 H1 (research run 2026-11-20)

Raw evidence pass for a free community Decentralized AI Day, 50-125 people, Saturday,
09:00-17:00 (8 hours). Everything below was fetched on 2026-11-20 from the working
machine; timestamps are the fetch date, not a browsing history.

## Method

1. Seed: the Seoul 2026 Q4 run (`research/seoul/2026-q4/venues.raw.json`) was read as a
   lead list only. Its 6 venues (Nodeul Island, DDP Design Hall, DDP Conference Hall,
   COEX Conference Room 300, Mongsang Space Mullae, KT&G SangSangMadang) carried no
   coordinates, so every retained venue was re-fetched and re-geocoded this pass.
2. Discovery queries (Korean and English):
   - `서울 세미나실 대관 100명 대관료 공간 대여`
   - `Seoul tech event venue hire 100 people hourly rate conference room`
   - `D.CAMP 서울 행사장 대관 dcamp.kr event hall rental`
   - `문화비축기지 대관 안내 대관료 T6 원형극장`
   - `코엑스 컨퍼런스룸 대관 안내 3층 300호 수용인원 임대료`
   - `연세대 백양누리 그랜드볼룸 대관료 신청 안내`
   - `KT&G 상상마당 홍대 라이브홀 대관 안내 신청 대관료`
3. Fetch route: `curl` with a desktop UA; pages that returned 0 bytes or a JS shell were
   re-fetched with headless Chromium
   (`chrome --headless=new --dump-dom --virtual-time-budget=45000`). DDP, GDG Seoul and
   the Modulabs event listing needed the render path.
4. Coordinates: OpenStreetMap Nominatim lookups (2026-11-20, 1 request/second), recorded
   per venue as an `openstreetmap.org` object URL in `evidence.geo`.

## Retained (13 entries, 10 with coordinates)

Price evidence comes in two categories, and the counts are deliberately separate:

- **Published rate tables at four venues** — SETEC (numeric per slot), DDP (numeric per
  hour/3h/day), 노들섬 (numeric weekday/weekend/holiday), 어울림플라자 (a
  `350,000~540,000원` band whose per-row unit is not stated, so no figure is claimed).
- **Rate-derived 8-hour estimates from two Space Cloud listings** — 그라운드옥탑
  (`200,000원/시간` weekend) and 앙트레블 (`88,000원/시간`), both labelled
  `estimated_from_rate`, not quotes.

That is why this log says "four venues" for published tables while `evidence_summary.md`
lists six KRW amounts: four table figures (three usable numbers plus one unusable band)
and two derived estimates. Every converted amount uses the ECB reference rate dated
2026-11-20 (EUR/USD 1.0990, EUR/KRW 1472.04, i.e. 1 USD = 1,339.44 KRW); USD totals are
rounded from the KRW total, so an hourly figure times eight can differ by one cent.

- SETEC 컨벤션센터 — 세미나실 1, 세미나실 2. `setec.or.kr/front/rent/rent05.do`,
  heading `사용료 / 시간대별 사용료 (부가가치세 별도, 단위 : 원)`: 세미나실1 189㎡
  8~17시(전일 8H) 890,000원; 세미나실2 166㎡ 760,000원; 컨벤션홀 422㎡ 2,240,000원.
  Hours 08:00-21:00. 2027 convention rental recruitment opened 2026-10-01
  (`2027년 SETEC 컨벤션센터 대관 모집 (26.10.01, 오전 10시 ~)`).
- DDP — 디자인홀. `ddp.or.kr/?menuno=714` (rendered), table `디자인랩 대관료`:
  시간당 296,000 / 3시간 888,000 / 1일 3,256,000; 약 110명; 컨벤션 기준시간
  08:00-20:00; LED 디스플레이 6.4m x 4m — screen confirmed.
- 노들섬 라이브하우스. `nodeul.org/rent/rent-livehouse/`: 토,일,공휴일 4,000,000(1회)
  / 6,000,000(2회), VAT 별도; 공연대관 10~23시; 지정좌석 456석.
- 서울시 어울림플라자 — 다목적강당. `seouleoullim.or.kr/site/reserve/info`: 다목적강당
  350,000~540,000원, 70~100명, 토·일·공휴일 20% 가산 조항. The per-row unit is not
  stated for this row, so the cost stays unclaimed.

Saturday-hours evidence: D.CAMP publishes `토요일 09:00 ~ 18:00`
(`dcamp.kr/news/notice/7339`, 2026.06.02). Nodeul and 어울림플라자 price Saturday use
directly (weekend/holiday rate rows), so Saturday operation is evidenced for those three.

## Rejected or not retained (with reasons)

- **aT Center (atcenter.or.kr)** — WAF challenge to direct fetch; no rate page readable.
  Not recorded. If needed later, use a browser session, not curl.
- **한국과학기술회관 (stcenter.or.kr)** — connection timeout from this host.
- **WeWork Seoul (wework.com/l/meeting-rooms/seoul)** — 403 to this client.
- **프론트원 / front1.co.kr** — DNS NXDOMAIN at fetch (`DNS_PROBE_FINISHED_NXDOMAIN`);
  the building at 마포대로 122 is instead recorded through D.CAMP 마포, which publishes
  the same address.
- **SparkPlus (sparkplus.co.kr)** — empty response to curl; no rate page obtained.
- **패스트파이브 (fastfive.co.kr)** — homepage fetchable but the meeting-room path
  returned `페이지를 찾을 수 없습니다`; no rates obtained.
- **KT&G 상상마당** — `/rental/` returned a JSON 404; the working page is
  `/rental/list`, which publishes the procedure, the 홍대 address and the contact route
  but no capacity or rate, so it is retained only as a `lead`.
- **Mongsang Space Mullae** (2026 Q4 seed) — the earlier record was an
  `estimated_from_rate` at KRW 99,000/hour. No current page was found to re-verify that
  rate, so it was dropped rather than carried forward as a stale claim.
- **DDP Conference Hall / DDP Art Hall 2** — the 2026 Q4 seed quoted a Seoul Culture
  Portal rate notice. That notice could not be re-fetched this pass and the rendered DDP
  page covers 디자인홀 only, so the Atlantic-Hall rows were dropped instead of restated.
- **Culture-tank T0 문화마당** — outdoor plaza with a published hourly rate
  (`141,613원/시간`), but it is outdoors and its capacity is an area figure (7,620㎡)
  with no seated basis; not a fit for an 8-hour indoor programme.
- **Space Cloud listings with masked addresses** — 그라운드옥탑 (68421) and 앙트레블
  (29372) publish real weekend/hourly rates, screens and Wi-Fi, but the platform hides
  the street address until booking. Both are retained with `latitude`/`longitude` null
  and a `location` question; no coordinate was invented for them.
- **Impact Hub Seoul** — still does not exist (no Seoul record in the installed
  `impact_hub_locations.json`); no hub seed was used.

## Access failures logged in `city_input.open_questions`

aiexpo.co.kr (redirect loop / render timeout), parks.seoul.go.kr deep links (404, content
read through the search-indexed page text), gdg.community.dev (404 to curl, fine under
render), ddp.or.kr (0 bytes to curl, fine under render), sparkplus.co.kr, front1.co.kr,
wework.com, atcenter.at.or.kr, stcenter.or.kr.

## Coordinate notes

- SETEC: OSM node 3720964309 (`amenity=conference_centre`). A street-name query first
  returned a wrong segment of 남부순환로 (수서동); the node result was used instead.
- D.CAMP 선릉: OSM address node 13946798758 at 551 선릉로 (the node is a shop inside the
  building; the coordinate is the published street address).
- D.CAMP 마포: OSM way 879299975, 마포대로 122 (프론트원 building, 공덕동) — the address
  printed in the D.CAMP site footer.
- COEX: OSM node 12192172874 at 513 영동대로 (코엑스몰 unit on the complex) — the published
  COEX street address.
- 어울림플라자: Nominatim returned only road-level features for 공항대로 489 / 등촌동;
  no building object was found, so coordinates are null rather than a road centroid.
- 백양누리: OSM node 13202367571 (`연세대 백양누리 플라자 더라운지, 50, 연세로`).
- 문화비축기지: OSM node 13805210084 (`문화비축기지 T2 공연장, 87, 증산로`) — the site,
  not the T6 room; recorded as the venue location.
- 상상마당: OSM way 299797614 (`KT&G 상상마당 빌딩, 65, 어울마당로`).
