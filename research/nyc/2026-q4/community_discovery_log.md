# New York City local-communities discovery log — Run A v2.6

- Task: t_e6f0a6b7 (Run A v2.6: NYC communities research)
- Research root: `~/repo_dev/coe-events`; city dir: `research/nyc/2026-q4/`
- Date checked: 2026-08-11 (all entries; accessed_on 2026-08-11)
- Plan: `local/runA-v2.6-communities-plan-v1.md` (NYC section, schema 2.3)
- Budapest/HK/SG calibration: PASS (Budapest review, HK review, and SG review
  all passed the same evidence gate); depth decision: recipe unchanged, keep
  Meetup city-directory sweep, keep group-controlled Meetup/Luma pages as
  claim-bearing sources, keep organizer-owned Luma event pages when
  fact-bearing, keep the language boundary (language-neutral facts only for
  non-English pages).
- Scope: evidence-bound community discovery only. No venue/calendar/city_input
  changes, no bundle/summary, no commits. Discovery listings never supply final
  evidence; every retained record cites a group/organizer-owned page.

## Channels checked

- AI Tinkerers: aitinkerers.org directory -> New York City chapter
  nyc.aitinkerers.org (official chapter page). Retained.
- Meetup Pro networks: PyData network landing (meetup.com/pro/pydata/) and R
  User Groups network (meetup.com/pro/r-user-groups/) used as discovery entry
  points; group-owned Meetup pages used as claim-bearing sources. Retained:
  PyData NYC, New York Open Statistical Programming Meetup (nyhackr), New York
  R User Group (dormant), R-Ladies New York (dormant), NYC PyLadies (dormant).
- Open searches (recipe query families, English; all retained pages were
  English-accessible — no non-English official page was required this pass):
  - "AI Tinkerers New York chapter official"
  - "PyData NYC meetup official"
  - "R User Group New York City meetup official"
  - "AI meetup New York City 2026 official community in-person"
  - "machine learning meetup NYC 2026 in-person community official"
  - "data science meetup NYC 2026 official group community in-person"
  - "web3 community New York Ethereum meetup 2026 official in-person"
  - "GDG New York Google Developer Groups chapter 2026"
  - "Columbia University AI club events" / "NYU AI society student org"
  - "coworking AI meetup New York 2026 hosted community event"
  - "quantitative finance meetup New York quant community 2026"
  - "Women in AI NYC / WiMLDS meetup 2026 in-person"
  - "Papers We Love NYC 2026"
  - "LangChain NYC meetup" / "ComfyUI NYC creative AI"
  - "CryptoMondays New York meetup 2026 events official"
  - "Startup Grind NYC 2026 AI events Civic Hall"
  - "ODSC / Open Data Science NYC meetup group 2026"
- Meetup city-directory sweep (meetup.com/find/us--ny--new-york/) — surfaced
  NYC Tech Meetup (rejected: general tech), NYC Quantum Computing Meetup
  (rejected: quantum computing outside the enumerated focus taxonomy), and
  AI-relevant events from retained groups; used as discovery only.
- Event roundups (discovery only): Bond AI - New York Luma calendar
  (luma.com/genai-ny — aggregator calendar; rejected as a source/community
  itself, but surfaced LangChain NY, NYC Creative AI, New York Robotics),
  TechMeetups.io (nycpython listing), GarysGuide, events.trymimetic.com,
  Startup Grind events feed, supermomos.com, vibecoding.app, usecarly.com
  NYC Tech Week schedule — all discovery/corroboration only.
- Web3-specific: CryptoMondays NYC (official Meetup page, retained active),
  Based Meetup - New York (Luma event page; rejected — single event, no
  standing chapter page), ethereum NYC conference-style signals (ETHNewYork /
  Ethereum NYC 2025 conference pages — conference, not standing community),
  Superteam Luma (no NYC-specific chapter calendar surfaced this pass).
- University: Columbia AI Club CUB (official Luma event page, retained
  active), NYU Data Science Club/DSC@NYU (official site dscnyu.org, retained
  active), Columbia Business School AI Club (official page, unresolved —
  no upcoming events and no dated recent in-person event verified this pass),
  NYU Center for Data Science (institutional department, not a community
  club), Columbia AI university initiative (institutional, not a club).

## Candidates (disposition)

- AI Tinkerers New York City — RETAINED (active).
  - Channel: aitinkerers.org directory + chapter page.
  - Official page: https://nyc.aitinkerers.org/ (chapter site). Page reports
    "Local cadence 36 events in the last 12 months"; next event August Demo
    Day ft Runpod on 2026-08-19 (6-9pm, +107 attending). Past in-person
    events: NYC Vision Hack v.2 2026-08-07 (+130), Hack and Run 5K with
    chat.dev 2026-08-01 (+21), NYC Summer Social rooftop 2026-07-29 (+302),
    Morning Build Sprint/Coworking Cafe 2026-07-24 (+36), closed-door dinner
    2026-07-22 (+151), Morning Build Sprint 2026-07-10 (+38), Run and Hack NY
    Tech Week 5k 2026-06-06 (+20), Emotionally Intelligent AI Hackathon with
    ElevenLabs 2026-06-06 (+122), NYTW Omakase Dinner 2026-06-04 (+157). No
    chapter member count on the page.
- PyData NYC — RETAINED (active, cohost_open true).
  - Channel: Meetup Pro PyData network; group Meetup page + official site
    nyc.pydata.org.
  - 8,006 members; "Part of PyData - 98 groups". In-person: "Making Static &
    Interactive Visualizations using Matplotlib" 2026-03-26 at CUNY Graduate
    Center, 365 5th Avenue (62 attendees); "Jupyter Open Studio Day"
    2026-04-20 at 919 Third Avenue, 23rd floor (1 attendee). Official site
    nyc.pydata.org states "Whether you're interested in giving a talk or
    sponsoring our event, we'd love to hear from you!" and "For Sponsors:
    Supporting our meetups can help foster the growth of the data science
    community, gain exposure, and connect with industry experts" with an
    interest form (own-page sponsorship invitation; quoted in
    cohost_evidence_phrase). Also lists LLMOps with Hopsworks and Modal Labs
    @ Microsoft and Time Series Forecasting @ Microsoft as past events.
- New York Open Statistical Programming Meetup (nyhackr) — RETAINED (active).
  - Channel: R network search; group Meetup page + own site nyhackr.org.
  - 13,617 members. In-person monthly at Pless Hall, 82 Washington Square
    East, New York (NYU-hosted): upcoming "Data exploration of Pixar films"
    2026-08-11 (7pm, $7 in-person, external registration at nyhackr);
    "Typst for Efficient Typesetting" 2026-07-13; "Genealogy and LLMs"
    2026-06-16. Own site states "Thank you to NYU for hosting us" for the
    August talk (event-level venue hosting, not a standing co-host invitation).
- (NYAI) New York Artificial Intelligence — RETAINED (active, cohost_open true).
  - Channel: open search; group Meetup page (meetup.com/nyaimeetup/).
  - 4,164 members; "Part of AI Community Collective - 9 groups". About states
    "NYAI.co is a global community focused on AI in NYC and beyond." Own-page
    partnership language: "Have a message to share with the AI community?
    Partner with us to lead an event or workshop." and "Interested in
    Sponsoring an AI event? Apply here." (quoted in cohost_evidence_phrase).
    In-person: "Vibe Code Live: Build, Learn, Repeat - #NYTechWeek (NYAI,
    WIMLDS, Brainstation)" 2026-06-02; "AI Summit New York 2025" 2025-12-10 at
    Jacob Javits Center (10 attendees). Upcoming partner event 2026-08-28
    (in-person information leaders meetup with AI Accelerator Institute).
- NYC AI Developers Group (AICamp NYC) — RETAINED (active, cohost_open true).
  - Channel: open search; group Meetup page (meetup.com/aittg-nyc/) + own
    event pages on aicamp.ai.
  - 12,211 members; site www.aicamp.ai. Own-page language: "If you'd like to
    speak at our meetups, co-host your events, or inquire about partnership
    opportunities, please feel free to reach out to us." (quoted in
    cohost_evidence_phrase). In-person: "Agentic AI in Finance" 2026-08-04 at
    307 West 38th Street, 14th Floor, Studio 1401, New York, NY 10018 (18
    attendees). AICamp's own event page for the Oct 16 2025 NYC meetup at
    JPMC (273 RSVPs) states "We are actively seeking sponsors to support our
    community. Whether it is by offering venue spaces, providing food/drink,
    or cash sponsorship" (aicamp.ai/event/eventdetails/W2025101614).
- GDG NYC — RETAINED (active, cohost_open true).
  - Channel: open search; official chapter page gdg.community.dev/gdg-nyc/.
  - 5,183 group members. Own-page sponsorship language: "Looking to showcase
    your brand or hire top tech talent? Explore sponsorship opportunities with
    North America's largest Google Developer Group" (quoted in
    cohost_evidence_phrase). In-person events: "Google Maps Platform Developer
    Community Day at the New York City Google Office" 2026-06-10; "Vibe Code
    & Tea: Intro to Gemini AI - #NYTechWeek" 2026-06-05; "Google I/O Build
    with AI Hackathon x Google Cloud Labs" 2026-05-22; "Gemini in Motion"
    2026-04-23. Winner of the 2026 "Technical Vanguard" award by Google
    Developer Groups.
- NYC Women in Machine Learning & Data Science (WiMLDS NYC) — RETAINED
  (active).
  - Channel: open search; group Meetup page (meetup.com/nyc-wimlds/).
  - 4,764 members; chapter page wimlds.org/chapters/about-nyc. In-person:
    "Vibe Code Live! WiMLDS at #NYTechWeek" 2026-06-02 at BrainStation,
    136 Crosby Street (33 attendees); "AI Demo Night with Women in Machine
    Learning & Data Science" 2025-12-11 at BrainStation (32 attendees);
    "WiMLDS: AI Workshop Series - Bootcamp #3: Women in AI Tech Panel"
    2025-10-14 at BrainStation (117 attendees).
- Global AI New York — RETAINED (active).
  - Channel: open search; official chapter page
    globalai.community/chapters/new-york/.
  - 338 members, 3 events, 3 organizers. In-person: "Global AI Night"
    upcoming 2026-09-21 (17:30-21:00, in person); "AgentCon - New York"
    2026-03-09 (10:00-17:00, in person, 13); "Agentic AI: Implementation and
    Org Transformation" 2025-11-13 (17:15-19:15, in person).
- The New York Python Meetup Group (NYC Python) — RETAINED (active).
  - Channel: open search; group Meetup page (meetup.com/nycpython/).
  - 17,449 members; site nycpython.org. In-person: "NYC Python x PyData NYC:
    Talk Night at Datadog!" 2025-10-01 at Datadog, New York Times Bldg,
    620 8th Avenue, 45th Floor (106 attendees); "Git for Data: How Table
    Formats Unify Software and Data Development" 2025-10-15 (17 attendees);
    "GenAI Zoo - NY Tech Week" 2025-06-03 at 11 Times Sq.
- Mindstone NY AI Meetup — RETAINED (active).
  - Channel: open search; group Meetup page (meetup.com/mindstone-ny-ai-meetup/).
  - 2,597 members; "Part of Mindstone #PracticalAI Community - 44 groups";
    site mindstone.com. In-person: "Mindstone New York February AI Meetup"
    2026-02-26 at Wix Playground, 100 Gansevoort St (121 attendees); "Mindstone
    New York December AI Meetup" 2025-12-09 at All Souls NYC, 1157 Lexington
    Ave (19 attendees); "Mindstone / Anote NYC June AI Meetup" 2025-06-04 at
    CIBC New York, 300 Madison Avenue (26 attendees).
- NYC Creative AI (formerly ComfyUI NYC) — RETAINED (active).
  - Channel: Bond AI calendar + open search; organizer-owned Luma event pages.
  - Event page states "Over 4000 community members. Join for our monthly
    event." In-person: "NYC Creative AI July Forum" 2026-07-10 at ZeroSpace,
    337-345 Butler St, Brooklyn (449 went; livestream and in-person); monthly
    events at ZeroSpace with past editions Apr/May/Jun 2026 listed.
- LangChain NYC — RETAINED (active).
  - Channel: Bond AI calendar + open search; organizer-owned Luma event page
    (luma.com/mimsk691).
  - "NYC LangChain Meetup: Ambient Agent Architectures" 2025-08-21, in-person
    at Grammarly NYC (210 went; NDA required on arrival per page); description
    states "Come meet other NYC-based engineers and developers building with
    LangChain and LangGraph." An upcoming "LangChain NY Meetup: LLM Wikis and
    Managing Agent Context" is listed on the Bond AI New York calendar
    (discovery-level corroboration only). Meetup Pro listing (357 members) is
    a network landing — discovery only, not a claim-bearing source.
- New York AI Engineers — RETAINED (active).
  - Channel: open search; group Meetup page (meetup.com/new-york-ai-engineers/).
  - 9,664 members; run by Fonzi (talent marketplace; communities in NY and
    SF). In-person: "NY AI Engineers: July" 2026-07-29 at Fonzi HQ, 25 Kent
    Ave, Ground Floor, New York (1 attendee); "AI Engineers: Devs & Drinks"
    2026-07-23; "AI Engineers: Poker & Game Night" 2026-07-16; "AI Engineers
    Presents: Founders to Follow" 2026-06-24.
- Papers We Love NYC — RETAINED (active).
  - Channel: open search; chapter page paperswelove.org/chapter/newyork/ +
    group Meetup page (meetup.com/papers-we-love/).
  - 4,241 members; chapter page states "meets monthly at different locations
    throughout the city." In-person: "Rylan Talerico on Zep: A Temporal
    Knowledge Graph Architecture for Agent Memory" 2025-10-15 at Datadog,
    620 8th Ave (76 attendees); "Michael Vaughn on EXE" 2025-09-17 at Datadog
    (86 attendees); "Alex Weisberger on Performal" 2025-03-12 at Datadog
    (104 attendees). Platinum sponsor Two Sigma per chapter page.
- ODSC AI New York — RETAINED (active).
  - Channel: open search; group Meetup page (meetup.com/open-data-science-ny-odsc/).
  - 6,931 members; "Part of ODSC-AI-Community - 33 groups". In-person: "Mind
    Games: Understanding AI Through Play" 2026-07-23 at Studio 1505, 307 West
    38th Street, New York (27 attendees). Most upcoming events are online
    webinars (e.g. "Building Context-Aware AI Agents" 2026-09-09 online) and
    out-of-city conferences (ODSC AI West 2026-10-27 San Francisco); the
    in-person 2026-07-23 event is the claim-bearing activity fact.
- Startup Grind NYC — RETAINED (active).
  - Channel: open search + Bond AI calendar; group Meetup page
    (meetup.com/startup-grind-nyc/) + own event feed startupgrind.com.
  - 13,276 members; "Part of Startup Grind - 17 groups". Own-page sponsorship
    line "Sponsor an event! - https://www.startupgrind.com/sponsor" is a
    network-level participation route, not a standing NYC-chapter co-host
    invitation (false-positive risk avoided per calibration). Recurring AI
    programming: "The AI Briefing by Startup Grind" at Civic Hall, 124 East
    14th Street — "The AI Briefing - Financial Services" 2026-04-10, "The AI
    Briefing - The C-Suite Gap in AI Readiness" 2026-07-10, upcoming "The AI
    Briefing - Agentic Governance" 2026-08-14 (per the group's own event
    feed); "The AI Workflow Exchange: Live Builder Demos" upcoming 2026-08-25
    at The Yard: Herald Square, 106 West 32nd Street.
- Columbia AI Club CUB — RETAINED (active, university).
  - Channel: open search; organizer-owned Luma event page
    (luma.com/t4kmbswi).
  - "Columbia CUB AI Summit 2026" 2026-04-26 (12:30-5:00pm) in person at
    International Affairs Building, Room 1501, Columbia University (28 went;
    page states 100+ students/researchers/industry leaders). About CUB: "the
    only university-wide AI club" at Columbia, founded Fall 2025, "370+
    members and a 14-person board."
- NYU Data Science Club (DSC@NYU) — RETAINED (active, university).
  - Channel: open search; official site dscnyu.org.
  - Official site describes the club as bringing "the Data Science community
    at NYU together"; "Datathon 2026" 2026-04-10..2026-04-12 in person at
    NYU (kickoff at 19 West 4th, Room 101; hosted with Pulse Foundry AI);
    earlier Datathon 2025 site describes the club founded in 2019. NYU CDS
    student-groups page lists DSC and WiDS as student groups.
- CryptoMondays NYC — RETAINED (active, web3).
  - Channel: open web3 search; group Meetup page (meetup.com/cryptomondaysnyc/).
  - 11,648 members; first CryptoMondays chapter (founded 2018); site
    cryptomondays.io. In-person: "CryptoMondays (Bitcoin)" 2026-04-20 at
    Pubkey, 85 Washington Pl (9 attendees); "CryptoMondays NYC Featuring
    Splyce" 2026-04-13 at Pubkey (9 attendees); "CryptoMondays Wall St"
    2026-04-06 at Pubkey (24 attendees). Weekly Monday cadence at Pubkey.
- AI Salon New York — RETAINED (active, cohost_open true).
  - Channel: open search + Bond AI calendar; organizer-owned Luma event page
    (luma.com/AI-Salon-NewYork-March-2026).
  - Chapter-based global community (www.AiSalon.ai); NYC event 2026-03-26/27
    in person at Casa 51, 625 W 51st St, New York (hosted by chapter leads
    Blanca Ireri Espinosa Saviñón, Sandy McCarron, Nicky Schaub, Jasper
    Wognum, Jeffrey D Abbott). Own-page sponsorship ticket "Apply to be a
    Sponsor - Sponsor AI Salon New York and connect with the city's leading
    voices in artificial intelligence" (quoted in cohost_evidence_phrase).
    Organizer LinkedIn confirms "first AI Salon of 2026" was held (2026).
- Data Umbrella — RETAINED (intermittent, digital-only).
  - Channel: open search; group Meetup page (meetup.com/nyc-data-umbrella/).
  - 3,340 members, New York, NY, US. Recent listed events are online-only:
    "Dataverse: an Open-Source Platform for Research Data" 2026-02-10
    (online), "PREreview" 2026-01-29 (online), "The Internet Archive for Data
    Scientists" 2026-01-20 (online), "PyData Global 2025" 2025-12-09
    (online). Digital-only marker applied; in-person presence question.
- AI Professionals NYC Machine Learning — RETAINED (intermittent,
  digital-only).
  - Channel: open search; group Meetup page (meetup.com/nyc-machine-learning/).
  - 12,310 members, New York, NY, US. Recent/upcoming listed events are
    online-only: "Networking for AI Professionals around the world"
    2026-08-13 (online), "Get Google AI Certified" 2026-08-17/2026-08-10
    (online), "Info Session: Central Europe" 2026-08-06 (online). No
    in-person NYC event listed within the 12 months before accessed_on.
    Digital-only marker applied; in-person presence question.
- The AI Collective New York — RETAINED (intermittent).
  - Channel: open search; organizer-owned Luma event page
    (luma.com/aic-ny-5-12) + chapter newsletter.
  - Global non-profit "uniting 200k+ pioneers across 100+ forums". NYC
    in-person: "B2B Fintech Founders Lunch: Using Content & Events to Scale"
    2026-05-12 at Fabrik NYC (past event; registration-required address);
    newsletter reports the NYC chapter's Research Roundtable with Tandem AI
    drew 170+ attendees. Single recent in-person event; cadence unproven.
- New York R User Group — RETAINED (dormant).
  - Channel: R network search; group Meetup page (meetup.com/new-york-r-users-group/).
  - 1,394 members, New York, NY, US. About text includes "Press inquiries,
    event space, food and drink sponsorship are welcome! please contact
    info@nycdatascience.com" — an old sponsorship line recorded as observed
    fact, NOT flagged cohost (false-positive risk avoided for dormant group
    per Budapest AISHK calibration). Last listed events: "Develop prompts for
    a Language Model (LLM) from the ground up" 2024-02-01 (online, 8
    attendees); "Readability Counts" 2022-09-27 (online). No in-person event
    within the 12 months before accessed_on.
- R-Ladies New York — RETAINED (dormant).
  - Channel: R network search; group Meetup page (meetup.com/rladiesnyc/) +
    own site rladiesnyc.org.
  - 3,114 members; "Part of RLadies+ - 251 groups". Last in-person events:
    "R-Ladies Tea and Code Hangout" 2025-06-16 at Cafe-Flor, 218 8th Ave
    (6 attendees); "BRMS2Stan: Intro to Stan for BRMS Users" 2025-05-07 at
    NYU Steinhardt (Kimball Hall), 246 Greene Street, 3rd floor (11
    attendees). No in-person event within the 12 months before accessed_on.
- NYC PyLadies — RETAINED (dormant).
  - Channel: open search; group Meetup page (meetup.com/nyc-pyladies/) + own
    site nyc.pyladies.com.
  - 4,035 members; "Part of Python Software Foundation Meetup Pro Network -
    123 groups". Last in-person event: "[In-Person] Exploring Vector Search
    and PyLadies Meet & Greet" 2024-10-24 at ElasticSearch, 45 W 27th Street
    (48 attendees); earlier "Pyladies Study Group (@GoogleNYC)" 2023-12-14.
    Site describes monthly events, but no event appears within the 12 months
    before accessed_on.
- Python for Quant Finance NYC — RETAINED (dormant, quant).
  - Channel: open quant search; group Meetup page
    (meetup.com/python-for-quant-finance-nyc/).
  - 1,421 members, New York, NY, US. Last listed events: "For Python Quants
    Bootcamp New York (paid event)" 2017-05-08 at CQF - Fitch Learning,
    55 Broad St (10 attendees); "For Python Quants Meetup" 2016-05-02 (83
    attendees). No event within the 12 months before accessed_on; retained
    as the standing NYC quant-relevant community signal (evidence gap for a
    currently active quant community is documented, not an absence claim).
- Learn Python NYC — REJECTED.
  - Channel: open search.
  - Reason: general-purpose Python learning group (6,494 members) with no
    listed event since 2020-12-12; no AI/ML/data/web3 focus evidenced on its
    own page; NYC Python + PyData NYC already cover the Python/data signal.
- NYC Data Science (meetup.com/nyc-data-science) — REJECTED.
  - Channel: open search.
  - Reason: 6,667-member data-science group whose last listed event is
    2017-06-28; nine years dormant is beyond useful historical/contextual
    context, and PyData NYC + nyhackr cover the active data-science signal.
- Based Meetup - New York — REJECTED.
  - Channel: open web3 search; Luma event page (luma.com/b7fek2i4).
  - Reason: single event page ("Based Meetup - New York" 2026-04-10 at
    Station 3 NYC, 26 Broadway; AI + Base/Coinbase stablecoin topics, 82
    went), hosted by an individual organizer (x.com/nickcryptopro); no
    standing chapter page or cadence evidence (event-week initiative
    precedent). Web3 coverage retained via CryptoMondays NYC.
- New York Robotics / NY Robotics Network — REJECTED.
  - Channel: Bond AI calendar + open search.
  - Reason: robotics-ecosystem group (nonprofit, 160+ startups); robotics is
    outside the enumerated focus taxonomy (machine_learning, data_science,
    ai, web3, quant, mixed, other) and no AI/ML/data/web3 community-meetup
    focus is evidenced on its official pages; the Bond AI "So You Want To Get
    Physical?" event is a discovery listing only.
- NYC Quantum Computing Meetup — REJECTED.
  - Channel: Meetup city-directory sweep.
  - Reason: quantum-computing interest group; outside the enumerated focus
    taxonomy and unrelated to the AI/ML/data/Web3/quant audience question
    (quant here means quantitative finance, not quantum computing).
- NYC Tech Meetup — REJECTED.
  - Channel: Meetup city-directory sweep.
  - Reason: general technology/innovation community; no AI/ML/data/web3
    community-meetup focus evidenced (JuniorDevSG precedent).
- Metis NYC data science group (meetup.com/metis-new-york-data-science) —
  REJECTED.
  - Channel: open search.
  - Reason: group page returns "Group not found" (404) at access time; no
    standing page to cite.
- GDG Brooklyn — REJECTED (as standalone).
  - Channel: open search (GDG chapter list).
  - Reason: duplicate chapter of the same network; GDG NYC is retained as the
    city chapter and Brooklyn events are not separately needed for the
    audience question.
- Columbia Business School AI Club — UNRESOLVED.
  - Channel: open search; official page groups.gsb.columbia.edu/aic/.
  - Reason: official page exists (912 members, 125 events, 21 officers) but
    shows no upcoming events and no dated recent in-person event was verified
    from the page in this pass. Columbia AI Club CUB covers the Columbia
    university AI signal. Not an absence claim.
- NYU AI Society / other NYU AI student organizations — UNRESOLVED.
  - Channel: open search (site:nyu.edu / engage.nyu.edu).
  - Reason: no accessible official society page with community/event evidence
    surfaced in this pass. NYU Data Science Club covers the NYU student
    signal. Not an absence claim.
- Women in AI NYC / AI-Powered Women NYC chapters — UNRESOLVED.
  - Channel: open search (womeninai.co, LinkedIn).
  - Reason: NYC chapter references are new/2026 launch signals on LinkedIn;
    no official chapter events page surfaced in this pass. Not an absence
    claim.
- Women in Web3 NYC — UNRESOLVED.
  - Channel: open web3 search.
  - Reason: no official NYC chapter events page surfaced in this pass; web3
    representation retained via CryptoMondays NYC. Not an absence claim.
- Columbia AI (ai.columbia.edu) university initiative — REJECTED (as
  community).
  - Channel: open search.
  - Reason: university-wide institutional initiative/events calendar, not a
    student club or community with its own meetup cadence; Columbia AI Club
    CUB is the retained club record.
- NYU Center for Data Science (cds.nyu.edu) — REJECTED (as community).
  - Channel: open search.
  - Reason: academic department, not a community; its student groups (DSC@NYU,
    WiDS) are the community layer; DSC@NYU is retained.
- Bond AI - New York (luma.com/genai-ny) — REJECTED (as community/source).
  - Channel: event roundup.
  - Reason: aggregator events calendar promoting other communities' events;
    directory/aggregator listings are never final evidence (community_sources
    boundary). Used as discovery only to surface LangChain NY, NYC Creative
    AI, and New York Robotics.
- Startup Grind "Sponsor an event!" line — recorded as observed fact, NOT
  flagged cohost (network-level sponsorship route, not a standing NYC-chapter
  co-host invitation; false-positive risk avoided per calibration).

## Discovery summary

- Channels exercised: AI Tinkerers directory, Meetup Pro PyData + R networks,
  open-query families (AI/ML/data/web3/university/coworking/quant/women),
  Meetup city-directory sweep, web3 Luma searches, event roundups (Bond AI,
  TechMeetups.io, GarysGuide, trymimetic, startupgrind events), LinkedIn
  signals. Candidates logged: 42 dispositions -> 27 retained, 11 rejected,
  4 unresolved (counts include subsumed/duplicate dispositions).
- Evidence yield: 27 retained records — 20 active, 3 intermittent, 4 dormant.
  Record count is descriptive, not a target; New York is the largest market
  in the five-city set and yielded more active standing communities than
  Budapest/HK/SG without relaxing the official-page rule.
- Category coverage: AI/ML very strong (AI Tinkerers NYC, NYAI, NYC AI
  Developers/AICamp, GDG NYC, Global AI NY, Mindstone, NYC Creative AI,
  LangChain NYC, New York AI Engineers, ODSC AI NY, Startup Grind AI
  Briefing, Columbia CUB, AI Salon NY, The AI Collective NY), data science
  (PyData NYC, nyhackr, WiMLDS, NYC Python, Papers We Love, Data Umbrella,
  R-Ladies dormant, New York R User Group dormant, NYC PyLadies dormant),
  web3 (CryptoMondays NYC; Based Meetup single-event and Ethereum NYC
  conference rejected as non-communities), quant (Python for Quant Finance
  NYC dormant — standing NYC quant community signal; no currently active
  standing quant community page surfaced, documented as an evidence gap, not
  an absence claim), university (Columbia CUB, NYU DSC).
- In-person evidence: 20 active records each carry a page-visible in-person
  event dated 2025-08-12..2026-08-11; 3 intermittent (Data Umbrella
  digital-only, AI Professionals NYC ML digital-only, The AI Collective NY
  single recent in-person event); 4 dormant have no in-person event within
  12 months.
- Co-host evidence: 5 true flags, each with an own-page quoted phrase and a
  manual follow-up question (PyData NYC sponsorship invitation on official
  site; NYAI "Partner with us to lead an event or workshop" + sponsorship
  application; NYC AI Developers "co-host your events" + partnership
  invitation; GDG NYC "Explore sponsorship opportunities"; AI Salon New York
  "Apply to be a Sponsor"). All true flags carry needs_human_verify true +
  a question. False-positive risks avoided: Startup Grind's network-level
  "Sponsor an event!" line and New York R User Group's stale sponsorship
  line recorded as observed facts, NOT flagged (Budapest/HK calibration);
  event-level venue hosting (nyhackr "Thank you to NYU for hosting us") not
  treated as a standing invitation.
- Official-source quality: all 27 retained records cite group/organizer-owned
  pages (chapter sites, group Meetup pages, org websites, organizer-owned
  Luma event pages). Meetup/Luma group pages qualified as claim-bearing when
  group-controlled (community_sources.md boundary); organizer-owned Luma
  event pages (LangChain NYC, ComfyUI/NYC Creative AI, Columbia CUB, AI
  Salon NY, The AI Collective NY) qualify when they visibly show group/event
  facts (HK/SG Luma precedent). No language-boundary entries required this
  pass (all retained pages were English-accessible).
- Depth decision for remaining cities (Montreal): continue the recipe
  unchanged; keep the Meetup city-directory sweep; keep organizer-owned Luma
  calendars and event pages as claim-bearing sources when group-owned and
  fact-bearing; keep the AI Tinkerers directory -> chapter-page flow; keep
  the false-positive discipline on co-host flags (event-level and
  network-level sponsorship lines are observed facts, not flags).
