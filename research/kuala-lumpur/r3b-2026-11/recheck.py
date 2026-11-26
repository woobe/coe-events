import json
from pathlib import Path
from PIL import Image, ImageFilter, ImageStat
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11")
for name in ["dojo-event-hall.jpg", "dojo-pano.png", "colony-klcc-capacity.jpg", "colony-ecocity-capacity.jpg"]:
    p = BASE / "images" / name
    im = Image.open(p); im.load()
    w, h = im.size
    rgb = im.convert("RGB")
    small = rgb.resize((160, max(1, int(160 * h / w))))
    px = list(small.get_flattened_data()) if hasattr(small, "get_flattened_data") else list(small.getdata())
    n = len(px)
    white = sum(1 for r, g, b in px if r > 235 and g > 235 and b > 235) / n
    sat = ImageStat.Stat(rgb.convert("HSV").resize((160, max(1, int(160 * h / w))))).mean[1]
    print(name, w, "x", h, "white", round(white, 3), "sat", round(sat, 1),
          "mean", [round(x, 1) for x in ImageStat.Stat(small).mean])
