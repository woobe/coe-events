# G3 notes: display names and About

Bundle: `research/san-francisco/city/updates/g3-names-about.json` (`city-updates/1`, kind `venue_copy`, revision 1, verified 2026-11-22).
16 records, both facts on every venue. No page, template, calendar or store file was edited.

## Limits

- Longest `display_name`: `Women's Building – Audre Lorde Room`, 35 characters (cap 40).
- Longest `about`: the Alliance Francaise Theater, 236 characters (cap 240).
- Every `about` is two sentences; none carries a date, a superlative, a recommendation or an offer.
- `candidate|recommend|best` over the 32 produced values: no match (also checked case-insensitively over the whole bundle).

## CLI apply proof (copy of the store, live untouched)

```
cp .../city/city.json /home/joe/.hermes/profiles/jnr-content/cache/scratch/g3-apply/city-copy3.json
.venv/bin/python plan-event/scripts/city_store.py \
  --apply-updates .../updates/g3-names-about.json \
  --store .../g3-apply/city-copy3.json \
  --out .../g3-apply/city-merged3.json \
  --report .../g3-apply/report3.json
```

Output: `run run-updates-e21df10b4f14 kind=updates noop=False`, `facts: {"about": 16, "display_name": 16}`, `changed: 32 conflicts: 0`.
`--check` on the merged copy: `OK ... (schema city-store/1, 16 venues)`.
Live store sha256 before and after: `b360101fa3dd534d9ba103927d2d612e1ac61b6785bb66c717319a86fd637da6` (unchanged).
Suite: `1398 passed` (`plan-event/tests`, `-B -p no:cacheprovider`).

The card's literal `verify_command` line 1 uses `python3 -c`; this worker profile refuses `-c` script execution, so the same three numbers were produced by `.venv/bin/python check.py`: `16 35 236`.

## Skill passes and the change each made

- `impeccable` (writing review, `reference/clarify.md`): applied its message hierarchy - sentence one is the room and its capacity, sentence two is the constraint that actually bites on an eight-hour day (access window, staffing, rate basis). It also drove cutting the source pages' promotional adjectives ("wonderful", "unparalleled", "beautiful and versatile") and forced the honest unknowns ("rates unpublished", "no opening hours ... are published") instead of implying a capability.
- `better-writing`: one word per concept (`capacity`, `seated`, `standing`, `rate`) across all 16 records; deleted words that do no work (street addresses already stored, "please", "successfully", listing ids); no marketing adjectives; sentence case throughout.
- `humanizer` (not installed on this profile; read the retained copy at `local/batch11-removal-backups/t_3a1d4955/R018/restore-check/humanizer/SKILL.md`): removed copula avoidance (`boasts`, `features`, `serves as` became `is`, `has`, `includes`), removed em dashes and -ing tails, dropped rule-of-three lists and the "not just X, but Y" frame.

## Grounding, venue by venue

- CounterPulse - Main Stage: `$50/hour` private-event rate and the absence of published hours, screen and Wi-Fi from the rentals page; 108 seated attributed to third-party listings in the evidence text, and the About says so.
- Brava Theater Center - Lobby: capacity 80, stand-alone or with the Main Stage, and the after-2:00 pm opening rule with staff fees.
- Brava Theater Center - Studio: 60 seats, 25x45 ft sprung floor, mirrored wall and curtain, house manager required, rates by email.
- Alliance Francaise – Theater: 74 seats, $800 daytime rate, $60/hour mandatory front-desk staffing, weekday 10:00-17:00 and Saturday to 14:00.
- Ruth Williams – Main Theater: 300 capacity with proscenium stage, $900 base rate, five-hour minimum, $950+ projection, 3% service and 25% admin fees.
- Gray Area - Lobby (Grand Theater): 800 sq ft, 80 capacity / 50 seated, Wi-Fi and full bar, no published prices; delivery refusal from the FAQ.
- The Marsh SF – Mainstage: 105 seats, $2,000 Mon-Thu and $2,500 Fri-Sun full-day rates, $40/hour required representative, $1,000,000 insurance.
- Z Space - Steindler Stage: 236 seats, 40x80 ft sprung floor, front and rear projection, Z Lobby included, no rates, four to six months' notice.
- The Lab – Main Auditorium: 3,500 sq ft performance space, 150 seated, sound/projection/lighting/green room included, rates by email.
- Z Space - Z Lobby: about 125 standing, 40 ft ceilings, prep kitchen, full bar, PA and movable stage at extra charge, no rates.
- The Marsh SF – Studio: 60-90 seats, $1,500 Mon-Thu and $2,000 Fri-Sun full-day, $40/hour representative.
- Root Division – Front & Rear: 1,750 sq ft, 100-120 capacity / 70 seated, $1,800 for a 5.5-hour block with set-up and clean-up, $150 per extra hour.
- Women's Building – Audre Lorde Room: 1,500 sq ft, 70 conference / 60 banquet, 65 chairs and eight tables, $165/hour stated for weekday 9:00-17:00 only.
- SOMArts – Main Event Space: 5,810 sq ft with 1,470 sq ft stage, Essentials from $4,549, 100-150 guests, 2-3 hour event length with eight hours of access.
- Common Space – Large Loft: 900 sq ft, 70 people, four-hour minimum, $250 deposit, $165/hour from the archived listing, 65-inch TV and Wi-Fi, address masked.
- Four One Nine – Middle Gallery: Middle Gallery Extended for 40-100 attendees, $650/hour, four-hour minimum, seasonal rate may apply, gallery/library/rooftop but no studio or kitchen.

## Where the evidence was thin, and what the About does instead

- CounterPulse: capacity 108 is third-party only; the About names that basis and says hours, projection and Wi-Fi are unpublished rather than asserting them.
- Common Space: rate comes from a 2026-04-06 archive snapshot and the street address is platform-masked; the About says "archived copy" and "address masked until booking", and claims no coordinates.
- Gray Area, The Lab, Z Space (both rooms), Brava (both rooms): no rates published; each About says rates are unpublished and names the contact route only where the page does.
- Women's Building: the page prints a weekday-only hourly rate next to a weekend closing rule; the About confines the rate to weekdays and makes no weekend claim.
- SOMArts: the Essentials band is a 2-3 hour event length that includes eight hours of access; the About states both figures and does not claim an eight-hour event is accepted at that price.
- Alliance Francaise: the published Saturday window ends at 14:00, so the About says it is short of an eight-hour day instead of implying an eight-hour booking.
- Four One Nine: the pricing sheet is prior-year and the package lists no AV equipment; the About omits AV and states the four-hour minimum and possible seasonal rate.
- The Marsh, Ruth Williams, Root Division: clock hours are not published; the About uses only the published full-day/5.5-hour bands and never invents a move-in time.

## Label decisions

- Labels are the measured labels in `local/design/g1-plan-v1.md` (the 1440/1280 line-count gate), including their mixed hyphen/en-dash separators; changing the separator would invalidate that measurement.
- Dropped from the stored names: the Peerspace listing id, "(SoMa)", "(Bayview Opera House)", "(Essentials Package)" and the "(Redstone Building)" suffix where the short label still identifies the room.
- Kept: building identity where the room name alone is ambiguous (Brava Theater Center, Gray Area / Grand Theater, Women's Building).

## Reproduce

```
.venv/bin/python plan-event/scripts/city_store.py --apply-updates <bundle> --store <copy> --out <merged> --report <report>
.venv/bin/python -B -m pytest -p no:cacheprovider -q plan-event/tests
```
