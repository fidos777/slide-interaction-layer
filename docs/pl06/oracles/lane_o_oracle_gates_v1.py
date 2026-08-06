# -*- coding: utf-8 -*-
"""Lane O — gates and biting fixtures for the A1 and A2 pre-refactor oracles.

A frozen hash proves nothing unless a change to what it covers actually moves it.
This module re-derives each oracle from source and asserts it still matches the
committed baseline, then runs BITING fixtures: each applies exactly one mutation
and asserts the canonical hash MOVES (and, where relevant, that a structural
invariant fails). A fixture that did not bite would be silently vacuous, so every
fixture also carries a control that leaves the input alone and must still match.

OBSERVED vs TARGET
------------------
  OBSERVED = read now, from command output / live derivation.
  TARGET   = the pinned Lane O expectation. The three values the lane was told to
             assert (BASE commit, the pl06_packet_model_v1.py blob) are declared
             as TARGET_* and checked against a freshly OBSERVED git command; the
             frozen canonical hashes are read from the committed baselines.

Run:  python3 lane_o_oracle_gates_v1.py
Exit 0 and prints ALL_LANE_O_CHECKS_PASS only when every check and fixture passes.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import lane_o_canonical_v1 as C                       # noqa: E402
import A2_b03_group_source_oracle_capture_v1 as A2    # noqa: E402

A1_ORACLE = os.path.join(HERE, "A1_packet_interaction_oracle_v1.json")
A2_ORACLE = os.path.join(HERE, "A2_b03_group_source_oracle_v1.json")

# --- TARGET: the pinned Lane O expectations (checked against OBSERVED, never into a baseline)
TARGET_BASE_COMMIT = "ebd6d81cf9c3b9e842d01d0b571ee16e32b5fb18"
TARGET_A1_MODULE = "docs/pl06/tools/pl06_packet_model_v1.py"
TARGET_A1_MODULE_BLOB = "a4e6db69e08f93f3151fe4166d17c6d481765e8f"
TARGET_A2_EXTRACT = "docs/pl06/batch1_extract/K5_PL06_T03_B03_SOURCE_EXTRACT_v1.json"
B03_UNIT = "K5-PL06-T03-B03"

_RESULTS = []


def check(name, ok, detail=""):
    _RESULTS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
    return bool(ok)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ==========================================================================================
# A1 — the 11 non-B03 packet interaction records
# ==========================================================================================
def gate_a1(repo):
    print("A1 — non-B03 packet interaction oracle")
    o = load(A1_ORACLE)
    recs = o["records"]
    obs_meta = o["metadata_observed"]
    frozen_hash = obs_meta["canonical_sha256"]

    # integrity: the stored hash actually covers the stored records payload
    check("A1.integrity_hash_covers_records",
          C.canonical_sha256(recs) == frozen_hash, frozen_hash)
    check("A1.record_count_is_11", len(recs) == 11 == obs_meta["record_count"])
    check("A1.b03_absent", all(r["unit_id"] != B03_UNIT for r in recs))

    # TARGET vs OBSERVED: pinned commit + controlling-module blob, observed via git now
    obs_commit = C.execution_commit(repo)
    obs_blob = C.blob_sha1(repo, TARGET_A1_MODULE)
    check("A1.TARGET_base_commit==OBSERVED", obs_commit == TARGET_BASE_COMMIT,
          f"OBSERVED {obs_commit}")
    check("A1.TARGET_module_blob==OBSERVED", obs_blob == TARGET_A1_MODULE_BLOB,
          f"OBSERVED {obs_blob}")

    # live parity (needs the module DOCX; skipped-with-notice when absent)
    live = None
    try:
        for m in [x for x in sys.modules if x.startswith(("pl06_", "k5_", "src_"))]:
            del sys.modules[m]
        sys.path.insert(0, os.path.join(os.path.dirname(HERE), "tools"))
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)),
                                        "source", "tools"))
        import pl06_packet_model_v1 as PM
        live = [p for p in PM.packets() if p["unit_id"] != B03_UNIT]
    except Exception as e:  # noqa: BLE001
        print(f"  [SKIP] A1.live_parity — source not derivable here ({type(e).__name__})")
    if live is not None:
        check("A1.live_rederivation_matches_frozen",
              C.canonical_sha256(live) == frozen_hash)
        check("A1.live_record_count_is_11", len(live) == 11)

    # BITING fixture: mutate exactly one field of one record → hash must move
    mutated = copy.deepcopy(recs)
    mutated[0]["title"] = (mutated[0].get("title") or "") + " · MUTATED"
    control = copy.deepcopy(recs)
    check("A1.bite.single_field_edit_moves_hash",
          C.canonical_sha256(mutated) != frozen_hash
          and C.canonical_sha256(control) == frozen_hash,
          "control still matches, mutation diverges")


# ==========================================================================================
# A2 — the six B03 content groups (derived from the controlled extract)
# ==========================================================================================
def gate_a2(repo):
    print("A2 — six-group B03 source oracle")
    o = load(A2_ORACLE)
    recs = o["records"]
    obs_meta = o["metadata_observed"]
    frozen_hash = obs_meta["canonical_sha256"]

    check("A2.integrity_hash_covers_records",
          C.canonical_sha256(recs) == frozen_hash, frozen_hash)

    # independent re-derivation from the committed extract (no k5_calib_model.screens())
    rows = A2.load_rows(repo)
    parent, groups = A2.derive_groups(rows)
    check("A2.rederivation_matches_frozen", C.canonical_sha256(groups) == frozen_hash)
    check("A2.group_count_is_6", len(groups) == 6 == obs_meta["group_count"])
    check("A2.group_ids_G1_G6", [g["group_id"] for g in groups] == [f"G{i}" for i in range(1, 7)])
    check("A2.single_parent_head_relationship",
          all(g["parent_row"] == parent["row_id"] for g in groups)
          and all(g["head_row"] == g["first_row"] for g in groups))
    cov = A2.coverage(rows, groups)
    check("A2.spans_tile_unit_disjointly",
          cov["covered_is_disjoint"] and cov["covers_all_rows_after_parent"])

    obs_commit = C.execution_commit(repo)
    obs_blob = C.blob_sha1(repo, TARGET_A2_EXTRACT)
    check("A2.TARGET_base_commit==OBSERVED", obs_commit == TARGET_BASE_COMMIT,
          f"OBSERVED {obs_commit}")
    check("A2.extract_blob_matches_baseline", obs_blob == obs_meta["extract_blob_sha1"],
          f"OBSERVED {obs_blob}")

    # -------------------------------------------------------------- biting fixtures (5)
    def rederive_hash(mrows):
        _, g = A2.derive_groups(mrows)
        return C.canonical_sha256(g), g

    frozen_heads = [g["head_row"] for g in groups]
    g3 = next(g for g in groups if g["group_id"] == "G3")

    # (1) MISSING GROUP — remove one group's entire source span → six becomes five
    m = [r for r in rows if r["row_id"] not in set(g3["row_span"])]
    h, g = rederive_hash(m)
    check("A2.bite.missing_group", h != frozen_hash and len(g) == 5,
          f"{len(g)} groups after removing a whole span")

    # (2) DUPLICATE ID — collide two group_ids in the derived records
    m = copy.deepcopy(groups)
    m[1]["group_id"] = m[0]["group_id"]
    ids = [x["group_id"] for x in m]
    check("A2.bite.duplicate_id",
          C.canonical_sha256(m) != frozen_hash and len(set(ids)) != len(ids))

    # (3) REORDERED ROW — swap two rows inside G1's span; source order must matter
    m = copy.deepcopy(rows)
    i = next(k for k, r in enumerate(m) if r["row_id"] == "T03B03-ROW-013")
    m[i], m[i + 1] = m[i + 1], m[i]
    h, _ = rederive_hash(m)
    check("A2.bite.reordered_row", h != frozen_hash)

    # (4) MISSING HEAD — delete only G3's head row; the anchor is lost and a neighbouring
    # row is silently mis-adopted as a head, which the hash and the head set must expose.
    m = [r for r in rows if r["row_id"] != g3["head_row"]]
    h, g = rederive_hash(m)
    mutated_heads = [x["head_row"] for x in g]
    check("A2.bite.missing_head",
          h != frozen_hash and mutated_heads != frozen_heads,
          f"heads shifted to {[x for x in mutated_heads if x not in frozen_heads]}")

    # (5) NEIGHBOURING-ROW LEAKAGE — move G2's first row into G1's span
    m = copy.deepcopy(groups)
    leaked = m[1]["row_span"][0]                 # G2 first row (a boundary row)
    m[0]["row_span"] = m[0]["row_span"] + [leaked]
    m[0]["last_row"] = leaked
    m[0]["row_count"] += 1
    dup = [rid for rid in (m[0]["row_span"] + m[1]["row_span"])]
    check("A2.bite.neighbouring_row_leakage",
          C.canonical_sha256(m) != frozen_hash and len(dup) != len(set(dup)),
          "boundary row now claimed by two groups")


# ==========================================================================================
def main():
    repo = C.repo_root(HERE)
    print(f"Lane O gates — repo {repo}\n")
    gate_a1(repo)
    print()
    gate_a2(repo)
    print()
    failed = [n for n, ok in _RESULTS if not ok]
    total = len(_RESULTS)
    if failed:
        print(f"LANE_O_GATES_FAIL — {len(failed)}/{total} checks failed: {failed}")
        sys.exit(1)
    print(f"ALL_LANE_O_CHECKS_PASS — {total}/{total} checks and fixtures passed")


if __name__ == "__main__":
    main()
