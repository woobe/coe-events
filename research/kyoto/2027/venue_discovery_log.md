# Venue discovery log — Kyoto 2027 deep refresh, 2026-11-28

Method: 18 English and Japanese searches, then a direct fetch of each surviving venue's own pages (fee page, room page, access page). That 18 is 14 core searches (items 1-14, identical to items 5-18 of `community_discovery_log.md`) plus 4 follow-up searches (items 15-18); the four follow-ups are the only searches outside that log's 31-item list, so the bundle-wide distinct total is 35 (see `community_discovery_log.md` header). Aggregators were discovery-only: instabase.jp, spacemarket.com, kashisikaigishitsu.net, kaigishitsu.com, ekiten.jp, gourmetplus.jp, kaigi-select.com, cangii.jp, shopcounter.jp, rentaloffice.jp. A venue is only recorded when its own page could be captured today.

## Queries (18)

1. 京都 イベントスペース 貸し出し 50人 セミナー 会場
2. 京都市 会議室 レンタル 土日 9時 21時 料金
3. 京都 スタートアップ イベントスペース 貸し切り 四条
4. 京都駅 イベントスペース 貸し切り 100人 セミナー 料金
5. 京都 河原町 貸会議室 ホール 50名 料金 9:00-21:00
6. 京都 岡崎 みやこめっせ 会議室 貸出 料金
7. 京都 伏見区 貸会議室 レンタルスペース イベント
8. 京都 左京区 一乗寺 レンタルスペース イベント 貸し出し
9. Kyoto event space rental 50 people conference room English
10. 京都市上京区 貸会議室 レンタルスペース イベント 50人
11. 京都市右京区 貸会議室 ホール レンタル イベント 料金
12. 京都アスニー 生涯学習総合センター 貸室 使用料 大会議室 定員
13. 京都府立京都学・歴彩館 貸室 使用料 ホール 定員 9時 21時
14. 京都大学 百周年時計台記念館 国際交流ホール 定員 100名 施設
15. 京都 イベントスペース 貸し切り 100人 (aggregator follow-up)
16. 京都 会議室 レンタル 50人 土日 (aggregator follow-up)
17. Kyoto conference room rental 50 persons (English follow-up)
18. 京都 四条 イベントスペース 貸切 ホール (district follow-up)

## District sweep

Karasuma/Shijo (3, 5, 18) · Kawaramachi (5) · Gion (5 results: 祇園四条 listings — aggregator only) · Okazaki (6 → Miyako Messe) · Kyoto Station (4) · Fushimi (7 — aggregator space listings only) · Ichijoji/Sakyo (8 — small studio/room listings only) · Kamigyo (10 → Impact Hub Kyoto block, aggregator listings) · Ukyo (11 → 右京区役所 free 30-person meeting rooms, below brief).

## Retained — 18 records in `venues.raw.json`

| # | Venue | Capacity | 09-17 JPY | USD | Tier |
| --- | --- | --- | --- | --- | --- |
| 1 | kokoka Event Hall | 130 | 74,500 | 466.96 | shortlist_ready |
| 2 | kokoka Special Conference Room | 80 | 69,800 | 437.50 | shortlist_ready |
| 3 | kokoka Conference Rooms 1+2 | 68 | 27,600 | 173.00 | shortlist_ready |
| 4 | kokoka Seminar Room | 50 | 27,100 | 169.86 | shortlist_ready |
| 5 | ハートピア京都 第5会議室 | 54 | 22,390 | 140.34 | shortlist_ready |
| 6 | ハートピア京都 大会議室 | 120 | 49,500 | 310.26 | shortlist_ready |
| 7 | みやこめっせ 大会議室 | 120 | 31,570 | 197.88 | shortlist_ready |
| 8 | 京都アスニー 第2研修室 | 104 | 25,130 | 157.51 | shortlist_ready |
| 9 | 京都アスニー 第3研修室 | 72 | 18,220 | 114.20 | shortlist_ready |
| 10 | ホテルエルシエント京都八条口 B | 72 | 150,000 (7 h + 1 h) | 940.19 | shortlist_ready |
| 11 | ハートンホテル京都 嵐山 | 72 | 84,000 | 526.51 | shortlist_ready |
| 12 | ハートンホテル京都 宇治伏見 | 100 | 134,000 | 839.91 | shortlist_ready |
| 13 | KRP 西地区4号館 ルーム2 | 96 | 128,700 | 806.68 | shortlist_ready |
| 14 | 京都大学 国際交流ホール I | 100 | 85,600 (hourly × 8) | 536.54 | lead |
| 15 | 京都府立京都学・歴彩館 小ホール | 100 | 32,200 (Sat, closes 17:00) | 201.83 | lead |
| 16 | Impact Hub Kyoto 2F 会所 | 70 (archive) | unpublished today | null | lead |
| 17 | THE TERMINAL KYOTO | unknown | unpublished | null | lead |
| 18 | FabCafe Kyoto 2F 和室 | unknown (14 tatami) | 44,000 rate estimate | 275.79 | lead |

(The scorer's own output is the authority; the table mirrors `venues.shortlist.json`.)

## Reviewed and excluded (with reason)

- **京都テルサ 中会議室 (96)** — official 2026-04-01 price PDF gives 48,840 (午前・午後) and 68,860 (全日 09:00-21:30), but the PDF prints 平日 and 土日祝 blocks that text extraction cannot attribute to a specific row with confidence; excluded rather than risk a wrong weekend rate.
- **キャンパスプラザ京都 ホール (80) / 第1会議室 (63)** — capacities readable in the PDF (184 m2 / 80 seats) but the fee rows cannot be mapped to rooms by text extraction; excluded.
- **京都経済センター** — 25 rental rooms, largest about 30 people (3-D); below the 50-person brief.
- **リーガロイヤルホテル京都 会議室** — publishes per-person banquet pricing (4 hours ¥425,040 for 60 guests) and small-room rates (10 guests ¥121,440), with no plain 50-person room rate; excluded.
- **イベントホール洛央 (333 m2 hall, 19,800-23,100円/h)** — surfaced only through the kaigishitsu.com aggregator; no official page captured, so not carried.
- **右京区役所 会議室** — free, but the largest room seats 30; below brief.
- **みやこめっせ 展示場 / サイエンスホール** — exhibition-scale or 150-230 seat halls; the 大会議室 is the right size and is the retained Miyako Messe record.
- **KRP A/B/C会議室 (42 school)** — below the 50-person brief; the retained KRP room is ルーム2 (96 school).
- **京都アスニー 第4研修室 (56), 第1実習室 (54), 第1/2サークル活動室 (60)** — real options, not carried to stay inside the 18-record cap; the two larger Asny rooms are recorded.
- **ハートピア 視聴覚室 (35), 第1-4会議室 (<35)** — below brief.

## Open items carried to the reviewer

1. Impact Hub Kyoto's live fee page did not respond on 2026-11-28 (HTTP 000 on four attempts); the record rests on a 2025-02-17 archive capture and is a `lead`, not a shortlist row.
2. KRP ルーム2 room-detail URL returned 404, so AV for that room is unconfirmed.
3. Three venue families publish no consumption-tax statement (kokoka, Heartpia, Rekisaikan); each carries a final-quote question. Miyako Messe, KRP, Hearton and Elcient state rates as tax-inclusive.
4. Alcohol: only 京都アスニー publishes a rule (alcoholic drinks prohibited). Every other venue carries the licence question rather than an assumption.
