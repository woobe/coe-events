# Seoul Run A (2026 Q4) — dated FX / conversion evidence capture

Research/access date: 2026-08-15. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. This file is a local research artifact;
nothing here is a recommendation, elimination, or date commitment.

## 1. Primary rate source (direct fetch)

- ECB euro foreign exchange reference rates, daily XML:
  https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml
- Fetched 2026-08-15 via curl (HTTP 200). The published Cube date is
  **2026-08-14** (the last ECB working-day reference before the fetch date).
- Relevant Cube entries:
  - `EUR 1 = USD 1.1567`
  - `EUR 1 = KRW 1632.42`
- Local copy of the fetched XML preserved at research time:
  `/tmp/ecb_daily.xml` (this run's scratch copy; not a deliverable).

## 2. Derived cross rate

- 1 KRW = USD (1.1567 / 1632.42) = **0.0007085798997806937 USD**
- Rounded for display and per-amount calculation: **1 KRW = USD 0.0007085799**
- Equivalently: **1 USD = 1411.2735 KRW** (1632.42 / 1.1567)
- Calculation basis: USD per KRW = (EUR per USD inverse applied) = EUR→USD
  rate divided by EUR→KRW rate. No FX rate is invented; the basis is the
  dated ECB reference pair above.

## 3. Converted amounts used in this package (all at the 2026-08-14 basis)

| Item | KRW | USD (0.0007085799/KRW) |
| --- | --- | --- |
| Nodeul Island Livehouse — Saturday performance rental, 1회 (공연 1회/일, VAT excluded) | 4,000,000 | 2,834.32 |
| Nodeul Island Livehouse — Saturday performance rental, 2회 (공연 2회/일, VAT excluded) | 6,000,000 | 4,251.48 |
| DDP Conference Hall (414 m²) — 2026 high-season daily rate (성수기 1.1, Sep/Oct) | 3,907,330 | 2,768.66 |
| DDP Art Hall 2 (1,547 m²) — 2026 high-season daily rate (성수기 1.1, Sep/Oct) | 14,600,580 | 10,345.68 |
| Mongsang Space Mullae — weekend hourly rate (주말 99,000원/h, Fri/holiday incl.) x 8h | 792,000 | 561.20 |

Notes:
- All amounts above are the venue's own published KRW figures (see venue
  records and venue_discovery_log.md for source URLs and accessed_on).
- DDP daily rates are VAT-inclusive (부가세 포함) per the official notice;
  Nodeul and Mongsang rates are VAT-excluded (VAT 별도) per their pages.
- The 09:00-17:00 8-hour window assumption: for hourly venues (Mongsang) the
  published weekend rate is applied linearly to 8 hours; for daily-rate venues
  (Nodeul performance rental, DDP) the published daily/Saturday rate is the
  figure used and the 8-hour-window applicability is a verification question.

## 4. Uncertainty

- The ECB 2026-08-14 reference is a dated published basis, not a live market
  rate and not a predictor of the 2026 Q4 rate. Re-confirm the conversion
  basis at booking time.
- No KRW amount was converted without this dated basis; every converted
  venue keeps its KRW amount in cost_local_amount and the USD equivalent in
  estimated_cost_usd with the rate_estimate_note citing this capture.
- Venues with no published rate (COEX, DDP Design Hall, KT&G SangSangMadang,
  hotels, coworking chains) keep estimated_cost_usd null with a
  confirm-cost question (cost_unknown soft kind; never invented).
