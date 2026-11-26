#!/usr/bin/env python3
"""Apply the R3b Kuala Lumpur photo pass to the city store.

Only the top-level `photos` mapping is touched. Every new row carries the page
that publishes the image, the wording that labels it, a rights statement, and a
placement proof. Withheld placeholders are removed where a venue now has a
verified image, and annotated with the routes checked where it does not.
"""
import json
from pathlib import Path

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur")
STORE = BASE / "city" / "city.json"
PROBES = ["spec-batch1-probe.json", "spec-batch2-probe.json", "spec-batch3-probe.json",
          "spec-batch4-probe.json",
          "spec-batch5-probe.json"]
CHECKED = "2026-11-26"

probe = {}
for name in PROBES:
    for row in json.loads((Path(__file__).parent / name).read_text()):
        probe[row["slug"]] = row

COLONY_RIGHTS = ("Operator gallery asset, © Colony Coworking Space; hotlinked from colony.work "
                 "with attribution; the page publishes no separate licence.")
COLONY_PAGE = "https://colony.work/event-space-for-rent-kl/"
MONTKIARA_PAGE = "https://colony.work/mont-kiara-coworking-and-event-space/"
MARRIOTT_RIGHTS = ("Operator gallery asset, © Marriott International; hotlinked from "
                   "cache.marriott.com with attribution; the page publishes no separate licence.")
MO_RIGHTS = ("Operator gallery asset, © Mandarin Oriental Hotel Group; hotlinked from "
             "media.ffycdn.net with attribution; the page publishes no separate licence.")

NEW = [
    # --- Colony, Mont Kiara rooms (operator event-space page + location page) ---
    dict(vid="kl-0cdc4b71c244", slug="colony-boardroom-event", view_kind="interior",
         alt="The Boardroom at Colony Mont Kiara",
         alt_basis="operator alt text 'The Boardroom - Colony event space Mont Kiara (The MET)'",
         placement_proof=("Colony's own event-space page serves this slide inside its 'The Boardroom' venue "
                          "panel, and the alt text names the room and Mont Kiara (The MET); the same page "
                          "prints The Boardroom's capacity."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    dict(vid="kl-4eb04c3f3d6e", slug="colony-sunroom-event", view_kind="interior",
         alt="The Sun Room at Colony Mont Kiara",
         alt_basis="operator alt text 'The Sun Room - Colony event space Mont Kiara (The MET)'",
         placement_proof=("Colony's own event-space page serves this slide inside its 'The Sun Room' venue "
                          "panel, and the alt text names the room and Mont Kiara (The MET)."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    dict(vid="kl-da30b023d91a", slug="colony-glassbox-event", view_kind="interior",
         alt="The Glass Box at Colony Mont Kiara",
         alt_basis="operator alt text 'The Glass Box - Colony event space Mont Kiara (The MET)'",
         placement_proof=("Colony's own event-space page serves this slide inside its 'The Glass Box' venue "
                          "panel, and the alt text names the room and Mont Kiara (The MET)."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    dict(vid="kl-2b41c6e4e1f7", slug="colony-lounge-event", view_kind="interior",
         alt="The Lounge at Colony Mont Kiara",
         alt_basis="operator alt text 'The Lounge - Colony event space Mont Kiara (The MET)' and file name '70-guests'",
         placement_proof=("Colony's own event-space page serves this slide inside its 'The Lounge' venue "
                          "panel, and the alt text names the room and Mont Kiara (The MET)."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    # Mont Kiara location page carries a second, uncropped view of two rooms
    dict(vid="kl-0cdc4b71c244", slug="cmk-boardroom", view_kind="interior",
         alt="The Boardroom at Colony Mont Kiara",
         alt_basis="operator file name 'the-boardroom-cropped-1A' in the Mont Kiara event-space gallery",
         placement_proof=("The Mont Kiara location page's event-space gallery serves 'the-boardroom-cropped-1A'; "
                          "the file name carries the room and the page is Colony's Mont Kiara property page."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=MONTKIARA_PAGE),
    dict(vid="kl-da30b023d91a", slug="cmk-glassbox-banquet", view_kind="interior",
         alt="The Glass Box at Colony Mont Kiara laid out for a banquet",
         alt_basis="operator file name 'The-Glass-Box-banquet-1' and alt 'the-glass-box' on the Mont Kiara page",
         placement_proof=("The Mont Kiara location page's event-space gallery serves 'The-Glass-Box-banquet-1' "
                          "with alt 'the-glass-box'; the page is Colony's Mont Kiara property page."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=MONTKIARA_PAGE),
    # --- Colony event lounges: the venue-card image names the room ---
    dict(vid="kl-a72a6c5f539d", slug="colony-klcc-capacity", view_kind="interior",
         alt="The Event Lounge at KLCC, Colony's two-storey event space",
         alt_basis="operator alt text 'Event Lounge at KLCC - Colony event space KLCC'",
         placement_proof=("Colony's event-space page serves this image inside the <article> whose own <h3> reads "
                          "'Event Lounge at KLCC', and the alt text names the room and KLCC."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    dict(vid="kl-b375b5ac812b", slug="colony-ecocity-capacity", view_kind="interior",
         alt="The Event Lounge at KL Eco City, Colony's event space",
         alt_basis="operator alt text 'Event Lounge at KL Eco City - Colony event space KL Eco City'",
         placement_proof=("Colony's event-space page serves this image inside the <article> whose own <h3> reads "
                          "'Event Lounge at KL Eco City', and the alt text names the room and the estate."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    # --- Colony rooftop: outdoor space, labelled exterior ---
    dict(vid="kl-1fb682196274", slug="colony-rooftop-event", view_kind="exterior",
         alt="The Rooftop Terrace at Colony Mont Kiara, an open-air event space",
         alt_basis="operator alt text 'Rooftop Terrace - Colony event space Mont Kiara (The MET)' and the page's own 'open-air outdoor event spaces' description",
         placement_proof=("Colony's event-space page serves this slide inside its 'Rooftop Terrace' venue panel; "
                          "the page describes its venues as including 'open-air outdoor event spaces and "
                          "breathtaking rooftop event spaces', so this is an outdoor space, not a room."),
         attribution="Colony Coworking Space", rights=COLONY_RIGHTS, source_page=COLONY_PAGE),
    # --- WORQ event hall at Sunway Putra ---
    dict(vid="kl-e67bf1a8718b", slug="worq-spm-event-01", view_kind="interior",
         alt="The WORQ event hall at Sunway Putra Mall, Kuala Lumpur",
         alt_basis="operator alt text 'WORQ Sunway Putra Mall Event Space'",
         placement_proof=("The record's address is Level 4-1, Sunway Putra Mall; WORQ's own Sunway Putra "
                          "location page serves this photo in its gallery with alt 'WORQ Sunway Putra Mall "
                          "Event Space'. The record's coordinate 3.1664, 101.6923 falls on Sunway Putra Mall "
                          "(3.1664, 101.6924), 0.0 km from the building."),
         attribution="WORQ Coworking Space",
         rights=("Operator gallery asset, © WORQ Coworking Space; hotlinked from worq.space with attribution; "
                 "the page publishes no separate licence."),
         source_page="https://worq.space/location/sunway-putra/"),
    dict(vid="kl-e67bf1a8718b", slug="worq-spm-event-02", view_kind="interior",
         alt="The WORQ event hall at Sunway Putra Mall, second view",
         alt_basis="operator alt text 'WORQ Sunway Putra Mall Event Space'",
         placement_proof=("Same Sunway Putra location gallery as the first view; the record's address and "
                          "coordinate both land on Sunway Putra Mall."),
         attribution="WORQ Coworking Space",
         rights=("Operator gallery asset, © WORQ Coworking Space; hotlinked from worq.space with attribution; "
                 "the page publishes no separate licence."),
         source_page="https://worq.space/location/sunway-putra/"),
    # --- DOJO event halls ---
    dict(vid="kl-977b423768cd", slug="dojo-event-hall", view_kind="interior",
         alt="DOJO's event hall at Menara Amplewest",
         alt_basis="operator file name 'event-hall-dojo-1' in the page's 'Featured Event Space' carousel",
         placement_proof=("DOJO's own event-and-meeting page serves this photo in its 'Featured Event Space' "
                          "carousel; the same page lists the event halls (NAMI, ZEN, MORI, MEGA HALL) at "
                          "Level 1, Menara Amplewest, 6 Jalan P. Ramlee."),
         attribution="DOJO Coworking Space",
         rights=("Operator gallery asset, © DOJO Coworking Space; hotlinked from workspacedojo.com with "
                 "attribution; the page publishes no separate licence."),
         source_page="https://workspacedojo.com/event-meeting-plan/"),
    # --- WTC Kuala Lumpur, Dewan Merdeka venue gallery ---
    dict(vid="kl-9026a709cac0", slug="wtc-merdeka-71", view_kind="interior",
         alt="Dewan Merdeka at World Trade Centre Kuala Lumpur",
         alt_basis="venue page section 'Venue Gallery', file series WTCKL_MERDEKA-HALL",
         placement_proof=("World Trade Centre Kuala Lumpur's own Dewan Merdeka venue page serves this file in "
                          "the page's 'Venue Gallery'; the page is the venue's own page and the file name "
                          "carries 'MERDEKA-HALL'."),
         attribution="World Trade Centre Kuala Lumpur",
         rights=("Operator gallery asset, © World Trade Centre Kuala Lumpur; hotlinked from "
                 "worldtradecentrekl.com with attribution; the page publishes no separate licence."),
         source_page="https://worldtradecentrekl.com/venue/dewan-merdeka/"),
    dict(vid="kl-9026a709cac0", slug="wtc-merdeka-55", view_kind="interior",
         alt="Dewan Merdeka at World Trade Centre Kuala Lumpur, second view",
         alt_basis="venue page section 'Venue Gallery', file series WTCKL_MERDEKA-HALL",
         placement_proof="Same Dewan Merdeka 'Venue Gallery' as the first view.",
         attribution="World Trade Centre Kuala Lumpur",
         rights=("Operator gallery asset, © World Trade Centre Kuala Lumpur; hotlinked from "
                 "worldtradecentrekl.com with attribution; the page publishes no separate licence."),
         source_page="https://worldtradecentrekl.com/venue/dewan-merdeka/"),
    dict(vid="kl-9026a709cac0", slug="wtc-merdeka-41", view_kind="interior",
         alt="Dewan Merdeka at World Trade Centre Kuala Lumpur, third view",
         alt_basis="venue page section 'Venue Gallery', file series WTCKL_MERDEKA-HALL",
         placement_proof="Same Dewan Merdeka 'Venue Gallery' as the first view.",
         attribution="World Trade Centre Kuala Lumpur",
         rights=("Operator gallery asset, © World Trade Centre Kuala Lumpur; hotlinked from "
                 "worldtradecentrekl.com with attribution; the page publishes no separate licence."),
         source_page="https://worldtradecentrekl.com/venue/dewan-merdeka/"),
    # --- Connexion Auditorium floor plan ---
    dict(vid="kl-ee4e1a43a7dd", slug="ccec-auditorium-plan", view_kind="floor_plan",
         alt="Auditorium floor plan at Connexion Conference & Event Centre",
         alt_basis=("operator file name 'Auditorium-scaled' in the Auditorium room section of the centre's "
                    "'Capacity & Floor Plan' page"),
         placement_proof=("The centre's 'Capacity & Floor Plan' page carries a per-room 'Floor Plan' block and "
                          "serves 'Auditorium-scaled' in the Auditorium block; the image is line art "
                          "(81.9% near-white pixels, zero colour saturation), consistent with a plan, and the "
                          "same page lists the Auditorium."),
         attribution="Connexion Conference & Event Centre (CCEC)",
         rights=("Operator site asset, © Connexion Conference & Event Centre; hotlinked from connexioncec.com "
                 "with attribution; the page publishes no separate licence."),
         source_page="https://connexioncec.com/capacity-and-floor-plan/"),
    # --- The RuMa, Bilik I meeting room ---
    dict(vid="kl-496b88997888", slug="ruma-bilik1", view_kind="interior",
         alt="Bilik I meeting room at The RuMa Hotel and Residences",
         alt_basis=("operator alt text 'Modern conference room with a long table, and leather chairs at The RuMa "
                    "Hotel and Residences' and file name 'ruma-bilik-I-boardroom'"),
         placement_proof=("The RuMa's own meetings-and-events page serves this in its meetings carousel with alt "
                          "text naming The RuMa; the file name names Bilik I, one of the meeting rooms the same "
                          "page lists."),
         attribution="The RuMa Hotel and Residences",
         rights=("Operator gallery asset, © The RuMa Hotel and Residences; hotlinked from theruma.com with "
                 "attribution; the page publishes no separate licence."),
         source_page="https://theruma.com/en/kuala-lumpur-luxury-hotel-meetings-and-events/"),
    # --- St. Regis: the whole Astor Rooms ---
    dict(vid="kl-d05389364eb2", slug="stregis-astor-room", view_kind="interior",
         alt="The Astor Rooms at The St. Regis Kuala Lumpur",
         alt_basis=("operator file name 'kulxr-astor-room-5291' in the events page's 'Iconic Spaces' carousel"),
         placement_proof=("The hotel's own Marriott events page serves this in its 'Iconic Spaces' event-space "
                          "carousel; the asset name carries the property code KULXR and the room name "
                          "'astor-room', and the same page's capacity table lists 'The Astor Rooms'. The image "
                          "shows the combined room, so it is recorded only on the combined-room record."),
         attribution="The St. Regis Kuala Lumpur (Marriott International)", rights=MARRIOTT_RIGHTS,
         source_page="https://www.marriott.com/en-us/hotels/kulxr-the-st-regis-kuala-lumpur/events/"),
    # --- W: Studio Three ---
    dict(vid="kl-5206ba734e80", slug="w-studio-three", view_kind="layout",
         alt="Studio Three in theatre layout at W Kuala Lumpur",
         alt_basis="operator alt text 'Studio Three - Theatre Setup'",
         placement_proof=("The hotel's own events page serves this asset with alt 'Studio Three - Theatre Setup' "
                          "in its meeting-room cards, and the same page's capacity table lists the Studios. "
                          "'Studio Three' matches the record's Studio 3."),
         attribution="W Kuala Lumpur (Marriott International)", rights=MARRIOTT_RIGHTS,
         source_page="https://www.marriott.com/en-us/hotels/kulwh-w-kuala-lumpur/events/"),
    # --- Mandarin Oriental function space ---
    dict(vid="kl-f13a656c8b31", slug="mo-grand-ballroom", view_kind="interior",
         alt="Theatre seating in the Grand Ballroom at Mandarin Oriental, Kuala Lumpur",
         alt_basis="operator gallery asset title 'Theatre seating at Grand Ballroom at Mandarin Oriental, Kuala Lumpur'",
         placement_proof=("Mandarin Oriental Kuala Lumpur's own meetings-and-events page serves this asset in the "
                          "Grand Ballroom carousel with that title; the page is the Kuala Lumpur property's "
                          "meeting-space page at Kuala Lumpur City Centre."),
         attribution="Mandarin Oriental, Kuala Lumpur", rights=MO_RIGHTS,
         source_page="https://www.mandarinoriental.com/en/kuala-lumpur/petronas-towers/meet"),
    dict(vid="kl-f13a656c8b31", slug="mo-diamond-ballroom", view_kind="interior",
         alt="Classroom seating in the Diamond Ballroom at Mandarin Oriental, Kuala Lumpur",
         alt_basis="operator gallery asset title 'Classroom seating at Diamond Ballroom at Mandarin Oriental, Kuala Lumpur'",
         placement_proof=("Same Mandarin Oriental Kuala Lumpur meetings page, Diamond Ballroom carousel, with the "
                          "room named in the asset title."),
         attribution="Mandarin Oriental, Kuala Lumpur", rights=MO_RIGHTS,
         source_page="https://www.mandarinoriental.com/en/kuala-lumpur/petronas-towers/meet"),
    # --- Common Ground Ampang and KL Eco City event spaces ---
    dict(vid="kl-79df5ab85172", slug="cg-ampang-event-space", view_kind="interior",
         alt="Common Ground Ampang event space",
         alt_basis=("page section 'Get Together, Host Events and Discussions' on the Ampang location page; file "
                    "name carries 'ap_es' (Ampang event space)"),
         placement_proof=("Common Ground's own Ampang location page serves this in the section headed 'Get Together, "
                          "Host Events and Discussions'; the file name carries 'ap_es' (Ampang event space) and the "
                          "page is the Ampang property page."),
         attribution="The Flexi Group (Common Ground)",
         rights=("Operator site asset, © The Flexi Group; hotlinked from commonground.work with attribution; the "
                 "page publishes no separate licence."),
         source_page="https://commonground.work/malaysia/ampang"),
    dict(vid="kl-bba8243f4e1d", slug="cg-klec-event-space", view_kind="interior",
         alt="Common Ground KL Eco City event space",
         alt_basis=("page section 'Get Together, Host Events and Discussions' on the KL Eco City location page; "
                    "file name carries 'klec' and 'es' (KL Eco City event space)"),
         placement_proof=("Common Ground's own KL Eco City location page serves this in the section headed 'Get "
                          "Together, Host Events and Discussions'; the file name carries 'klec' (KL Eco City) and "
                          "'es' (event space)."),
         attribution="The Flexi Group (Common Ground)",
         rights=("Operator site asset, © The Flexi Group; hotlinked from commonground.work with attribution; the "
                 "page publishes no separate licence."),
         source_page="https://commonground.work/malaysia/kl-eco-city"),
    # --- GMBB: The Grey Box event hall ---
    dict(vid="kl-7dcb2f4ad570", slug="gmbb-greybox-1a", view_kind="interior",
         alt="The Grey Box, GMBB's multipurpose event hall on Level G",
         alt_basis="operator page section 'THE GREY BOX' on the shared-spaces directory; file name '1A'",
         placement_proof=("GMBB's own shared-spaces directory describes 'THE GREY BOX' as an event hall on Level G "
                          "at GMBB, 2 Jalan Robertson (7 m ceiling, 110 pax), and serves this photo inside that "
                          "section."),
         attribution="GMBB",
         rights=("Operator gallery asset, © GMBB; hotlinked from gmbb.com.my with attribution; the page publishes "
                 "no separate licence."),
         source_page="https://gmbb.com.my/directory/shared-space/"),
]

# Venues where the hunt ended with no room-level image: append the routes to the
# existing withheld placeholder's rights_note.
ROUTES = {
    "kl-06d6f98467c0": ("the operator's meeting-rooms and event-spaces pages returned a Cloudflare challenge "
                        "(403), the Cvent listing's gallery is script-rendered with no operator asset, and no "
                        "Commons file depicts the function space"),
    "kl-451839c5383d": ("the operator's meeting-rooms and event-spaces pages returned a Cloudflare challenge "
                        "(403), the Cvent listing's gallery is script-rendered with no operator asset, and no "
                        "Commons file depicts the function space"),
    "kl-1e5cf3e49cb1": ("the operator home page carries only a mall hero image, /events carries none, the "
                        "event-spaces path returned 404 in the first pass, and the marketplace listing that names "
                        "MAP's halls is third-party and carries no addressable operator asset"),
    "kl-0c62e94089f8": ("the MECC path returned 404 and mecc.matrade.gov.my now returns a 44-byte stub; the only "
                        "floor plan found is ExpoFP's third-party 3D plan, which is not the operator's asset"),
    "kl-2758407243f1": ("the host does not resolve (DNS failure on 2026-11-26, as in the first pass) and no "
                        "archived snapshot exists"),
    "kl-8cd52f2406dc": ("the host does not resolve (DNS failure on 2026-11-26, as in the first pass) and no "
                        "archived snapshot exists"),
    "kl-b3c3f49638f4": ("the operator site serves a maintenance page and the Wayback snapshot is itself a "
                        "challenge page, so no room image or floor plan could be read"),
    "kl-ef79384c8cb6": ("the domain now serves an unrelated gambling page; no operator page exists to check"),
    "kl-7d5505fb90ae": ("the event-space page and the Mid Valley location page carry only generic shared imagery "
                        "with no room label or alt text, and no per-room gallery or plan is published"),
    "kl-aadb1df3eba1": ("the event-space page and the GTower location page carry only generic shared imagery with "
                        "no room label or alt text, and no per-room gallery or plan is published"),
    "kl-de410ec2db9b": ("wework.com's event-space path returned a Cloudflare challenge (403); the venue is a "
                        "multi-location record whose coordinate is not Equatorial Plaza, so the Venuerific listing "
                        "for Equatorial Plaza's rooms cannot be placed on it"),
    "kl-ce3f20a09b7e": ("the floor-plan page's plans are inline SVG (not addressable image files), the one "
                        "addressable plan is an image-only three-page PDF covering the whole centre, the 360 "
                        "gallery is script-rendered, and every per-room URL pattern tried returned 404"),
    "kl-81d962290b05": ("the floor-plan page's plans are inline SVG (not addressable image files), the one "
                        "addressable plan is an image-only three-page PDF covering the whole centre, the 360 "
                        "gallery is script-rendered, and every per-room URL pattern tried returned 404"),
    "kl-b5d70a38c3ac": ("the operator serves one 'Astor Room' asset, which is the combined room and is recorded on "
                        "The Astor Rooms; no image and no room-specific plan identifies Astor Room 1 alone"),
    "kl-847775bf825b": ("the operator serves one 'Astor Room' asset, which is the combined room and is recorded on "
                        "The Astor Rooms; no image and no room-specific plan identifies Astor Room 2 alone"),
    "kl-c2ad59673c94": ("the operator serves one 'Astor Room' asset, which is the combined room and is recorded on "
                        "The Astor Rooms; no image and no room-specific plan identifies Astor Room 3 alone"),
    "kl-150d9ba42b7e": ("the operator serves one 'Astor Room' asset, which is the combined room and is recorded on "
                        "The Astor Rooms; no image or plan identifies the 1-and-2 configuration specifically"),
    "kl-a638cc0aca94": ("the operator serves one 'Ringgit Room' asset that does not say which half it shows, so it "
                        "cannot be placed on Ringgit Room 1 without guessing"),
    "kl-30a190b7c4bf": ("the operator serves one 'Ringgit Room' asset that does not say which half it shows, so it "
                        "cannot be placed on Ringgit Room 2 without guessing"),
    "kl-3a2adf0f8901": ("the operator serves one 'Great Room' asset, already recorded on the whole Great Room "
                        "record; no image or plan identifies Great Room 1 alone"),
    "kl-f210808ad5ea": ("the operator serves one 'Great Room' asset, already recorded on the whole Great Room "
                        "record; no image or plan identifies Great Room 2 alone"),
    "kl-dbee37a1fb3e": ("the operator's meeting-room cards name 'Studio Room' and 'Studio Three' only; no image or "
                        "plan identifies Studio 1"),
    "kl-31e23e1eff30": ("the operator's meeting-room cards name 'Studio Room' and 'Studio Three' only; no image or "
                        "plan identifies Studio 2"),
    "kl-8d0f532cde2b": ("the operator lists The Gallery within Level 1A and serves a Level 1A plan (already "
                        "recorded on MITEC - Level 1A Novel) but no Gallery-specific photo or plan; the photo "
                        "gallery's images carry no room labels"),
    "kl-1501b357e078": ("the operator site has no 'Hall 1' page, and the record's 1,003 sqm/1,000-guest hall "
                        "matches Tun Dr Ismail and Tun Hussein Onn identically, so no image can be placed on "
                        "'Hall 1' without choosing between them"),
    "kl-1fb682196274": ("the operator's event-space page shows the Rooftop Terrace only as an open-air space - its "
                        "own copy calls the venues 'open-air outdoor event spaces and breathtaking rooftop event "
                        "spaces' - so there is no room photograph to find and no terrace floor plan is published"),
}


def row_from(entry, index):
    p = probe[entry["slug"]]
    if p.get("status") != 200 or "width" not in p:
        raise SystemExit("probe failed for {}: {}".format(entry["slug"], p))
    return {
        "alt": entry["alt"],
        "alt_basis": entry["alt_basis"],
        "attribution": entry["attribution"],
        "checked_on": CHECKED,
        "dimensions": {"height": p["height"], "width": p["width"]},
        "hotlink_ok": True,
        "index": index,
        "placement_proof": entry["placement_proof"],
        "rights": entry["rights"],
        "source_page": entry["source_page"],
        "url": p["url"],
        "verified": {"bytes": p["bytes"], "content_type": p["content_type"], "status": p["status"]},
        "view_kind": entry["view_kind"],
        "withheld": False,
    }


def main():
    store = json.loads(STORE.read_text(encoding="utf-8"))
    photos = store["photos"]
    gaining = sorted({e["vid"] for e in NEW})
    before = {vid: [dict(r) for r in rows] for vid, rows in photos.items()}

    for vid in gaining:
        rows = photos[vid]
        kept = [r for r in rows if not r.get("withheld")]
        removed = len(rows) - len(kept)
        if removed not in (0, 1):
            raise SystemExit("unexpected withheld placeholders on {}: removed {}".format(vid, removed))
        photos[vid] = kept

    next_index = {vid: (max((r.get("index", -1) for r in rows), default=-1) + 1)
                  for vid, rows in photos.items()}
    for entry in NEW:
        vid = entry["vid"]
        photos[vid].append(row_from(entry, next_index[vid]))
        next_index[vid] += 1

    for vid, note in ROUTES.items():
        rows = photos[vid]
        with_rows = [r for r in rows if r.get("withheld")]
        if not with_rows:
            src = (store["venues"][vid].get("fields", {}).get("source_url") or {}).get("value")
            rows.append({
                "alt": "No room-level photo of the venue",
                "alt_basis": "none",
                "checked_on": CHECKED,
                "index": next_index[vid],
                "licence": None,
                "licence_url": None,
                "player_page": None,
                "rights_basis": "none",
                "rights_note": ("No room-level photograph was found for this record; nothing is shown rather "
                                "than a look-alike or a placeholder. R3b (2026-11-26): also checked " + note + "."),
                "room": "none",
                "source_page": src,
                "url": None,
                "verified": None,
                "view_kind": "render",
                "withheld": True,
            })
            next_index[vid] += 1
            continue
        if len(with_rows) != 1:
            raise SystemExit("unexpected withheld rows on route venue {}: {}".format(vid, len(with_rows)))
        r = with_rows[0]
        base_note = (r.get("rights_note") or "").strip()
        r["rights_note"] = (base_note + " R3b (2026-11-26): also checked " + note + ".").strip()
        r["checked_on"] = CHECKED

    STORE.write_text(json.dumps(store, indent=1, sort_keys=False, ensure_ascii=False) + "\n",
                     encoding="utf-8")

    # report
    import collections
    def dist(snapshot):
        c = collections.Counter()
        for rows in snapshot.values():
            for r in rows:
                if not r.get("withheld"):
                    c[r.get("view_kind")] += 1
        return dict(sorted(c.items()))
    print("before", dist(before))
    print("after ", dist(photos))
    print("venues gaining images:", len(gaining))
    for vid in gaining:
        print("  ", store["venues"][vid]["name"], [r["view_kind"] for r in photos[vid] if not r.get("withheld")])
    print("no-room-photo notes:", len(ROUTES))


if __name__ == "__main__":
    main()
