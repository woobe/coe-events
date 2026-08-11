# Hong Kong local-communities discovery log — Run A v2.6

- Task: t_01c7b25c (Run A v2.6: Hong Kong communities research)
- Research root: `~/repo_dev/coe-events`; city dir: `research/hong-kong/2026-q4/`
- Date checked: 2026-08-11 (all entries; accessed_on 2026-08-11)
- Plan: `local/runA-v2.6-communities-plan-v1.md` (HK section, schema 2.3)
- Budapest calibration gate: PASS (local/runA-v2.6-budapest-communities-review-v1.md);
  depth decision: recipe unchanged, keep Meetup city-directory sweep, keep
  group-controlled Meetup pages as claim-bearing sources, keep the language
  boundary (language-neutral facts only for Chinese/English-sparse pages).
- Scope: evidence-bound community discovery only. No venue/calendar/city_input
  changes, no bundle/summary, no commits. Discovery listings never supply final
  evidence; every retained record cites a group/organizer-owned page.

## Channels checked

- AI Tinkerers: aitinkerers.org/all_cities directory -> Hong Kong chapter
  hong-kong.aitinkerers.org (official chapter page). Retained.
- Meetup Pro networks: PyData network landing (meetup.com/pro/pydata/) and R
  User Groups network (meetup.com/pro/r-user-groups/) used as discovery entry
  points; group-owned Meetup pages used as claim-bearing sources. Retained:
  PyData Hong Kong, R programming hub. HKRUG unresolved (Facebook-only).
- Open searches (recipe query families, English; Chinese only to locate an
  official page, never to translate unverified claims):
  - "AI meetup Hong Kong official" / "site:meetup.com Hong Kong AI"
  - "machine learning community Hong Kong official" / "machine learning meetup HK"
  - "data science meetup Hong Kong 2026 official" / "data science community HK"
  - "web3 community Hong Kong official" / "blockchain OR web3 meetup Hong Kong"
  - "AI Tinkerers Hong Kong" / "PyData Hong Kong" / "R User Group Hong Kong"
  - "university AI club HKUST OR HKU OR CUHK" / "HKUST AI club official"
  - "coworking AI meetup Hong Kong" (Good Lab, The Wave, Campfire, Hive)
  - "GDG Hong Kong AI" / "AWS User Group Hong Kong"
  - "Women in AI Hong Kong" / "Global Women in AI Hong Kong"
  - "quantitative finance meetup Hong Kong" / "Hong Kong Quant"
  - "Open Data Hong Kong" / "Open Source Hong Kong"
  - "852web3" / "Ethereum Hong Kong" / "Women in Web3 Hong Kong"
- Meetup city-directory sweep (meetup.com/find/hk--hong-kong/) — surfaced
  Data Science & Generative AI Hong Kong; used as discovery only.
- Web3-specific: Luma event pages (Ethereum hub, GWAI launch, Starknet, Token2049
  coffee, Consensus HK side events), 852web3.io, womeninweb3hk.com.
- University channel: HKU SOConnect portal, HKUST/HKU/CUHK searches; no official
  student AI/ML club community page with events surfaced in this pass.

## Candidates (disposition)

- AI Tinkerers Hong Kong — RETAINED (active).
  - Channel: aitinkerers.org/all_cities directory + events feed.
  - Official page: https://hong-kong.aitinkerers.org/ (chapter site). Page
    reports "Local cadence 33 events in the last 12 months"; in-person meetups
    include 2026-07-29 @ Wyndham Social (+41), 2026-06-24 @ Dialogue in the Dark
    (+54), 2026-05-07 AI Demo Night @ Google (+149), 2026-04-29 @ AWS (+158);
    next event 2026-08-31 "August Meetup with OAX Foundation and GMAsia".
    Organizers Dom Keller and John NG named in event descriptions.
- Hong Kong Machine Learning Meetup (HKML) — RETAINED (active, cohost_open true).
  - Channel: open search; group Meetup page + official archives hkml.ai.
  - Official page: https://www.meetup.com/hong-kong-machine-learning-meetup/
    (2,241 members; "Part of" none; organizers Gautier Marti + 1).
  - In-person meetups: HKML S8E3 2026-07-09 @ Maven Securities, Wanchai (18);
    S7E5 2025-12-18 @ Bullish, The Centrium, Central (26); 2025-10-15 networking
    @ The Executive Centre, 28 Stanley Street (34); S7E3 2025-07-10 @ HKU iCube
    (26). Co-host phrase quoted from About text (sponsors invitation).
- PyData Hong Kong — RETAINED (active).
  - Channel: Meetup Pro PyData network; meetup.com/pydata-hong-kong/ (group page).
  - 288 members ("Part of PyData - 98 groups", organizers Howard Cheung + 4).
  - In-person meetup 2025-12-16 "From Chaos to Causality" @ Hong Thai Expo &
    Business Centre, 5/F Unite Centre, Admiralty (11 attendees); recent listed
    events are network events (PyData Yerevan/London/Global). No upcoming events.
- Data Science & Generative AI Hong Kong — RETAINED (active).
  - Channel: Meetup city-directory sweep + open search.
  - Official page: https://www.meetup.com/data-science-hk/ (2,579 members,
    organizers Altaf Rehmani + 1). In-person events 2026-08-08 and 2026-07-18
    @ 300 Hennessy Rd, Wan Chai (18/21 attendees); upcoming paid weekend
    workshop 2026-08-29.
- GDG Hong Kong — RETAINED (active).
  - Channel: open search; official chapter page gdg.community.dev/gdg-hong-kong/
    (2,578 members; organizers Frankie Wu, Arik Chan, Kenneth Lui + helpers).
  - In-person: 2026 AI Paper Reading Club #1 2026-07-29 @ CG Marketing, Unit
    901-03, 9/F, Laford Centre, Cheung Sha Wan (27 RSVP'd); upcoming GDGHK AI
    Session: On-Device Intelligence & Agentic Web 2026-08-19; Build with AI HK
    2026 speaker sessions in 2026.
- Hong Kong Python User Group (HKPUG) — RETAINED (active).
  - Channel: open search; meetup.com/pythonhk/ (1,769 members, organizer Sammy
    Fung + 6). In-person: HKPUG #100 2026-07-11 @ CityU AC1 P4701 (32); #99
    2026-06-27 @ PolyU BC404 (19); #98 2026-05-30 @ CityU (28). Website pycon.hk
    linked from group page.
- Open Source Hong Kong (OSHK) — RETAINED (active).
  - Channel: open search (Open Data Day 2026 + substack).
  - Official page: https://opensource.hk/meetups/ (own site). Regular meetups:
    #95 2026-02-28 @ CityU (tech job market + Dify agent workshop); co-organized
    vLLM Hong Kong Meetup 2026-03-07 @ PolyU (first in city); #91 2025-12-09
    (Ansible); #88 2025-06-11 Agentic AI w/ Red Hat. Site text: "Open Source
    Hong Kong hosts regular meetups".
- AWS User Group Hong Kong (AWS UGHK) — RETAINED (active).
  - Channel: open search; meetup.com/hong-kong-amazon-aws-user-group/ (1,299
    members, "Part of Global AWS User Group Community - 416 groups", organizer
    Alex Lau + 5). In-person: 2026-07-24 IT 圍爐夜 (45) @ AWS Hong Kong Tower
    535; 2026-05-29 Kubernetes Night (42); 2026-04-11 x AgentCon (48);
    2026-03-31 Global Gathering (50).
- Global AI Hong Kong — RETAINED (active).
  - Channel: open search (Meetup page 404s); official chapter page
    globalai.community/chapters/hong-kong/ (532 members, 14 events, 5
    organizers). In-person: AgentCon - Hong Kong 2026-04-11 (in person; joint
    with AWS UG/HKIIT per AWS page); AgentCamp series online/hybrid (2026-02);
    Microsoft Reactor externals.
- AI Builders Hong Kong — RETAINED (intermittent).
  - Channel: open search (site:meetup.com HK AI).
  - Official page: https://www.meetup.com/ai-builders-hong-kong/ (22 members).
    Featured in-person event: Agent Creativity Hackathon for Autism Charity
    2026-08-18 @ HKPC 1/F, InnoSpace, Kowloon Tong (co-organized with Tencent
    Cloud). No past events listed; single upcoming event; new/small group.
- Advanced AI Concepts-Hong Kong — RETAINED (intermittent, digital-only).
  - Channel: open search (site:meetup.com HK AI).
  - Official page: https://www.meetup.com/advanced-ai-concepts-hong-kong/
    (32 members). Upcoming events listed are ONLINE (2026-08-15, 2026-08-17).
    Digital-first evidence explicit; in-person presence question.
- Women in Web3 Hong Kong (WiW3 HK) — RETAINED (active).
  - Channel: open web3 search; Luma event page (organizer's own page).
  - Official page: https://luma.com/5aw5ip6h (Women in Web3 Hong Kong Events,
    hosted by WiW3 HK Team). In-person: Stress Management Workshop 2026-06-14 @
    Tune In Wellness, 137-139 Johnston Rd, Wan Chai (sponsored by Animoca
    Brands); Animoca-hosted WiW3 career/AI workshop ~2026-07 per LinkedIn;
    Elevate women-focused Web3 gathering (past, full capacity). Official site
    womeninweb3hk.com is a JS shell (no extractable content).
- Hong Kong Ethereum Community Hub — RETAINED (active).
  - Channel: open web3 search; Luma page (hub's own event page).
  - Official page: https://luma.com/uf5v6joa (Hong Kong Ethereum Community Hub
    Events; operated by SNZ and ETHTAO; supported by Ethereum Foundation
    Ethereum Everywhere). In-person grand opening + meetup 2026-04-21, West
    Kowloon (Vitalik, EF President Aya, ecosystem panels).
- Global Women in AI (GWAI) Hong Kong Chapter — RETAINED (intermittent).
  - Channel: open search (Women in AI Hong Kong).
  - Official page: https://luma.com/k9tr14sl (GWAI HK Chapter launch @ LEAP
    East, hosted by Global Women In AI; 80 went). In-person launch 2026-07-09 @
    HKCEC Hall 3C. Chapter just launched; one launch event evidenced; ongoing
    cadence unproven.
- R programming hub (R 程式交流組) — RETAINED (intermittent).
  - Channel: Meetup Pro R User Groups + open search.
  - Official page: https://www.meetup.com/r-programming/ (10 members, organizer
    Bing Chong + 1). States it is "the only Meetup group in Hong Kong focused
    on the programming code R". One past event: "Variance debunked tutorial"
    2026-05-31, Hong Kong (paid, $100, 1 attendee). Cantonese-first group;
    English welcome. Language-neutral facts only.
- Artificial Intelligence Society of Hong Kong (AISHK) — RETAINED (dormant).
  - Channel: open search (site:meetup.com HK AI).
  - Official page: https://www.meetup.com/chatbot-ai-hong-kong/ (3,563 members,
    organizer Maurice Ng + 1; "Find out more at www.aisociety.hk").
  - Last listed events: 2024-04-19 HKAI LAB Cohort 11, 2023-12-01, 2023-11-18;
    official site aisociety.hk shows "There are no upcoming events" and last
    past event 2023-02-22. No activity within 12 months.
- 852Web3 — RETAINED (dormant).
  - Channel: open web3 search.
  - Official page: https://www.852web3.io/ (own site). Site events list ends
    2023-07-28 (852 IRL x Pixelmon); earlier 852 IRL series 2022-2023. LinkedIn
    claims ongoing "leading Web3 community/media platform" but no official-page
    event evidence within 12 months. 4000+ attendees claim is historical.
- Hong Kong Data Science Society (HKDSS) — RETAINED (dormant).
  - Channel: open search.
  - Official pages: https://www.meetup.com/hong-kong-data-science-society/
    (633 members) + https://hkdss.org/ (own site, linked from group page).
    Last Meetup events 2018; hkdss.org events end 2019 (AXA Hack for Health).
    No activity within 12 months.
- The AI Meetup (meetup.com/the-ai-meetup/) — REJECTED.
  - Channel: open search ("AI meetup Hong Kong official").
  - Reason: group is Utrecht, NL (510 members, events in Utrecht) — out of city.
- Real-Time Analytics meetup Hong Kong (meetup.com/meetup-group-hk/) — REJECTED.
  - Channel: open search (data science HK).
  - Reason: official Meetup page returns "Group not found" (defunct/unreachable).
- AI Hong Kong / AIHK (aihongkong.org) — REJECTED.
  - Channel: open search ("AI meetup Hong Kong").
  - Reason: industry association (memberships/masterclasses/advocacy); events
    page is JS-driven and shows only an external conference listing
    (Money20/20 Asia 2024 in Bangkok); no recurring local community meetup
    evidence on the page. Not a community-meetup record.
- AI Collective — REJECTED.
  - Channel: open search (aicollective.com/chapters).
  - Reason: no Hong Kong chapter listed in the chapters directory; global
    chapters page has no HK mention.
- The Buz (BEATS SOHO professional networking) — REJECTED.
  - Channel: Meetup city-directory sweep.
  - Reason: general professional/social networking group; no AI/ML/data/web3
    focus evidenced.
- Friday Beer Bay for Web, Tech & Startups — REJECTED.
  - Channel: Meetup city-directory sweep.
  - Reason: general web/tech/startup networking social; not an AI/ML/data/web3
    community with technical meetups evidenced.
- Hong Kong Founders / Startup Founders Association / FoundersHK — REJECTED.
  - Channel: open search (founders/startup).
  - Reason: founder/startup networking organizations; no AI/ML/data/web3
    community-meetup evidence on their pages.
- Open Data Hong Kong (odhk.github.io) — REJECTED.
  - Channel: open search ("Open Data Hong Kong").
  - Reason: site states "we meet every three weeks" but the listed meets end in
    2014 (Meet.20); no activity for 12+ years; too stale for useful context.
    Open-data activity now covered by Open Source Hong Kong record.
- Token2049 Coffee Meetup (CoffeeDAO + Cointelegraph HK) — REJECTED.
  - Channel: web3 Luma search.
  - Reason: conference side event (Token2049), not a standing community.
- Starknet in HK / Make Web3 Pop in HK / Consensus HK side events — REJECTED.
  - Channel: web3 Luma search.
  - Reason: conference side events / one-off ecosystem events, not standing
    communities.
- Bitcoin Asia 2026 (conference) — REJECTED.
  - Channel: web3 search.
  - Reason: conference (Aug 27-28 2026), not a community.
- HKUST / HKU / CUHK student AI clubs — UNRESOLVED.
  - Channel: "HKUST AI club official", "HKU SOConnect", "CUHK AI student
    society".
  - Reason: no official student AI/ML club page with community/event evidence
    surfaced in this pass (HKU SOConnect is a login portal; HKUST/HKU/CUHK
    searches returned department/alumni pages without club event pages). Not an
    absence claim; HKML's HKU iCube venue and HKPUG's CityU/PolyU venues show
    university-adjacent hosting.
- Hong Kong R User Group (HKRUG, Facebook) — UNRESOLVED.
  - Channel: Meetup Pro R User Groups + jumpingrivers directory.
  - Reason: directory lists HKRUG with a Facebook group link
    (facebook.com/groups/hkrusers/) but Facebook fetch returned HTTP 400 in
    this environment; no accessible official page to verify activity. R
    representation retained via R programming hub record.
- Women in AI (WAI global network) HK chapter — UNRESOLVED.
  - Channel: open search ("Women in AI Hong Kong").
  - Reason: no official HK chapter events page surfaced in this pass; the
    women-in-AI space in HK is represented by the GWAI HK Chapter launch
    (retained). Not an absence claim.
- Hong Kong quant community (QuantInsti/ICE gatherings) — UNRESOLVED.
  - Channel: open search ("quantitative finance meetup Hong Kong").
  - Reason: recurring "Hong Kong Quantitative Community Gathering" events are
    organizer/company-hosted event series (QuantInsti, ICE, LinkedIn posts),
    not a standing community with its own official page. Not an absence claim;
    HKML covers quant-adjacent ML audience directly.

## Discovery summary

- Channels exercised: AI Tinkerers directory, Meetup Pro PyData + R networks,
  open-query families (AI/ML/data/web3/university/coworking), Meetup city
  directory sweep, web3 Luma searches, association/official-site checks.
  Candidates logged: 33 dispositions -> 18 retained, 11 rejected, 4 unresolved
  (rejection lines that bundle several conference side-events count once).
- Evidence yield: 18 retained records — 11 active, 4 intermittent, 3 dormant.
  Record count is descriptive, not a target.
- Category coverage: AI/ML strong (AI Tinkerers HK, HKML, GDG HK, AWS UGHK,
  Data Science & Generative AI HK, Global AI HK, AI Builders HK, Advanced AI
  Concepts, GWAI HK, AISHK dormant), data science (PyData HK, Data Science &
  Generative AI HK, HKPUG, OSHK, HKDSS dormant, R programming hub), web3
  (852Web3 dormant, Women in Web3 HK, HK Ethereum Community Hub), quant covered
  via HKML (quantitative-finance ML events; no standing HK quant community
  page). Web3 is thinner on standing official pages than Budapest's Comets
  find; HK's web3 official evidence is concentrated in hub/chapter/community
  pages (Ethereum Hub, WiW3, 852Web3) plus conference side events (rejected).
- In-person evidence: 11 active records each carry a page-visible in-person
  event dated 2025-08-11..2026-08-11; 4 intermittent (AI Builders single
  upcoming hackathon; Advanced AI Concepts digital-first; GWAI HK single launch
  event; R programming hub single paid tutorial); 3 dormant have no in-person
  event within 12 months.
- Co-host evidence: 1 true flag (Hong Kong Machine Learning Meetup) with the
  quoted sponsorship-invitation phrase from the group's own Meetup About text
  ("We are always on the lookout for high-quality speakers and sponsors:
  Contact us!"); needs_human_verify true + verification question. All other
  records: no own-page sponsorship/collaboration invitation observed;
  cohost_open false with null phrase. AISHK's site carries "always on the
  search for speakers and event partners" but the group is dormant — recorded
  as observed fact, not flagged (false-positive risk avoided for dormant
  group; Budapest calibration precedent).
- Official-source quality: all 18 retained records cite group/organizer-owned
  pages (chapter sites, group Meetup pages, org websites, organizer Luma event
  pages). Luma event pages qualify when they are the organizer's own page
  (WiW3 HK, Ethereum Hub, GWAI launch) and visibly show group/event facts.
  Chinese/English boundary exercised: Cantonese-first R programming hub About
  text recorded as language-neutral facts only (name, member count, event
  date/venue/price); no translation of claims. Hong Kong R User Group
  (Facebook-only) not retained (inaccessible official page in this pass).
- Depth decision for remaining cities: continue the recipe unchanged; keep the
  Meetup city-directory sweep; keep organizer-owned Luma pages as claim-bearing
  sources when group-owned and fact-bearing; keep language-neutral handling of
  Cantonese/Chinese pages; do not relax the official-page evidence rule.
