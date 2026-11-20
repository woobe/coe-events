# Community discovery log — Seoul, 2027 H1 (research run 2026-11-20; round 2 same day)

Discovery/corroboration sources were the skill references (`community_sources.md`,
`event_sources.md`) plus open Korean/English search, then every claim was checked on the
group's own page or on an official event listing. Directory and aggregator hits (Meetup,
Luma, KBW events, event-us, dev-event, code4korea, Roovook, Space Cloud) were used only to
find candidates.

## Method

1. Seeds: the 10 groups in `research/seoul/2026-q4/communities.raw.json` were re-fetched
   and re-labelled from scratch. Three did not survive as "active": Seoul Ethereum Meetup
   (last event 2022-12-15), Ethereum Seoul Community (2024-era notices) and 한국 R 사용자회
   (its 서울 R Meetup subpage now 404s).
2. Round-1 discovery queries were Korean and English (`서울 Web3 커뮤니티 밋업 2026
   이더리움 한국 밋업 정기 모임`, `GDG Seoul ... 2026 밋업 일정`) plus the Luma Seoul
   calendar (`luma.com/seoul`), which on 2026-11-20 listed only November-December 2026
   events and nothing in 2027.
3. Round-2 discovery (added after the first review, because the card asks for at least
   10 groups with 2026 activity and round 1 delivered 6) used: rendered Meetup event
   lists for AI Seoul and PyLadies Seoul, the official Korea Blockchain Week 2026 events
   page, `openKcloud`/event-us and three Korean trade-press articles, the ethcollective.xyz
   site and notices, BuilderBase's own event page, and searches
   (`Seoul AI meetup 2026`, `서울 AI 커뮤니티 정기 밋업 2026`, `한국 R 컨퍼런스 2026`,
   `Seoul hackathon community 2026`). Meetup and KBW pages needed headless Chromium.
4. Every retained record quotes the own-page (or official-listing) line that justifies its
   activity label. `activity_status: active` required an in-person activity fact dated
   within 12 months of 2026-11-20.

## Retained (16 groups)

Active with a dated 2026 in-person fact (11):

- **AI Tinkerers Seoul** — `Next event: Tuesday, November 24, 2026`; past events
  2026-07-02 and 2026-08-20.
- **AWSKRUG** — sessions dated 2026-11-04, 2026-11-24, 2026-11-26 (AWSKRUG Connect at
  스파크플러스 강남 4호점 IR룸 11B).
- **PyLadies Seoul** — rendered event list shows monthly book clubs and workshops through
  2026 (2026-02-07, 03-04, 03-21, 04-01, 04-25, 05-06, 05-30, 06-03, 07-26, 09-05) plus
  PyLadies Asia Conference 2026 announced for 2026-11-29.
- **모두의연구소 (Modulabs)** — in-person seminars at 역삼디오슈페리움 2층 모두의연구소
  강남캠퍼스 (`11월 10일(화)`, `11월 26일(목)`, `11월 27일(금)`; weekday/day pairs match
  2026 only).
- **Bridge34** — event agency; 2026-04-14, 2026-05-07 and KBW2026 side events
  2026-09-28..10-02.
- **블록체인 밋업데이 (BCMD, KISA)** — 31st session 2026-11-14 (Sat), 10:00-18:00, KISA
  서울청사 10층 기업성장허브.
- **AI Seoul (Meetup group)** — bi-weekly `AI Adoption Talk` on 2026-06-06, 06-20, 07-04,
  07-18, 09-05, 09-19, 10-03, 10-17, 10-31, 11-14, 11-28, next 12-12; 326 members.
- **Superteam Korea** — official KBW 2026 listing: Solana Ecosystem Day 2026-09-28
  (Metaplex x Superteam Korea), Solana Summit Korea 2026-09-30, SANC Nine 2026-10-01.
- **openKcloud 커뮤니티 (ETRI)** — openKcloud DevDay 2026 on 2026-11-10, 13:30-18:00, ST
  Center 중회의실3 (event-us listing plus 전자신문/디지털데일리/아이티데일리 coverage).
- **Ethereum Collective Korea (ECK)** — research digests dated 2026-11-12/16/19 and a
  2026.09.29 notice for the Ethereum Korea One Genesis Day 2 builder day in Seongsu.
- **Builderbase Hackathons** — DIGITAL AF Seoul hackathon 2026-10-01, 14:00-18:00 KST,
  Yeongdong-daero (own event page with schema.org dates).

Intermittent (3):

- **파이토치 한국 사용자 모임 (PyTorch Korea)** — blog posts 2026-10-20/23/28 plus a site
  report of `KVCache Meetup Korea` on 2026-09-30 at 드림플러스 강남; no own events calendar.
- **한국 R 사용자회** — site names `서울 R Meetup` but `r2bit.com/seoul-r-meetup/` returned
  a 404 again this pass; `use-r.kr` is still the 2021 conference site; no dated 2026 meetup
  observed. A third-party listing (`jumpingrivers.github.io/meetingsR`) shows
  `November 19: Korea R Conference` without a year, which is not enough to claim 2026.
- **GDG Seoul** — organizer page renders with an empty `Upcoming Events` section; the
  `Build with AI Seoul 2026 with Google DeepMind` (May 2, 2026) event page now 404s and
  survives only in a search index.

Dormant (2):

- **Seoul Ethereum Meetup** — 3,983 members, but `Past events 46` newest entry is
  `Thu, Dec 15, 2022`.
- **Ethereum Seoul Community** — bi-weekly-meetup description, newest notices are 2024.

## Rejected / not retained (with reasons)

- **Chainlink House Seoul (luma.com/Chainlink.KR)** — only event payload is `2025-03-28`;
  no 2026 activity.
- **PyData Seoul** — no active Seoul chapter page (`pydata.kr` is a placeholder).
- **QuantNode / dcinside quant gallery** — forum/GitHub-hosted, no Seoul organisation page
  with own-page activity evidence.
- **GDG on Campus chapters** (Seoul Women's University, SeoulTech) — 2026 events appear in
  indexes but no own-page activity fact could be observed inside this pass's budget.
- **ETHGlobal Seoul Meetup @ KBW** — Luma page says "September 6th" with no year and the
  city-level page has ended; the date cannot be tied to 2026 reliably, so it was dropped
  rather than guessed.
- **한국 R 사용자회 2026 conference** — searched (`한국 R 컨퍼런스 2026 11월 19일`); no
  official 2026 page or notice found. Kept as intermittent, not promoted on a third-party
  line.
- **AI 놀이터 (event-us/ainolite)** — a 2026 autumn meetup exists, but the channel page is
  a single event series with no group-level activity evidence; not recorded.
- **Space Cloud / Roovook / hirespace listings, code4korea / dev-event aggregators** —
  venue-side or aggregator listings, not communities.
- **Impact Hub Seoul** — does not exist; no record can be seeded from it.

## Co-host notes

Only **Bridge34** carries own-page language about running events for others ("Bridge34
plans, hosts and runs off-line events for global Web3 projects in Korea"), so it is the
only `cohost_open: true` record. Everything else is `cohost_open: false` with
`cohost_evidence_phrase: null` — that records the absence of own-page language, not a
claim that the group would refuse. Superteam Korea, Builderbase and ECK all demonstrably
co-host with other parties, so their false value is the conservative reading and each
carries a specific question.
