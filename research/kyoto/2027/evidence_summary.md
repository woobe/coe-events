# Kyoto 2027 — evidence summary (deep refresh, Run A)

Prepared by: jnr-research (Kanban t_46265e91)
Research date: **2026-11-28**
Work root: `/home/joe/repo_dev/coe-events/research/kyoto/2027/`
Prior bundle: `research/kyoto/2027-q2/` (August 2026) — read as a lead list only, never edited, never cited as evidence.

---

## 1. What is in this package

| File | Kind | Records | Validator |
| --- | --- | --- | --- |
| `city_input.json` | city research input | 1 | not a validate_schema kind (consumed by bundle_assembler) |
| `venues.raw.json` | venue (schema 2.4) | 18 | PASS exit 0 |
| `venues.shortlist.json` | scorer output | 18 | scorer exit 0, byte-identical on re-run |
| `calendar_conflicts.json` | calendar_conflict | 12 (bare array) | PASS exit 0 |
| `communities.raw.json` | local_community | 13 | PASS exit 0 |
| `fx_evidence_2026-11-28.md` | FX basis | — | — |
| `captures/` + `INDEX.md` | evidence | 90 files (+ `INDEX.md`) | INDEX maps every file 1:1 |
| `source_uncertainty_notes.md` | uncertainty log | — | — |
| `community_discovery_log.md` | discovery/disposition | 35 queries bundle-wide (31 in its own list) | — |
| `venue_discovery_log.md` | discovery/disposition | 18 queries | — |

Validator exit codes (whole file and per record):

```
$ python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py venue research/kyoto/2027/venues.raw.json
PASS: research/kyoto/2027/venues.raw.json is valid [venue]            # exit 0
$ python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py calendar_conflict research/kyoto/2027/calendar_conflicts.json
PASS: research/kyoto/2027/calendar_conflicts.json is valid [calendar_conflict]   # exit 0
$ python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py local_community research/kyoto/2027/communities.raw.json
PASS: research/kyoto/2027/communities.raw.json is valid [local_community]        # exit 0
per-record venue validation: 18 / 18 passed
per-record calendar validation: 12 / 12 passed
per-record community validation: 13 / 13 passed
```

## 2. Scorer output — tiers and top five

```
$ python3 ~/.hermes/skills/plan-event/scripts/score_venues.py research/kyoto/2027/venues.raw.json \
    --output research/kyoto/2027/venues.shortlist.json --budget-usd 5000 --target-attendance 50
eligible: 0
shortlist_ready: 13
lead: 5
top selectable: 京都市生涯学習総合センター（京都アスニー）— 第3研修室 (score 0.8829, tier shortlist_ready)
```

Top five (from `venues.shortlist.json`):

```
0.8829  京都市生涯学習総合センター（京都アスニー）— 第3研修室        USD 114.20   shortlist_ready
0.8812  京都市生涯学習総合センター（京都アスニー）— 第2研修室        USD 157.51   shortlist_ready
0.8499  ホテルエルシエント京都八条口 — Conference Room B             USD 940.19   shortlist_ready
0.8200  kokoka 京都市国際交流会館 — Special Conference Room          USD 437.50   shortlist_ready
0.7746  京都市勧業館 みやこめっせ — 大会議室（B1F）                  USD 197.88   shortlist_ready
```

Full tier breakdown:

- **shortlist_ready (13):** Asny 第3 (0.8829), Asny 第2 (0.8812), Elcient B (0.8499), kokoka Special (0.8200), Miyako Messe 大会議室 (0.7746), Heartpia 第5 (0.7519), kokoka Seminar (0.7482), kokoka 第1+第2 (0.7481), Heartpia 大会議室 (0.7451), kokoka Event Hall (0.7388), Hearton 嵐山 (0.7114), KRP ルーム2 (0.7002), Hearton 宇治伏見 (0.6989).
- **lead (5):** FabCafe Kyoto (capacity unknown, 14 tatami), Impact Hub Kyoto (live page unreachable; archive-only evidence), THE TERMINAL KYOTO (capacity and price unpublished), 京都大学 国際交流ホール I (external-organiser eligibility material), 京都府立京都学・歴彩館 小ホール (purpose restriction material; Saturday closes 17:00).
- **eligible (0):** expected — every record carries at least one soft verification question, and the scorer reserves `eligible` for fully evidenced venues with no questions.

Byte-identity and hash:

```
$ cmp /tmp/sl_a.json research/kyoto/2027/venues.shortlist.json && echo "shortlist byte-identical"
shortlist byte-identical
$ cmp /tmp/score_run1.log /tmp/score_run2.log && echo "scorer logs byte-identical"
scorer logs byte-identical
$ sha256sum research/kyoto/2027/venues.shortlist.json
e0da38ac5fe08386825b370ca9c2f3432f613bb932a31e9a7e10767d3af51a7c
```

The hash moved from `ddb9bc36…` (round 1) to `e0da38ac…` because the round-2 fix pass added verification questions to the raw venue records and the scorer copies every raw field into the shortlist. The tiers, scores and ordering are unchanged (0 / 13 / 5, top still Asny 第3研修室 0.8829), and two consecutive scorer runs are byte-identical.

## 3. Coordinates audit

```
venues: 18
numeric coordinate pairs: 18 / 18
records with evidence.geo URL: 18 / 18
inside Kyoto bbox (34.90-35.10, 135.68-135.85): 18 / 18
distinct coordinate pairs: 12
```

Twelve distinct points carry eighteen records because four venues have two or four room-level records (kokoka ×4, Heartpia ×2, Asny ×2, Hearton ×2). Every point is a JSON number pair, never a string, and each record's `evidence.geo` is the GSI address-search URL that produced it, with the JSON response saved as `captures/geo_*.json`. In the round-2 fix pass each `evidence.geo` value was replaced with the exact URL string recorded in `captures/INDEX.md` (the captured queries are prefixed 京都府京都市…); all 18 now match their INDEX line verbatim and the coordinates are unchanged.

## 4. FX basis and three hand recomputations

Basis (see `fx_evidence_2026-11-28.md`): ECB `eurofxref-daily.xml`, fetched 2026-11-28, reference date printed 2026-11-27 — EUR 1 = USD 1.0957, EUR 1 = JPY 174.81 → USD 1 = JPY 159.5418, 1 JPY = USD 0.00626795.

1. Heartpia 第5会議室, JPY 22,390 × 0.00626795 = 140.3378 → **USD 140.34** (reverse: 140.34 × 159.541845 = 22,390.6 JPY).
2. kokoka Event Hall, JPY (30,300 + 44,200) = 74,500 × 0.00626795 = 466.9623 → **USD 466.96**.
3. Miyako Messe 大会議室, JPY 31,570 × 0.00626795 = 197.8791 → **USD 197.88**.
4. (hourly check) Kyoto University 国際交流ホール, JPY 10,700 × 0.00626795 = 67.0671/h → 8 h = **USD 536.54**.

## 5. Calendar disposition

- **12 records, all inside calendar year 2027** (start dates 2027-01-20 through 2027-11-19). `related` 2, `major_other` 10.
- `related`: AI博覧会 Osaka 2027 (2027-01-20/21, MyDome Osaka, relevance `ai`) and Japan IT Week 関西 2027 (2027-11-17/19, Intex Osaka, relevance `ai`).
- `major_other` (logistics only, relevance `other`, severity `none`): Kyoto Marathon 2027-02-21; KYOTOGRAPHIE 2027-04-17..05-16; World Masters Games 2027 KANSAI 2027-05-14..30; Aoi Matsuri 2027-05-15; BitSummit 2027 2027-05-21..23; Gion Matsuri 前祭 2027-07-17; Gion Matsuri 後祭 2027-07-24; Gozan no Okuribi 2027-08-16; Jidai Matsuri 2027-10-22; Golden Week 2027-04-29..05-05.
- **Holiday dates come only from the JP registry rows** (内閣府 list): 2027-04-29 昭和の日, 2027-05-03 憲法記念日, 2027-05-04 みどりの日, 2027-05-05 こどもの日. The Golden Week row spans 29 April-5 May and states in its own evidence that only those four dates are holidays.
- **School lane: unopened.** The registry carries JP, JP:osaka and JP:tokyo school authorities and no Kyoto school authority, so no Kyoto school-holiday date is asserted anywhere in this package.
- **Unknown-date notes:** IVS 2027 (organiser site still presents IVS2026; no 2027 edition page), KYOTOGRAPHIE theme/artists/venues (explicitly "to be announced"). Both are in `source_uncertainty_notes.md` §4.
- Excluded with reason: オープンソースカンファレンス 2027 Osaka (2027-01-30 — no closed-enum relevance fits, `related` forbids `other`), RubyKaigi 2027 (Miyazaki) and WebX 2027 (Tokyo) — outside Kansai, Tech Osaka Summit 2027 (no closed-enum topic relevance, negligible Kyoto logistics).

## 6. Community disposition

- **13 records:** 6 `active`, 6 `intermittent`, 1 `dormant`.
- Active with dated in-person activity inside the 12 months before 2026-11-28: KOIN (2026-12-02 events), Kyoto eggs (2026-11-14 定例会), KC3 (2026-09-23 conference at KRP), データサイエンススクール京都 / CIREDS (2026-09-19 session, 2,029 members), 関西デジタルコンテンツ事業協同組合「スナックAI」 (2026-12-14, Kobe), 大阪イノベーションハブ (2026-11-28 event, news dated 2026.11.26).
- Intermittent: GDG 京都, 京都大学ブロックチェーン研究センター, 鹿島・竹内研究室, 学習機械分野, Kyoto Next CxO Community, みやこでIT (bot-walled page, no claim).
- Dormant: PyData Osaka — its Meetup URL now returns "Group not found".
- **No co-host badge anywhere:** `cohost_open` is false on all 13 records because no group's own page carries quotable co-host solicitation language. Every record has a public HTTPS contact route (never an email address or phone number).

## 7. Which old-run (2027-q2) fields changed after re-verification

The August 2026 bundle is untouched. These are the fields that today's live pages contradict or cannot support:

1. **Impact Hub Kyoto — tier and cost.** Old: `shortlist_ready`, score 0.7069, top of the set, JPY 72,000 / USD 452.57 from the live page on 2026-08-13. Today: the live page returns HTTP 000 on four attempts, the only readable copy is a 2025-02-17 archive, and the record is a `lead` with `estimated_cost_usd: null` and a material `source_support` question. This is the biggest single change in the package.
2. **PyData Osaka — the source no longer exists.** Old: `dormant` with a working Meetup URL. Today: `meetup.com/pydata-osaka` serves Meetup's "Group not found" page.
3. **GDG Kyoto — activity status.** Old: `active`. Today: `intermittent`, because the site states a monthly intention but publishes no dated 2026 event and pushes announcements to external sites.
4. **Kyoto University Clock Tower — tier.** Old: `shortlist_ready` (0.5285). Today: `lead`, because external-organiser eligibility is a material question and the fee schedule applies a half rate only to specified event categories.
5. **kokoka rates — unchanged.** Old and new both read 74,500 yen for the Event Hall 09:00-17:00 (30,300 + 44,200); the Special Conference Room (69,800) and Seminar Room (27,100) are new records from the same table.
6. **KRP A/B/C — capacity confirmed, not changed.** The printed school capacity is 42, below the 50-person brief; the retained KRP record is ルーム2 (96 school seats).
7. **Hearton/KRP rate basis — clarified.** Hearton's tariff is duration-banded (7-8 h = 134,000 / 84,000 yen) and KRP's 全日 is 09:00-17:00 only with a separate 18:00-21:00 night block; both are now stated inside evidence rather than implied.
8. **Calendar — 6 records to 12.** Old: 6 `major_other`, 0 `related`, Q2 only. New: full-year, 2 `related` (AI博覧会 Osaka, Japan IT Week 関西) + 10 `major_other`, with IVS 2027 as an explicit unknown-date note instead of a guessed July window.
9. **Communities — 6 records to 13.** Old: 2 active / 2 intermittent / 2 dormant. New: 6 / 6 / 1, each with a page-level activity claim and a public contact route.
10. **Coordinates — added.** Old bundle had null latitude/longitude on every record (`map_location_unknown`); this run has 18/18 numeric pairs inside the Kyoto bounding box with a government-geocoder URL on each.
11. **FX basis — moved forward.** Old: ECB 2026-08-12 (1 JPY = USD 0.00628573). New: ECB 2026-11-27 (1 JPY = USD 0.00626795), a 0.3% difference in every USD figure.
12. **New venues not in the old set:** ハートピア京都 (×2), みやこめっせ 大会議室, 京都アスニー (×2), ホテルエルシエント, 京都府立京都学・歴彩館.
13. **Old-set venues not carried:** 京都テルサ and キャンパスプラザ京都 (rate tables present only as PDFs whose rows cannot be attributed to rooms without guessing), ICC Kyoto (no readable room-level capacity/rate; convention-centre scale), KRP A/B/C (42 school seats, replaced by KRP ルーム2).
14. **Reviewed and excluded this run (not in the old set either):** 京都経済センター (largest room about 30), リーガロイヤルホテル京都 (per-person banquet pricing, no plain 50-person room rate), イベントホール洛央 (aggregator-only, no official page captured), 右京区役所 meeting rooms (largest room 30).

## 8. Zero date commitments

Grepped across everything except `captures/`, for the five phrases the card names (written here in hyphenated form so this audit block is not itself a match):

```
recommended-date      0 matches
preferred-date        0 matches
candidate-Saturday    0 matches
target-date           0 matches
we-recommend          0 matches
```

Re-run output (raw):

```
$ for p in recommended-date preferred-date candidate-Saturday target-date we-recommend; do
    grep -rIn --exclude-dir=captures -i "${p//-/ }" . || echo "$p: 0 matches"; done
recommended-date: 0 matches
preferred-date: 0 matches
candidate-Saturday: 0 matches
target-date: 0 matches
we-recommend: 0 matches
```

Before the round-2 fix pass this section reproduced the five phrases verbatim (as the audit lines above), so a grep of the bundle returned those audit lines; the phrasing is now hyphenated so the grep is genuinely 0. `city_input.json` carries `target_date: null` and `date_window: null`; `score_venues.py` was run without `--event-date`; `score_dates.py` was not run. The only "recommend" strings in the bundle are the disclaimers that no date is recommended.

## 9. Evidence discipline notes for the reviewer

- **Facts vs inference** are separated inside every record: `evidence.observed_facts` is page content with the fetch date, `evidence.inference` is my reading. Nothing in `inference` is presented as a source claim.
- **Rate arithmetic** that is not a printed package is labelled in the record text (Elcient 7 h + 1 overtime hour; KRP 8 h package with the 12 h total in evidence; Kyoto University hourly × 8; Asny 午前 + 午後 summed because no combined row is printed).
- **Alcohol** is treated as a licensing question, never an amenity: only 京都アスニー publishes a rule (prohibited), and its two rooms record that prohibition as the answer; the other sixteen records each carry an explicit alcohol-permission question (permitted? which event liquor licence, held by whom?) and no hotel bar or cafe licence is assumed to cover a rented hall.
- **Nearest station** is stated on every record: sixteen with a station and walking time from a captured operator access page or already-captured page, two (Kyoto University, Impact Hub Kyoto) as an explicit unknown with a `location` question after the access URLs 404'd or timed out.
- **PNG/render/store work was not done.** No `city.json`, no page, no publish, no commit, no sentinel, and `research/kyoto/2027-q2/` was not modified.

## 10. Open questions for Joe / the reviewer

1. Impact Hub Kyoto cannot be priced today; the 2025 archive price is deliberately not converted. Do you want the office contacted directly, or the venue held as a lead?
2. 京都アスニー 第3研修室 tops the scorer at 0.8829 but is a 72-seat municipal study room with a separate 17:00-18:00 surcharge hour; the score rewards price, not room quality. Which two or three rooms should be quoted first?
3. Rekisaikan and Kyoto University both carry material eligibility questions (purpose restriction / external-organiser permission). Should they be approached before the shortlist is narrowed?
4. IVS 2027 is unannounced; a calendar refresh in spring 2027 would pick it up. Should that be a follow-up card?
5. The related-event set is thin (two records) because no other 2027 Kansai AI/ML/data/web3/fintech event with organiser-published dates exists yet. Is a Q1 2027 re-sweep desired?
6. School lane for Kyoto is unopened (no registry row). Should a Kyoto school authority be added to the registry card before the store build?

## 11. Round-2 fix pass (reviewer round 1, 2026-11-28)

Eight findings were fixed in one pass with no re-research, no new venues and no edit to `research/kyoto/2027-q2/`.

1. **Alcohol licensing question** added to the ten records that had none (kokoka ×4, Heartpia ×2, Elcient Room B, Kyoto University, 歴彩館, Impact Hub Kyoto), each as a `booking_terms` question. The two アスニー rooms record the page's published prohibition instead. Coverage re-audited: **16 records carry the question + 2 publish a prohibition = 18 / 18**.
2. **Nearest station + walking time** added to the fourteen records that lacked it, from captured operator access pages (`asny_accessmap.html`, `heartpia_fee.html`, `elcient_conference_jp.html`, `hearton_access.html`, `krp_access.html`, `rekisaikan_home.html`, `terminal_contact.html`, `kokoka_access.html`). Kyoto University and Impact Hub Kyoto are explicit unknown with a `location` question. Coverage: **18 / 18** state a station, a walking time or an explicit unknown.
3. **BitSummit 2027 `source_url`** replaced with the canonical percent-encoded organiser URL that `captures/INDEX.md` records.
4. **Golden Week row** now cites the captured Cabinet Office page `captures/cao_shukujitsu_2027.html` (HTTP 200, 20,682 bytes) and names the registry edition `令和9年（2027年）の国民の祝日・休日（内閣府）` with the four per-row locators inside `evidence.observed_facts`.
5. **Old Clock Tower score** corrected to **0.5285** in `source_uncertainty_notes.md` §6.4.
6. **Query count** reconciled: **35 bundle-wide** — 4 community-specific + 14 venue/district + 13 calendar + 4 venue follow-up (`venue_discovery_log.md` items 15-18) — with the 31-item breakdown (4 + 14 + 13) shown in the discovery-log header and its calendar list renumbered 19-31. The same 35 appears in §1 above and in §12 item 1.
7. **`evidence.geo`** now equals the exact captured GSI query URL for all 18 records (18 / 18 match `INDEX.md` verbatim); coordinates unchanged.
8. **THE TERMINAL KYOTO** Saturday availability stated as unknown (daily hours only) with an `availability` question; **PyData Osaka** cadence stated as unknown because its Meetup group page returns "Group not found".

Re-run after the pass:

```
venue validator:            PASS exit 0   (per record 18 / 18)
calendar validator:         PASS exit 0   (per record 12 / 12)
community validator:        PASS exit 0   (per record 13 / 13)
scorer:                     eligible 0 / shortlist_ready 13 / lead 5
shortlist sha256:           e0da38ac5fe08386825b370ca9c2f3432f613bb932a31e9a7e10767d3af51a7c
coordinate audit:           18 / 18 numeric, 18 / 18 in bbox, 12 distinct pairs
USD audit:                  16 priced, 0 mismatches at 2dp (1 cent boundary
                            case, KRP ルーム2, see fx_evidence_2026-11-28.md), 2 null-cost
captures:                   90 files, 90 index bullets, 0 orphans
```

The shortlist hash necessarily moved (the scorer copies raw fields, and the raw records gained questions); tiers, scores and ordering are unchanged.

## 12. Round-3 documentation pass (reviewer round 2, 2026-11-28)

Three documentation defects from review round 2 were closed. No research, no venue, calendar, community or cost record changed, and no field on `venues.raw.json` changed.

1. **Discovery total now equals its own enumeration.** Bundle-wide figure is **35** distinct searches: 4 community-specific + 14 venue/district + 13 calendar + 4 venue follow-up. The community log's own list is 31 (4 + 14 + 13) and its calendar queries are renumbered 19-31 to match the thirteen topics named. `venue_discovery_log.md` declares that its 18 = the same 14 core searches + 4 follow-ups (its items 15-18), which are the only searches outside the 31. The figure 35 appears identically in the community-log header, §1 above and §11 item 6.
2. **`city_input.json` `open_questions[1]`** first clause corrected from "five of eighteen" to **three of eighteen**, naming the three records that actually hold the gaps (Impact Hub Kyoto and THE TERMINAL KYOTO unpriced, THE TERMINAL KYOTO and FabCafe Kyoto with no headcount, overlapping at THE TERMINAL), with the second clause kept to the four priced-with-unknown-terms venues. This matters beyond prose because `bundle_assembler.py` copies `open_questions` into the bundle's `unresolved_checks`.
3. **`community_discovery_log.md`** calendar pointer corrected from `evidence_summary.md` §4 (FX basis) to **§5** (calendar disposition).

Re-run after the pass (all unchanged):

```
venue validator:            PASS exit 0
calendar validator:         PASS exit 0
community validator:        PASS exit 0
scorer:                     eligible 0 / shortlist_ready 13 / lead 5
shortlist sha256:           e0da38ac5fe08386825b370ca9c2f3432f613bb932a31e9a7e10767d3af51a7c
coordinate audit:           18 / 18 numeric, 18 / 18 in bbox
USD audit:                  16 priced, 0 mismatches at 2dp (1 cent boundary
                            case, KRP ルーム2, see fx note), 2 null-cost
calendar rows:              12, all 2027
communities:                13
captures:                   90 files, 90 index bullets
date grep (5 phrases):      0
```

`city_input.json` is not an input to `score_venues.py`, so the shortlist hash is unaffected by the `open_questions` wording change and stays `e0da38ac…`.
