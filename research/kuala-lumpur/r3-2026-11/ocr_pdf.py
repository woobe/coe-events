import sys
from pathlib import Path
import pymupdf
from rapidocr_onnxruntime import RapidOCR

src = Path(sys.argv[1])
out = Path(sys.argv[2])
doc = pymupdf.open(str(src))
engine = RapidOCR()
chunks = []
for i, page in enumerate(doc, 1):
    pix = page.get_pixmap(dpi=200)
    png = Path('/home/joe/.hermes/profiles/jnr-research/cache/scratch/_pg%d.png' % i)
    pix.save(str(png))
    result, _ = engine(str(png))
    chunks.append('=== PAGE %d ===' % i)
    if result:
        for box, text, score in result:
            chunks.append('%s' % text)
    else:
        chunks.append('(no text)')
text = '\n'.join(chunks)
out.write_text(text, encoding='utf-8')
print('pages', doc.page_count, 'chars', len(text))
print(text[:2500])
