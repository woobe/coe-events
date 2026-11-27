import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
out = []
for i, page in enumerate(r.pages):
    out.append('--- PAGE %d ---' % (i+1))
    out.append(page.extract_text() or '')
text = '\n'.join(out)
dest = sys.argv[2]
open(dest, 'w', encoding='utf-8').write('\n'.join('%4d| %s' % (i+1, l) for i, l in enumerate(text.splitlines())))
print(len(r.pages), 'pages', len(text), 'chars ->', dest)
