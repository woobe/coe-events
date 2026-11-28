# Community discovery log — Osaka 2027 (accessed 2026-11-28)

Discovery layer (never final evidence): connpass event pages and group listings, the GDG community directory, PyData Osaka's site, and the QUINTBRIDGE community pages. Every retained record was then read on the group's own page and saved under `captures/`. Connpass answers plain `curl` with HTTP 202 and a 2 KB bot challenge, so group pages were rendered with headless Chromium `--dump-dom` and saved as the `comm_*.html` captures.

Queries run (web_search):

1. connpass 大阪 AI 勉強会 コミュニティ
2. GDG Osaka 勉強会
3. PyData Osaka meetup
4. 大阪 Web3 勉強会 コミュニティ connpass
5. AI Tinkerers Osaka
6. 大阪 ブロックチェーン コミュニティ connpass Ethereum 関西
7. connpass 大阪 データサイエンス 機械学習 もくもく会 2026
8. QUINTBRIDGE 大阪 イベント コミュニティ

## Retained — 13 records

**Active (7)** — each carries an in-person event dated within 12 months of 2026-11-28:

- Deep Learning Osaka — 538 members, 91 events, KANSAI AI PUB on 2026-12-09 at 本庄東1-18-8.
- 大阪駆動開発 — 2,459 members, 436 events, four November 2026 events and one on 2026-12-09.
- GDG Greater Kwansai — 3,456 members, 47 events, DevFest Kansai 2026 on 2026-10-18 (1,409 of 1,500 seats).
- GDG on Campus Osaka — 1,054 members, 91 events, ハロウィン交流会 2026-10-28 and 週末開発会 #12 on 2026-10-17.
- GDG Osaka — 107 members, hackathon series 2026-10-24 / 2026-10-31 / 2026-11-14, results 2026-12-05.
- Management & AI Commons Osaka (OUE) — 211 members, 28 events, ゆるLT会 #12 on 2026-11-02.
- QUINTBRIDGE — 34,294 QB members (2026.9.30), event calendar with 第8回 関西インキュベーション機関 合同ピッチ会 on 2026-11-27.

**Intermittent (1)**:

- みやこでIT — 167 events and 651 members since 2019, Kyoto-based with Osaka partners (都市活力研究所, 大阪産業局); the page prints no dated 2026 event, so it is labelled intermittent with a question about the next date.

**Dormant (5)** — retained as historical/contextual leads only, never as a current audience:

- PyData Osaka — 494 members, 73 events, latest 2025-08-24 (about 15 months silent).
- 関西AI駆動開発コミュニティ&勉強会 — 60 members, 3 events, latest 2025-10-07 (about 13.7 months).
- CDLE大阪 — 40 members, 22 events, latest 2024-07-12.
- 大阪分散技術コミュニティ — 200 members, 174 events, latest 2020-02-14.
- Osaka BCH Meetup — 5 members, 1 event on 2019-10-10.

## Rejected or not retained, and why

- **AI Tinkerers Osaka** — searched; no Osaka chapter page was returned (the network's city index surfaced Tokyo and Mexico City only), so no record was written rather than inventing a chapter.
- **データもくもく (datamoku)** — active data-science もくもく会 with 113 events, but the upcoming events captured are in Yokohama (神奈川県横浜市), so it is not an Osaka group and was dropped (`comm_datamoku.html` kept as a context capture).
- **Ethereum Japan, JEDAI, AI駆動開発 大阪支部** — national or Tokyo-run bodies whose captured pages describe nationwide programmes; JEDAI's Osaka editions (2026-04-17 and 2026-09-18) are real but the group is a Japan-wide user group, so it is a promotion channel rather than an Osaka group. No record.
- **Osaka Innovation Hub** — the organiser host (innovation-osaka.jp) timed out on every attempt from this worker, so no OIH community record could be evidenced.
- **Osaka Startup ecosystem portal (osaka-startup.com)** — DNS resolution failed; no record.

## Co-host flag

Only **QUINTBRIDGE** is marked `cohost_open: true`, on its own how-to page language: 「会員のみなさんから持ち込んでいただいたイベント企画に対するアドバイスや、運営の支援を行っています」 together with 「イベントの主催、QBと共催」. Every other record is `cohost_open: false` because no own-page sponsorship or co-host language was captured — absence of evidence, not a negative finding.
