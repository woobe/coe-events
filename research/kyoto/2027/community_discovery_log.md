# Community discovery log — Kyoto/Kansai, 2026-11-28

Method: Japanese and English web search for Kyoto/Kansai technology and startup groups, then a direct fetch of each group's own page. A group is only recorded when its own page could be captured; directory and aggregator pages (connpass search, meetup.com/find, Doorkeeper event indexes, blog round-ups) were used for discovery only and never as a record's source.

## Queries run (35 bundle-wide; 31 enumerated in this log)

Count, bundle-wide: 4 community-specific + 14 venue/district + 13 calendar + 4 venue follow-up = **35** distinct searches.
Count, this log's own list: 1-4 community-specific + 5-18 venue/district + 19-31 calendar = **31**.
The four extra are the follow-up searches logged in `venue_discovery_log.md` items 15-18 (aggregator follow-ups); that log's own header counts 18 = its 14 core searches (identical to items 5-18 here) + those 4 follow-ups. Nothing in either list is uncounted.

Community-specific queries:
1. 京都 AI 勉強会 コミュニティ connpass 2026
2. 関西 Python 勉強会 京都 コミュニティ 2026
3. 京都 スタートアップ コミュニティ 勉強会 2026 イベント
4. doorkeeper 京都 勉強会 グループ 2026 開催

Venue and district queries that surfaced community or venue leads:
5. 京都 イベントスペース 貸し出し 50人 セミナー 会場
6. 京都市 会議室 レンタル 土日 9時 21時 料金
7. 京都 スタートアップ イベントスペース 貸し切り 四条
8. 京都駅 イベントスペース 貸し切り 100人 セミナー 料金
9. 京都 河原町 貸会議室 ホール 50名 料金 9:00-21:00
10. 京都 岡崎 みやこめっせ 会議室 貸出 料金
11. 京都 伏見区 貸会議室 レンタルスペース イベント
12. 京都 左京区 一乗寺 レンタルスペース イベント 貸し出し
13. Kyoto event space rental 50 people conference room English
14. 京都市上京区 貸会議室 レンタルスペース イベント 50人
15. 京都市右京区 貸会議室 ホール レンタル イベント 料金
16. 京都アスニー 生涯学習総合センター 貸室 使用料 大会議室 定員
17. 京都府立京都学・歴彩館 貸室 使用料 ホール 定員 9時 21時
18. 京都大学 百周年時計台記念館 国際交流ホール 定員 100名 施設

Calendar queries: 19-31, thirteen topics (IVS 2027, KYOTOGRAPHIE 2027, BitSummit 2027, Japan IT Week 関西 2027, 祇園祭 2027, 五山送り火 2027, 京都マラソン 2027, World Masters Games 2027, 葵祭 2027, 時代祭 2027, RubyKaigi 2027, 関西 Web3 AI カンファレンス 2027, Hack Osaka 2027 — see `evidence_summary.md` §5).

District coverage: Karasuma/Shijo (3, 7, 9), Kawaramachi (9), Gion (9 result set), Okazaki (10), Kyoto Station (8), Fushimi (11), Ichijoji/Sakyo (12), Kamigyo (14), Ukyo (15).

## Retained (in `communities.raw.json`) — 13 records

Active (dated in-person activity inside the 12 months before 2026-11-28):
1. KOIN (Kyoto Open Innovation Network) — `open.kyoto/event/` — dated 2026-12-02, 2026-12-11, 2027-01-15 events; 京都経済センター 3F.
2. Kyoto eggs — `kyoto-eggs.jp` — 定例会 2026-11-14, 例会 2026-10-10, anniversary 2026-09-12.
3. KC3 (関西情報系学生団体交流会) — `kc3.me/conf/conf2026/` — conference 2026-09-23 at 京都リサーチパーク.
4. データサイエンススクール京都 (Kyoto University CIREDS) — `cireds.doorkeeper.jp` — 2,029 members; sessions 2026-09-19 and 2026-09-01; 2027-01-15/01-30 already listed.
5. 関西デジタルコンテンツ事業協同組合 — AI勉強会「スナックAI」 — `kandigi.doorkeeper.jp` — 2026-12-14 (Kobe), 2026-12-17.
6. 大阪イノベーションハブ (OIH) — `innovation-osaka.jp` — news 2026.11.26, event 2026-11-28.

Intermittent (a live page, but no datable 2026 in-person event):
7. GDG 京都 — `kyoto-gtug.org` — states an intention of about one in-person event a month; announcements pushed to external sites; no dated 2026 event on the page.
8. 京都大学ブロックチェーン研究センター (BCK) — `blockchainkyoto.org` — BCK21-BCK26 series in navigation, no dated 2026 event in the captured HTML.
9. 鹿島・竹内研究室 (Kyoto University) — research laboratory, no public event calendar.
10. 京都大学 学習機械分野 — research laboratory, no public event calendar.
11. Kyoto Next CxO Community — `city.kyoto.lg.jp` — 145 + 80 members as of 2026-11-27, "several online study sessions a month", no individual event date, programme term ends 2027-03-31.
12. みやこでIT (MIT) — `mit.connpass.com` — page returned HTTP 202 with a 2,019-byte bot challenge; no content readable, so no claim is made beyond the URL.

Dormant:
13. PyData Osaka — `meetup.com/pydata-osaka` — the Meetup URL recorded by the August 2026 run now returns Meetup's "Group not found" page.

## Reviewed and not carried

- **Hacker News Kansai (hnkansai.org)** — connection timed out twice (45 s, zero bytes). No capture, so the group is not recorded; the prior run's Meetup URL (`meetup.com/hacker-news-kansai`) was not re-checked.
- **Kyoto AI Meetup (LINEヤフー × Sansan)** — connpass event pages for the 2026-02-27 first edition exist, but no standing group page with its own activity record; left out rather than built from an event page.
- **AI勉強会 in 京都 (rist.connpass.com)** — single event page (last dated 2026-11-08), no group-level activity record; not carried.
- **ITコーディネータ京都 Web/SNSマーケティング研究会** — 267 members and a 2026-11-01 event, but the focus is web/SNS marketing rather than AI/Web3; not carried.
- **EO Kyoto** — entrepreneurs' organisation with a 2026-11-25 meeting; membership by invitation and no public community page for outreach; not carried.
- **Kyoto University NLP laboratory (nlp.ist.i.kyoto-u.ac.jp)** — host did not resolve on 2026-11-28; no capture.
- **Code for Kyoto / civic-tech groups** — no own-page capture obtained in this pass; not carried.
- Aggregators used for discovery only: instabase.jp, spacemarket.com, kashispace.com, kaigishitu.com, ekiten.jp, meet-it.net, miyakodeit.com blog, kc3 aggregator listings, 10times, showsbee, tradefairdates.

## Counts

- 13 records retained: 6 active, 6 intermittent, 1 dormant.
- 0 co-host claims: no group's own page carries explicit co-host solicitation language that could be quoted, so `cohost_open` is false on every record and no badge is asserted.
- Public contact route recorded for every record (an HTTPS page, never an email address or phone number).
