# Kyoto Run A 2027 Q2 — raw-data evidence summary

Prepared by: jnr-research (KYO-RUNA-RESEARCH)
Research date: 2026-08-13
Working source of truth: installed skill `~/.hermes/skills/plan-event/` only.
Scope: raw data package only — no bundle, summary, recommendation, speaker
research, or commit (per plan Design B + review PASS).

## 1. Raw collections (all schema-valid exit 0)

| File | Kind | Records | Validator |
| --- | --- | --- | --- |
| city_input.json | city research input | 1 | (bundle_assembler consumes; not a validate_schema kind) |
| calendar_conflicts.json | calendar_conflict | 6 | PASS exit 0 |
| venues.raw.json | venue | 14 | PASS exit 0 |
| communities.raw.json | local_community | 6 | PASS exit 0 |
| source_uncertainty_notes.md | uncertainty log | — | — |
| venue_discovery_log.md | discovery/disposition | — | — |
| community_discovery_log.md | discovery/disposition | — | — |

Commands (all run from `~/repo_dev/coe-events/research/kyoto/2027-q2/`):

    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py calendar_conflict calendar_conflicts.json   # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py venue venues.raw.json                       # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py local_community communities.raw.json       # exit 0

## 2. Scorer reproducibility (byte-identical)

    python3 ~/.hermes/skills/plan-event/scripts/score_venues.py --output venues.shortlist.json \
      --budget-usd 5000 --target-attendance 50 --event-date 2027-04-03 --event-duration-hours 8 \
      venues.raw.json

- Run 1 exit 0; Run 2 exit 0; scorer logs byte-identical; shortlist outputs
  byte-identical (cmp PASS); SHA-256 of persisted scorer-owned
  venues.shortlist.json: `24cf67f6d9376c62a6860ece9d25615eaedc27946f30df8b8e7e2adbb2a0116f`
  (scorer_byte_identity.sha256).
- Result: eligible 0, shortlist_ready 10, lead 4.
- Shortlist_ready (top scores): Impact Hub Kyoto 2F Event Space 0.7069,
  kokoka Conference Rooms 1&2 0.6931, Kyoto Terrsa 中会議室 0.6666, Hearton 嵐山
  0.6339, Hearton 宇治伏見 0.6213, kokoka Event Hall 0.6013, Campus Plaza 第1会議室
  0.5403, Campus Plaza ホール 0.5388, Kyoto Univ. International Exchange Hall I
  0.5285, KRP Room 2 0.5176.
- Leads (score null, never selectable): KRP A/B/C Conference Rooms (school
  capacity 42 below 50 — material capacity question), ICC Kyoto (capacity/cost
  unknown), THE TERMINAL KYOTO (capacity/cost unknown), FabCafe Kyoto (capacity
  unknown).
- Persisted only scorer-owned `venues.shortlist.json` (no assembly/publish).

## 3. Calendar disposition (coverage 2027-03-15..2027-06-30, informational)

- 6 records, all `major_other` (relevance other, severity none): Golden Week
  2027 (Apr 29-May 5, Cabinet Office), cherry-blossom tourism peak (Kyoto City
  Official Guide), Aoi Matsuri May 15 (Kamigamo Shrine official), BitSummit
  2027 May 21-23 (official bitsummit.org), World Masters Games 2027 KANSAI
  May 14-30 (official wmg2027.jp + Kyoto City), June rainy season (JMA
  official).
- 0 `related` records retained: as of 2026-08-13 no 2027 Q2 Kyoto/Kansai
  AI/ML/data/web3/fintech/quant/DeAI/agent event has an official organizer page
  with published in-window dates — recorded as an explicit open question, never
  a false absence.
- All facts verified against official organizer/government pages (direct
  fetch or official-site snippet + corroboration where fetch was blocked).
- Calendar prose is date-neutral about Decentralized AI Day: the v2.9
  date-commitment family scan intent (no candidate-window, candidate-Saturday,
  coverage-window-range, or preferred-date phrasing in evidence fields) is
  satisfied — CLEAN on 2026-08-13 family scan.
- Adjacent-Q3 context notes (not records): Gion Matsuri (July 17/24), ACL 2027
  (Aug 17-22 Kyoto), IVS 2027 (recent early-July editions; not announced),
  ETHTokyo (Sep), PyCon JP/Kansai (later), Kyoto Marathon (Feb 21, before
  window), MLPR 2026 (Dec 2026, before window).

## 4. Venue disposition

- 14 retained records: 10 shortlist_ready, 4 lead.
- Impact Hub Kyoto (ih-052) is retained as a scored candidate, not a lead-only
  seed: its own current page (kyoto.impacthub.net/useourspace/) provides
  claim-bearing capacity (60-90), weekend pricing (JPY 72,000 tax-excl for
  9:00-17:00), free projector/PA, and a supported event window — satisfying the
  Budapest tv-02 / Boston ih-019 precedent for scoring above lead.
- Every retained venue: HTTPS source_url + accessed_on (2026-08-13),
  capacity/room/price-basis/screen/Wi-Fi/booking/window evaluated for an 8h
  09:00-17:00 event; unsupported material fields null + status + precise
  verification questions.
- All JPY costs preserve original amount/currency with the stated dated ECB
  conversion basis (2026-08-12) in evidence; no invented FX.
- Rejected/unresolved logged in venue_discovery_log.md (Miyako Messe oversized/
  no suitable public meeting-room page; hotel conference rooms without
  published 50-person rates; Doshisha/Ritsumeikan/KIT no public rental page;
  WeWork/platform listings discovery-only).

## 5. Community disposition

- 6 retained records: 2 active (GDG Kyoto, Kyoto University Blockchain Research
  Center), 2 intermittent (Kashima-Takeuchi Lab, Learning Machines Group),
  2 dormant (PyData Osaka, HN Kansai).
- cohost_open true ONLY for GDG Kyoto, backed by the chapter's own official
  page venue-provider solicitation language (quoted verbatim); every other
  record cohost_open false with no negative claim.
- contact_info null for all (only email/Slack/SNS routes visible; never
  inferred).
- Honest empty search recorded as community-research open questions in
  city_input.json: AI Tinkerers has no Kyoto/Osaka chapter; no standing Kansai
  quant community page; no public Kyoto University student AI/ML club page with
  activity; thin web3 landscape beyond BCK.

## 6. Source counts

- Calendar: 6 records; official sources include cao.go.jp (Cabinet Office),
  kyoto.travel (Kyoto City Official Guide), kamigamojinja.jp (Kamigamo Shrine),
  bitsummit.org, wmg2027.jp + city.kyoto.lg.jp + pref.kyoto.jp (WMG 2027),
  data.jma.go.jp (JMA).
- Venues: 14 records; official sources include kyoto.impacthub.net,
  kcif.or.jp (kokoka), kyoto-u.ac.jp (Clock Tower Centennial Hall),
  hearton.co.jp (Hearton Hotel Kyoto), kyoto-terrsa.or.jp (Terrsa),
  consortium.or.jp (Campus Plaza Kyoto), krp.co.jp (KRP), icckyoto.or.jp
  (ICC Kyoto), kyoto.theterminal.jp, fabcafe.com (FabCafe Kyoto).
- Communities: 6 records; official own pages include kyoto-gtug.org,
  blockchainkyoto.org, ml.ist.i.kyoto-u.ac.jp, lm.sys.i.kyoto-u.ac.jp,
  meetup.com/pydata-osaka, meetup.com/hacker-news-kansai (+ hnkansai.org).

## 7. FX conversion basis (stated, dated)

- ECB reference rate dated 2026-08-12 (EUR 1 = USD 1.1545; EUR 1 = JPY 183.67),
  fetched 2026-08-13; USD 1 = JPY 159.0905; 1 JPY = USD 0.00628573. Recorded
  per venue in evidence.observed_facts (and rate_estimate_note for the FabCafe
  rate-derived estimate). No invented FX; re-confirm at booking time.

## 8. Open questions for the reviewer / Joe

1. Related-event calendar is empty for 2027 Q2 because official 2027 pages are
   not yet published (IVS, ACL Aug, ETHTokyo, PyCon JP/Kansai); re-check closer
   to Q2 2027 — is a later calendar refresh desired?
2. Kyoto University Clock Tower external-eligibility: university facilities
   require permission and may not be open to a fully public community event —
   confirm whether an internal sponsor route exists.
3. Tax treatment: Impact Hub Kyoto published rates are tax-exclusive; kokoka's
   fee page does not state tax-inclusive — confirm the all-in totals.
4. Impact Hub Kyoto Wi-Fi in the event space is not explicitly confirmed.
5. KRP A/B/C school capacity is 42 (below 50); confirm the intended layout for
   a 50-person event.
6. Community gaps (AI Tinkerers Kyoto, Kansai quant, Kyoto student AI clubs,
   broader web3) are explicit open questions; no group was invented or assumed.
7. FX conversion basis is a 2026-08-12 point-in-time rate; re-confirm before
   booking.

## 9. Acceptance checklist

- [x] Every raw collection schema-valid exit 0 (calendar_conflict, venue,
  local_community)
- [x] Scorer reproducibility: byte-identical output on two runs (recorded,
  SHA-256 persisted)
- [x] Calendar prose passes the v2.9 date-commitment family scan intent (CLEAN)
- [x] Impact Hub Kyoto treated as seed (ih-052) with current claim-bearing
  evidence before scoring above lead; JPY costs with stated dated conversion
  basis; no invented FX
- [x] No bundle/summary/recommendation/speaker research/commit produced
