import sys
from pathlib import Path
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None
    import subprocess
p = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else p.with_suffix('.txt')
if PdfReader is None:
    raise SystemExit('pypdf missing')
reader = PdfReader(str(p))
lines = []
for i, page in enumerate(reader.pages, 1):
    lines.append('=== PAGE %d ===' % i)
    lines.append(page.extract_text() or '')
text = '\n'.join(lines)
out.write_text(text, encoding='utf-8')
print('pages', len(reader.pages), 'chars', len(text), '->', out)
