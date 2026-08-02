# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.5 QA — typed gates over the T04 pre-storyboard decision pack.

Every record carries an explicit `gate_type`; nothing is classified by ID substring.

    python3 docs/pl06/t04/tools/t04_pack_qa_v1.py
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_pack_data_v1 as P
import t04_data_v1 as SRC
import t04_pack_emit_v1 as EMIT

MAPPING_INTEGRITY = "MAPPING_INTEGRITY"
CONTRACT_INTEGRITY = "CONTRACT_INTEGRITY"
SMARTART_FIDELITY = "SMARTART_FIDELITY"
AUTHORSHIP_GUARD = "AUTHORSHIP_GUARD"
INVENTION_GUARD = "INVENTION_GUARD"
PROPAGATION_GUARD = "PROPAGATION_GUARD"
SAFETY_DISCLOSURE = "SAFETY_DISCLOSURE"
DECISION_INTEGRITY = "DECISION_INTEGRITY"
ARTIFACT_AGREEMENT = "ARTIFACT_AGREEMENT"
ACCOUNTING = "ACCOUNTING"
SUPERSESSION_MARKER = "SUPERSESSION_MARKER"

GATE_TYPES = {MAPPING_INTEGRITY, CONTRACT_INTEGRITY, SMARTART_FIDELITY, AUTHORSHIP_GUARD,
              INVENTION_GUARD, PROPAGATION_GUARD, SAFETY_DISCLOSURE, DECISION_INTEGRITY,
              ARTIFACT_AGREEMENT, ACCOUNTING, SUPERSESSION_MARKER}

EXPECTED_TREATMENTS = ["CLICK_TO_REVEAL", "CLICK_TO_REVEAL", "COMPARISON", "PENDING_HUMAN",
                       "PROCESS_FLOW", "SEQUENTIAL_STEPS"]
# The six SmartArt nodes, in the order the source draws them. Frozen here so a reorder fires.
EXPECTED_NODES = [
    "Koordinasi dan Demonstrasi Penyelenggaraan Taman",
    "Penyeliaan Penyelenggaraan Taman",
    "Penyeliaan Operasi Nurseri",
    "Penyeliaan Alatan dan Mesin Penyelenggaraan Taman",
    "Penyeliaan Inventori Taman",
    "Perancangan Sumber Manusia dan Kebajikan Pekerja",
]
FINAL_QUIZ_MARKERS = ("apakah", "yang manakah", "pilih jawapan", "jawapan yang betul",
                      "answer:", "correct answer", "jawapan:")


def run():
    res = []

    def chk(gid, gtype, value, expected):
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        ok=value == expected))

    M, C, S, R, Q, DEC = P.MAPPING, P.CONTRACTS, P.SMARTART, P.RUMUSAN, P.QUIZ, P.DECISIONS
    BY = SRC.BY_ID

    # ==================== 1. MAPPING ====================
    chk("SCREEN_CANDIDATES", MAPPING_INTEGRITY, len(M), 6)
    chk("ALL_SIX_B0_CANDIDATES_REPRESENTED", MAPPING_INTEGRITY,
        sorted(m["screen_candidate_id"] for m in M),
        sorted(c["candidate_id"] for c in SRC.SCREEN_CANDIDATES))
    chk("MAPPING_TREATMENTS", MAPPING_INTEGRITY,
        sorted(m["proposed_treatment"] for m in M), EXPECTED_TREATMENTS)
    chk("INVALID_TREATMENT_STATUSES", MAPPING_INTEGRITY,
        sorted({m["treatment_status"] for m in M
                if m["treatment_status"] not in P.TREATMENT_STATUSES}), [])
    ids = [m["screen_candidate_id"] for m in M]
    chk("DUPLICATE_SCREEN_CANDIDATE_IDS", MAPPING_INTEGRITY,
        sorted({i for i in ids if ids.count(i) > 1}), [])
    # Every proposed screen must bind to source rows that exist — except the one that
    # honestly has no source, which must declare itself PENDING_HUMAN.
    chk("SCREEN_ROWS_NOT_IN_EXTRACT", MAPPING_INTEGRITY,
        sorted({r for m in M for r in m["source_row_ids"] if r not in BY}), [])
    chk("SCREEN_WITHOUT_SOURCE_ROWS", MAPPING_INTEGRITY,
        [m["screen_candidate_id"] for m in M
         if not m["source_row_ids"] and m["proposed_treatment"] != "PENDING_HUMAN"], [])
    chk("EVERY_NON_PENDING_SCREEN_HAS_ROWS", MAPPING_INTEGRITY,
        all(m["source_row_ids"] for m in M if m["proposed_treatment"] != "PENDING_HUMAN"), True)
    chk("FINAL_SCREEN_COUNT_NOT_CLAIMED", MAPPING_INTEGRITY,
        P.SCREEN_COUNT_CLAIM["final_screen_count"], "NOT_CLAIMED")
    chk("SCREEN_COUNT_NOT_DERIVED_FROM_B02", MAPPING_INTEGRITY,
        P.SCREEN_COUNT_CLAIM["derived_from_b02"], False)

    # ==================== 2. CONTRACTS ====================
    chk("CONTRACTS", CONTRACT_INTEGRITY, len(C), 6)
    chk("CONTRACT_TYPES", CONTRACT_INTEGRITY,
        sorted(c["candidate_type"] for c in C), EXPECTED_TREATMENTS)
    cids = [c["contract_id"] for c in C]
    chk("DUPLICATE_CONTRACT_IDS", CONTRACT_INTEGRITY,
        sorted({i for i in cids if cids.count(i) > 1}), [])
    REQUIRED = ["contract_id", "candidate_type", "source_rows", "learner_facing_purpose",
                "base_state", "interaction_states", "completion_condition", "visual_treatment",
                "text_treatment", "vo_proposal", "speaker_notes_proposal",
                "accessibility_consideration", "fallback_behaviour", "source_authority",
                "open_decision", "bariah_approval"]
    chk("CONTRACTS_MISSING_A_REQUIRED_FIELD", CONTRACT_INTEGRITY,
        [c["contract_id"] for c in C if any(f not in c for f in REQUIRED)], [])
    chk("CONTRACT_ROWS_NOT_IN_EXTRACT", CONTRACT_INTEGRITY,
        sorted({r for c in C for r in c["source_rows"] if r not in BY}), [])
    chk("CONTRACTS_NOT_PENDING_APPROVAL", CONTRACT_INTEGRITY,
        [c["contract_id"] for c in C
         if c["bariah_approval"]["status"] != P.APPROVAL_STATUS], [])
    chk("CONTRACTS_PRE_APPROVED", CONTRACT_INTEGRITY,
        [c["contract_id"] for c in C if c["bariah_approval"]["decision"] is not None], [])
    # PENDING_HUMAN must present options and choose none of them.
    ph = next(c for c in C if c["candidate_type"] == "PENDING_HUMAN")
    chk("PENDING_HUMAN_OPTION_COUNT", CONTRACT_INTEGRITY, len(ph.get("options", [])), 3)
    chk("PENDING_HUMAN_OPTIONS_HAVE_TRADEOFFS", CONTRACT_INTEGRITY,
        [o["option"] for o in ph["options"] if not o.get("tradeoff")], [])
    chk("PENDING_HUMAN_SILENTLY_CHOSE_A_TREATMENT", CONTRACT_INTEGRITY,
        ph["base_state"].startswith("NOT PROPOSED"), True)

    # ==================== 3. REVEAL SAFETY ====================
    reveals = [c for c in C if c["candidate_type"] == "CLICK_TO_REVEAL"]
    chk("CLICK_TO_REVEAL_CONTRACTS", SAFETY_DISCLOSURE, len(reveals), 2)
    chk("REVEAL_HIDDEN_CONTENT_CLASSIFIED", SAFETY_DISCLOSURE,
        sorted({c.get("hidden_content_classification") for c in reveals}), ["SUPPLEMENTARY"])
    chk("REVEAL_JUSTIFICATION_PRESENT", SAFETY_DISCLOSURE,
        [c["contract_id"] for c in reveals if not c.get("hidden_content_justification")], [])
    # The load-bearing gate: no legal or safety row may sit on a CLICK_TO_REVEAL contract.
    legal = set(P.LEGAL_ROWS)
    chk("LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL", SAFETY_DISCLOSURE,
        sorted({c["contract_id"] for c in reveals if legal & set(c["source_rows"])}), [])
    compliance = next(c for c in C if c["candidate_type"] == "SEQUENTIAL_STEPS")
    chk("LEGAL_ROWS_CARRIED_BY_A_CONTRACT", SAFETY_DISCLOSURE,
        sorted(set(compliance["source_rows"])), sorted(legal))
    chk("LEGAL_OBLIGATIONS_VISIBLE_IN_BASE_STATE", SAFETY_DISCLOSURE,
        "ALL obligation headings visible in the base state" in compliance["base_state"], True)
    chk("COMPLIANCE_CONTRACT_HIDES_NOTHING_MANDATORY", SAFETY_DISCLOSURE,
        compliance.get("hidden_content_classification"),
        "NOT_APPLICABLE_NOTHING_MANDATORY_IS_HIDDEN")

    # ==================== 4. SMARTART ====================
    chk("SMARTART_NODE_COUNT", SMARTART_FIDELITY, S["node_count"], 6)
    chk("SMARTART_NODES_EXACT_AND_ORDERED", SMARTART_FIDELITY, S["nodes"], EXPECTED_NODES)
    chk("SMARTART_NODES_MATCH_EXTRACT", SMARTART_FIDELITY,
        S["nodes"], SRC.ASSETS[0]["source_subject_nodes"])
    chk("SMARTART_ASSET_SHA256", SMARTART_FIDELITY, S["asset_sha256"], SRC.ASSETS[0]["sha256"])
    chk("SMARTART_HIERARCHY_FLAT", SMARTART_FIDELITY, S["hierarchy"].startswith("NONE"), True)
    chk("SMARTART_FLOW_DIRECTIONAL", SMARTART_FIDELITY, S["directional_flow"],
        "LINEAR_LEFT_TO_RIGHT")
    chk("SMARTART_TREATMENT_STATUS", SMARTART_FIDELITY, S["treatment_status"],
        "PENDING_BARIAH_REVIEW")
    chk("SMARTART_ASSET_PRODUCTION_NOT_STARTED", SMARTART_FIDELITY,
        [S["review_storyboard_treatment"]["asset_production"],
         S["future_mmd_treatment"]["asset_production"]],
        ["NOT_STARTED", "NOT_STARTED_IN_THIS_STAGE"])
    chk("SMARTART_BOTH_TREATMENTS_DEFINED", SMARTART_FIDELITY,
        bool(S["review_storyboard_treatment"]["rules"]
             and S["future_mmd_treatment"]["rules"]), True)

    # ==================== 5. AUTHORSHIP ====================
    blob = json.dumps([M, C, R, Q, DEC, P.SMARTART], ensure_ascii=False)
    chk("RUMUSAN_CONTENT_STATUS", AUTHORSHIP_GUARD, R["content_status"], "CAIR_ASSISTED_DRAFT")
    chk("RUMUSAN_APPROVAL_STATUS", AUTHORSHIP_GUARD, R["approval_status"],
        "PENDING_BARIAH_REVIEW")
    chk("INSTRUCTIONAL_AUTHORITY_IS_BARIAH", AUTHORSHIP_GUARD,
        [R["instructional_authority"], P.INSTRUCTIONAL_AUTHORITY, Q["final_author"]],
        ["BARIAH", "BARIAH", "BARIAH"])
    chk("BARIAH_IS_SOLE_ID", AUTHORSHIP_GUARD,
        any("sole Instructional Designer" in x for x in P.ROLES["BARIAH"]), True)
    chk("CAIR_CLAIMS_INSTRUCTIONAL_AUTHORSHIP", AUTHORSHIP_GUARD,
        [x for x in P.ROLES["CAIR"]
         if "instructional" in x.lower() or "author" in x.lower()], [])
    for label in P.FORBIDDEN_LABELS:
        chk(f"FORBIDDEN_LABEL_{label}", AUTHORSHIP_GUARD,
            f'"{label}"' in blob or f"'{label}'" in blob, False)
    chk("DECISIONS_PRE_APPROVED", AUTHORSHIP_GUARD,
        [d["decision_id"] for d in DEC if d["approval"] is not None], [])

    # ==================== 6. RUMUSAN ====================
    chk("RUMUSAN_STATEMENTS", INVENTION_GUARD, len(R["statements"]), 5)
    chk("RUMUSAN_STATEMENTS_WITHOUT_SOURCE_ROWS", INVENTION_GUARD,
        [s["statement_id"] for s in R["statements"] if not s["source_row_ids"]], [])
    chk("RUMUSAN_ROWS_NOT_IN_EXTRACT", INVENTION_GUARD,
        sorted({r for s in R["statements"] for r in s["source_row_ids"] if r not in BY}), [])
    chk("RUMUSAN_STATEMENTS_WITHOUT_RISK_STATUS", INVENTION_GUARD,
        [s["statement_id"] for s in R["statements"] if not s.get("factual_risk_status")], [])
    chk("RUMUSAN_CLAIMS_MODULE_ORIGIN", INVENTION_GUARD,
        "did NOT come from the module" in R["provenance"], True)
    chk("RUMUSAN_REVIEW_TABLE_COLUMNS", INVENTION_GUARD, R["review_table_columns"],
        ["accept", "edit", "remove", "comment"])

    # ==================== 7. QUIZ ====================
    chk("QUIZ_STRUCTURE_UNRESOLVED", INVENTION_GUARD, Q["quiz_structure"],
        "AUTHORITY_UNRESOLVED")
    chk("QUIZ_CONTENT_BLUEPRINT_ONLY", INVENTION_GUARD, Q["quiz_content"], "BLUEPRINT_ONLY")
    qblob = json.dumps(Q, ensure_ascii=False).lower()
    chk("FINAL_QUIZ_QUESTION_PRESENT", INVENTION_GUARD,
        [m for m in FINAL_QUIZ_MARKERS if m in qblob], [])
    chk("FINAL_ANSWER_KEY_PRESENT", INVENTION_GUARD,
        [k for k in ("answer_key", "correct_option", "jawapan_betul") if k in qblob], [])
    chk("QUIZ_BLUEPRINT_ROWS_NOT_IN_EXTRACT", INVENTION_GUARD,
        sorted({r for b in Q["blueprint"] for r in b["source_rows"] if r not in BY}), [])
    chk("QUIZ_BLUEPRINT_WITHOUT_SOURCE_ROWS", INVENTION_GUARD,
        [b["blueprint_id"] for b in Q["blueprint"] if not b["source_rows"]], [])
    chk("QUIZ_STRUCTURE_OPTIONS", INVENTION_GUARD, len(Q["structure_options"]), 2)
    # The 60% threshold and the 4+1 shape must never be recorded as confirmed. Scanned with
    # the not_produced list REMOVED: that list exists precisely to say "confirmed 60 percent
    # threshold" is a thing we did not produce, and matching a prohibition as if it were a
    # claim is the same false positive that bit INVENTED_QUIZ_TEXT at Stage 4.2F-B0.
    _claims = json.dumps([M, C, R, dict(Q, not_produced=[]), DEC, P.SMARTART],
                         ensure_ascii=False).lower()
    chk("PASS_THRESHOLD_TREATED_AS_CONFIRMED", INVENTION_GUARD,
        [x for x in ("confirmed 60", "60% confirmed", "threshold: 60", "pass_mark_60")
         if x in _claims], [])
    chk("QUIZ_COMPOSITION_TREATED_AS_CONFIRMED", INVENTION_GUARD,
        [x for x in ("confirmed 4 mcq", "4 mcq + 1 mr confirmed") if x in _claims], [])
    chk("CONFIRMED_STRUCTURE_LISTED_AS_NOT_PRODUCED", INVENTION_GUARD,
        sorted(x for x in Q["not_produced"] if "confirmed" in x),
        ["confirmed 4 MCQ + 1 MR structure", "confirmed 60 percent threshold"])

    # ==================== 8. B02 PROPAGATION AND CAST ====================
    for token in SRC.B02_FORBIDDEN:
        chk(f"B02_PROPAGATION_{token.replace(' ', '_').upper()}", PROPAGATION_GUARD,
            [m["screen_candidate_id"] for m in M
             if token.lower() in (m["proposed_treatment"] + m["reusable_capability"]
                                  + m["new_capability_required"]).lower()], [])
    chk("B02_FAMILY_IN_CONTRACTS", PROPAGATION_GUARD,
        [c["contract_id"] for c in C
         if any(f in json.dumps(c, ensure_ascii=False) for f in ("FAMILY_S", "FAMILY_P1",
                                                                 "FAMILY_P2"))], [])
    cast = next(d for d in DEC if d["decision_id"] == "D-03")
    chk("CAST_DECISION_SCOPE", PROPAGATION_GUARD, cast["scope"].startswith("THIS_UNIT_ONLY"),
        True)
    chk("CAST_NOT_PROPAGATED_PL06_WIDE", PROPAGATION_GUARD,
        "NOT a PL06-global cast decision" in cast["scope"]
        or "explicitly NOT a PL06-global" in cast["scope"], True)
    chk("B02_CAST_NAMES_PROPOSED", PROPAGATION_GUARD,
        [n for n in ("Alya", "Encik Rahman") if n in cast["recommendation"]], [])

    # ==================== 9. DECISIONS ====================
    chk("DECISION_COUNT", DECISION_INTEGRITY, len(DEC), 5)
    chk("DECISION_IDS", DECISION_INTEGRITY, sorted(d["decision_id"] for d in DEC),
        ["D-01", "D-02", "D-03", "D-04", "D-05"])
    DREQ = ["decision_id", "current_source_evidence", "recommendation", "alternative",
            "consequence_recommended", "consequence_alternative", "scope", "affected_screens",
            "approval", "comments"]
    chk("DECISIONS_MISSING_A_FIELD", DECISION_INTEGRITY,
        [d["decision_id"] for d in DEC if any(f not in d for f in DREQ)], [])
    chk("DECISION_SCREENS_NOT_IN_CONTRACTS", DECISION_INTEGRITY,
        sorted({s for d in DEC for s in d["affected_screens"]
                if s != "all" and s not in cids}), [])
    chk("D01_RECOMMENDATION", DECISION_INTEGRITY,
        DEC[0]["recommendation"].startswith("TEXT_AND_DIAGRAM_LED"), True)
    chk("D03_RECOMMENDATION", DECISION_INTEGRITY,
        "HILMI_NARRATOR_LED" in DEC[2]["recommendation"]
        and "NO_ADDITIONAL_CHARACTERS_FOR_T04" in DEC[2]["recommendation"], True)

    # ==================== 10. PORTABILITY TEMPLATE ====================
    T = P.PORTABILITY_TEMPLATE
    chk("PORTABILITY_STATUS", DECISION_INTEGRITY, T["status"], "TEMPLATE_NOT_YET_MEASURED")
    chk("PORTABILITY_SCORE_NOT_CALCULATED", DECISION_INTEGRITY, T["score"], "NOT_CALCULATED")
    chk("PORTABILITY_METRIC_COUNT", DECISION_INTEGRITY, len(T["rows"]), 16)
    chk("PORTABILITY_FABRICATED_MEASUREMENTS", DECISION_INTEGRITY,
        [r["metric"] for r in T["rows"] if r["value"] != "NOT_MEASURED"], [])
    chk("PORTABILITY_BANDS", DECISION_INTEGRITY, len(P.PORTABILITY_BANDS), 4)

    # ==================== 11. ARTIFACT AGREEMENT ====================
    for n, _ in EMIT.FILES:
        chk(f"DELIVERABLE_PRESENT::{n}", ARTIFACT_AGREEMENT,
            os.path.exists(os.path.join(T04, n)), True)
    stale = []
    for n, fn in EMIT.FILES:
        p = os.path.join(T04, n)
        if not os.path.exists(p):
            stale.append(n); continue
        b = fn()
        if not b.endswith("\n"):
            b += "\n"
        if open(p, encoding="utf-8").read() != b:
            stale.append(n)
    chk("EMITTED_DELIVERABLES_STALE", ARTIFACT_AGREEMENT, stale, [])
    # Markdown and JSON must agree on the two paired artifacts.
    mj = json.load(open(os.path.join(T04, "T04_SOURCE_TO_SCREEN_MAPPING_v1.json"),
                        encoding="utf-8"))
    cj = json.load(open(os.path.join(T04, "T04_SCREEN_CONTRACTS_DRAFT_v1.json"),
                        encoding="utf-8"))
    chk("MAPPING_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        [s["screen_candidate_id"] for s in mj["screens"]], ids)
    chk("CONTRACTS_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        [c["contract_id"] for c in cj["contracts"]], cids)
    mmd = open(os.path.join(T04, "T04_SOURCE_TO_SCREEN_MAPPING_v1.md"), encoding="utf-8").read()
    cmd = open(os.path.join(T04, "T04_SCREEN_CONTRACTS_DRAFT_v1.md"), encoding="utf-8").read()
    chk("MAPPING_MD_JSON_DIVERGENCE", ARTIFACT_AGREEMENT,
        [i for i in ids if i not in mmd], [])
    chk("CONTRACTS_MD_JSON_DIVERGENCE", ARTIFACT_AGREEMENT,
        [i for i in cids if i not in cmd], [])
    wa = open(os.path.join(T04, "T04_BARIAH_WHATSAPP_DRAFT_v1.md"), encoding="utf-8").read()
    chk("WHATSAPP_DRAFT_NOT_SENT", ARTIFACT_AGREEMENT, "Not sent" in wa, True)
    chk("WHATSAPP_DRAFT_STATES_DRAFT_STATUS", ARTIFACT_AGREEMENT,
        "bukan rumusan muktamad" in wa and "Kami tidak tulis sebarang soalan" in wa, True)

    # ==================== 12. STAGE CONSTRAINTS ====================
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, timeout=60).stdout.split("\n")
    except Exception:
        tracked = []
    chk("GIT_INDEX_READ", ARTIFACT_AGREEMENT, len(tracked) > 100, True)
    chk("PPTX_GENERATED", ARTIFACT_AGREEMENT,
        [t for t in tracked if t.lower().endswith(".pptx") and "/pl06/" in t], [])
    try:
        gen = subprocess.run(["git", "status", "--porcelain",
                              "reviews/source-completion/generator"], cwd=REPO,
                             capture_output=True, text=True, timeout=60).stdout.strip()
    except Exception:
        gen = ""
    chk("GENERATOR_MODIFIED", ARTIFACT_AGREEMENT, gen, "")

    # ==================== 13. ACCOUNTING ====================
    g = [r["gate_id"] for r in res]
    chk("DUPLICATE_GATE_IDS", ACCOUNTING, sorted({x for x in g if g.count(x) > 1}), [])
    chk("EVERY_GATE_CARRIES_A_TYPE", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [])
    return res


def accounting(rows):
    m = [r for r in rows if r["gate_type"] == SUPERSESSION_MARKER]
    a = [r for r in rows if r["gate_type"] != SUPERSESSION_MARKER]
    by = {}
    for r in a:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    return dict(TOTAL_EMITTED_GATE_RECORDS=len(rows), SUPERSESSION_MARKERS_PRESENT=len(m),
                ACTIVE_TEST_GATES=len(a), ACTIVE_TEST_GATES_PASSING=sum(1 for r in a if r["ok"]),
                BY_TYPE=dict(sorted(by.items())),
                FAILING=[r["gate_id"] for r in rows if not r["ok"]])


if __name__ == "__main__":
    rows = run(); a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows); t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        print(f"{'PASS' if r['ok'] else 'FAIL'}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  "
              f"{r['value']!r}" + ("" if r["ok"] else f"   expected {r['expected']!r}"))
    print()
    print(f"{a['ACTIVE_TEST_GATES_PASSING']}/{a['ACTIVE_TEST_GATES']} active gates PASS  ·  "
          f"{a['SUPERSESSION_MARKERS_PRESENT']} supersession markers  ·  "
          f"{a['TOTAL_EMITTED_GATE_RECORDS']} emitted records")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<22} {v}")
    sys.exit(1 if a["FAILING"] else 0)
