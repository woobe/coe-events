# Montreal local-communities discovery log — Run A v2.6

- Task: t_0bbd30e5 (Run A v2.6: Montreal communities research)
- Research root: `~/repo_dev/coe-events`; city dir: `research/montreal/2026-q4/`
- Date checked: 2026-08-11 (all entries; accessed_on 2026-08-11)
- Plan: `local/runA-v2.6-communities-plan-v1.md` (Montreal section, schema 2.3)
- Budapest/HK/SG/NYC calibration: PASS (Budapest review, HK review, SG review,
  and NYC review all passed the same evidence gate); depth decision for
  Montreal: recipe unchanged, keep the Meetup city-directory sweep, keep
  group-controlled Meetup/Luma/Eventbrite organizer pages as claim-bearing
  sources, keep organizer-owned Luma event pages when fact-bearing, keep the
  language boundary (language-neutral facts only for non-English pages).
- Scope: evidence-bound community discovery only. No venue/calendar/city_input
  changes (city_input.json untouched this pass), no bundle/summary, no commits.
  Discovery listings never supply final evidence; every retained record cites a
  group/organizer-owned page.
- Bilingual handling note (Montreal): several official pages are bilingual
  (English + French) or French-first. Records record only facts visible in the
  page's own language — no translation of unverified claims. French-only
  official pages (UdeMAI) are retained only with language-neutral facts
  (schedule, room, purpose as stated) plus a verification question; they are
  never upgraded to claim-bearing English facts. This is a coverage boundary,
  not evidence of absence.

## Channels checked

- AI Tinkerers: aitinkerers.org directory -> Montreal chapter
  montreal.aitinkerers.org (official chapter page, English). Retained active.
- Meetup Pro networks: PyData network landing (meetup.com/pro/pydata/) used as
  discovery entry; group-owned Meetup page meetup.com/pydata-mtl/ used as
  claim-bearing source. Retained: PyData Montreal. R User Groups network
  landing surfaced "DSS Montreal | R User Group" but that group page now
  returns "Group not found" (dead); no verifiable standing Montreal R User
  Group page surfaced this pass — documented as an evidence gap, not absence.
  R-Ladies Montreal (group-owned Meetup page) retained dormant.
- Open searches (recipe query families; retained pages were English or
  bilingual-accessible except UdeMAI, handled under the language boundary):
  - "AI Tinkerers Montreal chapter official"
  - "PyData Montreal meetup official"
  - "R User Group Montreal meetup official"
  - "AI meetup Montreal 2026 in-person community official"
  - "machine learning meetup Montreal 2026 in-person community official"
  - "data science meetup Montreal 2026 official group community in-person"
  - "web3 community Montreal Ethereum meetup 2026 official in-person"
  - "GDG Montreal Google Developer Groups chapter 2026"
  - "McGill AI society MAIS club events official"
  - "MILA Montreal AI community events public meetup"
  - "Concordia University AI club student society events 2026"
  - "WiMLDS Montreal women in machine learning data science meetup"
  - "AI Salon Montreal Luma 2026"
  - "Global AI Community Montreal chapter globalai.community"
  - "AWS User Group Montreal cloud AI meetup 2026"
  - "Montreal blockchain meetup group 2026 bitcoin ethereum events official page"
  - "quant finance Montreal meetup group quantitative trading community"
  - "coworking AI meetup Montreal 2026 hosted community event"
  - "Montreal Python meetup 2026 events PyMontreal"
  - "Notman House Montreal tech AI meetup events 2026"
- Meetup city-directory sweep (meetup.com/find/ + topic pages) — surfaced
  Montreal Machine Learning, MTL Data, Data Drinks Montreal, AI ML Montreal
  Meetup Group, Bitcoin Montreal, Bitcoin Bay Montréal, Ethereum Blockchain
  Montreal 2.0, WiMLDS Montreal, R-Ladies Montreal; used as discovery only.
- Event roundups (discovery only, never final evidence): dev.events,
  createwith.com/cities/montreal, cryptoevents.global, bitcoinonly.events,
  allevents.in, stayhappening.com, trip.com event pages, techforum.ca,
  betakit.com (Notman House financial situation — context only),
  eventbrite.ca city browse. Aggregators rejected as sources.
- Web3-specific: Bitcoin Montreal (official Meetup page, retained active),
  Bitcoin Bay Montréal (official Meetup page, retained active; its Luma event
  "Open Claw, Open Mind, Open Floor" at District 3 is a Bitcoin Bay series
  event, not a separate community — recorded in the Bitcoin Bay record),
  Ethereum Blockchain Montreal 2.0 / ETHMontreal (official Meetup page +
  ethmontreal.com companion, dormant), CryptoMondays Montreal (Meetup page
  returns "Group not found" — no live official page; unresolved), Superteam
  Montreal / Ethereum conference signals (no standing chapter page surfaced),
  OpenClaw Montreal (single Luma event page, no standing community page —
  rejected as standalone; covered under Bitcoin Bay series).
- University: McGill AI Society / MAIS (official site mcgillai.com + events
  page, retained active with co-host flag), UdeM AI / UdeMAI (official
  French-only GitHub Pages about page, retained intermittent under the
  language boundary), Concordia (no official student AI/ML club page with
  held-event evidence surfaced — ConcordAI is an experiential learning program
  and "Concordia AI" is a Beijing/Singapore social enterprise, both rejected;
  documented as an evidence gap), MILA (research institute, not a community —
  rejected as a community record; noted as ecosystem context in the MAIS
  record venue facts).
- Coworking/hub-hosted: District 3 Innovation Center appears as a hosting
  venue for Bitcoin Bay and GDG events (venue facts recorded in those
  records), not retained as a community itself; Notman House is a hub/venue
  with an Eventbrite organizer page and is facing financial trouble (context
  only) — not retained as a community; MTL New Tech/ElanTech (general startup
  community, not AI/ML/data/web3 focused — rejected, NYC "general tech"
  precedent), Tech Montreal (general tech networking — rejected), Startup
  Grind Montreal (no verifiable chapter page surfaced — unresolved).

## Candidates (disposition)

- AI Tinkerers Montreal — RETAINED (active).
  - Channel: aitinkerers.org directory + chapter page.
  - Official page: https://montreal.aitinkerers.org/ (chapter site, English).
    Page reports monthly in-person demo nights: June Demo Meetup 2026-06-17
    (+207), May Demo Meetup @ Ubisoft 2026-05-26 (+215), April Demo Night
    2026-04-22 (+146), March Demo Night 2026-03-24 (+244), February 2026
    2026-02-24 (+166), January 2026 at Ateko 2026-01-21 (+176), Demo Night
    Nov 20 2025 (+131), Spooky October 2025 at Shopify 2025-10-21 (+159),
    September 2025 2025-09-24 (+131), May 2025 at LightSpeed 2025-05-07
    (+133). About: part of a 252-city global network with 115,000+ members.
    Sponsors per event (Ubisoft La Forge, PlusCompany, BDC, Cohere,
    Databricks, IBM, Réseau ÉTS, Cloudflare, Coveo, Shopify). No chapter
    member count on the chapter page.
- PyData Montreal — RETAINED (active).
  - Channel: Meetup Pro PyData network; group Meetup page meetup.com/pydata-mtl/.
  - 3,930 members; "Part of PyData - 98 groups"; Montréal, QC, CA. Bilingual
    About (French first, English follows) — data science, analytics, ML and
    deep learning with Python. In-person: "PyData Montreal Meetup #33
    (in-person | en personne)" 2026-02-18 at Moov AI, 358 Rue Beaubien O #500,
    Montreal (77 attendees); organizer LinkedIn confirms #32 (2025-11-26) at
    Potloc. Network events (Yerevan, London, Global 2025) listed separately as
    network events, not local activity. No own-page sponsorship invitation on
    the group page (PyData network-level sponsor page is network-level, not a
    chapter co-host invitation) — cohost_open false per calibration.
- Montreal AI Night — RETAINED (active).
  - Channel: open search + Eventbrite city browse.
  - Official page: https://www.eventbrite.ca/o/montreal-ai-night-121159366022
    (organizer-owned Eventbrite page).
  - Organizer description: "Montreal AI Night is a local community event
    created to bring together curious professionals, entrepreneurs,
    operators, and builders exploring the real-world impact of artificial
    intelligence." Numbered editions: #2 2026-05-28 at Université de Montréal
    Campus MIL (1375 Ave Thérèse-Lavoie-Roux), #4 wrapped (2026-07 Instagram
    reel), #5 upcoming 2026-08-20 at UdeM Campus MIL ("Women Shaping the
    Future With AI"). In-person series. No member count, no public contact URL
    (Eventbrite contact-organizer form).
- AI ML Montreal Meetup Group — RETAINED (active).
  - Channel: Meetup city-directory sweep + open search.
  - Official page: https://www.meetup.com/montreal-ai-ml-meetup-group/
    (group-controlled Meetup page).
  - 2,766 members; Montréal, QC, CA. About: "The AI Innovators Guild is a
    confluence of AI engineers, AI scientists, programmers, and tech
    aficionados" — the page brands the group as the Montréal AI/ML Meetup /
    AI Innovators Guild community (group name on page: "AI ML Montreal Meetup
    Group"). In-person: "Montreal AI ML Meetup" 2026-08-09 at Café 8oz. Chez
    l'Éditeur - Villeray, 7240 Rue St-Hubert (13 attendees); 2026-08-03 (6);
    2026-08-02 (16); "Microsoft Copilot Studio: Building Voice Agents for
    Telephony" 2026-07-28 at Grande Bibliothèque - BAnQ, 475 Boul. de
    Maisonneuve E (10). Discord invite in About (not recorded as contact).
- Montreal Python — RETAINED (active).
  - Channel: open search.
  - Official page: https://www.meetup.com/montreal-python/ (group-controlled
    Meetup page).
  - 7,060 members; "Part of Python Software Foundation Meetup Pro Network -
    123 groups". Bilingual About. In-person: "Python Picnic Party - 3"
    2026-05-30 at Saint Patrick Square, 1335 Rue Saint-Patrick (32
    attendees); "Montréal Python | MP123 Event" 2026-05-14 (hybrid) at NAD -
    École des arts numériques, 1501 Rue de Bleury (60). Upcoming: AGM
    2026-09-24 (online). General Python community; data/AI relevance is
    evidenced by related topics (Data Science, Machine Learning, Data
    Analytics) and data-focused presentations. montrealpython.org is linked on
    the page but currently serves a misconfigured page (verified 2026-08-11),
    so it is NOT recorded as a contact route; uncertainty noted.
- AI Salon Montreal — RETAINED (active).
  - Channel: open search ("AI Salon Montreal").
  - Official page: https://luma.com/AI-Salon-Montreal-March-2026
    (organizer-owned Luma event page).
  - AI Salon is "the global community bringing together AI founders and
    builders, investors, and partners... Decentralized, chapter-based."
    Montreal chapter co-founded by Nicholas Nadeau, Claude Théoret, Sylvain
    Carle. In-person: AI Salon Montreal #12 (March) 2026-03-26 at CRIM
    offices, 405 Avenue Ogilvy (226 went; sponsors Innovobot, Hélice,
    Innoprofit, GuruLink); AI Salon Montreal May 2026-05-19 at Ax.c (event
    page). Chapter page sponsor tiers are acknowledgments; the page invites
    startups to apply to pitch/demo but shows no "apply to be a sponsor /
    co-host" invitation — cohost_open false (NYC AI Salon "Apply to be a
    Sponsor" language not present on the Montreal pages checked).
- Global AI Montreal — RETAINED (active).
  - Channel: open search (globalai.community).
  - Official page: https://globalai.community/chapters/montreal/ (official
    chapter page).
  - 36 members, 2 events, 4 organizers. In-person: "Build //localhost:Montréal"
    2026-06-19 17:00-20:00 (in person); "🌍 Global AI Montreal – Community
    Meetup" 2026-03-08 13:00-15:00 at BHive Cafe, 2313 Rue Sainte-Catherine O
    (sponsor: Microsoft). No public contact URL on the chapter page
    (organizer LinkedIn buttons not recorded as contact routes).
- GDG Montreal — RETAINED (active).
  - Channel: open search.
  - Official page: https://gdg.community.dev/gdg-montreal/ (official GDG
    chapter page).
  - 893 group members. In-person past events: "GDG Montreal August Drink &
    Chat" 2026-08-06; "Build an app using Firebase & Flutter @SANAAQ (Room 2,
    upstairs)" 2026-07-08; "Google I/O Extended Montreal 2026: In-Person
    Highlights & Networking" 2026-07-02; "Build your first Flutter app with
    Codex OpenAI @District 3" 2026-05-13. General developer community with
    AI-adjacent content (Codex OpenAI workshop, I/O Extended); no upcoming
    events at access time. No sponsorship-invitation language on the chapter
    page (Contact Us is a form) — cohost_open false.
- GDG Cloud Montreal — RETAINED (active).
  - Channel: open search (GDG chapter directory).
  - Official page: https://gdg.community.dev/gdg-cloud-montreal/ (official
    GDG chapter page).
  - 1,050 group members. Mission: "democratize Cloud knowledge... Google Cloud
    services (AI, Kubernetes, Data, Security, and more)"; DevFest Montréal
    flagship. In-person past events: "GDG Montreal August Drink & Chat"
    2026-08-06; "GDG Cloud Southlake #54: Richard Seroter: How to Build with
    AI and Not Lose Your Soul" 2026-07-22; "GDG Windsor Build with Gemma
    Hackathon Launch" 2026-07-19; "Google I/O Extended Montreal 2026"
    2026-07-02. AI/ML/data-relevant (Gemma hackathon, AI build talks). No
    sponsorship-invitation language on the chapter page — cohost_open false.
- Bitcoin Montreal — RETAINED (active).
  - Channel: open search + Meetup city-directory sweep.
  - Official page: https://www.meetup.com/bitcoin-montreal/ (group-controlled
    Meetup page).
  - 3,453 members; bilingual About (English + French); "Since 2013, Bitcoin
    Montreal has worked to share knowledge and passion about Bitcoin... With
    the support of Francis Pouliot and Bull Bitcoin." In-person: "Bitcoin
    Pizza Day Celebration" 2026-05-22 at Le 1000 de la Gauchetiere (33
    attendees); "Get Paid to Heat Your Home" 2026-05-12 at Le Bon Vieux
    Temps, 2051B Rue St-Denis (19); "Cybersecurity: Outsmarting Today's
    Biggest Scams" 2026-03-10 at Le Bon Vieux Temps (14). No co-host
    invitation on the group page (Bull Bitcoin is a supporter, not a co-host
    invitation).
- Bitcoin Bay Montréal — RETAINED (active).
  - Channel: open search + Meetup city-directory sweep.
  - Official page: https://www.meetup.com/bitcoinbay_mtl/ (group-controlled
    Meetup page).
  - 625 members; "open community founded in 2014... blockchain tech." Upcoming
    in-person: "The Bull Run Blueprint: AI and Crypto for Q4" 2026-08-21 at D3
    Innovation Center, 1250 Guy St Suite #600 (AI x Crypto showcase; $15
    voluntary contribution for Human IP; event-level). Past in-person: "Open
    Claw, Open Mind, Open Floor" 2026-05-15 at D3 (21 attendees; DAI • RWA •
    DePIN + live OpenClaw demo); "Blockchain AI Summit End of the Year 2025"
    2025-12-18 at D3 (31). Web3 + AI crossover community.
- McGill Artificial Intelligence Society (MAIS) — RETAINED (active,
  cohost_open true).
  - Channel: open search.
  - Official page: https://mcgillai.com/events/2025-2026 (club's own events
    page; site mcgillai.com).
  - Student-run club under McGill Faculty of Engineering. In-person events:
    MAIS 202 bootcamp (Jan-Apr 2026, Leacock 14); "MAIS Hacks 2025" 2025-11-01
    & 11-02 at Trottier Mezzanine (one of Canada's largest AI hackathons, 150
    students); "Learnathon 2025" 2026-01-23 at Mila - Quebec AI Institute;
    "Montreal AI Undergraduate Project Fair" 2026-04-08 at MILA (hosted by
    MAIS and UdeMAI); "Python for Data Science" 2025-10-03 at 680 Sherbrooke.
    Own-page sponsorship language: "As a McGill AI club sponsor, you will
    have access to the CVs of our hundreds of event participants and reach
    our over 2000 subscribers. If you are interested in partnering with our
    club, please don't hesitate to reach out..." (quoted in
    cohost_evidence_phrase; contact email not recorded per policy).
    "over 2000 subscribers" is a newsletter count, not a member size — null.
- Data Drinks Montreal — RETAINED (active).
  - Channel: Meetup city-directory sweep.
  - Official page: https://www.meetup.com/data-drinks-montreal/
    (group-controlled Meetup page).
  - 901 members; bilingual About (English + French); "monthly meetup where
    data pros, AI builders and curious minds swap real-world insights over a
    drink"; strict non-promotional / non-commercial policy. Upcoming in-person:
    DATA DRINKS MONTHLY 2026-08-18 at Bar Bisou Bisou, 416 Rue Saint-Vincent
    (36 attending), 2026-09-15, 2026-10-20. Free RSVP. No co-host language
    (explicitly non-commercial; cohost_open false). LinkedIn group page
    mentioned but social not recorded as contact.
- UdeM AI (UdeMAI) — RETAINED (intermittent; language boundary).
  - Channel: open search.
  - Official page: https://udemai.github.io/about/ (club's own French-only
    GitHub Pages page; footer © 2023).
  - French-only page (language boundary — language-neutral facts only):
    club meets twice weekly at Pavillon André-Aisensdadt, local 3192
    (Mondays 14:00-15:30, Fridays 15:00-16:30), open to students with a
    programming base, working toward machine-learning competitions and CUCAI.
    No dated events on the page and no member count. Cross-reference: MAIS's
    English events page lists the "Montreal AI Undergraduate Project Fair"
    2026-04-08 at MILA as hosted by MAIS and UdeMAI (cross-page inference,
    needs verification). Intermittent with an in-person verification question.
- Montreal Machine Learning — RETAINED (dormant).
  - Channel: Meetup city-directory sweep + open search.
  - Official page: https://www.meetup.com/mtl-machine-learning/
    (group-controlled Meetup page).
  - 1,307 members. About describes mini-conferences (few times a year) and
    study groups (almost monthly), attendance limited. Last listed in-person
    events: "Study Group: On the Measure of Intelligence" 2020-03-08 at Café
    Parvis, 433 Rue Mayor (13); "Study Group: Single Headed Attention RNN"
    2020-01-28 (10); Mini-Conference Fall 2019 2019-10-23 (110). Companion
    site montrealml.dev (linked from group page) last article 2019-11-06 —
    dormant (>12 months no activity; standing historical Montreal ML
    community, useful context).
- MTL Data — RETAINED (dormant).
  - Channel: Meetup city-directory sweep.
  - Official page: https://www.meetup.com/mtldata/ (group-controlled Meetup
    page).
  - 5,392 members. About: "connect the data + dev communities in Montreal...
    In our monthly meetups, data experts join us..." Last listed in-person
    events: "Real-World AI: Development to Deployment" 2024-04-17 at Hôtel Alt
    Montréal, 120 Rue Peel (87); "Breaking Ground With Generative AI"
    2023-11-15 at Breathe Life (70). No event within 12 months — dormant.
- R-Ladies Montreal — RETAINED (dormant).
  - Channel: R User Groups network discovery.
  - Official page: https://www.meetup.com/rladies-montreal/ (group-controlled
    Meetup page).
  - 596 members; "Part of RLadies+ - 251 groups". Chapter update (March 2025):
    "We will be sharing a survey to gauge interest in meetup activities for
    the coming calendar year." Last events: "Reboot + Refresh Virtual Meetup"
    2025-06-16 (online, 8); in-person "RLadies February Meetup - Introduction
    to R and RStudio" 2024-02-27 at 550 Rue Sherbrooke O (7). No in-person
    event within 12 months — dormant; in-person verification question.
- WiMLDS Montreal — RETAINED (dormant).
  - Channel: open search.
  - Official page: https://www.meetup.com/wimlds-mtl/ (group-controlled
    Meetup page).
  - 1,061 members; bilingual About (English + French); inclusive definition of
    women; everyone welcome. Last events: "[Online] WIMLDS Montreal #7: AI in
    the Video Game Industry" 2020-11-26 (55); "[Online] #6: AI in Health"
    2020-11-12 (41); "Women's Data Day" 2020-09-12 (23); in-person "#5: AI for
    Good" 2019-11-14 at 6650 Rue Saint-Urbain (87). No in-person event within
    12 months — dormant; standing women-in-ML/data community signal.
- Ethereum Blockchain Montreal 2.0 (ETHMontreal) — RETAINED (dormant).
  - Channel: open search (web3 family).
  - Official page: https://www.meetup.com/Ethereum-Blockchain-Montreal/
    (group-controlled Meetup page; ethmontreal.com companion site).
  - 885 members. About: "at least once a month we'll hold an event with
    speakers, demos, updates, and coding projects." Last listed events:
    "Maker Dao Vision and Stable Coins" 2020-05-28 (online, 38); in-person
    "Ethereum Montreal - DEX and Collectible Card Game" 2019-06-06 at Maison
    Notman House (47); "Constantinople Hard Fork Explanation" 2019-01-29
    (57). No event within 12 months — dormant; standing Ethereum community
    signal for web3 category.
- DSS Montreal R User Group (meetup.com/dss-montreal-r-user-group/) —
  UNRESOLVED.
  - Channel: R User Groups network search.
  - Reason: the group page returns "Group not found" (dead page). No
    verifiable standing Montreal R User Group page surfaced this pass.
    Documented as an evidence gap (R ecosystem presence in Montreal is
    evidenced by R-Ladies Montreal, retained dormant), not absence.
- CryptoMondays Montreal (meetup.com/cryptomonday-montreal/) — UNRESOLVED.
  - Channel: web3 search.
  - Reason: search result describes a CryptoMondays Montreal group, but the
    Meetup page returns "Group not found" and cryptomondays.io does not list a
    live Montreal chapter page in this environment. No live official page to
    retain; not presented as a local meetup.
- OpenClaw Montreal (luma.com/78glslld) — REJECTED (as standalone).
  - Channel: open search (luma event).
  - Reason: single Luma event page ("Open Claw, Open Mind, Open Floor",
    2026-05-15 at District 3), no standing community page. Covered as a
    Bitcoin Bay Montréal series event in that record.
- Concordia student AI/ML club — UNRESOLVED (evidence gap).
  - Channel: university search.
  - Reason: no official Concordia student AI/ML club page with held-event
    evidence surfaced. "ConcordAI" (csu.qc.ca) is an experiential learning
    program, not a community club; "Concordia AI" (concordia-ai.com) is a
    Beijing/Singapore social enterprise, not Montreal. Documented as an
    evidence gap, not absence.
- MILA (Quebec AI Institute) — REJECTED (as community).
  - Channel: university/institute search.
  - Reason: research institute, not a community club (NYU CDS NYC precedent).
    Appears as a venue/ecosystem context in MAIS records (events at MILA).
- MTL New Tech / ElanTech (meetup.com/mtlnewtech/) — REJECTED.
  - Channel: coworking/general-tech search.
  - Reason: general startup/tech community (since 2008), not AI/ML/data/web3
    focused (NYC "general tech" precedent).
- Tech Montreal (meetup.com/techmtlorg/) — REJECTED.
  - Channel: general-tech search.
  - Reason: general tech/startup networking community (speakers, open mic),
    not AI/ML/data/web3 focused.
- Startup Grind Montreal — UNRESOLVED.
  - Channel: open search.
  - Reason: no verifiable Montreal chapter page surfaced this pass; network
    sponsor language is not a chapter-level co-host invitation (NYC
    calibration).
- Notman House — REJECTED (as community).
  - Channel: coworking/hub search.
  - Reason: a technology hub/venue with an Eventbrite organizer page; also
    reported to face financial trouble (betakit 2026 context). Venues are not
    retained as communities (venue records live in venues.raw.json).
- Women in AI (Eventbrite organizer page) — UNRESOLVED.
  - Channel: women-in-AI search.
  - Reason: ambiguous organizer page without a verified Montreal chapter page
    with held-event evidence this pass.
- AWS User Group Montreal — UNRESOLVED.
  - Channel: open search.
  - Reason: no verifiable Montreal chapter page surfaced this pass.

## Discovery summary

- Channels exercised: AI Tinkerers directory, Meetup Pro PyData + R networks,
  open-query families (AI/ML/data/web3/university/coworking/women/quant),
  Meetup city-directory sweep, web3 Luma searches, event roundups (dev.events,
  createwith, cryptoevents.global, bitcoinonly.events, Eventbrite city browse),
  LinkedIn/Instagram signals (corroboration only). Candidates logged: 30
  dispositions -> 19 retained, 5 rejected, 6 unresolved.
- Evidence yield: 19 retained records — 13 active, 1 intermittent, 5 dormant.
  Record count is descriptive, not a target; Montreal is a mid-size market in
  the five-city set with a strong AI ecosystem and yielded a healthy active
  set (13) plus standing dormant signals (Montreal Machine Learning, MTL Data,
  R-Ladies, WiMLDS, ETHMontreal) without relaxing the official-page rule.
- Category coverage: AI/ML strong (AI Tinkerers Montreal, PyData Montreal,
  Montreal AI Night, AI ML Montreal Meetup Group, AI Salon Montreal, Global AI
  Montreal, GDG Cloud Montreal, MAIS, UdeMAI, Montreal Machine Learning
  dormant), data science (PyData Montreal, Montreal Python, Data Drinks
  Montreal, MTL Data dormant, R-Ladies dormant, WiMLDS dormant), web3
  (Bitcoin Montreal, Bitcoin Bay Montréal, Ethereum Blockchain Montreal 2.0
  dormant), quant (0 standing — no verifiable standing Montreal quant
  community page surfaced; documented as an evidence gap, not an absence
  claim), mixed (GDG Montreal as general dev + AI).
- In-person evidence: 13 active records each carry a page-visible in-person
  event dated 2025-08-12..2026-08-11; 1 intermittent (UdeMAI — own page
  undated, cross-referenced 2026-04-08 event on MAIS page); 5 dormant have no
  in-person event within 12 months (Montreal Machine Learning, MTL Data,
  R-Ladies Montreal, WiMLDS Montreal, Ethereum Blockchain Montreal 2.0).
- Co-host evidence: 1 true flag (McGill AI Society / MAIS — own-page
  sponsorship/partnership invitation quoted, needs_human_verify true, with a
  verification question). False-positive risks avoided: PyData network-level
  sponsor page not treated as a chapter co-host invitation; GDG chapter
  sponsorship absent from chapter pages; Bitcoin Montreal "Bull Bitcoin"
  support is a supporter acknowledgment, not a co-host invitation; AI Salon
  Montreal sponsor tiers are acknowledgments (no "apply to be a sponsor"
  ticket like the NYC chapter); Data Drinks Montreal explicitly non-commercial.
- Official-source quality: all 19 retained records cite group/organizer-owned
  pages (chapter sites, group Meetup pages, club sites, organizer-owned Luma
  event pages, organizer-owned Eventbrite page). Meetup/Luma group pages
  qualified as claim-bearing when group-controlled; organizer-owned Luma event
  pages (AI Salon Montreal) qualify when they visibly show group/event facts
  (HK/SG/NYC Luma precedent). Language boundary exercised: UdeMAI's
  French-only page retained with language-neutral facts only (schedule, room,
  purpose) plus verification question; all other retained pages were English
  or bilingual-accessible. MILA and ConcordAI were rejected as institutes/
  programs rather than communities.
- Depth decision for remaining cities (none — Montreal is the final city in
  the five-city set): recipe unchanged; keep the Meetup city-directory sweep;
  keep organizer-owned Luma/Eventbrite pages as claim-bearing when
  fact-bearing; keep the language boundary for French-only pages; keep the
  false-positive discipline on co-host flags. If any city follows later,
  re-run the same recipe and this log's dispositions.

Note on counts: 30 dispositions logged (19 retained + 5 rejected + 6
unresolved). The retained breakdown is 13 active / 1 intermittent / 5 dormant
(the summary paragraph above counts 5 dormant — Montreal Machine Learning, MTL
Data, R-Ladies Montreal, WiMLDS Montreal, Ethereum Blockchain Montreal 2.0).
Disposition labels were reconciled so every candidate has exactly one: DSS
Montreal R User Group and Concordia student AI/ML club are UNRESOLVED
(dead/no verifiable page, evidence gap — same convention as CryptoMondays,
Startup Grind, and AWS User Group Montreal); the earlier draft's "34
dispositions (19 + 11 + 4)" mislabeled the 11 non-retained candidates as "11
rejected" and then added the 4 unresolved again separately, double-counting
the unresolved subset. Correct total: 30.
