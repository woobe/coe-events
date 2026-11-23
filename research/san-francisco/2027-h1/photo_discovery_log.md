# Photo discovery log — San Francisco venues (R2-P, 2026-11-21)

Card: t_47a27ecd. Companion data file: `photos.raw.json` in the same directory.
This log records what was tried per venue, how many usable photos came out, and where a site blocked scraping.

## Method

- Source pages were fetched with plain `curl`/urllib GET using a normal browser user agent. No cookies, no session, no rendered browser.
- Image URLs were extracted from the raw HTML: `<img src>`, `srcset`, `og:image`, JSON-LD, CSS `background-image`. Front pages, about/venue pages and sub-pages were added when the rental page carried no photography.
- Every URL that made it into `photos.raw.json` was then checked with a plain request (no referer, no cookies). Only 2xx plus an `image/*` content type is recorded as `hotlink_ok: true`. Anything else was dropped from the list and noted here. HEAD is used first; where the host answers HEAD with a Content-Length of 1 (Squarespace CDN on some files), a 2048-byte range GET confirms the real bytes and type.
- Intrinsic sizes come from what the publisher itself declares: WordPress filename suffixes and width/height attributes, Squarespace `data-image-dimensions`/`originalSize`, or the WordPress media API (`/wp-json/wp/v2/media`). No image bytes were downloaded or saved, so sizes are as published, not measured.
- Alt text reuses the publisher's caption or `alt` attribute where one exists; otherwise it is built from the page section or the filename the image sits under, and `alt_basis` says which. Images were not visually inspected, so no description claims more than the venue publishes.

## Totals

- Venues in `venues.raw.json`: 16
- Venues with at least three usable photos: 11
- Venues with one or two: 2 (CounterPulse - Main Stage, The Marsh San Francisco - Mainstage)
- Venues with none: 3 (The Marsh San Francisco - Studio, Alliance Francaise de San Francisco - Theater, Common Space - Large Loft in the Marina)
- Photos listed and verified reachable: 49

## Per venue

### SOMArts Cultural Center - Main Event Space (Essentials Package) — 4 photos

- Tried: https://somarts.org/rentals/ (twice), https://somarts.org/, and the 2026-03-01 Wayback copy of the rentals page for structure.
- The host answered HTTP 429 (nginx "too many requests" page, 1168 bytes) to the page and to every `/wp-content/uploads` image on the first attempts, with or without a browser user agent. Roughly an hour later the same requests returned 200.
- Usable: the event space, the stage view, the dance studio and the outdoor-space event photo, all published on the rentals page. Verified 200 / image/jpeg.
- Left out: the floorplan diagram (not a photo) and the notices/opportunity banners at the top of the page (not venue photography).

### Root Division - Front & Rear Galleries — 5 photos

- Tried: https://rootdivision.org/about/the-space/venue-rental (only page needed).
- The page groups images by rental option ("Front Gallery", "Front & Rear Galleries"), which is how the descriptions were assigned. No alt text is published. A real event photo (Nohea Photography credit) is included after the empty-room shots.
- Verified 200 / image/jpeg, 51–221 KB.

### Four One Nine - Middle Gallery Extended (SoMa) — 5 photos

- Tried: https://www.fouronenine.com/ (the image gallery lives there, not on /inquire), /inquire, and the venue's own 2026 pricing sheet https://fouronenine.com/s/FON_Pricing_2026.pdf.
- The gallery block carries per-item titles in its page data, so the image-to-caption pairing was read from the JSON items, not guessed from layout order. Titles used: "Middle Gallery", "Library & Wet Bar", "Library", "Rooftop Garden", "Roof Deck (with covering)".
- The pricing sheet lists the Middle Gallery Extended package as "Includes Middle Gallery, Library, Rooftop ... Restrictions: No main studio or kitchen access". The set was therefore restricted to those rooms. The page's Main Gallery, Main Gallery (Empty), Main Gallery & Open Kitchen, Open Kitchen, Entrance and Roll-up Garage photos were deliberately left out because they show spaces the package excludes.
- Verified 200 / image/jpeg; the CDN returns WebP to curl on the first image. HEAD answers with a Content-Length of 1 on four of these URLs, so reachability was confirmed by a 2048-byte range GET (206 image/jpeg) instead.

### CounterPulse - Main Stage — 1 photo

- Tried: https://counterpulse.org/rentals/ (fetched once, 1.3 MB) and /mission-history/ (429).
- The page publishes three space photos (main stage, upstairs studio, project space). Only the main stage belongs to this venue entry.
- The host then returned 429 for every image for about an hour and answered 200 on a later retry. The listed 1024x768 copy is verified 200 / image/jpeg.

### The Women's Building - Audre Lorde Room — 3 photos

- Tried: https://www.womensbuilding.org/our-building/rent-a-space.
- The page publishes three room photos with full descriptive alt text, plus two layout diagrams. Diagrams were excluded.
- Verified 200 / image/jpeg. The page declares no pixel sizes (Webflow CDN), so `thumb_note` says so.

### The Marsh San Francisco - Mainstage — 2 photos

- Tried: https://themarsh.org/rental-pricing/ (the venue source page — no venue photography at all), the homepage, https://themarsh.org/our-venues/ and https://themarsh.org/about/the-marsh-venues/.
- Photos exist only on /our-venues/, one under "Mainstage" and one under "The Marsh San Francisco". 1280x720 copies are used to keep the weight down; the full-size files are 1.3 MB each.
- Verified 200 / image/jpeg.

### The Marsh San Francisco - Studio — no photos

- Tried: the same four pages. The "Studio Theater" section on /our-venues/ has no image at all, and no other Marsh page carries Studio photography.
- Nothing to list.

### Ruth Williams Opera House (Bayview Opera House) - Main Theater — 3 photos

- Tried: https://rwoh.org/rentals/ (only page needed).
- Three photos, all sharing one generic alt sentence. Floorplan images on the same page were excluded.
- Verified 200 / image/webp, 190–345 KB. These three files fail on HTTP/2 HEAD (`PROTOCOL_ERROR`) but answer 200 `image/webp` on HTTP/1.1 HEAD and 206 `image/webp` on a range GET; that is a host quirk, not a hotlink failure.

### Brava Theater Center - Lobby — 5 photos

- Tried: https://www.brava.org/rentals, https://www.brava.org/main-theater, https://www.brava.org/studio, https://www.brava.org/lobby (404).
- There is no lobby page. The lobby photos are in the gallery on the Main Theater rental page, captioned "Outer Lobby", "Lobby Boxes", "Inner Lobby Bar", "Inner Lobby". Five used.
- Verified 200 / image/jpeg; listed at 1500 px wide via Squarespace's own resize parameter.

### Brava Theater Center - Studio — 4 photos

- Tried: https://www.brava.org/studio.
- Four photos captioned "Studio Event" (twice), "Studio Bar", "Studio Chairs". The fourth is portrait (2400x3600), listed at 1500 px wide, 446 KB.
- Verified 200 / image/jpeg.

### The Lab - Main Auditorium (Redstone Building) — 5 photos

- Tried: https://www.thelab.org/rental.
- A seven-photo gallery of the reopening event, no captions, no alt text. Five used, all from filenames `260327_TheLab_Reopening_RDH_0xx`. Descriptions stay at the level the venue supplies.
- Verified 200 / image/jpeg; listed at 1500 px wide, 202–233 KB.

### Z Space - Z Lobby — 5 photos

- Tried: https://zspace.org/rent (the "Z LOBBY" section there has no image, only the gallery further down) and https://zspace.org/z-lobby, which carries a dedicated lobby gallery.
- Seven distinct images; five used. No captions beyond filenames; one filename names an event ("Opening Night Joe Goode Performance Group CoPro 2011").
- Verified 200 / image/jpeg.

### Z Space - Steindler Stage — 4 photos

- Tried: https://zspace.org/rent and https://zspace.org/mainstage.
- The stage page has a hero shot plus a "THE SPACE" gallery. Originals are 3.5k–5.6k px wide; three are listed at 1500 px wide via Squarespace's resize parameter, 71–137 KB.
- Verified 200 / image/jpeg.

### Alliance Francaise de San Francisco - Theater — no photos

- Tried: https://www.afsf.com/about-afsf/space-rental/theater-rental/ (the venue source page), https://www.afsf.com/about-afsf/space-rental/ (404), /cultural-center/, /about-afsf/our-history/, plus the site's sitemap to check for a gallery or rental sub-page.
- The theater rental page carries only the site logo and layout background tiles. The cultural-center page carries event banners and the history page carries historical portraits. There is no photo of the theater anywhere on the site.
- Nothing to list.

### Common Space - Large Loft in the Marina (Peerspace listing 647656b424653c000e5dacf6) — no photos

- Tried: https://www.peerspace.com/pages/listings/647656b424653c000e5dacf6, the `/ca/` locale variant, the API path `/api/v2/listings/...`, and a search for another publisher of the listing.
- Every peerspace.com request returned HTTP 403 (Cloudflare) for the whole run, including the listing page that the venue entry points at. The hosts' photos live on that listing only, so no URL could be verified.
- Nothing to list. This venue is the one place where photos are probably available but unreachable from this host.

### Gray Area - Lobby (Grand Theater) — 3 photos

- Tried: https://grayarea.org/services/venue-rental/ (canonical; the `venue-rental/` URL in `venues.raw.json` redirects there) and https://grayarea.org/venue-rental/.
- The page's rental-space block names four spaces in order: Grand Theater Rental, Lobby, Half Theater Rental, Classroom, each with one image directly under its heading. The "Lobby" heading (800 square feet, 80 capacity) is followed by `2024/06/©Barak-Shrama-12-scaled.jpg`, so that is listed first.
- The other two photos are the adjoining Grand Theater main room (6,000 square feet, 800 capacity): the "Conference & Corporate Productions" shot and the "Community & Private Events" shot. Their alt text and the venue `notes` say they are the theater, not the lobby. The remaining theater, half-theater and classroom photos were dropped so the set cannot be read as the 800 sq ft room.
- Sizes come from the WordPress media API (`/wp-json/wp/v2/media`): the lobby photo's original is 2560x1707 and the 768 px PNG variants are used for the two theater shots.
- Verified 200 / image/jpeg and image/png.

## Conflicts and uncertainty

- `venues.raw.json` has no `id` field, so `venue_id` in `photos.raw.json` is a deterministic kebab-case slug of the venue name and `venue_index` is the 0-based position in `venues.raw.json`. The card assumed an existing id; there is none, in this file or anywhere else in the package (`venues.shortlist.json`, `bundle_inputs.md`, `.bundle-1/` all lack one).
- Alt text is publisher-derived, not visually verified. No image bytes were fetched, so nothing here claims what a photo shows beyond what the venue's own caption, section or filename states. `alt_basis` records the source for each.
- Byte sizes are the values a plain request reports. Squarespace's CDN sometimes returns a Content-Length of 1 on HEAD while serving real bytes on GET (four Four One Nine URLs, confirmed with a 2048-byte range GET), and WordPress hosts serve WebP to curl for some PNGs, so `thumb_note` sometimes differs from what a browser will receive.
- SOMArts and CounterPulse were rate-limited for part of the run (HTTP 429) and answered normally later. PeerSpace was blocked for the whole run (HTTP 403).
- Hosts filter on user agent rather than referer: on the round-1 re-check somarts.org and counterpulse.org returned 403 to one stale Chrome/124 string while no user agent, curl's default and Chrome/131 all got 200 image/jpeg. rwoh.org is flakier: HEAD fails over HTTP/2 (`PROTOCOL_ERROR`), one Chrome/131 request got an empty reply, and Chrome/124, Chrome/140, Safari and no user agent all got 200/206 `image/webp` on HTTP/1.1. Both are user-agent/host quirks, not referer or session checks, so `hotlink_ok: true` stands.
- No venue offered licensed third-party photography that would have been legitimate to include, and none was padded with stock or city imagery.

## Review round 1 corrections (2026-11-21)

- Four One Nine: the first set showed Main Gallery, Roll-up Garage and Open Kitchen, which the venue's own 2026 pricing sheet excludes from the Middle Gallery Extended package. Those four were replaced with Middle Gallery, Library & Wet Bar, Library, Rooftop Garden and Roof Deck (with covering). Re-verified by range GET (206 image/jpeg).
- Gray Area: the first set was five Grand Theater main-room shots for a venue booked as the 800 sq ft lobby. The venue's own Lobby image (`2024/06/©Barak-Shrama-12-scaled.jpg`, percent-encoded in the URL, 2560x1707, 200 image/jpeg) is now listed first, and only two theater shots are kept with alt text and `notes` saying they show the adjoining Grand Theater, not the lobby.
- Both venues remain at or above three photos, so the coverage split is unchanged: 11 venues with three or more, 2 with one or two, 3 with none. Photos listed and verified: 49 (down from 51 because Gray Area was reduced from 5 to 3).
- Searched for the corrections: the Four One Nine homepage gallery JSON (item titles + asset URLs + originalSize), the 2026 pricing PDF, the Gray Area venue-rental page markup, and the Gray Area WordPress media API for the lobby image's intrinsic size.

## Note on alt text for a human reviewer

- Two descriptions still lean on publisher-supplied labels rather than eyeballed content: Z Space "set for a wedding" (from the venue's filename `bay-area-wedding-photography-501`) and the Gray Area theater shots ("set for conference and corporate productions", from the page section label). `alt_basis` marks both. A human eyeball is worth doing before publish.
