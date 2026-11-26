#!/usr/bin/env python3
"""List internal links per saved page so we can find room-detail subpages."""
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
import lxml.html
from fetch_pages import PAGES

URLMAP = dict(PAGES)

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
HTML = BASE / "pages"

SLUGS = sys.argv[1:] or sorted(p.stem for p in HTML.glob("*.html"))
for slug in SLUGS:
    path = HTML / (slug + ".html")
    if not path.exists():
        continue
    doc = lxml.html.fromstring(path.read_text(errors="replace"))
    base = URLMAP.get(slug, "https://example.invalid/")
    print(f"\n## {slug}")
    seen = set()
    for a in doc.iter("a"):
        href = a.get("href") or ""
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        full = urljoin(base, href)
        host = urlparse(full).netloc
        if not host:
            continue
        label = " ".join(a.text_content().split())[:70]
        key = (host, urlparse(full).path)
        if key in seen:
            continue
        seen.add(key)
        print(f"  {host}{urlparse(full).path}  | {label}")
