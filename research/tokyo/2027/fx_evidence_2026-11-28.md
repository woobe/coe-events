# FX evidence — Tokyo (tokyo-jp) research run, accessed 2026-11-28

## Source

- Publisher: European Central Bank, euro foreign exchange reference rates.
- Endpoint fetched: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`
- Access date: **2026-11-28** (UTC). Saved capture: `captures/ecb_eurofxref_daily_2026-11-28.xml` (HTTP 200, 1,547 bytes).
- Reference date printed inside the file: **2026-11-27** (the ECB publishes the previous working day's rates in the daily file).

## Rates used

- EUR 1 = **USD 1.0957**
- EUR 1 = **JPY 174.81**

## Cross rate derived (and the one used in every venue record)

- USD 1 = 174.81 / 1.0957 = **JPY 159.541845**
- 1 JPY = 1.0957 / 174.81 = **USD 0.00626795** (stored to 8 decimal places)

Every `estimated_cost_usd` in `venues.raw.json` is `cost_local_amount × 0.00626795`, rounded half-up to two decimals. No other rate is used anywhere in the package.

## Three recomputations by hand (as required by the acceptance criteria)

1. Shinjuku i-Town, 8 h weekend 2027 rate: JPY 10,000/h × 8 = **JPY 80,000**; 80,000 × 0.00626795 = 501.436 → **USD 501.44**. Reverse check: 501.44 × 159.541845 = 80,000.7 JPY, i.e. the rounding is within 1 JPY.
2. Otemachi Place カンファレンス103, 09:00–17:00 block: **JPY 161,000**; 161,000 × 0.00626795 = 1,009.140 → **USD 1,009.14**.
3. Tokyo International Forum G402, 09:00–17:00 block: **JPY 138,600**; 138,600 × 0.00626795 = 868.738 → **USD 868.74**.
4. (cross-check on the 12-hour figures quoted inside venue evidence) Otemachi Place 全日 09:00–21:00: **JPY 230,000** → **USD 1,441.63**; AICC 301 09:00–17:00 + 4 × 67,000 = **JPY 668,000** → **USD 4,186.99**.

## Conversion table used across the package

- JPY 80,000 → USD 501.44
- JPY 8,100 → USD 50.77 (Minato 研修室1 午前+午後 blocks)
- JPY 90,000 → USD 564.12
- JPY 110,400 → USD 691.98 (Palette六本木 8 h × 13,800)
- JPY 120,000 → USD 752.15 (12-hour hourly equivalents)
- JPY 129,000 → USD 808.57
- JPY 138,600 → USD 868.74
- JPY 161,000 → USD 1,009.14
- JPY 168,800 → USD 1,058.03
- JPY 204,000 → USD 1,278.66
- JPY 230,000 → USD 1,441.63
- JPY 288,200 → USD 1,806.42
- JPY 400,000 → USD 2,507.18

## Limits of this basis

- It is a dated published reference rate, not a live market rate and not a 2027 rate. It cannot predict the rate at booking time, and the 2027 event month is not fixed.
- The ECB daily file lists only EUR crosses; the JPY→USD figure is a derived cross rate, derived here and recorded so it can be reproduced byte for byte.
- No other conversion (for example a bank's card rate or a venue's USD invoice) is assumed. Where a venue quotes tax-exclusive prices, the USD figure in this package is also tax-exclusive; the tax question is carried as a `final_quote` verification question on each such venue.
