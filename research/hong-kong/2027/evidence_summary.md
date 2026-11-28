# Evidence summary — Hong Kong (hong-kong-hk), 2027 research run

Research date: **2026-11-28**. Phase: Run A (venue / calendar / communities). No store build, no page render, no publication, no date selection.

## What this run actually produced

- **16 venue candidates** in `venues.raw.json`, all validator-clean, all with numeric coordinates from a recorded address lookup.
- Scorer tiers: **0 eligible / 13 shortlist_ready / 3 lead**. The card's floor of at least 6 shortlist_ready is met with room to spare.
- **8 calendar records** in `calendar_conflicts.json`: 4 `related` and 4 `major_other`, every one with an organiser page captured today.
- **15 community records** in `communities.raw.json`: 11 active, 4 intermittent, 0 dormant, each with a saved own-page capture.
- **39 distinct searches** (19 venue/district, 18 calendar, 2 community) and about 60 direct page fetches, all listed in `community_discovery_log.md` and `captures/INDEX.md`.

## Venue yield

Sixteen candidates across eleven areas on Hong Kong Island and in Kowloon: Wan Chai (3), Causeway Bay, Sheung Wan, Central (2), Quarry Bay, Kennedy Town, Tsim Sha Tsui, Ngau Chi Wan, Kwun Tong (2), Lai Chi Kok (2) and Sha Tin (Science Park).

Top five by scored rank:

1. **Igather 匯聚會議室 — 中環 E&F 特大型會議廳** — 0.7314 — 60-100 people, HK$10,000 full day (USD 1,277.43), free Wi-Fi, projection/large screen, whiteboard, open 24 hours, 19/F Hip Shing Hong Centre two minutes from Central MTR.
2. **牛池灣文娛中心 演講室** — 0.7178 — 30-70 seats, HK$360/hour (USD 367.90 for 8 h), 100 sq m, LCD projector, sound system, wired and wireless mics, LCSD civic centre.
3. **樹洞香港 TreeholeHK — 灣仔活動場地 AB** — 0.7059 — 50 seats, HK$650/hour (USD 664.26 for 8 h), TV screen, projector, speakers with two wireless mics, whiteboard, open every day including public holidays.
4. **Igather 匯聚會議室 — 觀塘 20–40 人會議室** — 0.6607 — 20-40 people, HK$900/hour (USD 919.75 for 8 h), Wi-Fi confirmed, but Saturday central air-conditioning is published only until 14:00.
5. **The Hive Kennedy Town — 8/F Studios** — 0.6575 — 50 seated / 80 standing, high-speed Wi-Fi, screen projector and sound system, cost unpublished (cost_unknown) so it scores with a null cost.

The rest of the shortlist, priced and unpriced. **Priced:** Sheung Wan Civic Centre lecture hall (150 raked seats, HK$1,330 per 4-hour session = USD 169.90), Garage Society Wan Chai (70 seated, HK$3,200/hour = USD 3,270.21 for 8 h), Garage Society Causeway Bay (40, HK$2,000/hour = USD 2,043.88 for 8 h) and Dream Impact (four-room combination, weekend HK$2,675/hour = USD 2,733.69 for 8 h). **No usable published price (cost null):** AMO TST (50 classroom seats, 120-inch LED screen, 24-hour), The Hive Wan Chai (50-100 guests), The Wave (500, quote only) and Good Lab (50/80, currency unresolved).

The three leads are informative:

- **Banyan Workspace** — the August 2026 run's top Hong Kong pick (0.7096 on a HK$888/hour rate). Today the live page publishes **no rate** and states **20 seated / 60 standing**, so a 50-person seated workshop is not evidenced; the old `corporate-events` URL is HTTP 404. Recorded as a lead with a capacity question.
- **PMQ 元創方 QUBE** — the page publishes headroom and floor plans but no capacity, no rate and no technical inventory. A lead, not a candidate.
- **Hong Kong Science Park (Golden Egg)** — Wi-Fi, screens and catering support are described, but the seat count is not on the page and charges are published only as a PDF that could not be read here.

**Why zero venues reached `eligible`.** `eligible` requires every material fact evidenced, confirmed screen and Wi-Fi, a sourced numeric cost, a supported window, `needs_human_verify: false` and **no verification questions at all**. In Hong Kong on 2026-11-28 no venue publishes a live 2027 calendar, almost none states a tax position, and none states an alcohol licensing position — so at least one soft question is unavoidable for every record. That is an information limit, not a shortened search.

## Comparability caveat (read before comparing the USD column)

The sixteen USD figures are not all prices for the same thing:

- **Hour × 8**: Garage Society Wan Chai and Causeway Bay, TreeholeHK, Igather Kwun Tong, Ngau Chi Wan (all at the 09:00-17:00 acceptable window).
- **Published full-day package**: Igather Central — HK$10,000 for the operator's full day (its hourly rate is HK$2,000).
- **Published 4-hour session**: Sheung Wan Civic Centre lecture hall — HK$1,330 buys a 4-hour session; a longer day is a multiple of that session price per the LCSD fee table.
- **Null**: AMO, both Hive venues, Banyan, The Wave, Good Lab, PMQ and HKSTP.

## The FX basis and hand recomputations

ECB reference rates, file dated 2026-11-27, fetched 2026-11-28: **EUR 1 = USD 1.0957**, **EUR 1 = HKD 8.5774**. Derived and used everywhere: **1 HKD = USD 0.12774267** (USD 1 = HKD 7.828238). Full working in `fx_evidence_2026-11-28.md`.

1. Garage Society Wan Chai, 8 h × HK$3,200 = **HK$25,600**; 25,600 × 0.12774267 = 3,270.212 → **USD 3,270.21**.
2. TreeholeHK Room AB, 8 h × HK$650 = **HK$5,200**; 5,200 × 0.12774267 = 664.262 → **USD 664.26**.
3. Igather Central full day = **HK$10,000**; 10,000 × 0.12774267 = 1,277.427 → **USD 1,277.43**.
4. Cross-check on the rate-derived LCSD record: HK$360/h × 8 = **HK$2,880**; 2,880 × 0.12774267 = 367.899 → **USD 367.90**, stored with `hourly_rate_usd` 45.98736 so the recorded product reconciles to the cent.

Reverse check on (1): USD 3,270.21 ÷ 0.12774267 = HK$25,599.9, inside rounding.

Note on the scorer output: `venues.shortlist.json` writes `meta.event_date` equal to the scorer's freshness reference, which defaults to the access date (2026-11-28). It is not an event date and nothing in this package proposes one.

## Calendar yield

Eight records, every one with an organiser page captured today:

- `related`: **Consensus Hong Kong 2027** (2027-02-02 to 02-03, HKCEC, web3, high); **Hong Kong Web3 Festival 2027** (2027-04-19 to 04-21, HKCEC, web3, high); **AIAIS 2027** (2027-01-22 to 01-24, City University of Hong Kong, ai, low); **AI 2030 Summit Hong Kong 2027** (2027-01-25, CityU, ai, low).
- `major_other` (logistics only): **Standard Chartered Hong Kong Marathon 2027** (2027-01-17, Nathan Road to Victoria Park); **Art Basel Hong Kong 2027** (2027-03-25 to 03-27, HKCEC); **Art Central 2027** (2027-03-24 to 03-28, Central Harbourfront); **Cathay/HSBC Hong Kong Sevens 2027** (2027-04-09 to 04-11, Kai Tak Stadium).

This is a real yield but a thin one, and the gap is announcement timing rather than search effort. **Eight major 2027 Hong Kong events are explicitly dated as unknown** in `source_uncertainty_notes.md`: Hong Kong FinTech Week x StartmeupHK 2027 (InvestHK is still procuring a 2027-2029 organiser, EOI due 10 December 2026), Hong Kong AI Week 2027 (April, no dates), Digital Economy Summit 2027, the whole HKTDC 2027 fair calendar (bot-walled), Wine & Dine 2027, Clockenflap 2027, ETH Hong Kong 2027, and AWS Summit Hong Kong 2027 (preliminary "May 26" inside an unreadable PDF). Techathon+ 2027 is organiser-dated (28-31 January) but its page does not state an AI topic, so it is noted rather than recorded.

Public-holiday context is not restated here or anywhere else: the `HK` registry rows in `references/school_holidays.json` (public holidays 2027-01-01 to 2027-12-31, gazetted 15 May 2026) are the only holiday authority, and the school side is declared unknown, so no Hong Kong school break is asserted.

## Community yield

Fifteen records: AI Tinkerers Hong Kong; Prompt in Progress; Hong Kong Machine Learning Meetup; PyData Hong Kong; Data Science & Generative AI Hong Kong; GDG Hong Kong; Hong Kong Python User Group; Open Source Hong Kong; AWS User Group Hong Kong; Global AI Hong Kong; Hong Kong Ethereum Community Hub; Women in Web3 Hong Kong; Bitcoin Association of Hong Kong; StartmeupHK; AI Builders Hong Kong.

Eleven carry a dated in-person activity fact inside the last twelve months and are marked active; four are intermittent with a precise question. Co-host openness is recorded for three groups only — HKML (own-page "always on the lookout for high-quality speakers and sponsors"), Prompt in Progress (partner list and the statement that AI Tinkerers Hong Kong is "our focused technical community") and OSHK (repeated "OSHK x HKPUG" joint events). No co-host relationship is claimed, and no contact route is stored that is not a public page.

## Old-run fields that changed after re-verification (what the store build should trust)

The August 2026 run (`research/hong-kong/2026-q4/`) is history and was not edited. These fields differ today, and the new values are the ones to trust:

- **Banyan Workspace — price gone, capacity restated.** Old: HK$7,104 for 8 h (HK$888/h, `estimated_from_rate`) at `banyanworkspace.com/corporate-events/`. Today: that URL is **HTTP 404**; the live page publishes **no rate** and **20 seated / 60 standing**. Old score 0.7096 (top of the city) → now a **lead** on a capacity question.
- **Garage Society — rate structure changed.** Old: one event-space record at HK$24,000 for 8 h (HK$3,000/h). Today: **two** venues with different rates — Causeway Bay (40 people) HK$2,000/h or HK$10,000 for 6 h, and Wan Chai (70 seated) HK$3,200/h with a 2-hour minimum.
- **The Hive Wan Chai — event-space rates removed.** Old: HK$20,000 for 8 h indoor (HK$2,500/h) and HK$10,000 for the terrace (HK$1,250/h). Today: the page describes the space and "50-100 guests" but publishes **no event-space rate**; cost is now null.
- **The Hive Kennedy Town — new record, no rate.** A search snippet quotes "Studio: $1200 per hour"; the live page publishes none, so the record carries cost_unknown and the snippet is not used.
- **Dream Impact — page and price structure are new.** Old: a Chinese landing page at a different URL (HTTP 502 today) with no price. Today: `dreamimpacthk.com/event-space` renders with a full rate table, including a **weekend rate of HK$2,675/hour** for the 200-person four-room combination.
- **Blueprint — unchanged and still a non-fit.** Weekday 09:00-18:00 only, closed weekends and public holidays, prices by enquiry. Dropped from the candidate set this run (old run kept it as a lead).
- **PMQ, The Wave, Cyberport, HKSTP — unchanged.** Enquiry-only or PDF-only as before; Cyberport still blocks (HTTP 403).
- **No closure was found.** No venue in the August 2026 set has a closure notice on its live page; the changes are price and page-architecture changes, not closures.

## Gaps Joe should know about

- **Cyberport has no record.** Both official pages return HTTP 403; the old run's Cyberport record cited a third-party page, which is not acceptable as operator evidence.
- **Eight venues are unpriced** (AMO, Hive Kennedy Town, Hive Wan Chai, Banyan, The Wave, Good Lab, PMQ, HKSTP), so half of the set cannot be compared on budget until quotes arrive. Dream Impact is priced, but only under a currency assumption: its weekend rate HK$2,675/h is read as HKD (HK$21,400 for eight hours = USD 2,733.69) and carries a confirm-currency question, so it is not in the unpriced list.
- **No 2027 availability is confirmed for any venue**, and only Igather Central and AMO publish an access window that certainly covers a 12-hour day.
- **District coverage is uneven.** Central, Wan Chai, Causeway Bay, Quarry Bay, Sheung Wan, Kennedy Town, Tsim Sha Tsui, Ngau Chi Wan, Kwun Tong, Lai Chi Kok and Sha Tin are represented. The district sweep for Admiralty, North Point, Mong Kok, Kowloon Bay and Kwai Chung surfaced only aggregator listings or rooms too small for 50 people (Metro Workspace Admiralty is 10 people; the Hong Kong Cultural Centre publishes room rates but no per-room head count). Two late finds were **not** carried and should be the first checks in a second pass: **AVS 香港義工學院 (Kwai Chung)** — 15-100 seats with a published hourly table and a projector included — and **HKFYG 持續進修中心 (Causeway Bay)** — 30-100 people with AV and a published booking page.
- **The calendar is announcement-limited**, as set out above: eight records and eight explicit unknown-date notes.
- **No DeAI group** with own-page activity was found in Hong Kong, and no quant group with a 2026 date. The DeAI audience would have to be assembled from AI-builder and Web3 groups.
- **MTR access is estimated, not published, for seven of the sixteen records.** Every venue record now names a nearest station; The Wave ("MTR Exit B1", "Short walk from MTR station"), Good Lab ("just 2-min walk from MTR station") and Dream Impact ("距離荔枝角地鐵站僅 3 分鐘路程") state access on their own pages. The other seven stations and walking times are derived from the stored coordinates and a saved Nominatim station lookup (method and formula in `source_uncertainty_notes.md` §6), and both the Good Lab and Dream Impact minute claims are contradicted by the measured distances (~710 m and ~688 m, about 11 minutes each).
- **No date is selected, ranked or recommended anywhere in this package.** The venue set is date-independent and every output can be re-read without inferring a scheduling decision.
