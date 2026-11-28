# FX evidence — Kyoto (kyoto-jp) research run, accessed 2026-11-28

## Source

- Publisher: European Central Bank, euro foreign exchange reference rates.
- Endpoint fetched: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`
- Access date: **2026-11-28** (UTC). Saved capture: `captures/ecb_eurofxref_daily_2026-11-28.xml` (HTTP 200, 1,547 bytes).
- Reference date printed inside the file: **2026-11-27** (the daily file carries the previous working day's rates; 28 November 2026 is a Saturday).

## Rates used

- EUR 1 = **USD 1.0957**
- EUR 1 = **JPY 174.81**

## Cross rate derived (and the one used in every venue record)

- USD 1 = 174.81 / 1.0957 = **JPY 159.541845**
- 1 JPY = 1.0957 / 174.81 = **USD 0.00626795** (stored to 8 decimal places)

Every `estimated_cost_usd` in `venues.raw.json` is `cost_local_amount × 0.00626795`, rounded half-up to two decimals. No other rate is used anywhere in the package.

Rounding check against the records (2026-11-28, round-3 pass): fifteen of the sixteen priced figures are the strict half-up two-decimal value of that product. The sixteenth, KRP ルーム2 at JPY 128,700 × 0.00626795 = 806.685165, is recorded as **USD 806.68**, one cent below the strict half-up value of 806.69 — a cent-level truncation. It is left as recorded rather than re-scored: a one-cent change moves no tier, score, ranking or budget test (USD 806.68 vs 806.69 against a USD 5,000 ceiling), and the card pins the delivered shortlist hash.

## Three recomputations by hand (as required by the acceptance criteria)

1. Heartpia Kyoto 第5会議室, published 午前・午後 (09:00-17:00) rate: **JPY 22,390**; 22,390 × 0.00626795 = 140.3378 → **USD 140.34**. Reverse check: 140.34 × 159.541845 = 22,390.6 JPY, i.e. within 1 JPY of the printed rate.
2. kokoka Event Hall, Saturday 09:00-17:00 = JPY 30,300 (morning) + 44,200 (afternoon) = **JPY 74,500**; 74,500 × 0.00626795 = 466.9623 → **USD 466.96**.
3. Miyako Messe 大会議室, 午前・午後 package: **JPY 31,570**; 31,570 × 0.00626795 = 197.8791 → **USD 197.88**.
4. (cross-check on an hourly record) Kyoto University 国際交流ホール, holiday hourly rate **JPY 10,700**; 10,700 × 0.00626795 = 67.0671 → hourly USD 67.067; × 8 hours = 536.536 → **USD 536.54**.

## Conversion table used across the package

- JPY 18,220 → USD 114.20 (Asny 第3研修室, 午前 + 午後)
- JPY 22,390 → USD 140.34 (Heartpia 第5会議室)
- JPY 25,130 → USD 157.51 (Asny 第2研修室)
- JPY 27,100 → USD 169.86 (kokoka Seminar Room)
- JPY 27,600 → USD 173.00 (kokoka Conference Rooms 1+2)
- JPY 31,570 → USD 197.88 (Miyako Messe 大会議室)
- JPY 32,200 → USD 201.83 (Rekisaikan 小ホール, Saturday two-block rate)
- JPY 49,500 → USD 310.26 (Heartpia 大会議室)
- JPY 69,800 → USD 437.50 (kokoka Special Conference Room)
- JPY 74,500 → USD 466.96 (kokoka Event Hall)
- JPY 79,940 → USD 501.06 (Heartpia 大会議室, 終日 09:00-21:00)
- JPY 84,000 → USD 526.51 (Hearton 嵐山, 7-8 hours)
- JPY 128,700 → USD 806.68 (KRP ルーム2, weekend 全日)
- JPY 134,000 → USD 839.91 (Hearton 宇治伏見, 7-8 hours)
- JPY 150,000 → USD 940.19 (Elcient Room B, 7-hour special + 1 overtime hour)
- JPY 50,600 → USD 317.16 (Miyako Messe 大会議室, 09:00-21:00)
- JPY 44,000 → USD 275.79 (FabCafe 8-hour rate estimate)

## Limits of this basis

- It is a dated published reference rate, not a live market rate and not a 2027 rate. It cannot predict the rate at booking time, and the 2027 event month is not fixed.
- The ECB daily file lists only EUR crosses; the JPY→USD figure is a derived cross rate, derived here and recorded so it can be reproduced exactly.
- No other conversion (a bank's card rate, a venue's USD invoice, a booking-platform rate) is assumed. Where a venue quotes tax-exclusive prices, the USD figure here is also tax-exclusive and the tax question is carried as a `final_quote` verification question on that venue.
