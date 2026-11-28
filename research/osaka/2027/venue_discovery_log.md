# Venue and calendar discovery log — Osaka 2027 (accessed 2026-11-28)

Platform first pass, run before web search:

- `python3 ~/.hermes/skills/plan-event/scripts/venue_platform_instructions.py --registry ~/.hermes/skills/plan-event/references/venue_platforms.json --cities ~/.hermes/skills/plan-event/references/cities.json --city osaka-jp` → **"No active platform coverage in registry; standard web discovery used."** (exit 0). No platform listing was therefore cited as venue evidence; Spacemarket and Instabase results that surfaced in search were used only as discovery clues and no record rests on them.

Search and fetch queries, in order (English where noted, otherwise Japanese). Every query was run through the web_search tool and every cited page was then fetched and saved.

1. 大阪 梅田 貸会議室 50名 イベントスペース
2. 大阪 イベントスペース 貸し出し 50人 土日
3. 大阪産業創造館 イベントホール 貸出 料金
4. 大阪市中央公会堂 集会室 使用料 貸出
5. マイドームおおさか 会議室 貸出 料金
6. 大阪国際会議場 会議室 利用料金 貸出
7. 大阪市立総合生涯学習センター 貸室 使用料 梅田
8. エル・おおさか 会議室 使用料 貸出
9. 大阪カンファレンスセンター 大会議室 料金 本町
10. 梅田スカイビル 貸会議室 料金 イベントホール
11. ナレッジキャピタル カンファレンスルーム 料金 グランフロント
12. 新大阪 貸会議室 50人 料金 イベントスペース
13. 弁天町 港区民センター ホール 使用料 貸室
14. 吹田市文化会館 メイシアター 大会議室 使用料
15. 大阪イノベーションハブ イベントスペース 貸出 グランフロント
16. 大阪 スタートアップ イベントスペース 貸出 コワーキング 梅田 本町
17. 大阪市 中央会館 ホール 使用料 定員 250名 難波
18. TKP新大阪カンファレンスセンター 会議室 料金 収容
19. Japan IT Week 関西 2027 インテックス大阪 11月
20. Tech Osaka Summit 2027
21. インテックス大阪 2027年 展示会 スケジュール
22. 大阪マラソン 2027 開催日
23. 大阪 AI カンファレンス 2027
24. AI・人工知能EXPO 関西 2027 インテックス大阪 開催
25. 関西 ブロックチェーン Web3 イベント 2027 大阪

District sweep and what it produced:

- **Umeda / Kita** — 梅田スカイビル (fee tables rendered client-side; not captured as a record), ナレッジキャピタル カンファレンスルーム (prices without a room map; not a record), 大阪駅前第2ビル 総合生涯学習センター **recorded**. グランフロント大阪 also hosts Tech Osaka Summit and OIH (see gaps).
- **Nakanoshima** — 大阪市中央公会堂 中集会室 and 小集会室 **recorded**; グランキューブ大阪 (大阪国際会議場) fee page fetched but its room tables sit in sub-pages/PDFs, not a record.
- **Honmachi / Sakaisuji-Honmachi / 本町橋** — マイドームおおさか 第1・第2 and 第3 **recorded**; 大阪産業創造館 会議室E and 4F ホール **recorded**; 大阪商工会議所 2号会議室 **recorded**.
- **Shinsaibashi / Namba / 島之内** — 難波市民学習センター 講堂 **recorded**; 大阪市立中央会館 ホール **recorded**.
- **Tennoji / Abeno / 上本町** — 阿倍野市民学習センター 講堂 **recorded**; 大阪カンファレンスセンター 中会議室 銀杏 **recorded** (null cost).
- **Bentencho (港区)** — 港区民センター ホール and 第1集会室 **recorded**.
- **Shin-Osaka** — swept: 新大阪ブリックビル, Brain会議室, ラミ新大阪 L-site, アットビジネスセンターPREMIUM新大阪, TKP新大阪カンファレンスセンター all surfaced, but each readable quote came from an operator/marketplace listing page (日本会議室, Spacemarket, kashikaigishitsu) rather than a venue-owned page, and the room sizes clustered at 12-70 seats. **No Shin-Osaka record was written**; the district is logged as a gap rather than padded with a platform listing.
- **Suita / Expo City** — 吹田市文化会館メイシアター fee table fetched (小ホール 平日全日 32,000 / 土日祝 42,000), but its hall-capacity pages 404'd and no official capacity number was captured, so **no record**; 万博記念公園 / EXPOCITY produced no readable rental page.
- **Sakaisuji** — covered through 大阪産業創造館 and マイドーム (both on the Sakaisuji line); no separate venue written.

Calendar discovery: Japan IT Week 関西 (organiser hub page captured), 大阪マラソン and 大阪マラソンEXPO (official 大会要項 captured), AI-ESS-16 (organiser page captured). Attempted and blocked: innovation-osaka.jp (Tech Osaka Summit and OIH — connection timeout), intex-osaka.com (price page — timeout), ospn.jp/osc2027-osaka (404; the オープンソースカンファレンス2027 Osaka listing appeared only on an aggregator). Those are recorded as gaps in `source_uncertainty_notes.md`, not as calendar rows.
