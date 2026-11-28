# Community discovery log — Seoul 2027 deep refresh, 2026-11-28

Method: 4 community-specific searches plus the 23 venue/district and 10 calendar searches (37 bundle-wide, as declared in `venue_discovery_log.md`), then a direct fetch of each surviving group's own page. Directories and aggregators (lu.ma discover, Meetup search, koreahackathons.com, ethereum.org events, irlevents, cryptocop) were discovery-only and are never used as final evidence.

## Queries — community-specific (4)

1. lu.ma Seoul AI meetup community 2026
2. lu.ma Seoul web3 crypto meetup 2026
3. GDG Korea Seoul meetup 2026 일정
4. 모두의연구소 모두콘 2026 일정 AI 커뮤니티

## Calendar searches run in the same sweep (10)

Korea Blockchain Week 2027 dates Seoul · ETH Seoul 2027 hackathon date · AI EXPO KOREA 2027 일정 코엑스 · 서울패션위크 2027 일정 개최 · World IT Show 2027 일정 코엑스 · Seoul Meta Week 2027 일정 · Upbit D Conference UDC 2027 일정 · 한국전자전 KES 2027 일정 코엑스 · 코리아핀테크위크 2027 일정 · 서울 스마트시티 엑스포 2027.

## Retained — 14 records in `communities.raw.json`

- 1. 모두의연구소 (Modulabs) — **active** — MODUCON 2026 on 2026-12-12 at Ewha Womans University ECC; free seminars and cohort programmes
- 2. 파이토치 한국 사용자 모임 (PyTorchKR) — **active** — KVCache Meetup Korea 2026-09-30 at 드림플러스 강남; PyTorch DeepDive 2026-11-22 at 스페이스쉐어 하모니홀
- 3. AI Tinkerers Seoul — **active** — next event listed as 2026-12-31 (New Year's Eve demo night)
- 4. GDG on Campus Dongguk University — **active** — Hangang Picnic Meetup 2026-05-08
- 5. GDG Korea WebTech — **intermittent** — 1,163 members; organiser meetup is the newest listed event, no 2026 date rendered
- 6. GDG Campus Korea — **dormant** — 727 members; newest past event 2020
- 7. Seoul AI Meetup — **dormant** — 318 members; newest past event 2025-03-20
- 8. SeoulWeb3 — **dormant** — 534 members; newest past event 2023-04-27 despite a stated monthly cadence
- 9. 한국블록체인협회 (KBCA) — **dormant** — notice board's newest visible items are 2023
- 10. 서울 AI 허브 — **intermittent** — city-backed support hub; programme text, no dated public event on the captured page
- 11. AI Network — **intermittent** — AI+blockchain project site, © 2026 footer, no dated event
- 12. 디센터 (Decenter) — **intermittent** — daily news dated 2026-11-27; digital-first, no in-person cadence
- 13. Hashed (Hashed Lounge / EastPoint:Seoul) — **intermittent** — describes the annual Hashed Potato Club, EastPoint:Seoul and a Worldcoin meetup at Hashed Lounge, but publishes no dates
- 14. ETH Seoul (KryptoSeoul · Ludium · Dystopia Labs) — **dormant** — newest edition found is 2024-03-29..31 at Neowiz Pangyo Tower

## Disposition notes

- **No co-host badge anywhere.** `cohost_open` is false on all 14 records because no group's own page carries quotable co-host or venue-partnership solicitation language. Hashed is the closest to a host route (it already runs a lounge and co-hosts EastPoint:Seoul) but the page is descriptive, not an invitation.
- **Activity status follows the evidence, not the group's reputation.** Three large groups (GDG Campus Korea 727, Seoul AI Meetup 318, SeoulWeb3 534) are recorded dormant because their own pages stop in 2020, 2025-03 and 2023-04 respectively.
- **Digital-first records are labelled.** 디센터 and AI Network have dated publishing activity but no in-person cadence, so they are intermittent with `typical_venue: null` and no in-person claim.
- **Contact routes** are public HTTPS pages only — no email addresses, phone numbers or private handles appear in `contact_info`.
- Communities not carried after review: Seoul iOS Meetup (Apple platforms, not AI/Web3), OWASP Korea (security), GDG Seoul (Meetup page returns 'Group not found'), KryptoSeoul (DNS failure, so no capture), 리벨리온/업스테이지 (companies, not communities), D.CAMP (site 404 at dcamp.kr and front1.kr redirects).

See `evidence_summary.md` §6 for the activity tally and §10 for questions.
