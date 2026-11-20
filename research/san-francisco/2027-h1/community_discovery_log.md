# Community discovery log — San Francisco, 2027 H1

Research date: 2026-11-20. Output: `communities.raw.json` (17 records: 12 active, 3 intermittent, 2 dormant).

## Method and rule applied

Discovery used the plan-event community source list (AI Tinkerers chapter directory, PyData/R User Groups networks, Web3 Events Guide, Crypto Events Global) plus open search on Meetup and organiser sites. A directory or aggregator was used only to find a candidate; every record's `source_url` is the group's or organiser's own claim-bearing page, and the activity claim is carried in `evidence.observed_facts` with a dated event.

`activity_status` was assigned by evidence, not by reputation:

- `active` — the group's own page shows a dated in-person event **dated before** `accessed_on` (2026-11-20) and inside the preceding 12 months.
- `intermittent` — the page exists but the recent evidence is irregular, global/online, or has moved to another platform.
- `dormant` — the page shows no activity for 12 months or more.

A future-dated listing is not activity evidence. Two records were corrected on that point this pass (below); the previously published edition of this file had counted future December 2026 events as the sole dated fact for two groups, and the validator passed only because the string "fetched 2026-11-20" satisfied its recency check. That is a validator artefact, not evidence, and it is not relied on.

## The two named sources the reviewer asked for, attempted once each

Attempt 1 — Luma San Francisco calendars. Fetched `https://luma.com/discover/sf/crypto` (HTTP 200, 158 KB) and `https://luma.com/discover/sf/ai` (HTTP 200, 484 KB) with a desktop user agent on 2026-11-20.

- Both pages are machine-readable at the listing level, but both render only an "Upcoming Events" block. The crypto page's earliest ISO date is 2026-11-28 and the AI page's earliest is 2026-11-20, so neither yields a **past**-dated 2026 fact.
- Result: not usable as activity evidence on its own, but the crypto calendar did name live Web3 hosts, including `SF Bitcoin Devs` for a "Bay Area Bitcoiner Holiday Party and BitDevs Socratic Seminar" at 38 Keyes Ave. Following that one link produced the SF Bitcoin Devs record below, whose own Meetup page carries past-dated San Francisco editions.
- Also named on those calendars and not turned into records: Introduction.com, NODE, DeepEval, Vibe House, Bay Area AI Artists Group. No past-dated in-person fact was reachable for them within this pass.

Attempt 2 — The AI Collective, SF Bay Area chapter. Fetched `https://www.aicollective.com/chapters/sf-bay-area`, which returns HTTP 200 with the literal page title "Chapter Not Found". Fetched `https://aicollective.com/hubs/bay-area`, which returns HTTP 200 but is a client-side app: the extracted page text is the single string "SF Bay Area Hub" with no dates and no event list.

- Result: failed. The chapter exists (the site's own navigation and third-party event pages both name it), but no dated in-person fact could be read from the organiser's own page today, so no record was created. Recording it as `intermittent` would have been a guess in the other direction.

Net: of the two named sources, one yielded a usable lead (SF Bitcoin Devs) and one failed outright. The remaining new records below came from the same open-web sweep, and each rests on a first-party dated page; none is padded from `intermittent` or `dormant`.

## Active (12)

- AI Tinkerers — San Francisco. Own page lists past offline editions "SF × MIT Hack Day: Energy" on 2026-11-08 10:00-19:30 PT at AGI House SF, 170 Saint Germain Avenue (45 capacity), and "Agents, Everywhere" global hackathon on 2026-09-12 10:00-17:00 PT in San Francisco; upcoming December editions on 2026-12-03, 2026-12-04 and 2026-12-08.
- SF AI (meetup.com/sfbay-ai). 16,434 members; in-person developer nights on 2026-11-12 (AWS Builder Loft, 525 Market St) and 2026-11-18 (50 Beale St).
- San Francisco AI Code and Coffee. 2,839 members; Sunday park meetup on 2026-10-25 (35 attendees) at Salesforce Park. A 2026-11-22 edition is listed on the page but falls after the 2026-11-20 access date, so it is recorded as upcoming only, with no attendance figure, and is not counted as activity evidence.
- AI Builders and Learners SF. 3,709 members; in-person "Own Your AI" hack night on 2026-11-03 in San Francisco (15 attendees); its 2026-12-08 and 2026-12-09 sessions are listed as online.
- SF Python. 13,223 members; 2026 events on 2026-06-17, 2026-07-29 and 2026-09-09 plus PyBay 2026 on 2026-10-03; page states 20+ live events a year and a monthly second-Wednesday presentation night.
- AGI House SF. Voice AI Hackathon dated 2026-09-19; page states 80+ build-a-thons and hackathons and a cadence of up to five events a week.
- Hedge West SF — Quant, Data, and AI. 267 members; quarterly meetups on 2026-06-02 (44 attendees) and 2026-09-01 (48 attendees) at House of AI, 40 Boardman Pl.
- Bay Area AI War Room. 1,447 members; SF Edition on 2026-10-17 10:00-12:00 PDT at JOE & THE JUICE, 525 Market St (25 attending, status PAST) and Berkeley Edition on 2026-11-07 (31 attending); monthly series on the 1st and 3rd Saturdays.
- SF Bitcoin Devs (new, Web3). 2026-10-01 Socratic Seminar 74 at DG717, 717 Market St, San Francisco (20 going) and 2026-09-03 Seminar 73 at Presidio Bitcoin, 38 Keyes Ave (12 going); own site lists Seminars 66-76 from 2026-01-08 to 2026-11-05, one per month.
- Funding the Commons (new, DeAI/Web3). Own site's past-events list carries "Funding the Commons SF 2026: Intelligence at the Frontier" and "Intelligence at the Frontier Hackathon", both 2026-03-14 to 2026-03-15 at Frontier Tower, San Francisco, offline format, 150-200 selected builders.
- ClawCamp — San Francisco chapter (new, DeAI-adjacent). Own events page lists "ClawMax.ai Build Night SF" on 2026-11-18, "ClawCamp Campfire: Sovereign AI - Own Your Stack" on 2026-11-02 at Tenki San Francisco, 590 Howard St, and a Dell x NVIDIA hackathon in San Francisco on 2026-10-25/26.
- Decentralized AI Builders Meetup (BitsLab) (new, DeAI/Web3). Luma event page records a past offline edition on 2026-03-04 17:00-20:30 PST at AWS Builder Loft, 525 Market St, with an AI-x-crypto agenda (x402, ERC-8004, agent-to-agent commerce).

## Intermittent (3)

- PyData San Francisco Bay Area — 696 members, but the 2026 entries on its page are global PyData conferences (Yerevan 2026-07-23, London 2026-06-05), not local meetups.
- SF Data and AI Engineering — 2,271 members; most recent listed event is 2026-09-09 in Amsterdam, and the page now points to `lu.ma/aiengineering` for scheduling.
- Blockchain Global Group — 499 members; last listed events 2025-12-16 and 2025-10-21, 2 attendees each, nothing in 2026.

## Dormant (2)

- SF Ethereum — 2,444 members; most recent listed event 2022-12-13 at Trellis Coworking, 981 Mission St.
- CryptoMondays San Francisco — 1,684 members; most recent listed date 2025-09-22 (2 attendees), nothing in 2026.

## Web3 and DeAI, stated plainly

The earlier version of this file said no San Francisco Web3 group with evidenced 2026 activity existed on any platform reachable that day. That was too strong. It remains true that the two Web3 groups on the old record (SF Ethereum, CryptoMondays SF) are dormant, but four Web3- or DeAI-facing groups with dated 2026 in-person evidence were reachable:

- SF Bitcoin Devs is unambiguously active (20 and 12 attendees at its last two San Francisco seminars) and is the strongest Web3 record in the set.
- Funding the Commons ran a 150-200 person DeAI-adjacent hackathon and festival in San Francisco on 2026-03-14/15 and is advertising a 2027-03-13/14 San Francisco forum.
- ClawCamp SF runs sovereign/local-AI build nights and hackathons in the city on a near-monthly cadence.
- The Decentralized AI Builders Meetup is the most directly DeAI-titled event found, but it is evidenced by a single published edition rather than a recurring calendar.

What is still missing: no Ethereum-side or general-purpose crypto meetup with 2026 San Francisco activity. The two tracked Ethereum/crypto groups are dormant, ETHGlobal's published 2027 stops are Cannes (Apr 14-16), New York (Jun 14-16), Tokyo (Aug 23-25) and Lisbon (Oct 13-15), and Solana Breakpoint's first US edition is at Pier 48 on 2027-09-08..10, outside H1.

## DeAI

No record carries a "decai" tag because the schema's focus-tag enum has no such value (`ai`, `machine_learning`, `data_science`, `web3`, `quant`, `mixed`, `other`). The DeAI flank is carried by three records instead: Funding the Commons (`ai` + `web3`), the Decentralized AI Builders Meetup (`ai` + `web3`) and ClawCamp (`ai` + `other`, recorded for its sovereign/local-AI framing). Hedge West SF remains the closest match to the campaign's quant/Numerai audience.

## Co-host openness

No group in this set publishes language inviting co-hosting, sponsorship of external events, or venue partnership on the page used as evidence, so every record carries `cohost_open: false` with a null evidence phrase. That is an absence-of-evidence state, not a claim that none of them would co-host; each record carries a question about co-hosting instead. Sponsorship appears in several places (AI Tinkerers names Omnara, Casco, WorkOS; SF AI names Google, AWS, Anthropic; Hedge West names Novum Cove and ExtractAlpha), but sponsor logos are vendor relationships, not an invitation to community co-hosting, and were not treated as one.

## Contact handling

No email address, phone number or private handle is stored. `contact_info` is null for every record: the pages publish organiser names and sponsor names but the obvious public route is the platform's own message form, which is not a stable public URL from the claim-bearing page. Verification questions therefore go through the group page rather than a captured address.

## Access failures

- The AI Collective's SF chapter page (`aicollective.com/chapters/sf-bay-area`) returns "Chapter Not Found"; its hub page (`aicollective.com/hubs/bay-area`) renders client-side with no readable dates. Both attempted 2026-11-20.
- Luma San Francisco calendars (`luma.com/discover/sf/crypto`, `luma.com/discover/sf/ai`) list upcoming events only, so they cannot evidence past activity directly.
- Meetup group pages for `/sf-ai/`, `/sf-ai-meetup/`, `/papers-we-love-sf/`, `/bay-area-blockchain/`, `/bay-area-web3/` and `/sf-blockchain/` all return "Group not found"; three of those 404s are recorded here only as negative search results, not as evidence about any group.
