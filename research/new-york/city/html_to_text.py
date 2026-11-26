"""Convert saved HTML captures to plain text next to them."""
import re, html, sys
from pathlib import Path

CAP = Path('/home/joe/repo_dev/coe-events/research/new-york/city/captures')
for name in sys.argv[1:]:
    p = CAP / name
    text = p.read_text(errors='ignore')
    text = re.sub(r'<script\b[^>]*>.*?</script>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'<style\b[^>]*>.*?</style>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    lines = [' '.join(line.split()) for line in text.splitlines()]
    out = p.with_suffix('.txt')
    out.write_text('\n'.join(line for line in lines if line), encoding='utf-8')
    print(out.name, out.stat().st_size)
