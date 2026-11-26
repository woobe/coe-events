"""R9: mine the saved event-lane captures for 2027 New York leads."""
import re, json, html
from pathlib import Path

CAP = Path('/home/joe/repo_dev/coe-events/research/new-york/city/captures')
OUT = {}

# --- MiraGather: event objects in the Next.js payload ------------------------
mira = []
for name in ('lane-miragather-main', 'lane-miragather-side', 'lane-miragather-ai'):
    raw = (CAP / (name + '.html')).read_text(errors='ignore')
    for m in re.finditer(r'\{"id":"rec[^"]+","description":.*?"promoStatus":\[\]\}', raw):
        blob = m.group(0)
        try:
            obj = json.loads(blob)
        except Exception:
            continue
        start = str(obj.get('startDate') or '')
        cities = obj.get('city') or []
        if '2027' not in start:
            continue
        if not any('new york' in str(c).lower() for c in cities):
            continue
        mira.append({'page': name, 'event': obj.get('event'), 'start': start,
                     'end': obj.get('endDate'), 'city': cities,
                     'country': obj.get('country'), 'slug': obj.get('slug'),
                     'url': 'https://miragather.com/e/' + str(obj.get('shortSlug') or obj.get('slug'))})
OUT['miragather'] = mira

# --- Meetup: schema.org Event blocks ---------------------------------------
meetup = []
for name in [p.stem for p in CAP.glob('lane-meetup-*.html')]:
    raw = (CAP / (name + '.html')).read_text(errors='ignore')
    for m in re.finditer(r'"@type":"Event".{0,2500}?"startDate":"([^"]+)"', raw, re.S):
        block = m.group(0)
        start = m.group(1)
        if '2027' not in start:
            continue
        nm = re.search(r'"name":"([^"]+)"', block)
        url = re.search(r'"url":"([^"]+)"', block)
        meetup.append({'lane': name, 'name': nm.group(1) if nm else None,
                       'start': start, 'url': url.group(1) if url else None})
OUT['meetup'] = meetup

# --- Eventbrite: schema.org Event blocks -----------------------------------
eb = []
for name in [p.stem for p in CAP.glob('lane-eventbrite-*.html')]:
    raw = (CAP / (name + '.html')).read_text(errors='ignore')
    for m in re.finditer(r'"@type"\s*:\s*"Event".{0,3000}?"startDate"\s*:\s*"([^"]+)"', raw, re.S):
        block = m.group(0)
        start = m.group(1)
        if '2027' not in start:
            continue
        nm = re.search(r'"name"\s*:\s*"([^"]+)"', block)
        url = re.search(r'"url"\s*:\s*"([^"]+)"', block)
        loc = re.search(r'"addressLocality"\s*:\s*"([^"]*)"', block)
        eb.append({'lane': name, 'name': html.unescape(nm.group(1)) if nm else None,
                   'start': start, 'url': url.group(1) if url else None,
                   'locality': loc.group(1) if loc else None})
OUT['eventbrite'] = eb

# --- Luma: any embedded event dates ---------------------------------------
luma = []
for name in [p.stem for p in CAP.glob('lane-luma-*.html')]:
    raw = (CAP / (name + '.html')).read_text(errors='ignore')
    hits = sorted(set(re.findall(r'20\d\d-\d\d-\d\dT[0-9:+\-]+', raw)))
    luma.append({'lane': name, 'dates': hits[:10], 'has_2027': '2027' in raw})
OUT['luma'] = luma

(CAP.parent / 'lane-mine.json').write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
print('miragather 2027 NYC:', len(mira))
for r in mira:
    print(' ', r['start'], r['event'], r['city'], r['url'])
print('\nmeetup 2027:', len(meetup))
for r in meetup[:25]:
    print(' ', r['start'], r['name'], r['url'])
print('\neventbrite 2027:', len(eb))
for r in eb[:25]:
    print(' ', r['start'], r['name'], r['locality'], r['url'])
print('\nluma:', luma)
