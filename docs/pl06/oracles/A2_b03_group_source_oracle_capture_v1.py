# -*- coding: utf-8 -*-
"""Lane O · A2 — capture the frozen six-group B03 source oracle.

WHAT A2 FREEZES
---------------
The current calibration population is "six B03 content groups"
    (docs/pl06/tools/k5_treatment_resolver_v1.py, POST-0A PARITY block).

A2 derives those six groups DIRECTLY from the controlled extract — the committed
    docs/pl06/batch1_extract/K5_PL06_T03_B03_SOURCE_EXTRACT_v1.json
— using source-order boundaries and the parent/head relationship, and records
each group's full row span together with the rows it excludes at each boundary.

INDEPENDENCE
------------
A2 does NOT call `k5_calib_model_v1.screens()` or `.groups()`, and does not import
the shared unit model. The group rule is inlined here so the oracle is a second,
independent reading the refactor's output can be checked against:

  * A structural heading is HEADING_1/HEADING_2 always, or a HEADING_3 whose raw
    text is <= 55 chars and does not end in a full stop
    (docs/pl06/tools/pl06_unit_model_v1.py: is_structural / STRUCTURAL_MAX_CHARS).
  * A content group is a structural HEADING_3 whose next structural HEADING_3 is
    one of the module's own component markers (Fungsi / Fokus Utama Kontraktor / …)
    (pl06_unit_model_v1.py: components / COMPONENT_MARKERS).
  * The group's parent is the unit's single HEADING_2.
  * The group's span runs, in source order, from its head row up to (not into) the
    next group's head row; the last group runs to the end of the unit's rows.

METADATA IS CAPTURED FROM COMMAND OUTPUT, NEVER TYPED
-----------------------------------------------------
  execution_commit    = git rev-parse HEAD
  extract_blob_sha1   = git hash-object docs/pl06/batch1_extract/…_SOURCE_EXTRACT_v1.json
  group_count         = len(records)                  (computed)
  canonical_sha256    = sha256 of compact canonical JSON of the six group records
Only the RECORDS payload is hashed.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_o_canonical_v1 as C            # noqa: E402

ORACLE_ID = "A2_B03_SIX_GROUP_SOURCE_ORACLE_v1"
UNIT_ID = "K5-PL06-T03-B03"
EXTRACT_REL = "docs/pl06/batch1_extract/K5_PL06_T03_B03_SOURCE_EXTRACT_v1.json"
OUT = os.path.join(HERE, "A2_b03_group_source_oracle_v1.json")

# --- inlined derivation constants (values, not imports; see module docstring) ---
STRUCTURAL_MAX_CHARS = 55
COMPONENT_MARKERS = {"Fungsi", "Fokus Utama Kontraktor", "Fokus Utama Kontraktor:",
                     "Aspek Kritikal Kontraktor:"}
BOUNDARY_BASIS = "CONTIGUOUS_SOURCE_ORDER_HEAD_ROW_UP_TO_NEXT_GROUP_HEAD_ROW"


def _raw(row):
    return (row.get("raw_source_text") or "").strip()


def is_structural(row):
    ct = row["content_type"]
    if ct in ("HEADING_1", "HEADING_2"):
        return True
    if ct != "HEADING_3":
        return False
    t = _raw(row)
    return len(t) <= STRUCTURAL_MAX_CHARS and not t.endswith(".")


def load_rows(repo):
    import json
    with open(os.path.join(repo, EXTRACT_REL), encoding="utf-8") as f:
        return json.load(f)["rows"]


def derive_groups(rows):
    """The six content groups, in source order, straight from the extract rows."""
    parent = next((r for r in rows if r["content_type"] == "HEADING_2"), None)
    if parent is None:
        raise ValueError("no HEADING_2 parent in the controlled extract")

    heads = [r for r in rows if r["content_type"] == "HEADING_3" and is_structural(r)]
    head_texts = [_raw(h) for h in heads]

    # component head = a structural HEADING_3 whose NEXT structural HEADING_3 is a marker
    comp_heads = []
    for i, h in enumerate(heads):
        nxt = head_texts[i + 1] if i + 1 < len(head_texts) else None
        if head_texts[i] not in COMPONENT_MARKERS and nxt in COMPONENT_MARKERS:
            comp_heads.append((h, heads[i + 1]))  # (name head, marker head)

    idx = {r["row_id"]: i for i, r in enumerate(rows)}
    groups = []
    for gi, (head, marker) in enumerate(comp_heads):
        start = idx[head["row_id"]]
        end = (idx[comp_heads[gi + 1][0]["row_id"]]
               if gi + 1 < len(comp_heads) else len(rows))
        span = rows[start:end]
        left = rows[start - 1]["row_id"] if start - 1 >= 0 else None
        right = rows[end]["row_id"] if end < len(rows) else None
        groups.append(dict(
            group_id=f"G{gi + 1}",
            ordinal=gi + 1,
            covers=_raw(head),
            head_row=head["row_id"],
            head_content_type=head["content_type"],
            head_text=(head.get("controlled_display_text") or "").strip(),
            marker_row=marker["row_id"],
            marker_label=_raw(marker),
            module_page=head.get("module_page"),
            parent_row=parent["row_id"],
            parent_text=(parent.get("controlled_display_text") or "").strip(),
            parent_content_type=parent["content_type"],
            source_index_start=start,
            source_index_end=end,
            first_row=span[0]["row_id"],
            last_row=span[-1]["row_id"],
            row_span=[r["row_id"] for r in span],
            row_count=len(span),
            left_neighbour_excluded=left,
            right_neighbour_excluded=right,
            boundary_basis=BOUNDARY_BASIS,
        ))
    return parent, groups


def coverage(rows, groups):
    """Every row after the parent is claimed by exactly one group; spans disjoint."""
    covered = [rid for g in groups for rid in g["row_span"]]
    all_after_parent = [r["row_id"] for r in rows[1:]]  # rows[0] is the parent HEADING_2
    return dict(
        parent_row=rows[0]["row_id"],
        total_rows=len(rows),
        covered_rows=len(covered),
        covered_is_disjoint=len(covered) == len(set(covered)),
        covers_all_rows_after_parent=covered == all_after_parent,
        pre_group_excluded=[rows[0]["row_id"]],  # the parent, excluded before G1
    )


def build():
    repo = C.repo_root(HERE)
    rows = load_rows(repo)
    parent, groups = derive_groups(rows)

    ids = [g["group_id"] for g in groups]
    assert len(groups) == 6, f"expected six groups, got {len(groups)}: {ids}"
    assert ids == [f"G{i}" for i in range(1, 7)], ids
    cov = coverage(rows, groups)
    assert cov["covered_is_disjoint"], "group spans overlap"
    assert cov["covers_all_rows_after_parent"], "group spans do not tile the unit"

    observed = dict(
        execution_commit=C.execution_commit(repo),
        controlling_extract=EXTRACT_REL,
        extract_blob_sha1=C.blob_sha1(repo, EXTRACT_REL),
        group_count=len(groups),                       # computed from records
        group_ids=ids,
        parent_row=parent["row_id"],
        canonical_sha256=C.canonical_sha256(groups),   # records payload only
        serialization=C.SERIALIZATION,
    )
    return dict(
        oracle_id=ORACLE_ID,
        lane="O",
        kind="PRE_REFACTOR_ORACLE",
        unit_id=UNIT_ID,
        population_basis="six B03 content groups derived directly from the controlled extract",
        controlling_extract=EXTRACT_REL,
        derivation="INLINE_SOURCE_ORDER_COMPONENT_RULE_NOT_k5_calib_model_screens",
        hash_scope="RECORDS_PAYLOAD_ONLY",
        coverage=cov,
        metadata_observed=observed,
        records=groups,
    ), observed


def main():
    obj, observed = build()
    C.write_json(OUT, obj)
    print("A2 ORACLE WRITTEN:", OUT)
    for k in ("execution_commit", "controlling_extract", "extract_blob_sha1",
              "group_count", "parent_row", "canonical_sha256", "serialization"):
        print(f"  OBSERVED {k:24} {observed[k]}")
    print("  OBSERVED group_ids            " + ",".join(observed["group_ids"]))


if __name__ == "__main__":
    main()
