# Capture index — Hong Kong 2027 research run, accessed 2026-11-28

Every page cited in `venues.raw.json`, `calendar_conflicts.json`, `communities.raw.json` and the notes has a raw capture here. Files ending `.txt` are plain-text extractions of the sibling `.html` (same bytes, tags stripped) and are not separate sources.

All fetches were made on **2026-11-28** (UTC). HTTP status is recorded where it matters.

**Capture inventory:** 185 raw capture files plus this INDEX.md. Files in section 4 are recorded so no opened lane is silently closed; files in section 5 support a coordinate claim (venue geocodes and station geocodes) rather than a record's own address. Section 8 holds the five claim and coverage pages plus the 404 record fetched by the city-store build (2026-11-28) for the three local-requirement claims and the school-lane coverage finding.

## 1. FX basis

- `ecb_eurofxref_daily_2026-11-28.xml` — https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml (HTTP 200; reference date inside: 2026-11-27)

## 2. Platform lanes (opened and recorded, per the standing rule)

- `lane_peerspace_hong-kong_blocked_cloudflare.html` — https://www.peerspace.com/s/hong-kong (HTTP 403 via curl; headless Chromium returns the Cloudflare "Just a moment..." challenge page — blocked)
- `lane_tagvenue_home_no_hk.html` — https://www.tagvenue.com/ (HTTP 200; no Hong Kong city page; /hk and /hk/hong-kong return HTTP 404)
- `lane_eventective_root_no_hk.html` — https://www.eventective.com/ (HTTP 200 at root; /hong-kong/ and /search/?q=Hong+Kong return HTTP 404 — no Hong Kong inventory)
- `lane_venuereport_hong-kong_redirect_home.html` — https://www.venuereport.com/venues/hong-kong/ (HTTP 403 via curl; headless Chromium lands on the Venue Report home page with zero Hong Kong mentions — no Hong Kong coverage)

## 3. Venue pages cited in venue records

- `garage_event_space.html` — https://www.thegaragesociety.com/service/event-space
- `treehole_wch_venue.html` — https://treehole.hk/wan-chai-venue-rental
- `igather_central.html` — https://igather.hk/central_meeting_room.html
- `igather_kwuntong.html` — https://igather.com.hk/%E8%A7%80%E5%A1%98%E6%9C%83%E8%AD%B0%E5%AE%A4.html
- `lcsd_ncwcc_hire_charges.html` — https://www.lcsd.gov.hk/tc/ncwcc/hiringarrangement/scaleofcharges.html
- `lcsd_ncwcc_lectureroom.html` — https://www.lcsd.gov.hk/tc/ncwcc/facilities/lectureroom.html
- `lcsd_swcc_hire_charges.html` — https://www.lcsd.gov.hk/tc/swcc/hiringinformation/scaleofhirecharges.html
- `lcsd_swcc_lecturehall.html` — https://www.lcsd.gov.hk/tc/swcc/facilities/lecturehall.html
- `dreamimpact_event_space.html` — https://dreamimpacthk.com/event-space?lang=zh-hant (HTTP 502 to plain requests; rendered with headless Chromium and captured)
- `amo_venue.html` — https://www.amohk.com/venue/
- `agg_commonroom_amo.html` — https://www.common-room.hk/o/amo (AMO's booking listing; used only to quote an indicative rate inside a verification question, not as the cost basis)
- `hive_kennedytown_events_venue_hire.html` — https://thehivekennedytown.com.hk/events-venue-hire/
- `hive_wch_events.html` — https://thehive.com.hk/events-venue-hire/
- `banyan_event_venue.html` — https://banyanworkspace.com/event-venue-hong-kong/
- `thewave_event_space.html` — https://thewave.com.hk/services/event-space/
- `goodlab_venue_hiring.html` — https://www.goodlab.hk/service/venue-hiring
- `pmq_venue_rental.html` — https://www.pmq.org.hk/the-site/event-venue-rental/
- `hkstp_mice_venue_page.html` — https://www.hkstp.org/en/rental/space/mice-venue/hong-kong-science-park-mice-venues
- `hkstp_mice_venues_list.html` — https://www.hkstp.org/en/rental/space/mice-venues

## 4. Venue pages opened, not load-bearing (recorded so the lane is not silently closed)

- `banyan_home.html` — https://banyanworkspace.com/ (old event-page URL `banyanworkspace.com/corporate-events/` now HTTP 404; the live event page is in section 3)
- `blueprint_50.html` — https://blueprint.swireproperties.com/en/event-venues/venues-up-to-50-persons/ (venue open weekdays 9AM-6PM only, closed weekends and public holidays, prices by enquiry — dropped from the candidate set)
- `campfire_home.html` — https://campfire.hk/ (no event-space rate found on the home page)
- `ebspace_meeting_room.html` — https://ebspace.hk/pages/meeting-room (HTTP 404 — the search result URL is dead)
- `hkcc_rooms.html` — https://www.lcsd.gov.hk/tc/hkcc/facilities/rooms.html (Hong Kong Cultural Centre rehearsal rooms and meeting rooms: hourly rates exist in the fee table but the rooms page publishes no per-room head count, so it was not carried into the candidate set)
- `lcsd_hkcc_basic_charges.html` — https://www.lcsd.gov.hk/tc/hkcc/hiringinformation/scaleofhirecharges/basichirecharges.html
- `cyberport_cec.html` — https://www.cyberport.hk/en/facilities/conference_exhibition_centre/ (HTTP 403, Cloudflare — blocked)
- `cyberport_event_venue_space.html` — https://www.cyberport.hk/en/event-venue-space/ (HTTP 403 — blocked)
- `dreamimpact_venue.html` — https://www.dreamimpacthk.com/%E6%B4%BB%E5%8B%95%E5%A0%B4%E5%9C%B0-%E8%8D%94%E6%9E%9D%E8%A7%92%E5%A4%A2%E5%89%B5%E5%9F%BA%E5%9C%B0/?lang=zh-hant (HTTP 502 — superseded by the live /event-space page above)
- `agg_commonroom_hive_lck_rooftop.html` — https://www.common-room.hk/o/the-hive-lck-rooftop-terrace (aggregator listing for The Hive Lai Chi Kok rooftop; discovered but not used as a record)
- `bitlab_venue_rental.html` — https://www.bitlab.com.hk/venue-rental-services (opened during the Kwun Tong sweep; no carried record)
- `com_echo_community.html` — https://myecho.space/ (client-rendered shell with no readable activity text; the group was dropped rather than described from a search snippet)
- `hkstp_mice_venues.html` — https://www.hkstp.org/en/rental/space/mice-venues (returns the HKSTP 404 page; superseded by the MICE venue pages in section 3)
- `hongthai_expo_centre.html` — https://www.htebc.com.hk/zh/ (opened during the Kwun Tong sweep; no carried record)
- `luplus_spaces.html` — https://www.theluplus.com/spaces (The LU+ Kwun Tong event space, opened during the sweep; no published capacity/rate combination that carried a record)
- `geocode_luplus.json` — Nominatim response for The LU+ address: empty array (recorded failure, nothing filled in)
- `geocode_luplus2.json` — fallback Nominatim lookup for The LU+ block: 22.3117437 / 114.2221577, an OSM "artwork" node, so it was not used as a venue coordinate

## 5. Coordinate lookups (Nominatim / OpenStreetMap, one saved JSON per venue, plus station lookups)

Each JSON is the raw response to the query URL printed in the venue record's `evidence.geo`. `geocode_treehole_wanchai.json` and `geocode_thewave.json` were saved empty in the first pass; both were re-fetched from the same recorded query URLs on 2026-11-28 and now hold the response (Treehole 22.2778363/114.1768740, The Wave 22.3092741/114.2251595).

- `geocode_garage_wanchai.json` — 93 Lockhart Road, Wan Chai (street-level)
- `geocode_garage_causewaybay.json` — Tower 535, 535 Jaffe Road, Causeway Bay (building)
- `geocode_treehole_wanchai.json` — 178 Johnston Road, Wan Chai (street-level)
- `geocode_igather_central.json` — Hip Shing Hong Centre, Des Voeux Road Central (building)
- `geocode_igather_kwuntong.json` — 49 Hoi Yuen Road, Kwun Tong (street-level)
- `geocode_ncwcc.json` — Ngau Chi Wan Municipal Services Building (building)
- `geocode_swcc.json` — Sheung Wan Civic Centre / Municipal Services Building (building)
- `geocode_dreamimpact.json` — 760 Cheung Sha Wan Road, Lai Chi Kok (street-level)
- `geocode_amo_tst.json` — Star House, Tsim Sha Tsui (building)
- `geocode_hive_kennedytown.json` — Smithfield Road, Kennedy Town (street-level)
- `geocode_hive_wanchai.json` — 23 Luard Road, Wan Chai (building number)
- `geocode_banyan.json` — 28 Hoi Chak Street, Quarry Bay (street-level)
- `geocode_thewave.json` — 4 Hing Yip Street, Kwun Tong (street-level)
- `geocode_goodlab.json` — 700 Castle Peak Road, Lai Chi Kok (street-level)
- `geocode_pmq.json` — 35 Aberdeen Street, Central (building)
- `geocode_hkstp.json` — Hong Kong Science Park, Pak Shek Kok (site)

MTR station lookups (supporting the `evidence.nearest_mtr` estimates; not venue addresses). Query pattern `https://nominatim.openstreetmap.org/search?q=<Station>+Station%2C+Hong+Kong&format=json&limit=1`:

- `geocode_mtr_wanchai.json` — Wan Chai Station (22.2775843 / 114.1728604) → TreeholeHK
- `geocode_mtr_central.json` — Central Station (22.2819377 / 114.1580765) → Igather Central
- `geocode_mtr_sheungwan.json` — Sheung Wan Station (22.2858993 / 114.1537070) → PMQ
- `geocode_mtr_kwuntong.json` — Kwun Tong Station (22.3113908 / 114.2274030) → Igather Kwun Tong, The Wave
- `geocode_mtr_choihung.json` — Choi Hung Station (22.3340444 / 114.2101746) → Ngau Chi Wan Civic Centre
- `geocode_mtr_kennedytown.json` — Kennedy Town Station (22.2813400 / 114.1277042) → The Hive Kennedy Town
- `geocode_mtr_hku.json` — HKU Station (22.2844491 / 114.1341875) → comparison point for The Hive Kennedy Town
- `geocode_mtr_laichikok.json` — Lai Chi Kok Station (22.3366732 / 114.1479840) → Good Lab, Dream Impact
- `geocode_mtr_university.json` — University Station (22.4127018 / 114.2105301) → Hong Kong Science Park

## 6. Calendar evidence

- `cal_consensus_hk_faq.html` — https://consensus-hongkong.coindesk.com/faq/ (Feb 2-3, 2027)
- `cal_hkweb3festival_luma.html` — https://luma.com/hkweb3festival_2027 (19-21 Apr 2027, HKCEC)
- `cal_aiais_2027.html` — https://aiais.site/index.html (22-24 Jan 2027, CityU)
- `cal_ai2030_eventbrite.html` — https://www.eventbrite.com/e/ai-2030-summit-hong-kong-2027-tickets-1257641101389 (25 Jan 2027, CityU)
- `cal_hkmarathon_raceinfo.html` — https://www.hkmarathon.com/race-information/ (17 Jan 2027)
- `cal_artbasel_hk.html` — https://artbasel.com/hong-kong (25-27 Mar 2027)
- `cal_artcentral_about.html` — https://artcentralhongkong.com/about (24-28 Mar 2027, Central Harbourfront)
- `cal_hksevens_details.html` — https://hksevens.com/about-us/details (9-11 Apr 2027, Kai Tak Stadium)
- `cal_fintechweek_home.html` — https://www.fintechweek.hk/ (2026 edition only; "Ready for 2027?" pre-registration with no dates)
- `cal_investhk_fintech_eoi.html` — https://www.hongkong-fintech.hk/ (InvestHK EOI for FinTech Week x StartmeupHK 2027-2029 event organisation)
- `cal_aiweek_hk.html` — https://aiweek.hk/ (rendered with headless Chromium; "April 2027, Hong Kong", no dates)
- `cal_techathon_keydates.html` — https://www.hktechathon.com/en/site/keydates (Techathon+ Finale 28-31 Jan 2027)
- `hktechathon_home.html` — https://www.hktechathon.com/en (no AI topic statement on the page)
- `cal_hktdc_2027_index.html` — https://event.hktdc.com/en?eventFormat=Exhibition&location=hk (HTTP 403 — blocked; headless Chromium returns an empty document)
- `cal_hktdc_home.html` — https://event.hktdc.com/en/ (HTTP 200 shell, no readable event data)
- `hktdc_bookfair.html` — https://www.hktdc.com/event/hkbookfair (no 2027 date in the page text)
- `hktdc_innoex.html` — https://www.hktdc.com/event/innoex (mentions InnoEX 2027 but prints no date)
- `hktdc_efse.html` — https://www.hktdc.com/event/hkelectronicsfairse (no 2027 date in the page text)
- `hktdc_toyfair.html` — https://www.hktdc.com/event/hktoyfair (no 2027 date in the page text)
- `hktb_events_index.html` — https://www.discoverhongkong.com/eng/events.html (client-rendered; no 2027 dates in the captured text)

## 7. Community evidence (each group's own page)

- `com_aitinkerers_hk.html` — https://hong-kong.aitinkerers.org/
- `com_hkml.html` — https://www.meetup.com/hong-kong-machine-learning-meetup/
- `com_pydata_hk.html` — https://www.meetup.com/pydata-hong-kong/
- `com_dsgenai_hk.html` — https://www.meetup.com/data-science-hk/
- `com_gdg_hk.html` — https://gdg.community.dev/gdg-hong-kong/
- `com_hkpug.html` — https://www.meetup.com/pythonhk/
- `com_oshk.html` — https://opensource.hk/meetups/
- `com_awsughk.html` — https://www.meetup.com/hong-kong-amazon-aws-user-group/
- `com_globalai_hk.html` — https://globalai.community/chapters/hong-kong/
- `com_eth_hub_hk.html` — https://luma.com/uf5v6joa
- `com_wiw3_hk.html` — https://luma.com/5aw5ip6h
- `com_bahk.html` — https://luma.com/4wvwlqbf
- `com_startmeuphk.html` — https://www.startmeup.hk/upcoming-events/
- `com_ai_builders_hk.html` — https://www.meetup.com/ai-builders-hong-kong/
- `com_prompt_in_progress.html` — https://promptinprogress.com/

## 8. Build evidence — local-requirement claims and the school lane (added 2026-11-28)

- `claim_language_hk_govhk_facts.html` — https://www.gov.hk/en/about/abouthk/facts.htm (HTTP 200; section "Language"; page last revised July 2026)
- `claim_alcohol_hk_llb_note.html` — https://www.fehd.gov.hk/english/LLB_web/note.html (HTTP 200; Liquor Licensing Board "Important Notes", last revised 2018-09-20)
- `claim_alcohol_hk_llb_policy.html` — https://www.fehd.gov.hk/english/LLB_web/policy.html (HTTP 200; Liquor Licensing Board "Policy", last revised 2026-11-04)
- `claim_food_hk_fehd_types.html` — https://www.fehd.gov.hk/english/licensing/Guide_on_Types_of_Licences_Required.html (HTTP 200; FEHD guide, last revised 2026-09-29)
- `coverage_school_hk_edb_index.html` — https://www.edb.gov.hk/en/curriculum-development/resource-support/guidelines-sch-calendar/index.html (HTTP 200; lists 2026/27 documents only, no 2027/28 calendar)
- `coverage_school_hk_edb_legacy_404.html` — https://www.edb.gov.hk/en/student-parents/sch-info/sch-calendar/index.html (HTTP 404, title "Not Found - Education Bureau"; the same day's 404s also covered /en/about-edb/publications-stat/school-calendar/index.html and the 2027/28 attachment paths Example_school calendar_2728_E.pdf and General Holidays_2728_E.pdf)

