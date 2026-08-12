# Boston Run A 2026 Q4 — raw-data evidence summary

Prepared by: jnr-research (BOS-RUNA-RESEARCH)
Research date: 2026-08-12
Working source of truth: installed skill `~/.hermes/skills/plan-event/` only.
Scope: raw data package only — no bundle, summary, recommendation, speaker
research, or commit (per plan Design B + review PASS).

## 1. Raw collections (all schema-valid exit 0)

| File | Kind | Records | Validator |
| --- | --- | --- | --- |
| city_input.json | city research input | 1 | (bundle_assembler consumes; not a validate_schema kind) |
| calendar_conflicts.json | calendar_conflict | 12 | PASS exit 0 |
| venues.raw.json | venue | 11 | PASS exit 0 |
| communities.raw.json | local_community | 10 | PASS exit 0 |
| source_uncertainty_notes.md | uncertainty log | — | — |
| venue_discovery_log.md | discovery/disposition | — | — |
| community_discovery_log.md | discovery/disposition | — | — |

Commands (all run from `~/repo_dev/coe-events/research/boston/2026-q4/`):

    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py calendar_conflict calendar_conflicts.json   # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py venue venues.raw.json                       # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py local_community communities.raw.json       # exit 0

## 2. Scorer reproducibility (byte-identical)

    python3 ~/.hermes/skills/plan-event/scripts/score_venues.py --output venues.shortlist.json \
      --budget-usd 5000 --target-attendance 50 --event-date 2026-09-26 --event-duration-hours 8 \
      venues.raw.json

- Run 1 exit 0; Run 2 exit 0; `cmp` of the two outputs: BYTE-IDENTICAL.
- Result: eligible 0, shortlist_ready 4, lead 7.
- Shortlist_ready: MIT Samberg Conference Center — Conference I (0.701),
  The Foundry — Performance Space (0.529), The Foundry — Red Multi (0.529),
  CIC Cambridge — Venture Café (0.47).
- Persisted only scorer-owned `venues.shortlist.json` (no assembly/publish).
- The scorer flag set is deterministic and correct for the evidence: every
  retained venue carries needs_human_verify true; Workbar is a lead only
  because its exact location is a material open question (no single address
  evidenced on the official page).

## 3. Calendar disposition (coverage 2026-09-15..2026-12-15, informational)

- 12 records: 7 `related`, 5 `major_other`.
- Related: Boston AI Week 2026, Boston Fintech Week 2026, EmTech Future 2026,
  RoboBoston 2026, DahShu Data Science Symposium 2026, Generative AI Summit
  Boston 2026, Nxt AI-2026.
- Major_other: MIT Future Fest 2026, Head of the Charles Regatta 2026,
  Boston Book Festival 2026, B.A.A. Boston Half 2026,
  Harvard Square Oktoberfest 2026.
- All facts verified against official organizer pages (direct fetch or
  official-site snippet + corroboration where the site blocked fetch).
- Calendar prose is date-neutral about Decentralized AI Day: the v2.9
  date-commitment family scan intent (no scheduling-window, candidate-date,
  or preferred-date phrasing) is satisfied on all calendar records — CLEAN.
- Explicitly NOT recorded: Boston Blockchain Week 2026 (Sep 8-10, before the
  Sep 15 coverage start; noted in source_uncertainty_notes.md as an adjacent
  event), ODSC AI East (spring), EmTech AI (spring), JSM (Aug 1-6), ETHBoston
  (2019 stale).

## 4. Venue disposition

- 11 retained records: 4 shortlist_ready (Samberg Conference I, Foundry x2,
  CIC Venture Café), 7 lead (Impact Hub Boston seed, WPI Seaport, Workbar,
  Artisan's Asylum, Harvard i-lab, MassRobotics, Emmanuel Parish Hall).
- Impact Hub Boston (ih-019) is retained as a DISCOVERY SEED / lead only: its
  official page says "Coming Soon" / new location, so no capacity/cost/screen/
  Wi-Fi/availability claim is supported (Budapest tv-02 precedent).
- Every retained venue: HTTPS source_url + accessed_on (2026-08-12),
  capacity/room/price-basis/screen/Wi-Fi/booking/window evaluated for an 8h
  09:00-17:00 event; unsupported material fields null + status + precise
  verification questions.
- Rejected/unresolved logged in venue_discovery_log.md (Greentown Labs
  Cloudflare-blocked, The Engine, WeWork generic pages, NEU/BU internal venues,
  BCEC/Hynes oversized).

## 5. Community disposition

- 10 retained records: 7 active (AI Tinkerers Boston, PyData Boston, Boston
  FinTech, CryptoMondays Boston, MIT Sloan AI & ML Club, HDSI, Boston Python),
  2 intermittent (ODSC AI Boston, LangChain Boston), 1 dormant (Boston
  Blockchain Association).
- cohost_open true ONLY for AI Tinkerers Boston, backed by the chapter's own
  sponsors page venue-partner language; every other record cohost_open false
  with no negative claim.
- contact_info null for all (only email/form routes visible; never inferred).
- Honest empty search recorded as community-research open questions in
  city_input.json (AI Salon Boston chapter not found; NEU/BU student groups not
  found with own-page activity; MIT undergrad clubs beyond Sloan not found).
- MIT/Harvard/Northeastern landscape covered via MIT Sloan AI & ML Club, HDSI,
  and explicit open questions where no own-page evidence existed.

## 6. Source counts

- Calendar: 12 records; verified official sources include aiweek.boston,
  bostonfintechweek.org, technologyreview.com/all-events, massrobotics.org,
  2026.dahshu.org, world.aiacceleratorinstitute.com, nxtai-conference.com,
  hocr.org, bostonbookfest.org, baa.org, harvardsquare.com.
- Venues: 11 records; official sources include boston.impacthub.net,
  scheduling.mit.edu (Samberg fees PDF), cambridgefoundry.org, districthallboston.org,
  cic.com, workbar.com, artisansasylum.com, innovationlabs.harvard.edu,
  massrobotics.org, tagvenue.com (platform lead for Emmanuel Parish Hall).
- Communities: 10 records; official own pages include boston.aitinkerers.org,
  boston.pydata.org, meetup.com/boston-fintech, meetup.com/crypto-mondays-boston,
  meetup.com/boston-data-mining, sloangroups.mit.edu/aiml/home/,
  datascience.harvard.edu, meetup.com/boston-blockchain-association,
  meetup.com/bostonpython, luma.com/iaie4h2x.

## 7. Open questions for the reviewer / Joe

1. Boston Blockchain Week 2026 (Sep 8-10, Quincy) precedes the calendar
   coverage start (Sep 15); retained only as an adjacent-event note — confirm
   whether Joe wants it promoted into the calendar collection.
2. Venue rates are overwhelmingly inquiry-only in Boston; written quotes are
   required before any cost claim above published/estimated status.
3. Impact Hub Boston's new space launch timing is unannounced; verify closer
   to the event whether the hub is bookable at all.
4. Samberg requires an MIT DLC sponsor for external organizations and a $3,500
   weekend F&B minimum — confirm whether a sponsoring MIT contact is available.
5. Community landscape beyond the retained 10 is thin on own-page activity
   evidence; AI Salon Boston and NEU/BU student groups are explicit
   community-research open questions.

## 8. Acceptance checklist

- [x] Every raw collection schema-valid exit 0
- [x] Scorer reproducibility: byte-identical output on two runs (recorded)
- [x] Calendar prose passes the v2.9 date-commitment family scan intent
- [x] Impact Hub Boston treated as seed, not suitability proof
- [x] No bundle/summary/recommendation/speaker research/commit produced
