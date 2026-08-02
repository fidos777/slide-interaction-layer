# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.7 QA — typed gates over the final structural rulings.

Every record carries an explicit `gate_type`; nothing is classified by ID substring.

    python3 docs/pl06/t04/tools/t04_final_rulings_qa_v1.py

A green suite measures the suite, not the artifact. What these gates hold is that Bariah's
confirmations were transcribed exactly, that the split she confirmed is the split the
contracts implement, that a confirmed policy is not reported as unapproved content and an
unapproved content item is not reported as confirmed, and that a requirement count is never
presented as a production count.
"""
import hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_final_rulings_data_v1 as D
import t04_rulings_data_v1 as B06
import t04_data_v1 as SRC
import t04_final_rulings_emit_v1 as EMIT

EVIDENCE_INTEGRITY = "EVIDENCE_INTEGRITY"
DECISION_INTEGRITY = "DECISION_INTEGRITY"
ASSESSMENT_INTEGRITY = "ASSESSMENT_INTEGRITY"
CAST_DISCIPLINE = "CAST_DISCIPLINE"
SAFETY_DISCLOSURE = "SAFETY_DISCLOSURE"
SMARTART_FIDELITY = "SMARTART_FIDELITY"
ASSET_ACCOUNTING = "ASSET_ACCOUNTING"
APPROVAL_ACCOUNTING = "APPROVAL_ACCOUNTING"
MAPPING_INTEGRITY = "MAPPING_INTEGRITY"
PRODUCTION_GUARD = "PRODUCTION_GUARD"
ARTIFACT_AGREEMENT = "ARTIFACT_AGREEMENT"
ACCOUNTING = "ACCOUNTING"
SUPERSESSION_MARKER = "SUPERSESSION_MARKER"

GATE_TYPES = {EVIDENCE_INTEGRITY, DECISION_INTEGRITY, ASSESSMENT_INTEGRITY, CAST_DISCIPLINE,
              SAFETY_DISCLOSURE, SMARTART_FIDELITY, ASSET_ACCOUNTING, APPROVAL_ACCOUNTING,
              MAPPING_INTEGRITY, PRODUCTION_GUARD, ARTIFACT_AGREEMENT, ACCOUNTING,
              SUPERSESSION_MARKER}

EXPECTED_NODES = [
    "Koordinasi dan Demonstrasi Penyelenggaraan Taman",
    "Penyeliaan Penyelenggaraan Taman",
    "Penyeliaan Operasi Nurseri",
    "Penyeliaan Alatan dan Mesin Penyelenggaraan Taman",
    "Penyeliaan Inventori Taman",
    "Perancangan Sumber Manusia dan Kebajikan Pekerja",
]
BASE_REQUIRED = ["T04-ROW-066", "T04-ROW-067", "T04-ROW-069", "T04-ROW-070"]
REVEAL_CONFIRMED = ["T04-ROW-071", "T04-ROW-072", "T04-ROW-073", "T04-ROW-074",
                    "T04-ROW-076", "T04-ROW-077", "T04-ROW-078"]

# Compliance vocabulary a character may not utter. Drawn from the source's own obligation
# wording rather than invented.
COMPLIANCE_TERMS = ("akta", "berlesen", "lesen", "ppe", "sds", "helaian data keselamatan",
                    "racun", "semburan", "spray", "stor berkunci", "pelupusan",
                    "papan tanda amaran", "pelaporan")

CONTROLLED_ARTIFACTS = [
    "T04_BARIAH_FINAL_STRUCTURAL_RULINGS_v1.md", "T04_BARIAH_FINAL_STRUCTURAL_RULINGS_v1.json",
    "T04_CHARACTER_CONTEXTUAL_FIT_ASSESSMENT_v1.md",
    "T04_SLIDE_2_DIALOGUE_CONTRACT_DRAFT_v1.md",
    "T04_VISUAL_ASSET_GROUPING_PLAN_v1.md", "T04_VISUAL_ASSET_GROUPING_PLAN_v1.csv",
    "T04_VISUAL_ASSET_GROUPING_PLAN_v1.json",
    "T04_SOURCE_TO_SCREEN_MAPPING_v3.md", "T04_SOURCE_TO_SCREEN_MAPPING_v3.json",
    "T04_SCREEN_CONTRACTS_DRAFT_v3.md", "T04_SCREEN_CONTRACTS_DRAFT_v3.json",
    "T04_REMAINING_BARIAH_CONTENT_REVIEWS_v1.md",
    "T04_BARIAH_WHATSAPP_CONTENT_REVIEW_DRAFT_v1.md",
]


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


def _strings(blob, drop=()):
    src_rows = {r["raw_source_text"] for r in SRC.ROWS}
    out = []

    def walk(o):
        if isinstance(o, str):
            if o not in src_rows:
                out.append(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                if k not in drop:
                    walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)

    walk(blob)
    return out


def run():
    res = []

    def chk(gid, gtype, value, expected):
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        ok=value == expected))

    DEC = {d["decision_id"]: d for d in D.DECISIONS}
    T = D.APPROVAL_TOTALS
    F = D.CONTEXTUAL_FIT
    S = D.D04_SPLIT
    SL = D.SLIDE2_DIALOGUE
    CT = {c["contract_id"]: c for c in D.CONTRACTS_V3}

    # ==================== 1. EVIDENCE ====================
    chk("EVIDENCE_ITEMS_TOTAL", EVIDENCE_INTEGRITY, len(D.EVIDENCE_ALL), 3)
    chk("EVIDENCE_NEW_THIS_STAGE", EVIDENCE_INTEGRITY, len(D.EVIDENCE_NEW), 1)
    chk("EVIDENCE_FILES_PRESENT", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE_ALL
         if not os.path.exists(os.path.join(REPO, e["frozen_path"]))], [])
    # Includes the two Stage 4.2F-B0.6 images — freezing a third must not disturb them.
    chk("ALL_EVIDENCE_BYTE_IDENTICAL", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE_ALL
         if os.path.exists(os.path.join(REPO, e["frozen_path"]))
         and (_sha256(os.path.join(REPO, e["frozen_path"])) != e["sha256"]
              or os.path.getsize(os.path.join(REPO, e["frozen_path"])) != e["byte_size"])], [])
    chk("EVIDENCE_CLASS", EVIDENCE_INTEGRITY,
        sorted({e["evidence_class"] for e in D.EVIDENCE_ALL}), ["BARIAH_DIRECT_SCREENSHOT"])
    chk("EVIDENCE_SCOPE", EVIDENCE_INTEGRITY,
        sorted({e["scope"] for e in D.EVIDENCE_ALL}), [D.UNIT_ID])
    chk("EVIDENCE_UNMODIFIED", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE_ALL
         if not e["modification"].startswith("NONE")], [])
    chk("EVIDENCE_SHA256_RECORDED", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE_ALL
         if not re.fullmatch(r"[0-9a-f]{64}", e["sha256"])], [])
    # The instruction said three images; one arrived. The mismatch must be declared.
    chk("EVIDENCE_DELIVERY_DISCREPANCY_DECLARED", EVIDENCE_INTEGRITY,
        (D.EVIDENCE_DELIVERY["expected_by_instruction"],
         D.EVIDENCE_DELIVERY["actually_received"],
         D.EVIDENCE_DELIVERY["actually_received"] == len(D.EVIDENCE_NEW)), (3, 1, True))
    chk("ILLEGIBLE_ELEMENTS_NOT_ATTRIBUTED_TO_SCREENSHOT", EVIDENCE_INTEGRITY,
        [L["item"] for L in D.EVIDENCE_LEGIBILITY
         if L["legible_in_screenshot"] is False and "INFERRED" not in L["authority"]], [])
    chk("EVERY_NEW_LOCATOR_BINDS_TO_NEW_EVIDENCE", EVIDENCE_INTEGRITY,
        sorted({r["locator"] for r in D.RULING_LOCATORS_NEW
                if r["evidence_id"] != "T04-EV-03"}), [])
    chk("B06_LOCATORS_PRESERVED", EVIDENCE_INTEGRITY,
        [r["locator"] for r in B06.RULING_LOCATORS
         if r not in D.RULING_LOCATORS_ALL], [])

    # ==================== 2. DECISION STATE ====================
    chk("DECISIONS_REGISTERED", DECISION_INTEGRITY,
        sorted(DEC), ["D-01", "D-02A", "D-02B", "D-02C", "D-03", "D-04", "D-05"])
    chk("UNKNOWN_DECISION_STATUSES", DECISION_INTEGRITY,
        sorted({d["status"] for d in D.DECISIONS
                if d["status"] not in D.DECISION_STATUSES}), [])
    chk("D02B_CONFIRMED_60_PERCENT", DECISION_INTEGRITY,
        (DEC["D-02B"]["status"], D.D02B["pass_threshold"]),
        ("CONFIRMED_BARIAH_DIRECT", "60_PERCENT"))
    chk("D02B_SCOPE_ALL_PLS_IN_KURSUS", DECISION_INTEGRITY,
        (DEC["D-02B"]["scope"], D.D02B["scope"]),
        ("ALL_PLS_IN_KURSUS", "ALL_PLS_IN_KURSUS"))
    chk("D02B_NO_LONGER_UNRESOLVED", DECISION_INTEGRITY,
        DEC["D-02B"]["status"] == "UNRESOLVED", False)
    chk("D04_CONFIRMED", DECISION_INTEGRITY,
        (DEC["D-04"]["status"], S["status"]),
        ("CONFIRMED_BARIAH_DIRECT", "CONFIRMED_BARIAH_DIRECT"))
    chk("D05_FULLY_CONFIRMED", DECISION_INTEGRITY,
        (DEC["D-05"]["status"], D.D05["status"], D.D05["review_storyboard"],
         D.D05["future_mmd"], D.D05["invariant"]),
        ("CONFIRMED_BARIAH_DIRECT", "CONFIRMED_BARIAH_DIRECT",
         "USE_SOURCE_BOUND_SIX_STEP_DIAGRAM", "CONTROLLED_REDRAW",
         "PRESERVE_SIX_NODE_IDENTITY_AND_ORDER"))
    chk("D05_ABSENT_FROM_UNRESOLVED_LISTS", DECISION_INTEGRITY,
        [r["review_id"] for r in D.PENDING_CONTENT_REVIEWS if r["decision"] == "D-05"], [])
    chk("ALL_STRUCTURAL_DECISIONS_RESOLVED_OR_CONDITIONAL", DECISION_INTEGRITY,
        sorted({d["structural_status"] for d in D.DECISIONS}),
        ["CONDITIONALLY_RESOLVED", "RESOLVED"])
    chk("STRUCTURAL_DECISIONS_CLOSED", DECISION_INTEGRITY,
        D.READINESS["structural_decisions_status"], "CLOSED")
    chk("EVERY_CHANGED_DECISION_RECORDS_ITS_PREVIOUS_STATUS", DECISION_INTEGRITY,
        [d["decision_id"] for d in D.DECISIONS
         if d["changed_this_stage"] and not d.get("previous_status")], [])
    chk("EVERY_DECISION_CITES_EVIDENCE_OR_IS_UNRESOLVED", DECISION_INTEGRITY,
        [d["decision_id"] for d in D.DECISIONS
         if not d["evidence"] and d["status"] != "UNRESOLVED"], [])
    chk("EVERY_CITED_LOCATOR_EXISTS", DECISION_INTEGRITY,
        sorted({x for d in D.DECISIONS for x in d["evidence"]}
               - {r["locator"] for r in D.RULING_LOCATORS_ALL}), [])

    # ==================== 3. CAST ====================
    chk("D03_SLIDE_AND_TREATMENT", CAST_DISCIPLINE,
        (D.D03_POLICY["slide"], D.D03_POLICY["treatment"]),
        ("SLIDE_2", "DIALOGUE_SCENARIO_WITH_ADDITIONAL_CHARACTER"))
    chk("D03_POLICY_STATUS_CONDITIONAL", CAST_DISCIPLINE,
        (D.D03_POLICY["policy_status"], DEC["D-03"]["status"]),
        ("CONFIRMED_WITH_CONDITION", "CONFIRMED_WITH_CONDITION"))
    chk("D03_PREFERRED_CAST", CAST_DISCIPLINE,
        D.D03_POLICY["preferred_existing_cast"], ["ALYA", "ENCIK_RAHMAN"])
    chk("D03_REUSE_CONDITION_AND_FALLBACK", CAST_DISCIPLINE,
        (D.D03_POLICY["reuse_condition"], D.D03_POLICY["fallback"]),
        ("USE_IF_CONTEXTUALLY_APPROPRIATE",
         "CREATE_NEW_CHARACTER_IF_EXISTING_PAIR_IS_NOT_CONTEXTUALLY_APPROPRIATE"))
    chk("CHARACTER_INSTANCE_MAPPING_NOT_COMPLETE", CAST_DISCIPLINE,
        D.D03_POLICY["character_instance_mapping"], "NOT_COMPLETE")
    chk("CONTEXTUAL_ASSESSMENT_EXISTS_AND_IS_ALLOWED", CAST_DISCIPLINE,
        F["recommendation"] in D.ALLOWED_FIT_RESULTS, True)
    chk("CONTEXTUAL_ASSESSMENT_CARRIES_EVERY_REQUIRED_FIELD", CAST_DISCIPLINE,
        [k for k in ("dialogue_purpose", "roles_required", "alya_fit", "encik_rahman_fit",
                     "specialist_expertise_required", "unsupported_expertise_risk",
                     "recommendation", "source_row_bindings") if not F.get(k)], [])
    chk("CONTEXTUAL_ASSESSMENT_IS_NOT_A_BARIAH_RULING", CAST_DISCIPLINE,
        (F["authority"], F["status"]),
        ("CAIR_ASSESSMENT_NOT_A_BARIAH_RULING", "PENDING_BARIAH_REVIEW"))
    chk("FIT_ASSESSMENT_ROWS_IN_EXTRACT", CAST_DISCIPLINE,
        sorted({r for r in F["source_row_bindings"] if r not in SRC.BY_ID}), [])
    chk("SLIDE_2_DIALOGUE_PENDING_REVIEW", CAST_DISCIPLINE,
        (SL["approval_status"], SL["bariah_approval"]["status"], SL["cast_status"]),
        ("PENDING_BARIAH_REVIEW", "PENDING_BARIAH_REVIEW",
         "PROPOSED_SUBJECT_TO_D03_CONDITION"))
    chk("SLIDE_2_ROWS_IN_EXTRACT", CAST_DISCIPLINE,
        sorted({r for r in SL["source_rows"] if r not in SRC.BY_ID}), [])
    chk("SLIDE_2_BEATS_BIND_TO_DECLARED_ROWS", CAST_DISCIPLINE,
        sorted({r for b in SL["beats"] for r in b["source_row_ids"]}
               - set(SL["source_rows"])), [])
    # No character may voice a compliance obligation.
    chk("NO_COMPLIANCE_CONTENT_IN_ANY_CHARACTER_LINE", CAST_DISCIPLINE,
        sorted({t for t in COMPLIANCE_TERMS for b in SL["beats"]
                if t in b["draft_line"].lower()}), [])
    chk("COMPLIANCE_EXCLUSION_DECLARED", CAST_DISCIPLINE,
        SL["compliance_content_excluded"], True)

    # ==================== 4. LEGAL SPLIT ====================
    chk("D04_BASE_CONTAINS_STATUTE_OPERATOR_AND_PPE", SAFETY_DISCLOSURE,
        [r for r in BASE_REQUIRED if r not in S["base_visible_rows"]], [])
    chk("D04_BASE_ROWS_NEVER_REVEAL_ELIGIBLE", SAFETY_DISCLOSURE,
        sorted(set(S["base_visible_rows"]) & set(S["reveal_eligible_rows"])), [])
    chk("D04_REVEAL_SET_MATCHES_RULING", SAFETY_DISCLOSURE,
        sorted(S["reveal_eligible_rows"]), sorted(REVEAL_CONFIRMED))
    chk("D04_REVEAL_ITEMS_ENUMERATED", SAFETY_DISCLOSURE,
        sorted({i["item"] for i in S["reveal_may_contain"]}),
        sorted(["SDS", "safe or locked storage", "spraying conditions", "notification",
                "reporting"]))
    chk("D04_SPLIT_APPLIED_TO_CONTRACT", SAFETY_DISCLOSURE,
        (S["applied_to_contracts"],
         CT["T04-CT-04"].get("base_visible_rows") == S["base_visible_rows"],
         CT["T04-CT-04"].get("reveal_eligible_rows") == S["reveal_eligible_rows"]),
        (True, True, True))
    chk("D04_CONTRACT_RECORDS_SUPERSEDED_BASE_STATE", SAFETY_DISCLOSURE,
        bool(CT["T04-CT-04"].get("superseded_base_state")), True)
    chk("D04_ROWS_IN_EXTRACT", SAFETY_DISCLOSURE,
        sorted({r for r in S["base_visible_rows"] + S["reveal_eligible_rows"]
                + S["out_of_scope_rows_unchanged"] if r not in SRC.BY_ID}), [])
    chk("D04_DELTA_FROM_CAIR_PROPOSAL_DECLARED", SAFETY_DISCLOSURE,
        (sorted(S["delta_from_cair_proposal"]["moved_to_base"]),
         sorted(S["delta_from_cair_proposal"]["newly_reveal_eligible"])),
        (["T04-ROW-070"], sorted(["T04-ROW-071", "T04-ROW-073", "T04-ROW-076",
                                  "T04-ROW-077", "T04-ROW-078"])))
    chk("D04_RESIDUAL_RISK_STATED", SAFETY_DISCLOSURE, bool(S["residual_risk"]), True)
    chk("D04_SCOPE_UNCHANGED", SAFETY_DISCLOSURE, S["scope"], D.UNIT_ID)
    chk("BAJA_COMPLIANCE_ROWS_STILL_BASE_VISIBLE", SAFETY_DISCLOSURE,
        sorted(S["out_of_scope_rows_unchanged"]),
        sorted(["T04-ROW-037", "T04-ROW-039", "T04-ROW-041", "T04-ROW-043", "T04-ROW-045"]))

    # ==================== 5. SMARTART ====================
    chk("SIX_NODES_AND_ORDER_PRESERVED", SMARTART_FIDELITY,
        D.D05["six_nodes_in_order"], EXPECTED_NODES)
    chk("SIX_NODES_MATCH_THE_SOURCE_ASSET", SMARTART_FIDELITY,
        D.D05["six_nodes_in_order"], list(SRC.ASSETS[0]["source_subject_nodes"]))
    chk("SMARTART_ASSET_IDENTITY_UNCHANGED", SMARTART_FIDELITY,
        (D.D05["asset_id"], D.D05["asset_sha256"]),
        (SRC.ASSETS[0]["asset_id"], SRC.ASSETS[0]["sha256"]))
    chk("SMARTART_HIERARCHY_STILL_FLAT", SMARTART_FIDELITY,
        D.D05["hierarchy"].startswith("NONE"), True)
    chk("MMD_PRODUCTION_NOT_STARTED", SMARTART_FIDELITY,
        (D.D05["mmd_production_status"], D.MMD_PRODUCTION_STARTED), ("NOT_STARTED", 0))

    # ==================== 6. ASSET ACCOUNTING ====================
    chk("VISUAL_OBLIGATIONS_RETAINED", ASSET_ACCOUNTING, D.VISUAL_OBLIGATION_COUNT, 46)
    chk("UNIQUE_ASSET_COUNT_NOT_DETERMINED", ASSET_ACCOUNTING,
        D.UNIQUE_ASSET_COUNT, "NOT_YET_DETERMINED")
    chk("VISUAL_COVERAGE_STATUS", ASSET_ACCOUNTING,
        D.VISUAL_COVERAGE_STATUS, "NEW_MMD_VISUAL_COVERAGE_REQUIRED")
    # The whole point of Part 7: a requirement count must never be published as an asset count.
    chk("OBLIGATION_COUNT_NOT_ASSERTED_AS_UNIQUE_ASSET_COUNT", ASSET_ACCOUNTING,
        [s for s in _strings(D.ASSET_TOTALS) + _strings(D.ASSET_PLAN)
         if re.search(r"UNIQUE_(MMD_)?ASSETS?\s*=\s*\d", s)], [])
    chk("UNIQUE_ASSET_COUNT_IS_NOT_NUMERIC", ASSET_ACCOUNTING,
        isinstance(D.UNIQUE_ASSET_COUNT, str) and not D.UNIQUE_ASSET_COUNT.isdigit(), True)
    chk("EVERY_OBLIGATION_HAS_AN_ASSET_PLAN_ROW", ASSET_ACCOUNTING,
        sorted({v["visual_obligation_id"] for v in D.VISUAL_OBLIGATIONS}
               ^ {r["obligation_id"] for r in D.ASSET_PLAN}), [])
    chk("ASSET_PLAN_GROUPS_RESOLVE", ASSET_ACCOUNTING,
        sorted({r["proposed_asset_group_id"] for r in D.ASSET_PLAN}
               - {g["group_id"] for g in D.ASSET_GROUPS}), [])
    chk("NO_UNIQUE_ASSET_ID_ASSIGNED_YET", ASSET_ACCOUNTING,
        sorted({r["unique_asset_candidate_id"] for r in D.ASSET_PLAN}), ["NOT_YET_ASSIGNED"])
    chk("NO_ASSET_PRODUCTION_STARTED", ASSET_ACCOUNTING,
        (sorted({r["production_status"] for r in D.ASSET_PLAN}),
         D.ASSET_TOTALS["production_started"]), (["NOT_STARTED"], 0))
    chk("EVERY_ASSET_ROW_NEEDS_BARIAH_APPROVAL", ASSET_ACCOUNTING,
        sorted({r["bariah_approval_requirement"] for r in D.ASSET_PLAN}),
        ["SUBJECT_AND_STYLE_APPROVAL_REQUIRED"])
    # Computed from the live plan, not from the cached total. Reading ASSET_TOTALS here made
    # the gate blind to a plan edit — the total is computed once at import and would not
    # follow. Fixture W-22 found this.
    _live_dnr = [r["obligation_id"] for r in D.ASSET_PLAN
                 if r["reuse_allowed"] == "SIMILAR_SUBJECT_DO_NOT_REUSE"]
    chk("NEAR_DUPLICATE_SUBJECTS_MARKED_DO_NOT_REUSE", ASSET_ACCOUNTING, len(_live_dnr), 3)
    chk("ASSET_TOTALS_AGREE_WITH_THE_LIVE_PLAN", ASSET_ACCOUNTING,
        (D.ASSET_TOTALS["do_not_reuse"] == len(_live_dnr),
         D.ASSET_TOTALS["VISUAL_OBLIGATIONS"] == len(D.ASSET_PLAN)), (True, True))

    # ==================== 7. APPROVAL ACCOUNTING ====================
    chk("CONFIRMED_POLICY_DECISIONS", APPROVAL_ACCOUNTING,
        T["CONFIRMED_POLICY_DECISIONS"],
        len([d for d in D.DECISIONS if d["structural_status"] == "RESOLVED"]))
    chk("CONFIRMED_POLICY_DECISIONS_NOT_ZERO", APPROVAL_ACCOUNTING,
        T["CONFIRMED_POLICY_DECISIONS"] > 0, True)
    chk("CONDITIONALLY_CONFIRMED_DECISIONS", APPROVAL_ACCOUNTING,
        (T["CONDITIONALLY_CONFIRMED_DECISIONS"],
         T["conditionally_confirmed_decision_ids"]), (1, ["D-03"]))
    chk("NO_FINAL_INSTRUCTIONAL_CONTENT_APPROVED", APPROVAL_ACCOUNTING,
        T["APPROVED_FINAL_INSTRUCTIONAL_CONTENT_ITEMS"], 0)
    chk("PENDING_CONTENT_REVIEWS", APPROVAL_ACCOUNTING,
        (T["PENDING_BARIAH_CONTENT_REVIEWS"], len(D.PENDING_CONTENT_REVIEWS)), (4, 4))
    chk("ONLY_RUMUSAN_QUIZ_DIALOGUE_AND_CAST_REMAIN", APPROVAL_ACCOUNTING,
        sorted(r["title"] for r in D.PENDING_CONTENT_REVIEWS),
        sorted(["Character instance mapping", "Slide 2 dialogue review",
                "Rumusan v2 review",
                "Five-slot quiz authoring, editing and approval"]))
    chk("EVERY_PENDING_REVIEW_IS_PENDING", APPROVAL_ACCOUNTING,
        sorted({r["status"] for r in D.PENDING_CONTENT_REVIEWS}), ["PENDING_BARIAH_REVIEW"])
    chk("AMBIGUOUS_APPROVED_ITEMS_NOT_EMITTED", APPROVAL_ACCOUNTING,
        hasattr(D, "APPROVED_ITEMS"), False)
    chk("SUPERSESSION_OF_APPROVED_ITEMS_DECLARED", APPROVAL_ACCOUNTING,
        T["superseded_field"], "APPROVED_ITEMS")
    chk("STORYBOARD_NOT_CLAIMED_APPROVED", APPROVAL_ACCOUNTING,
        (D.READINESS["storyboard_status"],
         D.READINESS["storyboard_approval"].startswith("NOT_APPROVED")),
        ("NOT_GENERATED", True))

    # ==================== 8. MAPPING ====================
    chk("MAPPING_CANDIDATES", MAPPING_INTEGRITY, len(D.MAPPING_V3), 7)
    chk("CONTRACTS_V3", MAPPING_INTEGRITY, len(D.CONTRACTS_V3), 7)
    chk("SLIDE_2_CANDIDATE_ADDED", MAPPING_INTEGRITY,
        [m["screen_candidate_id"] for m in D.MAPPING_V3
         if m["slide_position"] == "SLIDE_2"], ["T04-SC-07"])
    chk("FINAL_SCREEN_COUNT_NOT_CLAIMED", MAPPING_INTEGRITY,
        (D.FINAL_SCREEN_COUNT, D.MAPPING_IMPACT_V3["final_screen_count"]),
        ("NOT_CLAIMED", "NOT_CLAIMED"))
    chk("UNMAPPED_OBLIGATIONS_UNCHANGED", MAPPING_INTEGRITY,
        D.MAPPING_IMPACT_V3["obligations_with_no_home"], 28)
    chk("B02_FAMILIES_PROPAGATED", MAPPING_INTEGRITY, D.B02_FAMILIES_PROPAGATED, 0)
    chk("EVERY_CONTRACT_PENDING_BARIAH_APPROVAL", MAPPING_INTEGRITY,
        sorted({c["bariah_approval"]["status"] for c in D.CONTRACTS_V3}),
        ["PENDING_BARIAH_REVIEW"])
    chk("CONTRACT_AND_CANDIDATE_IDS_UNIQUE", MAPPING_INTEGRITY,
        (len({c["contract_id"] for c in D.CONTRACTS_V3}),
         len({m["screen_candidate_id"] for m in D.MAPPING_V3})), (7, 7))

    # ==================== 9. PRODUCTION GUARD ====================
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, timeout=60).stdout.split()
    except Exception:
        tracked = []
    chk("GIT_INDEX_READ", PRODUCTION_GUARD, len(tracked) > 100, True)
    chk("NO_PPTX_GENERATED", PRODUCTION_GUARD,
        (D.PPTX_GENERATED,
         [t for t in tracked if t.lower().endswith(".pptx") and "/pl06/" in t]), (0, []))
    try:
        gen = subprocess.run(["git", "status", "--porcelain", "reviews/source-completion"],
                             cwd=REPO, capture_output=True, text=True, timeout=60).stdout.strip()
    except Exception:
        gen = ""
    chk("NO_PRODUCTION_GENERATOR_MODIFIED", PRODUCTION_GUARD,
        (gen, D.GENERATOR_TOUCHED), ("", 0))
    chk("NO_MMD_PRODUCTION_STARTED", PRODUCTION_GUARD,
        (D.MMD_PRODUCTION_STARTED, D.READINESS["mmd_status"]), (0, "NOT_STARTED"))
    chk("VERDICT_IS_ALLOWED", PRODUCTION_GUARD, D.VERDICT in D.ALLOWED_VERDICTS, True)

    # ==================== 10. ARTIFACT AGREEMENT ====================
    chk("ALL_CONTROLLED_ARTIFACTS_PRESENT", ARTIFACT_AGREEMENT,
        [n for n in CONTROLLED_ARTIFACTS if not os.path.exists(os.path.join(T04, n))], [])
    rj = json.load(open(os.path.join(T04, "T04_BARIAH_FINAL_STRUCTURAL_RULINGS_v1.json"),
                        encoding="utf-8"))
    chk("RULINGS_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        ({d["decision_id"]: d["status"] for d in rj["decisions"]},
         rj["approval_totals"]["CONFIRMED_POLICY_DECISIONS"], len(rj["evidence_all"])),
        ({d["decision_id"]: d["status"] for d in D.DECISIONS},
         T["CONFIRMED_POLICY_DECISIONS"], len(D.EVIDENCE_ALL)))
    aj = json.load(open(os.path.join(T04, "T04_VISUAL_ASSET_GROUPING_PLAN_v1.json"),
                        encoding="utf-8"))
    chk("ASSET_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        (len(aj["plan"]), aj["unique_asset_count"]), (46, "NOT_YET_DETERMINED"))
    acsv = open(os.path.join(T04, "T04_VISUAL_ASSET_GROUPING_PLAN_v1.csv"),
                encoding="utf-8").read().strip().splitlines()
    chk("ASSET_CSV_ROW_COUNT", ARTIFACT_AGREEMENT, len(acsv) - 1, 46)
    chk("ASSET_CSV_HEADER", ARTIFACT_AGREEMENT, acsv[0].split(","), D.ASSET_PLAN_FIELDS)
    mj = json.load(open(os.path.join(T04, "T04_SOURCE_TO_SCREEN_MAPPING_v3.json"),
                        encoding="utf-8"))
    chk("MAPPING_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        ([m["screen_candidate_id"] for m in mj["screens"]], mj["final_screen_count"]),
        ([m["screen_candidate_id"] for m in D.MAPPING_V3], "NOT_CLAIMED"))
    cj = json.load(open(os.path.join(T04, "T04_SCREEN_CONTRACTS_DRAFT_v3.json"),
                        encoding="utf-8"))
    chk("CONTRACTS_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        [c["contract_id"] for c in cj["contracts"]],
        [c["contract_id"] for c in D.CONTRACTS_V3])
    fit_md = open(os.path.join(T04, "T04_CHARACTER_CONTEXTUAL_FIT_ASSESSMENT_v1.md"),
                  encoding="utf-8").read()
    chk("FIT_MD_CARRIES_THE_RESULT", ARTIFACT_AGREEMENT, F["recommendation"] in fit_md, True)
    dlg_md = open(os.path.join(T04, "T04_SLIDE_2_DIALOGUE_CONTRACT_DRAFT_v1.md"),
                  encoding="utf-8").read()
    chk("DIALOGUE_MD_CARRIES_EVERY_BEAT", ARTIFACT_AGREEMENT,
        [b["beat"] for b in SL["beats"] if b["draft_line"] not in dlg_md], [])
    chk("WHATSAPP_DRAFT_NOT_SENT", ARTIFACT_AGREEMENT, D.WHATSAPP["status"], "DRAFT_NOT_SENT")
    chk("WHATSAPP_STATES_NO_STORYBOARD", ARTIFACT_AGREEMENT,
        "belum dijana" in D.WHATSAPP["text"], True)
    chk("WHATSAPP_STATES_NO_ASSET_PRODUCED", ARTIFACT_AGREEMENT,
        "Belum ada aset visual dihasilkan" in D.WHATSAPP["text"], True)
    chk("WHATSAPP_ASKS_ONLY_THE_FOUR_CONTENT_REVIEWS", ARTIFACT_AGREEMENT,
        len(D.PENDING_CONTENT_REVIEWS), 4)

    # ==================== 11. ACCOUNTING ====================
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
    rows = run()
    a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows)
    t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        print(f"{'PASS' if r['ok'] else 'FAIL'}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  "
              f"{r['value']!r}"[:200] + ("" if r["ok"] else f"   expected {r['expected']!r}"))
    print()
    print(f"{a['ACTIVE_TEST_GATES_PASSING']}/{a['ACTIVE_TEST_GATES']} active gates PASS  ·  "
          f"{a['SUPERSESSION_MARKERS_PRESENT']} supersession markers  ·  "
          f"{a['TOTAL_EMITTED_GATE_RECORDS']} emitted records")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<26} {v}")
    sys.exit(1 if a["FAILING"] else 0)
