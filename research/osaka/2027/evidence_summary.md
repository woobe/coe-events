# Evidence summary — Osaka 2027, Run A (deep, from scratch)

Access date for every source: **2026-11-28**. Work root `/home/joe/repo_dev/coe-events`, research only — no store, no page, no publish, no commit. Currency JPY, EN + 日本語.

## 1. What was produced

- `venues.raw.json` — **16 venue records**, schema 2.4, all validated, all with numeric coordinates traceable to a saved Nominatim body.
- `venues.shortlist.json` — scorer output: **0 eligible / 16 shortlist_ready / 0 lead** (budget USD 5,000, attendance 50).
- `calendar_conflicts.json` — **4 organiser-verified 2027 rows** (3 `major_other`, 1 `related`).
- `communities.raw.json` — **13 records**: 7 active, 1 intermittent, 5 dormant.
- `fx_evidence_2026-11-28.md` — ECB basis dated 2026-11-27, fetched 2026-11-28, with hand recomputations.
- `captures/` — **88 files plus `INDEX.md`**, and **15 blocked-response files** under `captures/blocked/`; 79 INDEX bullets map every capture to its URL and its role.
- `venue_discovery_log.md`, `community_discovery_log.md`, `source_uncertainty_notes.md`.

## 2. Real yield, and why it looks like this

Osaka is a **public-hall market**. Seven of the sixteen records are municipal or prefectural rooms with printed fee tables in yen, published Saturday multipliers and no published alcohol or network position: マイドームおおさか, 大阪市中央公会堂, エル・おおさか, the three 大阪市立生涯学習センター halls, 大阪産業創造館, 港区民センター and 中央会館. The other shapes are thin: commercial conference centres either publish nothing readable (大阪カンファレンスセンター, PDF only), render their tables client-side (梅田スカイビル, ナレッジキャピタル) or are unreachable (innovation-osaka.jp, intex-osaka.com).

Consequences for the brief:

- **Price is not the constraint.** The recorded day rates run from USD 66.94 (港区民センター 第1集会室) to USD 992.84 (大阪商工会議所, 8 hours), i.e. 1.3%-20% of the soft USD 5,000 budget. Every shortlisted venue is comfortably inside budget on rent alone; the budget question here is AV, catering and staffing, not the room.
- **09:00 is the constraint.** Only エル・おおさか prints an explicit 09:00-21:00 全日 band (40,000 JPY / 9012, 57,200 JPY / 708) and マイドームおおさか prints a 09:00-21:00 終日 band (125,620 / 88,880 JPY). The municipal halls open at 09:30, which supports a 09:30-21:30 twelve-hour programme but not a 09:00 start. This is carried on each record as an availability question, never assumed.
- **Saturday pricing is a printed multiplier, not a guess.** 中央公会堂, the 生涯学習センター halls and the 港区民センター / 中央会館 halls all print 「土日祝は2割増」, and the recorded Saturday amounts are the printed weekday figure times that printed 1.2.
- **Alcohol is a licence question everywhere.** Not one venue page permits or forbids alcohol for a rented hall. 中央公会堂 中集会室 is the only page that describes catered parties as a use case; 大阪カンファレンスセンター is the only venue with in-house catering. The question is on all 16 records.
- **Recording strength is concentrated.** 大阪カンファレンスセンター 中会議室 銀杏 has an installed video projector and roll screen plus a control room, and 大阪産業創造館 4F has a 200-inch projector; that is why they score well on recording despite one unknown cost and one oversize flag.

## 3. Tier and score output (verbatim)

```
eligible: 0
shortlist_ready: 16
lead: 0
top selectable: マイドームおおさか — 第3会議室（8F） (score 0.8652, tier shortlist_ready)
```

Top five by score (from `venues.shortlist.json`):

```
0.8652  マイドームおおさか — 第3会議室（8F）              availability_unconfirmed,final_quote_required
0.8560  マイドームおおさか — 第1・第2会議室（連結, 8F）      availability_unconfirmed,final_quote_required
0.7224  大阪市中央公会堂 — 小集会室（3F, 定員150名）        screen_unknown,wifi_unknown,availability_unconfirmed
0.6625  大阪カンファレンスセンター — 中会議室 銀杏（3F）      cost_unknown,wifi_unknown,availability_unconfirmed
0.5723  港区民センター — 第1集会室（3F, 定員114名）         wifi_unknown,availability_unconfirmed,final_quote_required
```

The top two are the same building: MyDome's 第3会議室 is cheaper per seat and has free operator Wi-Fi plus rentable projector/screen; 第1・第2 is the larger option at 125,620 JPY. The scorer's `meta.event_date` is the access date (2026-11-28) because no event date was supplied — a technical artefact of date-independent scoring, not a scheduling statement.

No `eligible` tier is claimed: an eligible venue needs confirmed screen **and** Wi-Fi **and** a sourced cost **and** no open questions. Only MyDome has confirmed Wi-Fi, and every record carries at least an availability and an alcohol question, so nothing can honestly reach that tier from published pages alone.

## 4. Coordinates, captures and FX (verification output)

```
venue records: 16
numeric coordinates: 16/16
matched to a saved geocode response: 16/16
distinct geo bodies: 16
```

Validator exit codes: `venue_exit=0`, `community_exit=0`, `calendar_exit=0` (all `PASS:`).

Date-commitment grep across every `.md`/`.json` in `research/osaka/2027` (captures excluded):

```
phrase [recommended date] files=0 hits=0
phrase [preferred date]   files=0 hits=0
phrase [candidate Saturdays] files=0 hits=0
phrase [candidate window] files=0 hits=0
phrase [date commitment]  files=0 hits=0
```

`city_input.json` has `"target_date": null` and `"date_window": "2027-01-01 to 2027-12-31"`; no Saturday is named, ranked or proposed anywhere.

FX: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`, fetched 2026-11-28, reference date **2026-11-27**, EUR 1 = USD 1.0957 and EUR 1 = JPY 174.81 → **JPY 1 = USD 0.00626795**. Every one of the 15 known costs was regenerated from that single factor; three hand recomputations are in `fx_evidence_2026-11-28.md` (125,620 → USD 787.38; 31,100 → USD 194.93; 10,680 → USD 66.94) with reverse checks.

## 5. Calendar yield

Verified from organiser pages and captured: Japan IT Week / Japan DX & AX Week【関西】**2027-11-17..19** at インテックス大阪; 大阪マラソン2027 **2027-02-28** (9:15-16:15, Midosuji/Dotonbori course); 大阪マラソンEXPO2027 **2027-02-26..27** at インテックス大阪 6号館; AI-ESS-16 **2027-09-13..17** in Osaka. Three are logistics flags (`major_other`), one is an AI-audience `related` flag.

Four rows is a thin Osaka calendar, and that is the finding rather than a gap in effort: the two organisers that would carry most of it — Osaka Innovation Hub (innovation-osaka.jp) and Intex Osaka (intex-osaka.com) — did not respond to this worker, and the Tech Osaka Summit 2027 page sits on the unreachable host. オープンソースカンファレンス2027 Osaka (2027-01-30 per an aggregator) and ICAIIC 2027 (Osaka University venue printed, dates not printed) are recorded as unknown-date items, not rows.

## 6. Community yield

Thirteen records: Deep Learning Osaka (538), 大阪駆動開発 (2,459), GDG Greater Kwansai (3,456), GDG on Campus Osaka (1,054), GDG Osaka (107), Management & AI Commons Osaka (211) and QUINTBRIDGE (34,294 QB members) are active with dated 2026 activity; みやこでIT (651, 167 events since 2019) is intermittent because no 2026 date is printed; PyData Osaka, 関西AI駆動開発, CDLE大阪, 大阪分散技術コミュニティ and Osaka BCH are dormant by the 12-month rule and labelled as such.

The honest shape: **the AI/cloud developer scene is strong and the pure Web3 scene in Osaka is not.** GDG and 大阪駆動開発 give a large promotion surface; the Web3 side is one Kyoto-based Kansai group plus dormant Osaka crypto records. Co-host language exists on exactly one page (QUINTBRIDGE), so only one record carries the flag.

## 7. Every gap, stated

1. **Tech Osaka Summit 2027** — dates (2027-01-26..27) seen only in search snippets; organiser host unreachable. Not a calendar row.
2. **Osaka Innovation Hub** — no venue or community record; host unreachable on every attempt.
3. **Intex Osaka** — no venue record and no venue schedule; price page timed out.
4. **Shin-Osaka** — swept, but every readable quote came from operator/marketplace listings; no venue-owned page produced a 50-seat room, so no record was written rather than pad the set with a platform listing.
5. **Suita / Expo City** — メイシアター fee table captured (小ホール 土日祝 全日 42,000 JPY) but no official capacity page (404), so no record.
6. **大阪カンファレンスセンター price** — PDF only, unreadable here; null cost with a `cost_unknown` question.
7. **Alcohol** — unanswered by every source; 16 open questions.
8. **Wi-Fi** — confirmed at MyDome only; 15 unknown with questions.
9. **09:00 start** — impossible at the 09:30 municipal halls; 12-hour brief fully supported only at エル・おおさか and MyDome as printed.
10. **Shin-Osaka and Suita district coverage** — swept but unrepresented in the record set; the set skews to Kita / Nakanoshima / Chuo / Tennoji / Minato.
11. **Community contact routes** — only GDG Osaka's page publishes a contact form; the rest are join/apply pages, so no email or phone is recorded anywhere.
12. **No 2027 venue availability is confirmed** — every record's Saturday question is open; nothing here is a hold or a booking.
