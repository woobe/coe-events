# R3b — Kuala Lumpur photo quality pass (2026-11-26)

Store: `research/kuala-lumpur/city/city.json`
Before: `city.pre-r3b.json`, sha256 `11972bfd3d5b3e746e7f0735e15f07d971eaab9719e6a337155f0edee4ef04cb`
After: `city.json`, sha256 `a93df91c19e52317da1f30315ed4bfe740f1eaa6d0b8ec501418d0dc958e7a64`
(1,874,381 bytes), after the round-2 review fix below. The round-1 post-R3b
state is preserved as `city.pre-r3b-round2.json`, sha256
`c03f3aa08be5a0d140d4c903d8b8f2183f818138bbe23ab20d2d5e4d335251d3`.
`city_store.py --check`: `OK: ... (schema city-store/1, 55 venues)`
`refresh_revision`: `1` (unchanged)

## Round 2 — review fix (DOJO TLS honesty, Marriott transform bytes)

Review round 1 found one blocking defect and one reporting defect. Both are
fixed; nothing else changed (`round2-diff.json` holds the field-level diff).

- **DOJO Coworking — Event Halls, row `kl-977b423768cd`.** The operator host
  `workspacedojo.com` presents a TLS certificate valid 2026-05-12 to
  **2026-08-10** — expired. `curl` without `-k` exits 60 and Python `urllib`
  raises `CERTIFICATE_VERIFY_FAILED`; only `curl -k` returns the recorded
  127,365-byte body. The row now records `hotlink_ok: false`; `rights` states
  the expiry and that the asset was fetched without certificate validation, so
  it is evidence only and the venue's page shows no room photo from it;
  `verified.note` repeats the measurement condition. The row keeps its
  `interior` kind and label evidence — the photograph exists, it just cannot be
  hotlinked.
- **Replacement hunt for the DOJO asset (no usable replacement found).**
  - FlySpaces listing `flyspaces.com/kuala-lumpur/dojo-kl-menara-amplewest/751`
    serves 7 DOJO photos from `media.flyspaces.com` (TLS valid) but has no alt
    text, caption or room label, and the marketplace's terms are not a reuse
    licence — the photo's kind and rights cannot be established from it.
  - Coworker (`coworker.com/malaysia/kuala-lumpur/dojo-kl`) and Coworkbooking
    listings redirect/script-render and expose no operator-labelled asset.
  - The Internet Archive has no snapshot of the asset (CDX/asset fetch
    unavailable or 404 at check time), so an archived TLS-valid copy is not
    available either.
- **W Kuala Lumpur — Studio 3 and The St. Regis — The Astor Rooms.** Both
  Marriott URLs are dynamic resize transforms. Byte counts re-measured
  2026-11-26: 723,984 → 733,689 and 906,235 → 833,161 respectively, with
  dimensions unchanged (1920×1280; 2880×1620). `verified.note` now states that
  the endpoint re-encodes, so the byte count is a per-fetch snapshot and the
  dimensions are the stable invariant.
- No row was added or removed; three rows were edited. Live rows by `view_kind`
  stay exterior 43, floor_plan 4, interior 28, layout 3, lobby 1, withheld 26 —
  but the **renderable** count (passing the `_photo_cleared` gate) is interior
  27, because DOJO's interior row is now evidence-only.
- A TLS sweep of all 51 unique live photo URLs found no other expired or invalid
  certificate. The only other non-2xx replies were bot/rate gates (Marriott
  `403` and Wikimedia `429` without a browser user-agent), which clear when
  re-probed with a UA or after a pause.

## What changed

Only the top-level `photos` key changed. Every other top-level value hashes
identically (`verify_r3b.py`: `non-photos keys changed: []`, 24 keys, byte-stable
round-trip). No venue row, claim, coordinate, holiday or event row was edited.

- 43 photo groups touched: 18 venues gained at least one operator image, 25
  venues had their no-room-photo finding written down.
- 24 live image rows added; 15 stale "No verifiable photo of the venue"
  placeholders removed from venues that now have an image; 9 new withheld
  placeholders added where an exterior or lobby image already existed but no
  room-level image could be found, so the finding is explicit.
- Withheld rows: 32 before, 26 after.

## Distribution by `view_kind` (live, non-withheld rows)

- Before: exterior 42, interior 7, floor_plan 3, layout 2, lobby 1 (55 live; 32 withheld placeholders)
- After: exterior 43, interior 28, floor_plan 4, layout 3, lobby 1 (79 live; 26 withheld placeholders). Renderable rows after the round-2 fix: interior 27 (DOJO's row is evidence-only; see Round 2 above).
- Room-level family (interior + layout + floor_plan + past_event): 12 before, 29 after.
- Exterior only (no room-level row): 9 venues.
- No image at all (withheld placeholder): 17 venues.

## Venues that gained a room-level image (17)

Each row below is a real downloaded image (HTTP 200, decoded, dimensions
recorded). "Label basis" is the wording on the publishing page that names the
room; the record's `placement_proof` carries the same evidence.

- Colony — The Boardroom (Mont Kiara): interior x2. `Colony-TheMET-Boardroom-slider-desktop-1.jpg` (1774x887) alt "The Boardroom - Colony event space Mont Kiara (The MET)" plus `the-boardroom-cropped-1A.png` (633x461) from the Mont Kiara page.
- Colony — The Sun Room (Mont Kiara): interior. `Colony-TheMET-SunRoom-slider-desktop.jpg` (881x441) alt names the Sun Room and Mont Kiara (The MET).
- Colony — The Glass Box: interior x2. Slider (1837x920) alt names the Glass Box and Mont Kiara; `The-Glass-Box-banquet-1-960x750.jpg` (960x750) on the Mont Kiara page.
- Colony — The Lounge: interior. `Colony-TheMET-TheLounge-Slider-desktop-70-guests.webp` (881x441) alt names the Lounge and Mont Kiara.
- Colony — Event Lounge at KLCC: interior. `Colony-KLCC-capacity-desktop.jpg` (1836x919), served inside the `<article>` whose `<h3>` reads "Event Lounge at KLCC"; alt names the room and KLCC.
- Colony — Event Lounge at KL Eco City: interior. `Colony-Eco-City-capacity-desktop.jpg` (1836x919), same page structure, alt names the room and KL Eco City.
- WORQ — Event Space: interior x2. `spm-event-space-01.jpg` / `-02.jpg` (1920x1280) on WORQ's Sunway Putra location page, alt "WORQ Sunway Putra Mall Event Space"; record address is Level 4-1, Sunway Putra Mall and the record coordinate (3.1664, 101.6923) sits on the mall (0.0 km).
- DOJO Coworking — Event Halls: interior. `event-hall-dojo-1-1024x576.jpg` in the page's "Featured Event Space" carousel on the operator's event page (event halls at Menara Amplewest). Round 2: recorded `hotlink_ok: false` because the operator host's TLS certificate expired 2026-08-10 — evidence only, not renderable.
- WTC Kuala Lumpur — Dewan Merdeka: interior x3. `WTCKL_MERDEKA-HALL_71/55/41-scaled.jpg` (2560x1707/1709) in the Dewan Merdeka venue page's "Venue Gallery".
- Connexion — Auditorium: floor_plan. `Auditorium-scaled.jpg` (2560x1440) in the Auditorium room block of the centre's "Capacity & Floor Plan" page; line art (81.9% near-white, zero saturation).
- The RuMa — Event Space: interior. `ruma-bilik-I-boardroom.jpg` (1920x1080), meetings carousel with alt naming The RuMa; file name names Bilik I.
- The St. Regis — The Astor Rooms: interior. `kulxr-astor-room-5291-hor-wide.jpg` (2880x1620) in the hotel's "Iconic Spaces" carousel; property code KULXR + "astor-room", and the capacity table lists "The Astor Rooms".
- W Kuala Lumpur — Studio 3: layout. `kulwh-meeting-facilities-3802-hor-clsc.jpg` (1920x1280), alt "Studio Three - Theatre Setup".
- Mandarin Oriental — Function Space: interior x2. Grand Ballroom and Diamond Ballroom assets (4096x2730) from the hotel's `/petronas-towers/meet` page, each with the room named in its asset title.
- Common Ground Ampang — Event Space: interior. `ap_es-web-9-...-1024x681.jpg` in the Ampang page's "Get Together, Host Events and Discussions" section; file name carries `ap_es`.
- Common Ground KL Eco City — Event Space: interior. `klec-web-es.jpg` (1920x1280) in the same section on the KL Eco City page.
- GMBB — Event Space: interior. `1A-1024x576.jpg` (1024x576) inside the operator's "THE GREY BOX" shared-space section; that section describes The Grey Box as GMBB's event hall on Level G.

Colony — Rooftop Terrace also gained the operator's own photo
(`Colony-TheMET-RooftopTerrace-slider-wedding-desktop-V2.jpg`, 881x441) but is
labelled **exterior**: the page calls its venues "open-air outdoor event
spaces and breathtaking rooftop event spaces", so it is an outdoor space, not a
room. It stays in the exterior-only bucket.

## Venues still exterior-only (9) and why

- The St. Regis — Astor Room 1, Astor Room 2, Astor Room 3, Astor Rooms 1 and 2:
  the operator publishes one "Astor Room" asset, which is the combined room and
  is recorded on The Astor Rooms. No image and no room-specific plan identifies
  an individual Astor subdivision.
- The St. Regis — Ringgit Room 1, Ringgit Room 2: one "Ringgit Room" asset, with
  nothing on the page saying which half it shows.
- MITEC — The Gallery: the operator lists The Gallery under Level 1A and serves
  a Level 1A plan (already recorded on MITEC — Level 1A Novel), but no
  Gallery-specific photo or plan; the photo gallery's images carry no room
  labels.
- Publika Shopping Gallery — Event Spaces: only a mall lobby photo; see routes
  below.
- Colony — Rooftop Terrace: outdoor venue, no room exists; the operator photo is
  recorded as exterior and the record carries a withheld placeholder stating the
  route and why.

## Venues with no image at all (17): routes checked

Recorded in each withheld row's `rights_note`, all prefixed "R3b (2026-11-26): also checked ...".

- Shangri-La KL — Function Space and Traders Hotel KL — Function Space: operator meeting-rooms and event-spaces pages return a Cloudflare challenge (403); the Cvent listing's gallery is script-rendered with no operator asset; no Commons file shows the function space.
- Publika — Event Spaces: home page carries only a mall hero; `/events` carries no images; `/event-spaces` returned 404 in the first pass; the marketplace listing that names MAP's halls is third-party and carries no addressable operator asset.
- MATRADE MECC: the `/en/about-matrade/mecc` path is 404 and `mecc.matrade.gov.my` now returns a 44-byte stub; the only floor plan found is ExpoFP's third-party 3D plan, not the operator's asset.
- Sunway Pyramid Convention Centre and APW Bangsar: the hosts do not resolve (DNS failure, 2026-11-26) and no Wayback snapshot exists.
- The Bee, Publika: operator site is a maintenance page; the Wayback snapshot is itself a challenge page.
- The Co.: the domain now serves an unrelated gambling page.
- WSPACE — Event Space 50 (Mid Valley) and Event Space 80 (GTower): the event-space page and both location pages carry only generic shared imagery with no room label or alt text; no per-room gallery or plan is published.
- WeWork Malaysia — Event Space: wework.com's event-space path returns 403; the venue is a multi-location record whose coordinate is not Equatorial Plaza, so the Venuerific listing for Equatorial Plaza's rooms cannot be placed on it.
- KLCC — Plenary Hall and Plenary Theatre: the floor-plan page's plans are inline SVG (not addressable image files); the one addressable plan is an image-only three-page PDF covering the whole centre; the 360 gallery is script-rendered; every per-room URL pattern tried returned 404.
- W Kuala Lumpur — Great Room 1, Great Room 2, Studio 1, Studio 2: the operator's meeting-room cards name only "Great Room", "Studio Room" and "Studio Three"; no image or plan identifies a subdivision.
- WTC KL — Hall 1: the operator site has no "Hall 1" page, and the record's 1,003 sqm / 1,000-guest hall matches Tun Dr Ismail and Tun Hussein Onn identically, so no image can be placed without choosing between them.

## Diff proof (script: `verify_r3b.py`, run output saved below)

```
top keys identical: True 24 24
non-photos keys changed: []
refresh_revision: 1 -> 1
venue ids identical: True
photo groups identical: True
round-trip byte identical: True
sha256: c03f3aa08be5a0d140d4c903d8b8f2183f818138bbe23ab20d2d5e4d335251d3 bytes 1873272
before live/withheld: ({'exterior': 42, 'floor_plan': 3, 'interior': 7, 'layout': 2, 'lobby': 1}, 32)
after  live/withheld: ({'exterior': 43, 'floor_plan': 4, 'interior': 28, 'layout': 3, 'lobby': 1}, 26)
new live rows: 24
bad new rows: []
outcomes: {'no image': 17, 'room-level': 29, 'exterior-only': 9} total 55
```

Round 2 (`round2_verify.py`, full field-level diff in `round2-diff.json`):

```
sha before: c03f3aa08be5a0d140d4c903d8b8f2183f818138bbe23ab20d2d5e4d335251d3 1873272
sha after : a93df91c19e52317da1f30315ed4bfe740f1eaa6d0b8ec501418d0dc958e7a64 1874381
round-trip byte identical: True
top-level keys changed vs pre-round-2: ['photos']
top-level keys changed vs pre-r3b   : ['photos']
refresh_revision: 1 -> 1
key count: 24 24
rows changed: 3 ['kl-5206ba734e80', 'kl-977b423768cd', 'kl-d05389364eb2']
live rows by view_kind: {'exterior': 43, 'floor_plan': 4, 'interior': 28, 'layout': 3, 'lobby': 1}
renderable (hotlink gate) by view_kind: {'exterior': 43, 'floor_plan': 4, 'interior': 27, 'layout': 3, 'lobby': 1}
withheld rows: 26 groups: 55
outcomes: no image 17, exterior/lobby-only 9, room-level 29, total 55
city_store.py --check: OK (city-store/1, 55 venues)
```

The per-row change list is in `photo-changes.json`.

## Kind verification, and what it rests on

Every new image was downloaded, decoded and measured (`image_sanity.py`):
dimensions match the stored record, every `interior`/`layout` asset is a
photograph (near-white share 0.00–0.13, normal saturation), and the one
`floor_plan` asset is line art (82% near-white, saturation 0.1). No image
labelled a photo measured like a plan, and vice versa.

Residual uncertainty, stated plainly: this worker has no vision tool, so
"what the photo depicts" is taken from the publishing page's own label (alt
text, asset title, section heading, room panel) plus the file name — the same
standard the R3 pass used (`alt_basis` records it per row). The mechanical
checks can separate a plan from a photograph and confirm the asset is live;
they cannot tell a room from a building. Two spots carry more of that risk than
the rest:

1. Colony's `*-capacity-desktop.jpg` assets are named for the capacity panel but
   measure as photographs (EXIF DateTime 2025:06:20, no large white panel), and
   the page's own `<article>` heading and alt text name the event lounge. Read as
   interior on that evidence.
2. The WTC Dewan Merdeka gallery images carry no captions. They are read as
   interior from the file series (`WTCKL_MERDEKA-HALL_*`) and the venue page's
   "Venue Gallery" placement only.

If a reviewer can open the images, those three WTC files and the two Colony
"capacity" files are the ones worth eyeballing first.

## Other conflicts and notes

- The R1 record for WTC "Hall 1" cannot be disambiguated from the operator's two
  identically specified halls. That is a record-level ambiguity, not a photo
  problem, and it was left alone.
- No separately labelled past-event album was reachable as addressable images.
  Where the operator's venue gallery shows the room set for an event (WTC, MO,
  Colony), the photo is recorded as `interior`/`layout` with the event setup
  stated in `alt`; none is labelled `past_event`.
- `research-log.md` and `holiday-supplement.json` were already modified before
  this card (mtime 05:54); this card did not touch them. Only `city.json`
  changed among the store files.

## Follow-ups

1. Eyeball the five flagged assets (WTC Merdeka 71/55/41, Colony KLCC/Eco City
   capacity images) if a vision-capable reviewer is available.
2. A per-room photo pass for the St. Regis Astor subdivisions and the W
   Great Room / Studio subdivisions needs a hire pack or PDF floor plan the
   operator does not publish on the pages read.
3. KLCC Plenary Hall/Theatre need either a per-room plan published as an image
   or an extracted room plan from the capacity-chart PDF; the inline SVG floor
   plans are the place to start.
4. Shangri-La and Traders need a route past Cloudflare (operator media library
   or a hire pack) before any function-space photo can be verified.
