#!/usr/bin/env python3
"""Build the revision-1 Kuala Lumpur candidate store from the R3 evidence."""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlencode

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
R3 = BASE / 'r3-2026-11'
STORE = BASE / 'city' / 'city.json'
RUN = 'run-20261126-kl-r3'
STAMP = '2026-11-26'
UPDATED = '2026-11-26T09:00:00Z'

store = json.loads(STORE.read_text())
original = json.loads(STORE.read_text())

man = {}
for path in (R3 / 'capture-manifest.json', BASE / 'city' / 'capture-manifest.json'):
    if path.exists():
        for row in json.loads(path.read_text())['pages']:
            man.setdefault(row['slug'], row)


def capdir(slug):
    for d in (R3 / 'captures', BASE / 'city' / 'captures'):
        p = d / (slug + '.txt')
        if p.exists():
            return p
    raise KeyError(slug)


def cap_lines(slug):
    return [ln.rstrip('\n') for ln in capdir(slug).read_text(
        encoding='utf-8', errors='replace').splitlines()]


def q(slug, a, b=None):
    lines = cap_lines(slug)
    b = a if b is None else b
    return '\n'.join(lines[a - 1:b]).strip()


def src(slug):
    row = man.get(slug) or {}
    return row.get('url'), row.get('title')


def cid(vid, field, tag=''):
    return 'cl-' + hashlib.sha256(('%s|%s|%s|%s' % (RUN, vid, field, tag)).encode()).hexdigest()[:12]


def claim(vid, field, value, slug=None, lines=None, extra=None, quote=None,
          title=None, url=None, locator=None):
    if slug:
        u, t = src(slug)
        url, title = url or u, title or t
        if lines:
            locator = locator or 'capture %s lines %s' % (
                slug, lines[0] if len(lines) == 1 else '%s-%s' % (lines[0], lines[1]))
    row = {
        'claim_id': cid(vid, field, extra.get('_tag', '') if extra else ''),
        'run_id': RUN, 'verified_at': STAMP, 'value': value,
        'source_url': url, 'source_title': title,
    }
    if quote:
        row['quote'] = quote
    if locator:
        row['source_locator'] = locator
    if extra:
        for k, v in extra.items():
            if not k.startswith('_'):
                row[k] = v
    return row


def put(vid, field, row):
    venue = store['venues'][vid]
    old = venue['fields'].get(field)
    if old and old.get('claim_id') and old.get('claim_id') != row['claim_id']:
        venue.setdefault('history', {}).setdefault(field, []).append(old)
    venue['fields'][field] = row


# ---------------------------------------------------------------- coordinates
COORD = {
    # tier, lat, lon, map target, returned place
    'kl-0d48d9041b4d': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, Kampung Sungai Baru, Kampung Paya, Kampung Cendana, Kuala Lumpur, 50450, Malaysia'),
    'kl-3a2adf0f8901': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, ... 50450, Malaysia'),
    'kl-50c8e7eb20a3': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, ... 50450, Malaysia'),
    'kl-dbee37a1fb3e': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, ... 50450, Malaysia'),
    'kl-f210808ad5ea': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, ... 50450, Malaysia'),
    'kl-31e23e1eff30': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, ... 50450, Malaysia'),
    'kl-5206ba734e80': ('building', 3.1584938, 101.7094106, 'W Kuala Lumpur, 121 Jalan Ampang, 50450 Kuala Lumpur', '121, Jalan Ampang, ... 50450, Malaysia'),
    'kl-847775bf825b': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, KL Sentral, Kuala Lumpur, 50470, Malaysia'),
    'kl-a638cc0aca94': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, ... 50470, Malaysia'),
    'kl-b5d70a38c3ac': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, ... 50470, Malaysia'),
    'kl-c2ad59673c94': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, ... 50470, Malaysia'),
    'kl-d05389364eb2': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, ... 50470, Malaysia'),
    'kl-150d9ba42b7e': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, ... 50470, Malaysia'),
    'kl-30a190b7c4bf': ('building', 3.1368090, 101.6885767, 'The St. Regis Kuala Lumpur, 6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur', '6, Jalan Stesen Sentral 2, ... 50470, Malaysia'),
    'kl-da30b023d91a': ('building', 3.1807816, 101.6647099, 'The MET Corporate Towers, 20 Jalan Dutamas 2, 50480 Kuala Lumpur', 'The MET Corporate Towers, 20, Jalan Dutamas 2, KL Metropolis, Segambut, Kepong, Kuala Lumpur, 51200, Malaysia'),
    'kl-1fb682196274': ('building', 3.1807816, 101.6647099, 'The MET Corporate Towers, 20 Jalan Dutamas 2, 50480 Kuala Lumpur', 'The MET Corporate Towers, ... 51200, Malaysia'),
    'kl-2b41c6e4e1f7': ('building', 3.1807816, 101.6647099, 'The MET Corporate Towers, 20 Jalan Dutamas 2, 50480 Kuala Lumpur', 'The MET Corporate Towers, ... 51200, Malaysia'),
    'kl-0cdc4b71c244': ('building', 3.1807816, 101.6647099, 'The MET Corporate Towers, 20 Jalan Dutamas 2, 50480 Kuala Lumpur', 'The MET Corporate Towers, ... 51200, Malaysia'),
    'kl-4eb04c3f3d6e': ('building', 3.1807816, 101.6647099, 'The MET Corporate Towers, 20 Jalan Dutamas 2, 50480 Kuala Lumpur', 'The MET Corporate Towers, ... 51200, Malaysia'),
    'kl-a72a6c5f539d': ('building', 3.1521760, 101.7129298, 'Colony KLCC, 6 Jalan Kia Peng, 50450 Kuala Lumpur', '6, Jalan Kia Peng, Bukit Bintang, Kuala Lumpur, 50450, Malaysia'),
    'kl-1501b357e078': ('building', 3.1687535, 101.6915588, 'World Trade Centre Kuala Lumpur, 41 Jalan Tun Ismail, 50480 Kuala Lumpur', 'World Trade Centre Kuala Lumpur, 41, Jalan Tun Ismail, Chow Kit, Sentul, Kuala Lumpur, 50480, Malaysia'),
    'kl-9026a709cac0': ('building', 3.1687535, 101.6915588, 'World Trade Centre Kuala Lumpur, 41 Jalan Tun Ismail, 50480 Kuala Lumpur', 'World Trade Centre Kuala Lumpur, ... 50480, Malaysia'),
    'kl-496b88997888': ('building', 3.1524155, 101.7143738, 'The RuMa Hotel and Residences, 7 Jalan Kia Peng, 50450 Kuala Lumpur', 'The RuMa Hotel & Residences, 7, Jalan Kia Peng, Bukit Bintang, Kuala Lumpur, 50450, Malaysia'),
    'kl-7dcb2f4ad570': ('building', 3.1447455, 101.7045274, 'GMBB, 2 Jalan Robertson, 50150 Kuala Lumpur', 'GMBB, 2, Jalan Robertson, Bukit Bintang, Kuala Lumpur, 50150, Malaysia'),
    'kl-1e5cf3e49cb1': ('building', 3.1711882, 101.6658545, 'Publika Shopping Gallery, Solaris Dutamas, Jalan Dutamas, 50480 Kuala Lumpur', 'The Boulevard, Publika - Solaris Dutamas, Segambut, Kuala Lumpur, 50480, Malaysia'),
    'kl-b3c3f49638f4': ('building', 3.1711882, 101.6658545, 'Publika Shopping Gallery, Solaris Dutamas, Jalan Dutamas, 50480 Kuala Lumpur (The Bee outlet)', 'The Boulevard, Publika - Solaris Dutamas, Segambut, Kuala Lumpur, 50480, Malaysia'),
    'kl-e67bf1a8718b': ('building', 3.1663944, 101.6923863, 'WORQ Sunway Putra, Level 4-1 Sunway Putra Mall, 100 Jalan Putra, 50350 Kuala Lumpur', 'Sunway Putra Mall, 100, Jalan Putra, Chow Kit, Sentul, Kuala Lumpur, 50350, Malaysia'),
    'kl-d86dffabc235': ('building', 3.1790267, 101.6678236, 'MITEC, Kompleks MITEC, 8 Jalan Dutamas 2, 50480 Kuala Lumpur', 'Malaysia International Trade and Exhibition Centre, Jalan Boulevard, KL Metropolis, Segambut, Kepong, Kuala Lumpur, 50480, Malaysia'),
    'kl-a2b2e1986ea5': ('building', 3.1790267, 101.6678236, 'MITEC, Kompleks MITEC, 8 Jalan Dutamas 2, 50480 Kuala Lumpur', 'Malaysia International Trade and Exhibition Centre, ... 50480, Malaysia'),
    'kl-8d0f532cde2b': ('building', 3.1790267, 101.6678236, 'MITEC, Kompleks MITEC, 8 Jalan Dutamas 2, 50480 Kuala Lumpur', 'Malaysia International Trade and Exhibition Centre, ... 50480, Malaysia'),
    'kl-13ee3afff10b': ('building', 3.1790267, 101.6678236, 'MITEC, Kompleks MITEC, 8 Jalan Dutamas 2, 50480 Kuala Lumpur', 'Malaysia International Trade and Exhibition Centre, ... 50480, Malaysia'),
    'kl-06d6f98467c0': ('building', 3.1542618, 101.7068121, 'Shangri-La Kuala Lumpur, Jalan Sultan Ismail, 50250 Kuala Lumpur', 'Shangri-La, Jalan Sultan Ismail, Kampung Paya, Kampung Cendana, Kuala Lumpur, 50250, Malaysia'),
    'kl-451839c5383d': ('building', 3.1541033, 101.7150455, 'Traders Hotel Kuala Lumpur, Persiaran KLCC, 50088 Kuala Lumpur', 'Traders Hotel, Persiaran KLCC, Bukit Bintang, Kuala Lumpur, 50088, Malaysia'),
    'kl-0c62e94089f8': ('exact_venue', 3.1776540, 101.6667160, 'MATRADE Exhibition and Convention Centre, Menara MATRADE, Jalan Sultan Haji Ahmad Shah, 50480 Kuala Lumpur', 'MATRADE Exhibition and Convention Centre, Jalan Sultan Haji Ahmad Shah, Segambut, Kuala Lumpur, 50480, Malaysia'),
    'kl-6521a5218690': ('building', 3.1479745, 101.7183366, 'Common Ground Bukit Bintang, 198 Jalan Bukit Bintang, 55100 Kuala Lumpur', 'Lux Catering, 198, Jalan Bukit Bintang, Pinggiran TRX, Maluri, Bukit Bintang, Kuala Lumpur, 55100, Malaysia'),
    'kl-b32ee88b3dc6': ('building', 3.1536113, 101.7121373, 'Menara Darussalam, 12 Jalan Pinang, 50450 Kuala Lumpur', 'Grand Hyatt, 12, Jalan Pinang, Kampung Paya, Kampung Cendana, Kuala Lumpur, 50450, Malaysia'),
    'kl-aadb1df3eba1': ('building', 3.1590042, 101.7197559, 'G Tower, 199 Jalan Tun Razak, 50450 Kuala Lumpur', 'G Tower, 199, Jalan Tun Razak, Kampung Datuk Keramat, Kuala Lumpur, 50450, Malaysia'),
    'kl-cfd935e61947': ('building', 3.1096794, 101.6662169, 'Connexion Conference & Event Centre, Nexus, 7 Jalan Kerinchi, 59200 Kuala Lumpur', 'Connexion Conference & Event Centre, 7, Jalan Kerinchi, Bangsar South, Pantai Dalam, Kuala Lumpur, 59200, Malaysia'),
    'kl-ee4e1a43a7dd': ('building', 3.1096794, 101.6662169, 'Connexion Conference & Event Centre, Bangsar South, Jalan Kerinchi, 59200 Kuala Lumpur', 'Connexion Conference & Event Centre, 7, Jalan Kerinchi, ... 59200, Malaysia'),
    'kl-8cd52f2406dc': ('exact_venue', 3.1242885, 101.6740792, 'APW Bangsar, Jalan Riong, Bangsar, 59100 Kuala Lumpur', 'A Place Where - APW, Jalan Riong, Bangsar, Kuala Lumpur, 59100, Malaysia'),
    'kl-977b423768cd': ('building', 3.1520515, 101.7062312, 'DOJO Coworking, Jalan Puncak, 50250 Kuala Lumpur', 'DOJO Coworking space, Jalan Puncak, Bukit Bintang, Kuala Lumpur, 50250, Malaysia'),
    'kl-2758407243f1': ('exact_venue', 3.0723108, 101.6067125, 'Sunway Pyramid Convention Centre, 3 Jalan PJS 11/15, Bandar Sunway, 47500 Petaling Jaya, Selangor', 'Sunway Pyramid Convention Centre, CP3, To Roof Sunway Pyramid, Sunway City, PJS 11, Subang Jaya City Council, Petaling, Selangor, Malaysia'),
    'kl-f13a656c8b31': ('building', 3.1557412, 101.7118967, 'Mandarin Oriental Kuala Lumpur, Kuala Lumpur City Centre, 50088 Kuala Lumpur', 'Mandarin Oriental, Kuala Lumpur, Persiaran Petronas, Kuala Lumpur City Centre (KLCC), Kuala Lumpur, 50088, Malaysia'),
    'kl-81d962290b05': ('building', 3.1543230, 101.7126043, 'KLCC Convention Centre, Kuala Lumpur City Centre, 50088 Kuala Lumpur', 'KLCC Convention Center, KLCC-Bukit Bintang Pedestrian Walkway, Kuala Lumpur City Centre (KLCC), Bukit Bintang, Kuala Lumpur, 50088, Malaysia'),
    'kl-ce3f20a09b7e': ('building', 3.1543230, 101.7126043, 'KLCC Convention Centre, Kuala Lumpur City Centre, 50088 Kuala Lumpur', 'KLCC Convention Center, ... 50088, Malaysia'),
    'kl-de410ec2db9b': ('building', 3.1186464, 101.6740140, 'WeWork, Medan Syed Putra Selatan, 50614 Kuala Lumpur', 'WeWork, Medan Syed Putra Selatan, Seputeh, Kuala Lumpur, 50614, Malaysia'),
    'kl-73ee37f91926': ('building', 3.1851390, 101.6863584, 'Kuala Lumpur Performing Arts Centre (klpac), Sentul Park, Jalan Strachan, 51100 Kuala Lumpur', 'Kuala Lumpur Performing Arts Centre (KLPAC), Jalan Strachan, Million Garden, Sentul, Kuala Lumpur, 51100, Malaysia'),
    'kl-ade0334f2820': ('building', 3.1851390, 101.6863584, 'Kuala Lumpur Performing Arts Centre (klpac), Sentul Park, Jalan Strachan, 51100 Kuala Lumpur', 'Kuala Lumpur Performing Arts Centre (KLPAC), ... 51100, Malaysia'),
    'kl-dc1d07124580': ('building', 3.1851390, 101.6863584, 'Kuala Lumpur Performing Arts Centre (klpac), Sentul Park, Jalan Strachan, 51100 Kuala Lumpur', 'Kuala Lumpur Performing Arts Centre (KLPAC), ... 51100, Malaysia'),
    'kl-b375b5ac812b': ('area', 3.1179206, 101.6736487, 'KL Eco City, Jalan Bangsar, 59200 Kuala Lumpur', 'KL Eco City, Seputeh, Kuala Lumpur, Malaysia'),
    'kl-bba8243f4e1d': ('area', 3.1179206, 101.6736487, 'KL Eco City, Jalan Bangsar, 59200 Kuala Lumpur', 'KL Eco City, Seputeh, Kuala Lumpur, Malaysia'),
    'kl-7d5505fb90ae': ('area', 3.1185060, 101.6768457, 'Mid Valley City, Lingkaran Syed Putra, 59200 Kuala Lumpur', 'Mid Valley City, Seputeh, Kuala Lumpur, Malaysia'),
    'kl-7dd2a97334c6': ('street', 3.0702000, 101.7027770, 'No.68, Kuala Lumpur-Seremban Expressway, Taman Bukit, 57100 Kuala Lumpur', 'Kuala Lumpur\u2013Seremban Expressway, Taman Castlefield, Sungai Besi, Kuala Lumpur, 57000, Malaysia'),
    'kl-ef79384c8cb6': ('street', 3.1576940, 101.6997200, 'Jalan Doraisamy, Chow Kit, 50100 Kuala Lumpur', 'Jalan Doraisamy, Kampung Periuk, Chow Kit, Kampung Cendana, Kuala Lumpur, 50100, Malaysia'),
    'kl-79df5ab85172': ('street', 3.1611045, 101.7534624, 'Jalan Kolam Air Lama, 68000 Ampang Jaya, Selangor', 'Jalan Kolam Air Lama, Ulu Kelang, Ampang Jaya Municipal Council, Gombak, Selangor, Malaysia'),
}

QUERY = {
    'kl-0d48d9041b4d': '121 Jalan Ampang, 50450 Kuala Lumpur',
    'kl-847775bf825b': '6 Jalan Stesen Sentral 2, 50470 Kuala Lumpur',
    'kl-da30b023d91a': '20 Jalan Dutamas 2, 50480 Kuala Lumpur',
    'kl-a72a6c5f539d': '6 Jalan Kia Peng, 50450 Kuala Lumpur',
    'kl-1501b357e078': 'World Trade Centre Kuala Lumpur, 41 Jalan Tun Ismail',
    'kl-496b88997888': '7 Jalan Kia Peng, 50450 Kuala Lumpur',
    'kl-7dcb2f4ad570': 'GMBB, 2 Jalan Robertson, 50150 Kuala Lumpur',
    'kl-1e5cf3e49cb1': 'Publika, Solaris Dutamas, Kuala Lumpur',
    'kl-e67bf1a8718b': 'Sunway Putra Mall, 100 Jalan Putra, 50350 Kuala Lumpur',
    'kl-d86dffabc235': 'Malaysia International Trade and Exhibition Centre Kuala Lumpur',
    'kl-06d6f98467c0': 'Shangri-La Kuala Lumpur',
    'kl-451839c5383d': 'Traders Hotel Kuala Lumpur',
    'kl-0c62e94089f8': 'MATRADE Exhibition and Convention Centre',
    'kl-6521a5218690': '198 Jalan Bukit Bintang, 55100 Kuala Lumpur',
    'kl-b32ee88b3dc6': 'Menara Darussalam, 12 Jalan Pinang, 50450 Kuala Lumpur',
    'kl-aadb1df3eba1': 'GTower, Jalan Tun Razak, 50450 Kuala Lumpur',
    'kl-cfd935e61947': 'Connexion Conference & Event Centre, Bangsar South',
    'kl-8cd52f2406dc': 'APW Bangsar',
    'kl-977b423768cd': 'DOJO Coworking Kuala Lumpur',
    'kl-2758407243f1': 'Sunway Pyramid Convention Centre, Bandar Sunway, Selangor',
    'kl-f13a656c8b31': 'Mandarin Oriental Kuala Lumpur',
    'kl-81d962290b05': 'KLCC Convention Centre',
    'kl-de410ec2db9b': 'WeWork Kuala Lumpur',
    'kl-73ee37f91926': 'Kuala Lumpur Performing Arts Centre, Sentul',
    'kl-b375b5ac812b': 'KL Eco City, Kuala Lumpur',
    'kl-7d5505fb90ae': 'Mid Valley City, Kuala Lumpur',
    'kl-7dd2a97334c6': 'No.68, Kuala Lumpur-Seremban Expressway, Taman Bukit, 57100 Kuala Lumpur',
    'kl-ef79384c8cb6': 'Jalan Doraisamy, Kuala Lumpur',
    'kl-79df5ab85172': 'Jalan Kolam Air Lama, 68000 Ampang Jaya, Selangor',
}

MATCH_NOTE = {
    'kl-6521a5218690': 'The returned POI is another business at house number 198 Jalan Bukit Bintang, the number the operator prints for Menara Worldwide; the point is the building frontage, not the tower entrance.',
    'kl-b32ee88b3dc6': 'OSM returns the Grand Hyatt at 12 Jalan Pinang, the number the operator prints for Menara Darussalam; the tower itself has no OSM POI, so this is the shared address point.',
    'kl-1e5cf3e49cb1': 'The returned place is The Boulevard inside the Publika development; the operator prints Solaris Dutamas, No 1 Jalan Dutamas.',
    'kl-7dd2a97334c6': 'Only the expressway carriageway resolves; the operator prints No.68 at Taman Bukit, so the pin is the street, not the building.',
    'kl-ef79384c8cb6': 'The operator site is dead; the street is the one a 2016 Time Out Kuala Lumpur listing gives for The Co. at 50 Jalan Doraisamy (capture timeout-theco line 112). Nothing proves the outlet still operates.',
    'kl-de410ec2db9b': 'A directory record: OSM returns one WeWork in Kuala Lumpur (Medan Syed Putra Selatan) and the operator page is blocked, so the pin is that location, not a room.',
    'kl-b375b5ac812b': 'No OSM POI exists for Menara 2; the point is the KL Eco City development area the operator names.',
    'kl-bba8243f4e1d': 'No OSM POI exists for Menara 2; the point is the KL Eco City development area the operator names.',
    'kl-7d5505fb90ae': 'Centrepoint North has no OSM POI; the point is the Mid Valley City area the operator prints, not the tower.',
    'kl-2758407243f1': 'The convention centre has its own OSM POI inside Sunway Pyramid; Bandar Sunway is in Selangor, outside the Federal Territory.',
    'kl-79df5ab85172': 'Only the road resolves; the operator prints Lot 36904 on Jalan Kolam Air Lama, in Selangor.',
    'kl-06d6f98467c0': 'The operator page is behind a Cloudflare challenge; the building is located by name in OSM on Jalan Sultan Ismail.',
    'kl-451839c5383d': 'The operator page is behind a Cloudflare challenge; the building is located by name in OSM on Persiaran KLCC.',
    'kl-81d962290b05': 'The operator page prints no street address; the convention centre is located by name in OSM inside the KLCC precinct.',
    'kl-ce3f20a09b7e': 'The operator page prints no street address; the convention centre is located by name in OSM inside the KLCC precinct.',
    'kl-8cd52f2406dc': 'The venue site did not resolve; the venue is located by name in OSM on Jalan Riong.',
    'kl-977b423768cd': 'The venue site TLS failed; the venue is located by name in OSM on Jalan Puncak.',
    'kl-0c62e94089f8': 'The MECC path on matrade.gov.my returns 404 and mecc.matrade.gov.my did not resolve; the building is located by name in OSM.',
}

tiers = {}
for vid in store['venues']:
    tier, lat, lon, target, returned = COORD[vid]
    query = QUERY.get(vid) or None
    if query is None:
        # every other record shares a verified address query
        addr = ((store['venues'][vid]['fields'].get('address') or {}).get('value')) or ''
        query = addr or ('%s Kuala Lumpur' % store['venues'][vid]['name'])
    url = 'https://nominatim.openstreetmap.org/search?' + urlencode(
        {'q': query, 'format': 'jsonv2', 'limit': '4', 'addressdetails': '1',
         'accept-language': 'en'})
    note = MATCH_NOTE.get(vid)
    extra = {
        '_tag': tier,
        'provider': 'OpenStreetMap Nominatim',
        'query': query,
        'returned_place': returned,
        'checked_on': STAMP,
        'derived': True,
        'derived_from': 'address' if (store['venues'][vid]['fields'].get('address') or {}).get('value') else 'venue name',
        'match_evidence': 'Nominatim returned "%s" for the query; %s' % (
            returned, ('the road/number matches the operator-printed address' if tier != 'area'
                       else 'the named district matches the operator-printed location')),
    }
    if note:
        extra['note'] = note
    put(vid, 'coordinates', claim(
        vid, 'coordinates',
        {'latitude': lat, 'longitude': lon, 'precision': tier, 'map_target': target},
        extra=extra, quote=returned, url=url,
        title='Nominatim (OpenStreetMap) forward geocode',
        locator='Nominatim response checked %s' % STAMP))
    tiers[vid] = tier

print('coordinates written', len(tiers), {t: list(tiers.values()).count(t) for t in set(tiers.values())})

# -------------------------------------------------------------------- address
plan = json.loads((R3 / 'address-plan.json').read_text())['venues']
changed_addr = 0
for vid, entry in plan.items():
    if not entry.get('address') or not entry.get('lines'):
        continue
    lines = entry['lines']
    text = q(entry['slug'], lines[0], lines[-1])
    put(vid, 'address', claim(
        vid, 'address', entry['address'], slug=entry['slug'], lines=lines,
        quote=text, extra={'_tag': 'addr'},
        title=None, url=None))
    changed_addr += 1
print('address claims refreshed', changed_addr)

# --------------------------------------------------------------------- photos
def assign_view_kind(row):
    """Let the recorded room decide the view; never default a view to `interior`.

    A row that came from an operator page already carries the `view_kind` its
    page proves. A legacy row records `room`: `building` means the photograph is
    of the building itself, so it is an exterior, and a named room means an
    interior. A row with neither stays without a view rather than guessing one.
    """
    if row.get('view_kind'):
        return
    room = row.get('room')
    if room == 'building':
        row['view_kind'] = 'exterior'
    elif room in (None, '', 'none'):
        if row.get('withheld'):
            row['view_kind'] = 'render'
        else:
            row.pop('view_kind', None)
    else:
        row['view_kind'] = 'interior'


photo_records = json.loads((R3 / 'photo-records.json').read_text())
photo_fail = [u for u, r in [] ]
for vid, rows in photo_records.items():
    keep = []
    for row in rows:
        if not str((row.get('verified') or {}).get('status', '')).startswith('2'):
            continue
        keep.append(row)
    if not keep:
        continue
    existing = [p for p in store['photos'].get(vid, [])
                if p.get('withheld') is not True and p.get('url')]
    merged = existing + keep
    for i, row in enumerate(merged):
        row['index'] = i
        assign_view_kind(row)
    store['photos'][vid] = merged

for vid, rows in store['photos'].items():
    for row in rows:
        assign_view_kind(row)

# ---------------------------------------------------------------- access rows
WINDOW = {
    'worq': ('yes', 'The event-space FAQ publishes booking from 8 am to 10 pm daily, which contains 09:00-21:00; closing 22:00.', 'worq-events', [101]),
    'wtc': ('unknown', 'The only clock on the page is the contact line 9.00 am-6.00 pm (Mon-Fri), an office-hours statement, not a hire interval.', 'wtckl', [110]),
    'wspace': ('unknown', 'The only clock is the branches\u2019 business hours, Monday through Friday from 9:00am to 6:00pm, not an event interval; the FAQ adds a three-hour minimum for non-office hours.', 'wspace-contact', [41, 42]),
    'publika': ('unknown', 'The only clock is the gallery\u2019s opening hours, Monday-Sunday 10:00am-10:00pm, not an event-hire interval.', 'publika', [24, 25]),
    'spcc': ('unknown', 'The mall page prints shopping hours only; no convention-centre hire interval is published.', 'sp-mall', [349]),
    'connexion': ('unknown', 'The centre prints room names and layouts but no daily hire interval; the only clocks are a specific August event\u2019s opening times.', 'connexion', [230]),
    'gmbb': ('unknown', 'The contact page prints office hours only; no event-space hire interval.', 'gmbb-contact', [26]),
    'colony': ('unknown', 'The event-space page and location pages print capacities, starting rates and a booking form, and no event start or end clock.', 'colony-events', [38]),
    'w': ('unknown', 'The events page prints the capacity chart and a gallery; no event start or end clock.', 'w-events', [216]),
    'stregis': ('unknown', 'The events page prints the capacity chart; no event start or end clock.', 'stregis-events', [1575]),
    'cg': ('unknown', 'The location page prints the event-space pax and address; no hire interval.', 'cg-klcc', [112]),
    'klpac': ('unknown', 'The venue-hire page prints seat counts, layouts and rates; no daily hire interval.', 'klpac-venue', [107]),
    'mitec': ('unknown', 'The venue page prints levels and floor plans; no daily hire interval.', 'mitec-venues', [116]),
    'default': ('unknown', 'The operator page prints no event start or end clock, and no hire pack or FAQ with an interval was published on the pages read.', None, None),
}
OP = {
    'colony': 'colony',
    'w': 'w', 'stregis': 'stregis',
    'worq': 'worq', 'wspace': 'wspace', 'klpac': 'klpac', 'mitec': 'mitec',
    'cg': 'cg', 'wtc': 'wtc', 'publika': 'publika', 'spcc': 'spcc',
    'connexion': 'connexion', 'gmbb': 'gmbb',
}


def operator_of(vid, name):
    n = name.lower()
    if n.startswith('colony'):
        return 'colony'
    if n.startswith('w kuala lumpur'):
        return 'w'
    if n.startswith('the st. regis'):
        return 'stregis'
    if n.startswith('common ground'):
        return 'cg'
    if n.startswith('worq'):
        return 'worq'
    if n.startswith('wspace'):
        return 'wspace'
    if n.startswith('klpac'):
        return 'klpac'
    if n.startswith('mitec'):
        return 'mitec'
    if n.startswith('world trade centre'):
        return 'wtc'
    if n.startswith('publika') or n.startswith('the bee'):
        return 'publika'
    if n.startswith('sunway pyramid'):
        return 'spcc'
    if n.startswith('connexion'):
        return 'connexion'
    if n.startswith('gmbb'):
        return 'gmbb'
    return 'default'


for vid, venue in store['venues'].items():
    op = operator_of(vid, venue['name'])
    state, basis, slug, lines = WINDOW[op]
    extra = {'_tag': op}
    if slug and lines:
        text = q(slug, lines[0], lines[-1])
        locator = 'capture %s lines %s' % (slug, lines[0] if len(lines) == 1 else '%s-%s' % (lines[0], lines[-1]))
        url, title = src(slug)
    else:
        own = (venue['fields'].get('source_url') or {})
        url, title = own.get('value'), own.get('source_title')
        text = None
        locator = 'absence on the pages read %s 2026-11-26: no clock printed' % url
    if op == 'worq':
        put(vid, 'programme_windows', claim(
            vid, 'programme_windows',
            {'8': {'state': 'yes', 'basis': 'The published bookable day runs 8 am to 10 pm daily, which contains 09:00-17:00.'},
             '12': {'state': 'yes', 'basis': 'The published bookable day runs 8 am to 10 pm daily, which contains 09:00-21:00; closing 22:00.'}},
            extra=extra, quote=text, locator=locator, url=url, title=title))
    else:
        put(vid, 'programme_windows', claim(
            vid, 'programme_windows',
            {'8': {'state': 'unknown', 'basis': basis},
             '12': {'state': 'unknown', 'basis': basis}},
            extra=extra, quote=text, locator=locator, url=url, title=title))
        put(vid, 'access_window', claim(
            vid, 'access_window', None, extra=extra, quote=text, locator=locator,
            url=url, title=title))

# -------------------------------------------------------------------- holidays
ocr = (R3 / 'pdf' / 'KPM_ocr.txt').read_text(encoding='utf-8')
(R3 / 'captures' / 'kpm-kalendar-2027-ocr.txt').write_text(ocr, encoding='utf-8')
kpm_url = 'https://www.moe.gov.my/storage/files/shares/pekeliling_dan_garis_panduan/surat_siaran/SS%20KPM%20Bil.%201%20Tahun%202026%20-%20Kalendar%20Akademik%20Tahun%202027.pdf'
kpm_title = 'Surat Siaran KPM Bil. 1 Tahun 2026 - Kalendar Akademik Tahun 2027'
loc = cap_lines('kpm-kalendar-2027-ocr')


def ocr_line(needle, start=0):
    for i in range(start, len(loc)):
        if needle in loc[i]:
            return i + 1
    return None


def sch(name, start, end, quote, line, note=''):
    return {
        'holiday_name': name, 'jurisdiction_id': 'MY-14', 'kind': 'school_holiday',
        'start_date': start, 'end_date': end, 'accessed_on': STAMP,
        'needs_human_verify': False,
        'source_edition': 'Kalendar Akademik Tahun 2027, Kumpulan B (KPM Surat Siaran Bil. 1/2026)',
        'source_title': kpm_title, 'source_url': kpm_url,
        'source_locator': 'Lampiran B / Lampiran C, line %d of the OCR capture' % line,
        'quote': quote,
        'evidence': {'observed_facts': quote.replace('\n', ' ')[:400],
                     'note': note or 'Kumpulan B names Wilayah Persekutuan Kuala Lumpur among its states and territories.'},
        'verification_questions': [],
    }


school_rows = [
    sch('Cuti Penggal 1 (Kumpulan B)', '2027-03-06', '2027-03-14',
        'CUTIPENGGAL1,TAHUN2027 1 06.03.2027-14.03.2027 9', 200),
    sch('Cuti Pertengahan Tahun (Kumpulan B)', '2027-05-22', '2027-06-06',
        'CUTIPERTENGAHANTAHUN2027 2 22.05.2027-06.06.2027 16', 216),
    sch('Cuti Penggal 2 (Kumpulan B)', '2027-08-28', '2027-09-05',
        'CUTIPENGGAL2,TAHUN2027 1 28.08.2027-05.09.2027 9', 233),
    sch('Cuti Akhir Persekolahan (Kumpulan B)', '2027-12-04', '2027-12-31',
        'CUTIAKHIRPERSEKOLAHANTAHUN2027 4 04.12.2027 31.12.2027 28', 252),
]
extra_days = {
    '2027-02-05': '05.02.2027 (Jumaat)',
    '2027-02-09': '09.02.2027 (Selasa)',
    '2027-02-10': '10.02.2027 (Rabu)',
    '2027-02-11': '11.02.2027 (Khamis)',
    '2027-02-12': '12.02.2027 (Jumaat)',
    '2027-05-18': '18.05.2027 (Selasa)',
    '2027-05-19': '19.05.2027 (Rabu)',
    '2027-05-21': '21.05.2027 (Jumaat)',
    '2027-10-27': '27.10.2027 (Rabu)',
    '2027-10-29': '29.10.2027 (Jumaat)',
}
names = {
    '2027-02-05': 'Cuti Tambahan KPM Tahun Baharu Cina (Kumpulan B)',
    '2027-02-09': 'Cuti Tambahan KPM Tahun Baharu Cina (Kumpulan B)',
    '2027-02-10': 'Cuti Tambahan KPM Tahun Baharu Cina (Kumpulan B)',
    '2027-02-11': 'Cuti Tambahan KPM Tahun Baharu Cina (Kumpulan B)',
    '2027-02-12': 'Cuti Tambahan KPM Tahun Baharu Cina (Kumpulan B)',
    '2027-05-18': 'Cuti Tambahan KPM Hari Raya Korban (Kumpulan B)',
    '2027-05-19': 'Cuti Tambahan KPM Hari Raya Korban (Kumpulan B)',
    '2027-05-21': 'Cuti Tambahan KPM Hari Wesak (Kumpulan B)',
    '2027-10-27': 'Cuti Tambahan KPM Deepavali (Kumpulan B)',
    '2027-10-29': 'Cuti Tambahan KPM Deepavali (Kumpulan B)',
}
for day, text in extra_days.items():
    line = ocr_line(text)
    school_rows.append(sch(names[day], day, day, text, line,
                           note='Lampiran C lists this date in the Kumpulan B column.'))

store['holidays'] = list(store['holidays']) + school_rows
for row in store['holidays']:
    y, m, d = (int(x) for x in row['start_date'].split('-'))
    row['weekday'] = date(y, m, d).strftime('%A')

print('holiday rows', len(store['holidays']), 'school', len(school_rows))

# ---------------------------------------------------------------------- events
def ev_field(eid, field, value, slug=None, lines=None, quote=None, locator=None):
    """One event field, carrying its own line and quote (one claim per fact)."""
    row = {'claim_id': cid(eid, field), 'run_id': RUN, 'verified_at': STAMP,
           'value': value}
    if slug:
        url, title = src(slug)
        row['source_url'], row['source_title'] = url, title
    if slug and lines:
        row['source_locator'] = 'capture %s line%s %s' % (
            slug, '' if len(lines) == 1 else 's',
            lines[0] if len(lines) == 1 else '%s-%s' % (lines[0], lines[-1]))
        row['quote'] = quote if quote is not None else q(slug, lines[0], lines[-1])
    if locator:
        row['source_locator'] = locator
    return row


def event(eid, name, slug, fields, observed, note=''):
    url, title = src(slug)
    return {'city_slug': store['city_slug'], 'event_id': eid, 'name': name,
            'fields': fields, 'history': {},
            'evidence': [{'observed_facts': observed, 'run_id': RUN, 'verified_at': STAMP,
                          'source_url': url, 'source_title': title,
                          'inference': note or None}]}


gaicc = 'kl-ev-0f2a91c4d7b3'
store['events'][gaicc] = event(
    gaicc, 'GAICC AI Governance Conference Malaysia 2027', 'eb-gaicc',
    {
        'date_range': ev_field(gaicc, 'date_range',
                               {'start': '2027-01-24', 'end': '2027-01-24'},
                               'eb-gaicc', [134], q('eb-gaicc', 134)),
        'kind': ev_field(gaicc, 'kind', 'conference', 'eb-gaicc', [104],
                         q('eb-gaicc', 104)),
        'relevance': ev_field(gaicc, 'relevance', 'ai', 'eb-gaicc', [100],
                              q('eb-gaicc', 100)),
        'organiser': ev_field(
            gaicc, 'organiser',
            'Global AI Certification Council (GAICC); Malaysia partner Global Master '
            'Training & Consultancy Sdn. Bhd.', 'eb-gaicc', [104], q('eb-gaicc', 104)),
        'venue': ev_field(gaicc, 'venue',
                          'The Majestic Hotel Kuala Lumpur, Autograph Collection',
                          'eb-gaicc', [96], q('eb-gaicc', 96)),
        'status': ev_field(
            gaicc, 'status', None,
            locator='absence on %s checked 2026-11-26: no status word is printed'
                    % src('eb-gaicc')[0]),
        'conflict_severity': ev_field(gaicc, 'conflict_severity', 'low',
                                      'eb-gaicc', [97], q('eb-gaicc', 97)),
    },
    'Date:Sunday, 24 January 2027 / Time:9:00 AM \u2013 5:00 PM (MYT) / '
    'Venue:The Majestic Hotel Kuala Lumpur, Malaysia / '
    'ByGlobal Master Training & Consultancy Sdn Bhd / one-day professional conference '
    'organised by the Global AI Certification Council (GAICC), with Global Master '
    'Training & Consultancy Sdn. Bhd. as the Malaysia Partner.',
    'Two blocks on the page print the same date (lines 97 and 134), so the conflict '
    'severity is low. The page prints no status word, so status is left unrecorded.')

bg = 'kl-ev-7c41b0e2a9d5'
store['events'][bg] = event(
    bg, 'Business Growth, AI & Digital Transformation Summit 2027', 'eb-bizgrowth',
    {
        'date_range': ev_field(bg, 'date_range',
                               {'start': '2027-07-15', 'end': '2027-07-15'},
                               'eb-bizgrowth', [95], q('eb-bizgrowth', 95)),
        'kind': ev_field(bg, 'kind', 'conference', 'eb-bizgrowth', [97],
                         q('eb-bizgrowth', 97)),
        'relevance': ev_field(bg, 'relevance', 'ai', 'eb-bizgrowth', [93],
                              q('eb-bizgrowth', 93)),
        'organiser': ev_field(
            bg, 'organiser', None,
            locator='absence on %s checked 2026-11-26: no organiser is named; '
                    'the only organiser text is the footer link "Contact your event organizer"'
                    % src('eb-bizgrowth')[0]),
        'venue': ev_field(bg, 'venue',
                          'Jalan Bukit Bintang, Kuala Lumpur 55100 (no venue name printed)',
                          'eb-bizgrowth', [121, 122]),
        'status': ev_field(
            bg, 'status', None,
            locator='absence on %s checked 2026-11-26: no status word is printed'
                    % src('eb-bizgrowth')[0]),
        'conflict_severity': ev_field(bg, 'conflict_severity', 'low',
                                      'eb-bizgrowth', [95], q('eb-bizgrowth', 95)),
    },
    q('eb-bizgrowth', 93) + ' / ' + q('eb-bizgrowth', 95) + ' / '
    + q('eb-bizgrowth', 121, 122),
    'The page names a one-day Summit, so it is stored in the conference lane, and it '
    'prints a nine-hour 9 AM-6 PM block. It prints no organiser and no status word, so '
    'both are left unrecorded; one page prints this date and no second source disagreed, '
    'so the conflict severity is low.')

print('events', len(store['events']))
STORE.write_text(json.dumps(store, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('wrote', STORE, len(STORE.read_bytes()))
json.dump({'tiers': tiers}, open(R3 / 'coordinate-tiers.json', 'w'), indent=1)
