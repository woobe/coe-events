# Source uncertainty notes — Tokyo 2027 run (accessed 2026-11-28)

Each item below is a source that could not be read, a figure that could not be published, or a conflict between two readable sources. Nothing in this list was filled in by guessing; where a figure is missing the venue carries a null cost or an open question instead.

## Unreadable or blocked sources

1. **`https://www.fsi.co.jp/akibaplaza/pdf/fee.pdf` (Fuji Soft Akiba Plaza fee table)** — HTTP 200, 183,536 bytes, but the box has no PDF text extractor (`pdftotext`, `mutool`, `pdftohtml` are all absent), so no room rate could be read. Consequence: セミナールーム1 carries `cost_basis: unknown` with a `cost_unknown` question.
2. **`https://www.hikarie8.com/hubfs/hikarie8_2026/assets/images/cube/CUBE使用料金表_20250930.pdf` (Shibuya Hikarie 8/CUBE fee table)** — same PDF limitation. Consequence: CUBE carries a null cost and a `cost_unknown` question.
3. **`https://granpark-c.com/granpa/wp-content/themes/gran/assets/pdf/guide/gran_price_list.pdf` (Granpark price list)** and the room page's "料金表" link — PDF only. The room page publishes a "from ¥91,300 (tax-inclusive)" starting figure with no duration, so the venue carries a null cost rather than an assumed day rate.
4. **TKP池袋カンファレンスセンター (`kashikaigishitsu.net/facilitys/cc-ikebukuro`)** — returned HTTP 404 to `curl` on 2026-11-28, and a headless-Chromium dump produced a 925-byte empty document. The search index shows the room table (ホール6A, 150 school seats, ¥25,700–31,700/h), but nothing could be saved, so the venue was dropped rather than cited from a search snippet. (TKP新宿, the same operator, was readable and is included.)
5. **ビジョンセンター品川 (`visioncenter.jp/shinagawa/price/`)** — the price table is rendered client-side; the plain fetch and a 30-second Chromium `--dump-dom` both returned template placeholders (`{{ discount.label }}`) instead of prices. No 品川 Vision Center record is included.
6. **connpass (all group pages: `*.connpass.com`)** — every request returned HTTP 202 with a zero-byte body (bot challenge). Affected: 生成AI勉強会, AI実装勉強会/AI社会実装勉強会, Tokyo.R, PyData Tokyo. These groups are listed in the discovery log as dropped, not as records.
7. **`meetup.com/machine-learning-tokyo`** — page and events page both HTTP 200, but the event calendar is JavaScript and the saved text carries no dates; the group could not be given an evidenced activity status and is not a record.
8. **`solana.com/ja/community`** — HTTP 429 (rate limited); nothing saved.
9. **DNS failures on 2026-11-28** (no live host, so no evidence): `www.solacity.jp`, `www.shibuya-owada.jp`, `gdg-tokyo.org`, `cryptobase.jp`, `centrum.tokyo`, `tokyo.pydata.org`, `www.ai-salon.tokyo`, `ai-tinkerers.org` (apex; the Tokyo subdomain worked).
10. **Dead paths on live sites**: `t-i-forum.co.jp/rental/` (404; the organiser conference-room page was found instead), `finolab.jp` (404 on root and `/event/`), `jdla.org/activity/` (404; homepage used), `kashikaigishitsu.net/facilitys/cc-ikebukuro/room_detail/3564/` (404).

## Readable but excluded after reading

11. **武蔵野公会堂 (Kichijoji)** — the official Musashino City page states the hall has been closed since 令和8年5月1日 (2026-05-01) for renovation. Excluded as a venue; no Kichijoji venue record is included in this run.
12. **&BIZ conference (Tokyo Midtown Yaesu / Nihonbashi)** — the page publishes full per-room rates, but states the rooms are for 三井のオフィステナント様向け (tenant companies of Mitsui buildings) only. Excluded: not publicly bookable for this event.
13. **OpenTAO "Bittensor Tokyo" chapter page** — readable but not credible as evidence (undated "up next" events, generic host bios, counters that do not reconcile). Dropped and flagged in the community log.

## Conflicts between two readable sources

14. **浅草橋ヒューリック カンファレンス ROOM 0 capacity** — the 使用内容例 page gives スクール形式（3名掛け）102名 while the 機材・備品 page gives スクール120席 for the same room. ROOM 2 (used in this package) is consistent at 72 seats on both pages, so the conflict does not affect any recorded venue; it is noted because ROOM 0 would otherwise have been a candidate.
15. **Bellesalle 六本木グランド Room C screen** — the facility page states screens are installed in rooms of 150㎡ or more, while Room C is listed at 154㎡ yet the room-level AV inventory is not published. Screen status is recorded as `confirmed` only because the facility's own threshold rule covers 154㎡, and a screen question is still carried.
16. **品川インターシティ 会議室1 ロの字 capacity** — the operator's own fee page gives 24名, while an aggregator page gives 30名. The operator figure is used; the room recorded is 会議室1+2 at 90 school seats, which both sources agree on.
17. **Tokyo Marathon 2027 field size** — the official 20th-anniversary page states the field rises from 39,000 to 40,000 runners; the race date (2027-03-07) is stated on the same official page.

## Announced-elsewhere but not organiser-confirmed for 2027 (kept out of the calendar array)

These events plausibly belong in a 2027 Tokyo calendar, but no organiser page with 2027 dates could be captured, so they are **not** in `calendar_conflicts.json` (the schema requires a real start date). They are recorded here with an explicit unknown-date note:

- **Japan Blockchain Week 2027** — `captures/cal_jbw_2026.html` (japanblockchainweek.jp, fetched 2026-11-28) still carries the 2026 edition only: "JUL 1st - JUL 15th, 2026", with the kickoff event on July 12, 2026. No 2027 dates or edition page are published.
- **PyCon JP 2027** — `captures/cal_pyconjp2026.html` (2026.pycon.jp, fetched 2026-11-28) gives the 2026 conference as 2026-08-21..22 at 広島国際会議場 with a sprint on 2026-08-23 at 広島大学; no 2027 page or date is published.
- **ETHGlobal Tokyo 2027** — `https://ethglobal.com/events` returned HTTP 403 (bot wall) to a plain curl fetch on 2026-11-28, so no 2027 schedule could be read; nothing recorded. No capture was kept, since a challenge page is not evidence.
- **IVS 2027 (Kyoto)** — outside the Tokyo/Kanto scope and not announced.
- **Tokyo AI Community 2027 editions** — none announced; only the 2026-12-13 edition is published.
- **WEF/startup "SusHi Tech Weeks" partner events 2027** — the Tokyo Metropolitan Government page states partner events will be recruited to broaden SusHi Tech Tokyo 2027 into "SusHi Tech Weeks", but no partner-event dates exist yet.

## Corrections made after review round 1 (2026-11-28, card `t_eea71ce6`)

1. **Japan Fintech Week 2027 / FIN/SUM 2027.** An earlier version of this file said "neither the FSA nor the Fintech Association of Japan page captured on 2026-11-28 states those dates". That was wrong. `captures/cal_jfw2027_fsa.html` (fsa.go.jp, news items dated 2026.11.17) states 「2027年2月22日（月）から3月5日（金）にかけて…「Japan Fintech Week 2027」を開催します」, and `captures/cal_finsum2027.html` gives 開催日時「2027年3月2日(火) - 5日(金)」(丸ビルホールほか, 主催 日本経済新聞社・金融庁). Both are now records in the calendar array; the earlier secondary window (2027-02-24..03-05) is superseded by the organiser pages.
2. **Japan IT Week 秋 2027 — date and venue.** `captures/cal_japan_it_week_2027.html` (japan-it.jp, fetched 2026-11-28) lists the 2027 schedule as 春展 2027/4/7–9 東京ビッグサイト, 名古屋展 2027/7/21–23 ポートメッセなごや, 秋展 2027/9/8–10 幕張メッセ, 関西展 2027/11/17–19 インテックス大阪. The autumn edition recorded in the array is therefore **2027-09-08 to 2027-09-10 at Makuhari Messe**. A review-round note mapped that 2027-11-17..19 window to Tokyo Big Sight; the capture places it in Osaka as the Kansai edition, so it is not recorded as a Tokyo/Kanto event.
3. **TKP新宿 カンファレンスルーム4C — table column alignment.** The rendered room table in `captures/tkp_shinjuku.html` has a nine-column capacity header (定員(最大収容)／スクール／島型／T字島／ロノ字／コの字／正餐／立食／シアター) but the 4C row emits only eight numeric cells (101名, 78名, 72名, 54名, 48名, 32名, 88名, 124名), with no 定員 cell, so the row is shifted one column left when rendered. The page's embedded room JSON for roomNumber 2270 keys the same figures by layout name — スクール 101名, 島型 78名, T字島 72名, ロノ字 54名, コの字 48名, シアター 124名, 正餐 32名, 立食 88名 — and the record follows that layout-keyed data. School seating is 101, theatre 124, standing buffet (立食) 88. The venue's `evidence.observed_facts` now states both readings; capacity and basis are unchanged, so no score moved.
4. **新宿アイタウン 2027 price page — tax treatment conflict.** `captures/itown_price_2027.html` contains both the sentence 「料金はすべて税込・1時間あたりです」 and a table that reads 「9,000円（税込：9,900円）」. The record stores the ¥10,000 weekend rate as the local amount with a `final_quote` question and quotes the page's ¥11,000 tax-inclusive counterpart; the store build must not silently adopt one reading without the quote.

## Structural limits of this run

- The research date is 2026-11-28. Any 2027 price, hour or availability statement is a statement about the venue's published position on that date, not a 2027 guarantee. Prices explicitly dated to change (Shinjuku i-Town from 2027-04-01) are flagged in their records.
- Tax treatment varies: Hulic, Otemachi Place, AICC, TGSC, TKP, Minato, Shinagawa Intercity and Tokyo International Forum publish some tax-exclusive figures; Palette and i-Town publish tax-inclusive or clearly labelled figures. Every tax-exclusive cost carries a `final_quote` question.
- Availability is not published in machine-readable form by almost any Tokyo venue; every candidate therefore carries an `availability` question and none is described as confirmed for any date.
