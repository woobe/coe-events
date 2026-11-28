# Capture index — Osaka 2027 deep research run (accessed 2026-11-28)

Every page cited in `venues.raw.json`, `calendar_conflicts.json` and `communities.raw.json` is saved here, plus the FX source, the Nominatim responses that carry each coordinate, and the context captures used for discovery. Fetches used `curl` (browser user agent, Japanese `Accept-Language`, 45-90 s timeouts) and, for connpass group pages that answer HTTP 202 with a bot challenge, headless Chromium `--dump-dom` (`~/.cache/ms-playwright/chromium-1234`). Files under `blocked/` are the pages that refused or timed out; they are listed at the end and are not evidence for any record.

## FX basis

- `ecb_eurofxref_daily_2026-11-28.xml` → https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml → HTTP 200, 1,547 bytes → ECB euro foreign exchange reference rates, reference date 2026-11-27 (EUR/USD 1.0957, EUR/JPY 174.81) — the basis for every USD figure in this package.

## Venue records — 16 records in `venues.raw.json`

**マイドームおおさか 第1・第2会議室 and 第3会議室**
- `mydome_price_conference.html` → https://www.mydome.jp/organizer/price/conference → the fee page with the earlier table and the "（2027年4月1日以降）" table: 第1・第2会議室 205 m² 終日 125,620 JPY and 第3会議室 143 m² 終日 88,880 JPY on the new table (100,540 / 71,170 on the old one), all 税込 — the cited source for both records' cost and window.
- `mydome_conference_index.html` → https://www.mydome.jp/organizer/conference → room index: 第1・第2会議室 205 m² 最大210名, 第3会議室 143 m² 最大144名.
- `mydome_room_0102.html` → https://www.mydome.jp/organizer/conference/01-02room → 第1・第2会議室 layouts (school 100, theatre 160/210) and the noodle cafe Q catering note.
- `mydome_room_03.html` → https://www.mydome.jp/organizer/conference/03room/ → 第3会議室 room page.
- `mydome_room_06.html` → https://www.mydome.jp/organizer/conference/06room/ → 第6会議室 room page (context for the room family).
- `mydome_facility_wifi.html` → https://www.mydome.jp/organizer/facility/network/ → free wireless LAN (Wi-Fi) service statement — the source for `wifi_status: confirmed`.
- `mydome_access.html` → https://www.mydome.jp/organizer/access/ → 堺筋本町 12番出口 徒歩約6分, 本町橋2番5号.
- `mydome_home.html` → https://www.mydome.jp/ → facility home (context).

**大阪市中央公会堂 中集会室 and 小集会室**
- `chuokokaido_pricing.html` → https://osaka-chuokokaido.com/ja/facility-pricing → 施設利用料 table (weekday base: 中集会室 全日 98,400; 小集会室 全日 50,200; 土日祝 2割増 note) — the cited source for both records.
- `chuokokaido_middle_room.html` → https://osaka-chuokokaido.com/ja/facilities/middle-meeting-room → 中集会室 定員500, school ~300, 926.5 m², audio/lighting, ケータリングを入れてのパーティー.
- `chuokokaido_small_room.html` → https://osaka-chuokokaido.com/ja/facilities/small-meeting-room → 小集会室 定員150, school ~90, 162.1 m², equipment, sound-insulation warning, Saturday multiplier.
- `chuokokaido_home.html` → https://osaka-chuokokaido.jp/ → hall home (address 中之島1-1-27).
- `chuokokaido_access.html` → https://osaka-chuokokaido.com/ja/access → access page (context).

**エル・おおさか 9012 and 708**
- `losaka_meeting_rooms.html` → https://www.l-osaka.or.jp/meetingroom/ → the room table with 定員/面積/午前〜全日 rates: 9012 (60名, 120 m², 全日 40,000), 708 (117名, 171 m², 全日 57,200), 大会議室 (200名, 61,400) — the cited source for both records.
- `losaka_large_room.html` → https://www.l-osaka.or.jp/meetingroom/6large.html → 大会議室 detail page (context).
- `losaka_access.html` → https://www.l-osaka.or.jp/access/ → access page (map only; no street address printed).

**大阪市立総合生涯学習センター 第1研修室**
- `manabu_umeda.html` → https://osakademanabu.com/venues/umeda → hours 9:30-21:30 (Sat), the room table (第1研修室 183 m², 112/87, weekday 43,200, Sat 51,840), and the 営利活動 restriction — the cited source.
- `manabu_access_umeda.html` → https://osakademanabu.com/access/umeda → centre access page.
- `manabu_access.html` → https://osakademanabu.com/access → the three centres' postal addresses (梅田1-2-2-500, 阿倍野筋3-10-1-300, 湊町1-4-1).

**難波市民学習センター 講堂**
- `manabu_namba.html` → https://osakademanabu.com/venues/namba → room table (講堂 200 m², 120名, Sat 全日 51,840) and the same use restriction — the cited source.

**阿倍野市民学習センター 講堂**
- `manabu_abeno.html` → https://osakademanabu.com/venues/abeno → room table (講堂 150 chairs / 120 desks, 土日祝 全日 46,680) — the cited source.

**大阪産業創造館 会議室E and 4F イベントホール**
- `sansokan_price_list.html` → https://shisetsu.sansokan.jp/rent/shi_list.html → the full room fee table incl. 会議室E (114名, 177 m², 終日 25,900 / weekend 31,100) and the 5割増 and Sunday-evening notes — cited for 会議室E.
- `sansokan_rent_e.html` → https://shisetsu.sansokan.jp/rent/rent_e.html → 4F イベントホール page: 279 m², 200-inch projector, 定員 320/180/160/260, 終日 58,900 (70,700) — cited for the hall.
- `sansokan_access.html` → https://shisetsu.sansokan.jp/access/ → 堺筋本町駅より徒歩約5分, 土日も利用可能.
- `obda_sansokan.html` → https://www.obda.or.jp/jigyo/shisetsu-sansokan.html → operator (大阪産業局) facility page (context).
- `city_osaka_sansokan.html` → https://www.city.osaka.lg.jp/keizaisenryaku/page/0000651997.html → Osaka City page on 大阪産業創造館 (context).

**大阪カンファレンスセンター 中会議室 銀杏**
- `ihosaka_icho_room.html` → https://www.ih-osaka.jp/facilities/icyo.html → 中会議室 銀杏: 90名, 188.38 m², 100 school seats, roll screen + video projector + interpretation equipment, 開館 9:00-21:00, address 上本町8-2-6 — the cited source.
- `ihosaka_fee_page.html` → https://www.ih-osaka.jp/guidance/index.html?id=fee → fee landing page that links the fee table only as a PDF — the basis for the null cost.
- `ihosaka_fee_pdf.pdf` → https://www.ih-osaka.jp/pdf/shisetsu_fee.pdf → the fee PDF (binary, 201,525 bytes) that could not be text-extracted in this environment.
- `ihosaka_croom.html` / `ihosaka_main.html` / `ihosaka_access.html` → https://www.ih-osaka.jp/facilities/c-room.html, /facilities/main.html, /access/index.html → facility context.

**港区民センター ホール and 第1集会室**
- `minato_fee.html` → https://www.osakacommunity.jp/minato-center/guide/fee/ → holiday fee tables: ホール 全日 50,520, 第1集会室 全日 10,680, 2割増 note — cited for both records.
- `minato_floor.html` → https://www.osakacommunity.jp/minato-center/floor/ → ホール 定員400 644 m², 第1集会室 定員114 161 m², projector/microphone at extra charge — cited for capacity and AV.
- `minato_facility.html` → https://www.osakacommunity.jp/minato-center/facility/ → access (弁天町駅3号出口 徒歩1分) and building context.

**大阪市立中央会館 ホール**
- `chuo_floor.html` → https://www.osakacommunity.jp/chuo-kaikan/floor/ → ホール 定員250, 230.4 m², library-above noise restriction — cited for capacity.
- `chuo_fee.html` → https://www.osakacommunity.jp/chuo-kaikan/guide/fee/ → ホール holiday 全日 41,880, 2割増 note, projector 550 / screen 350 / PA 1,650 — cited for cost and AV.

**大阪商工会議所 B1F 2号会議室**
- `osaka_cci_price.html` → https://www.osaka.cci.or.jp/kaijou/price/ → per-hour rate table: 2号会議室 144.42 m², 50 机椅子 / 90 椅子, general holiday 19,800 JPY/h, 8:00-18:00 band, AV separate — the cited source.

## Geocoder responses — one saved Nominatim body per address (11 bodies for 16 records)

- `geo_mydome.json` → https://nominatim.openstreetmap.org/search?q=マイドームおおさか → 34.6848530, 135.5111489; display name 'マイドームおおさか, 豊後町通, 本町橋, 中央区, 大阪市, 大阪府, 540-0029'
- `geo_chuokokaido.json` → q=大阪市中央公会堂 → 34.6935404, 135.5040087; '大阪市中央公会堂, 27, 中之島一丁目, 北区'
- `geo_losaka.json` → q=エル・おおさか → 34.6897201, 135.5130479; 'エル・おおさか, 骨屋町筋, 石町二丁目, 中央区'
- `geo_manabu_umeda2.json` → q=大阪駅前第2ビル → 34.6988267, 135.4979466; '大阪駅前第2ビル, 樋之筋, 梅田一丁目, 北区' (the centre occupies 5-6F)
- `geo_namba2.json` → q=OCAT 大阪 → 34.6663886, 135.4951081; 'OCAT, 1, 湊町一丁目, 浪速区' (難波市民学習センター is on 4F)
- `geo_abeno.json` → q=阿倍野市民学習センター → 34.6418118, 135.5112421; '阿倍野市民学習センター, あべの筋, 阿倍野筋三丁目, 阿倍野区'
- `geo_sansokan.json` → q=大阪産業創造館 → 34.6840476, 135.5092015; '大阪産業創造館, 5, 本町一丁目, 中央区, 541-0053'
- `geo_ihosaka.json` → q=大阪国際交流センター → 34.6618180, 135.5176313; '大阪国際交流センター, 上町筋, 上本町八丁目, 天王寺区'
- `geo_minato.json` → q=港区土地区画整理記念・交流会館 → 34.6677602, 135.4617324; '港区土地区画整理記念・交流会館, 中央大通, 磯路一丁目, 港区'
- `geo_chuo.json` → q=大阪市立中央会館 → 34.6717235, 135.5079641; '市立中央会館, 周防町筋, 島之内二丁目, 中央区'
- `geo_cci.json` → q=大阪商工会議所 → 34.6843729, 135.5112811; '大阪商工会議所, 松屋町筋, 本町橋, 中央区, 540-0026'

Failed or superseded geocoder bodies kept for the audit trail (they are **not** used by any record): `geo_manabu_umeda.json` (empty — centre name alone resolves nothing), `geo_namba.json` (returned 阿倍野市民学習センター, the wrong centre), `geo_minato2.json` (returned a different 港区民センター), `geo_minato3.json` (弁天町駅, a station not a building), `geo_abeno2.json` (あべのベルタ building, superseded by the centre point), `geo_losaka2.json` (duplicate of geo_losaka.json).

## Calendar records — 4 rows in `calendar_conflicts.json`

- `japanit_hub.html` → https://www.japan-it.jp/hub/ja-jp.html → the organiser schedule block printing 【関西展 (11月)】2027/11/17(水)～19(金) at インテックス大阪 alongside the 2027/4/7-9, 7/21-23 and 9/8-10 editions — cited for the Japan IT Week 関西 row.
- `osaka_marathon_gist.html` → https://www.osaka-marathon.com/2027/info/gist/ → 大会要項: 2027年2月28日（日）, 9:15開始/16:15終了, 大阪府庁前→大阪城公園 course via 御堂筋・道頓堀, and the 大阪マラソンEXPO2027 展示エリア at インテックス大阪 6号館 on 2月26-27日 — cited for both marathon rows.
- `aiess16.html` → https://www.aaseconference.org/2027-events/ai-ess-16-september-13-17-2027-osaka-japan → AI-ESS-16, September 13–17 2027, Osaka, Japan, with submission and registration deadlines — cited for the AI-ESS-16 row.

## Community records — 13 records in `communities.raw.json`

- `comm_deeplearning_osaka.html` → https://deep-learning-osaka.connpass.com/ (Chromium DOM) → group description, 91 events, KANSAI AI PUB 2026-12-09, 538 members.
- `comm_osaka_driven_dev.html` → https://osaka-driven-dev.connpass.com/ (Chromium DOM) → 436 events, XR/AI strands, latest 2026-12-09, 2,459 members.
- `comm_gdg_kwansai.html` → https://gdgkwansai.connpass.com/ (Chromium DOM) → 47 events, DevFest Kansai 2026 1409/1500, 3,456 members.
- `comm_gdgoc_osaka.html` → https://gdsc-osaka-univ.connpass.com/ (Chromium DOM) → 91 events, weekly もくもく会 + monthly event, 1,054 members.
- `comm_gdg_osaka.html` → https://gdg.community.dev/gdg-osaka → 107 members, 2026 hackathon series, contact form.
- `comm_oue_meetup.html` → https://oue-meetup.connpass.com/ (Chromium DOM) → Management & AI Commons Osaka, monthly LT/もくもく, 28 events, 211 members.
- `comm_quintbridge.html` → https://www.quintbridge.jp/ → 34,294 QB members (2026.9.30), 150-person main stage, Nov-Dec 2026 event calendar.
- `comm_quintbridge_qb.html` → https://www.quintbridge.jp/qbcommunity/ → QB-certified communities list incl. AI研究所@トキワバレー 関西HUB.
- `comm_pydata_osaka.html` → https://pydataosaka.connpass.com/ (Chromium DOM) → 73 events, 494 members, latest 2025-08-24.
- `comm_pydata_site.html` → https://osaka.pydata.org/ → PyData Osaka site with channel links.
- `comm_kansai_ai_driven.html` → https://kansai-ai-driven.connpass.com/ (Chromium DOM) → monthly cafe meetup, 3 events, latest 2025-10-07, 60 members.
- `comm_cdle_osaka.html` → https://cdle-osaka.connpass.com/ (Chromium DOM) → 22 events, latest 2024-07-12, 40 members.
- `comm_osaka_dtc.html` → https://osaka-dtc.connpass.com/ (Chromium DOM) → 174 events, latest 2020-02-14, 200 members.
- `comm_osaka_bch.html` → https://osaka-bch.connpass.com/ (Chromium DOM) → 1 event 2019-10-10, 5 members.
- `comm_miyakodeit.html` → https://miyakodeit.com/kansai-web3 → みやこでIT, 167 events and 651 members since 2019, Kyoto-based Kansai Web3 group.

## Context captures (discovery only; not cited as a record's evidence)

- `gco_home.html`, `gco_price.html` → https://www.gco.co.jp/, /price/ → グランキューブ大阪 (大阪国際会議場) price landing page; room fee tables are sub-pages/PDFs, no record built.
- `kcspace_home.html`, `kcspace_prices.html`, `kcspace_information.html`, `kcspace_plan.html`, `kcspace_access.html` → https://kc-space.jp/ ... → ナレッジキャピタル カンファレンスルーム; the price page prints amounts without a room map in the captured DOM, so no record built.
- `skybldg_charge.html`, `skybldg_rooms.html` → https://www.skybldg.co.jp/convention/... → 梅田スカイビル 貸会議室; the room and fee tables are rendered client-side and did not appear in the captured HTML, so no record built.
- `maytheater_pricelist.html`, `maytheater_access.html` → https://maytheater.jp/for-users/pricelist/, /access → 吹田市文化会館メイシアター fee tables (大/中/小ホール, weekday and 土日祝); the hall capacity pages 404'd, so no record built.
- `icaiic_home.html` → https://icaiic.org/ → ICAIIC 2027 (Osaka University venue); the page prints deadlines but no conference dates, so no calendar row.
- `comm_datamoku.html` → https://datamoku.connpass.com/ (Chromium DOM) → データもくもく; upcoming events are in Yokohama, so it is not an Osaka group and no record was built.

## Local-requirement claims (Asia C1 store build, accessed 2026-11-28)

- `claim_language_osaka_yasashii.html` → https://www.city.osaka.lg.jp/shimin/page/0000510655.html → 大阪市 市民局 「やさしい日本語」で話してみませんか？ (page dated 2026-10-14, page no. 510655): about 1 in 16 Osaka residents is a foreign national (over 170,000), and the page lists the five やさしい日本語 points — short sentences, simple words, no katakana loanwords, specific wording, no dialect — the **language** claim.
- `claim_food_osaka_kyoka.html` → https://www.city.osaka.lg.jp/kenko/page/0000537192.html → 大阪市：飲食店等の食品衛生法に基づく営業許可 (page dated 2026-11-02, page no. 537192): a 食品衛生法 licence is required to run a 飲食店 or prepare/process/sell food, applied for at the 生活衛生監視事務所 that covers the site, two to three weeks before opening, with the 食品衛生責任者 qualification document — the **food** claim.
- `claim_food_osaka_fee.html` → https://www.city.osaka.lg.jp/kenko/page/0000005787.html → 大阪市：食品衛生関係の申請手数料 (page dated 2026-04-07, page no. 5787): 飲食店営業 16,000円 new / 12,800円 renewal; read for the licence route, not quoted in the claim value.
- `claim_alcohol_nta_qa03.html` → https://www.nta.go.jp/taxes/sake/qa/03b/03.htm → 国税庁 お酒に関するQ&A【販売業免許関係】Q3 (Shift_JIS): a 酒場・料理店 serving alcohol for drinking 専ら自己の営業場 needs no 販売業免許, but selling alcohol for consumption off the premises needs a 酒類販売業免許 from the 所轄税務署長 under 酒税法第9条・第46条 — quoted in the **alcohol** claim for what Q3 actually covers.
- `claim_alcohol_nta_sake_menkyo.html` → https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/sake/annai/23600071.htm → 国税庁 E1-3 酒類の販売業免許の申請 (Shift_JIS): the ［提出時期］ paragraph (apply before trading; two weeks ahead for a 期限付 licence), the "no application fee, 登録免許税 applies" note and 添付書類 item 4, which directs anyone setting up a temporary 販売場 at an 博覧会場・即売会場 to the 期限付酒類小売業免許 — quoted in the **alcohol** claim for the temporary-sale route.

## Blocked / unreachable (no evidence taken)

- `blocked/failed_sansokan_home.html` → https://www.sansokan.jp/ → 403 Forbidden (WAF/geo block) — the main site was replaced by the shisetsu.sansokan.jp rental subdomain, which did serve.
- `blocked/failed_cci_access.html`, `blocked/failed_cci_room2.html` → https://www.osaka.cci.or.jp/kaijou/access/, /kaijou/facility/2/ → 404.
- `blocked/failed_comm_deeplearning_osaka.html`, `failed_comm_osaka_driven_dev.html`, `failed_comm_kansai_ai_driven.html`, `failed_comm_gdg_kwansai.html`, `failed_comm_gdgoc_osaka.html`, `failed_comm_pydata_osaka.html`, `failed_comm_osaka_dtc.html`, `failed_comm_cdle_osaka.html` → the same connpass URLs over plain `curl`; connpass answered HTTP 202 with a 2 KB bot challenge. Re-fetched via headless Chromium (the `comm_*.html` files).
- `blocked/failed_may_smallhall.html` → https://maytheater.jp/halls/small-hall/ → 404.
- `blocked/failed_osc2027_osaka.html`, `blocked/failed_osc2027_osaka2.html` → https://www.ospn.jp/osc2027-osaka/ and https://ospn.jp/osc2027-osaka/ → 404; the オープンソースカンファレンス2027 Osaka date (2027-01-30) was seen only in an aggregator listing, so it is not recorded.
- `blocked/failed_pref_osaka_losaka.html` → https://www.pref.osaka.lg.jp/o100080/l-osaka/index.html → 404.
- **Not captured at all (connection timeout, no HTTP response):** https://www.innovation-osaka.jp/ , https://innovation-osaka.jp/tech-osaka-summit/en , https://www.intex-osaka.com/jp/organizer/guide/price/ , https://www.osaka-startup.com/ (DNS failure).
