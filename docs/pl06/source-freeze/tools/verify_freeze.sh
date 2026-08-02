#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"
sha256sum -c records/SHA256SUMS.txt
python3 tools/verify_manifest.py
