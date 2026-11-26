#!/usr/bin/env python3
"""Report every difference between the round-1 store and the round-2 rebuild."""
import json
from pathlib import Path

base = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur')
a = json.loads((base / 'r3-2026-11/city.round1.json').read_text())
b = json.loads((base / 'city/city.json').read_text())
changes = []


def walk(x, y, path):
    if type(x) is not type(y) and not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        changes.append((path, repr(x)[:70], repr(y)[:70]))
        return
    if isinstance(x, dict):
        for k in sorted(set(x) | set(y)):
            if k not in x:
                changes.append((path + '/' + k, '<missing>', repr(y[k])[:70]))
            elif k not in y:
                changes.append((path + '/' + k, repr(x[k])[:70], '<missing>'))
            else:
                walk(x[k], y[k], path + '/' + k)
    elif isinstance(x, list):
        if len(x) != len(y):
            changes.append((path, 'len %d' % len(x), 'len %d' % len(y)))
            return
        for i, (xi, yi) in enumerate(zip(x, y)):
            walk(xi, yi, '%s[%d]' % (path, i))
    elif x != y:
        changes.append((path, repr(x)[:70], repr(y)[:70]))


walk(a, b, '')
print('changes', len(changes))
groups = {}
for path, old, new in changes:
    key = path.split('/')[1] if path.count('/') > 1 else path
    groups[key] = groups.get(key, 0) + 1
print('by top key', groups)
for path, old, new in changes:
    print(path, '|', old, '->', new)
