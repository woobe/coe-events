#!/usr/bin/env python3
"""Download candidate images, measure them, and write a probe report.

Measurements are deliberately mechanical: HTTP status, bytes, real pixel size,
and simple colour/shape statistics that distinguish line-art plans from
photographs. They do not and cannot name what a photo depicts - that comes from
the page that publishes it.
"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageStat

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
IMGS = BASE / "images"
IMGS.mkdir(exist_ok=True)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/158.0.0.0 Safari/537.36")


def fetch(slug, url, referer=None):
    ext = ".jpg"
    for cand in (".png", ".webp", ".jpeg", ".gif"):
        if cand in url.lower():
            ext = cand
    path = IMGS / (slug + ext)
    args = ["curl", "-sS", "-k", "-L", "--compressed", "-m", "90", "-A", UA]
    if referer != "":
        args += ["-H", "Referer: " + (referer or url)]
    args += ["-o", str(path),
             "-w", "%{http_code} %{content_type} %{size_download}", url]
    proc = subprocess.run(args, capture_output=True, text=True, timeout=120)
    parts = (proc.stdout or "").split()
    code = int(parts[0]) if parts else 0
    ctype = parts[1] if len(parts) > 1 else ""
    info = {"slug": slug, "url": url, "status": code, "content_type": ctype,
            "bytes": path.stat().st_size if path.exists() else 0, "file": str(path)}
    if code == 200 and info["bytes"]:
        try:
            im = Image.open(path)
            im.load()
            w, h = im.size
            rgb = im.convert("RGB")
            small = rgb.resize((160, max(1, int(160 * h / w))))
            st = ImageStat.Stat(small)
            mean = [round(x, 1) for x in st.mean]
            # near-white and near-black share
            px = list(small.getdata())
            n = len(px)
            white = sum(1 for r, g, b in px if r > 235 and g > 235 and b > 235) / n
            black = sum(1 for r, g, b in px if r < 60 and g < 60 and b < 60) / n
            colours = len(set((r // 32, g // 32, b // 32) for r, g, b in px))
            sat = ImageStat.Stat(rgb.convert("HSV").resize((160, max(1, int(160 * h / w))))).mean[1]
            edges = small.convert("L").filter(ImageFilter.FIND_EDGES)
            edge_mean = round(ImageStat.Stat(edges).mean[0], 1)
            info.update({"width": w, "height": h, "format": im.format,
                         "mean_rgb": mean, "white_share": round(white, 3),
                         "black_share": round(black, 3), "colour_buckets": colours,
                         "mean_saturation": round(sat, 1), "edge_mean": edge_mean,
                         "lineart_like": bool(white > 0.55 and sat < 60 and colours < 60)})
        except Exception as exc:
            info["decode_error"] = str(exc)
    return info


def main(spec_path):
    spec = json.loads(Path(spec_path).read_text())
    out = []
    for item in spec["images"]:
        r = fetch(item["slug"], item["url"], "" if item.get("no_referer") else item.get("page"))
        r.update({k: item[k] for k in item if k not in ("slug", "url")})
        out.append(r)
        print(json.dumps(r, ensure_ascii=False))
    dest = BASE / (Path(spec_path).stem + "-probe.json")
    dest.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print("wrote", dest, len(out))


if __name__ == "__main__":
    main(sys.argv[1])
