"""Audit every nonempty city.json quote against its URL-linked local capture.

Run with .venv/bin/python -B <city dir>/audit-r9-quotes.py from hermes-skills.
Outputs JSON on stdout. Historical misses are not treated as current quotes.
"""
from collections import Counter, defaultdict
from functools import cache
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

CITY = Path(__file__).resolve().parent
CAP = CITY / 'captures'


def load(path):
    return json.loads((CITY / path).read_bytes())


def url_key(url):
    parts = urlsplit(url)
    return parts.netloc, parts.path.rstrip('/'), tuple(sorted(parse_qsl(parts.query)))


def quotes(obj, path: tuple[str | int, ...] = ()):
    if isinstance(obj, dict):
        if obj.get('quote'):
            yield path, obj
        for key, child in obj.items():
            yield from quotes(child, (*path, key))
    elif isinstance(obj, list):
        for i, child in enumerate(obj):
            yield from quotes(child, (*path, i))


def normalize(text):
    return ' '.join(text.split())


@cache
def normalized(path):
    return normalize(path.read_text(encoding='utf-8', errors='replace'))


def audit():
    store = load('city.json')
    venues = load('venue-fetch-report.json')
    events = load('event-fetch-report.json')
    sources = defaultdict(list)

    def add(section, record, url, *paths):
        sources[section, record, url_key(url)].extend(paths)

    for vid, rows in venues.items():
        for row in rows:
            add('venues', vid, row['url'], *(CAP / row[k] for k in ('text', 'capture') if row.get(k)))
    for vid, row in load('geocode-log.json').items():
        for lookup in row['lookups'].values():
            if lookup.get('url'):
                add('venues', vid, lookup['url'], CITY / 'geocode' / f'{vid}.json')
    civic = 'nyc-4c6638c43df6'
    add('venues', civic, 'https://civichall.org/contact-us',
        CAP / 'rev1-civic-hall-contact.txt', CAP / 'rev1-civic-hall-contact.html')
    coord = store['venues'][civic]['fields']['coordinates']
    add('venues', civic, coord['request_url'], CITY / 'geocode' / f'{civic}-124e14.json')
    for eid, row in events.items():
        if row.get('url'):
            add('events', eid, row['url'], CAP / f'event-{eid}.txt', CAP / f'event-{eid}.html')
    add('events', 'nyc-ev-agntsummit2027', 'https://events.linuxfoundation.org/agntsummit-new-york-city/',
        CAP / 'event-nyc-ev-agntsummit2027-lf.html')
    add('events', 'nyc-ev-ethconf2027', 'https://ethglobal.com/events',
        CAP / 'event-nyc-ev-432d4f5d6f60.txt', CAP / 'event-nyc-ev-432d4f5d6f60.html')
    add('events', 'nyc-ev-daoscon7-2027', 'https://www.eventbrite.com/e/daos-con-7-tickets-1994392414399',
        CAP / 'event-candidate-daos.html')
    add('events', 'nyc-ev-bts-20270928', 'https://www.eventbrite.com/e/blockchain-tech-summit-4th-annual-tickets-1990305841349',
        CAP / 'event-candidate-bts.html')

    checked, matched = Counter(), Counter()
    matches, unresolved = [], []
    for path, claim in quotes(store):
        assert len(path) >= 2, path
        section, rid = path[:2]
        bucket = f'{section}.{path[2]}' if section in ('venues', 'events') else section
        checked[bucket] += 1
        candidates = sources[section, rid, url_key(claim['source_url'])]
        # A file-and-lines locator is binding, not just a hint.
        locator = claim.get('source_locator') or ''
        explicit_path, _, line_spec = locator.partition(':')
        if explicit_path.startswith('captures/') and line_spec:
            candidates = [p for p in candidates if p == CITY / explicit_path]
        existing = [p for p in dict.fromkeys(candidates) if p.is_file()]
        q = normalize(claim['quote'])
        hit = next((p for p in existing if q in normalized(p)), None)
        row = {'path': '.'.join(map(str, path)), 'claim_id': claim.get('claim_id'),
               'source_url': claim['source_url'], 'verified_at': claim.get('verified_at')}
        if hit:
            if explicit_path.startswith('captures/') and line_spec:
                line_range = line_spec.split()[0]
                start, _, end = line_range.partition('–')
                assert q in normalize('\n'.join(hit.read_text().splitlines()[int(start)-1:int(end or start)])), row
            matched[bucket] += 1
            matches.append({**row, 'capture': str(hit.relative_to(CITY))})
        else:
            unresolved.append({**row, 'quote': claim['quote'], 'locator': locator or None,
                               'captures_searched': [str(p.relative_to(CITY)) for p in existing],
                               'disposition': ('Legacy blocked-probe diagnostic, not a policy quote; no raw request log retained.'
                                               if section == 'local_requirements' else
                                               'Legacy history preserved; not verified as a verbatim capture quote.'
                                               if bucket == 'venues.history' else 'Current claim: investigate.')})
    return {
        'checked_on': '2026-11-26',
        'store_sha256': hashlib.sha256((CITY / 'city.json').read_bytes()).hexdigest(),
        'method': 'Recursively enumerate all nonempty quote entries, counting current and historical occurrences separately. Search the record-and-URL-linked raw captures and text extracts for a contiguous substring after collapsing whitespace only; no global cross-record quote matching. Negatives cannot establish what appeared on the earlier live page.',
        'counts': {k: {'checked': n, 'matched': matched[k], 'unresolved': n-matched[k]} for k,n in checked.items()},
        'total': {'checked': checked.total(), 'matched': matched.total(), 'unresolved': len(unresolved)},
        'matches': matches,
        'unresolved': unresolved,
    }


if __name__ == '__main__':
    result = audit()
    print(json.dumps(result, indent=1, ensure_ascii=False))
    assert all(not row['disposition'].startswith('Current claim') for row in result['unresolved']), 'Current quote failed'
