# Geneva Run A (2026 Q4) — venue discovery and disposition log

Research date: 2026-08-13. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. All HTTP fetches used a browser user
agent; web_extract is unavailable in this environment (search-only backend).

Disposition convention: RETAINED (schema-valid record in venues.raw.json),
REJECTED (examined, does not fit scope/evidence), UNRESOLVED (lead not
retained because evidence is incomplete or inaccessible this pass).

## Retained (9 records)

1. Impact Hub Geneva — Grand Salon (Rue Fendt 1, 1201 Genève)
   - Evidence: geneva.impacthub.net/en/spaces (CHF 950/4h, 90 m², 20-150) +
     /rooms/grand-salon/ (50 seated w/ chairs & tables, up to 120 chairs
     only, standing 150; big screen, flipcharts, high-speed WiFi, audio).
   - Cost: CHF 950/4h -> est. CHF 1,900/8h -> USD 2,338.08 (ECB 2026-08-13).
   - Tier: shortlist_ready (0.6631). Saturday booking + final quote open.
   - Source URLs: https://geneva.impacthub.net/rooms/grand-salon/ and
     https://geneva.impacthub.net/en/spaces/ (both fetched 2026-08-13).
2. Impact Hub Geneva — Petit Salon
   - Evidence: /en/spaces (CHF 550/4h, 40 m², 10-40 people).
   - Cost: CHF 550/4h -> est. CHF 1,100/8h -> USD 1,353.61 (ECB 2026-08-13).
   - Tier: lead (capacity 40 < 50 target; material capacity question).
3. Salle communale de Plainpalais — Salle des Assemblées (Rue de Carouge 52)
   - Evidence: geneve.ch/salle-communale-plainpalais + official 2024 tarif
     PDF (CHF 92/h 9h-19h, Lun-dim; 100 w/ tables, 150 chairs, 200 no
     furniture; prep/cleanup CHF 51/h min 1h before + after).
   - Cost: CHF 736/8h -> USD 905.69 (ECB 2026-08-13), + prep ~CHF 102.
   - Tier: shortlist_ready (0.5904). Screen/Wi-Fi, 2026 rates, municipal
     booking terms open.
4. Palexpo — Meeting Rooms E/F/G (Route François-Peyrot 30, Le Grand-Saconnex)
   - Evidence: palexpo.ch/en/meeting-rooms (E/F/G up to 120 theatre each,
     72 school, 40 boardroom; K 230, L 108; 800 m² foyer).
   - Cost: none published — quote-only. Tier: shortlist_ready (0.6067).
   - Note: scorer placed it shortlist_ready (core capacity evidenced, cost
     unknown is soft); written quote still required.
5. Hotel N'vY — Nolita / Sausalito (18 rue de Richemont, 1202 Genève)
   - Evidence: hotelnvygeneva.com/en/meeting-rooms (Nolita 70 m² up to 50;
     Sausalito 2x65 m² up to 110/50; foyer 60 m² up to 45).
   - Cost: none published — proposal required. Tier: shortlist_ready (0.5392).
6. Warwick Geneva — Mont-Blanc (14 Rue de Lausanne, 1201 Genève)
   - Evidence: warwickhotels.com Mont-Blanc page (max capacity 105, "modern
     audiovisual equipment").
   - Cost: none published. Tier: shortlist_ready (0.5392).
7. CERN Science Gateway — Auditorium / Globe (Esplanade des Particules 1,
   1217 Meyrin)
   - Evidence: visit.cern venue-rental PDF Jan 2025 (CHF 15,000-60,000/day;
     event days 8-24h; AV + 2 technicians included).
   - Cost: min CHF 15,000 -> USD 18,458.34 (ECB 2026-08-13) — far over soft
     budget. Tier: lead (over budget; Meyrin non-local conservatism).
8. Decentral House — Main Hall (Lancy-Pont-Rouge, Geneva)
   - Evidence: decentral.house/events (Main Hall up to 120 theatre, 4K
     projection, surround sound, live-streaming; boardroom 12).
   - Cost: none published — booking form. Tier: lead (location + cost open;
     exact street address unpublished).
9. Mövenpick Hotel & Casino Geneva — meeting floor
   - Evidence: movenpick.accor.com meeting-rooms + FAQ (19 meeting rooms,
     events up to 800 guests; no per-room small-room capacity published).
   - Cost: none published. Tier: lead (capacity + cost unknown).

## Rejected (examined, not retained)

- BFM (Bâtiment des Forces Motrices): Salle Théodore Turrettini 1,000+
  seats; Foyer up to 1,000 — oversized for a 50-person event; no sub-room
  rates published (bfm.ch/fr/location/).
- CICG (Centre International de Conférences Genève): up to 2,200
  participants, quote-based — oversized for a 50-person community event
  (cicg.ch).
- CIC (Cambridge Innovation Center): no Geneva location exists (cic.com
  redirects to the global locations page; Geneva is not listed).
- coworkinggeneva.ch "Event Space" page: platform/directory with aggregated
  "from CHF 450/day" rates (Centre Ville Auditorium up to 200, Plainpalais
  Loft up to 120, Carouge Workshop Hall up to 80, Eaux-Vives Lakeside Room up
  to 60) — the operating venue is not identified, so per evidence policy the
  platform's rates cannot support a venue record. Logged as a platform lead.
- SSPACE Genève (Geneva Business Center, Avenue des Morgines 12, Petit
  Lancy): contact-only page, no capacities/rates/rooms published.
- Salle communale de Plainpalais — Grande salle: 500 w/ tables (600 chairs,
  1,000 no furniture) — oversized for a 50-person event (the Salle des
  Assemblées record covers the fit).

## Unresolved (lead not retained this pass)

- Fongit (Campus Biotech B4, Chem. des Mines 9, 1202 Genève; HQ
  Plan-les-Ouates): active startup incubator that hosts events
  (café+croissant, investor days, FONGIT-Life) but publishes no venue-rental
  page or rates — verify whether Fongit rents space to external organizers.
- La Muse Bouge (Rue Jean-Charles Amat 6, 1202 Genève): associative
  coworking (Mon-Fri 09-18), membership-based; no event-space rental page —
  verify whether the coworking space is rentable for events.
- HPE Geneva Customer Innovation Center: hosts HPE Hackathon (14 Sep 2026
  per ai-weeks.ch) but no public venue-rental page found — verify.
- Geneva Network of Innovators / SDG Solution Space: hosted the AI Tinkerers
  Geneva inaugural meetup (2026-05-13); SDG Solution Space (Geneva) appears
  to host community events but has no public rental/rate page captured.

## Platform / directory leads (discovery only, not venue evidence)

- coworkinggeneva.ch (event-space directory, CHF 450-1,200/day ranges)
- workin.space / spacebase.com / tagvenue.com Geneva listings
- CAGI "Salles à Genève" venue catalog (International Geneva Welcome Centre
  PDF, cagi.ch) — used as a discovery index; capacities therein were
  re-verified against official venue pages before retention.
