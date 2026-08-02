# -*- coding: utf-8 -*-
"""Stage 4.2F-A QA — gates over the PL06 scale-out inventory.

Every gate record carries an EXPLICIT typed `gate_type`. Nothing here infers a gate's kind
from a substring in its ID, because that is precisely how the v0.4.4 supersession-marker
count came out six short: `SUPERSEDED` in a gate ID matched six ordinary live tests.

    python3 docs/pl06/tools/pl06_inventory_qa_v1.py
"""
import csv, hashlib, io, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(DOCS))
sys.path.insert(0, HERE)
import pl06_inventory_data_v1 as D
import pl06_emit_v1 as EMIT

# Typed gate kinds. A gate declares its kind; the ID is a label, never a classifier.
INVENTORY_INTEGRITY = "INVENTORY_INTEGRITY"
AUTHORITY_DISCIPLINE = "AUTHORITY_DISCIPLINE"
RULE_PORTABILITY = "RULE_PORTABILITY"
SELECTION_INTEGRITY = "SELECTION_INTEGRITY"
STOP_CONDITION = "STOP_CONDITION"
ARTIFACT_AGREEMENT = "ARTIFACT_AGREEMENT"
PLAN_INTEGRITY = "PLAN_INTEGRITY"
SUPERSESSION_MARKER = "SUPERSESSION_MARKER"
ACCOUNTING = "ACCOUNTING"
SOURCE_CUSTODY = "SOURCE_CUSTODY"
BOUNDARY_INTEGRITY = "BOUNDARY_INTEGRITY"

REQUIRED_DELIVERABLES = [
    "PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.md",
    "PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.csv",
    "PL06_RULE_PORTABILITY_MATRIX_v1.md",
    "PL06_CAPABILITY_COVERAGE_MATRIX_v1.md",
    "PL06_FIRST_SCALE_OUT_SELECTION_v1.md",
    "PL06_EXECUTION_PLAN_v1.md",
    "PL06_OPEN_AUTHORITY_ITEMS_v1.md",
    "B02_BARIAH_CALL_APPROVAL_RECORD_v1.md",
]

# Authority classes ordered weakest to strongest. Inflation is any claim that a unit's
# authority exceeds what its cited evidence class supports.
AUTHORITY_STRENGTH = {
    "FIRDAUS_ATTESTED_BARIAH_CALL": 1,
    "MEASURED_FACT": 2,
    "BARIAH_SUPPLIED_UPSTREAM_ARTIFACT": 2,
    "SOURCE_ATTESTED_EXTRACT": 3,
    "CONSOLIDATED_EXECUTABLE_SG": 3,
    "RATIFIED_ARCHITECTURE_DECISION": 4,
    "RATIFIED_CHARACTER_BANK": 4,
    "DELIVERED_REVIEW_CANDIDATE": 3,
    "BARIAH_DIRECT_WRITTEN_CONFIRMATION": 5,
    "BARIAH_DIRECT_SCREENSHOT": 5,
    # Stage 4.2F-A2. The module source itself ranks with the other source-attested extracts.
    "PROOFREAD_FINAL_MODULE_SOURCE": 3,
    # Deliberately WEAKER than the source it derives from: the boundaries are anchored to named
    # body headings, but the lesson grouping they express rests on an artifact nobody holds
    # (GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN). A unit may not claim more than this.
    "DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING": 2,
}

# A unit may only be called fully complete if it has every one of these.
COMPLETENESS_FIELDS = ["controlled_content_available", "storyboard_input_available",
                       "rumusan_available", "quiz_mcq_available", "quiz_mr_available"]

FULLY_COMPLETE_READINESS = {"READY"}


def run():
    res = []

    def chk(gate_id, gate_type, value, expected):
        res.append(dict(gate_id=gate_id, gate_type=gate_type, value=value,
                        expected=expected, ok=value == expected))

    U = D.UNITS
    ids = [u["unit_id"] for u in U]

    # ==================== 1. INVENTORY INTEGRITY ====================
    chk("INVENTORY_UNITS_EVALUATED", INVENTORY_INTEGRITY, len(U) > 0, True)
    chk("UNITS_WITHOUT_SOURCE_REFERENCE", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U if not str(u.get("source_reference") or "").strip()], [])
    chk("UNITS_WITHOUT_EVIDENCE_REF_IN_SOURCE_REFERENCE", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U
         if not any(u["source_reference"].startswith(e["ref"] + " ") for e in D.EVIDENCE)], [])
    chk("DUPLICATE_UNIT_IDS", INVENTORY_INTEGRITY,
        sorted({i for i in ids if ids.count(i) > 1}), [])
    tb = [(u["topik_number"], u["bahagian_number"]) for u in U]
    chk("DUPLICATE_TOPIK_BAHAGIAN_COMBINATIONS", INVENTORY_INTEGRITY,
        sorted({f"T{t}/B{b}" for t, b in tb if tb.count((t, b)) > 1}), [])
    chk("INVALID_READINESS_VALUES", INVENTORY_INTEGRITY,
        sorted({u["readiness_status"] for u in U
                if u["readiness_status"] not in D.READINESS_VALUES}), [])
    chk("INVALID_LANE_VALUES", INVENTORY_INTEGRITY,
        sorted({u["lane"] for u in U if u["lane"] not in D.LANE_VALUES}), [])
    chk("INVALID_UNIT_SCOPE_VALUES", INVENTORY_INTEGRITY,
        sorted({u["unit_scope"] for u in U
                if u["unit_scope"] not in D.UNIT_SCOPE_VALUES}), [])
    chk("UNITS_MISSING_A_CSV_FIELD", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U if any(c not in u for c in D.CSV_COLUMNS)], [])
    chk("ALL_SEVEN_TOPIK_REPRESENTED", INVENTORY_INTEGRITY,
        sorted({u["topik_number"] for u in U}), [1, 2, 3, 4, 5, 6, 7])

    # A unit that names a Bahagian number must also name its title, and vice versa.
    chk("BAHAGIAN_NUMBER_WITHOUT_TITLE", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U
         if (u["bahagian_number"] is not None) != bool(u["bahagian_title"])], [])
    # No Bahagian may be numbered unless a source establishes that boundary. Until Stage
    # 4.2F-A2 the only qualifying attestation was FULL_UNIT_CONTENT, because the montage
    # enumerated Topik and nothing else. The frozen boundary map now attests every unit's
    # boundary by named DOCX heading anchor, so that attestation qualifies too — and nothing
    # weaker does.
    BOUNDARY_ATTESTATIONS = {"FULL_UNIT_CONTENT", "UNIT_BOUNDARY_AND_PAGE_RANGE"}
    chk("BAHAGIAN_NUMBERS_INVENTED", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U if u["bahagian_number"] is not None
         and u["source_attests"] not in BOUNDARY_ATTESTATIONS], [])

    # ==================== 2. READINESS DISCIPLINE ====================
    blocking = [c["id"] for c in D.STOP_CONDITIONS if c["scope"] == "BLOCKS_THIS_UNIT"]
    blocking_conditions = {c["condition"] for c in D.STOP_CONDITIONS
                           if c["scope"] == "BLOCKS_THIS_UNIT"}
    chk("BLOCKING_STOP_CONDITIONS_EVALUATED", STOP_CONDITION, len(blocking) > 0, True)
    chk("READY_UNIT_WITH_UNRESOLVED_BLOCKING_SOURCE", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U if u["readiness_status"] == "READY"
         and any(b in blocking_conditions for b in u["blocking_conditions"])], [])
    # Matched one literal until Stage 4.2F-A2 renamed it, at which point the gate silently
    # stopped covering anything — fixture N-06 caught that. Now it matches the PREFIX, so a
    # future rename of the reason cannot switch the gate off again.
    chk("UNSUPPORTED_INTERACTION_CLASSIFIED_READY", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U
         if u["readiness_status"] in ("READY", "READY_WITH_HOLDS")
         and str(u["interaction_pattern_candidate"]).startswith("NOT_DETERMINABLE")], [])
    chk("UNIT_WITHOUT_RUMUSAN_MARKED_FULLY_COMPLETE", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U
         if u["readiness_status"] in FULLY_COMPLETE_READINESS and not u["rumusan_available"]], [])
    chk("UNIT_WITHOUT_QUIZ_SOURCE_MARKED_FULLY_COMPLETE", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U if u["readiness_status"] in FULLY_COMPLETE_READINESS
         and not (u["quiz_mcq_available"] and u["quiz_mr_available"])], [])
    chk("LANE_D_UNIT_NOT_MARKED_SOURCE_BLOCKED", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U if u["lane"] == "LANE_D_SOURCE_INCOMPLETE"
         and u["readiness_status"] not in ("SOURCE_INCOMPLETE",
                                           "SOURCE_AUTHORITY_UNRESOLVED")], [])
    # Was pinned to source_document == "NONE_IN_CUSTODY", a population that emptied the moment
    # the module arrived — the gate went vacuous and fixture N-12 caught it. Re-pinned to the
    # thing that actually matters now: having the source document is not having read it.
    chk("UNIT_CLAIMING_CONTENT_WITHOUT_SOURCE_DOCUMENT", INVENTORY_INTEGRITY,
        [u["unit_id"] for u in U
         if not u["controlled_content_available"]
         and any(u[f] for f in COMPLETENESS_FIELDS if f != "controlled_content_available")], [])

    # ==================== 3. AUTHORITY DISCIPLINE ====================
    chk("EVIDENCE_REGISTER_EVALUATED", AUTHORITY_DISCIPLINE, len(D.EVIDENCE) > 0, True)
    chk("UNKNOWN_AUTHORITY_CLASSES", AUTHORITY_DISCIPLINE,
        sorted({e["authority_class"] for e in D.EVIDENCE
                if e["authority_class"] not in AUTHORITY_STRENGTH}), [])
    chk("UNIT_AUTHORITY_CLASSES_KNOWN", AUTHORITY_DISCIPLINE,
        sorted({u["source_authority_class"] for u in U
                if u["source_authority_class"] not in AUTHORITY_STRENGTH}), [])
    # Inflation: a unit claiming authority stronger than the evidence entry it cites.
    ev_by_ref = {e["ref"]: e for e in D.EVIDENCE}
    inflated = []
    for u in U:
        ref = u["source_reference"].split(" ")[0]
        e = ev_by_ref.get(ref)
        if e and AUTHORITY_STRENGTH.get(u["source_authority_class"], 99) > \
                AUTHORITY_STRENGTH.get(e["authority_class"], 0):
            inflated.append(u["unit_id"])
    chk("AUTHORITY_CLASS_INFLATION", AUTHORITY_DISCIPLINE, inflated, [])
    # The call approval must never be dressed up as direct evidence.
    A = D.APPROVAL_RECORD
    chk("CALL_APPROVAL_AUTHORITY_CLASS", AUTHORITY_DISCIPLINE,
        A["authority_class"], "FIRDAUS_ATTESTED_BARIAH_CALL")
    chk("CALL_APPROVAL_NOT_CLASSIFIED_AS_DIRECT", AUTHORITY_DISCIPLINE,
        [f for f in A["forbidden_classifications"] if f == A["authority_class"]], [])
    chk("CALL_APPROVAL_WRITTEN_CONFIRMATION_PENDING", AUTHORITY_DISCIPLINE,
        A["written_confirmation"], "PENDING")
    chk("CALL_APPROVAL_DOES_NOT_AUTHORISE_FREEZE", AUTHORITY_DISCIPLINE,
        all(any(k in m for k in ("canonical freeze", "MMD readiness", "production release"))
            is not None for m in A["may_not_authorise"])
        and any("canonical freeze" in m for m in A["may_not_authorise"]), True)
    # No unit may be attributed to Bariah directly unless its cited evidence IS direct.
    direct = {"BARIAH_DIRECT_WRITTEN_CONFIRMATION", "BARIAH_DIRECT_SCREENSHOT"}
    bad_direct = []
    for u in U:
        if u["source_authority_class"] in direct:
            e = ev_by_ref.get(u["source_reference"].split(" ")[0])
            if not e or e["authority_class"] not in direct:
                bad_direct.append(u["unit_id"])
    chk("SOURCE_DERIVED_SUBJECT_LABELLED_BARIAH_DIRECT", AUTHORITY_DISCIPLINE, bad_direct, [])
    # A unit whose evidence attests existence only must not claim content.
    # Attestation classes that establish WHERE a unit is but say nothing about WHAT is in it.
    # A unit resting on one of these may not report source rows or assets: those come from
    # reading the content, which has not happened.
    NON_CONTENT_ATTESTATIONS = ("TOPIK_EXISTENCE_AND_TITLE_ONLY",
                                "EXISTENCE_ONLY — no number, no title, no page range was given",
                                "UNIT_BOUNDARY_AND_PAGE_RANGE")
    chk("EXISTENCE_ONLY_EVIDENCE_CLAIMING_CONTENT", AUTHORITY_DISCIPLINE,
        [u["unit_id"] for u in U
         if u["source_attests"] in NON_CONTENT_ATTESTATIONS
         and (u["source_rows_count"] or u["source_assets_count"])], [])

    # ==================== 4. RULE PORTABILITY ====================
    chk("RULES_EVALUATED", RULE_PORTABILITY, len(D.RULES) > 0, True)
    rids = [r["rule_id"] for r in D.RULES]
    chk("DUPLICATE_RULE_IDS", RULE_PORTABILITY, sorted({r for r in rids if rids.count(r) > 1}), [])
    chk("INVALID_PORTABILITY_CLASSES", RULE_PORTABILITY,
        sorted({r["portability_class"] for r in D.RULES
                if r["portability_class"] not in D.PORTABILITY_CLASSES}), [])
    chk("RULES_WITHOUT_EVIDENCE", RULE_PORTABILITY,
        [r["rule_id"] for r in D.RULES if not str(r["evidence"]).strip()], [])
    # The mandatory B02-specific list from the stage brief. Each must be present and LOCAL.
    MANDATORY_LOCAL = {
        "Family S": "RP-201", "Family P1": "RP-202", "Family P2": "RP-203",
        "B02 component names": "RP-204", "B02 component cardinalities": "RP-205",
        "Papan Tanda ruling": "RP-206", "BBQ Pit ruling": "RP-207",
        "B02 source rows": "RP-208", "B02 visual subjects": "RP-209",
        "B02 learner-screen counts": "RP-210", "B02 runtime-state counts": "RP-211",
        "B02 interaction-item counts": "RP-212", "B02-specific text and factual claims": "RP-213",
    }
    by_id = {r["rule_id"]: r for r in D.RULES}
    chk("MANDATORY_B02_SPECIFIC_RULES_PRESENT", RULE_PORTABILITY,
        sorted(k for k, v in MANDATORY_LOCAL.items() if v not in by_id), [])
    chk("B02_SPECIFIC_RULE_PROMOTED_GLOBALLY", RULE_PORTABILITY,
        sorted(v for v in MANDATORY_LOCAL.values()
               if by_id.get(v, {}).get("portability_class") != "B02_SPECIFIC_DO_NOT_PROPAGATE"),
        [])
    # A global rule whose destination scope is not every unit is misclassified.
    chk("GLOBAL_RULE_WITH_NARROW_DESTINATION", RULE_PORTABILITY,
        [r["rule_id"] for r in D.RULES if r["portability_class"] == "PL06_GLOBAL_REUSABLE"
         and r["destination_scope"] != "ALL_PL06_UNITS"], [])
    # A B02-specific rule must never be scoped beyond B02.
    chk("B02_SPECIFIC_RULE_WITH_WIDE_DESTINATION", RULE_PORTABILITY,
        [r["rule_id"] for r in D.RULES
         if r["portability_class"] == "B02_SPECIFIC_DO_NOT_PROPAGATE"
         and not r["destination_scope"].startswith("K5-PL06-T03-B02")], [])
    # A rule with no automated oracle must say a human is required.
    chk("UNORACLED_RULE_WITHOUT_HUMAN_AUTHORITY", RULE_PORTABILITY,
        [r["rule_id"] for r in D.RULES if not r["automated_oracle_available"]
         and r["human_authority_required"] in (None, "", "NONE", "N/A")], [])

    # ==================== 5. SELECTION INTEGRITY ====================
    S = D.SELECTION
    chk("SELECTED_PROOF_UNIT_PRESENT_IN_INVENTORY", SELECTION_INTEGRITY,
        S["selected_unit_id"] in ids, True)
    sel = next((u for u in U if u["unit_id"] == S["selected_unit_id"]), None)
    chk("SELECTED_PROOF_UNIT_IS_NOT_B02", SELECTION_INTEGRITY,
        S["selected_unit_id"] != "K5-PL06-T03-B02", True)
    sel_blocked = bool(sel and [b for b in sel["blocking_conditions"] if b in blocking_conditions])
    chk("SELECTED_PROOF_UNIT_BLOCKING_CONDITIONS", SELECTION_INTEGRITY, sel_blocked, True)
    # If the selected unit is blocked, the selection MUST be conditional and say so.
    chk("BLOCKED_SELECTION_DECLARED_UNCONDITIONAL", SELECTION_INTEGRITY,
        sel_blocked and S["selection_is_unconditional"], False)
    chk("BLOCKED_SELECTION_WITHOUT_PRECONDITIONS", SELECTION_INTEGRITY,
        sel_blocked and not S["required_preconditions"], False)
    # Assert the SHAPE, not one literal: a blocked selection must declare itself conditional
    # and say what it is pending. Hardcoding one string would have to be edited every time the
    # pending reason changes, and an edit is exactly where "SELECTED_READY" slips in.
    chk("SELECTION_STATUS_DECLARED", SELECTION_INTEGRITY,
        S["selection_status"].startswith("SELECTED_CONDITIONAL_PENDING_"), True)
    chk("SELECTION_STATUS_VALUE", SELECTION_INTEGRITY,
        S["selection_status"], "SELECTED_CONDITIONAL_PENDING_CONTENT_EXTRACTION")
    chk("REJECTED_CANDIDATES_RECORDED", SELECTION_INTEGRITY, len(S["rejected"]) > 0, True)
    chk("REJECTED_CANDIDATES_NOT_IN_INVENTORY", SELECTION_INTEGRITY,
        [r["unit_id"] for r in S["rejected"] if r["unit_id"] not in ids], [])
    chk("SCORED_CANDIDATES_NOT_IN_INVENTORY", SELECTION_INTEGRITY,
        [c["unit_id"] for c in D.CANDIDATE_SCORES if c["unit_id"] not in ids], [])
    chk("CANDIDATE_SCORES_OUT_OF_RANGE", SELECTION_INTEGRITY,
        [c["unit_id"] for c in D.CANDIDATE_SCORES
         if any(not (0 <= v <= 5) for v in c["scores"].values())], [])
    chk("CANDIDATE_SCORES_MISSING_A_CRITERION", SELECTION_INTEGRITY,
        [c["unit_id"] for c in D.CANDIDATE_SCORES
         if sorted(c["scores"]) != sorted(D.SELECTION_CRITERIA)], [])
    # A candidate with zero source completeness must not be scored above zero on the
    # things that depend on reading the source.
    # Was gated on source_completeness == 0, which stopped selecting anything once the module
    # arrived. The real invariant is stronger and survives the ingest: a candidate whose
    # CONTENT has not been extracted cannot be scored on anything that requires reading it,
    # however good its source custody now is.
    _by_id = {u["unit_id"]: u for u in U}
    chk("SOURCELESS_CANDIDATE_SCORED_ON_CONTENT", SELECTION_INTEGRITY,
        [c["unit_id"] for c in D.CANDIDATE_SCORES
         if not _by_id.get(c["unit_id"], {}).get("controlled_content_available")
         and any(c["scores"][k] > 0 for k in ("visual_availability", "quiz_completeness",
                                              "interaction_representativeness"))], [])

    # ==================== 6. PLAN INTEGRITY ====================
    chk("PLAN_ROWS_EVALUATED", PLAN_INTEGRITY, len(D.PLAN_ROWS) > 0, True)
    chk("EXECUTION_ORDER_UNIT_ABSENT_FROM_INVENTORY", PLAN_INTEGRITY,
        [r["unit_id"] for r in D.PLAN_ROWS if r["unit_id"] not in ids], [])
    chk("WAVE_UNIT_ABSENT_FROM_INVENTORY", PLAN_INTEGRITY,
        [u for w in D.WAVES for u in w["units"] if u not in ids], [])
    chk("PLAN_ROWS_COVER_EVERY_REMAINING_UNIT", PLAN_INTEGRITY,
        sorted(u["unit_id"] for u in U if u["unit_scope"] == "REMAINING"),
        sorted(r["unit_id"] for r in D.PLAN_ROWS))
    chk("WAVE_0_UNIT_IS_THE_SELECTION", PLAN_INTEGRITY,
        D.WAVES[0]["units"], [S["selected_unit_id"]])
    chk("DUPLICATE_EXECUTION_ORDER", PLAN_INTEGRITY,
        sorted({u["recommended_execution_order"] for u in U
                if [x["recommended_execution_order"] for x in U].count(
                    u["recommended_execution_order"]) > 1}), [])
    # Any duration that is not measured must be declared NOT_EVIDENCED, never guessed.
    measured = {m["metric"]: m["value"] for m in D.MEASURED_BASIS}
    chk("MEASURED_BASIS_RECORDED", PLAN_INTEGRITY, len(measured) > 0, True)
    chk("PLAN_DURATION_WITHOUT_BASIS", PLAN_INTEGRITY,
        [f"{r['unit_id']}/{k}" for r in D.PLAN_ROWS
         for k in ("source_extraction", "controlled_model", "generation", "automated_qa",
                   "rendered_inspection", "powerpoint_smoke", "bariah_review")
         if r["unit_id"] != S["selected_unit_id"] and r[k] != "NOT_EVIDENCED"], [])
    chk("POWERPOINT_SMOKE_ESTIMATED_WITHOUT_EVIDENCE", PLAN_INTEGRITY,
        [r["unit_id"] for r in D.PLAN_ROWS if r["powerpoint_smoke"] != "NOT_EVIDENCED"], [])

    # ==================== 7. STOP CONDITIONS ====================
    chk("INVALID_STOP_SCOPES", STOP_CONDITION,
        sorted({c["scope"] for c in D.STOP_CONDITIONS if c["scope"] not in D.STOP_SCOPES}), [])
    sids = [c["id"] for c in D.STOP_CONDITIONS]
    chk("DUPLICATE_STOP_IDS", STOP_CONDITION, sorted({i for i in sids if sids.count(i) > 1}), [])
    chk("STOP_APPLIES_TO_UNKNOWN_UNIT", STOP_CONDITION,
        sorted({u for c in D.STOP_CONDITIONS for u in c["applies_to"]
                if u != "ALL" and u not in ids}), [])
    chk("STOP_CONDITION_WITHOUT_RESOLVER", STOP_CONDITION,
        [c["id"] for c in D.STOP_CONDITIONS if not str(c["resolver"]).strip()], [])
    # A global open item must not be scoped as blocking an unrelated unit.
    chk("GLOBAL_ITEM_BLOCKING_UNRELATED_UNIT", STOP_CONDITION,
        [c["id"] for c in D.STOP_CONDITIONS
         if c["applies_to"] == ["ALL"] and c["scope"] == "BLOCKS_THIS_UNIT"], [])
    # Every blocking condition named on a unit must exist in the stop register.
    known = {c["condition"] for c in D.STOP_CONDITIONS} | {
        "MS2680_VERIFICATION", "B02_CAIR_INT_001", "LMS_NAVIGATION_RULING",
        "POWERPOINT_SMOKE_NOT_RECORDED", "NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY",
        "BAHAGIAN_BOUNDARY_UNRESOLVED", "NO_RUMUSAN_SOURCE", "NO_QUIZ_SOURCE",
        "CAST_BINDING_UNRESOLVED"}
    chk("UNIT_BLOCKER_NOT_IN_STOP_REGISTER", STOP_CONDITION,
        sorted({b for u in U for b in u["blocking_conditions"] if b not in known}), [])

    # ==================== 8. ARTIFACT AGREEMENT ====================
    for name in REQUIRED_DELIVERABLES:
        p = os.path.join(DOCS, name)
        chk(f"DELIVERABLE_PRESENT::{name}", ARTIFACT_AGREEMENT, os.path.exists(p), True)
    # The Markdown and CSV inventories must agree, field for field, unit for unit.
    csv_path = os.path.join(DOCS, "PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.csv")
    md_path = os.path.join(DOCS, "PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.md")
    divergence = []
    if os.path.exists(csv_path):
        rows = list(csv.DictReader(io.StringIO(open(csv_path, encoding="utf-8").read())))
        chk("CSV_ROW_COUNT_EQUALS_INVENTORY", ARTIFACT_AGREEMENT, len(rows), len(U))
        for u, r in zip(U, rows):
            for c in D.CSV_COLUMNS:
                if r.get(c, "") != EMIT._cell(u[c]):
                    divergence.append(f"{u['unit_id']}/{c}")
    else:
        divergence.append("CSV_ABSENT")
    chk("MARKDOWN_CSV_INVENTORY_DIVERGENCE", ARTIFACT_AGREEMENT, divergence, [])
    # Every unit id must appear in the Markdown inventory too.
    md = open(md_path, encoding="utf-8").read() if os.path.exists(md_path) else ""
    chk("UNIT_ABSENT_FROM_MARKDOWN_INVENTORY", ARTIFACT_AGREEMENT,
        [i for i in ids if i not in md], [])
    # The emitted files must be current with the controlled data source.
    stale = []
    for name, fn in EMIT.FILES:
        p = os.path.join(DOCS, name)
        if not os.path.exists(p):
            stale.append(name); continue
        body = fn()
        if not body.endswith("\n"):
            body += "\n"
        if open(p, encoding="utf-8").read() != body:
            stale.append(name)
    chk("EMITTED_DELIVERABLES_STALE", ARTIFACT_AGREEMENT, stale, [])
    # The verdict must be one of the three allowed and none of the four forbidden.
    chk("VERDICT_IS_ALLOWED", ARTIFACT_AGREEMENT,
        D.VERDICT in ("PL06_SCALE_OUT_INVENTORY_COMPLETE_READY_FOR_FIRST_NON_B02_PROOF",
                      "PL06_SCALE_OUT_BLOCKED_BY_SOURCE_INVENTORY_GAPS",
                      "PL06_SCALE_OUT_BLOCKED_BY_UNRESOLVED_UNIT_BOUNDARIES",
                      "PL06_SOURCE_BOUNDARY_INGEST_COMPLETE_READY_FOR_T04_EXTRACTION",
                      "PL06_SOURCE_BOUNDARY_INGEST_BLOCKED"), True)
    chk("FORBIDDEN_VERDICT_CLAIMED", ARTIFACT_AGREEMENT,
        [v for v in D.FORBIDDEN_VERDICTS if v == D.VERDICT], [])
    # A COMPLETE verdict requires no unit to be blocked on source.
    # A verdict claiming the source boundary ingest is complete may not coexist with a unit
    # whose SOURCE AUTHORITY is still unresolved. Units blocked on CONTENT extraction are
    # compatible with it — that is precisely what the ingest left open.
    unresolved_authority = [u["unit_id"] for u in U
                            if u["readiness_status"] == "SOURCE_AUTHORITY_UNRESOLVED"]
    chk("INGEST_COMPLETE_VERDICT_WITH_UNRESOLVED_SOURCE_AUTHORITY", ARTIFACT_AGREEMENT,
        D.VERDICT.startswith("PL06_SOURCE_BOUNDARY_INGEST_COMPLETE")
        and bool(unresolved_authority), False)
    unresolved = [u["unit_id"] for u in U
                  if u["readiness_status"] in ("SOURCE_INCOMPLETE",
                                               "SOURCE_AUTHORITY_UNRESOLVED")]
    chk("COMPLETE_VERDICT_WITH_UNRESOLVED_UNITS", ARTIFACT_AGREEMENT,
        D.VERDICT.endswith("READY_FOR_FIRST_NON_B02_PROOF") and bool(unresolved), False)

    # ==================== 9. SOURCE INGEST — STAGE 4.2F-A2 ====================
    FREEZE = os.path.join(DOCS, "source-freeze")
    chk("SOURCE_FREEZE_DIRECTORY_PRESENT", ARTIFACT_AGREEMENT, os.path.isdir(FREEZE), True)
    man_p = os.path.join(FREEZE, "FREEZE_MANIFEST.json")
    sums_p = os.path.join(FREEZE, "SHA256SUMS.txt")
    man = {a["path"]: a for a in json.load(open(man_p, encoding="utf-8"))["artifacts"]} \
        if os.path.exists(man_p) else {}
    sums = {}
    if os.path.exists(sums_p):
        for ln in open(sums_p, encoding="utf-8"):
            if ln.strip():
                h, pth = ln.rstrip("\n").split("  ", 1)
                sums[pth] = h
    chk("FREEZE_MANIFEST_ARTIFACTS", SOURCE_CUSTODY, len(man), 29)
    chk("FREEZE_HASH_REGISTER_LINES", SOURCE_CUSTODY, len(sums), 30)
    # Every ingested file must still hash to what the freeze says it is.
    mismatched, missing = [], []
    for dest, orig in D.INGESTED_FILES:
        fp = os.path.join(FREEZE, dest)
        if not os.path.exists(fp):
            missing.append(dest); continue
        h = hashlib.sha256(open(fp, "rb").read()).hexdigest()
        n = os.path.getsize(fp)
        if orig is None:
            continue                                    # the register cannot self-hash
        if orig in man and (man[orig]["sha256"] != h or man[orig]["bytes"] != n):
            mismatched.append(f"{dest}:manifest")
        if sums.get(orig) != h:
            mismatched.append(f"{dest}:sums")
    chk("INGESTED_FILES_EVALUATED", SOURCE_CUSTODY, len(D.INGESTED_FILES), 13)
    chk("INGESTED_FILES_MISSING", SOURCE_CUSTODY, missing, [])
    chk("INGESTED_FILES_MATCH_FREEZE_HASHES", SOURCE_CUSTODY, mismatched, [])
    chk("T04_BOUNDARY_EVIDENCE_IMAGES_PRESENT", SOURCE_CUSTODY,
        sorted(f for f in ("boundary_pages/p294.png", "boundary_pages/p302.png")
               if os.path.exists(os.path.join(FREEZE, f))),
        ["boundary_pages/p294.png", "boundary_pages/p302.png"])

    # Nothing oversized may enter the index, by decision.
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, timeout=60).stdout.split("\n")
    except Exception:
        tracked = []
    chk("GIT_INDEX_READ", SOURCE_CUSTODY, len(tracked) > 100, True)
    # A per-pattern gate disappears if its pattern is deleted, so deleting one would go
    # undetected — fixture N-47. Pin the guard list itself before iterating it.
    chk("FORBIDDEN_TRACKED_PATTERNS_COMPLETE", SOURCE_CUSTODY,
        sorted(t[0] for t in D.FORBIDDEN_TRACKED_PATTERNS),
        ["FULL_DOCX", "RENDERED_PDF", "TRANSPORT_ZIP"])
    for label, ext, needle in D.FORBIDDEN_TRACKED_PATTERNS:
        chk(f"FORBIDDEN_TRACKED_{label}", SOURCE_CUSTODY,
            [t for t in tracked if t.endswith(ext) and needle in t], [])
    chk("GIT_LFS_NOT_CONFIGURED", SOURCE_CUSTODY,
        os.path.exists(os.path.join(REPO, ".gitattributes")), False)
    chk("NO_INCOMING_RESIDUE_TRACKED", SOURCE_CUSTODY,
        [t for t in tracked if t.startswith("incoming/") or t.startswith("tmp/")], [])

    # ==================== 10. BOUNDARY MAP AND TOPOLOGY ====================
    rows = D.BOUNDARY_ROWS
    chk("BOUNDARY_MAP_LESSONS", BOUNDARY_INTEGRITY, len(rows), 14)
    chk("BOUNDARY_MAP_UNIQUE_UNIT_IDS", BOUNDARY_INTEGRITY,
        len({r["unit_id"] for r in rows}), 14)
    chk("INVENTORY_UNIT_COUNT", BOUNDARY_INTEGRITY, len(U), 14)
    chk("INVENTORY_UNIQUE_UNIT_IDS", BOUNDARY_INTEGRITY, len(set(ids)), 14)
    chk("PL06_TOPOLOGY", BOUNDARY_INTEGRITY,
        [D.TOPOLOGY[t] for t in sorted(D.TOPOLOGY)], [3, 2, 5, 1, 1, 1, 1])
    chk("COMPLETED_UNITS", BOUNDARY_INTEGRITY,
        [u["unit_id"] for u in U if u["unit_scope"] == "DELIVERED_BASELINE"],
        ["K5-PL06-T03-B02"])
    chk("REMAINING_UNITS", BOUNDARY_INTEGRITY,
        sum(1 for u in U if u["unit_scope"] == "REMAINING"), 13)
    # The Stage 4.2F-A error: B02's bahagian title was the Topik title.
    b02 = next(u for u in U if u["unit_id"] == "K5-PL06-T03-B02")
    chk("B02_BAHAGIAN_TITLE", BOUNDARY_INTEGRITY, b02["bahagian_title"],
        "Struktur Taman dan Perabot Taman")
    chk("B02_BAHAGIAN_TITLE_IS_NOT_TOPIK_TITLE", BOUNDARY_INTEGRITY,
        b02["bahagian_title"] == b02["topik_title"], False)
    chk("UNITS_WHOSE_BAHAGIAN_TITLE_EQUALS_TOPIK_TITLE", BOUNDARY_INTEGRITY,
        sorted(u["unit_id"] for u in U
               if u["bahagian_title"] == u["topik_title"] and u["topik_number"] in (1, 2, 3)), [])
    # T03-BNEXT is resolved and must no longer exist as a placeholder.
    chk("UNRESOLVED_PLACEHOLDER_UNITS", BOUNDARY_INTEGRITY,
        [i for i in ids if i.endswith("BNEXT") or i.endswith("UNRESOLVED")], [])
    t303 = next((u for u in U if u["unit_id"] == "K5-PL06-T03-B03"), None)
    chk("T03_B03_PRESENT", BOUNDARY_INTEGRITY, t303 is not None, True)
    chk("T03_B03_TITLE", BOUNDARY_INTEGRITY, t303 and t303["bahagian_title"], "Infrastruktur")
    chk("T03_B03_PAGE_RANGE", BOUNDARY_INTEGRITY,
        t303 and t303["source_page_range"].startswith("modul ms 250-255"), True)
    chk("UNITS_WITH_NULL_BAHAGIAN_NUMBER", BOUNDARY_INTEGRITY,
        [u["unit_id"] for u in U if u["bahagian_number"] is None], [])
    # T04 boundary, the selected proof.
    t4 = next(r for r in rows if r["unit_id"] == "K5-PL06-T04-B01")
    chk("T04_MODULE_PAGE_RANGE", BOUNDARY_INTEGRITY, t4["module_page_range"], "276-283")
    chk("T04_PDF_PAGE_RANGE", BOUNDARY_INTEGRITY, t4["pdf_page_range"], "294-301")
    chk("T04_START_ANCHOR_IS_BODY_STRING", BOUNDARY_INTEGRITY,
        t4["start_anchor"].startswith("4.0 PENJAAGAAN DAN PENYELENGGARAAN"), True)
    chk("T04_END_BEFORE_ANCHOR", BOUNDARY_INTEGRITY, t4["end_before"],
        "5.0 PENGURUSAN KUALITI PROJEK")
    chk("T04_BOUNDARY_IS_CLEAN", BOUNDARY_INTEGRITY,
        (t4["shared_start"], t4["shared_end"]), (False, False))
    chk("SHARED_BOUNDARY_PAGES", BOUNDARY_INTEGRITY, D.SHARED_BOUNDARY_PAGES,
        [181, 188, 215, 237, 250, 255])
    # Markdown / CSV / JSON agreement inside the frozen map itself.
    csv_p = os.path.join(FREEZE, "PL06_LESSON_BOUNDARY_MAP_v1.csv")
    md_p = os.path.join(FREEZE, "PL06_LESSON_BOUNDARY_MAP_v1.md")
    div = []
    if os.path.exists(csv_p):
        crows = list(csv.DictReader(open(csv_p, encoding="utf-8-sig")))
        for a, b in zip(rows, crows):
            for f in ("unit_id", "topik", "bahagian", "topik_title", "lesson_title",
                      "module_page_range", "pdf_page_range", "start_anchor", "end_before",
                      "docx_para_start", "docx_para_end_before", "status"):
                if str(a[f]) != b.get(f, ""):
                    div.append(f"{a['unit_id']}/{f}")
    else:
        div.append("CSV_ABSENT")
    chk("BOUNDARY_MAP_JSON_CSV_DIVERGENCE", BOUNDARY_INTEGRITY, div, [])
    mdtxt = open(md_p, encoding="utf-8").read() if os.path.exists(md_p) else ""
    chk("BOUNDARY_MAP_UNITS_ABSENT_FROM_MARKDOWN", BOUNDARY_INTEGRITY,
        [r["unit_id"] for r in rows if r["unit_id"] not in mdtxt], [])

    # ==================== 11. AUTHORITY AND CUSTODY STATUS ====================
    G = D.GROUPING_AUTHORITY
    chk("GROUPING_AUTHORITY_STATUS_EXPLICIT", AUTHORITY_DISCIPLINE,
        G["status"], "REFERENCED_NOT_FROZEN")
    chk("GROUPING_AUTHORITY_NOT_CLAIMED_CANONICAL", AUTHORITY_DISCIPLINE,
        G["canonical_authority_claimed"], False)
    chk("GROUPING_AUTHORITY_DOES_NOT_BLOCK_EXTRACTION", AUTHORITY_DISCIPLINE,
        G["blocks_extraction"], False)
    chk("GROUPING_AUTHORITY_ARTIFACT_ABSENT", AUTHORITY_DISCIPLINE,
        [i for i in G["referenced_identifiers"]
         if any(i in open(os.path.join(r, f), encoding="utf-8", errors="ignore").read()
                for r, _, fs in os.walk(os.path.join(REPO, "reviews")) for f in fs
                if f.endswith((".md", ".json")))], [])
    C = D.EXTERNAL_CUSTODY
    chk("PRIMARY_DOCX_CUSTODY_EXPLICIT", AUTHORITY_DISCIPLINE,
        C["primary_docx"]["custody"], "EXTERNAL_DURABLE_SOURCE_BY_IDENTITY")
    chk("PRIMARY_DOCX_NOT_TRACKED", AUTHORITY_DISCIPLINE,
        C["primary_docx"]["tracked_in_git"], False)
    chk("PRIMARY_DOCX_IDENTITY_RECORDED", AUTHORITY_DISCIPLINE,
        (C["primary_docx"]["bytes"], C["primary_docx"]["sha256"][:8]), (16832861, "5a9142cd"))
    chk("FREEZE_PACKAGE_CUSTODY_EXPLICIT", AUTHORITY_DISCIPLINE,
        C["freeze_package"]["custody"], "DURABLE_CUSTODY_PENDING")
    chk("SHARED_TEAM_CUSTODY_NOT_CLAIMED", AUTHORITY_DISCIPLINE,
        C["freeze_package"]["shared_team_custody_claimed"], False)
    chk("RENDERED_PDF_CLASSIFICATION", AUTHORITY_DISCIPLINE,
        C["rendered_pdf"]["classification"],
        "DERIVED_ARTIFACT_PRESERVED_INSIDE_FREEZE_PACKAGE")
    chk("RENDERED_PDF_NOT_TRACKED_SEPARATELY", AUTHORITY_DISCIPLINE,
        C["rendered_pdf"]["tracked_in_git"], False)
    chk("GIT_LFS_STATUS_EXPLICIT", AUTHORITY_DISCIPLINE, C["git_lfs"], "NOT_CONFIGURED")
    # Source ingest closed exactly two stop conditions; nothing else may claim to be resolved.
    chk("RESOLVED_STOP_CONDITIONS", STOP_CONDITION,
        sorted(c["id"] for c in D.STOP_CONDITIONS if c["status"] == "RESOLVED"),
        ["STOP-001", "STOP-002"])
    chk("RESOLVED_STOP_WITH_UNITS_STILL_ATTACHED", STOP_CONDITION,
        [c["id"] for c in D.STOP_CONDITIONS if c["status"] == "RESOLVED" and c["applies_to"]], [])
    chk("INVALID_STOP_STATUSES", STOP_CONDITION,
        sorted({c["status"] for c in D.STOP_CONDITIONS
                if c["status"] not in D.STOP_STATUSES}), [])

    # ==================== 12. ACCOUNTING ====================
    gate_ids = [r["gate_id"] for r in res]
    chk("DUPLICATE_GATE_IDS", ACCOUNTING,
        sorted({g for g in gate_ids if gate_ids.count(g) > 1}), [])
    chk("EVERY_GATE_CARRIES_A_TYPE", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in (
            INVENTORY_INTEGRITY, AUTHORITY_DISCIPLINE, RULE_PORTABILITY, SELECTION_INTEGRITY,
            STOP_CONDITION, ARTIFACT_AGREEMENT, PLAN_INTEGRITY, SUPERSESSION_MARKER,
            ACCOUNTING, SOURCE_CUSTODY, BOUNDARY_INTEGRITY)], [])
    return res


def accounting(rows):
    """Typed accounting. Membership of a class is read from `gate_type`, never from the ID."""
    markers = [r for r in rows if r["gate_type"] == SUPERSESSION_MARKER]
    active = [r for r in rows if r["gate_type"] != SUPERSESSION_MARKER]
    by_type = {}
    for r in active:
        by_type[r["gate_type"]] = by_type.get(r["gate_type"], 0) + 1
    return dict(TOTAL_EMITTED_GATE_RECORDS=len(rows),
                SUPERSESSION_MARKERS_PRESENT=len(markers),
                ACTIVE_TEST_GATES=len(active),
                ACTIVE_TEST_GATES_PASSING=sum(1 for r in active if r["ok"]),
                BY_TYPE=dict(sorted(by_type.items())),
                FAILING=[r["gate_id"] for r in rows if not r["ok"]])


if __name__ == "__main__":
    rows = run()
    a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows)
    t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        print(f"{'PASS' if r['ok'] else 'FAIL'}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  "
              f"{r['value']!r}" + ("" if r["ok"] else f"   expected {r['expected']!r}"))
    print()
    print(f"{a['ACTIVE_TEST_GATES_PASSING']}/{a['ACTIVE_TEST_GATES']} active gates PASS  ·  "
          f"{a['SUPERSESSION_MARKERS_PRESENT']} supersession markers  ·  "
          f"{a['TOTAL_EMITTED_GATE_RECORDS']} emitted records")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<24} {v}")
    sys.exit(1 if a["FAILING"] else 0)
