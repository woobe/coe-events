# Seoul Run A 2026 Q4 — raw-data evidence summary

Prepared by: jnr-research (SEOU-RUNA-RESEARCH)
Research date: 2026-08-15
Working source of truth: installed skill `~/.hermes/skills/plan-event/` only.
Scope: raw data package only — no bundle, summary, recommendation, speaker
research, or commit (per plan Design B + review PASS).

## 1. Raw collections (all schema-valid exit 0)

| File | Kind | Records | Validator |
| --- | --- | --- | --- |
| city_input.json | city research input | 1 | (bundle_assembler consumes; not a validate_schema kind) |
| calendar_conflicts.json | calendar_conflict | 7 | PASS exit 0 |
| venues.raw.json | venue | 6 | PASS exit 0 |
| communities.raw.json | local_community | 10 | PASS exit 0 |
| fx_evidence_2026-08-15.md | FX/evidence capture | — | — |
| source_uncertainty_notes.md | uncertainty log | — | — |
| venue_discovery_log.md | discovery/disposition | — | — |
| community_discovery_log.md | discovery/disposition | — | — |

Commands (all run from `~/repo_dev/coe-events/research/seoul/2026-q4/`):

    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py calendar_conflict calendar_conflicts.json   # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py venue venues.raw.json                       # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py local_community communities.raw.json       # exit 0

## 2. Scorer reproducibility (byte-identical)

    python3 ~/.hermes/skills/plan-event/scripts/score_venues.py --output venues.shortlist.json \
      --budget-usd 5000 --target-attendance 50 --event-date 2026-09-26 --event-duration-hours 8 \
      venues.raw.json

- Run 1 exit 0; Run 2 exit 0; `cmp` of the two score logs: BYTE-IDENTICAL
  (score_run1.log / score_run2.log identical).
- SHA-256: `32e6eeec5cdbeae4d7ed7b59a5b457a6ed378063d249f3bdf02e96f1c85c3fca`
  (recorded in scorer_byte_identity.sha256; venues.shortlist.json).
- Result: eligible 0, shortlist_ready 4, lead 2.
- Shortlist_ready: Mongsang Space — Main Hall (0.6876), COEX — Conference
  Room 300 (0.53), DDP — Design Hall (0.53), Nodeul Island — Livehouse
  (0.2599).
- Lead: DDP — Conference Hall (capacity material gap; priced KRW 3,907,330
  high-season daily), KT&G SangSangMadang Hongdae — Live Hall (capacity +
  location material gaps).
- Persisted only scorer-owned `venues.shortlist.json` (no assembly/publish).

## 3. Calendar disposition (coverage 2026-09-15..2026-12-15, informational)

- 7 records: 4 `related`, 3 `major_other`.
- Related: Korea Blockchain Week 2026 (Sep 29 - Oct 1, Walkerhill Hotels &
  Resorts; web3/high), GWDC 2026 Korea (Sep 29-30, aT Center; web3/medium),
  Korea Fintech Week 2026 (Nov 25-27, aT Center; fintech/low), COMEUP 2026
  (Dec 9-11, COEX; ai/low).
- Major_other: Chuseok 2026 (Sep 24-26; mass domestic travel, closures),
  National Foundation Day (Oct 3 + observed Oct 5; office/bank closures),
  Hangeul Day (Oct 9; office/bank closures).
- All facts verified against official sources where possible (direct fetch
  on 2026-08-15): koreablockchainweek.com, gwdc.net, english.visitkorea.or.kr,
  fsc.go.kr (press-release PDF), comeup.org + third-party factual dates for
  COMEUP 2026 (JS-rendered official shell; dates from mhnet.kr /
  ntradeshows.com / neventum.com, stored as third-party factual dates).
- Chuseok 2026 (Sep 24-26) VERIFIED from the official VISITKOREA public
  holidays page — do not assume "early October"; the official page places it
  in late September 2026.
- KBW 2026 (Sep 29 - Oct 1) VERIFIED from the official organizer page
  (koreablockchainweek.com) — not assumed from the "typically Sep" pattern.
- Calendar prose is date-neutral about Decentralized AI Day: no
  scheduling-window, candidate-date, or preferred-date phrasing is stated
  anywhere in calendar records.
- Adjacent context only (documented in source_uncertainty_notes.md): World
  Knowledge Forum (Sep 8-10), Try Everything 2026 (Sep 9-10), Seoul
  International Fireworks Festival (Sep 5), AI Summit Seoul & Expo (Aug
  19-21), Bitcoin Seoul (Jun 4-5), 2026 Blockchain Meetup Conference (Mar
  12) — all outside the coverage window.

## 4. Venue disposition

- 6 retained records: 4 shortlist_ready, 2 lead (tiers from the
  deterministic scorer; scorer-owned venues.shortlist.json).
- Impact Hub Seoul DOES NOT EXIST: installed `references/impact_hub_locations.json`
  (150 records) has 0 Seoul/Korea/KR entries, and the live
  impacthub.net/locations page lists no Seoul location. No hub seed, no
  fabricated resolver match — documented as an explicit finding.
- Every retained venue: HTTPS source_url + accessed_on (2026-08-15),
  capacity/room/price-basis/screen/Wi-Fi/booking/window evaluated for an 8h
  09:00-17:00 event; unsupported material fields null (or 0 + `unknown`
  capacity basis per schema) + status + precise verification questions.
- KRW costs with stated dated conversion basis (ECB 2026-08-14: EUR 1 =
  USD 1.1567; EUR 1 = KRW 1632.42; 1 KRW = 0.0007085799 USD). No invented
  FX. Nodeul Livehouse KRW 6,000,000 -> USD 4,251.48; DDP Conference Hall
  KRW 3,907,330 -> USD 2,768.66; Mongsang base 8h KRW 792,000 -> USD 561.20.
- Rejected/unresolved logged in venue_discovery_log.md (COEX Auditorium
  oversized; DDP Art Hall 1/2 over budget; Lotte Executive rooms too small;
  ST Center unreachable; aT Center WAF-blocked; WeWork/Hyatt 403; Fastfive/
  SparkPlus JS-only rates; Seoul Startup Hub JS-rendered).

## 5. Community disposition

- 10 retained records: 6 active (AI Tinkerers Seoul, GDG Seoul, AWSKRUG,
  Modulabs, PyLadies Seoul, Korea R User Group), 4 intermittent (Seoul
  Ethereum Meetup, Ethereum Seoul Community, Superteam Korea, PyTorch
  Korea), 0 dormant.
- cohost_open true ONLY for 3 records with same-page language: AI Tinkerers
  Seoul ('sponsored by PostHog and DanaIX'), AWSKRUG (sponsor/venue-sponsor
  section), Korea R User Group (donation/sponsorship language, flagged
  conservatively); each needs_human_verify true + question.
- contact_info set only for AWSKRUG (awskr.org, visibly referenced on the
  same official page); all other records null (email/form routes refused).
- Korea's Web3 market is a DISCOVERY HYPOTHESIS: this pass retained only
  own-page-evidenced Seoul web3 groups (Seoul Ethereum Meetup, Ethereum
  Seoul Community, Superteam Korea), honestly labeled; no market claim.
- Honest empty search recorded as community-research open questions in
  city_input.json (no standing Seoul quant community page; no Startup Grind
  Seoul chapter page with observed activity; WAI Korea is a company in
  Ansan, not a Seoul community).

## 6. Advisory prose probe (non-blocking)

    python3 ~/.hermes/skills/plan-event/scripts/prose_consistency_probe.py \
      --input venues.raw.json --kind venue \
      --report prose-consistency-seoul-2026-q4.json \
      --generated-at 2026-08-15 --quarter 2026-q4 --city seoul

- Exit 0 (advisory; never the blocking release scanner).
- Report: `prose-consistency-seoul-2026-q4.json` (generated_at 2026-08-15).
- finding_count: match 0, mismatch_candidate 0, ambiguous_candidate 7,
  insufficient_evidence 7, ignored 0.
- Ambiguous candidates are expected advisory noise on this raw package:
  capacity prose (e.g., 'about 110 people', '20-300 pax') is
  configuration-ambiguous, and the FX-basis sentence embedded in
  observed_facts contains the numeric '0.0007085799' which the probe reads
  as a rate-like token. No `mismatch_candidate` (no structured-vs-prose
  contradiction) was found. These are reviewable advisory records, not
  blockers; the same advisory class appeared in prior city raw packages
  (Geneva 11 ambiguous / 18 insufficient).
- The release scanner (scan_event_output.py) is NOT run at research stage —
  it belongs to the rollout stage.

## 7. Open questions for the reviewer / Joe

1. Impact Hub Seoul does not exist in the installed snapshot or live global
   locations — confirm no hub seed should be added and no resolver change is
   needed for Seoul.
2. aT Center and ST Center are real, active Seoul venues but could not be
   captured via curl this pass (JS challenge / connection timeout); a
   browser-capable fetch or the venues' sales desks are required before they
   can become scored candidates.
3. COEX, DDP Design Hall, KT&G SangSangMadang, and all hotel/coworking
   candidates are inquiry-only; written quotes are required before any cost
   claim above published/estimated status.
4. Nodeul Livehouse's published performance start is 10:00; the assessed
   09:00-17:00 window's start needs confirmation. The venue is also
   oversized (456-708) for a 50-person event.
5. Community landscape: no standing Seoul quant community page, no Startup
   Grind Seoul chapter page with observed activity, and no additional
   standing Seoul data-science meetup beyond the retained groups surfaced
   this pass — recorded as explicit open questions, not absence claims.
6. FX: the ECB 2026-08-14 reference is a dated published basis, not a live
   market rate; re-confirm at booking time.
7. COMEUP 2026 dates (Dec 9-11) are third-party factual dates pending the
   official JS-rendered site publishing its 2026 edition page.

## 8. Acceptance checklist

- [x] Every raw collection schema-valid exit 0 (calendar 7, venue 6,
      local_community 10)
- [x] Scorer reproducibility: byte-identical output on two runs (recorded,
      SHA-256 32e6eeec…)
- [x] KRW preserved first; every USD conversion has a dated ECB 2026-08-14
      basis and reproducible calculation (fx_evidence_2026-08-15.md)
- [x] Impact Hub Seoul absence verified; no fabricated hub assertion
- [x] Calendar facts verified against official sources where possible;
      Chuseok 2026 and KBW 2026 dates VERIFIED, not assumed; date-neutral
      prose throughout
- [x] Advisory prose probe run with pinned generation date 2026-08-15,
      exit 0, report saved
- [x] No bundle/summary/recommendation/speaker research/commit produced
