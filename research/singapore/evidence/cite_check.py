"""Field-level provenance audit plus the claim-object count used by the gap text.

Two different questions, deliberately reported separately:
  * fields missing a quote or a locator (a field-level test; the nine unknown
    access rows carry locator_note instead of an invented line);
  * claim objects with a claim_id and neither source_locator nor capture (the
    definition the round-1 reviewer reproduced: 750).
"""
import json
import collections

s = json.load(open('research/singapore/city/city.json'))
miss = collections.Counter()
total = collections.Counter()
noquote = []
for vid, v in s['venues'].items():
    for f, e in v['fields'].items():
        total[f] += 1
        if not e.get('quote') or not e.get('source_locator'):
            miss[f] += 1
            if len(noquote) < 12:
                noquote.append((vid, f, e.get('value') if not isinstance(e.get('value'), (dict, list)) else '...',
                                e.get('source_locator'), e.get('verified_at')))
print('venue fields', sum(total.values()), 'missing quote/locator', sum(miss.values()))
for f, n in miss.most_common():
    print(' ', f, n, 'of', total[f])
print(noquote)


def count(obj, path, acc):
    if isinstance(obj, dict):
        if obj.get('claim_id') and not obj.get('source_locator') and not obj.get('capture'):
            acc[path] += 1
        for value in obj.values():
            count(value, path, acc)
    elif isinstance(obj, list):
        for value in obj:
            count(value, path, acc)


acc = collections.Counter()
count(s['venues'], 'venue', acc)
count(s['events'], 'event', acc)
print('claim objects with claim_id and neither locator nor capture:', sum(acc.values()), dict(acc))
