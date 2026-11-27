import json
from pathlib import Path

DIMS = json.load(open(Path('/home/joe/repo_dev/coe-events/research/singapore/evidence/photo-dimensions.json')))

PHOTO_TOKENS = {
    'sg-123024e521a4': ['trehaus'],
    'sg-1f9af9e53c6a': ['offline room'],
    'sg-31b594bd4607': ['room2f', 'bras basah'],
    'sg-42a07044079a': ['ju space'],
    'sg-42a16aa5a0df': ['studio2f', 'waterloo'],
    'sg-47e22cc263a7': ['cypress', 'metro y', 'metropolitan'],
    'sg-5bab95b878e0': ['chrysalis', 'lovorth'],
    'sg-5be91e319a02': ['level 9', 'hive north bridge'],
    'sg-5d80f59cd550': ['pico'],
    'sg-6aaa43c58493': ['visual art'],
    'sg-83af406debab': ['dedao', 'high street centre - idol'],
    'sg-8b90835a276b': ['common ground'],
    'sg-8cb81459951c': ['rooftop', 'hive carpenter'],
    'sg-9787a5fba342': ['enclosed'],
    'sg-9d1a91764baf': ['first class', 'synergy'],
    'sg-a5d5d094bf2e': ['function room 4-5', 'isca'],
    'sg-afe29d71b4e8': ['masons'],
    'sg-b5dffa99af1f': ['function room 4-3', 'isca'],
    'sg-b988c8bb26eb': ['ntuc', 'training rooms 701'],
    'sg-bea2d52eb16e': ['highfive', 'entire venue'],
    'sg-dca78c5c3a05': ['mit universe', 'mit space'],
    'sg-ed2e35df4121': ['auditorium', 'collyer'],
    'sg-f1b65d2b83d9': ['level 17', 'suntec'],
    'sg-f6e791a82485': ['standard plus', 'rnn'],
}
ROOM = {
    'sg-123024e521a4': 'Event Hall', 'sg-1f9af9e53c6a': 'Ground Floor Event Space',
    'sg-31b594bd4607': 'City Space', 'sg-42a07044079a': 'Ju Space',
    'sg-42a16aa5a0df': 'City Workshop', 'sg-47e22cc263a7': 'Cypress',
    'sg-5bab95b878e0': 'Chrysalis', 'sg-5be91e319a02': 'Level 9 Lounge',
    'sg-5d80f59cd550': 'Pico Auditorium', 'sg-6aaa43c58493': 'Chinatown Gallery & Studio',
    'sg-83af406debab': 'Dedao Club Space', 'sg-8b90835a276b': 'Auditorium',
    'sg-8cb81459951c': 'Rooftop Lounge', 'sg-9787a5fba342': 'Enclosed Event Space',
    'sg-9d1a91764baf': 'First Class Room #05-20', 'sg-a5d5d094bf2e': 'Function Room 4-5',
    'sg-afe29d71b4e8': 'Main Room', 'sg-b5dffa99af1f': 'Function Room 4-3',
    'sg-b988c8bb26eb': 'Training Rooms 701 & 801', 'sg-bea2d52eb16e': 'Entire Venue',
    'sg-dca78c5c3a05': 'MIT Universe', 'sg-ed2e35df4121': 'Level 1 Auditorium',
    'sg-f1b65d2b83d9': 'Level 17 Common Area', 'sg-f6e791a82485': 'Standard Plus',
}

AHG = 'https://www.artshousegroup.sg'
NG = 'https://www.nationalgallery.sg'
MANUAL_PHOTOS = {
    'sg-34d6bf1ba39c': [
        (AHG + '/images/venues-microsite/tah/venues/gallery/screening-room-%d.jpg' % i, 'Screening Room at The Arts House', 'interior', 'Screening Room', 'Operator gallery image on the room page; filename names the room.')
        for i in (1, 2, 3, 4, 5, 6)],
    'sg-c5e0795f1042': [
        (AHG + '/images/venues-microsite/aac/venue-hire/multipurpose-hall/multipurpose-hall-%d.jpg' % i, 'Multi-Purpose Hall at Aliwal Arts Centre', 'interior', 'Multi-Purpose Hall', 'Operator gallery image on the hall page; filename names the hall.')
        for i in (4, 6, 7, 8, 9, 10)],
    'sg-5d3fcedef47c': [
        (NG + '/content/dam/about/venue-rental/glass-room/glass-room-masthead-%d.webp' % i, 'Glass Room at National Gallery Singapore', 'interior', 'Glass Room', 'Operator page masthead image for the Glass Room.')
        for i in (1, 2, 3)] + [
        (NG + '/content/dam/about/venue-rental/glass-room/glass-room-map.webp', 'Glass Room floor plan', 'floor_plan', 'Glass Room', 'Operator floor plan on the Glass Room page.'),
        (NG + '/content/dam/about/venue-rental/glass-room/glass-room-360-m.webp', 'Glass Room 360 view', 'interior', 'Glass Room', 'Operator 360 still on the Glass Room page.')],
    'sg-d9552dd03dd7': [
        (NG + '/content/dam/about/venue-rental/ngee-ann-kongsi-auditorium-and-foyer/the-ngee-ann-auditorium-masthead-%d.webp' % i, 'Ngee Ann Kongsi Auditorium', 'interior', 'Ngee Ann Kongsi Auditorium', 'Operator page masthead image for the auditorium.')
        for i in (1, 2, 3)] + [
        (NG + '/content/dam/about/venue-rental/ngee-ann-kongsi-auditorium-and-foyer/ngee-ann-foyer-map.webp', 'Ngee Ann Kongsi Auditorium foyer plan', 'floor_plan', 'Foyer', 'Operator floor plan on the auditorium page.'),
        (NG + '/content/dam/about/venue-rental/ngee-ann-kongsi-auditorium-and-foyer/ngee-ann-360-m.webp', 'Ngee Ann Kongsi Auditorium 360 view', 'interior', 'Ngee Ann Kongsi Auditorium', 'Operator 360 still on the auditorium page.')],
    'sg-09795cef4b0f': [
        ('https://www.justcoglobal.com/wp-content/uploads/2023/10/SG-12_MarinaSq-carousel-%d.jpg' % i, 'JustCo Marina Square centre interior', 'interior', 'Centre interior (not the listed event space)', 'Operator centre-page carousel image; depicts the centre, not the event room, so it is a labelled fallback.')
        for i in (1, 2, 3, 4)],
    'sg-13d49f8566fb': [
        ('https://images.squarespace-cdn.com/content/v1/6509091695d2fb63ff1b90d1/6dea85ee-2316-4682-8a94-0c94c61cf558/1KS-Workspot-11-Web.jpg', '1 Keong Saik workspot', 'interior', 'Workspace (not a hire room)', 'Operator page image of the Keong Saik workspace; no room-level hire exists, so it is a labelled fallback.'),
        ('https://images.squarespace-cdn.com/content/v1/6509091695d2fb63ff1b90d1/e6c8d33b-f3c5-4ba8-99df-8bc59fc86d5f/TWC-The_Commons-4.jpeg', 'The Commons at 1 Keong Saik', 'interior', 'The Commons (not a hire room)', 'Operator page image of the Commons; labelled fallback.'),
        ('https://images.squarespace-cdn.com/content/v1/6509091695d2fb63ff1b90d1/637c2ba7-33ef-4a4f-a1d8-f1ff05914a95/TWC-Space_Workspace-3.jpeg', 'Workspace at 1 Keong Saik', 'interior', 'Workspace (not a hire room)', 'Operator page image of the workspace; labelled fallback.'),
        ('https://images.squarespace-cdn.com/content/v1/6509091695d2fb63ff1b90d1/618e71e8-cabf-40ec-9db9-09e0097af181/TWC-Reception_Area-1.jpeg', 'Reception at 1 Keong Saik', 'lobby', 'Reception', 'Operator page image of the reception; labelled fallback.')],
}


def classify(alt):
    a = alt.lower()
    if 'floor plan' in a or 'layout plan' in a:
        return 'floor_plan'
    if any(w in a for w in ('building', 'facade', 'exterior', 'street view', 'parking', 'entrance')):
        return 'exterior'
    if any(w in a for w in ('reception', 'lobby')):
        return 'lobby'
    return 'interior'


def photo_records(vid):
    recs = []
    if vid in MANUAL_PHOTOS:
        items = MANUAL_PHOTOS[vid]
    elif vid in LISTING:
        items = []
        tokens = PHOTO_TOKENS.get(vid, [])
        for im in LISTING[vid]['images']:
            alt = im['alt']
            if not any(t in alt.lower() for t in tokens):
                continue
            items.append((im['url'], alt, classify(alt), ROOM.get(vid, 'Room'), 'Operator listing image on the room-specific page; alt text names the venue and view.'))
        # put interior first, then floor plan, then exterior/lobby
        order = {'interior': 0, 'floor_plan': 1, 'past_event': 2, 'lobby': 3, 'exterior': 4, 'render': 5}
        items.sort(key=lambda x: order.get(x[2], 9))
        items = items[:6]
    else:
        items = []
    for i, (url, alt, kind, room, proof) in enumerate(items):
        # A centre/workspace image that the operator caption places outside the
        # hire room is a fallback, whichever view_kind it carries.
        room_specific = (kind in ('interior', 'floor_plan', 'past_event')
                         and 'fallback' not in (proof or '').lower())
        dims = DIMS.get(url) or {}
        recs.append({
            'alt': alt,
            'alt_basis': 'operator_caption',
            'checked_on': CHECKED,
            'dimensions': {'height': dims.get('height'), 'width': dims.get('width')},
            'index': i,
            'licence': 'Operator-published image; hotlinked from the operator page, not copied or redistributed',
            'licence_url': None,
            'placement_proof': proof,
            'player_page': None,
            'rights_basis': 'operator_page',
            'rights_note': 'Image is published by the operator on the page that sells this room; no independent licence grant is claimed and the file is not copied into the repository.',
            'room': room,
            'room_specific': room_specific,
            'source_page': STORE['venues'][vid]['fields']['source_url']['value'],
            'url': url,
            'verified': True,
            'view_kind': kind,
            'distance_m': 0,
            'withheld': False,
        })
    if not recs:
        recs.append({
            'alt': 'No verifiable photo of the venue',
            'alt_basis': 'none',
            'checked_on': CHECKED,
            'dimensions': {'height': None, 'width': None},
            'index': 0,
            'licence': None,
            'licence_url': None,
            'placement_proof': 'Withheld: no image on a captured operator page could be placed at this venue or room on 2026-11-26.',
            'player_page': None,
            'rights_basis': 'none',
            'rights_note': 'Nothing is shown rather than a look-alike, stock image or unlicensed copy.',
            'room': 'none',
            'room_specific': False,
            'source_page': STORE['venues'][vid]['fields']['source_url']['value'],
            'url': None,
            'verified': None,
            'view_kind': None,
            'distance_m': None,
            'withheld': True,
        })
    return recs
