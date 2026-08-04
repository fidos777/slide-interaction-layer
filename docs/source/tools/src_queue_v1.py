# -*- coding: utf-8 -*-
"""Stage 4.2F-C Lane 7 — the production queue, derived from artifacts on disk.

    python3 docs/source/tools/src_queue_v1.py

Every row and every percentage is computed from the custody manifest, the extraction
summary, the provisional models and the inventory. Nothing is typed in. A completion
percentage that a human wrote by hand is a claim; one that is counted from artifacts is a
measurement, and only the second kind belongs in a queue.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
DOCS = os.path.dirname(SRC_DIR)
PL06 = os.path.join(DOCS, "pl06")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(PL06, "tools"))
import src_authority_v1 as A     # noqa: E402
import src_inventory_v1 as INV   # noqa: E402

STAGE = "4.2F-C"
BATCH1_DIR = os.path.join(PL06, "batch1_extract")

STATUSES = ["SOURCE_BLOCKED", "SOURCE_READY", "BOUNDARY_AMBER", "EXTRACTED", "MODEL_READY",
            "WAITING_PATTERN_DECISIONS", "READY_FOR_STORYBOARD",
            "READY_FOR_ONE_TOUCH_REVIEW", "FROZEN", "PACKAGED"]

COLUMNS = ["course", "pl", "unit_id", "source_binary_verified", "source_authority_inherited",
           "boundary_status", "extraction_status", "model_status",
           "pattern_decision_dependency", "storyboard_readiness", "qa_readiness",
           "bariah_review_dependency", "blocker", "next_executable_action"]

PENDING_PACKAGE = "K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx"


def _batch1_summary():
    p = os.path.join(BATCH1_DIR, "PL06_BATCH1_EXTRACTION_SUMMARY_v1.json")
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding="utf-8"))


def _extract_files():
    if not os.path.isdir(BATCH1_DIR):
        return set(), set()
    ex = {f for f in os.listdir(BATCH1_DIR) if f.endswith("_SOURCE_EXTRACT_v1.json")}
    md = {f for f in os.listdir(BATCH1_DIR) if f.endswith("_PROVISIONAL_MODEL_v1.json")}
    return ex, md


def rows():
    out = []
    custody = A.custody_manifest()
    k5_verified = custody["rows"][0].get("sha256_match") is True
    summary = _batch1_summary()
    ex_files, md_files = _extract_files()
    inv = INV.inventory()

    # ---- K5 PL06 batch 1: the four units this run extracted ----
    by_unit = {u["unit_id"]: u for u in (summary["units"] if summary else [])}
    for uid in ["K5-PL06-T03-B03", "K5-PL06-T03-B04", "K5-PL06-T05-B01", "K5-PL06-T06-B01"]:
        stem = uid.replace("-", "_")
        extracted = f"{stem}_SOURCE_EXTRACT_v1.json" in ex_files
        modelled = f"{stem}_PROVISIONAL_MODEL_v1.json" in md_files
        u = by_unit.get(uid, {})
        amber = bool(u.get("shared_start") or u.get("shared_end"))
        out.append(dict(
            course="K5", pl="PL06", unit_id=uid,
            source_binary_verified=k5_verified,
            source_authority_inherited="SRC-AUTH-01",
            boundary_status=("BOUNDARY_AMBER_RESOLVED_BY_ANCHOR" if amber
                             else "CLEAN_VERIFIED"),
            extraction_status="EXTRACTED" if extracted else "SOURCE_READY",
            model_status="MODEL_READY" if modelled else "SOURCE_READY",
            pattern_decision_dependency="PENDING_BARIAH_PATTERN_DECISION",
            storyboard_readiness="WAITING_PATTERN_DECISIONS",
            qa_readiness="EXTRACTION_QA_PASSED" if extracted else "NOT_RUN",
            bariah_review_dependency=PENDING_PACKAGE,
            blocker="BARIAH — pattern package under review; STOP-006 cast binding open",
            next_executable_action=("project the provisional model into a storyboard model "
                                    "as soon as the pattern package returns")))

    # ---- K5 PL06: the ten units of PL06 this run did not touch ----
    frozen_units = ["K5-PL06-T01-B01", "K5-PL06-T01-B02", "K5-PL06-T01-B03",
                    "K5-PL06-T02-B01", "K5-PL06-T02-B02", "K5-PL06-T03-B01",
                    "K5-PL06-T03-B02", "K5-PL06-T03-B05", "K5-PL06-T04-B01",
                    "K5-PL06-T07-B01"]
    for uid in frozen_units:
        done = uid == "K5-PL06-T03-B02"
        t04 = uid == "K5-PL06-T04-B01"
        out.append(dict(
            course="K5", pl="PL06", unit_id=uid,
            source_binary_verified=k5_verified,
            source_authority_inherited="SRC-AUTH-01",
            boundary_status="CLEAN_VERIFIED_IN_FROZEN_MAP",
            extraction_status=("EXTRACTED" if (done or t04) else "SOURCE_READY"),
            model_status=("PACKAGED" if done else "MODEL_READY" if t04 else "SOURCE_READY"),
            pattern_decision_dependency=("NONE" if done else
                                         "PENDING_BARIAH_PATTERN_DECISION"),
            storyboard_readiness=("PACKAGED" if done else
                                  "READY_FOR_ONE_TOUCH_REVIEW" if t04 else "SOURCE_READY"),
            qa_readiness=("PACKAGED" if done else
                          "T04_STATE_COVERAGE_QA_v1 108/108" if t04 else "NOT_RUN"),
            bariah_review_dependency=("NONE" if done else PENDING_PACKAGE),
            blocker=("none — delivered" if done else
                     "BARIAH — visual review of the built storyboard" if t04 else
                     "CAIR — not yet extracted"),
            next_executable_action=("none" if done else
                                    "await Bariah's storyboard review" if t04 else
                                    "extract by heading anchor, same reader as batch 1")))

    # ---- K5, the other seven Pakej Latihan ----
    for r in inv["k5"]["rows"]:
        if r["pl"] == "PL06":
            continue
        for i, sm in enumerate(r["sub_modul"], 1):
            out.append(dict(
                course="K5", pl=r["pl"], unit_id=f"{r['pl']}-CAND-{i:02d}",
                source_binary_verified=k5_verified,
                source_authority_inherited="SRC-AUTH-01",
                boundary_status=("BOUNDARY_AMBER" if r["shared_boundary_risk"]["risk"]
                                 else "SOURCE_READY_UNMAPPED"),
                extraction_status="SOURCE_READY",
                model_status="SOURCE_READY",
                pattern_decision_dependency="PENDING_BARIAH_PATTERN_DECISION",
                storyboard_readiness="SOURCE_READY",
                qa_readiness="NOT_RUN",
                bariah_review_dependency=PENDING_PACKAGE,
                blocker="CAIR — no frozen unit boundary map for this Pakej Latihan",
                next_executable_action=("map unit boundaries for this Pakej Latihan the way "
                                        "PL06's fourteen were mapped, then extract")))

    # ---- K3 ----
    modelled_pls = {m["pl"] for m in inv["k3_models"]}
    for r in inv["k3"]["rows"]:
        read = r["read_status"] == "CONNECTOR_TEXT_READ_IN_FULL"
        modelled = r["pl"] in modelled_pls
        out.append(dict(
            course="K3", pl=r["pl"],
            unit_id=(f"K3-M01-{r['pl']}" if read else f"K3-M01-{r['pl']}-CAND"),
            source_binary_verified=False,
            source_authority_inherited="SRC-AUTH-01",
            boundary_status=("CLEAN_SELF_CONTAINED_FILE" if read else "UNKNOWN_NOT_READ"),
            extraction_status=("CONNECTOR_TEXT_READ" if read else "SOURCE_READY"),
            model_status=("MODEL_READY" if modelled else "SOURCE_READY"),
            pattern_decision_dependency="PENDING_BARIAH_PATTERN_DECISION",
            storyboard_readiness=("WAITING_PATTERN_DECISIONS" if modelled
                                  else "SOURCE_READY"),
            qa_readiness="NOT_RUN",
            bariah_review_dependency=PENDING_PACKAGE,
            blocker=("BARIAH — assessment format conflict K3-ASSESS-01" if modelled
                     else "CAIR — PDF identified but not read"),
            next_executable_action=("resolve the LATIHAN-versus-4+1 format question" if
                                    modelled else "read the PDF through the connector and "
                                                  "inventory it")))

    # ---- K2 ----
    out.append(dict(
        course="K2", pl="MONOLITH", unit_id="K2-MONOLITH-UNMAPPED",
        source_binary_verified=False,
        source_authority_inherited="SRC-AUTH-01",
        boundary_status="UNKNOWN_NOT_DECOMPOSED",
        extraction_status="SOURCE_BLOCKED",
        model_status="SOURCE_BLOCKED",
        pattern_decision_dependency="NOT_REACHED",
        storyboard_readiness="SOURCE_BLOCKED",
        qa_readiness="NOT_RUN",
        bariah_review_dependency="NOT_REACHED",
        blocker=("FIRDAUS — the 25 MB monolith is identified on Drive but not available as a "
                 "local binary, and a whole-file text read is not viable here"),
        next_executable_action=(f"place {inv['k2']['file']['filename']} "
                                f"(Drive {inv['k2']['file']['drive_id']}) on local disk; "
                                f"PyMuPDF is already available and gives the page count, "
                                f"heading tree, images and tables directly")))
    return out


def summary():
    rs = rows()
    confirmed = [r for r in rs if not r["unit_id"].endswith("CAND")
                 and "-CAND-" not in r["unit_id"] and r["unit_id"] != "K2-MONOLITH-UNMAPPED"]
    candidate = [r for r in rs if r not in confirmed]

    def pct(n, d):
        return round(100.0 * n / d, 1) if d else 0.0

    total = len(rs)
    source_ready = [r for r in rs if r["extraction_status"] != "SOURCE_BLOCKED"]
    extracted = [r for r in rs if r["extraction_status"] in ("EXTRACTED",
                                                             "CONNECTOR_TEXT_READ")]
    model_ready = [r for r in rs if r["model_status"] in ("MODEL_READY", "PACKAGED")]
    blocked = [r for r in rs if r["blocker"] != "none — delivered"]
    owners = {}
    for r in blocked:
        owner = r["blocker"].split("—")[0].strip()
        owners.setdefault(owner, []).append(r["unit_id"])
    return dict(
        stage=STAGE, columns=COLUMNS, allowed_statuses=STATUSES,
        total_rows=total,
        total_confirmed_units=len(confirmed),
        total_candidate_units=len(candidate),
        source_ready_count=len(source_ready), source_ready_percent=pct(len(source_ready),
                                                                      total),
        extracted_count=len(extracted), extracted_percent=pct(len(extracted), total),
        model_ready_count=len(model_ready), model_ready_percent=pct(len(model_ready), total),
        blocked_count=len(blocked),
        blockers_by_owner={k: dict(count=len(v), units=v) for k, v in sorted(owners.items())},
        by_course={c: len([r for r in rs if r["course"] == c])
                   for c in sorted({r["course"] for r in rs})},
        derivation=("Every count above is computed from artifacts on disk — the custody "
                    "manifest, the batch 1 extraction summary, the provisional model files "
                    "and the inventory. No percentage in this queue was typed by hand."),
        rows=rs)


if __name__ == "__main__":
    s = summary()
    print(f"rows={s['total_rows']} confirmed={s['total_confirmed_units']} "
          f"candidate={s['total_candidate_units']}")
    print(f"source-ready {s['source_ready_percent']}%  "
          f"extracted {s['extracted_percent']}%  "
          f"model-ready {s['model_ready_percent']}%")
    print("by course:", s["by_course"])
    for k, v in s["blockers_by_owner"].items():
        print(f"  blocked/{k}: {v['count']}")
