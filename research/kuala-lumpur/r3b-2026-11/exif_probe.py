from PIL import Image, ExifTags
from pathlib import Path
BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3b-2026-11/images")
for name in ["colony-klcc-capacity.jpg", "colony-ecocity-capacity.jpg", "colony-glassbox-event.jpg",
             "colony-boardroom-event.jpg", "wtc-merdeka-71.jpg", "mo-grand-ballroom.jpg",
             "stregis-astor-room.jpg", "gmbb-greybox-1a.jpg", "ccec-auditorium-plan.jpg",
             "worq-spm-event-01.jpg"]:
    im = Image.open(BASE / name)
    ex = im.getexif()
    tags = {ExifTags.TAGS.get(k, k): v for k, v in ex.items()}
    keep = {k: tags[k] for k in ("Make", "Model", "Software", "DateTime", "ImageDescription", "Artist")
            if k in tags}
    print(name, im.format, im.size, "exif:", keep or "none", "| info keys:", list(im.info)[:6])
