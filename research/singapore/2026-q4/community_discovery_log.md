# Singapore local-communities discovery log — Run A v2.6

- Task: t_4f544543 (Run A v2.6: Singapore communities research)
- Research root: `~/repo_dev/coe-events`; city dir: `research/singapore/2026-q4/`
- Date checked: 2026-08-11 (all entries; accessed_on 2026-08-11)
- Plan: `local/runA-v2.6-communities-plan-v1.md` (Singapore section, schema 2.3)
- Budapest/HK calibration: PASS (Budapest review + HK review both passed the
  same evidence gate); depth decision: recipe unchanged, keep Meetup
  city-directory sweep, keep group-controlled Meetup/Luma pages as claim-bearing
  sources, keep organizer-owned Luma event pages when fact-bearing, keep the
  language boundary (language-neutral facts only for non-English pages).
- Scope: evidence-bound community discovery only. No venue/calendar/city_input
  changes, no bundle/summary, no commits. Discovery listings never supply final
  evidence; every retained record cites a group/organizer-owned page.

## Channels checked

- AI Tinkerers: aitinkerers.org/all_cities directory -> Singapore chapter
  singapore.aitinkerers.org (official chapter page). Retained.
- Meetup Pro networks: PyData network landing (meetup.com/pro/pydata/) and R
  User Groups network (meetup.com/pro/r-user-groups/) used as discovery entry
  points; group-owned Meetup pages used as claim-bearing sources. Retained:
  PyData Singapore (dormant), RUGS (via official Luma calendar). R-Ladies
  Singapore surfaced via R network search (retained dormant).
- Open searches (recipe query families, English; no local-language pages
  required this pass — Singapore communities are predominantly
  English-accessible):
  - "AI Tinkerers Singapore chapter"
  - "PyData Singapore meetup official" / "meetup.com pydata-sg"
  - "R User Group Singapore meetup official" / "RUGS Singapore"
  - "AI meetup Singapore official meetup.com 2026"
  - "machine learning community Singapore meetup official 2026"
  - "data science meetup Singapore official community 2026"
  - "web3 community Singapore meetup official blockchain 2026"
  - "GDG Singapore meetup official 2026" / "AWS User Group Singapore meetup"
  - "Women in AI Singapore chapter events official"
  - "NUS OR NTU OR SMU AI club student society official events 2026"
  - "quantitative finance meetup Singapore quant community official"
  - "open source Singapore meetup community 2026"
  - "Superteam Singapore community Luma events" / "Ethereum Singapore"
  - "ClaudeSG" / "Vibe Coders Singapore" / "OpenClaw Singapore" /
    "Lorong AI" / "The AI Collective Singapore" / "Build Club Singapore"
- Meetup city-directory sweep (meetup.com/find/sg--singapore/) — surfaced
  Global AI Construct (Global AI Singapore), JuniorDevSG (rejected: general
  developer group, not AI/ML/data/web3-focused); used as discovery only.
- Event roundups (discovery only): The Generative Beings weekly newsletter
  (thegenerativebeings.com/blog/ai-events-this-week-2026-08-10), SG AI Oasis
  (sgaievent.vercel.app — student-run aggregation site, not a community's own
  page), TechMeetups.io, devsgowhere.com, connections.sg, LinkedIn community
  maps (Brian Chew's "unofficial map of Singapore's AI communities") — all
  discovery/corroboration only.
- Web3-specific: luma.com/superteamSG (official), luma.com/op6tobdu (OpenClaw
  SG), luma.com/rugs (RUGS), ethereum.sg (event-week initiative — rejected),
  btc-singapore.com (one-day conference — rejected), Facebook-only groups
  (rejected/unresolved per HKRUG precedent).

## Candidates (disposition)

- AI Tinkerers Singapore — RETAINED (active).
  - Channel: aitinkerers.org directory + chapter page.
  - Official page: https://singapore.aitinkerers.org/ (chapter site). Page
    reports "Local cadence 9 recent events"; in-person events include
    AI Tinkerers x Redis: Built for Speed 2026-08-05 (+130), Tencent Cloud
    Hackathon 2026-07-22 (+380), ElevenLabs Side Quests Demo Night 2026-05-21
    (+147), The Agentic Future 2026-04-21 (+153), Age of AI & Infrastructure
    2026-02-11 (+130), ElevenLabs Worldwide Hackathon 2025-12-11, AIT x Redis x
    Cloudflare Mini-Hack 2025-10-24, AI Agents Showcase 2025-10-07, scalable
    agentic workflows 2025-08-12. No chapter member count on the page.
- PyData Singapore — RETAINED (dormant). Fix R1 (data review P1): dormancy
  claim now bound to the archived official group page (Wayback snapshot
  2023-03-30, https://web.archive.org/web/20230330135945/https://www.meetup.com/pydata-sg/),
  which visibly lists "PyData Meetup - Tracking Economic Change with Open
  Data" (event 266721848, Mon Dec 2, 2019, 6:30 PM) as the last local meetup,
  with only a partner event (Apr 2020) and PyData Global 2021/2022
  (GLOBAL ONLINE CONFERENCE) after it.
  - Channel: Meetup Pro PyData network; meetup.com/pydata-sg/ (group page).
  - 5,689 members; live group page lists network events (PyData London 2026,
    PyData Global 2025, PyData London 2025, PyData Virginia 2025) as the most
    recent listed events; no local in-person event appears in either the live
    page or the archived page within the 12 months before accessed_on.
- RUGS (R User Group - Singapore) — RETAINED (intermittent).
  - Channel: R User Groups network + open search; official calendar
    luma.com/rugs (group-owned).
  - Upcoming in-person meetup 2026-08-20 at Autodesk Asia, 3 Fusionopolis Way,
    #10-21 Symbiosis, Singapore (7-9pm; free). Meetup group
    (meetup.com/r-user-group-sg) is private; last visible past event there is
    2025-05-21. No in-person event within the 12 months before accessed_on on
    the official page; cadence irregular.
- Global AI Singapore — RETAINED (active).
  - Channel: open search; official chapter page
    globalai.community/chapters/singapore/.
  - 763 members, 12 events, 5 organizers. In-person: SG AgenticNights July
    Meetup 2026-07-29; AgentCamp - Singapore 2026-05-21; SG Agentic Nights
    (Jan-Apr 2026 series); Nov 2025; Oct 2025; AgentCon 2025 - Singapore
    2025-09-09. Upcoming: Global AI Construct Singapore 2026-08-27, AgentCon -
    Singapore 2026-11-05.
- GDG Singapore — RETAINED (active, cohost_open true).
  - Channel: open search; official chapter page
    https://gdg.community.dev/gdg-singapore/ + group Meetup page
    meetup.com/gdg-singapore.
  - 6,044 members (chapter page; Meetup shows 4,045). In-person: Google
    Builders Night 2026-08-04 (external registration), Google I/O Extended
    Singapore 2026-06-27, Google Cloud Next Extended 2026-06-27, GDG Monthly
    Meetup #2604 2026-04-28, Build with AI Singapore 2026-03-28 (all at Google
    Developers Space, 80 Pasir Panjang Rd). Partnership invitation on the
    chapter page's own About text (quoted in cohost_evidence_phrase).
- AWS User Group Singapore — RETAINED (active).
  - Channel: open search; meetup.com/aws-sg/ (group page).
  - 9,990 members ("Part of Global AWS User Group Community - 416 groups").
    Monthly meetups; in-person: AWS User Group Meetup June 2026 (2026-06-17, 175
    attendees) and AWS Security User Group Meetup (2026-07-01) at Amazon Web
    Services Singapore, 2 Central Blvd, IOI Central Boulevard Towers, Level 5;
    upcoming AWS Community Day Singapore 2026-08-22 (SGD 80, Eventbrite).
- Free and Open Source Singapore (Open Source Singapore) — RETAINED (active).
  - Channel: open search; meetup.com/free-and-open-source-singapore/ (group
    page).
  - 1,422 members; group states quarterly meetup aim (last Thursday of month).
    In-person: "Open source AI unlocked | In collaboration with TGB" 2025-09-25
    at SQ Collective, 65 Mohamed Sultan Road; upcoming "Build Better with Open
    Source & AI" 2026-08-27 at SQ Collective (Luma signup 9zcnfaua). Event
    description confirms group also goes by Open Source Singapore.
- Python User Group Singapore (PUGS) — RETAINED (active).
  - Channel: open search; official site pugs.org.sg + official Luma calendar
    luma.com/pugs (group-owned; site confirms migration from Meetup to Luma).
  - Monthly NLB LearnX community, free and open. Luma calendar lists in-person
    events 2025-09-26, 2025-10-03, 2025-10-10, 2025-10-31, 2025-11-28,
    2026-01-30, 2026-06-19, 2026-06-22, 2026-06-26 (library@harbourfront).
- ClaudeSG (Claude Singapore Community) — RETAINED (active).
  - Channel: open search; official site claudecode.sg + Luma calendar
    luma.com/claudesg.
  - Non-profit community "dedicated to teaching and building with Claude";
    1,500+ builders in network claim on site. In-person events: ClaudeSG x AWS x
    Anthropic 2026-08-12, Claude for Communities 2026-08-24 (WeWork), Claude101
    LIVE 2026-08-26 (*SCAPE), plus Apr-Jul 2026 series on Luma (19 events).
- The Generative Beings (TGB) — RETAINED (active).
  - Channel: open search; official platform thegenerativebeings.com.
  - Singapore-based AI community (Pte Ltd) with a physical hub (TGB GenAI Lab at
    SQ Collective). 3,910 members, 634 events platform-wide; events page lists
    124 Singapore events incl. in-person 2026 masterclasses/meetups (e.g.
    Claude Code for absolute beginners 2026-08-20, Build Your Hermes AI Agent
    2026-08-22).
- Singapore AI & Robotics Demo Nights — RETAINED (active).
  - Channel: open search; official Luma calendar luma.com/singapore-demo-nights
    (series-owned; formerly "Singapore AI Showcase").
  - Monthly in-person demo nights at National Library / Lee Kong Chian
    Reference Library, 100 Victoria St (Jun 2026 edition, 696 went; Aug 11 2026
    edition = accessed day; calendar Dec 2024-Dec 2026). Hosted by Menlo
    Research.
- Superteam SG — RETAINED (active).
  - Channel: open web3 search; official Luma calendar luma.com/superteamSG.
  - Solana ecosystem community of founders/operators; "200+ events and
    counting"; weekly Thursday Lunch (108 events since 2025-08-11, e.g.
    2026-08-13); Solana Summit Singapore 2026-10-06. Website sg.superteam.fun
    linked from calendar.
- OpenClaw Singapore (Claw SG) — RETAINED (active).
  - Channel: open search + LinkedIn; organizer's own Luma event pages
    (luma.com/op6tobdu first event; luma.com/kdltg63f AWS edition).
  - OpenClaw AI-agent builder community organized by The AI Capitol supporting
    Claw SG. In-person: first OpenClaw Singapore event 2026-02-27 at SQ
    Collective x Gen-AI Labs (461 went), OpenClaw Singapore x AWS 2026-03-23 at
    IOI Central Boulevard Towers (724 went), ISCA x OpenClaw SG 2026-04-15.
- Ads & AI Singapore — RETAINED (active).
  - Channel: SQ Collective calendar + open search; organizer's Luma event pages.
  - Numbered in-person meetup series for AI marketing startups/builders at SQ
    Collective x Gen-AI Labs, 65 Mohamed Sultan Rd. #11 (2026-06-18, 180 went),
    #10 (2026-05-06), upcoming #12 (2026-08-19). Hosted by Martin Bertilsson.
- Lorong AI — RETAINED (active).
  - Channel: open search; official site lorong.ai + Luma calendar
    (luma.com/Ai-labs).
  - Singapore AI hub bringing together government, industry, research; site
    states 300+ core members, 8,500+ community network, 200+ events annually;
    weekly AI Wednesdays; Luma calendar lists 382 events (217 within 12 months
    before accessed_on; e.g. 2026-08-05, 2026-08-06; upcoming 2026-08-12/13/14).
    Now operating at One-North and 22 Cross Street.
- NUS Fintech Society — RETAINED (active, university).
  - Channel: open search; official site fintechsociety.comp.nus.edu.sg.
  - University society with ML, Blockchain, Quantitative, Software Development
    departments; flagship NUS Fintech Summit 2026 held in person 2026-01-05..09
    at NUS (opening ceremony and demo day physical at COM3 MPH; hackathon on
    XRPL; society's site links nusfintechsummit.com).
- NUS SoC AI Society (AISOC) — RETAINED (active, university).
  - Channel: open search; official site nusaisociety.org.
  - Student AI research/engineering society at COM1, 13 Computing Dr. Events
    page lists in-person "Computer Vision: Beyond Image Classification"
    2026-03-30 at COM3-01-20 (SR11) and NUS120 Open House 2026-03-07 (Tembusu
    College, UTown); Telegram channel states 500+ members.
- Vibe Coders SG — RETAINED (active).
  - Channel: open search + TGB newsletter; official Luma calendar
    luma.com/VibeCodersSG + group Meetup page (48 members).
  - "A cozy community to share what we're building with AI every month";
    monthly in-person shareouts (2026-04-17, 2026-05-28, 2026-06-19,
    2026-07-31; Central Area) and a jam session with Base44 on 2026-08-11
    (per TGB newsletter). Discord invite public.
- Build Club Singapore — RETAINED (intermittent).
  - Channel: open search; organizer Luma event pages + global Build Club Luma
    calendar (buildercommunityanz).
  - Build Club is a global AI community (50+ cities, 30K+ community). Singapore
    events: Build Club Singapore: AI x Marketing 2025-11-20 (148 went);
    FIRST PROMPT {2026} APAC Flagship AI Conference hosted at the AWS Singapore
    office (2026, date not confirmed from official page). Irregular local
    cadence; retained with verification question.
- ODSC AI Singapore — RETAINED (intermittent, digital-only).
  - Channel: open search; meetup.com/singapore-data-analytics/ (group page).
  - 1,495 members ("Part of ODSC-AI-Community - 33 groups"); recent listed
    events are ONLINE (Zerve x ODSC AI Datathon 2026-04-29 online, ODSC AI East
    2026-04-28 online, 2024 virtual sessions). Digital-only marker applied;
    in-person presence question.
- Women in AI - The AI Collective Singapore — RETAINED (intermittent).
  - Channel: open search; organizer's Luma event page luma.com/aic-women-in-ai.
  - In-person "Women in AI - The AI Collective Singapore" gathering 2026-03-13
    in Singapore (registration closed; The AI Collective is a global non-profit
    with a Singapore chapter; chapter page aicollective.com/chapters/singapore
    is a JS shell — event page is the claim-bearing source). Single recent
    in-person event; cadence unproven.
- R-Ladies Singapore — RETAINED (dormant).
  - Channel: R network search; meetup.com/rladies-singapore-sg/ (group page).
  - 54 members ("Part of RLadies+ - 251 groups"). Last in-person event
    "R-Ladies: Cowork Session" 2025-01-12 at NUS AS6 Level B1 COOP (2
    attendees); more recent listed events online (2024-12-21, 2024-08-30). No
    in-person event within 12 months before accessed_on.
- Ethereum Singapore (ETHSG) — REJECTED.
  - Channel: open web3 search; ethereum.sg.
  - Reason: event-week initiative (Ethereum Singapore Week, 29 Sep - 3 Oct 2025,
    ArtScience Museum) around TOKEN2049, not a standing community with its own
    events page (Budapest Blockchain Community Week precedent).
- Bitcoin Singapore (btc-singapore.com) — REJECTED.
  - Channel: open web3 search.
  - Reason: one-day conference, not a standing community.
- Singapore Blockchain Club (Facebook) — REJECTED.
  - Channel: open web3 search (facebook.com/groups/bitcoin.sg).
  - Reason: Facebook-only presence; no accessible official page (HKRUG
    precedent).
- SGUni DAO — UNRESOLVED.
  - Channel: open web3 search (linktr.ee/sgunidao, X, Telegram).
  - Reason: Linktree/Telegram/X presence only; no official events page
    accessible in this pass. Not an absence claim.
- GWAI Singapore chapter — UNRESOLVED.
  - Channel: open search (Global Women in AI).
  - Reason: launch referenced via LinkedIn (International Women's Day 2026
    gathering); no official chapter events page surfaced in this pass. Women in
    AI representation retained via The AI Collective Singapore event record.
    Not an absence claim.
- Women in AI (womeninai.co) SG chapter — UNRESOLVED.
  - Channel: open search (Women in AI Singapore).
  - Reason: no official SG chapter events page surfaced in this pass
    (womeninai.co has no SG chapter page found); The AI Collective's Women in
    AI event covers the space. Not an absence claim.
- Data Science SG / DSSG (data science community) — UNRESOLVED.
  - Channel: open search (Data Science SG / DataScience Singapore).
  - Reason: 2018-era references only (preferred.ai), no current official page
    surfaced in this pass. Data-science coverage retained via PyData SG, PUGS,
    ODSC AI Singapore. Not an absence claim.
- The AI Collective Singapore chapter page — UNRESOLVED (as standalone record).
  - Channel: open search; aicollective.com/chapters/singapore.
  - Reason: chapter page is a JS shell (no extractable content in this
    environment); the Women in AI - The AI Collective Singapore event page is
    the retained claim-bearing evidence.
- JuniorDevSG — REJECTED.
  - Channel: Meetup city-directory sweep.
  - Reason: general junior-developer interest group (bi-monthly social,
    mentoring, Code & Tell); no AI/ML/data/web3 community-meetup focus
    evidenced on its pages.
- NUS Fintech Lab / other NUS labs — UNRESOLVED.
  - Channel: open search (fintechlab.nus.edu.sg/hackathon returned a minimal
    response in this environment).
  - Reason: NUS Fintech Society record covers the university channel; lab
    pages without community/event evidence were not retained. Not an absence
    claim.
- Acacia AI Society (NUS student-led summit) — UNRESOLVED.
  - Channel: SG AI Oasis aggregation + open search.
  - Reason: annual summit event referenced via aggregation sites; no official
    society page with community/event evidence surfaced in this pass. Not an
    absence claim.
- ClickHouse / Zenika / INTERLUNAR / vendor-run tech sessions — REJECTED.
  - Channel: SG AI Oasis + open search.
  - Reason: vendor/company-run single sessions or short series (ClickHouse
    Tech Session, AI For Normies by INTERLUNAR, Zenika panel), not standing
    local communities with their own pages.
- "Build with TRAE" / TRAE events — REJECTED.
  - Channel: open search.
  - Reason: company-run product workshop events (ByteDance TRAE), not a
    standing community.
- The AI Capitol (agency) — REJECTED (as standalone).
  - Channel: open search.
  - Reason: AI automation agency; its community activity is represented via
    the OpenClaw Singapore record. Not a community itself.
- SQ Collective (coworking) — REJECTED (as standalone).
  - Channel: coworking sweep; luma.com/Ai-labs.
  - Reason: coworking venue/hub hosting many named communities (OpenClaw SG,
    Ads & AI, TGB Lab, FOSS); the venue itself is not a community record; the
    named hosted communities are retained individually.
- Base44 / Genius Central / other venues — REJECTED (as standalone).
  - Reason: venue-only; no community record without a named group page.
- PyData/ODSC network-level conference events (London, Global, East, Virginia)
  — REJECTED.
  - Reason: network events hosted elsewhere/online; not local standing
    communities (used only as context in PyData SG and ODSC records).

## Discovery summary

- Channels exercised: AI Tinkerers directory, Meetup Pro PyData + R networks,
  open-query families (AI/ML/data/web3/university/coworking/open-source/
  quant), Meetup city-directory sweep, web3 Luma searches, event roundups
  (TGB, SG AI Oasis), LinkedIn community maps. Candidates logged: 39
  dispositions -> 22 retained, 10 rejected, 7 unresolved (counts include
  subsumed/duplicate dispositions).
- Evidence yield: 22 retained records — 15 active, 5 intermittent, 2 dormant.
  Record count is descriptive, not a target; Singapore's English-accessible
  ecosystem is dense (TGB alone lists 124 SG events) and yielded more active
  standing communities than Budapest/HK without relaxing the official-page
  rule.
- Category coverage: AI/ML very strong (AI Tinkerers, Global AI, GDG, AWS UG,
  ClaudeSG, TGB, Demo Nights, OpenClaw, Lorong AI, Vibe Coders, Ads & AI,
  NUS AISOC, Build Club, Women in AI - AI Collective), data science (PyData SG
  dormant, PUGS, FOSS/Open Source SG, ODSC AI intermittent, RUGS intermittent,
  R-Ladies dormant), university (NUS Fintech Society, NUS AISOC), web3
  (Superteam SG; Ethereum SG event-week and Bitcoin conference rejected as
  non-communities). Quant remains an evidence gap for a standing SG quant
  community page (only NUS Fintech's Quantitative department and conference
  signals surfaced) — documented as an evidence gap, not an absence claim.
- In-person evidence: 15 active records each carry a page-visible in-person
  event dated 2025-08-11..2026-08-11; 5 intermittent (ODSC AI digital-only,
  Build Club single visible SG event + flagship signal, Women in AI - AI
  Collective single event, RUGS upcoming-only on official page, Vibe Coders SG
  2026 shareouts with venue unconfirmed on the Luma page); 2 dormant have no
  in-person event within 12 months.
- Co-host evidence: 1 true flag (GDG Singapore) with the quoted partnership
  invitation from the chapter page's own About text ("Have an idea for a
  partnership? We'd love to hear from you at info@gdg-singapore.org.");
  needs_human_verify true + verification question. All other records: no
  own-page sponsorship/collaboration invitation observed; cohost_open false
  with null phrase. AWS UG's Sessionize speaker call, FOSS's "wish to speak"
  line, and Lorong AI's "Collaborate with Us" CTA are participation/speaker
  routes, not co-host invitations (false-positive risk avoided; Budapest/HK
  calibration).
- Official-source quality: all 22 retained records cite group/organizer-owned
  pages (chapter sites, group Meetup pages, org websites, organizer-owned Luma
  calendars/event pages). Meetup/Luma group pages qualified as claim-bearing
  sources when group-controlled (per community_sources.md boundary);
  organizer-owned Luma event pages (OpenClaw SG, Ads & AI, Build Club SG,
  Women in AI - AI Collective) qualify when they visibly show group/event
  facts (HK Luma precedent). No language-boundary entries required this pass
  (all retained pages were English-accessible); SG AI Oasis and LinkedIn map
  used as discovery only.
- Depth decision for remaining cities: continue the recipe unchanged; keep the
  Meetup city-directory sweep; keep organizer-owned Luma calendars and event
  pages as claim-bearing sources when group-owned and fact-bearing; keep
  company-run/hub-hosted community records when the named community is
  evidenced (TGB, Demo Nights, Ads & AI, Lorong AI); do not relax the
  official-page evidence rule.
