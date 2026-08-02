#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'records' / 'FREEZE_MANIFEST.json').read_text(encoding='utf-8'))
errors = []
for item in manifest['artifacts']:
    p = root / item['path']
    if not p.is_file():
        errors.append(f"MISSING {item['path']}")
        continue
    size = p.stat().st_size
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    if size != item['bytes']:
        errors.append(f"SIZE {item['path']} expected={item['bytes']} actual={size}")
    if digest != item['sha256']:
        errors.append(f"HASH {item['path']} expected={item['sha256']} actual={digest}")
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f"PASS {len(manifest['artifacts'])}/{len(manifest['artifacts'])} artifacts verified")
