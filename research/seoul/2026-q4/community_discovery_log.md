# Seoul Run A (2026 Q4) — community discovery and disposition log

Research date: 2026-08-15. Working source of truth: installed skill
`~/.hermes/skills/plan-event/` only. Discovery layer: open web search plus
official community/organizer pages; every retained record was verified
against the group's own official page (Korean-language pages valid; only
language-neutral or directly supported facts recorded). Korea's Web3 market
is a DISCOVERY HYPOTHESIS, not a retained fact — this pass retained only
own-page-evidenced Seoul web3 groups.

Disposition convention: RETAINED (schema-valid local_community record in
communities.raw.json), REJECTED (examined, does not meet locality/own-page/
activity evidence rules), UNRESOLVED (candidate found but evidence
inaccessible or incomplete this pass).

## Retained (10 records)

1. AI Tinkerers Seoul — active (ai/machine_learning), cohost_open TRUE
   - Own page: seoul.aitinkerers.org. Inaugural meetup July 2, 2026; next
     event August 20, 2026 'AI Tinkerers Seoul: August Demo Night ft PostHog
     and DanaIX' (7-10pm KST). Sponsorship phrase on the same official page:
     'sponsored by PostHog and DanaIX.' needs_human_verify true + question.
2. GDG Seoul — active (ai/mixed)
   - Own page: gdg.community.dev/gdg-seoul. 1,321 members; 'Build with AI
     Seoul 2026 with Google DeepMind' May 2, 2026; DevFest Cloud x Seoul
     Nov 30, 2025. No co-host language captured -> cohost_open false.
3. AWSKRUG (AWS 한국사용자모임) — active (ai/mixed), cohost_open TRUE
   - Own page: meetup.com/ko-kr/awskrug. 11,671 members; sponsor section
     ('후원사 모두 보기') with Musinsa/LG U+/Daangn/Olive Young and venue
     sponsors; 9 upcoming events incl. DevOps 25th meetup Aug 19, 2026 and
     AI Engineering OpenClaw workshop Aug 20, 2026 at Centerfield, Gangnam.
     Contact route: awskr.org visibly referenced on the same page.
4. 모두의연구소 (Modulabs) — active (ai/machine_learning/data_science)
   - Own page: modulabs.co.kr/community/momos. Offline seminars/study groups
     in Seoul (모두팝 Dec 4; AI for Science Mar 26; 모두콘 2025 Dec 13).
     No co-host language captured -> cohost_open false.
5. PyLadies Seoul — active (data_science/ai)
   - Own page: meetup.com/seoul-pyladies-meetup (253 members) + official
     events page pyladies.kr/en/events (upcoming git tutorial workshop
     Jul 26, 2026; monthly 2026 bookclubs). No co-host language -> false.
6. Korea R User Group / Seoul R Meetup — active (data_science/machine_learning),
   cohost_open TRUE (conservative)
   - Own page: r2bit.com. Monthly Seoul R Meetup claim; donation-oriented
     sponsorship language ('여러분의 후원으로 더욱 강력해지세요'). Flagged
     true conservatively with a question distinguishing donations from event
     co-hosting; needs_human_verify true.
7. Seoul Ethereum Meetup — intermittent (web3)
   - Own page: meetup.com/seoul-ethereum-meetup. 4,156 members; no upcoming
     event displayed at fetch; 2026 activity unconfirmed -> intermittent.
8. Ethereum Seoul Community — intermittent (web3)
   - Own page: ethereum-seoul.community. Bi-weekly meetups at Ethaewon
     Hacker House; most recent dated notices reference 2024-era Ethcon
     organizing -> intermittent.
9. Superteam Korea — intermittent (web3)
   - Own page: superteam.fun/earn/regions/korea. South Korea Solana
     community; bounties/grants (digital-first); 2026 Seoul in-person
     meetup activity not evidenced from official page -> intermittent.
10. 파이토치 한국 사용자 모임 (PyTorch Korea) — intermittent (machine_learning/ai)
    - Own page: pytorch.kr. Digital-first Korean PyTorch user community with
      July 2026 blog translations; no standing Seoul in-person meetup
      evidenced -> intermittent (digital-only marker + in-person question).

## Rejected (examined, not retained)

- WAI Korea (waikorea.com): an AI/data company (주식회사 더블유에이아이)
  headquartered in Ansan (Gyeonggi), not a Seoul community; not a standing
  local meetup.
- Womxn Who Code Korea (facebook.com/wwcodeseoul): Facebook-page-only group;
  no HTTPS own page with observed activity captured this pass.
- QuantNode (restful3.github.io): GitHub-hosted open community for AI/n8n
  quant automation; not a Seoul-local organization page with observed
  in-person activity.
- dcinside '퀀트 마이너 갤러리' (gall.dcinside.com/mgallery/board/lists/?id=quant):
  a forum gallery, not a standing community organization page.
- Seoul International Fireworks Festival / Korean R Conference / PyCon KR /
  Try Everything / COMEUP / AI Summit Seoul: events/conferences, not
  standing communities (calendar layer handles the events).

## Unresolved (candidates found, evidence inaccessible/incomplete)

- Startup Grind Seoul: no current official Seoul chapter page with observed
  2026 activity surfaced this pass (search returned other chapters).
- Women in AI Korea chapter: global network (womeninai.co) has region pages
  but no Seoul/Korea chapter page with observed activity was captured.
- Bitcoin Seoul (bitcoin-seoul.kr): a June 2026 event at FKI Tower, not a
  standing community page with ongoing activity.
- Seoul data-science meetups beyond PyLadies/R: no additional standing Seoul
  data-science community page with observed 2026 activity surfaced.
- Standing Seoul quant community: no public own-page group found — recorded
  as an explicit community-research open question in city_input.json, never
  as a false absence.

## Notes

- cohost_open is true ONLY where the same official page states sponsorship/
  partnership/collaboration/venue-partner language (AI Tinkerers Seoul
  'sponsored by PostHog and DanaIX'; AWSKRUG sponsor/venue-sponsor section;
  Korea R User Group donation/sponsorship language flagged conservatively).
  Each carries needs_human_verify true and a verification question.
- contact_info is set only for a public HTTPS route visibly shown on the
  same official page: AWSKRUG (awskr.org). All other records keep null
  (email addresses, forms, organizer buttons are refused by policy).
- member_size_public uses only the number displayed on the group's own page
  (GDG Seoul 1,321; AWSKRUG 11,671; PyLadies Seoul 253; Seoul Ethereum
  Meetup 4,156); null elsewhere (never estimated).
- Activity labels are honest: 'active' only with an observed in-person fact
  within 12 months before accessed_on; 'intermittent' where evidence is
  irregular, digital-first, or 2026 activity unconfirmed; no 12-month-silent
  group is called current.
