# -*- coding: utf-8 -*-
"""Lane O · A1 — capture the frozen oracle of the 11 non-B03 packet interaction records.

WHAT A1 FREEZES
---------------
The current packet population is, in the words of the shared resolver,
"ONE interaction record per active unit"
    (docs/pl06/tools/k5_treatment_resolver_v1.py, POST-0A PARITY block).

`pl06_packet_model_v1.packets()` returns one such record per ACTIVE unit (12).
B03 (K5-PL06-T03-B03) is the single calibrated unit and is handled by the A2
source-group oracle instead, so A1's population is the remaining 11 records, in
`UNIT_ROLL` order with B03 removed.

METADATA IS CAPTURED FROM COMMAND OUTPUT, NEVER TYPED
-----------------------------------------------------
  execution_commit          = git rev-parse HEAD
  controlling_module_blob   = git hash-object docs/pl06/tools/pl06_packet_model_v1.py
  record_count              = len(records)                 (computed)
  canonical_sha256          = sha256 of the compact canonical JSON of records
  source_docx_sha256        = identity of the extractor's module source (captured)

Only the RECORDS payload is hashed; the metadata that carries the hash is not.

SOURCE
------
`packets()` reads the controlled rows through the committed extractor, which opens
the K5 module DOCX resolved by `PL06_MODULE_DOCX` (documented search order in
docs/source/tools/src_authority_v1.py). The capture does not modify any input.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(os.path.dirname(HERE), "tools")
SRC_TOOLS = os.path.join(os.path.dirname(os.path.dirname(HERE)), "source", "tools")
sys.path.insert(0, HERE)
sys.path.insert(0, TOOLS)
sys.path.insert(0, SRC_TOOLS)

import lane_o_canonical_v1 as C            # noqa: E402
import pl06_packet_model_v1 as PM          # noqa: E402
import src_authority_v1 as SRC             # noqa: E402

ORACLE_ID = "A1_NON_B03_PACKET_INTERACTION_ORACLE_v1"
B03_UNIT = "K5-PL06-T03-B03"
CONTROLLING_MODULE_REL = "docs/pl06/tools/pl06_packet_model_v1.py"
OUT = os.path.join(HERE, "A1_packet_interaction_oracle_v1.json")


def records():
    """The 11 non-B03 interaction records, in UNIT_ROLL order, B03 removed."""
    return [p for p in PM.packets() if p["unit_id"] != B03_UNIT]


def build():
    repo = C.repo_root(HERE)
    recs = records()

    # Fail loudly rather than freeze a wrong-shaped population.
    ids = [r["unit_id"] for r in recs]
    assert B03_UNIT not in ids, "B03 must not appear in the A1 population"
    assert len(recs) == len(set(ids)) == 11, f"expected 11 distinct records, got {ids}"

    observed = dict(
        execution_commit=C.execution_commit(repo),
        controlling_module=CONTROLLING_MODULE_REL,
        controlling_module_blob_sha1=C.blob_sha1(repo, CONTROLLING_MODULE_REL),
        record_count=len(recs),                       # computed from records
        unit_ids=ids,
        canonical_sha256=C.canonical_sha256(recs),    # records payload only
        serialization=C.SERIALIZATION,
        source_docx_name=SRC.K5_DOCX_NAME,
        source_docx_sha256=SRC.K5_DOCX_SHA256,
    )
    return dict(
        oracle_id=ORACLE_ID,
        lane="O",
        kind="PRE_REFACTOR_ORACLE",
        population_basis=("ONE interaction record per active unit "
                          "(pl06_packet_model_v1.packets()), with the calibrated "
                          "B03 unit removed — that unit is frozen by the A2 oracle."),
        controlling_module=CONTROLLING_MODULE_REL,
        hash_scope="RECORDS_PAYLOAD_ONLY",
        metadata_observed=observed,
        records=recs,
    ), observed


def main():
    obj, observed = build()
    C.write_json(OUT, obj)
    print("A1 ORACLE WRITTEN:", OUT)
    for k in ("execution_commit", "controlling_module", "controlling_module_blob_sha1",
              "record_count", "canonical_sha256", "serialization",
              "source_docx_sha256"):
        print(f"  OBSERVED {k:28} {observed[k]}")
    print("  OBSERVED unit_ids                 " + ",".join(observed["unit_ids"]))


if __name__ == "__main__":
    main()
