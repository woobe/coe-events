# Geneva Run A (2026 Q4) — community discovery and disposition log

Research date: 2026-08-13. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. Discovery layer per
`references/community_sources.md` (AI Tinkerers chapters, PyData/RUG
networks, Web3 Events Guide, Crypto Events Global, open city search) plus
direct web search; every retained record was verified against the group's own
official page.

Disposition convention: RETAINED (schema-valid local_community record in
communities.raw.json), REJECTED (examined, does not meet locality/own-page/
activity evidence rules), UNRESOLVED (candidate found but evidence
inaccessible or incomplete this pass).

## Retained (6 records)

1. AI Tinkerers Geneva — active (ai/machine_learning)
   - Own page: geneva.aitinkerers.org (organizers Ilia & Sajad; 252-city
     network; 3-hour demo format). Inaugural Geneva meetup 2026-05-13 at SDG
     Solution Space (ge-ni.ch co-organizer page corroborates).
   - cohost_open false (chapter /sponsors page 403 to direct fetch; no
     own-page partnership language captured).
2. Geneva AI (Mindstone) — intermittent (ai)
   - Own pages: community.mindstone.com/events/geneva_ai_november_28
     ("Unavailable" at fetch; BIRD, 1214 Vernier; free, 200 spots) +
     mindstone.beehiiv.com/p/geneva-ai-meetup-jan25-follow-up (Feb 2025
     meetup at Voisins Plainpalais; Feb 27 2025 follow-up).
   - 2026 cadence unconfirmed -> intermittent + verification question.
3. Decentral House — Community Hub — active (ai/web3)
   - Own page: decentral.house (+ events page, + luma.com/DecentralHouse
     calendar). 100+ founders; hosts Onchain Leaders Gathering; AI/FinTech/
     Web3 focus in Lancy-Pont-Rouge. Also retained as a venue record.
   - cohost_open false (no explicit external co-host language observed).
4. Open Geneva — active (mixed)
   - Own page: opengeneva.org. Nonprofit; 6,000+ community; 140+ hackathons
     since 2018; UN-recognized hackathons; Geneva-based.
   - cohost_open false (partner-ecosystem language, no external co-host
     application path observed).
5. GDG Geneva — intermittent (ai/data_science)
   - Own page: meetup.com/gdg-geneva. 55 members; Genève CH; "particular
     focus on AI and Data products"; no upcoming events at fetch.
6. Geneva Network of Innovators (ge-ni) — active (ai/mixed), cohost_open
   TRUE
   - Own page: ge-ni.ch/ai-tinkerers-meetup + ge-ni.ch. Explicit own-page
     co-organization language: "The event is co-organised with the AI
     Tinkerers, Bengoo AI, and the Young AI leaders". May 13, 2026 meetup at
     SDG Solution Space. needs_human_verify true + question.

## Rejected (examined, not retained)

- PyData Geneva: does not exist — nearest chapter is PyData Lausanne
  (meetup.com/pydata-lausanne), ~60 km away. Not a Geneva locality.
- Swiss AI / swissAI (swissai.ch): Swiss national AI user association,
  German-first, Zürich-based Geschäftsstelle; no Geneva locality evidence —
  adjacency, not a Geneva record.
- Crypto Valley (Zug): blockchain ecosystem hub in Zug, not Geneva —
  adjacency documented honestly, never claimed as Geneva locality.
- GenevaLovesData / SIB Swiss Institute of Bioinformatics: life-science data
  initiative/institute (Geneva-headquartered, ECCB 2026 partner) — an
  institute and a campaign, not a standing community group; context only.
- Geneva Internet Platform (GIP / DiploFoundation): digital-policy platform
  operated by Diplo, supported by Canton/Republic of Geneva — policy
  platform, not a local community meetup; context only.
- Women-in-tech / UN-agency communities: no Geneva own-page community record
  with observed activity was captured this pass (evidence gap, not absence).

## Unresolved (candidates found, evidence inaccessible/incomplete)

- Genève R User Group (meetup.com/geneve-r-user-group): "Group not found" at
  fetch; an R-community index lists a "Genève Data Analytics Group"
  (481 members) — could not be verified on an own page this pass. Quant/data
  adjacency: RUG network has no Geneva listing in the Pro directory found.
- Geneva FinTech / web3 beyond Decentral House: no standing Geneva
  web3/DeFi meetup with own-page activity evidence surfaced (Crypto Valley
  events are Zug; "Geneva Blockchain Connection" appears only as an icoholder
  directory listing with no verifiable organizer page).
- Standing Geneva quant community: no public own-page group found — recorded
  as an explicit community-research open question in city_input.json, never
  as a false absence.
- AI Tinkerers Geneva /sponsors and /events subpages: HTTP 403 (WAF) to
  direct fetch — fall 2026 schedule and venue-partner language unverified.

## Notes

- contact_info is null for all retained records (only email/form/organizer-
  button routes visible; email is refused by policy; no inferred routes).
- member_size_public only where displayed on the group's own page
  (Decentral House 100+, Open Geneva 6,000+, GDG Geneva 55); null elsewhere.
- Honest empty search results are recorded as explicit open questions in
  city_input.json (PyData Geneva absent, Genève RUG unverifiable, no standing
  Geneva quant/web3 group) — never "deferred to Run B", never a false
  absence claim.
