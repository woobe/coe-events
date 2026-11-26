# Round-2 remediation — San Francisco revision-1 store

Card `t_f9db5e38`, reviewer round 1 returned four fixes. Store before this pass:
1,217,727 B, sha256 `41e3bde9…347b`. Store after: 1,259,462 B, sha256
`57f757cc674e258e32910db94a91bdb9af078db8b06c6ca802429d6739edc523`; `city_store.py --check`
OK (city-store/1, 16 venues); `build_ranking(store, "2026-11-26")` = 14 rows + 2 leads, ids
identical to the store; whole-store loss check clean; strict revision-1 scratch render
1,802,218 B.

## 1. Stale AFSF access blocker (reader-facing)

- Cause: `venues.sf-307c9dd57430.blockers[0]` (claim `cl-a3f0b7215cf1`, verified 2026-11-20)
  still said "published window ends at 14:00; 4 hour cap for a 8-hour programme", while the
  refreshed row stores `booking_hour_cap: 8` and a Sunday 09:00–17:00 band.
- Fix: blockers are now derived from the resolved field
  `venues.<id>.fields.programme_windows.value["8"].state` at build time. A blocker is produced
  only when that state is `"no"`; the text is generated from the claim's own `basis` and the
  claim id is minted from the generated text, so no hand-typed cap can survive a re-derivation.
- Result: AFSF's 8-hour state is `"yes"` (Sunday 09:00–17:00) → zero blockers produced, the
  legacy blocker is withdrawn and dispositioned in `runs[…].retired_claims`. No venue has an
  8-hour state of `"no"`, so no blocker is produced city-wide. Re-render prints one `8 h cap`
  in the AFSF cell (verified by parsing the rendered row; the only `4 h cap` left in the HTML
  is a CSS comment in the stylesheet).
- Log: `fix2/round2-log.json.blocker_derivation`.

## 2. California state-holiday evidence

- 9 of 18 US-CA rows had no locator carrying the date. All 18 now carry the Government Code
  6700 subdivision locator copied from the pinned registry (`plan-event/references/
  school_holidays.json`, read 2026-11-20), plus a `court_check` line and an explicit
  `statute_read` note that leginfo returned HTTP 403 on 2026-11-26.
- The full SF Superior Court 2027 list (15 closures) is reconciled row by row in the new
  coverage entry `coverage[US-CA|public_holiday_coverage|2027-01-01]`: 9 court closures match a
  stored statute row exactly; 6 do not and are now stored as US-CA public rows —
  Farmworkers Day 2027-04-09, Juneteenth 2027-06-18, Thanksgiving 2027-11-25, Day After
  Thanksgiving 2027-11-26, Christmas 2027-12-24, New Year's Day 2028 on 2027-12-31. The last
  two of the six also cite the DGS OAH 2027 tentative state list.
- Replaced the wrong late-year coverage assertion (it named Christmas and New Year only) with
  the corrected text naming Day After Thanksgiving and the observed dates; all US-CA coverage
  rows and rows are re-dated `reconciled_on: 2026-11-26`, `accessed_on: 2026-11-26`.
- Counts after: 24 US-CA public rows (18 statute + 6 court), 36 local public rows, 7 school
  rows, 43 local rows, 42 intersecting 2027, 70 coverage rows, 362 holiday rows total
  (43 local + 25 other US scopes + 294 foreign countries).

## 3. Loss check scope and claim ids

- The refreshed event evidence entries now carry claim ids minted by the canonical
  `city_store._claim(event_id, "evidence", [observed_facts, inference], verified_at, url)`.
- The 9 replaced evidence entries are retained under `events.<id>.history.evidence` with
  `retired_on: 2026-11-26` and a `disposition` naming the replacement claim id.
- The 6 RSA Conference claims are listed in
  `runs[run-20261126-sf-r1-refresh].retired_claims` with the drop reason; the 6 new event
  evidence claim ids are `cl-fb2ba4245d2d`, `cl-f81f62597321`, `cl-6f5677ea41a8`,
  `cl-b2f4bbb54f3c` (one per retained event).
- The whole-store check (`report.json.loss_check`) compares HEAD's 416 unique claim ids with
  the refreshed store: 0 absent unexplained. It is labelled whole-store, not venue-only.

## 4. Event totals and runs ledger

- `event-matrix.json` totals are 54 cells, 48 read, 6 blocked (AI Tinkerers × six themes), 82
  pages read, 4 retained, 1 dropped. The report, this note and the handoff now use those
  numbers; the earlier "51 read / 3 blocked" came from the handoff text, not the matrix.
- `run-20261126-sf-r1-refresh` is appended to `store.runs` with the refresh date, input
  digests (registry, court text, DGS OAH, DGS OHR, OPM tables, event matrix, HEAD pre-image),
  the retired-claim ledger and the blocker-derivation record.

## Non-blocking items also addressed

- `declared_gaps`: every entry now carries `checked_on: 2026-11-26` and refs in a resolvable
  keyed form (`holidays[US-CA|public_holiday|2027-11-26]`,
  `coverage[US-CA|public_holiday_coverage|2027-01-01]`, `runs[…]`, `venues.<id>.fields.<name>`,
  `photos.<id>[i]`, evidence-relative paths). A resolver ran over all refs; 0 unresolved.
- The state-holiday gap text now states the full reconciliation instead of "differs on four
  points".
- SOMArts (sf-b3be38e30978) stays `floor_only`: 8 hours by duration line, no clock, so it is
  not counted as a shorter clock window.
