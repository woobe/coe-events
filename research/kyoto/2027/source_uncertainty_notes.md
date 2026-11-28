# Source uncertainty notes — Kyoto 2027 deep refresh (accessed 2026-11-28)

This file records every place where the evidence is thinner than the record implies, every failed fetch, and every question that a human must close. Nothing here is a recommendation.

## 1. Bot walls and failed fetches

- **Impact Hub Kyoto `/useourspace/`** — HTTP 000, zero bytes, four attempts: `curl` with a browser user agent at 45 s and 120 s, and headless Chromium (`--virtual-time-budget=30000`). The site root answered HTTP 200 in 0.7 s, so the failure is specific to that path. Only an Internet Archive capture of 2025-02-17 is readable (`captures/impacthub_useourspace_archive_20250217.html`), which is roughly 21 months old at the access date. The venue is recorded as a `lead` with a material `source_support` question.
- **connpass みやこでIT** (`mit.connpass.com`) — HTTP 202 with a 2,019-byte challenge body on two attempts with different browser user agents. No group content was served, so the record carries no activity claim.
- **Hacker News Kansai** (`hnkansai.org`) — connection timed out after 45 s with zero bytes. No capture, so the group is not recorded at all (the prior run's Meetup URL was not re-checked).
- **KRP ルーム2 detail page** (`krp.co.jp/kaigi/room/room2.html`) — HTTP 404. AV for that room is therefore unconfirmed and carried as a screen question.
- **Kyoto University clock-tower facility page** (`.../clocktower/facilities`) — HTTP 404; the correct facility page was found through search and captured as `kyotou_kokusai_hall.html`.
- **ハートピア京都 access and 京都アスニー access** — both guessed URLs returned 404. Addresses were taken from the official fee/room pages' own footers instead, and geocoding used the GSI address search.
- **京都観光Navi 時代祭 page** (`ja.kyoto.travel/event/major/jidaimatsuri`) — HTTP 404. The Jidai Matsuri date was taken from the shrine's own page instead.
- **平安神宮** — TLS chain error (`unable to get local issuer certificate`), fetched with `curl -k`. The content is the public shrine site; the certificate chain problem is recorded because it means the capture was made without verification.
- **PyData Osaka Meetup** — the URL recorded by the August 2026 run now returns Meetup's "Group not found" page ("Sorry, the group you're looking for doesn't exist"). No event history or member count is served. This is stronger than dormancy: the group has no live page.
- **京都大学 NLP laboratory** (`nlp.ist.i.kyoto-u.ac.jp`) — host did not resolve.
- **Access pages (round-2 fix pass)** — the clock tower's own access URL (`.../clocktower/access`) returned HTTP 404 today, and the two captured campus access pages (`/ja/access`, `/ja/access/campus/yoshida`) carry maps without any station name or walking time, so the Kyoto University record's nearest station is recorded as unknown. THE TERMINAL's guessed `/access/` path returned HTTP 404 (the live page is `/contact/#access`). 歴彩館's `/access/` path returned HTTP 404 (the access text sits on the homepage). アスニー's `/access/` path returned HTTP 404 (the official access map is `/asnymap.html`). Impact Hub Kyoto's `/access/` path timed out with zero bytes at 45 s (HTTP 000), so no file was written for it; its station remains unknown.

## 2. Geocoding method and its limits

- Coordinates come from the **Geospatial Information Authority of Japan (GSI) address-search API** (`https://msearch.gsi.go.jp/address-search/AddressSearch?q=...`), a government geocoder, with the JSON response saved as `captures/geo_*.json`. Nominatim answered `Access denied` to this host (`nominatim.openstreetmap.org` 403 with the required user agent), so it could not be used; Photon (komoot) was used only as a cross-check on three venues.
- GSI returns a **block-level point for the address**, not a surveyed building entrance. Twelve distinct coordinate pairs cover the eighteen records (kokoka ×4, Heartpia ×2, Asny ×2, Hearton ×2 share their building's point).
- 京都大学 時計台 was geocoded from 吉田本町 (the campus address on the university page); the returned point is the campus block, and the clock tower itself is a short walk inside it.
- Impact Hub Kyoto: the address published on the archived page is 甲斐守町97 (Nakadachiuri, Aburanokoji-nishi-iru), not the 相国寺町 variant that a first search guessed; GSI resolved 甲斐守町97 to 35.024364, 135.753296, which matches the OpenStreetMap "Impact Hub Kyoto" node (35.0249, 135.7533) within about 60 m.

## 3. Business-term uncertainty (per venue, folded into each record)

- **Tax treatment**: kokoka, Heartpia and Rekisaikan print fee tables without a consumption-tax statement; their records carry `final_quote` questions. Miyako Messe, KRP, Hearton and Elcient state tax-inclusive rates.
- **Impact Hub Kyoto**: no 2027 price readable. Cost is null with a `cost_unknown` question, and the 2025 archive price table is deliberately not converted.
- **THE TERMINAL KYOTO and FabCafe Kyoto**: no published headcount. Capacity is 0/unknown with a material `capacity` question, so both are `lead` regardless of price.
- **Kyoto University**: eligibility for an external organiser is unconfirmed and the fee schedule applies a half rate to specified event categories, so the recorded hourly estimate may not be the applicable class. Material `other_material` question.
- **京都学・歴彩館**: use is restricted to lectures and seminars related to Kyoto's history and culture; an AI×Web3 event may be refused. Material `other_material` question. The hall also closes at 17:00 on Saturdays and is closed on public holidays.
- **Alcohol**: an event-licence question, carried on every record. 京都アスニー is the only venue that publishes a rule (アルコール飲料類は禁じております — prohibited), so its two rooms record the prohibition as the answer and need no question. The other sixteen records each carry an explicit alcohol-permission question — whether serving alcohol at a private community event is allowed, whether an event liquor licence is required and who must hold it — rather than assuming that a hotel bar, restaurant or cafe licence covers a rented hall; the Elcient hotel record says so in as many words.
- **Nearest station**: stated with a walking time on all eighteen records. Twelve were added in the round-2 fix pass from a captured operator access page (kokoka rooms: Keage 6 min; both Heartpia rooms: Marutamachi direct underground link; both Asny rooms: Nijo station then bus 15/52 and 400 m west; Elcient: JR Kyoto Station Hachijo east exit 2 min; Hearton 宇治伏見: Karasuma Oike 2 min; KRP ルーム2: JR Tanbaguchi 5 min; 歴彩館: Kitayama 4 min; THE TERMINAL: Shijo exit 6 / Hankyu Karasuma 6 min), and four already carried theirs (kokoka Event Hall: Keage; Miyako Messe: Higashiyama 8 min; Hearton 嵐山: Karasuma Oike 2 min; FabCafe: Gojo 10 min). Two are explicitly unknown with a location question: Kyoto University (access URL 404, campus pages maps-only) and Impact Hub Kyoto (`/access/` timed out, archive names no station).
- **12-hour window**: only kokoka, Heartpia, Miyako Messe, Asny, Elcient, Hearton, KRP and Kyoto University publish hours that reach 21:00 or later. Rekisaikan stops at 17:00 on Saturdays; 京都テルサ would have reached 21:30 but was excluded on rate-attribution grounds.
- **Indirect rate arithmetic**: Elcient's recorded 150,000 yen is its printed 7-hour special (130,000) plus one printed overtime hour (20,000); KRP's recorded 128,700 yen is the printed 09:00-17:00 package and the 12-hour total (plus the 28,600 yen night block) is stated in evidence only. Both are arithmetic on printed rates, labelled as such.

## 4. Calendar uncertainty

- **IVS 2027 is unannounced.** The organiser site (`ivs.events`, captured) still presents IVS2026 (2026-07-01 to 03, Miyako Messe + Hotel Okura Kyoto) and has no 2027 edition page. The prior run's note that editions run in early July is a pattern, not a 2027 date, so IVS is an unknown-date note, not a calendar row.
- **Gion Matsuri dates** come from the Yamaboko Rengokai's official schedule, which prints the 17 and 24 July processions without a year (the date was fixed in 1888). 17 and 24 July 2027 both fall on Saturdays; the record cites the organiser schedule and the weekday arithmetic is the only inference.
- **KYOTOGRAPHIE 2027** dates (2027-04-17 to 05-16) come from the festival's own news post; theme, artists and venues are explicitly "to be announced".
- **Golden Week** spans 2027-04-29 to 2027-05-05 as a single row; only 29 April, 3, 4 and 5 May are public holidays per the JP registry, and the row's evidence says so rather than implying a seven-day holiday.
- **No school lane.** The plan-event registry carries JP, JP:osaka and JP:tokyo school authorities but no Kyoto school authority. No Kyoto school-holiday date is asserted anywhere in this package; the school lane for Kyoto is **unopened**.
- **Excluded on topic grounds**: オープンソースカンファレンス 2027 Osaka (2027-01-30, captured) — no closed-enum relevance fits an OSS event and `related` forbids `other`. RubyKaigi 2027 (2027-04-14..16) and WebX 2027 (2027-08-25..26) are outside Kansai (Miyazaki and Tokyo). Tech Osaka Summit 2027 (2027-01-26..27, Grand Front Osaka) is a startup summit with no closed-enum topic relevance and negligible Kyoto logistics impact, so it is logged here rather than in the array.
- **Only two `related` records** (AI博覧会 Osaka, Japan IT Week 関西) — that is a coverage finding, not an omission: no other 2027 Kansai AI/ML/data/web3/fintech/quant/DeAI/agent event with an organiser-published 2027 date was found in this sweep.

## 5. Scorer artefacts

- `score_venues.py` was run without `--event-date`, so `meta.event_date` in `venues.shortlist.json` reads `2026-11-28` (the access date). That field is a scoring artefact; no date is recommended anywhere in this package. `score_dates.py` was not run.
- The scorer's tiers are deterministic for these inputs; `venues.shortlist.json` is byte-identical across runs (SHA-256 recorded in `evidence_summary.md`).

## 6. Prior-run conflicts (2027-q2 bundle, August 2026)

These are the differences found when re-verifying the old bundle's fields against live pages today. The old bundle was not edited.

1. **Impact Hub Kyoto**: old run ranked it first at 0.7069 (`shortlist_ready`). Today's live page does not respond, so it is a `lead` with a null cost. This is the single largest change in the package.
2. **PyData Osaka**: old run recorded it as `dormant` with a working Meetup URL; the group page no longer exists.
3. **GDG Kyoto**: old run recorded `active`; today's page carries no dated 2026 event, so the status is `intermittent`.
4. **Kyoto University Clock Tower**: old run recorded it `shortlist_ready` at 0.5285; the external-organiser eligibility question is material, so it is a `lead`.
5. **KRP A/B/C 42 seats**: old run's "material capacity question" is confirmed — the printed school capacity is 42, below the 50-person brief.
6. **kokoka rates**: old run recorded 74,500 yen for the Event Hall 09:00-17:00; the current page prints the same figure (30,300 + 44,200), so that field is unchanged.
7. **Calendar**: the old run had 6 records and 0 `related`; this run has 12 records and 2 `related`, plus IVS/IVS-adjacent notes.
8. **Communities**: old run had 6 records (2 active); this run has 13 (6 active, 6 intermittent, 1 dormant) with narrower, page-level claims.

## 7. Round-2 fix pass (reviewer round 1, 2026-11-28)

The eight findings were fixed without re-research, without new venues and without touching `research/kyoto/2027-q2/`:

1. Alcohol-permission questions added to the ten records that lacked one (kokoka ×4, Heartpia ×2, Elcient Room B, Kyoto University, 歴彩館, Impact Hub Kyoto); the two アスニー rooms record the page's published prohibition instead. `city_input.json` and §3 above now say "sixteen questions plus two published prohibitions", which is what the records carry.
2. Nearest station and walking time added to the fourteen records that lacked one, from captured operator access pages; Kyoto University and Impact Hub Kyoto are recorded as unknown with a `location` question. All eighteen records now state a station, a walking time or an explicit unknown.
3. BitSummit 2027 `source_url` replaced with the canonical percent-encoded organiser URL.
4. Golden Week row now cites the captured Cabinet Office page (`captures/cao_shukujitsu_2027.html`) and names the JP registry edition `令和9年（2027年）の国民の祝日・休日（内閣府）` with per-row locators.
5. Old Clock Tower score corrected from 0.538 to **0.5285** in §6.4.
6. Query count reconciled: the discovery log's header and `evidence_summary.md` §1 now say **26**, the number the log actually enumerates.
7. `evidence.geo` on all eighteen records now equals the GSI query URL recorded in `captures/INDEX.md` (the captured queries use 京都府京都市…); coordinates are unchanged.
8. THE TERMINAL KYOTO's Saturday stance and PyData Osaka's cadence are now explicit: Saturday availability unknown (daily hours only) with a question; cadence unknown because the Meetup group page is gone.
