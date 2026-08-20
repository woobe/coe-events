# Venue Discovery Log — Warsaw (2026-Q4) — Phase Re-run

## Date: 2026-08-20
## Worker: jnr-research
## Context: Original Run A found 7 venues all scoring "lead". Re-run with ddgs installed.

## Platform Check
- Result: No active platform coverage for Warsaw in venue_platforms.json
- Standard web discovery used

## Search Queries (14 total)
1. "event space Warsaw 50 people rental" → 8 results
2. "conference room Warsaw booking Poland" → 6 results
3. "loft event space Warsaw Poland" → 8 results (mostly UK retail)
4. "warehouse event venue Warsaw" → 8 results (fashion brands)
5. "coworking event space Warsaw Poland" → 8 results (mostly Google Maps)
6. "Impact Hub Warsaw event space" → 8 results (generic impact.com)
7. "CIC Warsaw event space Varso" → 8 results (UK CIC definitions)
8. "Tagvenue Warsaw Poland" → 8 results (UK-focused Tagvenue)
9. "eventvenue.pl Warsaw" → 8 results (Microsoft Outlook links)
10. "centrum konferencyjne Warszawa" → 8 results (strong: ADN, salekonferencyjne.pl, konferencje.pl)
11. "Google for Startups Warsaw" → 8 results (strong: Campus Warsaw, Firstview)
12. "sala eventowa Warszawa" → 8 results (strong: WE EVENT WTT, Messalka, Samo Centrum)
13. "warszawa wynajem sali eventowej" → 8 results (Wikipedia)
14. "venue hire Warsaw 50 guests" → 8 results (UK aggregators)

## Deep Dive Venues (fetched via curl)

### 1. WE EVENT — Sala Eventowa Warsaw Trade Tower
- Source: https://www.sala-eventowa-warszawa.pl/
- Address: Chłodna 51, 00-867 Warszawa, Wola (32nd floor WTT)
- Capacity: Up to 200 theater; Panorama Wola 120m² or 230m²
- WiFi: Yes (from venue type)
- Catering: In-house (WE Catering)
- Hours: Mon-Fri 08:00-18:00, Sat-Sun 10:00-02:00; 24/7 availability
- Parking: Underground + street
- Google rating: 5.0 (Trustindex verified)
- Price: Quote-based (standard rates for 09:00-17:00)
- Email: biuro@sala-eventowa-warszawa.pl
- Phone: +48 22 249 1609
- VAT ID: PL7010667258

### 2. Messalka Events
- Source: https://messalka.events/
- Address: Krakowskie Przedmieście 16/18, 00-325 Warszawa
- Capacity: 30-600 guests; 750m² across 4 levels
- Rating: 4.8/5 (34 reviews)
- Founded: 2022
- Phone: +48 690 292 576
- Email: booking@messalka.events
- Nearest metro: Nowy Świat-Uniwersytet
- Historic 1911 bathhouse (Łaźnia Messalka)
- VOID Acoustics sound system
- Premium catering + Live Cooking
- Price: Quote-based

### 3. ADN Centrum Konferencyjne
- Source: https://ckadn.pl/en/
- Address: Browary Warszawskie, Warszawa
- Rooms: 25 air-conditioned, daylight + blackout
- Key rooms: 1A (111m²/100p), 1B (112m²/100p), 14 (62m²/75p), 13B (66m²/75p)
- Largest: 500m² for 550 people
- Tech: Advanced equipment
- Phone: 22 208 21 12
- Price: Quote-based

### 4. Samo Centrum Wszechświata
- Source: https://samocentrum.com/
- Address: Chłodna 29, Warszawa
- Capacity: 1000m² across 9 modular rooms
- Style: Industrial/modern, restored historic kamienica
- Events: Weddings, corporate, training, banquets
- Price: Quote-based

### 5. Google for Startups Warsaw (Campus Warsaw)
- Source: https://googleforstartups-warsaw.firstview.us/en
- Address: Plac Konesera 1, 03-736 Warszawa, Praga-Polnoc
- Type: Tech hub campus
- WiFi: Yes
- Potential: Free/subsidized space for qualifying community events
- Price: Unknown (possibly free for qualifying events)

### 6. CIC Warsaw — Event Spaces at Varso Place
- Source: https://cic.com/warsaw/event-spaces/
- Address: Varso Place, Warsaw
- Rooms: Design Room, Research Room, Strategy Room + full-size bar
- AV: "AV, support, and flexible setups"
- Location: Next to Central Railway Station
- Price: Quote-based

### 7. Impact Hub Warsaw
- Source: https://warsaw.impacthub.net/
- Address: Nowogrodzka 47a, Warsaw
- Status: NOT in installed Impact Hub snapshot
- Type: Coworking + event spaces + community
- Price: Unknown

## Results
- 11 venues in venues.raw.json
- 7 shortlist_ready (score ≥ threshold)
- 4 leads (capacity unknown)
- Top venue: ADN Centrum Konferencyjne (score 0.5867)

## Files Modified
- research/warsaw/2026-q4/venues.raw.json (rewritten)
- research/warsaw/2026-q4/venues.shortlist.json (regenerated)

## Files NOT Modified
- communities.raw.json (untouched)
- calendar_conflicts.json (untouched)
- city_input.json (untouched)
