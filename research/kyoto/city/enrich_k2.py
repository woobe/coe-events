"""Replay only Kyoto K2 from the frozen rev-2 store and hashed overlay inputs."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

D = Path(__file__).resolve().parent
CAP = D.parent / '2027/captures'
SKILL = Path.home() / '.hermes/skills/plan-event'
PIN = SKILL / 'references/editions/school_holidays-3b20667d.json'
BASE = '5bb21a7a7c1670fcce784fd8dd03026598a3d0e2e90d463372c0b1fd028c7d3c'
SIDE = 'db7cc8afe5d1c98a680a6f4064b5bc137d01e9bdc5ea69c3b9f18d0750312700'
PAGE = '7f30bf9eed19ed6ef398ddb7f538687d35c4e0ba22105796217c8f53e482473f'
# Exact pre-approval K2 output, accepted only as an input to the guarded write.
PRE_APPROVAL = ('1ae6531db44d954ce16dc313176f20e590ddae7d2aa7a0fea5a27b8ab7f7c0e5',
                'b3d1a72c640e3896787c848bf77e14b9798f0961a72edda3bf9e98db140d3bdb')
APPROVED_GLOSS_SHA = 'e54cc2b93530747422e99f71b6d5d524fa522cf2936f5a8369346bed7391f961'
DAY = '2026-11-28'
STAMP = f'{DAY}T15:20:00Z'
HOST = 'JP:kyoto'
PREF = 'JP:kyoto-prefecture'
COMPARE = {('US-CA:sfusd', 'school_holiday'), ('GB-SCT:edinburgh', 'school_holiday'),
           ('CA-BC:vsb', 'school_holiday'), ('DE-BE', 'school_holiday'), ('IE', 'school_holiday')}
SOURCES = {
    'fy8': ('https://www.city.kyoto.lg.jp/kyoiku/page/0000236396.html', '京都市教育委員会 令和8年度 学期及び長期休業期間 (2026-04-03)', 'school_kyoto_reiwa8_schedule.html'),
    'city-rule': ('http://www.edu.city.kyoto.jp/hp/chosa/reiki_honbun/x898RG00000134.html', '京都市教育委員会規則第5号・管理運営規則 第3条', 'school_kyoto_kanri_kisoku.html'),
    'pref-rule': ('https://www.pref.kyoto.jp/reiki/reiki_honbun/a300RG00000836.html#e000000731', '京都府立学校の管理運営に関する規則 第7条', 'k2/pref-school.html'),
    'city-code': ('https://en3-jg.d1-law.com/kyoto/d1w_reiki/H401901010005/H401901010005_j.html', '京都市の休日を定める条例（平成元年 条例第5号）', 'k2/city-code.html'),
    'pref-code': ('https://www.pref.kyoto.jp/reiki/reiki_honbun/a300RG00000020.html#e000000028', '京都府の休日を定める条例（平成元年 条例第4号）', 'k2/pref-office.html'),
}
LABELS = {'winter': ('冬季休業日', 'Winter break'), 'summer': ('夏季休業日', 'Summer break'),
          'year-end': ('学年末休業日', 'School year-end break'), 'year-start': ('学年始休業日', 'School year-start break')}
GROUPS = {'kindergarten': 'kindergartens', 'elementary': 'elementary schools', 'junior-high': 'junior high schools',
          'integrated': 'integrated schools', 'prefectural-junior-high': 'prefectural junior high schools',
          'prefectural-other': 'prefectural schools other than junior high', 'prefectural-all': 'prefectural schools'}
ERROR = 'store.holidays: revision 1 needs local school rows or an evidenced no_applicable_days coverage finding'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + '\n'


def table(name):
    with (D / name).open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def key(row):
    return tuple(row.get(k) for k in ('jurisdiction_id', 'kind', 'holiday_name', 'start_date', 'end_date',
                                      'observance', 'school_authority_id', 'school_group'))


def evidence(url, edition, locator, capture):
    if not capture.startswith('school_holidays-'):
        assert (CAP / capture).is_file(), capture
    return dict(source_url=url, source_edition=edition, source_locator=locator, source_capture=capture, accessed_on=DAY)


def local(item):
    src, term, group = (item[k] for k in ('source', 'term', 'group'))
    url, edition, capture = SOURCES[src]
    scope = PREF if src == 'pref-code' else HOST
    default = src in {'city-rule', 'pref-rule'}
    if group == 'office-only':
        name, en = ('京都府の休日（府機関のみ）', 'Kyoto Prefecture office closure (offices only)') if scope == PREF else (
            '京都市の休日（市役所等のみ）', 'Kyoto City office closure (offices only)')
    else:
        name, en = LABELS[term]
        en += f' ({GROUPS[group]}' + ('; rule-based default)' if default else ')')
    row = dict(jurisdiction_id=scope, kind='municipal_holiday' if term == 'office' else 'school_holiday',
               start_date=item['start'], end_date=item['end'], name=name, holiday_name=name, name_en=en,
               translation_provenance={'kind': 'reviewer_approved_gloss', 'source_context': item['locator']},
               calendar_status='rule_default' if default else 'dated_notice' if src == 'fy8' else 'office_only',
               source_title=edition, needs_human_verify=default,
               verification_questions=['Check for authority or school exceptions before relying on the default.'] if default else [],
               evidence={'observed_facts': item['locator']}, **evidence(url, edition, item['locator'], capture))
    if term != 'office':
        row.update(school_authority_id={'city-board': 'kyoto-city-board-of-education', 'pref-board': 'kyoto-prefecture-board-of-education'}[item['authority']], school_group=group, school_term=term)
    else:
        row['office_only'] = True
    return row


def validate(store):
    return subprocess.run(['python3', '-B', str(SKILL / 'scripts/city_store.py'), '--check', str(store), '--registry', str(PIN)],
                          text=True, capture_output=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write', action='store_true', help='replace Kyoto city.json and its sidecar only after successful validation')
    a = p.parse_args()
    for name, sha in [('city.json', BASE), ('holiday-supplement.json', SIDE), ('kyoto-summary.html', PAGE)]:
        assert digest(D / 'preimage' / name) == sha, name
    overlay_sha = hashlib.sha256()
    for line in (D / 'k2-overlay.sha256').read_text().splitlines():
        sha, rel = line.split(maxsplit=1)
        assert digest(D / rel) == sha, rel
        overlay_sha.update((line + '\n').encode())
    s = json.loads((D / 'preimage/city.json').read_bytes())
    reg = s['holiday_registry']
    assert s['city_slug'] == 'kyoto-jp' and s['schema_version'] == 'city-store/1' and s['refresh_revision'] == 2
    assert reg['host_jurisdiction_id'] == HOST and len(reg['base_jurisdiction_ids']) == 36
    assert digest(PIN) == reg['sha256'] == reg['edition_copy_sha256']
    gloss_file = D / 'k2-glosses.tsv'
    assert digest(gloss_file) == APPROVED_GLOSS_SHA, 'Gloss wording changed; obtain fresh reviewer approval'
    gloss = dict(line.split('\t', 1) for line in gloss_file.read_text().splitlines())
    with (CAP / 'k2/http.tsv').open() as stream:
        captures = {r['requested_url']: 'k2/' + r['capture'] for r in csv.DictReader(stream, delimiter='\t') if r['curl_exit'] == '0'}
    local_rows = [local(r) for r in table('k2-local.tsv')]
    assert len({key(r) for r in local_rows}) == len(local_rows)
    assert {str(r['school_group']) for r in local_rows if r['calendar_status'] == 'dated_notice'} == {'kindergarten', 'elementary', 'junior-high', 'integrated'}
    assert any(r['kind'] == 'school_holiday' and r['jurisdiction_id'] == HOST for r in local_rows)
    gaps = [dict(kind='school_lane', jurisdiction_id=r['scope'], school_group=r['group'], school_term=r['term'],
                 text=r['text'], verified_at=DAY, evidence_ledger='k2-evidence.md') for r in table('k2-gaps.tsv')]
    s['declared_gaps'] = [r for r in s['declared_gaps'] if r['kind'] != 'school_lane'] + gaps
    old_local = [r for r in s['coverage'] if r.get('jurisdiction_id') == HOST]
    assert {r['kind'] for r in old_local} == {'public_holiday_coverage', 'school_lane_finding'}
    closure = local_rows[-4:]
    local_cov = [dict(r, kind='municipal_office_coverage', finding='office_closures_only') for r in closure]
    s['coverage'] = [r for r in s['coverage'] if r.get('jurisdiction_id') != HOST] + local_cov
    ids = [HOST, PREF]
    supplement = dict(city_slug=s['city_slug'], checked_on=DAY, jurisdiction_ids=ids, holidays=local_rows,
                      coverage=local_cov, overlay_inputs_sha256=overlay_sha.hexdigest(), note='Kyoto-only office and school layers; see dated school gaps in city.json.')

    checked = set()
    rows = []
    for r in s['holidays']:
        name, scope = r['holiday_name'], r['jurisdiction_id']
        if (scope, r['kind']) in COMPARE:
            # Add the second authority boundary where the pinned summer end was derived.
            if name == 'Summer Break' and scope == 'CA-BC:vsb':
                secondary = next(url for url in captures if 'compact-vsb-calendar-2027-2028-' in url)
                r['end_date'] = '2027-09-06'
                r['source_locator'] = "2026/27 key dates: 'June 30 - Administrative Day'"
                r['calendar_status'] = 'between_instruction_terms'
                r['additional_source'] = evidence(secondary, '2027-2028 compact final', "Key dates: 'September 07 - First Day of School'", captures[secondary])
            elif name == 'Summer Break' and scope == 'US-CA:sfusd':
                secondary = next(url for url in captures if '202027-28' in url)
                r['calendar_status'] = 'between_instruction_terms'
                r['additional_source'] = evidence(secondary, '2027-28 SFUSD District-Wide Calendar', "August details: 'Aug 16: First Day of Fall Instruction'", captures[secondary])
            elif name == 'Summer holidays' and scope == 'GB-SCT:edinburgh':
                secondary = next(url for url in captures if '/downloads/file/40106/' in url)
                r['calendar_status'] = 'between_instruction_terms'
                r['additional_source'] = evidence(secondary, 'School Session Dates 2027/28', "'Pupils resume | Wednesday | 18 August | 2027'", captures[secondary])
            r['source_capture'] = captures[r['source_url']]
            r['source_rechecked_on'] = DAY
            k = key(r)
            if k in checked:
                if any(x == r for x in rows):
                    print('Exact comparison duplicate dropped:', k)
                    continue
                raise ValueError(f'Comparison identity collision (not exact): {k}')
            checked.add(k)
        if name in gloss or scope == 'KR':
            en = gloss[name] if name in gloss else name.rsplit(' (', 1)[1][:-1]
            r['name_en'] = en
            r['name'] = name
            r['translation_provenance'] = dict(kind='reviewer_approved_gloss', source_context=r['source_locator'])
            r.setdefault('source_capture', 'cao_shukujitsu_2027.html' if scope == 'JP' else PIN.name)
            if r['source_capture'] == PIN.name:
                r['source_capture_kind'] = 'pinned_registry_row_snapshot'
        elif scope in {'AT', 'AT:vienna', 'CZ', 'CZ:prague', 'DE-BE', 'DE-BY', 'DE-HE', 'PL', 'PL:mazowieckie', 'JP', 'JP:osaka', 'JP:tokyo', 'TH'}:
            raise ValueError(f'Missing gloss: {scope} {name}')
        rows.append(r)
    # Add the FY26/27 winter tail omitted in the original SFUSD projection.
    sf = next(r for r in rows if (r['jurisdiction_id'], r['kind'], r['holiday_name']) == ('US-CA:sfusd', 'school_holiday', 'Spring Recess'))
    locator = "2026-27 Calendar Details, December/January: 'Dec 21 - Jan 1: Winter Recess (School Sites & EED Closed)'"
    rows.append(dict(sf, holiday_name='Winter Recess', start_date='2026-12-21', end_date='2027-01-01',
                     source_locator=locator, evidence={'observed_facts': locator}))
    assert len({key(r) for r in rows if (r['jurisdiction_id'], r['kind']) in COMPARE}) == len([r for r in rows if (r['jurisdiction_id'], r['kind']) in COMPARE])
    s['holidays'] = rows + local_rows
    assert len(s['events']) == 12
    events = table('k2-events.tsv')
    assert len(events) == len(s['events'])
    for e in events:
        row = s['events']['kyoto-ev-' + e['id']]
        claim = row['evidence'][0]
        row.update(name_en=e['english'], locality=e['locality'], status=e['status'],
                   translation_provenance=dict(kind='official_english' if e['translation'] == 'official' else 'reviewer_approved_gloss', source_context=e['locator']),
                   **evidence(claim['source_url'], claim['source_title'], e['locator'], e['capture']))
    reg.update(_supplement_source='holiday-supplement.json', jurisdiction_ids=reg['base_jurisdiction_ids'] + ids,
               holiday_rows=len(s['holidays']), coverage_rows=len(s['coverage']))
    s.update(refresh_revision=3, updated_at=STAMP)
    s['runs'].append(dict(kind='refresh', run_id='run-kyoto-2027-k2-overlay-3', updated_at=STAMP,
                          holiday_rows=len(s['holidays']), coverage_rows=len(s['coverage']), event_rows=len(s['events']), overlay_inputs_sha256=overlay_sha.hexdigest()))

    with tempfile.TemporaryDirectory(prefix='k2-check-', dir=D) as tmp:
        stage = Path(tmp)
        side = stage / 'holiday-supplement.json'
        side.write_text(dump(supplement))
        reg['supplement'] = dict(jurisdiction_ids=ids, path=side.name, sha256=digest(side))
        store = stage / 'city.json'
        store.write_text(dump(s))
        good = validate(store)
        print(good.stdout + good.stderr, end=''); print('correct layout exit', good.returncode)
        assert good.returncode == 0

        # Keep exactly one host school row so moving that row tests the release gate.
        probe = json.loads(store.read_bytes())
        host_school = [r for r in probe['holidays'] if (r['jurisdiction_id'], r['kind']) == (HOST, 'school_holiday')]
        chosen = next(r for r in host_school if r['school_group'] == 'junior-high' and r['school_term'] == 'year-end')
        probe['holidays'] = [r for r in probe['holidays'] if r not in host_school or r is chosen]
        test_store = stage / 'layout-probe.json'
        subscope = HOST + ':junior-high'
        probe['holiday_registry']['jurisdiction_ids'].append(subscope)
        probe['holiday_registry']['supplement']['jurisdiction_ids'].append(subscope)
        test_store.write_text(dump(probe))
        result = validate(test_store)
        print(result.stdout + result.stderr, end=''); print('single host school row exit', result.returncode)
        assert result.returncode == 0
        chosen['jurisdiction_id'] = subscope
        test_store.write_text(dump(probe))
        result = validate(test_store)
        print(result.stdout + result.stderr, end=''); print('single school-only subscope row exit', result.returncode)
        assert result.returncode == 1 and ERROR in result.stdout + result.stderr
        if a.write:
            live, live_side = D / 'city.json', D / side.name
            assert digest(live) in {BASE, PRE_APPROVAL[0], digest(store)}, 'Unexpected live store; refusing to replace'
            assert digest(live_side) in {SIDE, PRE_APPROVAL[1], digest(side)}, 'Unexpected live supplement; refusing to replace'
            side.replace(live_side)
            store.replace(live)
    print('scope\tkind\trows')
    for (scope, kind), count in sorted(Counter((r['jurisdiction_id'], r['kind']) for r in s['holidays']).items()):
        print(f'{scope}\t{kind}\t{count}')
    print('events:', len(s['events']), 'holiday name_en:', sum('name_en' in r for r in s['holidays']),
          'event name_en:', sum('name_en' in r for r in s['events'].values()))
    print('rev-3 sha256:', hashlib.sha256(dump(s).encode()).hexdigest())
    print('overlay manifest sha256:', overlay_sha.hexdigest())


if __name__ == '__main__':
    main()
