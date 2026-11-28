# Kyoto K2 evidence, checked 2026-11-28 UTC

## Reiwa 9 search ledger

The search did not verify a Board-wide FY2027/28 terms and long-break notice. This is not a finding that there are no school holidays. Exact replacement language is in `k2-gaps.tsv` and `city.json:declared_gaps` (filter `kind == school_lane`).

- `京都市教育委員会 令和9年度 学校 休業日 夏季 冬季 学年末 京都市立 幼稚園 令和9年度 令和10年 site:edu.city.kyoto.jp OR site:city.kyoto.lg.jp`
- `site:city.kyoto.lg.jp/kyoiku 京都市立幼稚園 小学校 中学校 小中学校 始業式 終業式 令和9年度`
- `"京都市立幼稚園、小学校、中学校、小中学校の学期及び長期休業期間" "令和9年度" 京都市 学年始`
- `site:cms.edu.city.kyoto.jp 京都市 令和9年度 令和９年度 2027年度 年間行事予定 学年始休業日 夏季休業日 冬季休業日 学年末休業日`
- `site:city.kyoto.lg.jp/kyoiku 京都市立幼稚園 学期及び長期休業期間 令和9年度 令和8年度`
- `site:cms.edu.city.kyoto.jp 京都市 "令和9年度" "夏季休業日" OR "冬季休業日" OR "学年始休業日" OR "年間行事予定"`
- `site:city.kyoto.lg.jp OR site:cms.edu.city.kyoto.jp 京都市 令和９年度 2027 学年始 夏季休業 冬季休業 年間行事 京都京北 洛風 西京 特別支援`

Results included the FY8 and FY7 Board notices, Board school-instruction page and all-city CMS, no FY9 long-break notice. The fourth and sixth queries do not establish coverage of school-specific PDFs absent from the search index. Recheck the Board and relevant individual schools before release and when the Board normally posts the annual notice (FY7 and FY8 were both posted April 3).

- `https://www.city.kyoto.lg.jp/kyoiku/category/179-3-3-0-0-0-0-0-0-0.html` — HTTP 200, `k2/notices.html`, long-break notices through FY8 only in the captured index.
- `https://www.city.kyoto.lg.jp/kyoiku/soshiki/29-2-9-0-0.html` — HTTP 200, `k2/instruction.html`, latest discoverable annual long-break notice FY8; school-instruction office contact listed there, no outreach or reply recorded.
- `https://cms.edu.city.kyoto.jp/kyoto` and `https://cms.edu.city.kyoto.jp/kyoto/area_schedule` — both HTTP 200, `k2/cms.html`, `k2/area-schedule.html`; latter is an interactive events search, not a Board-wide long-break calendar. The initial HTML is not a census of every school result.
- `https://cms.edu.city.kyoto.jp/kyoto/search?keyword=%e4%bb%a4%e5%92%8c9%e5%b9%b4%e5%ba%a6` — HTTP 200, `k2/cms-reiwa9.html`; initial response contains site search heading, no usable long-break schedule. No negative inference from an unpopulated response.
- `https://www.edu.city.kyoto.jp/hp/` — HTTP 000, curl 60, incomplete TLS chain; `http://www.edu.city.kyoto.jp/hp/` — HTTP 200, `k2/directory-http.html`. Existing Rule No. 5 capture `school_kyoto_kanri_kisoku.html` reused; original HTTP capture was compared to a diagnostic HTTPS fetch in rev 2. No TLS bypass was used for the new fetches.
- `https://www.city.kyoto.lg.jp/kyoiku/page/0000236396.html` — existing capture `school_kyoto_reiwa8_schedule.html`, line 275, §§1–4. FY8 elementary year-start **2026-04-01–09**, versus Rule No. 5 Article 3 **April 1–7**; not applied as the 2027 annual date. Junior high Mar 20–31 from FY8 notice, not the Art. 3 lower bound Mar 21. Integrated schools expressly follow three-term junior highs (§4 `全て中学校（3学期制）に準ずる。`). FY8 annual HTML is the date source. Its `chirashi.pdf` attachment returned HTTP 200 at `https://www.city.kyoto.lg.jp/kyoiku/cmsfiles/contents/0000236/236396/chirashi.pdf`; `k2/reiwa8-attachment.pdf` is image-only and was not used for row dates.
- `https://cms.edu.city.kyoto.jp/300308/download/document/17733251` — HTTP 200, `k2/city-high.pdf`, Saikyo handbook rule excerpt Article 6(1)(4)–(8); principal-set windows only, not a dated FY9 notice or a support-school schedule.

## Offices and comparisons

`../2027/captures/k2/http.tsv` records capture filenames, requested/effective URLs, and actual HTTP and curl outcomes. City and prefecture ordinances Article 1 list weekends, national holidays and year-end office closures, with no further general office-closure category in the cited provisions. Neither creates a public holiday for all workers. The Jan 1 national day is not duplicated as a city or prefecture closure row; weekends are not standalone holiday rows. Prefectural school dates are Article 7 defaults with school exceptions, never attributed to the City Board.

- SFUSD: 2026/27 Calendar Details column confirmed Mar 26–Apr 2 and the Jun 2 last instruction boundary; added the missing Dec 21–Jan 1 named winter recess. The 2027/28 edition gives Aug 16 as first instruction, the Nov 22–23 recess and Nov 25–26 fall holidays (Nov 24 is a separately named closure), and Dec 20–31 recess. Intersession is not a district-wide closure claim.
- Edinburgh: 2026/27 council page sections Mid-term/Winter/Spring and June 29 term end; 2027/28 PDF pupil return Aug 18, Oct 26 and Jan 6 with staff returning earlier. Pinned edition already has only one Edinburgh summer row. Source boundary joins are explicit, not deduplication across authorities.
- VSB: both compact finals. Dec 2026/2027 named winter-break rows end Dec 31; January statutory/observed days are listed elsewhere in the documents. Mar 15–25 is the 2027 named spring break. July–September pupil interval updated from the June 30 administrative day and Sept 7 opening (Sept 6 Labour Day), not tagged as an official named break.
- Berlin: all pinned FY26/27 dates match VEVENT start and exclusive end in the current Berlin ICS. Both autumn 2027 break and December 2027 break match the FY27/28 KMK Berlin row. Not combined with Bavaria, Hesse or German public days.
- Ireland: PDF title page identifies Circular 0018/2026 despite the filename. Appendix A covers October, Christmas, February and Easter; March/April variations and shared February days documented; §1(d) does not standardise school-year boundaries. No national school summer interval was inferred.

## Translation and review

Each translated record preserves the original and its source context. The round-1 reviewer on `t_a99683f9` approved `k2-glosses.tsv` as written (SHA-256 `e54cc2b93530747422e99f71b6d5d524fa522cf2936f5a8369346bed7391f961`); the manager confirmed the provenance change for the 222 formerly pending rows. There are 214 holiday rows and 10 event rows with `reviewer_approved_gloss`, and two event rows with `official_english` (the organiser's own English title). No gloss wording changed. Rows marked `pinned_registry_row_snapshot` point to the existing pinned registry as the capture of inherited wording, not a claim of a fresh primary-source fetch. `k2-row-lineage.tsv` is the row-level URL, edition, exact locator and capture export, including inherited off-tab multilingual records. Capture fields are relative to `research/kyoto/2027/captures/` except named pinned edition snapshots. The Japan IT Week organiser URL redirects to its show hub (HTTP 200, curl 0); both URLs are recorded in `k2/http.tsv`.

No publishing or Git operations by the K2 implementer. The hard no-Git constraint takes precedence over the requested `git status --porcelain` evidence; see the reviewer's round-1 note for pre-existing paths outside Kyoto. The deterministic replay reads the immutable rev-2 fixture, validates the normal layout and the one-row relocation control, and only updates the live store and sidecar when invoked with `--write`. The control keeps exactly one host school row before relocating it to `JP:kyoto:junior-high`: the validator requires at least one school row in the host scope, not that each school row be in that scope. No renderer or converter change.
