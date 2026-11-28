# Evidence summary — Tokyo (tokyo-jp), 2027 research run

Research date: **2026-11-28**. Phase: Run A (venue / calendar / communities). No store build, no page render, no publication, no date selection.

## What this run actually produced

- **16 venue candidates** in `venues.raw.json`, all validator-clean, all with numeric coordinates from a recorded address lookup.
- Scorer tiers: **0 eligible / 14 shortlist_ready / 2 lead**. The card's floor of at least 5 shortlist_ready is met with room to spare; the low eligible count is explained below and is a property of Tokyo's published information, not of a shortened search.
- **17 calendar records** in `calendar_conflicts.json`, every one with organiser-confirmed 2027 dates and a saved capture: 13 `related` and 4 `major_other`.
- **12 community records** in `communities.raw.json`: 9 active, 3 intermittent, 0 dormant, each with a saved own-page capture.
- **31 distinct search queries** plus 40+ direct page captures, listed in `community_discovery_log.md` and cited per record.

## Venue yield — what is real and what it cost

Sixteen candidates, spread across 12 areas in five wards inside the ~30 km sweep: Shinjuku (2), Asakusabashi, Roppongi (2), Otemachi, Akasaka, Toranomon, Tamachi, Shiba, Yurakucho, Shibuya (2), Akihabara, Shinagawa (2).

Top five by scored rank (all shortlist_ready):

1. **大手町プレイス カンファレンス103** — 0.9146 — 110 seats, ¥161,000 tax-excl. for 09:00–17:00 (¥230,000 for 09:00–21:00), free Wi-Fi in every room, projector set with 150-inch screen, published by the operator.
2. **新宿アイタウン会議室** — 0.9124 — 60 seats, ¥10,000/h weekend for 2027, 120-inch screen and 5,200 lm projector included, Wi-Fi 7, 08:00–21:00 published window.
3. **浅草橋ヒューリック カンファレンス ROOM 2** — 0.9074 — 72 seats, ¥90,000 tax-excl. all-day 09:00–21:00, projector set with 150-inch screen ¥8,000, 09:00–21:00 block published.
4. **Palette六本木** — 0.8798 — 81 seats, ¥13,800/h tax-included, projector, screen, four wireless mics and speakers included, food and drink brought in allowed, 09:00–22:00.
5. **東京国際フォーラム G402** — 0.8153 — 81 school / 130 theatre, ¥138,600 tax-incl. 09:00–17:00 (¥198,000 for 09:00–21:00), retractable screen standard, wireless LAN access points.

Other priced shortlist options worth naming: 品川インターシティ 会議室5 (¥129,000 tax-excl. 09:00–20:00, the only room in the sweep that explicitly permits alcohol-inclusive catering); AICC Room 301 and 東京虎ノ門グローバルスクエア Room A+B (both ¥400,000 tax-excl. for 09:00–17:00, hotel-grade AV, free Wi-Fi); ベルサール六本木グランド Room C (from ¥288,200 tax-incl., reference price only).

Comparability caveat: each USD figure is the price of that venue's own published package, and the packages are not the same length. i-Town, Palette and TKP are 8 hours of an hourly rate; Otemachi Place, AICC, TGSC and TIF are 8-hour day blocks; Hulic is a 12-hour all-day block; Shinagawa Intercity is an 11-hour all-day block; Bellesalle is a shortest-use reference price. Read the venue's `evidence.observed_facts` before treating two figures as like-for-like.

One source-reading note: TKP新宿's rendered room table drops the 定員(最大収容) cell for カンファレンスルーム4C, so its eight numbers render one column left of the header. The page's embedded layout-keyed JSON gives スクール 101名, シアター 124名, 立食 88名, which is what the record uses; the reasoning is written into the venue's evidence and into `source_uncertainty_notes.md`.

The two leads are informative rather than failures:

- **渋谷ヒカリエ 8/CUBE** — the venue is real and central, but the official page publishes area only (107㎡ total) and puts fees in a PDF that cannot be read here, so both capacity and cost are open. A 50-person event cannot be evidenced against it.
- **港区立産業振興センター 研修室1** — the cheapest 90-seat room with a projector found anywhere in the sweep (¥8,100 for the 09:00–17:00 morning+afternoon blocks at ward-group rates, roughly USD 51), but the fee schedule is restricted to registered ward or outside-ward small-business bodies, and outside groups pay double or four times those blocks. Whether an external community organiser can book it at all is a material open question, so it is a lead, not a shortlist pick.

## Why zero venues reached `eligible`

`eligible` requires a venue with every material fact evidenced, confirmed screen and Wi-Fi, a sourced numeric cost, a window supporting the duration, `needs_human_verify: false` and **no verification questions at all**. In Tokyo on 2026-11-28:

- No venue in the sweep publishes live 2027 availability in machine-readable form, so an `availability` question is unavoidable for every candidate.
- Almost every operator publishes prices tax-exclusive, so a `final_quote` question is unavoidable.
- Wi-Fi or screen inventory is genuinely absent from the published pages for 5 and 9 venues respectively.

That is a real information limit, not an artificial one. The shortlist_ready tier is exactly where these belong: selectable by Joe, with the remaining checks named.

## The FX basis and three hand recomputations

ECB reference rates, file dated 2026-11-27, fetched 2026-11-28: **EUR 1 = USD 1.0957**, **EUR 1 = JPY 174.81**. Derived and used everywhere: **1 JPY = USD 0.00626795** (USD 1 = JPY 159.541845). Full working in `fx_evidence_2026-11-28.md`.

1. i-Town weekend 2027: ¥10,000/h × 8 = **¥80,000**; 80,000 × 0.00626795 = 501.436 → **USD 501.44**.
2. Otemachi Place 103, 09:00–17:00: **¥161,000**; 161,000 × 0.00626795 = 1,009.140 → **USD 1,009.14**.
3. Tokyo International Forum G402, 09:00–17:00: **¥138,600**; 138,600 × 0.00626795 = 868.738 → **USD 868.74**.

Reverse check on (1): USD 501.44 × 159.541845 = ¥80,000.7, inside the rounding tolerance.

Note on the scorer output: `venues.shortlist.json` writes `meta.event_date` equal to the scorer's freshness reference, which defaults to the access date (2026-11-28). It is not an event date and nothing in this package proposes one.

## Calendar yield

Seventeen records, all with organiser-confirmed 2027 dates and captured source pages (nine from the first pass, eight added in review round 1 from organiser pages already on the wire or newly fetched):

- `related`: **AI・人工知能EXPO NEO 2027** (2027-01-07 to 01-08, Tokyo International Forum Hall E, ai); **Japan Fintech Week 2027** (2027-02-22 to 03-05, FSA + Fintech Association, fintech); **MoneyX 2027** (2027-03-01, ANA InterContinental, fintech); **FIN/SUM 2027** (2027-03-02 to 03-05, 丸ビルホールほか丸の内, fintech); **TEAMZ SUMMIT 2027 AI Edition** (2027-04-05 to 04-07, Happo-en, web3); **Japan IT Week 春 2027** (2027-04-07 to 04-09, Tokyo Big Sight, ai); **NexTech Week 2027 春** (2027-04-21 to 04-23, Tokyo Big Sight, ai); **SusHi Tech Tokyo 2027** (2027-05-20 to 05-22, Tokyo Big Sight, ai); **AI・人工知能EXPO Vertical 2027** (2027-06-16 to 06-18, Tokyo Big Sight, ai); **WebX 2027** (2027-08-25 to 08-26, Tokyo Big Sight, web3); **ETHTokyo 2027** (2027-08-25 to 08-29, city-wide, venues TBA, web3); **Japan IT Week 秋 2027** (2027-09-08 to 09-10, Makuhari Messe, ai); **NexTech Week 2027 秋** (2027-12-08 to 12-10, Makuhari Messe, ai).
- `major_other` (logistics only): **東京マラソン 2027** (2027-03-07); **Golden Week 2027** (2027-04-29 to 05-05); **東京ゲームショウ 2027** (2027-09-16 to 09-20, Makuhari); **CEATEC 2027** (2027-10-19 to 10-22, Makuhari).

Two organiser facts are worth flagging because they are easy to misread from a summary table. Japan IT Week's 2027-11-17..19 window on the japan-it.jp schedule is the 関西展 at インテックス大阪, not a Tokyo show; the Kanto autumn edition is 2027-09-08..10 at Makuhari Messe. And ETHTokyo 2027 is now announced by its own site for 2027-08-25..29 with venues TBA, which puts its first two days on the same dates as WebX 2027.

This is a real yield, not a complete one: several 2027 events are simply not announced yet, and a few organiser pages are unreachable. They are listed with an explicit unknown-date note in `source_uncertainty_notes.md` (Japan Blockchain Week 2027, PyCon JP 2027, ETHGlobal Tokyo 2027 — the last blocked by HTTP 403, IVS 2027) rather than being given a guessed window.

## Community yield

Twelve records: AI Tinkerers Tokyo; Tokyo AI Community; Ethereum Meetup Tokyo; Ethereum Japan; Web3 Tokyo / Offchain Tokyo; ICP Japan; 100BANCH; JDLA; Fintech Association of Japan; Japan Blockchain Association; TEAMZ; enXross DAO.

Nine carry a dated activity fact inside the last twelve months (2026-11-28 minus one year) and are marked active; three are intermittent with a precise in-person question. No group is marked active without a date, no co-host relationship is claimed, and the only member count stored is Tokyo AI Community's 156, which its own Meetup page displays. Co-host openness is recorded only once, for AI Tinkerers Tokyo, because its own pages name venue hosts and partners.

## What Tokyo's market made hard

1. **Prices live in PDFs.** Three of the most promising private venues (Akiba Plaza, Hikarie 8/CUBE, Granpark) publish rate cards only as PDFs, and this box has no PDF extractor. Three of the four null-cost records exist for that reason; the fourth (SHIBUYA QWS) publishes no rate at all.
2. **Public rooms are means-tested.** The cheapest halls are ward facilities with registered-group eligibility and lottery booking. The Minato case is the clearest: a 90-seat room with a projector at roughly USD 51 for the 09:00–17:00 blocks at ward-group rates (double for outside-ward groups, four times for outside-ward commercial use), open only to defined Japanese SME bodies.
3. **Conference rooms are tenant-only more often than the marketing suggests.** &BIZ conference publishes full rate tables but is restricted to Mitsui building tenants; it was excluded after reading, not before.
4. **Inquiry-only is the default for hotel and startup-hub floors.** QWS and Hikarie publish no rate at all, and most hub event spaces in the sweep are inquiry-only. Inquiry-only venues are retained as evidence-bound records with confirm-cost questions rather than being inflated into priced picks.
5. **21:00 closes are rarer than 12-hour days.** Otemachi Place, Hulic, TIF, AICC, TGSC, i-Town and Palette all publish a window that reaches 21:00 or later; 品川インターシティ closes at 20:00 and ベルサール publishes no hours at all.
6. **Tax-exclusive quoting is the norm.** Twelve of the sixteen records carry a published price, and eight of those twelve state 税抜/税別 explicitly (the rest are tax-inclusive or do not state tax). That is why `final_quote` questions dominate the verification set.
7. **Platform coverage is thin where it matters.** Japanese space marketplaces (Space Market, Instabase, Kashikaigishitsu, 会議室.COM) are useful discovery indexes, but for this package every price is taken from the operator's own page, so no marketplace listing is load-bearing evidence.
8. **Renovation and dead ends are normal.** 武蔵野公会堂 in Kichijoji has been closed since 2026-05-01 for renovation, which removed the only obvious cheap hall in that district.

## Gaps Joe should know about

- **Zero Kichijoji venue** (hall closed; only platform-listed private spaces surfaced, none with an operator page worth citing).
- **No 池袋 venue**: TKP池袋 was bot-walled (404 to curl, empty DOM from Chromium), so it was dropped rather than cited from a search snippet.
- **No 品川 Vision Center**: its price table is client-rendered and did not resolve in a headless browser; 品川 is covered instead by Shinagawa Intercity.
- **Two null-cost venues** (Granpark 401, Akiba Plaza セミナールーム1) and one null-cost hub (QWS) need a quote before they can be compared on budget.
- **Four screen-unknown and nine Wi-Fi-unknown** venues carry soft questions; none of those questions has been sent to a venue.
- **No 2027 availability** is confirmed for any venue. Every record says so.
- **Calendar is announcement-limited**: Japan Blockchain Week 2027 and PyCon JP 2027 have no 2027 edition yet, ETHGlobal's events index is bot-walled (HTTP 403), and IVS 2027 is unannounced; the array will need a second pass closer to the year.
- **Community depth is uneven**: the AI and Web3 layers are well evidenced, the DeAI layer thin (ICP Japan is the only explicit DeAI group), and the quant layer absent (no Tokyo quant community with own-page activity was found).
- **No date is selected or recommended anywhere in this package.** The venue set is date-independent, and every output can be re-read without inferring a scheduling decision.
