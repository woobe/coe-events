# FX evidence — Hong Kong (hong-kong-hk) research run, accessed 2026-11-28

## Source

- Publisher: European Central Bank, euro foreign exchange reference rates.
- Endpoint fetched: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`
- Access date: **2026-11-28** (UTC, 03:31). Saved capture: `captures/ecb_eurofxref_daily_2026-11-28.xml` (HTTP 200, 1,547 bytes).
- Reference date printed inside the file: **2026-11-27** (the ECB daily file carries the previous working day's rates).

## Rates used

- EUR 1 = **USD 1.0957**
- EUR 1 = **HKD 8.5774**

## Cross rate derived (and the one used in every venue record)

- USD 1 = 8.5774 / 1.0957 = **HKD 7.828238**
- 1 HKD = 1.0957 / 8.5774 = **USD 0.12774267** (stored to 8 decimal places)

Every `estimated_cost_usd` in `venues.raw.json` is `cost_local_amount × 0.12774267`, rounded half-up to two decimals. No other rate is used anywhere in the package.

## Three recomputations by hand (as required by the acceptance criteria)

1. **Garage Society Wan Chai**, 8 h at HK$3,200/hour: 8 × 3,200 = **HK$25,600**; 25,600 × 0.12774267 = 3,270.212 → **USD 3,270.21**. Reverse check: 3,270.21 / 0.12774267 = 25,599.9 HKD, i.e. inside one cent of rounding.
2. **TreeholeHK Wan Chai Room AB**, 8 h at HK$650/hour: 8 × 650 = **HK$5,200**; 5,200 × 0.12774267 = 664.262 → **USD 664.26**.
3. **Igather Central E&F hall**, published full-day rate: **HK$10,000**; 10,000 × 0.12774267 = 1,277.427 → **USD 1,277.43**.
4. (cross-check on the rate-derived LCSD record) **Ngau Chi Wan Civic Centre lecture room**, HK$360/hour × 8 h = **HK$2,880**; 2,880 × 0.12774267 = 367.899 → **USD 367.90**; the stored `hourly_rate_usd` is 45.98736 so that 45.98736 × 8 = 367.8989, inside the 0.01 tolerance.

## Conversion table used across the package

- HK$1,330 (Sheung Wan Civic Centre lecture hall, one 4-hour session) → **USD 169.90**
- HK$2,880 → **USD 367.90**
- HK$5,200 → **USD 664.26**
- HK$7,200 → **USD 919.75**
- HK$10,000 → **USD 1,277.43**
- HK$16,000 → **USD 2,043.88**
- HK$21,400 → **USD 2,733.69**
- HK$25,600 → **USD 3,270.21**

## Limits of this basis

- It is a dated published reference rate, not a live market rate and not a 2027 rate. It cannot predict the rate at booking time, and no 2027 event month is fixed.
- The ECB daily file lists only EUR crosses; the HKD→USD figure is a derived cross rate, derived here and recorded so it can be reproduced byte for byte.
- No other conversion (a bank card rate, a venue's USD invoice, a USD-pegged assumption) is used. The HKD is pegged within a band, but this package does not rely on the peg: it uses the ECB cross rate as published.
- Where a venue quotes tax-exclusive prices, the USD figure here is also tax-exclusive; the tax question is carried as a `final_quote` verification question on each such venue.
- Two Hong Kong venues print a bare `$`; see `city_input.json` currency assumptions and `source_uncertainty_notes.md`. Only Dream Impact is converted, and it carries a confirm-currency question.
