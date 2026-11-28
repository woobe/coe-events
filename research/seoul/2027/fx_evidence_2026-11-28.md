# FX evidence — Seoul (seoul-kr) research run, accessed 2026-11-28

## Source

- Publisher: European Central Bank, euro foreign exchange reference rates.
- Endpoint fetched: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`
- Access date: **2026-11-28** (UTC). Saved capture: `captures/ecb_eurofxref_daily_2026-11-28.xml` (HTTP 200, 1,547 bytes).
- Reference date printed inside the file: **2026-11-27** (the daily file carries the previous working day's rates; 28 November 2026 is a Saturday).

## Rates used

- EUR 1 = **USD 1.0957**
- EUR 1 = **KRW 1462.65**

## Cross rate derived (and the one used in every venue record)

- USD 1 = 1462.65 / 1.0957 = **KRW 1334.9001**
- 1 KRW = 1.0957 / 1462.65 = **USD 0.00074912** (stored to 8 decimal places)

Every `estimated_cost_usd` in `venues.raw.json` is `cost_local_amount × 0.00074912`, rounded half-up to two decimals. No other rate is used anywhere in the package. The soft budget of USD 5,000 corresponds to about KRW 6,674,501 at this basis.

## Three recomputations by hand (as required by the acceptance criteria)

1. DDP Design Hall, published one-day (11-hour) rate **KRW 3,256,000**; 3,256,000 × 0.00074912 = 2,439.1347 → **USD 2,439.13**. Reverse check: 2,439.13 / 0.00074912 = 3,255,994 KRW, i.e. within 6 KRW of the printed rate.
2. 판교 경기창조경제혁신센터 대회의실, published full-day (08:00-17:00, VAT included) **KRW 264,000**; 264,000 × 0.00074912 = 197.7677 → **USD 197.77**. Reverse check: 197.77 / 0.00074912 = 263,999 KRW.
3. 노들섬 라이브하우스, published weekend one-performance rate (VAT excluded) **KRW 4,000,000**; 4,000,000 × 0.00074912 = 2,996.48 → **USD 2,996.48**.
4. (cross-check on a rate estimate) COCOC 컨퍼런스룸 A, published hourly **KRW 176,000** = 131.84512 USD/h; × 8 hours = 1,054.76096 → **USD 1,054.76**.

## Conversion table used across the package

- KRW 264,000 → USD 197.77 (판교 대회의실, full day)
- KRW 120,000 → USD 89.89 (마로니에공원 다목적홀, 8 h at 15,000 KRW/h)
- KRW 440,000 → USD 329.61 (몽상가들 서브 세미나룸, 8 h at 55,000 KRW/h)
- KRW 1,346,000 → USD 1,008.32 (노들섬 노들라운지, weekend day, VAT excluded)
- KRW 1,408,000 → USD 1,054.76 (COCOC 컨퍼런스룸 A, 8 h at 176,000 KRW/h)
- KRW 2,420,000 → USD 1,812.87 (COCOC 대강당, published 9-hour package)
- KRW 2,640,000 → USD 1,977.68 (판교 국제회의장, full day)
- KRW 2,651,000 → USD 1,985.92 (DDP 서울-온 화상스튜디오, day)
- KRW 2,988,000 → USD 2,238.37 (DDP 잔디사랑방, day)
- KRW 3,256,000 → USD 2,439.13 (DDP 디자인홀, day)
- KRW 4,000,000 → USD 2,996.48 (노들섬 라이브하우스, weekend, VAT excluded)

## Limits of this basis

- It is a dated published reference rate, not a live market rate and not a 2027 rate. It cannot predict the rate at booking time, and the 2027 event month is not fixed.
- The ECB daily file lists only EUR crosses; the KRW→USD figure is a derived cross rate, derived here and recorded so it can be reproduced exactly.
- No other conversion (a bank's card rate, a venue's USD invoice, a booking-platform rate) is assumed. Where a venue quotes VAT-excluded prices — DDP (tax statement not printed), 노들섬 (`VAT 별도`), 마로니에공원 (VAT 10% separate) — the USD figure here is also tax-excluded and the tax question is carried as a `final_quote` verification question on that venue.
