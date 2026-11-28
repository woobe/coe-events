# Capture index — Seoul 2027 deep-refresh run (accessed 2026-11-28)

Every page cited in `venues.raw.json`, `calendar_conflicts.json` and `communities.raw.json` is saved in this directory, plus the FX source, the geocoder responses, and the context/platform captures listed at the end. Fetches were made with `curl` (browser user agent, Korean `Accept-Language`, 30-60 s timeouts, `-k` only where a Korean public site serves an incomplete certificate chain). No headless-browser DOM dump was needed: every cited page was readable as served.

## FX basis

- `ecb_eurofxref_daily_2026-11-28.xml` → https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml → HTTP 200, 1,547 bytes → ECB euro foreign exchange reference rates, reference date 2026-11-27 (EUR/USD 1.0957, EUR/KRW 1462.65) — the basis for every USD figure in this package

## Venue records — 16 records in `venues.raw.json`

- `ddp_designlab_rates.html` → https://ddp.or.kr/?menuno=725 → DDP rental-facility page: Design Lab Design Hall 627.6 m² / about 110 persons at 3,256,000 KRW per day, Jandi-sarangbang 570 m² at 2,988,000 KRW, Seoul-On studio 378.22 m² at 2,651,000 KRW — fee table only: the captured page carries no HH:MM token, so it is **not** the source for any operating window (see the next line)
- `ddp_deep_designlab_facility.html` → https://deep.ddp.or.kr/introduce/c003.do → DDP 대관정보서비스 Design Lab facility page: the '대관 가능 시간' table (컨벤션 '08:00 ~ 20:00 (12시간)'; 전시관(뮤지엄) · 갤러리문 · 이간수문전시장 '10:00 ~ 21:00 (11시간)'; '기타 시설' '10:00 ~ 21:00 (11시간)'; '※ 기준시간을 초과하여 대관하는 경우 초과 시간당 기준액의 150% 적용') printed directly above the 디자인랩 대관료 table (화상스튜디오 2,651,000 / 디자인홀 3,256,000 / 잔디사랑방 2,988,000 per day) — the cited source for the three DDP `event_window_evidence` entries
- `ddp_event_guide.pdf` → https://ddp.or.kr/file/attach/DDP_EVENT_GUIDE2.pdf → DDP Organizer Guide (4,501,743 bytes): room equipment (6.4m x 4m LED, LS9 console, d&b speakers, Shure microphones), Jandi-sarangbang capacity about 150-200 persons and catering capability, Seoul-On studio up to 80 persons and broadcast chain, food brought into the Design Lab requires prior consultation
- `cococ_home.html` → https://www.cococ.kr/ → 한국컨퍼런스센터 room index: 대강당 (170명) 363,000 KRW/h, 컨퍼런스룸 A (54명) 176,000 KRW/h, other rooms, 2 minutes from Gangnam station exit 5, free screens/projectors/microphones, catering service, address 서초구 강남대로53길 8
- `cococ_product_auditorium.html` → https://www.cococ.kr/product/auditorium/ → 대강당 detail: 384 m², 170 seats (132 + 8 + 30), 24-hour daily operation, 9-hour package 2,420,000 KRW, 4K projector / 250-inch screen / microphones / Wi-Fi
- `coex_meeting_facilities.html` → https://business.coex.co.kr/meeting-room/facilities-information/ → COEX meeting-room facilities: 컨퍼런스룸(남) 3F 20-300 persons at 40-311 m², Studio 159 294 m² / 70-100 seats / up to 100 people; no rates published
- `pangyo_gcei_facility.html` → https://www.pangyotechnovalley.org/base/rentalManagement/facility?building=4&menuLevel=4&menuNo=3 → 판교테크노밸리 rental page: 경기창조경제혁신센터 대회의실 68 seats / 146 m² at 264,000 KRW per day (VAT included), 국제회의장 540 seats / 913 m² at 2,640,000 KRW per day, internet + beam + screen + microphone included, food ban, 판교역 4번 출구 17 minutes
- `eshare_marronnier.html` → https://eshare.go.kr/UserPortal/Upv/UprResrcFacl/index.do?rsrc_no=DF03O1304240 → 공유누리 record for 마로니에공원 다목적홀: 143 m², 50-100 persons, 30,000 KRW per 2 hours VAT excluded, use hours 10:00-20:00, 대학로 104
- `mongsang_pricing.html` → https://www.mongsang-space.com/pricing → 몽상가들 스페이스 pricing: 서브 세미나룸 44,000 KRW/h weekday and 55,000 KRW/h weekend/holiday, catering from 10,000 KRW per person, '최대 70인', food and alcohol brought in require separate consultation
- `mongsang_home.html` → https://www.mongsang-space.com/ → venue description: 문래동, soundproofing, unlimited parking, 5 minutes from a subway station, screen/beam/prompters, footer address 문래북로 8 에이스NS타워 B102
- `nodeul_livehouse.html` → https://nodeul.org/facility/livehouse/ → 노들섬 라이브하우스: 1,320 m², 456 seats / 708 standing, weekend 4,000,000 KRW for one performance and 6,000,000 for two (VAT excluded), performance window 10:00-23:00, sound/light/instruments/house manager included
- `nodeul_lounge.html` → https://nodeul.org/facility/nodeul-lounge/ → 노들섬 노들라운지: 557 m², capacity '행사 운영에 따라 상이', 1,003,000 KRW weekday and 1,346,000 KRW weekend/holiday (VAT excluded), summer window 10:00-21:00
- `nodeul_rent_guide.html` → https://nodeul.org/rent-guide/ → Nodeul rental guide: 2026 second-half open call runs to 2026-10-31, schedules subject to the Nodeul Global Art Island project, applications at least four weeks ahead, address 양녕로 445
- `sangsangmadang_rental.html` → https://www.sangsangmadang.com/rental/list → KT&G 상상마당 rental guide: four-step application, review within seven days, no published capacity, rate or hours
- `sangsangmadang_space.html` → https://www.sangsangmadang.com/main/HD → 상상마당 홍대 building page: address 어울마당로 65, access from Hongik University station exit 9 and Hapjeong station exit 3
- `spaceshare_home.html` → https://www.spaceshare.co.kr/ → 스페이스쉐어 centre index: eight Seoul centres, room lists, Samsung centre described as two minutes from Samsung station exit 8
- `spaceshare_samsung.html` → https://sm.spaceshare.kr/ → 삼성역센터 site: 11 rooms including 100+ person halls, address 영동대로 96길 20 대화빌딩 지하 1층
- `spaceshare_reservation.html` → https://spaceshare.co.kr/reservation/ → reservation and quote page: 삼성역센터 room list including 컨퍼런스B룸(60명) and 컨퍼런스C룸(64명), four bookable bands (종일 09:00-18:00, 오전 09:00-12:00, 오후 13:00-18:00, 야간 19:00-22:00), no hourly booking, contract confirmed on a 30% deposit
- `sd_facility_list.html` → https://www.sd.go.kr/booking/selectUnityFcltyOperWebList.do?key=4837 → 성동구 신속예약 facility list: 성공 스페이스 (회의실, 110 persons, 유료, phone), 성수1가제1동 30, 성수2가제1동 50, 용답동 50 with the note that weekend and public-holiday rentals are not accepted at the 용답 hall

## Geocoder responses — 10 used, one per distinct venue address (plus 10 failed building-level lookups for 성공 스페이스)

- `geo_ddp2.json` → https://nominatim.openstreetmap.org/search?q=동대문디자인플라자,+서울&format=jsonv2&limit=1 → 37.5670686, 127.0098990; display name '동대문디자인플라자, 281, 을지로, 을지로7가, 광희동, 중구, 서울특별시, 04566'
- `geo_cococ.json` → https://nominatim.openstreetmap.org/search?q=강남대로53길+8,+서초구,+서울특별시&format=jsonv2&limit=1 → 37.4941299, 127.0274305; street-level match for 강남대로53길, 서초2동 (the building is not a mapped point — see source_uncertainty_notes.md §3)
- `geo_coex.json` → https://nominatim.openstreetmap.org/search?q=서울특별시+강남구+영동대로+513&format=jsonv2&limit=1 → 37.5125275, 127.0588489; 513 영동대로, 삼성동
- `geo_pangyo.json` → https://nominatim.openstreetmap.org/search?q=경기도+성남시+분당구+대왕판교로645번길+12&format=jsonv2&limit=1 → 37.4003390, 127.1048351; '경기창조경제혁신센터, 12, 대왕판교로645번길, 삼평동'
- `geo_marronnier4.json` → https://nominatim.openstreetmap.org/search?q=마로니에공원&format=jsonv2&limit=1 → 37.5805083, 127.0028444; '마로니에공원, 104, 동숭동, 이화동, 종로구'
- `geo_mongsang.json` → https://nominatim.openstreetmap.org/search?q=서울특별시+영등포구+문래북로+8&format=jsonv2&limit=1 → 37.5213537, 126.8856839; 8 문래북로, 문래동6가
- `geo_nodeul.json` → https://nominatim.openstreetmap.org/search?q=서울특별시+용산구+양녕로+445&format=jsonv2&limit=1 → 37.5181487, 126.9582184; '노들섬 라이브하우스, 445, 양녕로, 이촌2동'
- `geo_sangsangmadang.json` → https://nominatim.openstreetmap.org/search?q=서울특별시+마포구+어울마당로+65&format=jsonv2&limit=1 → 37.5509886, 126.9210678; 'KT&G 상상마당 빌딩, 65, 어울마당로, 서교동'
- `geo_spaceshare_samsung.json` → https://nominatim.openstreetmap.org/search?q=서울특별시+강남구+영동대로96길+20&format=jsonv2&limit=1 → 37.5107900, 127.0642270; '대화빌딩, 20, 영동대로96길, 삼성동'
- `geo_seonggong.json` → https://nominatim.openstreetmap.org/search?q=서울특별시+성동구+왕십리로+135&format=jsonv2&limit=1 → 37.5600451, 127.0364011; **road-segment point, not the building**: display name '왕십리로, 행당동, 행당1동, 성동구, 서울특별시, 04751'. Nominatim returns the 왕십리로 way for this address, so the record uses exactly this pair and labels it a street-level point (see source_uncertainty_notes.md §2)

### 성공 스페이스 building-level lookups — all failed, all kept

Ten further geocoder calls tried to resolve the 상가동 building at 왕십리로 135. None returned a building point; the responses are stored so the failure is auditable, not asserted.

- `geo_seonggong_bldg.json` → q='서울특별시 성동구 왕십리로 135 상가동' → 0 hits
- `geo_seonggong_housenumber.json` → q='왕십리로 135, 성동구, 서울특별시' → 3 hits, every one the 왕십리로 road way
- `geo_seonggong_structured.json` → street='135 왕십리로', city=서울특별시, county=성동구 → 3 hits, every one the road way (first hit 37.5600451, 127.0364011)
- `geo_seonggong_freeform2.json` → q='서울 성동구 왕십리로 135' → 3 hits, every one the road way
- `geo_seonggong_freeform3.json` → q='왕십리로135' → 0 hits
- `geo_seonggong_name.json` → q='성공스페이스' → 0 hits
- `geo_seonggong_overpass.json` → Overpass `addr:street~왕십리로` + `addr:housenumber=135` in the Seongdong bbox → 0 elements
- `geo_seonggong_overpass_named.json` → Overpass `name~성공` in the same bbox → 0 elements
- `geo_seonggong_op_hnum135.json` → Overpass `addr:housenumber=135` across the wider bbox → 3 elements, all on other streets (다산로, 답십리로64길, 아차산로)
- `geo_seonggong_op_street_presence.json` → Overpass `addr:street~왕십리` → mapped houses at 206, 287, 291-16, 328 and 지하374; no 135

## Calendar records — 7 rows in `calendar_conflicts.json`

- `aiexpo_kr.html` → https://aiexpo.co.kr/ → AI EXPO KOREA 2027: '4. 14 (수) – 16 (금), COEX Hall A', 10th edition
- `wis2027_en.html` → https://www.worlditshow.co.kr/eng/introduce/01.php → World IT Show 2027: 'Dates April 21 – 23, 2027', '10:00-17:00', 'COEX, SEOUL, KOREA'
- `smw2027_en.html` → http://seoulmetaweek.com/en → Seoul Meta Week 2027: '2027. 04. 29 - 30', 'Coex, Grand Ballroom', 7th edition
- `aisummitseoul_2027.html` → https://www.aisummitseoul.com/2027-agenda → AI Summit Seoul & Expo 2027: 'Aug 11–13, 2027 · COEX Grand Ballroom & Hall B, Seoul'
- `paiexpo2027_en.html` → https://p-aiexpokorea.com/en/ai-expo-english/ → Physical AI EXPO KOREA 2027: 'September 9 (Thu) – 11 (Sat), 2027', Songdo Convensia Hall 4
- `kes2027_home.html` → https://kes2026.micehub-gov.com/fairDash.do?hl=KOR → KES 2027: '2027.10.12–15 | COEX' and '2027.10.20–22 | KINTEX'
- `koreabuild_home.html` → https://koreabuild.co.kr/ → 코리아빌드위크 2027: '8. 4(수) – 7(토) 서울 코엑스' (second-half edition) and the February KINTEX edition

## Community records — 14 records in `communities.raw.json`

- `comm_moducon2026.html` → https://moducon.modulabs.co.kr → 모두콘 2026: '2026년 12월 12일(토) · 이화여대 ECC'
- `comm_modulabs.html` → https://modulabs.co.kr/ → Modulabs site: 모두콘 2026, 모두팝 free seminars, courses marked 모집중, community lounge
- `comm_pytorch_kr.html` → https://pytorch.kr/ → PyTorchKR blog index: dated posts Oct 2026, KVCache Meetup Korea held 2026-09-30 at 드림플러스 강남
- `comm_aitinkerers_seoul.html` → https://seoul.aitinkerers.org/ → AI Tinkerers Seoul: 'Next event: Thursday, December 31, 2026', builder demo-night format
- `comm_gdgoc_dgu.html` → https://gdg.community.dev/events/details/google-gdg-on-campus-dongguk-university-seoul-south-korea-presents-gdgoc-dgu-hangang-picnic-meetup/ → GDGoC Dongguk University Hangang Picnic Meetup, May 8, 2026
- `comm_meetup_gdgwebtech.html` → https://www.meetup.com/gdg-webtech/ → GDG Korea WebTech group: 1,163 members, organiser meetup listed as a past event
- `comm_meetup_gdgcampus.html` → https://www.meetup.com/gdg-campus/ → GDG Campus Korea group: 727 members, newest past event 2020
- `comm_meetup_seoulai.html` → https://www.meetup.com/seoul-ai-meetup/ → Seoul AI Meetup group: 318 members, newest past event 2025-03-20
- `comm_meetup_seoulweb3.html` → https://www.meetup.com/seoulweb3/ → SeoulWeb3 group: 534 members, newest past event 2023-04-27
- `comm_kbca.html` → https://www.kblockchain.org/ → 한국블록체인협회 notice board; newest visible items 2023
- `comm_seoulaihub.html` → https://seoulaihub.kr/ → 서울 AI 허브: programme intake/education/event application text, no dated public event
- `comm_ainetwork.html` → https://ainetwork.ai/ → AI Network project site, © 2026 footer, no dated event
- `comm_decenter.html` → https://www.decenter.kr/ → 디센터 news index with items dated 2026-11-27
- `comm_hashed.html` → https://www.hashed.com/ → Hashed: Hashed Potato Club, EastPoint:Seoul, Worldcoin meetup at Hashed Lounge, Seoul office address
- `comm_ethseoul2024.html` → https://ethseoul2024.devfolio.co/ → ETHSeoul 2024: Mar 29-31, 2024, Neowiz Pangyo Tower, organised by KryptoSeoul / Ludium / Dystopia Labs

## Context captures (not cited as venue, calendar or community evidence)

- `kasa_2027_calendar.html` → https://www.kasa.go.kr/bbs/BBSMSTR_000000000018/view.do?nttId=B000000003234Li6nD2 → the 2027 월력요항 notice page (우주항공청공고 제2026-0078호); the holiday table itself is not rendered in the captured HTML, so the lunar dates used in this package come from the KR registry rows, not from this page
- `kbw_home.html` → https://koreablockchainweek.com/ → KBW2027 landing page: 'Join ... for KBW2027' and 2027 participation applications, with no 2027 dates printed — the basis for the unknown-date note
- `atcenter_home.html` (atcenter.go.kr) and `coex_home.html` (coex.co.kr) → convention-centre home pages checked for a published room-rate table; neither exposes one (COEX routes rates through the business site, which publishes exhibition-hall rates only)
- `mapo_cheongsa.html` → https://www.mapo.go.kr/site/main/content/mapo040203 → 마포구 청사시설물 대관신청 page: eligibility text, fee table not rendered in the captured HTML
- `gangnam_rental.html` → https://www.gangnam.go.kr/board/community_center/list.do?mid=ID04_040801 → 강남구 유휴공간 대관 list: row text does not include fees in the capture (fee rows are images), so no Gangnam district hall is carried
- `eshare_gwanak_youth.html` → https://eshare.go.kr/UserPortal/Upv/UprResrcFacl/index.do?rsrc_id=EE31K4241351 → 관악청년청 다목적강당 (50 persons, 30,000 KRW, 120-240 minutes): reviewed, dropped because no geocoder returned a building-level point
- `spacecloud_48685.html`, `sc_82926.html`, `sc_56454.html`, `sc_78369.html` → https://www.spacecloud.kr/space/<id> → registered platform (Space Cloud) listings checked for the platform lane: prices and capacities are published but the exact address is withheld until booking ('자세한 주소는 예약 확정 후'), so no platform-only record can satisfy the coordinate requirement
- `startup_hub_gongdeok_rental.html` → https://hubgongdeok.startup-plus.kr/rental/place → 서울창업허브 공덕 rental list: rendered client-side, room rows not present in the HTML

## Build-run captures — local-requirement claims, school lane and photo pages (added 2026-11-28, Asia C5 build)

The three dated local claims and the school-lane finding read pages that the research run did not capture. Each is saved here, and every quoted segment is a verbatim substring of the saved bytes after tag stripping and whitespace normalisation (the PDF after text extraction).

- `claim_language_seoul_120_multilingual.html` → https://mediahub.seoul.go.kr/archives/2019947 → 내 손안에 서울 (서울특별시 대표 소통포털), '120다산콜 영어 문자상담 시작…다국어 맞춤 서비스 확대!', 발행일 2026.11.05 — the five-language telephone list, the multilingual online commitment, and the AI 통역 / VISIT SEOUL sentences quoted by the `language` claim
- `claim_alcohol_law_article5.html` → https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031277957 → 국가법령정보센터 조문정보, 「주류 면허 등에 관한 법률」 제5조(주류 판매업면허) [시행 2026.7.1., 법률 제21716호] — the 판매장마다 관할 세무서장 면허 sentence, the 신고 deeming sentence and its 「식품위생법」 영업허가 제1호, quoted by the `alcohol` claim; no 管轄 table is printed
- `claim_alcohol_nts_guidebook_2023.pdf` → https://www.nts.go.kr/comm/nttFileDownload.do?fileKey=219e161b1c0c6d770d5f811263e302d9 → 국세청 주류면허 신청 가이드북 (2023), 52 pages, 1,895,503 bytes — Ⅴ. 주류 판매면허 신청 → 의제주류판매업면허 민원개요 and the 식품접객업 category bullet, plus Ⅲ. 시행령 제8조③ '판매장 관할 세무서장'; text extracted with pypdf for quoting
- `claim_food_seoul_foodservice.html` → https://news.seoul.go.kr/welfare/archives/221025 → 서울특별시 시민건강국 식품정책과, '식품접객업 영업현황 및 신고(허가)처리 과정' (banner 수정일 2018-11-08) — the 영업의 종류 table, 허가업종/신고업종, 처리기관 : 구청(위생담당 부서), 허가처리 기한 3일 and 신고수리 3시간, quoted by the `food` claim
- `school_kr_registry_extract.json` → projection of the installed registry `/home/joe/.hermes/skills/plan-event/references/school_holidays.json` (sha256 `3b20667de940342954040f06d6695d490d8e27515d536969d127a0fa92bacdaf`) → KR:seoul is listed, 20 KR rows all with jurisdiction_id KR, 0 KR:seoul holiday rows, 0 KR:seoul coverage rows; the file records the sha256 and the query so the absence is reproducible
- `school_neis_schedule_api.html` → https://www.data.go.kr/data/15137088/openapi.do → 교육부_나이스(NEIS) 교육정보 개방 포털_학사일정 (공공데이터포털) — the 설명 paragraph and the (제공데이터) field list showing 학사일정 is a per-school feed
- `school_sen_index_netfunnel.html` → https://www.sen.go.kr/ → 477-byte NetFunnel queue script served instead of the education office's index; kept as blocked evidence, not read as an absence of policy
- `venue_coex_studio159.html` → https://business.coex.co.kr/meeting-room/studio-159/ → the Studio 159 room gallery that supplies the three Studio 159 photographs
- `venue_coex_conference3f.html` → https://business.coex.co.kr/meeting-room/conference-room-3f/ → the 컨퍼런스룸(남) 3F block page (room 300 is 264 m², 114 lecture / 225 theatre) whose gallery carries no per-room caption; the basis for the withheld room-300 photo record

## Failed fetches (attempted, not stored)

- `https://front1.or.kr/` — DNS not resolvable
- `https://www.seongsuhanok.com/` and `https://seongsuhanok.com/` — TLS connect failure
- `https://www.kryptoseoul.com/` — DNS not resolvable
- `https://gdg.kr/` — connection timeout
- `https://www.dcamp.kr/` — HTTP 404
- `https://www.awskrug.github.io/` — 273-byte redirect shell; `/meetup/` answered HTTP 404
- `https://pydata.org/seoul/` — HTTP 404
- `https://www.setec.or.kr/front/rent/rent02.do` and `/front/location/traffic.do` — HTTP 200 with a JavaScript-rendered fee table / HTTP 404
- `https://www.mongsang-space.com` (home) — HTTP 200 but the pricing page is the only page carrying rates
