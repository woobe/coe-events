# FX evidence — Osaka (osaka-jp) research run, accessed 2026-11-28

## Source

- Publisher: European Central Bank, euro foreign exchange reference rates.
- Endpoint fetched: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`
- Access date: **2026-11-28** (UTC). Saved capture: `captures/ecb_eurofxref_daily_2026-11-28.xml` (HTTP 200, 1,547 bytes).
- Reference date printed inside the file: **2026-11-27** (`<Cube time='2026-11-27'>`; 28 November 2026 is a Saturday, so the daily file carries the previous working day's rates).

## Rates used

- EUR 1 = **USD 1.0957**
- EUR 1 = **JPY 174.81**

## Cross rate derived (and the one used in every venue record)

- USD 1 = 174.81 / 1.0957 = **JPY 159.5418**
- JPY 1 = 1.0957 / 174.81 = **USD 0.00626795** (stored to 8 decimal places)

Every `estimated_cost_usd` in `venues.raw.json` is `cost_local_amount × 0.00626795`, rounded half-up to two decimals. No other rate is used anywhere in the package. The soft budget of USD 5,000 corresponds to about JPY 797,709 at this basis.

## Three recomputations by hand (as required by the acceptance criteria)

1. マイドームおおさか 第1・第2会議室, published 終日 9-21時 on the post-2027-04-01 table **JPY 125,620**; 125,620 × 0.00626795 = 787.3802 → **USD 787.38**. Reverse check: 787.38 / 0.00626795 = 125,619.4 JPY, within 1 JPY of the printed rate.
2. 大阪産業創造館 6F 会議室E, published weekend 終日 9:30-21:30 **JPY 31,100**; 31,100 × 0.00626795 = 194.9332 → **USD 194.93**. Reverse check: 194.93 / 0.00626795 = 31,099.5 JPY.
3. 港区民センター 第1集会室, published holiday 全日 9:30-21:30 **JPY 10,680**; 10,680 × 0.00626795 = 66.9417 → **USD 66.94**.
4. (cross-check on the one rate-derived estimate) 大阪商工会議所 2号会議室, published general holiday **JPY 19,800/hour** = 124.1053 USD/h; × 8 hours = **USD 992.84**, and 158,400 × 0.00626795 = 992.8434 → USD 992.84.

## Conversion table used across the package

- JPY 10,680 → USD 66.94 (港区民センター 第1集会室, holiday 全日)
- JPY 31,100 → USD 194.93 (大阪産業創造館 会議室E, weekend 終日)
- JPY 40,000 → USD 250.72 (エル・おおさか 9012, 全日 9-21)
- JPY 41,880 → USD 262.50 (中央会館 ホール, holiday 全日)
- JPY 46,680 → USD 292.59 (阿倍野市民学習センター 講堂, 土日祝 全日)
- JPY 50,520 → USD 316.66 (港区民センター ホール, holiday 全日)
- JPY 51,840 → USD 324.93 (総合生涯学習センター 第1研修室; 難波市民学習センター 講堂, Saturday 全日)
- JPY 57,200 → USD 358.53 (エル・おおさか 708, 全日)
- JPY 60,240 → USD 377.58 (中央公会堂 小集会室, Saturday = 50,200 × 1.2)
- JPY 70,700 → USD 443.14 (大阪産業創造館 4F イベントホール, weekend 終日)
- JPY 88,880 → USD 557.10 (マイドームおおさか 第3会議室, post-2027-04-01 終日)
- JPY 118,080 → USD 740.12 (中央公会堂 中集会室, Saturday = 98,400 × 1.2)
- JPY 125,620 → USD 787.38 (マイドームおおさか 第1・第2会議室, post-2027-04-01 終日)
- JPY 158,400 → USD 992.84 (大阪商工会議所 2号会議室, 8 h at 19,800/h)

## Limits of this basis

- It is a dated published reference rate, not a live market rate and not a 2027 rate. It cannot predict the rate at booking time, and no 2027 event month is fixed.
- The ECB daily file lists only EUR crosses; the JPY→USD figure is a derived cross rate, derived here and recorded so it can be reproduced exactly.
- Where a venue quotes tax-exclusive prices (マイドームおおさか prints amounts 税込; 大阪産業創造館 prints 消費税込; 中央公会堂 prints 税込), the USD figure inherits that basis. The two Saturday-multiplier amounts (中央公会堂 中/小集会室) are arithmetic on two printed numbers, not quoted Saturday rates.
- No bank rate, card rate, venue USD invoice or booking-platform rate is assumed anywhere.
