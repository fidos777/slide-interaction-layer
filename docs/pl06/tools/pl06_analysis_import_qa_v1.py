from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

TOOLS_DIR = Path(__file__).resolve().parent
PL06_DIR = TOOLS_DIR.parent
REPO_ROOT = PL06_DIR.parents[1]
ANALYSIS_DIR = PL06_DIR / "unit_analysis"

sys.path.insert(0, str(TOOLS_DIR))

import pl06_packet_model_v1 as PM
import pl06_unit_model_v1 as U


EXPECTED_STATIC_IDS = {
    "K5-PL06-T03-B03",
    "K5-PL06-T03-B04",
    "K5-PL06-T05-B01",
    "K5-PL06-T06-B01",
}

EXPECTED_IMPORTED_IDS = {
    "K5-PL06-T01-B01",
    "K5-PL06-T01-B02",
    "K5-PL06-T01-B03",
    "K5-PL06-T02-B01",
    "K5-PL06-T02-B02",
    "K5-PL06-T03-B01",
    "K5-PL06-T03-B05",
    "K5-PL06-T07-B01",
}


def json_paths(value: Any) -> list[str]:
    found: list[str] = []

    if isinstance(value, str):
        if value.endswith(".json"):
            found.append(value)

    elif isinstance(value, dict):
        for child in value.values():
            found.extend(json_paths(child))

    elif isinstance(value, list):
        for child in value:
            found.extend(json_paths(child))

    return found


def row_ids(value: Any) -> set[str]:
    found: set[str] = set()

    if isinstance(value, dict):
        row_id = value.get("row_id")

        if isinstance(row_id, str) and row_id:
            found.add(row_id)

        for child in value.values():
            found.update(row_ids(child))

    elif isinstance(value, list):
        for child in value:
            found.update(row_ids(child))

    return found


print("=== IMPORT IDENTITY ===")

static_ids = set(U.STATIC_UNIT_ANALYSIS_IDS)
imported_ids = set(U.SOURCE_ANALYSIS_IMPORTED_IDS)
runtime_ids = set(U.UNIT_ANALYSIS)
active_ids = set(PM.active_unit_ids())

print(f"STATIC_IDS={sorted(static_ids)}")
print(f"IMPORTED_IDS={sorted(imported_ids)}")
print(f"RUNTIME_COUNT={len(runtime_ids)}")
print(f"ACTIVE_COUNT={len(active_ids)}")
print(
    "RUNTIME_EQUALS_ACTIVE="
    f"{runtime_ids == active_ids}"
)

if static_ids != EXPECTED_STATIC_IDS:
    raise SystemExit(
        "STOP: STATIC_ID_SET_MISMATCH"
    )

if imported_ids != EXPECTED_IMPORTED_IDS:
    raise SystemExit(
        "STOP: IMPORTED_ID_SET_MISMATCH"
    )

if static_ids & imported_ids:
    raise SystemExit(
        "STOP: STATIC_IMPORTED_OVERLAP"
    )

if runtime_ids != active_ids:
    raise SystemExit(
        "STOP: RUNTIME_COVERAGE_INCOMPLETE"
    )


print("=== RUNTIME SHAPES ===")

required_types = {
    "mandatory_propositions": list,
    "terminology": list,
    "compliance_sensitive": list,
    "ambiguities": list,
    "visual_subjects": list,
    "rumusan_beats": list,
    "dialogue": dict,
    "assessment": list,
    "pattern": dict,
}

for unit_id in sorted(imported_ids):
    record = U.UNIT_ANALYSIS[unit_id]
    defects = []

    for field, expected_type in (
        required_types.items()
    ):
        value = record.get(field)

        if not isinstance(value, expected_type):
            defects.append(
                f"{field}:"
                f"{type(value).__name__}"
            )

    print(
        "IMPORT_SHAPE|"
        f"UNIT={unit_id}|"
        f"DEFECTS={defects}"
    )

    if defects:
        raise SystemExit(
            "STOP: IMPORT_SHAPE_FAILED:"
            f"{unit_id}:{defects}"
        )


print("=== FROZEN ROW BINDING ===")

frozen_rows = {}

for unit_id in sorted(imported_ids):
    stem = unit_id.replace("-", "_")
    analysis_path = (
        ANALYSIS_DIR
        / f"{stem}_UNIT_ANALYSIS_v1.json"
    )

    source = json.loads(
        analysis_path.read_text(
            encoding="utf-8"
        )
    )

    candidates = []

    for raw_path in json_paths(
        source.get("source_extract")
    ):
        candidate = Path(raw_path)

        if not candidate.is_absolute():
            candidate = REPO_ROOT / candidate

        if candidate.is_file():
            candidates.append(
                candidate.resolve()
            )

    candidates = sorted(set(candidates))

    if len(candidates) != 1:
        raise SystemExit(
            "STOP: FROZEN_EXTRACT_PATH_COUNT:"
            f"{unit_id}:{len(candidates)}"
        )

    extract = json.loads(
        candidates[0].read_text(
            encoding="utf-8"
        )
    )
    ids = sorted(row_ids(extract))

    if not ids:
        raise SystemExit(
            "STOP: FROZEN_EXTRACT_HAS_NO_ROWS:"
            f"{unit_id}"
        )

    frozen_rows[unit_id] = {
        "rows": [
            {"row_id": row_id}
            for row_id in ids
        ]
    }

    print(
        "FROZEN_ROWS|"
        f"UNIT={unit_id}|"
        f"COUNT={len(ids)}"
    )


print("=== CONFORMANCE ===")

original_all_rows = PM.all_rows

try:
    PM.all_rows = lambda: frozen_rows

    for unit_id in sorted(imported_ids):
        defects = PM.analysis_conformance(
            unit_id
        )

        print(
            "IMPORT_CONFORMANCE|"
            f"UNIT={unit_id}|"
            f"DEFECTS={defects}"
        )

        if defects:
            raise SystemExit(
                "STOP: IMPORT_CONFORMANCE_FAILED:"
                f"{unit_id}:{defects}"
            )

finally:
    PM.all_rows = original_all_rows


gap_rows = PM.analysis_gap_matrix()

print(f"ANALYSIS_GAP_ROW_COUNT={len(gap_rows)}")

if gap_rows:
    raise SystemExit(
        "STOP: ANALYSIS_GAP_MATRIX_NOT_EMPTY"
    )

print("PL06_ANALYSIS_IMPORT_QA=PASS")
