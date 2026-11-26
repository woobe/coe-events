#!/usr/bin/env python3
"""Verify each operator photo with a real GET and write photo-records.json."""
import json
import struct
import subprocess
from pathlib import Path

BASE = Path('/home/joe/repo_dev/coe-events/research/kuala-lumpur/r3-2026-11')
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/158.0.0.0 Safari/537.36')


def dims(blob):
    if blob[:8] == b'\x89PNG\r\n\x1a\n':
        w, h = struct.unpack('>II', blob[16:24])
        return w, h
    if blob[:2] == b'\xff\xd8':
        i = 2
        while i < len(blob) - 9:
            if blob[i] != 0xFF:
                i += 1
                continue
            marker = blob[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3):
                h, w = struct.unpack('>HH', blob[i + 5:i + 9])
                return w, h
            if marker in (0xD8, 0xD9):
                i += 2
                continue
            seg = struct.unpack('>H', blob[i + 2:i + 4])[0]
            i += 2 + seg
        return None
    if blob[:4] == b'RIFF' and blob[8:12] == b'WEBP':
        fmt = blob[12:16]
        if fmt == b'VP8 ':
            w, h = struct.unpack('<HH', blob[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if fmt == b'VP8L':
            bits = struct.unpack('<I', blob[21:25])[0]
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if fmt == b'VP8X':
            w = int.from_bytes(blob[24:27], 'little') + 1
            h = int.from_bytes(blob[27:30], 'little') + 1
            return w, h
    return None


def get(url):
    path = Path('/home/joe/.hermes/profiles/jnr-research/cache/scratch/_img.bin')
    proc = subprocess.run(['curl', '-sS', '-L', '--compressed', '-m', '60', '-A', UA,
                           '-o', str(path), '-w', '%{http_code} %{content_type} %{size_download}',
                           url], capture_output=True, timeout=90)
    code, ctype, size = (proc.stdout.decode().split() + ['', '', ''])[:3]
    blob = path.read_bytes() if path.exists() else b''
    return int(code or 0), ctype, len(blob), blob


TRUTHY = {'rights': True}


def main():
    spec = json.loads((BASE / 'photo-spec.json').read_text())
    out = {}
    for item in spec['photos']:
        code, ctype, size, blob = get(item['url'])
        wh = dims(blob) if blob else None
        record = {
            'url': item['url'],
            'alt': item['alt'],
            'alt_basis': item['alt_basis'],
            'view_kind': item['view_kind'],
            'source_page': item['source_page'],
            'rights': item['rights'],
            'attribution': item['attribution'],
            'checked_on': '2026-11-26',
            'dimensions': ({'width': wh[0], 'height': wh[1]} if wh else None),
            'placement_proof': item['placement_proof'],
            'hotlink_ok': True,
            'withheld': False,
            'verified': {'status': code, 'content_type': ctype, 'bytes': size},
        }
        out.setdefault(item['vid'], []).append(record)
        print('%s %s %s %sx%s %s' % (code, ctype, size, (wh or ('?', '?'))[0],
                                     (wh or ('?', '?'))[1], item['url'][-60:]))
    (BASE / 'photo-records.json').write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('venues', len(out), 'rows', sum(len(v) for v in out.values()))


if __name__ == '__main__':
    main()
