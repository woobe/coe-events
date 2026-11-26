"""Round 2 review fix: DOJO TLS honesty + Marriott transform byte re-measure.

Touches only city.json's top-level `photos` value. Refuses if the inputs do not
match the expected pre-round-2 state.
"""
import hashlib
import json
import shutil
from pathlib import Path

BASE = Path("/home/joe/repo_dev/coe-events/research/kuala-lumpur")
CITY = BASE / "city" / "city.json"
PRE = BASE / "city" / "city.pre-r3b-round2.json"

EXPECT_SHA = "c03f3aa08be5a0d140d4c903d8b8f2183f818138bbe23ab20d2d5e4d335251d3"


def dump_json(value):
    # the store's on-disk format: 1-space indent, insertion key order, UTF-8
    return json.dumps(value, indent=1, ensure_ascii=False) + "\n"


before_bytes = CITY.read_bytes()
before_sha = hashlib.sha256(before_bytes).hexdigest()
assert before_sha == EXPECT_SHA, "city.json is not the approved post-R3b store: %s" % before_sha
store = json.loads(before_bytes.decode("utf-8"))

# snapshot the exact pre-round-2 state for the reviewer's diff
if not PRE.exists():
    shutil.copyfile(CITY, PRE)

photos = store["photos"]

# --- 1. DOJO row: the operator host's certificate expired 2026-08-10 --------
dojo = photos["kl-977b423768cd"]
assert len(dojo) == 1
row = dojo[0]
assert row["url"] == ("https://workspacedojo.com/wp-content/uploads/2024/05/"
                      "event-hall-dojo-1-1024x576.jpg")
assert row["hotlink_ok"] is True and row["verified"]["status"] == 200
row["hotlink_ok"] = False
row["rights"] = (
    "Operator gallery asset, \u00a9 DOJO Coworking Space. The operator's host "
    "workspacedojo.com presents a TLS certificate that expired 2026-08-10, so the "
    "asset was only retrievable with certificate validation disabled (HTTP 200, "
    "127,365 B under `curl -k`; validating curl exits 60, Python urllib raises "
    "CERTIFICATE_VERIFY_FAILED). Not hotlinkable: a browser blocks the image with a "
    "certificate error, so this record is evidence only and the venue's page shows "
    "no room photo from it. The "
    "page publishes no separate licence.")
row["verified"]["note"] = (
    "Status and bytes measured with TLS certificate validation disabled (`curl -k`) "
    "because the host chain expired 2026-08-10; a validating client cannot load this "
    "URL. Re-checked 2026-11-26.")

# --- 2. Marriott transform URLs: byte counts re-measured ---------------------
TRANSFORMS = {
    "kulwh-meeting-facilities-3802-hor-clsc.jpg": (733689, "W \u2014 Studio 3"),
    "kulxr-astor-room-5291-hor-wide.jpg": (833161, "St. Regis \u2014 The Astor Rooms"),
}
seen = set()
for vid, rows in photos.items():
    for r in rows:
        url = r.get("url") or ""
        for needle, (measured, label) in TRANSFORMS.items():
            if needle in url:
                assert r["hotlink_ok"] is True, label
                old = r["verified"].get("bytes")
                r["verified"]["bytes"] = measured
                r["verified"]["note"] = (
                    "Dynamic Marriott resize transform (output-quality/downsize "
                    "parameters): the endpoint re-encodes, so the byte count is a "
                    "per-fetch snapshot and dimensions are the stable invariant. "
                    "Dimensions re-checked and bytes re-measured 2026-11-26 "
                    "(was %d)." % old)
                seen.add(needle)
                print("%s: bytes %s -> %s" % (label, old, measured))
assert set(seen) == set(TRANSFORMS), "missed a transform row: %s" % (set(TRANSFORMS) - seen)

after_text = dump_json(store)
CITY.write_text(after_text, encoding="utf-8")
after_bytes = CITY.read_bytes()
print("before sha:", before_sha, len(before_bytes))
print("after  sha:", hashlib.sha256(after_bytes).hexdigest(), len(after_bytes))

# --- proofs ---------------------------------------------------------------
reload = json.loads(CITY.read_text(encoding="utf-8"))
assert dump_json(reload) == CITY.read_text(encoding="utf-8"), "round-trip not byte-identical"
prev = json.loads(PRE.read_text(encoding="utf-8"))
changed = [k for k in reload if json.dumps(reload[k], sort_keys=True) != json.dumps(prev[k], sort_keys=True)]
print("top-level keys changed:", changed)
assert changed == ["photos"], changed
orig = json.loads((BASE / "city" / "city.pre-r3b.json").read_text(encoding="utf-8"))
changed_orig = [k for k in reload if json.dumps(reload[k], sort_keys=True) != json.dumps(orig[k], sort_keys=True)]
print("keys changed vs city.pre-r3b.json:", changed_orig)
assert changed_orig == ["photos"], changed_orig
print("refresh_revision:", prev["refresh_revision"], "->", reload["refresh_revision"])
assert prev["refresh_revision"] == reload["refresh_revision"] == 1

# which photo rows differ from the pre-round-2 snapshot
diffs = []
for vid in reload["photos"]:
    a, b = prev["photos"][vid], reload["photos"][vid]
    if a == b:
        continue
    assert len(a) == len(b), vid
    for i, (ra, rb) in enumerate(zip(a, b)):
        if ra != rb:
            diffs.append((vid, i, sorted(set(ra) | set(rb))))
print("rows changed:", len(diffs))
for d in diffs:
    print("  ", d)
assert len(diffs) == 3, diffs
