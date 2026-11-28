# Capture index — Kyoto 2027 deep-refresh run (accessed 2026-11-28)

Every page cited in `venues.raw.json`, `calendar_conflicts.json` and `communities.raw.json` is saved in this directory. Format: file → source URL (HTTP status, bytes at fetch) → what it evidences.

Fetches were made with `curl` (browser user agent, 45-120 s timeouts) or headless Chromium where noted; geocodes use the Geospatial Information Authority of Japan address-search API (a government geocoder) and the JSON responses are stored as `geo_*.json`.

## FX basis

- `ecb_eurofxref_daily_2026-11-28.xml` → https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml → HTTP 200, 1547 bytes → ECB euro foreign exchange reference rates, reference date 2026-11-27 (EUR/USD 1.0957, EUR/JPY 174.81) — the basis for every USD figure

## Venues — records in venues.raw.json

- `kokoka_en_facility.html` → https://kcif.or.jp/web/en/facilityrental/facility → HTTP 200, 43796 bytes → kokoka official English fee page: nine rooms, weekday and Sat/Sun/holiday block rates, capacities, 09:00-21:00 rule
- `kokoka_jp_overview.html` → https://www.kcif.or.jp/web/jp/facilityrental/overview/ → HTTP 200, 48992 bytes → kokoka official Japanese rental overview: application procedure, 09:00-20:30 reception, address, 09:00-21:00 restriction
- `kokoka_access.html` → https://www.kcif.or.jp/web/jp/access/ → HTTP 200, 33561 bytes → kokoka access page: 〒606-8536 京都市左京区粟田口鳥居町2-1, 最寄り駅から徒歩6分
- `asny_accessmap.html` → https://asny.ne.jp/asnymap.html → HTTP 200, 14870 bytes → 京都アスニー official access map: metro/JR Nijo (二条) station, then city bus 15 or 52 to the 丸太町七本松 stop and about 400 m west on foot (no station within walking distance)
- `heartpia_fee.html` → https://heartpia-kyoto.jp/convention/fee.html → HTTP 200, 10597 bytes → ハートピア京都 official fee page: block and continuous-use rates for 大会議室 and 第5会議室, AV equipment prices, closure dates; page banner reads 地下鉄丸太町駅直結 (direct underground link to Marutamachi station)
- `terminal_contact.html` → https://kyoto.theterminal.jp/contact/ → HTTP 200, 17586 bytes → THE TERMINAL KYOTO access page: 市営地下鉄「四条」駅 6番出口 徒歩6分, 阪急「烏丸」駅 徒歩6分; daily 09:00-18:00 hours only
- `rekisaikan_home.html` → https://rekisaikan.jp/ → HTTP 200, 125650 bytes → 京都府立京都学・歴彩館 homepage access section: 京都市営地下鉄烏丸線 北山駅 1番出口から南へ徒歩約4分
- `kyotou_campus_access.html` → https://www.kyoto-u.ac.jp/ja/access → HTTP 200, 74138 bytes → 京都大学 access index (links to the three campuses; no rail or walking text for the clock tower)
- `kyotou_yoshida_access.html` → https://www.kyoto-u.ac.jp/ja/access/campus/yoshida → HTTP 200, 66552 bytes → 京都大学 吉田キャンパス access page: maps only, no station name or walking time in the readable text
- `miyakomesse_daikaigishitsu.html` → https://www.miyakomesse.jp/planner/information/conference-room-main/ → HTTP 200, 44292 bytes → みやこめっせ 大会議室 page: 182 m2, 120 people, included screen/whiteboard/projector and room Wi-Fi, fee row
- `miyakomesse_price.html` → https://www.miyakomesse.jp/planner/price/ → HTTP 200, 55324 bytes → みやこめっせ general price page: tax-inclusive statement, block structure, extension rates
- `miyakomesse_access.html` → https://www.miyakomesse.jp/access/ → HTTP 200, 27750 bytes → みやこめっせ access page: 〒606-8343, Higashiyama station 8 minutes
- `asny_rooms.html` → https://asny.ne.jp/room/ → HTTP 200, 45984 bytes → 京都アスニー room index: capacities, block rates, 09:00-21:00 hours, Tuesday closure, Wi-Fi service, alcohol prohibition
- `asny_kaigishitsu.html` → https://asny.ne.jp/room/015_kaigi.html → HTTP 200, 10883 bytes → 京都アスニー 会議室 page (40 seats) — below the 50-person brief, retained as context
- `elcient_conference_jp.html` → https://elcient.com/kyoto/conference → HTTP 200, 124906 bytes → ホテルエルシエント京都八条口 conference page: Room A/B capacities, 3 h / 7 h specials, overtime, 09:00-21:00, equipment list
- `hearton_kyo_places.html` → https://www.hearton.co.jp/hall/kyoto/kyo-places → HTTP 200, 58455 bytes → ハートンホテル京都 hall page: 嵐山 and 宇治伏見 capacities, duration bands, night surcharge, tax-inclusive statement
- `hearton_access.html` → https://www.hearton.co.jp/access/kyoto → HTTP 200, 55968 bytes → ハートンホテル京都 access page: 〒604-0836 船屋町405, Karasuma Oike 2 minutes
- `krp_price.html` → https://www.krp.co.jp/kaigi/room/price.html → HTTP 200, 76497 bytes → 京都リサーチパーク fee page: ルーム2 capacity and 土日祝 全日/夜間 rates, A/B/C room capacity 42
- `krp_access.html` → https://www.krp.co.jp/access/ → HTTP 200, 59860 bytes → KRP access page: 〒600-8813 中堂寺南町134 and 西地区 中堂寺粟田町90-94
- `krp_room_list.html` → https://www.krp.co.jp/kaigi/room/ → HTTP 200, 64730 bytes → KRP room list page (room-detail URLs indexed; /room/room2.html answered 404)
- `kyotou_kokusai_hall.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower/organizer/riyo-sisetu/kokusai → HTTP 200, 78677 bytes → 京都大学 国際交流ホール page: 300 seats in three rooms of 100, 09:00-21:30
- `kyotou_clocktower_charge.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower/organizer/charge → HTTP 200, 77477 bytes → 京都大学 百周年時計台記念館 fee schedule: hourly rates incl. 国際交流ホール 9,500/10,700 yen, tax included, part-hours rounded up
- `kyotou_riyo_sisetu.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower/organizer/riyo-sisetu → HTTP 200, 80466 bytes → 京都大学 利用できる施設 page: permission requirement for events matching the facility purpose
- `kyotou_organizer.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower/organizer → HTTP 200, 76759 bytes → 京都大学 organizer index (navigation only)
- `kyotou_clocktower.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower → HTTP 200, 78657 bytes → 京都大学 clock tower building page (navigation only)
- `rekisaikan_hall_annai.pdf` → https://rekisaikan.jp/cms/wp-content/themes/rekisaikan//pdf/hall/hall_annai.pdf → HTTP 200, 1283666 bytes → 京都府立京都学・歴彩館 hall guide: 小ホール 100 seats, LAN/Wi-Fi, streaming support, fee table, 17:00 weekend closure, purpose restriction
- `terminal_home.html` → https://kyoto.theterminal.jp/ → HTTP 200, 29358 bytes → THE TERMINAL KYOTO site: machiya event space, 09:00-18:00, no capacity or hire price published
- `fabcafe_meeting.html` → https://fabcafe.com/jp/kyoto/service/meeting-space/ → HTTP 200, 76701 bytes → FabCafe Kyoto 2F tatami room: 14 tatami, 5,500 yen/hour tax-inclusive, one-month booking window
- `fabcafe_access.html` → https://fabcafe.com/jp/kyoto/access/ → HTTP 200, 61236 bytes → FabCafe Kyoto access page: 〒600-8119 本塩竈町554, Gojo 10 minutes
- `impacthub_home.html` → https://kyoto.impacthub.net/ → HTTP 200, 100314 bytes → Impact Hub Kyoto homepage (HTTP 200, 0.7 s) proving the site is up and the failure is path-specific; links to /useourspace/
- `impacthub_useourspace_archive_20250217.html` → http://web.archive.org/web/20250217175235/https://kyoto.impacthub.net/useourspace/ → HTTP 200, 120797 bytes → Internet Archive capture (2025-02-17) of the Impact Hub fee page: 2F 会所 180 m2, 60-90 seats, 09:00-21:00, free projector/PA — the only readable copy

## Venues — access failures kept as evidence

- `impacthub_useourspace.html` → https://kyoto.impacthub.net/useourspace/ → HTTP 000, 0 bytes → live Impact Hub Kyoto fee page: HTTP 000, zero bytes, four attempts (evidence of the access failure only)
- `krp_room2.html` → https://www.krp.co.jp/kaigi/room/room2.html → HTTP 404, 45474 bytes → KRP ルーム2 detail URL: HTTP 404 — recorded as the reason AV is unconfirmed
- `kyotou_clocktower_facilities.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower/facilities → HTTP 404, 54348 bytes → attempted facility page: HTTP 404
- `heartpia_access.html` → https://heartpia-kyoto.jp/convention/access.html → HTTP 404, 19268 bytes → attempted ハートピア access URL: HTTP 404
- `asny_access.html` → https://asny.ne.jp/access/ → HTTP 404, 236 bytes → attempted 京都アスニー access URL: HTTP 404 (the official access map is `asny_accessmap.html`)
- `terminal_access.html` → https://kyoto.theterminal.jp/access/ → HTTP 404, 7477 bytes → attempted THE TERMINAL access URL: HTTP 404 (the live access page is `terminal_contact.html`)
- `rekisaikan_access.html` → https://rekisaikan.jp/access/ → HTTP 404, 33108 bytes → attempted 歴彩館 access URL: HTTP 404 (access text is on the homepage, `rekisaikan_home.html`)
- `kyotou_access.html` → https://www.kyoto-u.ac.jp/ja/about/facilities/campus/clocktower/access → HTTP 404, 54348 bytes → attempted clock-tower access URL: HTTP 404

## Venues — reviewed and excluded

- `terrsa_price.pdf` → https://www.kyoto-terrsa.or.jp/lib/pdf/guide/price.pdf → HTTP 200, 226428 bytes → 京都テルサ 2026-04-01 price PDF: 中会議室 96 seats at 48,840 / 68,860 yen — excluded because the PDF's 平日/土日祝 blocks could not be attributed without ambiguity
- `terrsa_home.html` → https://www.kyoto-terrsa.or.jp/ → HTTP 200, 39739 bytes → 京都テルサ homepage (address 〒601-8047 東九条下殿田町70)
- `terrsa_info.html` → https://www.kyoto-terrsa.or.jp/info/index.php → HTTP 200, 18179 bytes → 京都テルサ information page (context only)
- `campusplaza_fee.html` → https://www.consortium.or.jp/about-cp-kyoto/fee → HTTP 200, 77196 bytes → キャンパスプラザ京都 fee page: rates are PDF-only
- `campusplaza_fee_ippan.pdf` → https://www.consortium.or.jp/wp-content/uploads/page/123/20250812_shisetsufee_ippan.pdf → HTTP 200, 257298 bytes → キャンパスプラザ京都 general fee PDF: room capacities readable (ホール 184 m2 / 80 seats) but the fee rows cannot be attributed to rooms by text extraction — excluded rather than guessed
- `rihga_meeting_room.html` → https://www.rihga.co.jp/kyoto/party/plan/meeting-room → HTTP 200, 35635 bytes → リーガロイヤルホテル京都 meeting-room page: per-person banquet pricing, no plain 50-person room rate — excluded
- `keizaicenter_price.html` → https://keizai-center.kyoto/room/?type=price → HTTP 200, 54352 bytes → 京都経済センター fee page: 25 rooms, largest about 30 people — below the 50-person brief

## Calendar

- `cao_shukujitsu_2027.html` → https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html → HTTP 200, 20682 bytes → 内閣府 国民の祝日 page: 令和9年（2027年）block with 昭和の日 4月29日, 憲法記念日 5月3日, みどりの日 5月4日, こどもの日 5月5日 (the Golden Week row's source)

- `gionmatsuri_schedule.html` → http://gionmatsuri.or.jp/schedule → HTTP 200, 13999 bytes → 祇園祭山鉾連合会 official schedule: 17 July 前祭山鉾巡行, 24 July 後祭山鉾巡行
- `kyototravel_okuribi.html` → https://ja.kyoto.travel/event/major/okuribi → HTTP 200, 110587 bytes → 京都市公式 京都観光Navi 五山送り火 page: 8月16日, 20:00 ignition, 19:50-20:50 lighting blackout request
- `kyotomarathon_info.html` → https://kyoto-marathon.com/info/ → HTTP 200, 72091 bytes → 京都マラソン2027 official 大会実施要項: 2027-02-21, 08:55/09:00 starts, check-in at みやこめっせ 02-19/20
- `wmg2027_games.html` → https://wmg2027.jp/games/ → HTTP 200, 101051 bytes → World Masters Games 2027 KANSAI official outline: 2027-05-14 to 05-30, 35 sports, 50,000 target
- `kyotographie_2027_dates.html` → https://kyotographie.jp/en/news/2026/18727 → HTTP 200, 23895 bytes → KYOTOGRAPHIE official English news: 2027-04-17 to 2027-05-16
- `bitsummit_2027_dates.html` → https://bitsummit.org/%E3%80%8Cbitsummit%E3%80%8D2027%E5%B9%B4%E3%81%AE%E9%96%8B%E5%82%AC%E6%97%A5%E7%A8%8B%E3%82%92%E7%99%BA%E8%A1%A8%EF%BC%81%E4%BD%B5%E3%81%9B%E3%81%A6%E3%80%81%E3%81%94%E6%9D%A5%E5%A0%B4%E8%80%85/ → HTTP 200, 41202 bytes → BitSummit official post (2026-05-24): 2027-05-21 to 05-23 at みやこめっせ
- `bitsummit_home.html` → https://bitsummit.org/ → HTTP 200, 227391 bytes → BitSummit homepage confirming the 2027 edition announcements
- `kamigamojinja_home.html` → https://www.kamigamojinja.jp/ → HTTP 200, 81144 bytes → 上賀茂神社 official 賀茂祭（葵祭） page: 五月十五日
- `heianjingu_jidai.html` → https://www.heianjingu.or.jp/ritual/jidaimatsuri/ → HTTP 200, 35837 bytes → 平安神宮 時代祭 page: 毎年10月22日（雨天順延）
- `heianjingu_home.html` → https://www.heianjingu.or.jp/ → HTTP 200, 42544 bytes → 平安神宮 homepage (SSL chain failed; fetched with -k, content is the public site)
- `kyototravel_jidai.html` → https://ja.kyoto.travel/event/major/jidaimatsuri → HTTP 404, 71736 bytes → attempted 京都観光Navi 時代祭 URL: HTTP 404 (its text still references the 2026 10月22日 event)
- `aismiley_aihaku_osaka2027.html` → https://aismiley.co.jp/ai_news/aihaku_osaka_2027/ → HTTP 200, 389312 bytes → AIsmiley organiser announcement: AI博覧会 Osaka 2027 on 2027-01-20/21 at マイドームおおさか
- `japanit_osaka.html` → https://www.japan-it.jp/osaka/ja-jp.html → HTTP 200, 209676 bytes → Japan IT Week official hub: 2027 show calendar incl. 関西展 2027-11-17 to 11-19 at インテックス大阪
- `osc2027_osaka.html` → https://event.ospn.jp/osc2027-osaka → HTTP 200, 27383 bytes → オープンソースカンファレンス2027 Osaka: 2027-01-30 — excluded from the calendar because no topic relevance in the closed enum fits an OSS event
- `ivs_home.html` → https://www.ivs.events/ → HTTP 200, 1421548 bytes → IVS official site: only IVS2026 (2026-07-01 to 03, みやこめっせ + ホテルオークラ) is announced; no IVS2027 date exists yet

## Communities

- `comm_koin_events.html` → https://open.kyoto/event/ → HTTP 200, 814041 bytes → KOIN event calendar: dated 2026 and 2027 events, 京都経済センター 3F
- `comm_kyotoeggs.html` → https://kyoto-eggs.jp/ → HTTP 200, 14954 bytes → Kyoto eggs: 2026-11-14 定例会, 2026-10-10 例会, 2026-09-12 30th anniversary
- `comm_kc3.html` → https://kc3.me/ → HTTP 200, 112028 bytes → KC3 homepage navigation: KC3 2026/2025 and KC3Hack editions
- `comm_kc3_conf2026.html` → https://kc3.me/conf/conf2026/ → HTTP 200, 170843 bytes → KC3 2026 conference page: 2026-09-23 at 京都リサーチパーク
- `comm_cireds_kyoto.html` → https://cireds.doorkeeper.jp/ → HTTP 200, 34258 bytes → Doorkeeper データサイエンススクール京都: 2,029 members, sessions 2026-09-19 and 2026-09-01, upcoming 2027-01-15/01-30
- `comm_kandigi_ai.html` → https://kandigi.doorkeeper.jp/ → HTTP 200, 35830 bytes → Doorkeeper 関西デジタルコンテンツ事業協同組合: AI勉強会「スナックAI」 2026-12-14 in Kobe, 忘年会 2026-12-17
- `comm_oih.html` → https://www.innovation-osaka.jp/ → HTTP 200, 309125 bytes → 大阪イノベーションハブ homepage: dated news (2026.11.26 Tech Osaka Summit 2027 registration) and a 2026-11-28 event
- `comm_oih_events.html` → https://www.innovation-osaka.jp/event/ → HTTP 200, 143658 bytes → OIH event index (dated listings)
- `comm_gdg_kyoto.html` → https://www.kyoto-gtug.org/ → HTTP 200, 122014 bytes → GDG 京都 site: stated monthly in-person intention, external announcement channels, event reports since 2014, no dated 2026 event
- `comm_bck.html` → https://www.blockchainkyoto.org/ → HTTP 200, 1105480 bytes → 京都大学ブロックチェーン研究センター: research abstract, BCK21-BCK26 series navigation, no dated 2026 event
- `comm_kashima_lab.html` → https://www.ml.ist.i.kyoto-u.ac.jp/ → HTTP 200, 46265 bytes → 鹿島・竹内研究室 site: research themes and pages, no public event calendar
- `comm_lm_group.html` → https://lm.sys.i.kyoto-u.ac.jp/ → HTTP 200, 16623 bytes → 京都大学 学習機械分野 site: research/members/publications pages, address, no public event calendar
- `comm_pydata_osaka.html` → https://www.meetup.com/pydata-osaka/ → HTTP 200, 55506 bytes → Meetup 'Group not found' page served at meetup.com/pydata-osaka — evidence the August 2026 group URL no longer exists
- `comm_kyoto_cxo.html` → https://www.city.kyoto.lg.jp/sankan/page/0000350015.html → HTTP 200, 37967 bytes → 京都市 Kyoto Next CxO Community page (updated 2026-11-27): 145 + 80 members, monthly sessions, term to 2027-03-31
- `comm_miyakodeit.html` → https://mit.connpass.com/ → HTTP 202, 0 bytes → connpass みやこでIT group page: HTTP 202 with a 2,019-byte challenge body — bot wall, no content

## Geocode responses (GSI address search)

- `geo_asny.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E4%B8%AD%E4%BA%AC%E5%8C%BA%E8%81%9A%E6%A5%BD%E5%BB%BB%E6%9D%BE%E4%B8%8B%E7%94%BA9-2 → 京都府京都市中京区聚楽廻松下町9-2 → lat 35.019047, lon 135.738464
- `geo_elcient.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E5%8D%97%E5%8C%BA%E6%9D%B1%E4%B9%9D%E6%9D%A1%E6%9D%B1%E5%B1%B1%E7%8E%8B%E7%94%BA13 → 京都府京都市南区東九条東山王町13 → lat 34.983540, lon 135.761627
- `geo_fabcafe.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E4%B8%8B%E4%BA%AC%E5%8C%BA%E6%9C%AC%E5%A1%A9%E7%AB%88%E7%94%BA554 → 京都府京都市下京区本塩竈町554 → lat 34.995129, lon 135.765045
- `geo_hearton.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E4%B8%AD%E4%BA%AC%E5%8C%BA%E8%88%B9%E5%B1%8B%E7%94%BA405 → 京都府京都市中京区船屋町405 → lat 35.011631, lon 135.760818
- `geo_heartpia.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E4%B8%AD%E4%BA%AC%E5%8C%BA%E6%B8%85%E6%B0%B4%E7%94%BA375 → 京都府京都市中京区清水町375 → lat 35.016354, lon 135.759842
- `geo_impacthub.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=京都市上京区甲斐守町97 → 京都府京都市上京区甲斐守町97 → lat 35.024364, lon 135.753296
- `geo_kokoka.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E5%B7%A6%E4%BA%AC%E5%8C%BA%E7%B2%9F%E7%94%B0%E5%8F%A3%E9%B3%A5%E5%B1%85%E7%94%BA2-1 → 京都府京都市左京区粟田口鳥居町2-1 → lat 35.010658, lon 135.787567
- `geo_krp.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E4%B8%8B%E4%BA%AC%E5%8C%BA%E4%B8%AD%E5%A0%82%E5%AF%BA%E7%B2%9F%E7%94%B0%E7%94%BA93 → 京都府京都市下京区中堂寺粟田町93 → lat 34.994980, lon 135.738541
- `geo_kyotou.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E5%B7%A6%E4%BA%AC%E5%8C%BA%E5%90%89%E7%94%B0%E6%9C%AC%E7%94%BA → 京都府京都市左京区吉田本町 → lat 35.026962, lon 135.781967
- `geo_miyakomesse.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E5%B7%A6%E4%BA%AC%E5%8C%BA%E5%B2%A1%E5%B4%8E%E6%88%90%E5%8B%9D%E5%AF%BA%E7%94%BA9-1 → 京都府京都市左京区岡崎成勝寺町9-1 → lat 35.013077, lon 135.781433
- `geo_rekisaikan.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E5%B7%A6%E4%BA%AC%E5%8C%BA%E4%B8%8B%E9%B4%A8%E5%8D%8A%E6%9C%A8%E7%94%BA1-29 → 京都府京都市左京区下鴨半木町1-29 → lat 35.050365, lon 135.759750
- `geo_terminal.json` → https://msearch.gsi.go.jp/address-search/AddressSearch?q=%E4%BA%AC%E9%83%BD%E5%BA%9C%E4%BA%AC%E9%83%BD%E5%B8%82%E4%B8%8B%E4%BA%AC%E5%8C%BA%E5%B2%A9%E6%88%B8%E5%B1%B1%E7%94%BA424 → 京都府京都市下京区岩戸山町424 → lat 35.000706, lon 135.756927

## Local-requirement claims and the school lane (Kyoto store build, 2026-11-28)

- `claim_language_kyoto_yasashii.html` → https://www.city.kyoto.lg.jp/sogo/page/0000250837.html → HTTP 200, 28152 bytes → 京都市 生活ガイドブック（やさしい日本語版）総合目次 (page 250837, 2019-04-26): the city's own definition of 「やさしい日本語」 and the audience it is written for; footer names 京都市 総合企画局市長公室広報担当 — language claim source
- `claim_alcohol_nta_limited_retail.html` → https://www.nta.go.jp/taxes/sake/menkyo/tebiki/kourigyou2016/index.htm → HTTP 200, 16239 bytes (Shift_JIS) → 国税庁 期限付酒類小売業免許について: the 博覧会場等 temporary-sales-point licence rule, the two-week / ten-day timing, the 所轄税務署 filing desk and the eleven 届出 requirements — alcohol claim source
- `claim_alcohol_nta_qa03.html` → https://www.nta.go.jp/taxes/sake/qa/03b/03.htm → HTTP 200, 9246 bytes (Shift_JIS) → 国税庁 お酒に関するQ&A【販売業免許関係】Q3: the 酒場・料理店 own-premises exemption and the away-from-premises licensing rule — quoted so the alcohol value cannot overreach Q3
- `claim_alcohol_osaka_kokuzeicho_soudan.html` → https://www.nta.go.jp/about/organization/osaka/sake/info/info.htm → HTTP 200, 12765 bytes (Shift_JIS) → 大阪国税局 酒税とお酒の免許に関するご質問やご相談等について, 表1/表2 — read 2026-11-28 and retained as reading evidence only, **not cited in the alcohol claim**: 表2 prints tax-office names and 酒類指導官部門 desks with no 管轄区域 table, so it establishes no per-venue or ward routing
- `claim_food_kyoto_kyoka.html` → https://www.city.kyoto.lg.jp/hokenfukushi/page/0000082748.html → HTTP 200, 43062 bytes → 京都市 営業許可申請方法 (page 82748, updated 2026-07-07): 食品衛生法 営業許可 for a 飲食店, the 事前相談→申請→審査→許可 flow and 医療衛生センター as the counter — food claim source
- `school_kyoto_kanri_kisoku.html` → http://www.edu.city.kyoto.jp/hp/chosa/reiki_honbun/x898RG00000134.html → HTTP 200, 141949 bytes → 京都市立小学校、中学校、小中学校及び幼稚園の管理運営に関する規則（昭和62年12月25日 教育委規則第5号）第3条 休業日 table: the fixed 学年始・学年末 breaks and the 幼稚園 夏季・冬季 breaks; 小学校・中学校 夏季・冬季 are 校長が定める日 inside a printed window. Fetched over `http://` because the `https://` endpoint fails certificate validation on this host (incomplete chain); the bytes are the same page.
- `school_kyoto_reiwa8_schedule.html` → https://www.city.kyoto.lg.jp/kyoiku/page/0000236396.html → HTTP 200, 32437 bytes → 京都市教育委員会 京都市立幼稚園、小学校、中学校、小中学校の学期及び長期休業期間（令和8年度） (page 236396, 2026-04-03): evidence that the Board publishes the term and long-break dates one school year at a time; no 令和9年度 (2027/28) page existed at 2026-11-28
- `krp_room2_detail.html` → https://www.krp.co.jp/kaigi/room/detail/room2.html → HTTP 200, 67326 bytes → 京都リサーチパーク ルーム2 room page (the `/kaigi/room/room2.html` URL recorded as 404 in the research bundle was the wrong path): six room photographs
- `heartpia_convention.html` → https://heartpia-kyoto.jp/convention/ → HTTP 403, 1509 bytes → attempted ハートピア京都 convention index for a room gallery; blocked, so both ハートピア rooms carry a withheld photo record

## Not captured

- www.hnkansai.org — connection timed out after 45 s with zero bytes on 2026-11-28; Hacker News Kansai is therefore not recorded (see `source_uncertainty_notes.md`).
- meetup.com/hacker-news-kansai — not attempted after the HNKansai site failure; the group's Meetup URL from the August 2026 run was not re-checked.
- IVS 2027 — no organiser page exists yet; `ivs_home.html` is the capture that proves the 2027 edition is unannounced.
