import os
import shutil
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/singapore')
EVID = BASE / 'evidence'
CITY = BASE / 'city'

# restore the pre-refresh store so the build is idempotent
bak = EVID / 'city.pre-r8.json'
if not bak.exists():
    shutil.copy2(CITY / 'city.json', bak)
else:
    shutil.copy2(bak, CITY / 'city.json')

os.chdir(EVID)
import sys
sys.path.insert(0, str(EVID))
ns = {'__name__': '__main__', '__file__': str(EVID / 'run_build.py')}
for name in ('build_rev1.py', 'build_venues.py', 'build_holidays.py', 'build_events.py',
             'build_matrix.py', 'build_meta.py', 'update_supplement.py', 'dispositions.py'):
    path = EVID / name
    print('--- exec', name, flush=True)
    exec(compile(path.read_text(encoding='utf-8'), str(path), 'exec'), ns)
