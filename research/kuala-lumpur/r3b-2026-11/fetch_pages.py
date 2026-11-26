#!/usr/bin/env python3
"""Fetch operator pages for the KL R3b photo pass and save raw HTML."""
import subprocess, sys, json, re
from pathlib import Path

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
HTML = BASE / "pages"
HTML.mkdir(parents=True, exist_ok=True)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/158.0.0.0 Safari/537.36")

PAGES = [
    ("colony-event-space", "https://colony.work/event-space/"),
    ("cg-klcc", "https://commonground.work/malaysia/klcc"),
    ("cg-kl-eco-city", "https://commonground.work/malaysia/kl-eco-city"),
    ("cg-ampang", "https://commonground.work/malaysia/ampang"),
    ("mitec-venues", "https://mitec.com.my/organise/venues"),
    ("klcc-floorplan", "https://www.klccconventioncentre.com/organisers/plan-an-event/floor-plan"),
    ("klcc-venues", "https://www.klccconventioncentre.com/venues"),
    ("connexioncec", "https://connexioncec.com/"),
    ("worq-event-space", "https://worq.space/event-space/"),
    ("wspace-event-space", "https://wspace.com/membership/event-space/"),
    ("sunway-pcc", "https://www.sunwaypyramidconventioncentre.com/"),
    ("wtc-kl", "https://www.wtckl.com/"),
    ("apw-bangsar", "https://apwbangsar.com/"),
    ("gmbb", "https://gmbb.com.my/"),
    ("dojo-event-meeting", "https://workspacedojo.com/event-meeting"),
    ("thebee", "https://www.thebee.com.my/"),
    ("theco", "https://www.theco.my/"),
    ("ruma-events", "https://www.theruma.com/events"),
    ("matrade-mecc", "https://www.matrade.gov.my/en/about-matrade/mecc"),
    ("publika", "https://www.publika.com.my/"),
    ("wework-kl-event", "https://www.wework.com/en-MY/l/event-space/kuala-lumpur--MY"),
    ("mo-meetings", "https://www.mandarinoriental.com/en/kuala-lumpur/klcc/meetings-and-events"),
    ("shangrila-meeting-rooms", "https://www.shangri-la.com/kualalumpur/shangrila/meetings-events/meeting-rooms/"),
    ("traders-meeting-rooms", "https://www.shangri-la.com/kualalumpur/traders/meetings-events/meeting-rooms/"),
    ("marriott-stregis-events", "https://www.marriott.com/en-us/hotels/kulxr-the-st-regis-kuala-lumpur/events/"),
    ("marriott-w-events", "https://www.marriott.com/en-us/hotels/kulwh-w-kuala-lumpur/events/"),
    ("wtc-dewan-merdeka", "https://worldtradecentrekl.com/venue/dewan-merdeka/"),
    ("wtc-hall-1", "https://worldtradecentrekl.com/venue/hall-1/"),
    ("wtc-venues", "https://worldtradecentrekl.com/venues/"),
    ("wtc-gallery", "https://worldtradecentrekl.com/gallery/"),
    ("mitec-gallery", "https://mitec.com.my/medias/photo-gallery"),
    ("connexion-venue", "https://connexioncec.com/our-venue/"),
    ("connexion-floorplan", "https://connexioncec.com/capacity-and-floor-plan/"),
    ("colony-mont-kiara", "https://colony.work/mont-kiara-coworking-and-event-space/"),
    ("colony-klcc", "https://colony.work/klcc/"),
    ("colony-eco-city", "https://colony.work/kl-eco-city/"),
    ("gmbb-shared-space", "https://gmbb.com.my/directory/shared-space/"),
    ("gmbb-gallery", "https://gmbb.com.my/gallery/"),
    ("worq-event-hall-pricing", "https://worq.space/event-hall-pricing/"),
    ("worq-sunway-putra", "https://worq.space/location/sunway-putra/"),
    ("wspace-location", "https://wspace.com/location/"),
    ("publika-events", "https://www.publika.com.my/events"),
    ("dojo-event-plan", "https://workspacedojo.com/event-meeting-plan/"),
    ("wspace-mid-valley", "https://wspace.com/wspace-mid-valley/"),
    ("wspace-gtower", "https://wspace.com/wspace-gtower/"),
    ("klcc-360", "https://www.klccconventioncentre.com/organisers/plan-an-event/360-gallery"),
    ("mo-meet", "https://www.mandarinoriental.com/en/kuala-lumpur/petronas-towers/meet"),
]

def fetch(slug, url):
    out = HTML / (slug + ".html")
    proc = subprocess.run(
        ["curl", "-sS", "-k", "-L", "--compressed", "--http1.1", "-m", "60", "-A", UA,
         "-H", "Accept-Language: en-US,en;q=0.9",
         "-o", str(out), "-w", "%{http_code} %{content_type} %{size_download} %{url_effective}",
         url], capture_output=True, text=True, timeout=90)
    meta = (proc.stdout or proc.stderr).strip()
    title = ""
    try:
        raw = out.read_text(errors="replace")
        m = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S | re.I)
        title = re.sub(r"\s+", " ", m.group(1)).strip()[:90] if m else ""
    except Exception:
        pass
    print(f"{slug:28s} {meta}\n    title={title!r}")
    return meta

if __name__ == "__main__":
    only = sys.argv[1:]
    for slug, url in PAGES:
        if only and slug not in only:
            continue
        try:
            fetch(slug, url)
        except Exception as exc:
            print(f"{slug:28s} ERROR {exc}")
