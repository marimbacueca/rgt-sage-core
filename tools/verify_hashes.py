#!/usr/bin/env python3
import hashlib, sys
from pathlib import Path

def sha256sum(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def main(root='.'):
    root = Path(root)
    manifest = None
    for name in ('SHA256_MANIFEST.txt', 'RGT_Sage_v1.0_repo_SHA256.txt'):
        p = root / name
        if p.exists():
            manifest = p
            break
    if not manifest:
        print("No manifest found.", file=sys.stderr)
        return 2
    expected = {}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        h, rel = line.split(None, 1)
        expected[rel.strip()] = h.strip()
    ok = True
    for rel, h in expected.items():
        p = root / rel
        if not p.exists():
            print(f"MISS: {rel}")
            ok = False
            continue
        hh = sha256sum(p)
        if hh != h:
            print(f"MISMATCH: {rel}")
            ok = False
        else:
            print(f"OK: {rel}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else '.'))
