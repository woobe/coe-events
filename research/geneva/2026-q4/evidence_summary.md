# Geneva Run A 2026 Q4 — raw-data evidence summary

Prepared by: jnr-research (GVA-RUNA-RESEARCH)
Research date: 2026-08-13
Working source of truth: installed skill `~/.hermes/skills/plan-event/` only.
Scope: raw data package only — no bundle, summary, recommendation, speaker
research, or commit (per plan Design B + review PASS).

## 1. Raw collections (all schema-valid exit 0)

| File | Kind | Records | Validator |
| --- | --- | --- | --- |
| city_input.json | city research input | 1 | (bundle_assembler consumes; not a validate_schema kind) |
| calendar_conflicts.json | calendar_conflict | 7 | PASS exit 0 |
| venues.raw.json | venue | 9 | PASS exit 0 |
| communities.raw.json | local_community | 6 | PASS exit 0 |
| source_uncertainty_notes.md | uncertainty log | — | — |
| venue_discovery_log.md | discovery/disposition | — | — |
| community_discovery_log.md | discovery/disposition | — | — |

Commands (all run from `~/repo_dev/coe-events/research/geneva/2026-q4/`):

    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py calendar_conflict calendar_conflicts.json   # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py venue venues.raw.json                       # exit 0
    python3 ~/.hermes/skills/plan-event/scripts/validate_schema.py local_community communities.raw.json       # exit 0

## 2. Scorer reproducibility (byte-identical)

    python3 ~/.hermes/skills/plan-event/scripts/score_venues.py --output venues.shortlist.json \
      --budget-usd 5000 --target-attendance 50 --event-date 2026-09-26 --event-duration-hours 8 \
      venues.raw.json

- Run 1 exit 0; Run 2 exit 0; `cmp` of the two outputs: BYTE-IDENTICAL.
- SHA-256: `8d0eb470a219ca723926bda94d67b5c9ef20f73238cfdc9c664fe5010a86a1dd`
  (recorded in scorer_byte_identity.sha256; score_run1.log/score_run2.log).
- Result: eligible 0, shortlist_ready 5, lead 4.
- Shortlist_ready: Impact Hub Geneva — Grand Salon (0.6631), Palexpo —
  Meeting Rooms E/F/G (0.6067), Salle communale de Plainpalais — Salle des
  Assemblées (0.5904), Hotel N'vY — Nolita/Sausalito (0.5392), Warwick
  Geneva — Mont-Blanc (0.5392).
- Lead: CERN Science Gateway (over soft budget, CHF 15k-60k/day), Decentral
  House (location + cost open), Impact Hub Geneva — Petit Salon (capacity 40
  < 50 target), Mövenpick Hotel & Casino Geneva (capacity + cost unknown).
- Persisted only scorer-owned `venues.shortlist.json` (no assembly/publish).

## 3. Calendar disposition (coverage 2026-09-15..2026-10-31, informational)

- 7 records: 2 `related`, 5 `major_other`.
- Related: Swiss IT Forum(s) 2026 (Sep 30-Oct 1, Palexpo, AI & Data/Web3
  forums; severity high), Geneva Hackathon 2026 / Swiss {ai} Weeks (Sep
  25-27, Giga Connectivity Centre, Campus Biotech; severity medium).
- Major_other: WTO Public Forum 2026 (Sep 15-17, IGO/diplomatic, 2,000+
  delegates), UN Human Rights Council 63rd session (Sep 7-Oct 9, Palais des
  Nations), AidEx 2026 (Oct 21-22, Palexpo, 3,400+ delegates), Bachata
  Geneva Festival (Oct 8-12, Palexpo, 70+ countries), MEGALLOWEEN 20 ans
  (Oct 31, Palexpo).
- All facts verified against official organizer pages (direct fetch on
  2026-08-13): swiss-it-forums.tech, palexpo.ch, ai-weeks.ch, wto.org,
  ohchr.org, aid-expo.com, bachatagenevafestival.com.
- Calendar prose is date-neutral about Decentralized AI Day: the v2.9
  date-commitment family scan (exact rules v1: PE29-DATE-001..004) found 0
  findings on calendar evidence/inference/verification_questions — CLEAN.
- Adjacent context only (never in-window assertions, documented in
  source_uncertainty_notes.md): Fête de Genève (August), Geneva Digital
  Week / AI for Good / Global Dialogue on AI Governance (Jul 6-10), ECCB
  2026 / #GenevaLovesData (Aug 31-Sep 4), Generali Genève Marathon (May
  9-10), GDC26 (Sep 1-3), IGF 2026 consultations (Sep 7-9), HPE Hackathon
  (Sep 14). Geneva AI Summit 2027 referenced only as 2027 context.

## 4. Venue disposition

- 9 retained records: 5 shortlist_ready, 4 lead (tiers from the deterministic
  scorer; scorer-owned venues.shortlist.json).
- Impact Hub Geneva (ih-038) is a Tier-1 trusted resolver match AND a scored
  candidate: its own current pages (spaces page, Grand Salon room page,
  online booking system) support capacity (50 seated w/ tables), screen
  (big screen), WiFi (high-speed), and the CHF 950/4h published rate —
  unlike the Boston ih-019 "Coming Soon" case. Saturday availability and
  final quotes remain verification questions (shortlist_ready, not eligible).
- Every retained venue: HTTPS source_url + accessed_on (2026-08-13),
  capacity/room/price-basis/screen/Wi-Fi/booking/window evaluated for an 8h
  09:00-17:00 event; unsupported material fields null + status + precise
  verification questions.
- CHF costs with stated dated conversion basis (ECB 2026-08-13: EUR 1 =
  USD 1.1534; EUR 1 = CHF 0.9373; 1 CHF = 1.230556 USD). No invented FX.
- Rejected/unresolved logged in venue_discovery_log.md (BFM + CICG
  oversized, CIC no Geneva location, coworkinggeneva.ch platform rates
  unsupported, SSPACE contact-only, Fongit + La Muse Bouge no rental pages,
  HPE CIC + SDG Solution Space unresolved).

## 5. Community disposition

- 6 retained records: 4 active (AI Tinkerers Geneva, Decentral House,
  Open Geneva, Geneva Network of Innovators/ge-ni), 2 intermittent (Geneva
  AI/Mindstone, GDG Geneva), 0 dormant.
- cohost_open true ONLY for Geneva Network of Innovators (ge-ni), backed by
  its own page's explicit co-organization language ("The event is co-
  organised with the AI Tinkerers, Bengoo AI, and the Young AI leaders");
  needs_human_verify true + question. Every other record cohost_open false
  with no negative claim.
- contact_info null for all (only email/form/organizer-button routes
  visible; never inferred).
- Honest empty search recorded as community-research open questions in
  city_input.json (no PyData Geneva chapter — nearest is Lausanne; Genève R
  User Group page "Group not found"; no standing Geneva quant group; Crypto
  Valley/Zug and swissAI are Swiss-national adjacency, not Geneva records).

## 6. Source counts

- Calendar: 7 records; verified official sources: swiss-it-forums.tech,
  palexpo.ch (agenda + AidEx event page), ai-weeks.ch, wto.org, ohchr.org,
  aid-expo.com, bachatagenevafestival.com.
- Venues: 9 records; official sources: geneva.impacthub.net (+ booking
  system geneva.impacthub.ch), geneve.ch (+ municipal tarif PDF),
  palexpo.ch, visit.cern (venue-rental PDF), hotelnvygeneva.com,
  warwickhotels.com, movenpick.accor.com, decentral.house. Discovery index:
  CAGI "Salles à Genève" catalog (cagi.ch PDF).
- Communities: 6 records; official own pages: geneva.aitinkerers.org,
  community.mindstone.com, mindstone.beehiiv.com, decentral.house,
  opengeneva.org, meetup.com/gdg-geneva, ge-ni.ch.
- FX: ECB eurofxref-daily.xml (2026-08-13) fetched directly.

## 7. Open questions for the reviewer / Joe

1. Impact Hub Geneva's stated reception hours are Monday-Friday 9h-19h;
   Saturday event-space availability must be confirmed via the event-space
   form before the Grand Salon can move from shortlist_ready to eligible.
2. Salle communale de Plainpalais tarif is dated 2024; current 2026 rates,
   screen/Wi-Fi inventory, and municipal booking terms (association status,
   deposit) need confirmation.
3. Hotel/convention venues (Palexpo, N'vY, Warwick, Mövenpick, Decentral
   House) are inquiry-only; written quotes are required before any cost
   claim above published/estimated status.
4. CERN Science Gateway is over budget (CHF 15k-60k/day) and in Meyrin;
   retained only as an awareness lead per the plan's conservative
   non-local rule.
5. Community landscape is thin on own-page 2026 activity evidence beyond the
   retained 6; PyData Geneva, Genève R User Group, and standing Geneva
   quant/web3 groups are explicit community-research open questions.
6. FX: the ECB 2026-08-13 reference is a dated published basis, not a live
   market rate; re-confirm at booking time.

## 8. Acceptance checklist

- [x] Every raw collection schema-valid exit 0 (calendar 7, venue 9,
      local_community 6)
- [x] Scorer reproducibility: byte-identical output on two runs (recorded,
      SHA-256 8d0eb470…)
- [x] Calendar prose passes the v2.9 date-commitment family scan intent
      (exact rules v1 scan: 0 findings)
- [x] Impact Hub Geneva treated as seed + scored candidate only on current
      claim-bearing own-page evidence; CHF costs with stated dated ECB
      conversion basis; no invented FX
- [x] No bundle/summary/recommendation/speaker research/commit produced
