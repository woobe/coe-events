import sys
from pathlib import Path
import fitz  # pymupdf

p = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else p.with_suffix('.txt')
doc = fitz.open(str(p))
chunks = []
for i, page in enumerate(doc, 1):
    chunks.append('=== PAGE %d ===' % i)
    chunks.append(page.get_text('text'))
text = '\n'.join(chunks)
out.write_text(text, encoding='utf-8')
print('pages', doc.page_count, 'chars', len(text), 'images', sum(len(pg.get_images()) for pg in doc))
print(text[:1500])
