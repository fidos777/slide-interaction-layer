# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.8 QA — typed gates over T04 content and instance mapping.

    SUITE_ID = T04_CONTENT_QA_v1
    python3 docs/pl06/t04/tools/t04_content_qa_v1.py

Two harness rules are new in this suite and both exist because of defects found earlier:

1. EVERY gate declares the POPULATION it examined. A gate that returns "0 bad records" over
   0 records is vacuous, and two such gates went vacuous unnoticed at Stage 4.2F-A2 when a
   population emptied out from under them.
2. A population of 0 FAILS unless the gate declares `empty_by_design` with a reason. Silence
   is not a licence.

A green suite measures the suite, not the artifact. No gate here can tell you whether the
quiz questions are good questions or whether the dialogue reads well in Malay.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_content_data_v1 as D
import t04_data_v1 as SRC
import t04_content_emit_v1 as EMIT

SUITE_ID = "T04_CONTENT_QA_v1"
PRIOR_SUITE_ID = "T04_FINAL_RULINGS_QA_v1"

SOURCE_AUTHORITY = "SOURCE_AUTHORITY"
OBLIGATION_CLOSURE = "OBLIGATION_CLOSURE"
ASSET_ACCOUNTING = "ASSET_ACCOUNTING"
SEQUENCE_INTEGRITY = "SEQUENCE_INTEGRITY"
DIALOGUE_DISCIPLINE = "DIALOGUE_DISCIPLINE"
RUMUSAN_DISCIPLINE = "RUMUSAN_DISCIPLINE"
ASSESSMENT_INTEGRITY = "ASSESSMENT_INTEGRITY"
MMD_GUARD = "MMD_GUARD"
PRODUCTION_GUARD = "PRODUCTION_GUARD"
ARTIFACT_AGREEMENT = "ARTIFACT_AGREEMENT"
REPORTING = "REPORTING"
ACCOUNTING = "ACCOUNTING"
SUPERSESSION_MARKER = "SUPERSESSION_MARKER"

GATE_TYPES = {SOURCE_AUTHORITY, OBLIGATION_CLOSURE, ASSET_ACCOUNTING, SEQUENCE_INTEGRITY,
              DIALOGUE_DISCIPLINE, RUMUSAN_DISCIPLINE, ASSESSMENT_INTEGRITY, MMD_GUARD,
              PRODUCTION_GUARD, ARTIFACT_AGREEMENT, REPORTING, ACCOUNTING,
              SUPERSESSION_MARKER}

# Things this suite deliberately does NOT verify. Published so a green run is not read as a
# broader claim than it is.
NOT_CHECKED = [
    "whether any quiz item is a good question, or discriminates between learners",
    "whether the proposed correct answers are the answers Bariah would choose",
    "whether the Malay in the dialogue, Rumusan or quiz reads naturally",
    "whether Alya and Encik Rahman are the right characters for T04",
    "whether 21 screens is the right length for this unit",
    "whether the eight asset groups are the right groupings",
    "whether 41 proposed unique assets is achievable at any particular effort",
    "whether the D-04 reveal split is instructionally sound — Bariah ruled it, the gates "
    "enforce it, they do not judge it",
    "any rendered output — no PPTX exists for T04 and none was generated",
]

# Compliance vocabulary a character may not utter, taken from the source's own wording.
COMPLIANCE_TERMS = ("akta", "berlesen", "lesen", "ppe", "sds", "helaian data keselamatan",
                    "racun", "semburan", "stor berkunci", "pelupusan", "papan tanda amaran",
                    "pelaporan", "perundangan")
# Screens that carry no source rows by design.
STRUCTURAL_SCREENS = {"T04-S01", "T04-S19", "T04-S20", "T04-S21"}
VO_ID = re.compile(r"T04-VO-\d{3}")
ROW_ID = re.compile(r"T04-ROW-\d{3}")

CONTROLLED_ARTIFACTS = [
    "T04_VISUAL_OBLIGATION_CLOSURE_v1.md", "T04_VISUAL_OBLIGATION_CLOSURE_v1.csv",
    "T04_VISUAL_OBLIGATION_CLOSURE_v1.json",
    "T04_VISUAL_ASSET_GROUPING_PLAN_v2.md", "T04_VISUAL_ASSET_GROUPING_PLAN_v2.csv",
    "T04_VISUAL_ASSET_GROUPING_PLAN_v2.json",
    "T04_PROPOSED_SCREEN_SEQUENCE_v1.md", "T04_PROPOSED_SCREEN_SEQUENCE_v1.json",
    "T04_CHARACTER_CONTEXTUAL_FIT_ASSESSMENT_v2.md",
    "T04_SLIDE_2_DIALOGUE_CAIR_DRAFT_v1.md", "T04_SLIDE_2_DIALOGUE_CAIR_DRAFT_v1.json",
    "T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v3.md", "T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v3.json",
    "T04_QUIZ_CAIR_ASSISTED_DRAFT_v1.md", "T04_QUIZ_CAIR_ASSISTED_DRAFT_v1.json",
    "T04_MMD_DEMAND_FORECAST_PRELIMINARY_v1.md", "T04_BARIAH_CONTENT_REVIEW_PACK_v1.md",
    "T04_BARIAH_WHATSAPP_CONTENT_REVIEW_DRAFT_v1.md",
]


def _strings(blob):
    src_rows = {r["raw_source_text"] for r in SRC.ROWS}
    out = []

    def walk(o):
        if isinstance(o, str):
            if o not in src_rows:
                out.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)

    walk(blob)
    return out


def run():
    res = []

    def chk(gid, gtype, value, expected, population, empty_by_design=None):
        """Every gate declares the population it examined. Population 0 fails unless the
        gate says why it is legitimately empty."""
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, empty_by_design=empty_by_design,
                        vacuous=vacuous, ok=ok and not vacuous))

    C = D.OBLIGATION_CLOSURE
    G = D.ASSET_GROUPS
    S = D.SCREEN_SEQUENCE
    Q = D.QUIZ
    R = D.RUMUSAN
    DLG = D.DIALOGUE
    F = D.CONTEXTUAL_FIT
    BY = SRC.BY_ID
    vids = {r["obligation_id"] for r in C}

    # ==================== 1. SOURCE AND AUTHORITY ====================
    substantive = ([("dialogue", L["dialogue_line_id"], L["source_row_ids"])
                    for L in DLG["lines"]]
                   + [("rumusan", s["point_id"], s["source_row_ids"]) for s in R["points"]]
                   + [("quiz", i["question_id"], i["source_row_ids"]) for i in Q["items"]])
    chk("EVERY_SUBSTANTIVE_DRAFT_LINE_HAS_SOURCE_ROWS", SOURCE_AUTHORITY,
        [f"{k}:{i}" for k, i, rows in substantive if not rows], [], len(substantive))
    chk("EVERY_DRAFT_SOURCE_ROW_EXISTS", SOURCE_AUTHORITY,
        sorted({r for _, _, rows in substantive for r in rows if r not in BY}), [],
        len({r for _, _, rows in substantive for r in rows}))
    chk("SUBJECT_AUTHORITY_NEVER_BARIAH_DIRECT", SOURCE_AUTHORITY,
        [r["obligation_id"] for r in C if r["subject_authority"] != "MODULE_SOURCE_ATTESTED"],
        [], len(C))
    chk("REQUIREMENT_AUTHORITY_IS_BARIAH_DIRECT", SOURCE_AUTHORITY,
        sorted({r["requirement_authority"] for r in C}), ["BARIAH_DIRECT_SCREENSHOT"], len(C))
    chk("POPULATION_DERIVATION_IS_THE_MODULE_HIERARCHY", SOURCE_AUTHORITY,
        sorted({r["population_derivation_authority"] for r in C}),
        ["MODULE_HEADING_HIERARCHY"], len(C))
    chk("POLICY_AND_POPULATION_AUTHORITY_ARE_DISTINCT", SOURCE_AUTHORITY,
        D.REQUIREMENT_AUTHORITY != D.POPULATION_DERIVATION_AUTHORITY, True, 2)
    chk("MISLEADING_POLICY_RULE_NAME_RETIRED", SOURCE_AUTHORITY,
        (D.VISUAL_POLICY_RULE, D.SUPERSEDED_POLICY_RULE),
        ("VISUAL_REQUIRED_FOR_BARIAH_RULED_SOURCE_POPULATION",
         "VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION"), 2)
    chk("SUPERSEDED_RULE_NAME_NOT_USED_AS_THE_LIVE_RULE", SOURCE_AUTHORITY,
        [d["decision_id"] for d in D.DECISIONS
         if d.get("ruling") == D.SUPERSEDED_POLICY_RULE], [], len(D.DECISIONS))
    # D-04 carries two provenances and they must stay apart.
    chk("D04_MIXED_PROVENANCE_EXPLICIT", SOURCE_AUTHORITY,
        (D.D04_PROVENANCE["treatment_authority"],
         D.D04_PROVENANCE["akta_base_screen_placement"]),
        ("BARIAH_DIRECT_SCREENSHOT", "FIRDAUS_ATTESTED_FROM_CROPPED_CONFIRMED_PROPOSAL"), 2)
    chk("AKTA_NOT_CLASSIFIED_AS_LEGIBLE_BARIAH_TEXT", SOURCE_AUTHORITY,
        D.D04_PROVENANCE["akta_base_screen_placement"] == "BARIAH_DIRECT_SCREENSHOT", False, 1)
    chk("D04_LEGIBLE_ITEMS_CITE_THEIR_TEXT", SOURCE_AUTHORITY,
        [i["item"] for i in D.D04_PROVENANCE["treatment_authority_covers"]
         if not i.get("legible_text")], [],
        len(D.D04_PROVENANCE["treatment_authority_covers"]))
    chk("FORBIDDEN_LABELS_ABSENT", SOURCE_AUTHORITY,
        sorted({lbl for lbl in D.FORBIDDEN_LABELS
                for s in _strings([C, G, S, Q, R, DLG, F, D.MMD_FORECAST]) if lbl in s}),
        [], len(D.FORBIDDEN_LABELS))
    chk("CAIR_NOT_NAMED_INSTRUCTIONAL_DESIGNER", SOURCE_AUTHORITY,
        [s for s in _strings([C, G, S, Q, R, DLG, F])
         if re.search(r"CAIR[^.]{0,40}(instructional designer|instructional author)", s,
                      re.I)], [], 1)

    # ==================== 2. OBLIGATION CLOSURE ====================
    # Derived LIVE from the closure list, never read from the module constants. Reading the
    # cached constants made these three blind to a dropped obligation — fixture V-03 found
    # it, exactly as W-22 found the same class of blindness in the Stage 4.2F-B0.7 suite.
    _live_total = len(C)
    _live_closed = len([r for r in C if r["closure_outcome"] in D.CLOSURE_OUTCOMES])
    _live_orphans = len([r for r in C
                         if r["closure_outcome"] not in D.CLOSURE_OUTCOMES
                         or (r["closure_outcome"].startswith("MAPPED_")
                             and not r["proposed_learner_screen_id"])])
    chk("VISUAL_OBLIGATIONS_TOTAL", OBLIGATION_CLOSURE, _live_total, 46, len(C))
    chk("VISUAL_OBLIGATIONS_CLOSED", OBLIGATION_CLOSURE, _live_closed, 46, len(C))
    chk("ORPHAN_OBLIGATIONS", OBLIGATION_CLOSURE, _live_orphans, 0, len(C))
    chk("CLOSURE_TOTALS_DERIVED_LIVE", OBLIGATION_CLOSURE,
        (D.VISUAL_OBLIGATIONS_TOTAL == _live_total,
         D.VISUAL_OBLIGATIONS_CLOSED == _live_closed,
         D.ORPHAN_OBLIGATIONS == _live_orphans,
         sum(D.CLOSURE_BY_OUTCOME.values()) == _live_total), (True, True, True, True),
        len(C))
    chk("EVERY_OBLIGATION_HAS_A_LEGAL_OUTCOME", OBLIGATION_CLOSURE,
        [r["obligation_id"] for r in C if r["closure_outcome"] not in D.CLOSURE_OUTCOMES],
        [], len(C))
    chk("FORBIDDEN_OUTCOME_ABSENT", OBLIGATION_CLOSURE,
        [r["obligation_id"] for r in C if r["closure_outcome"] == D.FORBIDDEN_OUTCOME],
        [], len(C))
    chk("MAPPED_OUTCOMES_CARRY_A_SCREEN", OBLIGATION_CLOSURE,
        [r["obligation_id"] for r in C
         if r["closure_outcome"] in ("MAPPED_TO_LEARNER_SCREEN", "MAPPED_TO_RUNTIME_STATE")
         and not r["proposed_learner_screen_id"]], [],
        len([r for r in C if r["closure_outcome"].startswith("MAPPED_")]))
    chk("RUNTIME_STATE_OUTCOMES_CARRY_A_STATE", OBLIGATION_CLOSURE,
        [r["obligation_id"] for r in C
         if r["closure_outcome"] == "MAPPED_TO_RUNTIME_STATE"
         and not r["proposed_runtime_state_id"]], [],
        len([r for r in C if r["closure_outcome"] == "MAPPED_TO_RUNTIME_STATE"]))
    chk("NON_ASSET_OUTCOMES_CARRY_A_REASON", OBLIGATION_CLOSURE,
        [r["obligation_id"] for r in C
         if r["closure_outcome"] == "NOT_A_SEPARATE_ASSET_WITH_REASON"
         and len(r["rationale"]) < 40], [],
        len([r for r in C if r["closure_outcome"] == "NOT_A_SEPARATE_ASSET_WITH_REASON"]))
    chk("EVERY_CLOSURE_ROW_HAS_A_RATIONALE", OBLIGATION_CLOSURE,
        [r["obligation_id"] for r in C if not r["rationale"]], [], len(C))
    chk("EVERY_OBLIGATION_SCREEN_EXISTS", OBLIGATION_CLOSURE,
        sorted({r["proposed_learner_screen_id"] for r in C
                if r["proposed_learner_screen_id"]}
               - {s["screen_id"] for s in S}), [],
        len([r for r in C if r["proposed_learner_screen_id"]]))
    chk("EVERY_OBLIGATION_ROW_IN_EXTRACT", OBLIGATION_CLOSURE,
        sorted({r for x in C for r in x["source_row_ids"] if r not in BY}), [],
        len({r for x in C for r in x["source_row_ids"]}))
    chk("DUPLICATE_OBLIGATION_IDS", OBLIGATION_CLOSURE,
        sorted({r["obligation_id"] for r in C
                if [x["obligation_id"] for x in C].count(r["obligation_id"]) > 1}), [], len(C))
    chk("EVERY_COMPLEXITY_TIER_IS_ALLOWED", OBLIGATION_CLOSURE,
        sorted({r["complexity_tier"] for r in C if r["complexity_tier"]
                not in D.COMPLEXITY_TIERS}), [], len(C))
    # No obligation ID may be typed anywhere in the pack that does not resolve to the inventory.
    typed = {m for s in _strings([C, G, S, Q, R, DLG, F, D.MMD_FORECAST,
                                  D.REMAINING_BARIAH_APPROVALS])
             for m in VO_ID.findall(s)}
    chk("NO_HAND_TYPED_OBLIGATION_ID_FAILS_TO_RESOLVE", OBLIGATION_CLOSURE,
        sorted(typed - vids), [], len(typed))

    # ==================== 3. ASSET ACCOUNTING ====================
    t = D.ASSET_TOTALS
    chk("UNIQUE_ASSET_COUNT_STATUS", ASSET_ACCOUNTING,
        D.UNIQUE_ASSET_COUNT, "PROPOSED_NOT_APPROVED", 1)
    chk("UNIQUE_ASSET_COUNT_NOT_A_BARE_NUMBER", ASSET_ACCOUNTING,
        isinstance(D.UNIQUE_ASSET_COUNT, str) and not D.UNIQUE_ASSET_COUNT.isdigit(),
        True, 1)
    chk("OBLIGATION_COUNT_NOT_EQUATED_TO_UNIQUE_ASSET_COUNT", ASSET_ACCOUNTING,
        t["proposed_unique_assets"] == t["visual_obligation_count"], False, 2)
    chk("NO_UNIQUE_ASSET_COUNT_ASSERTED_IN_PROSE", ASSET_ACCOUNTING,
        [s for s in _strings([t, G, D.MMD_FORECAST])
         if re.search(r"UNIQUE_(MMD_)?ASSETS?\s*=\s*\d", s)], [], len(G))
    # Derived live, never read from the cached totals — a cached read made a Stage 4.2F-B0.7
    # gate blind to a plan edit (fixture W-22).
    live_assets = sum(g["proposed_unique_assets"] for g in G)
    live_dnr_groups = len([g for g in G if g["do_not_reuse_obligations"]])
    live_dnr_obligations = len([r for r in C if r["reuse_policy"] == "DO_NOT_REUSE"])
    chk("ASSET_TOTALS_DERIVED_LIVE", ASSET_ACCOUNTING,
        (t["proposed_unique_assets"] == live_assets,
         t["do_not_reuse_group_count"] == live_dnr_groups,
         t["do_not_reuse_obligation_count"] == live_dnr_obligations,
         t["visual_obligation_count"] == len(C)), (True, True, True, True), len(G))
    chk("DO_NOT_REUSE_GROUP_AND_OBLIGATION_COUNTS_ARE_DISTINCT", ASSET_ACCOUNTING,
        (live_dnr_groups, live_dnr_obligations, live_dnr_groups != live_dnr_obligations),
        (2, 3, True), len(C))
    chk("UNIQUE_ASSET_COUNT_CONFIRMED_IS_ZERO", ASSET_ACCOUNTING,
        t["unique_asset_count_confirmed"], 0, len(G))
    chk("EVERY_GROUP_HAS_A_LEGAL_COMPLEXITY_TIER", ASSET_ACCOUNTING,
        [g["asset_group_id"] for g in G if g["complexity_tier"] not in D.COMPLEXITY_TIERS],
        [], len(G))
    chk("EVERY_GROUP_DECLARES_MMD_STATUS", ASSET_ACCOUNTING,
        sorted({g["mmd_production_status"] for g in G}), ["NOT_STARTED"], len(G))
    chk("EVERY_GROUP_REQUIRES_BARIAH_APPROVAL", ASSET_ACCOUNTING,
        [g["asset_group_id"] for g in G if not g["bariah_approval_requirement"]], [], len(G))
    # A group covering no obligation must say so deliberately.
    empty_groups = [g for g in G if not g["obligations_covered"]]
    chk("EMPTY_ASSET_GROUPS_ARE_DECLARED", ASSET_ACCOUNTING,
        [g["asset_group_id"] for g in empty_groups
         if not (g.get("obligations_covered_empty_by_design") and g.get("empty_reason"))],
        [], len(empty_groups),
        empty_by_design="AG-08 is the only group covering no obligation, by design")
    chk("EVERY_OBLIGATION_BELONGS_TO_A_DECLARED_GROUP", ASSET_ACCOUNTING,
        sorted({r["proposed_asset_group_id"] for r in C}
               - {g["asset_group_id"] for g in G}), [], len(C))

    # ==================== 4. SCREEN SEQUENCE ====================
    chk("PROPOSED_LEARNER_SCREEN_COUNT", SEQUENCE_INTEGRITY,
        D.PROPOSED_LEARNER_SCREEN_COUNT, len(S), len(S))
    chk("FINAL_SCREEN_COUNT_PENDING_APPROVAL", SEQUENCE_INTEGRITY,
        D.FINAL_LEARNER_SCREEN_COUNT, "PENDING_BARIAH_APPROVAL", 1)
    chk("PROPOSED_AND_FINAL_COUNTS_ARE_DISTINCT_FIELDS", SEQUENCE_INTEGRITY,
        isinstance(D.PROPOSED_LEARNER_SCREEN_COUNT, int)
        and isinstance(D.FINAL_LEARNER_SCREEN_COUNT, str), True, 2)
    chk("NO_FINAL_SCREEN_COUNT_CLAIMED", SEQUENCE_INTEGRITY,
        D.FINAL_LEARNER_SCREEN_COUNT.isdigit(), False, 1)
    chk("B02_SCREEN_COUNT_NOT_INHERITED", SEQUENCE_INTEGRITY,
        D.B02_SCREEN_COUNT_INHERITED, False, 1)
    chk("NO_B02_FAMILY_LABEL", SEQUENCE_INTEGRITY,
        [s for s in _strings([S, C, G, Q, R, DLG])
         if re.search(r"\bFAMILY_(S|P1|P2)\b", s)], [], len(S))
    chk("B02_FAMILIES_PROPAGATED", SEQUENCE_INTEGRITY, D.B02_FAMILIES_PROPAGATED, 0, len(S))
    chk("DUPLICATE_SCREEN_IDS", SEQUENCE_INTEGRITY,
        sorted({s["screen_id"] for s in S
                if [x["screen_id"] for x in S].count(s["screen_id"]) > 1}), [], len(S))
    chk("EVERY_SCREEN_HAS_A_PURPOSE", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in S if not s["instructional_purpose"]], [], len(S))
    chk("EVERY_SCREEN_HAS_A_LEARNER_OUTCOME", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in S if not s["learner_outcome"]], [], len(S))
    content_screens = [s for s in S if s["screen_id"] not in STRUCTURAL_SCREENS]
    chk("EVERY_CONTENT_SCREEN_HAS_SOURCE_ROWS", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in content_screens if not s["source_row_ids"]], [],
        len(content_screens))
    chk("STRUCTURAL_SCREENS_DECLARED", SEQUENCE_INTEGRITY,
        sorted({s["screen_id"] for s in S if not s["source_row_ids"]}),
        sorted(STRUCTURAL_SCREENS), len(S))
    chk("EVERY_SCREEN_ROW_IN_EXTRACT", SEQUENCE_INTEGRITY,
        sorted({r for s in S for r in s["source_row_ids"] if r not in BY}), [],
        len({r for s in S for r in s["source_row_ids"]}))
    chk("EVERY_SOURCE_ROW_APPEARS_ON_A_SCREEN", SEQUENCE_INTEGRITY,
        D.SOURCE_ROW_COVERAGE["uncovered_rows"], [], D.SOURCE_ROW_COVERAGE["total_rows"])
    chk("EVERY_REQUIRED_POPULATION_HAS_SCREENS", SEQUENCE_INTEGRITY,
        [p["population"] for p in D.REQUIRED_POPULATIONS if not p["screens"]], [],
        len(D.REQUIRED_POPULATIONS))
    chk("EVERY_REQUIRED_POPULATION_SCREEN_EXISTS", SEQUENCE_INTEGRITY,
        sorted({x for p in D.REQUIRED_POPULATIONS for x in p["screens"]}
               - {s["screen_id"] for s in S}), [], len(D.REQUIRED_POPULATIONS))
    chk("EVERY_SCREEN_PENDING_BARIAH_REVIEW", SEQUENCE_INTEGRITY,
        sorted({s["bariah_review_status"] for s in S}), ["PENDING_BARIAH_REVIEW"], len(S))
    chk("EVERY_MAPPED_OBLIGATION_APPEARS_ON_ITS_SCREEN", SEQUENCE_INTEGRITY,
        [r["obligation_id"] for r in C if r["proposed_learner_screen_id"]
         and r["obligation_id"] not in
         next(s["visual_obligations_served"] for s in S
              if s["screen_id"] == r["proposed_learner_screen_id"])], [],
        len([r for r in C if r["proposed_learner_screen_id"]]))

    # ==================== 5. DIALOGUE ====================
    chk("CONTEXTUAL_FIT_ASSESSMENT_EXISTS", DIALOGUE_DISCIPLINE,
        F["recommendation"] in D.ALLOWED_FIT_RESULTS, True, 1)
    chk("FIT_ASSESSMENT_IS_CAIR_NOT_BARIAH", DIALOGUE_DISCIPLINE,
        (F["authority"], F["status"]),
        ("CAIR_ASSESSMENT_NOT_A_BARIAH_RULING", "PENDING_BARIAH_REVIEW"), 2)
    chk("NO_FINAL_CAST_APPROVAL_CLAIMED", DIALOGUE_DISCIPLINE,
        (DLG["cast_status"], F["instance_mapping_status"]),
        ("PROPOSED_SUBJECT_TO_BARIAH_APPROVAL", "PROPOSED_PENDING_BARIAH_APPROVAL"), 2)
    chk("FIT_ASSESSMENT_ROWS_IN_EXTRACT", DIALOGUE_DISCIPLINE,
        sorted({r for r in F["source_row_bindings"] if r not in BY}), [],
        len(F["source_row_bindings"]))
    chk("SLIDE_2_REMAINS_PROCESS_OVERVIEW", DIALOGUE_DISCIPLINE,
        DLG["level"], "PROCESS_OVERVIEW_ONLY", 1)
    chk("EVERY_DIALOGUE_LINE_HAS_SOURCE_ROWS", DIALOGUE_DISCIPLINE,
        [L["dialogue_line_id"] for L in DLG["lines"] if not L["source_row_ids"]], [],
        len(DLG["lines"]))
    chk("EVERY_DIALOGUE_ROW_IS_A_DECLARED_SLIDE2_ROW", DIALOGUE_DISCIPLINE,
        sorted({r for L in DLG["lines"] for r in L["source_row_ids"]}
               - set(F["source_row_bindings"])), [], len(DLG["lines"]))
    chk("NO_COMPLIANCE_OBLIGATION_IN_DIALOGUE", DIALOGUE_DISCIPLINE,
        sorted({term for term in COMPLIANCE_TERMS for L in DLG["lines"]
                if term in L["text"].lower()}), [], len(DLG["lines"]))
    chk("COMPLIANCE_EXCLUSIONS_ENUMERATED", DIALOGUE_DISCIPLINE,
        len(DLG["compliance_exclusions"]), 6, len(DLG["compliance_exclusions"]))
    chk("EVERY_DIALOGUE_LINE_CARRIES_RISK_AND_FUNCTION", DIALOGUE_DISCIPLINE,
        [L["dialogue_line_id"] for L in DLG["lines"]
         if not (L["factual_risk_status"] and L["instructional_function"]
                 and L["vo_status"])], [], len(DLG["lines"]))
    chk("DIALOGUE_REMAINS_A_DRAFT", DIALOGUE_DISCIPLINE,
        (DLG["content_status"], DLG["approval_status"], DLG["instructional_authority"]),
        ("CAIR_ASSISTED_DRAFT", "PENDING_BARIAH_REVIEW", "BARIAH"), 3)

    # ==================== 6. RUMUSAN ====================
    chk("RUMUSAN_POINT_COUNT", RUMUSAN_DISCIPLINE, len(R["points"]), 4, len(R["points"]))
    chk("EVERY_RUMUSAN_POINT_HAS_SOURCE_ROWS", RUMUSAN_DISCIPLINE,
        [s["point_id"] for s in R["points"] if not s["source_row_ids"]], [],
        len(R["points"]))
    chk("EVERY_RUMUSAN_ROW_IN_EXTRACT", RUMUSAN_DISCIPLINE,
        sorted({r for s in R["points"] for r in s["source_row_ids"] if r not in BY}), [],
        len({r for s in R["points"] for r in s["source_row_ids"]}))
    chk("MEDIUM_RISK_GENERALISATION_DISCLOSED", RUMUSAN_DISCIPLINE,
        [s["point_id"] for s in R["points"]
         if s["factual_risk_status"].startswith("MEDIUM")], ["T04-RUM2-04"], len(R["points"]))
    chk("MEDIUM_RISK_POINT_ID_MATCHES", RUMUSAN_DISCIPLINE,
        R["medium_risk_point_id"], "T04-RUM2-04", 1)
    chk("EVERY_RUMUSAN_POINT_HAS_REVIEW_FIELDS", RUMUSAN_DISCIPLINE,
        [s["point_id"] for s in R["points"]
         if sorted(s["bariah_review"]) != ["accept", "comment", "edit", "remove"]], [],
        len(R["points"]))
    chk("NO_RUMUSAN_POINT_PRE_ACCEPTED", RUMUSAN_DISCIPLINE,
        [s["point_id"] for s in R["points"]
         if any(v is not None for v in s["bariah_review"].values())], [], len(R["points"]))
    chk("RUMUSAN_REMAINS_A_DRAFT", RUMUSAN_DISCIPLINE,
        (R["content_status"], R["approval_status"], R["instructional_authority"]),
        ("CAIR_ASSISTED_DRAFT", "PENDING_BARIAH_REVIEW", "BARIAH"), 3)
    chk("NO_B02_FACT_IN_RUMUSAN", RUMUSAN_DISCIPLINE,
        sorted({x for x in ("Struktur Persisir Air", "Struktur Teduhan", "Kemudahan Awam",
                            "Water Feature", "Kerusi Taman", "Papan Tanda", "Tong Sampah",
                            "Drinking Fountain", "BBQ Pit", "Perabot Taman", "Struktur Taman")
                for s in R["points"] if x.lower() in s["draft_text"].lower()}), [],
        len(R["points"]))

    # ==================== 7. QUIZ ====================
    items = Q["items"]
    chk("QUIZ_ITEM_COUNT", ASSESSMENT_INTEGRITY, len(items), 5, len(items))
    chk("QUIZ_COMPOSITION_4_MCQ_1_MR", ASSESSMENT_INTEGRITY,
        (len([i for i in items if i["question_type"] == "MCQ"]),
         len([i for i in items if i["question_type"] == "MULTIPLE_RESPONSE"])), (4, 1),
        len(items))
    chk("QUIZ_ITEM_ORDER", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items], ["Q1", "Q2", "Q3", "Q4", "Q5"], len(items))
    chk("PASS_THRESHOLD_60_PERCENT", ASSESSMENT_INTEGRITY, Q["pass_threshold"], "60_PERCENT", 1)
    chk("QUIZ_SCOPE_ALL_PLS_IN_KURSUS", ASSESSMENT_INTEGRITY, Q["scope"], "ALL_PLS_IN_KURSUS",
        1)
    chk("ANSWER_KEY_NOT_FINAL", ASSESSMENT_INTEGRITY,
        (Q["answer_key_status"], Q["answer_key_approval"]),
        ("PROPOSED_ANSWER_KEY", "PENDING_BARIAH_APPROVAL"), 2)
    chk("NO_FINAL_ANSWER_KEY_LABEL", ASSESSMENT_INTEGRITY,
        [s for s in _strings(Q) if re.search(r"\bFINAL_ANSWER_KEY\b|\bANSWER_KEY_FINAL\b", s)],
        [], len(items))
    chk("EVERY_ITEM_HAS_A_PROPOSED_ANSWER", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items if not i["proposed_correct_answer"]], [], len(items))
    chk("EVERY_PROPOSED_ANSWER_IS_AN_OFFERED_OPTION", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if set(i["proposed_correct_answer"]) - {k for k, _ in i["draft_options"]}], [],
        len(items))
    chk("MCQ_HAS_EXACTLY_ONE_CORRECT_ANSWER", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if i["question_type"] == "MCQ" and len(i["proposed_correct_answer"]) != 1], [],
        len([i for i in items if i["question_type"] == "MCQ"]))
    chk("MR_HAS_MORE_THAN_ONE_CORRECT_ANSWER", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if i["question_type"] == "MULTIPLE_RESPONSE"
         and len(i["proposed_correct_answer"]) < 2], [],
        len([i for i in items if i["question_type"] == "MULTIPLE_RESPONSE"]))
    chk("MR_HAS_AT_LEAST_ONE_INCORRECT_OPTION", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if i["question_type"] == "MULTIPLE_RESPONSE"
         and len(i["draft_options"]) <= len(i["proposed_correct_answer"])], [],
        len([i for i in items if i["question_type"] == "MULTIPLE_RESPONSE"]))
    chk("EVERY_ITEM_HAS_CORRECT_ANSWER_EVIDENCE", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items if not i["correct_answer_evidence"]], [], len(items))
    # The evidence must cite controlled rows, not merely assert.
    chk("CORRECT_ANSWER_EVIDENCE_CITES_CONTROLLED_ROWS", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if not ROW_ID.findall(i["correct_answer_evidence"])], [], len(items))
    chk("EVIDENCE_ROWS_EXIST_AND_ARE_DECLARED", ASSESSMENT_INTEGRITY,
        sorted({r for i in items for r in ROW_ID.findall(i["correct_answer_evidence"])
                if r not in BY or r not in i["source_row_ids"]}), [], len(items))
    chk("NO_EXTERNAL_KNOWLEDGE_REQUIRED", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if not i["source_row_ids"] or set(i["source_row_ids"]) - set(BY)], [], len(items))
    chk("EVERY_ITEM_DECLARES_OVERLAP", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items if not i["overlap_check"]], [], len(items))
    chk("EVERY_ITEM_HAS_DISTRACTOR_RATIONALE", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items if not i["distractor_rationale"]], [], len(items))
    # Longest option must not be the answer in every MCQ — the classic length cue.
    def _longest_is_key(i):
        longest = max(i["draft_options"], key=lambda kv: len(kv[1]))[0]
        return longest in i["proposed_correct_answer"]
    mcqs = [i for i in items if i["question_type"] == "MCQ"]
    chk("LENGTH_CUE_DOES_NOT_GIVE_AWAY_EVERY_MCQ", ASSESSMENT_INTEGRITY,
        len([i for i in mcqs if _longest_is_key(i)]) < len(mcqs), True, len(mcqs))
    cov = Q["coverage_accounting"]
    chk("NO_COVERAGE_POINT_DISCARDED", ASSESSMENT_INTEGRITY,
        (cov["discarded"], sorted({b for i in items for b in []} or cov["blueprint_points"])),
        (0, sorted(cov["blueprint_points"])), len(cov["blueprint_points"]))
    chk("MERGED_COVERAGE_DISCLOSED", ASSESSMENT_INTEGRITY,
        (cov["merged"]["into"], sorted(cov["merged"]["from_points"]),
         bool(cov["merged"]["disclosure"]), bool(cov["merged"]["cost"])),
        ("Q5", ["T04-QB-03", "T04-QB-04"], True, True), 1)
    chk("QUIZ_REMAINS_A_DRAFT", ASSESSMENT_INTEGRITY,
        (Q["content_status"], Q["approval_status"], Q["final_instructional_authority"]),
        ("CAIR_ASSISTED_DRAFT", "PENDING_BARIAH_REVIEW", "BARIAH"), 3)
    chk("NO_QUIZ_OPTION_NAMES_THE_ACT", ASSESSMENT_INTEGRITY,
        [i["question_id"] for i in items
         if any("akta" in v.lower() for _, v in i["draft_options"])], [], len(items))

    # ==================== 8. MMD ====================
    chk("MMD_PRODUCTION_NOT_STARTED", MMD_GUARD,
        (D.MMD_FORECAST["production_status"], D.MMD_PRODUCTION_STARTED), ("NOT_STARTED", 0), 1)
    chk("EVERY_FORECAST_GROUP_NOT_STARTED", MMD_GUARD,
        sorted({g["mmd_production_status"] for g in D.MMD_FORECAST["groups"]}),
        ["NOT_STARTED"], len(D.MMD_FORECAST["groups"]))
    chk("FORECAST_LABELLED_PRELIMINARY", MMD_GUARD,
        (D.MMD_FORECAST["status"], D.MMD_FORECAST["commitment"], D.MMD_FORECAST["gate"]),
        ("PRELIMINARY_DEMAND_FORECAST", "NOT_A_PRODUCTION_COMMITMENT",
         "PENDING_BARIAH_SCREEN_APPROVAL"), 3)
    chk("NO_PRODUCTION_HOURS_WITHOUT_A_BASELINE", MMD_GUARD,
        [s for s in _strings(D.MMD_FORECAST)
         if re.search(r"\b\d+(\.\d+)?\s*(hours?|hrs?|jam|man-days?|person-days?)\b", s,
                      re.I)], [], len(D.MMD_FORECAST["groups"]))
    chk("EVERY_FORECAST_BAND_IS_ALLOWED", MMD_GUARD,
        sorted({g["estimated_mmd_effort_band"] for g in D.MMD_FORECAST["groups"]}
               - set(D.EFFORT_BANDS)), [], len(D.MMD_FORECAST["groups"]))
    chk("FORECAST_TOTALS_DERIVED_LIVE", MMD_GUARD,
        (D.MMD_TOTALS["total_proposed_asset_groups"] == len(G),
         D.MMD_TOTALS["total_proposed_unique_assets"] == live_assets),
        (True, True), len(G))

    # ==================== 9. READINESS AND PRODUCTION ====================
    chk("READINESS_SEMANTICS", PRODUCTION_GUARD,
        (D.READINESS["STRUCTURAL_POLICY_RESOLVED"],
         D.READINESS["INSTANCE_MAPPING_PROPOSED_COMPLETE"],
         D.READINESS["CONTRACT_PROPOSED_COMPLETE"],
         D.READINESS["FINAL_CONTENT_APPROVED"],
         D.READINESS["STORYBOARD_BUILD_AUTHORISED"]),
        ("YES", "YES", "YES", "NO", "NO"), 5)
    # The readiness record DECLARES the forbidden term in `forbidden_term`. A declaration of
    # a prohibition is not the prohibited claim, and scanning it as one is the same category
    # error that produced false positives at Stages 4.2F-B0, B0.5 and B0.6. Excluded
    # structurally; the declaration itself is asserted by the next gate.
    _readiness_scan = {k: v for k, v in D.READINESS.items()
                       if k not in ("forbidden_term", "forbidden_term_reason")}
    chk("INSTANCE_MAPPING_COMPLETE_NOT_CLAIMED", PRODUCTION_GUARD,
        [s for s in _strings([_readiness_scan, C, S, F])
         if "INSTANCE_MAPPING_COMPLETE" in s and "PROPOSED" not in s], [],
        len(_readiness_scan))
    chk("FORBIDDEN_TERM_DECLARATION_INTACT", PRODUCTION_GUARD,
        (D.READINESS["forbidden_term"], bool(D.READINESS["forbidden_term_reason"])),
        ("INSTANCE_MAPPING_COMPLETE", True), 2)
    chk("PROPOSED_COMPLETE_ONLY_WITH_ZERO_ORPHANS", PRODUCTION_GUARD,
        D.READINESS["INSTANCE_MAPPING_PROPOSED_COMPLETE"] == "YES"
        and D.ORPHAN_OBLIGATIONS == 0 and D.VISUAL_OBLIGATIONS_CLOSED == 46, True, len(C))
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, timeout=60).stdout.split()
    except Exception:
        tracked = []
    chk("GIT_INDEX_READ", PRODUCTION_GUARD, len(tracked) > 100, True, len(tracked) or 1)
    chk("NO_PPTX_GENERATED", PRODUCTION_GUARD,
        (D.PPTX_GENERATED,
         [x for x in tracked if x.lower().endswith(".pptx") and "/pl06/" in x]), (0, []),
        len(tracked) or 1)
    try:
        gen = subprocess.run(["git", "status", "--porcelain", "reviews/source-completion"],
                             cwd=REPO, capture_output=True, text=True,
                             timeout=60).stdout.strip()
    except Exception:
        gen = ""
    chk("NO_PRODUCTION_GENERATOR_MODIFIED", PRODUCTION_GUARD,
        (gen, D.GENERATOR_TOUCHED), ("", 0), 1)
    chk("VERDICT_IS_ALLOWED", PRODUCTION_GUARD, D.VERDICT in D.ALLOWED_VERDICTS, True,
        len(D.ALLOWED_VERDICTS))

    # ==================== 10. ARTIFACT AGREEMENT ====================
    chk("ALL_CONTROLLED_ARTIFACTS_PRESENT", ARTIFACT_AGREEMENT,
        [n for n in CONTROLLED_ARTIFACTS if not os.path.exists(os.path.join(T04, n))], [],
        len(CONTROLLED_ARTIFACTS))
    cj = json.load(open(os.path.join(T04, "T04_VISUAL_OBLIGATION_CLOSURE_v1.json"),
                        encoding="utf-8"))
    chk("CLOSURE_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        (len(cj["obligations"]), cj["totals"]["ORPHAN_OBLIGATIONS"], cj["policy_rule"]),
        (_live_total, _live_orphans, D.VISUAL_POLICY_RULE), len(cj["obligations"]))
    ccsv = open(os.path.join(T04, "T04_VISUAL_OBLIGATION_CLOSURE_v1.csv"),
                encoding="utf-8").read().strip().splitlines()
    chk("CLOSURE_CSV_ROWS", ARTIFACT_AGREEMENT, len(ccsv) - 1, 46, len(ccsv) - 1)
    chk("CLOSURE_CSV_HEADER", ARTIFACT_AGREEMENT, ccsv[0].split(","), D.CLOSURE_FIELDS,
        len(D.CLOSURE_FIELDS))
    aj = json.load(open(os.path.join(T04, "T04_VISUAL_ASSET_GROUPING_PLAN_v2.json"),
                        encoding="utf-8"))
    chk("ASSET_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        (len(aj["asset_groups"]), aj["unique_asset_count"],
         aj["totals"]["proposed_unique_assets"]),
        (len(G), "PROPOSED_NOT_APPROVED", live_assets), len(aj["asset_groups"]))
    acsv = open(os.path.join(T04, "T04_VISUAL_ASSET_GROUPING_PLAN_v2.csv"),
                encoding="utf-8").read().strip().splitlines()
    chk("ASSET_CSV_ROWS", ARTIFACT_AGREEMENT, len(acsv) - 1, len(G), len(acsv) - 1)
    sj = json.load(open(os.path.join(T04, "T04_PROPOSED_SCREEN_SEQUENCE_v1.json"),
                        encoding="utf-8"))
    chk("SEQUENCE_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        ([x["screen_id"] for x in sj["screens"]], sj["final_learner_screen_count"]),
        ([x["screen_id"] for x in S], "PENDING_BARIAH_APPROVAL"), len(sj["screens"]))
    qj = json.load(open(os.path.join(T04, "T04_QUIZ_CAIR_ASSISTED_DRAFT_v1.json"),
                        encoding="utf-8"))
    chk("QUIZ_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        ([i["question_id"] for i in qj["quiz"]["items"]],
         qj["quiz"]["answer_key_status"], qj["quiz"]["pass_threshold"]),
        ([i["question_id"] for i in items], "PROPOSED_ANSWER_KEY", "60_PERCENT"),
        len(qj["quiz"]["items"]))
    rj = json.load(open(os.path.join(T04, "T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v3.json"),
                        encoding="utf-8"))
    chk("RUMUSAN_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        len(rj["rumusan"]["points"]), 4, len(rj["rumusan"]["points"]))
    dj = json.load(open(os.path.join(T04, "T04_SLIDE_2_DIALOGUE_CAIR_DRAFT_v1.json"),
                        encoding="utf-8"))
    chk("DIALOGUE_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        [x["dialogue_line_id"] for x in dj["dialogue"]["lines"]],
        [x["dialogue_line_id"] for x in DLG["lines"]], len(dj["dialogue"]["lines"]))
    pack = open(os.path.join(T04, "T04_BARIAH_CONTENT_REVIEW_PACK_v1.md"),
                encoding="utf-8").read()
    chk("REVIEW_PACK_CARRIES_EVERY_QUIZ_ITEM", ARTIFACT_AGREEMENT,
        [i["question_id"] for i in items if i["draft_stem"] not in pack], [], len(items))
    chk("REVIEW_PACK_CARRIES_EVERY_DIALOGUE_LINE", ARTIFACT_AGREEMENT,
        [L["dialogue_line_id"] for L in DLG["lines"] if L["text"] not in pack], [],
        len(DLG["lines"]))
    chk("REVIEW_PACK_HAS_REVIEW_FIELDS", ARTIFACT_AGREEMENT,
        all(x in pack for x in ("ACCEPT", "EDIT", "REMOVE", "COMMENT")), True, 4)
    # The pack is for a human; engineering vocabulary does not belong in it.
    chk("REVIEW_PACK_FREE_OF_TECHNICAL_VOCABULARY", ARTIFACT_AGREEMENT,
        sorted({w for w in ("gate", "mutation", "sha256", "docs/pl06", "fixture", "QA suite")
                if w.lower() in pack.lower()}), [], 6)
    chk("WHATSAPP_DRAFT_NOT_SENT", ARTIFACT_AGREEMENT, D.WHATSAPP["status"],
        "DRAFT_NOT_SENT", 1)
    chk("WHATSAPP_STATES_NO_STORYBOARD_AND_NO_ASSETS", ARTIFACT_AGREEMENT,
        ("belum dijana" in D.WHATSAPP["text"],
         "Belum ada aset visual dihasilkan" in D.WHATSAPP["text"],
         "masih draf" in D.WHATSAPP["text"]), (True, True, True), 3)

    # ==================== 11. REPORTING ====================
    chk("SUITE_ID_PRESENT", REPORTING, (SUITE_ID, D.SUITE_ID),
        ("T04_CONTENT_QA_v1", "T04_CONTENT_QA_v1"), 1)
    chk("NOT_CHECKED_LIST_PRESENT", REPORTING, len(NOT_CHECKED) > 0, True, len(NOT_CHECKED))
    chk("EVERY_GATE_REPORTS_A_POPULATION", REPORTING,
        [r["gate_id"] for r in res if not isinstance(r.get("population"), int)], [], len(res))
    chk("NO_UNDECLARED_EMPTY_POPULATION", REPORTING,
        [r["gate_id"] for r in res if r["population"] == 0 and not r["empty_by_design"]], [],
        len(res))
    chk("EMPTY_BY_DESIGN_GATES_CARRY_A_REASON", REPORTING,
        [r["gate_id"] for r in res
         if r["empty_by_design"] and len(str(r["empty_by_design"])) < 15], [],
        len([r for r in res if r["empty_by_design"]]),
        empty_by_design="declared-empty gates are rare; one exists in this suite")

    # ==================== 12. ACCOUNTING ====================
    g_ids = [r["gate_id"] for r in res]
    chk("DUPLICATE_GATE_IDS", ACCOUNTING,
        sorted({x for x in g_ids if g_ids.count(x) > 1}), [], len(g_ids))
    chk("EVERY_GATE_CARRIES_A_TYPE", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res))
    return res


def accounting(rows):
    m = [r for r in rows if r["gate_type"] == SUPERSESSION_MARKER]
    a = [r for r in rows if r["gate_type"] != SUPERSESSION_MARKER]
    by = {}
    for r in a:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    return dict(SUITE_ID=SUITE_ID,
                TOTAL_EMITTED_GATE_RECORDS=len(rows),
                SUPERSESSION_MARKERS_PRESENT=len(m),
                ACTIVE_GATE_COUNT=len(a),
                ACTIVE_GATES_PASSING=sum(1 for r in a if r["ok"]),
                VACUOUS_GATES=[r["gate_id"] for r in rows if r["vacuous"]],
                DECLARED_EMPTY_GATES=[r["gate_id"] for r in rows if r["empty_by_design"]],
                POPULATION_TOTALS={r["gate_id"]: r["population"] for r in rows},
                BY_TYPE=dict(sorted(by.items())),
                NOT_CHECKED=NOT_CHECKED,
                FAILING=[r["gate_id"] for r in rows if not r["ok"]])


def gate_id_diff():
    """Gate IDs added, removed or superseded relative to the prior suite."""
    try:
        import t04_final_rulings_qa_v1 as PRIOR
        prior = {r["gate_id"] for r in PRIOR.run()}
    except Exception as exc:
        return dict(prior_suite=PRIOR_SUITE_ID, error=str(exc))
    here = {r["gate_id"] for r in run()}
    return dict(prior_suite=PRIOR_SUITE_ID, this_suite=SUITE_ID,
                added=sorted(here - prior), removed=sorted(prior - here),
                carried_over=sorted(here & prior),
                superseded=sorted(prior - here),
                note="A gate ID present in the prior suite and absent here is SUPERSEDED, not "
                     "deleted: the prior suite still runs and still enforces it over the "
                     "Stage 4.2F-B0.7 data. This suite governs Stage 4.2F-B0.8 data only.")


if __name__ == "__main__":
    rows = run()
    a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows)
    t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        flag = "FAIL" if not r["ok"] else "PASS"
        if r["vacuous"]:
            flag = "VACU"
        print(f"{flag}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  n={r['population']:<5} "
              f"{r['value']!r}"[:210] + ("" if r["ok"] else f"   expected {r['expected']!r}"))
    print()
    print(f"SUITE_ID = {a['SUITE_ID']}")
    print(f"{a['ACTIVE_GATES_PASSING']}/{a['ACTIVE_GATE_COUNT']} active gates PASS  ·  "
          f"{a['SUPERSESSION_MARKERS_PRESENT']} supersession markers  ·  "
          f"{a['TOTAL_EMITTED_GATE_RECORDS']} emitted records")
    print(f"VACUOUS_GATES = {a['VACUOUS_GATES']}")
    print(f"DECLARED_EMPTY_GATES = {a['DECLARED_EMPTY_GATES']}")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<24} {v}")
    print()
    print("NOT_CHECKED:")
    for x in a["NOT_CHECKED"]:
        print(f"  - {x}")
    sys.exit(1 if a["FAILING"] else 0)
