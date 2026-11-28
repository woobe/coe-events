# Source uncertainty notes — Osaka 2027 (accessed 2026-11-28)

## 1. Hosts that never answered

- **innovation-osaka.jp** (Osaka Innovation Hub, and the Tech Osaka Summit 2027 organiser host) — connection timeout on both `https://www.innovation-osaka.jp/` and `https://innovation-osaka.jp/tech-osaka-summit/en` (75-90 s). Consequence: no OIH venue record; **Tech Osaka Summit 2027 is not in `calendar_conflicts.json`**, even though search snippets showed 2027-01-26..27 at Knowledge Capital Congrès Convention Center. Those dates are unverified from the organiser and are carried here as a verification item only.
- **intex-osaka.com** — the organiser price page timed out (75 s). Consequence: no Intex Osaka venue record and no Intex event schedule read from the venue itself.
- **osaka-startup.com** — DNS resolution failed. Consequence: no ecosystem-portal evidence used.
- **www.sansokan.jp** — HTTP 403 on every attempt (plain curl and headless Chromium). The rental subdomain `shisetsu.sansokan.jp` served normally and is the cited source for both 大阪産業創造館 records; the main site is not claimed.

## 2. Pages that exist but publish an unreadable price

- **大阪カンファレンスセンター** publishes its room fee table only as `pdf/shisetsu_fee.pdf`. This environment has no PDF text extractor (`pdftotext`, `mutool`, `qpdf`, `gs` absent; `pypdf`/`pdfminer` not installed). The PDF is captured (`ihosaka_fee_pdf.pdf`, 201,525 bytes) but no amount is read from it, so `estimated_cost_usd` is null with a `cost_unknown` question. The room is otherwise the strongest recording fit in the set (installed video projector + roll screen, 90 seats, in-house catering).

## 3. Rate revision and which table applies

- **マイドームおおさか** prints two fee tables on one page: the current one and one headed 「（2027年4月1日以降）」, and its news page announces a conference-room rate revision for bookings starting on or after 2027-04-01. Both records use the **post-revision** amount (125,620 and 88,880 JPY 終日) because most of 2027 falls after the change; the pre-revision amounts (100,540 and 71,170) are recorded in `evidence.observed_facts` and each record carries a `final_quote` question. A January-March 2027 booking would be cheaper than the recorded figure.
- **大阪市中央公会堂** publishes a weekday base table and a printed 「土日祝は2割増」 multiplier. The Saturday amounts (118,080 and 60,240 JPY) are arithmetic on two printed numbers, not quoted Saturday rates; this is stated in both records.

## 4. Capacity basis and oversized halls

- 公会堂 中集会室 (500), 港区民センター ホール (400), 中央会館 ホール (250) and 大阪産業創造館 4F ホール (320/180) are all larger than a 50-person day. The scorer flags them `oversized_capacity`; the comfortable figure recorded is a conservative reading of the published layout, and each carries a `room_assignment` question about the flat-floor/chair configuration actually booked. None is a capacity claim at 50.
- 大阪市立総合生涯学習センター 第1研修室 (112 chairs-only / 87 with desks), 阿倍野 講堂 (150 chairs / 120 desks) and マイドーム 第1・第2 (100 school / 210 theatre) record the desk-seated figure, not the chair maximum.

## 5. Windows: 09:00 is the binding constraint

- Published openings: 09:30 for 公会堂, 総合生涯学習センター, 難波/阿倍野 講堂, 大阪産業創造館 and 港区民センター; 09:00 for エル・おおさか, マイドーム (午前 9-12時), 中央会館 (9:30 actually), 大阪カンファレンスセンター (9:00) and 大阪商工会議所 (8:00).
- Only **エル・おおさか** publishes an explicit 09:00-21:00 全日 band, which is exactly the 12-hour brief; **マイドームおおさか** publishes a 09:00-21:00 終日 band. Every 09:30 hall can still cover a 12-hour programme ending 21:30 but cannot start at 09:00 — that is carried as an `availability` question on each record rather than assumed.
- **大阪商工会議所** closes at 18:00 in its base-rate window, so the 12-hour brief is impossible there; the record is scored on an 8-hour day and the after-hours charge is an open question.

## 6. Alcohol, catering and network

- No venue page in this set publishes an alcohol permission for a rented hall. Every record carries an explicit licence question; 中央公会堂 中集会室 is the only page that describes catered parties as a use case, and 大阪カンファレンスセンター is the only one with in-house catering (お弁当・ドリンク等各種ご提供可能).
- Wi-Fi is confirmed only at **マイドームおおさか** (free wireless LAN service page). All other records carry `wifi_unknown` and a wifi question. 中央公会堂's downloads page mentions a Pocket Wi-Fi rental and a fixed-line option — not a room service, so it stays unknown.
- Screens/projectors are confirmed only where the operator prints installed or rentable equipment: マイドーム (75-inch monitor 16,500 JPY/day, projector 16,500, screen 1,650), 大阪産業創造館 4F ホール (200-inch projector), 大阪カンファレンスセンター (video projector + roll screen), 港区民センター (projector at extra charge), 中央会館 (projector 550 / screen 350 JPY per use).

## 7. Coordinates

- Eleven Nominatim bodies cover sixteen records (two or more rooms share one building point). Every coordinate pair in `venues.raw.json` is a JSON number copied from a saved response; the response file is named in `captures/INDEX.md` and the URL is in each record's `evidence.geo`.
- Six failed or superseded lookups are kept for the audit trail and are not used by any record: empty `geo_manabu_umeda.json`; `geo_namba.json`, which resolved 阿倍野市民学習センター instead of the Namba centre (the OCAT building body is used instead); `geo_minato2.json`, which resolved a different 港区民センター; `geo_minato3.json` (弁天町駅, a station); `geo_abeno2.json` (あべのベルタ building, superseded by the centre point); `geo_losaka2.json` (duplicate).
- エル・おおさか prints no street address on any captured page; its `address` field is null and the point comes from the building-name lookup (display name 石町二丁目). 港区民センター's address is recorded at quarter level (磯路一丁目) because the official pages print no block number.

## 8. Calendar gaps

- Verified from organiser pages: Japan IT Week / Japan DX & AX Week【関西】2027-11-17..19 (Intex Osaka), 大阪マラソン2027 on 2027-02-28 and 大阪マラソンEXPO2027 on 2027-02-26..27 (Intex 6号館), AI-ESS-16 on 2027-09-13..17 (Osaka, venue not printed).
- Unverified and therefore **not written as rows**: Tech Osaka Summit 2027 (2027-01-26..27, organiser host unreachable), Osaka Innovation Hub events (host unreachable), オープンソースカンファレンス2027 Osaka (2027-01-30 per an aggregator; organiser URL 404), ICAIIC 2027 (venue Osaka University printed, conference dates not printed), WebX 2027 (Tokyo, out of scope), VketReal in 関西 2027-01-23 (aggregator only, and not an AI/Web3 topic).
- No Japanese holiday date is asserted anywhere in this package; only the JP and JP:osaka registry rows are available for date context and no date ranker was run.

## 9. Communities

- Five of the thirteen records are `dormant` by the 12-month rule and are labelled as such; they are retained only because they are topically relevant historical leads. Three active-group member counts come from platform pages (connpass / gdg.community.dev) and are quoted, never estimated.
- みやこでIT is Kyoto-based. It is included as the Kansai Web3 channel with that limitation stated in the record, not as an Osaka-resident group.
- Only QUINTBRIDGE carries own-page co-hosting language. No co-host relationship is implied for any other group.
