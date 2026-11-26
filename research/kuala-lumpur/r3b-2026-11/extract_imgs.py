#!/usr/bin/env python3
"""Inventory images on each saved operator page with the context that labels them."""
import json, re, sys
from pathlib import Path
import lxml.html

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
HTML = BASE / "pages"
OUT = BASE / (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].endswith(".txt") else "image-inventory.txt")


def _slugs():
    args = sys.argv[1:]
    if args and args[0].endswith(".txt"):
        args = args[1:]
    return args or sorted(p.stem for p in HTML.glob("*.html"))

IMG_EXT = re.compile(r"\.(?:jpe?g|png|webp|avif)(?:\?|$)", re.I)


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def text_of(el, limit=120):
    try:
        return norm(el.text_content())[:limit]
    except Exception:
        return ""


def walk(doc):
    """Yield (element, heading, section_label) in document order."""
    heading = ""
    section_label = ""
    for el in doc.iter():
        tag = el.tag if isinstance(el.tag, str) else ""
        if tag in ("h1", "h2", "h3", "h4"):
            heading = text_of(el, 100)
        if tag in ("section", "div"):
            ident = " ".join(filter(None, [el.get("id"), el.get("class")]))
            if ident and len(ident) < 120:
                section_label = ident
        yield el, heading, section_label


def main(slugs):
    lines = []
    for slug in slugs:
        path = HTML / (slug + ".html")
        if not path.exists():
            continue
        raw = path.read_text(errors="replace")
        try:
            doc = lxml.html.fromstring(raw)
        except Exception as exc:
            lines.append(f"### {slug}: PARSE ERROR {exc}")
            continue
        title = doc.findtext(".//title") or ""
        lines.append(f"\n## {slug}  title={norm(title)[:100]}")
        seen = set()
        n = 0
        for el, heading, sect in walk(doc):
            tag = el.tag if isinstance(el.tag, str) else ""
            src = None
            if tag == "img":
                src = (el.get("src") or el.get("data-src") or el.get("data-lazy-src")
                       or el.get("data-original") or "")
                if not src or src.startswith("data:"):
                    ss = el.get("srcset") or el.get("data-srcset") or ""
                    if ss:
                        src = ss.split(",")[0].strip().split(" ")[0]
            elif tag == "source":
                ss = el.get("srcset") or el.get("data-srcset") or ""
                if ss:
                    src = ss.split(",")[0].strip().split(" ")[0]
            if not src or not IMG_EXT.search(src):
                continue
            key = src
            if key in seen:
                continue
            seen.add(key)
            n += 1
            alt = norm(el.get("alt"))
            cap = ""
            parent = el.getparent()
            hops = 0
            while parent is not None and hops < 5:
                if parent.tag == "figure":
                    fc = parent.find("figcaption")
                    if fc is not None:
                        cap = text_of(fc)
                    break
                parent = parent.getparent()
                hops += 1
            lines.append(
                f"- src={src}\n  alt={alt!r} cap={cap!r}\n  heading={heading!r} sect={sect[:70]!r}")
        njson = 0
        for m in re.finditer(r"https?://[^\"'\\s<>]+?\.(?:jpe?g|png|webp)(?:\?[^\"'\\s<>]*)?", raw):
            u = m.group(0).replace("\\/", "/")
            if u in seen:
                continue
            seen.add(u)
            njson += 1
            if njson <= 40:
                ctx = norm(raw[max(0, m.start() - 90):m.start()])[-90:]
                lines.append(f"* raw-url={u}\n  ctx=...{ctx!r}")
        lines.append(f"  [{slug}: {n} img tags, {njson} extra raw urls]")
    OUT.write_text("\n".join(lines))
    print("wrote", OUT, "pages", len(slugs))


if __name__ == "__main__":
    slugs = _slugs()
    main(slugs)
