# Previous San Francisco pages

Dated snapshots, newest last. Never edit a snapshot in place; add a new file.

## 2027-h1-san-francisco-summary.2026-11-22.html

- SHA-256: `4c14256b836b7d705b0ed1d6cf24638cbe78805f9c557d124ea988de4e1af5c3`
- Size: 1,263,395 bytes
- This was the last period-keyed San Francisco page (`2027-h1-san-francisco-summary.html`). It is superseded by the permanent city page and is kept byte-for-byte as the published reference.

## san-francisco-summary.2026-11-22.html

- SHA-256: `22ca3bc57de1725108403c06328b36fa25a0304bb9ad76b8abf6abdb7fc5d22c`
- Size: 2,012,788 bytes
- First version of the permanent city page, rendered from `research/san-francisco/city/city.json`. It is preserved before any future refresh overwrites it.
- This snapshot is the post-scrub render: six `candidate Saturday <date>` strings were removed from the store's related-event inference/verification prose (and the page re-rendered twice byte-identically) before the snapshot was taken. No earlier render of this page was ever published, so the same-day file was re-frozen rather than added twice.

## san-francisco-summary.2026-11-22.pre-v2.html

- SHA-256: `57d5a7423bcd2bfa2fd1be4c1a80921ba9771f6cf2c8a56ce514b3b77abf794b`
- Size: 1,801,731 bytes
- Approved F2–F4 build as it stood at F5 intake, before integrated fixes. The `.pre-v2` suffix avoids overwriting the first permanent city page, frozen earlier on the same date.

## san-francisco-summary.2026-11-22.pre-v3.html

- SHA-256: `8ecbe2ce20d276e1ea4c9195a683365efc5040a601095cb7809d62787bd9f8ff`
- Size: 1,833,377 bytes
- G5 intake, the approved G4 build. The `.pre-v3` suffix preserves both earlier snapshots from the same date.

## san-francisco-summary.2026-11-23.html

- SHA-256: `382e883d6d74f05e0b233c37f99fdc1b3694d48c55f7d76c6e20b21a81a909a5`
- Size: 1,825,262 bytes
- H5 intake: approved H4 build before integration checks or fixes.

These copies are byte-identical to their source files at copy time. Check with:

```
cd ~/repo_dev/coe-events
sha256sum summary/previous/*.html summary/2027-h1-san-francisco-summary.html summary/san-francisco-summary.html
```
