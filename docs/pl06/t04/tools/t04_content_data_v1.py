# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.8 — the ONE controlled data source for T04 content and instance mapping.

Everything downstream (Markdown, CSV, JSON) is emitted from here, so the representations
cannot drift.

NOTHING HERE IS APPROVED INSTRUCTIONAL CONTENT.
Bariah is the sole Instructional Designer. This stage prepares proposals — a screen sequence,
a closure for all 46 visual obligations, a dialogue, a Rumusan and five quiz items — for her
to accept, edit, remove or replace.

AUTHORITY, kept in three separate fields on every obligation
------------------------------------------------------------
    requirement authority          BARIAH_DIRECT_SCREENSHOT
                                   Bariah ruled that a visual is required.
    population derivation          MODULE_HEADING_HIERARCHY
                                   WHICH descendants exist is decided by the module's heading
                                   structure, not by Bariah. She wrote "their sub"; the module
                                   says what the subs are.
    subject authority              MODULE_SOURCE_ATTESTED
                                   WHAT each visual shows comes from the module.

The Stage 4.2F-B0.6 rule name VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION was misleading:
Bariah named three groups, not 46 obligations. The population was derived. Renamed here.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_data_v1 as SRC
import t04_rulings_data_v1 as B06
import t04_final_rulings_data_v1 as B07

STAGE = "4.2F-B0.8"
SUITE_ID = "T04_CONTENT_QA_v1"
UNIT_ID = "K5-PL06-T04-B01"
LESSON_TITLE = "Penjagaan dan Penyelenggaraan"
GENERATED_BY = "docs/pl06/t04/tools/t04_content_emit_v1.py"

CONTENT_STATUS = "CAIR_ASSISTED_DRAFT"
APPROVAL_STATUS = "PENDING_BARIAH_REVIEW"
INSTRUCTIONAL_AUTHORITY = "BARIAH"
FORBIDDEN_LABELS = ["BARIAH_APPROVED", "FINAL_INSTRUCTIONAL_CONTENT", "ID_AUTHORED_BY_CAIR",
                    "READY_FOR_PRODUCTION"]

REQUIREMENT_AUTHORITY = "BARIAH_DIRECT_SCREENSHOT"
POPULATION_DERIVATION_AUTHORITY = "MODULE_HEADING_HIERARCHY"
SUBJECT_AUTHORITY = "MODULE_SOURCE_ATTESTED"

VISUAL_POLICY_RULE = "VISUAL_REQUIRED_FOR_BARIAH_RULED_SOURCE_POPULATION"
SUPERSEDED_POLICY_RULE = "VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION"
POLICY_RENAME_REASON = (
    "The old name implied Bariah named the population. She did not — she named three groups "
    "and wrote 'Their sub – perlu visual'. The 46 descendants were derived from the module's "
    "heading hierarchy. The policy is hers; the population is the module's. Conflating the "
    "two would attribute 46 individual rulings to a person who gave three.")

BY_ID = SRC.BY_ID
ROWS = SRC.ROWS
VISUAL_OBLIGATIONS = B06.VISUAL_OBLIGATIONS

# ==========================================================================================
# PART 1 — DECISION PROVENANCE, PRESERVED AND CORRECTED
# ==========================================================================================
DECISIONS = [
    dict(decision_id="D-01", title="Visual policy",
         status="CONFIRMED_WITH_EXPANSION", ruling=VISUAL_POLICY_RULE,
         superseded_ruling_name=SUPERSEDED_POLICY_RULE,
         evidence=["BR-L1", "BR-L2", "BR-L3", "BR-L4", "BR-L5", "BR-L6"],
         requirement_authority=REQUIREMENT_AUTHORITY,
         population_derivation_authority=POPULATION_DERIVATION_AUTHORITY,
         subject_authority=SUBJECT_AUTHORITY,
         scope="THIS_UNIT_ONLY"),
    dict(decision_id="D-02A", title="Quiz composition",
         status="CONFIRMED_BARIAH_DIRECT", ruling="4 MCQ + 1 MULTIPLE_RESPONSE",
         evidence=["BR-W2"], scope="ALL_PLS_IN_KURSUS"),
    dict(decision_id="D-02B", title="Passing threshold",
         status="CONFIRMED_BARIAH_DIRECT", ruling="60_PERCENT",
         evidence=["BR-C2"], scope="ALL_PLS_IN_KURSUS"),
    dict(decision_id="D-02C", title="Rumusan",
         status="DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW",
         ruling="FOLLOW_WRITING_STYLE_TOPIK_3_BAHAGIAN_2",
         evidence=["BR-W1", "BR-W3"], scope="THIS_UNIT_ONLY"),
    dict(decision_id="D-03", title="Slide 2 dialogue and cast",
         status="CONFIRMED_WITH_CONDITION",
         ruling="SLIDE_2_DIALOGUE_SCENARIO_WITH_ADDITIONAL_CHARACTER",
         evidence=["BR-C3", "BR-C5"], scope="THIS_UNIT_ONLY",
         preferred_cast=["Alya", "Encik Rahman"],
         reuse_condition="USE_IF_CONTEXTUALLY_APPROPRIATE"),
    dict(decision_id="D-04", title="Legislative content base/reveal split",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="BASE_OPERATOR_AND_PPE__REVEAL_ELIGIBLE_SDS_STORAGE_SPRAY_NOTIFY_REPORT",
         evidence=["BR-C1"], scope=UNIT_ID,
         treatment_authority=REQUIREMENT_AUTHORITY),
    dict(decision_id="D-05", title="SmartArt production treatment",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="SOURCE_BOUND_IN_REVIEW__CONTROLLED_REDRAW_IN_MMD__SIX_NODE_ORDER_INVARIANT",
         evidence=["BR-L1", "BR-C4"], scope="THIS_UNIT_ONLY",
         mmd_production_status="NOT_STARTED"),
]

# D-04 carries TWO provenances and they must not be merged into one.
D04_PROVENANCE = dict(
    decision_id="D-04",
    treatment_authority=REQUIREMENT_AUTHORITY,
    treatment_authority_covers=[
        dict(item="licensed operator requirement", rows=["T04-ROW-067"],
             legible_text="…rator berlesen … dipaparkan terus pada skrin"),
        dict(item="PPE", rows=["T04-ROW-069", "T04-ROW-070"],
             legible_text="dan PPE dipaparkan terus pada skrin"),
        dict(item="reveal-eligible set", rows=["T04-ROW-071", "T04-ROW-072", "T04-ROW-073",
                                               "T04-ROW-074", "T04-ROW-076", "T04-ROW-077",
                                               "T04-ROW-078"],
             legible_text="…S, penyimpanan, penyemburan, notifikasi dan laporan boleh guna cli…"),
    ],
    akta_base_screen_placement="FIRDAUS_ATTESTED_FROM_CROPPED_CONFIRMED_PROPOSAL",
    akta_rows=["T04-ROW-066"],
    akta_note="The left margin of the confirming screenshot is cropped and the word 'Akta' "
              "appears nowhere in it. Bariah confirmed the whole proposal she was sent, and "
              "Firdaus's stage instruction states the base screen must show the Act — but the "
              "text itself is not legible. The placement is therefore attested, not read.",
    prohibition="The unreadable Akta text must NOT be classified as a directly legible Bariah "
                "statement.")

# ==========================================================================================
# PART 2 — CLOSURE OF THE 46-OBLIGATION POPULATION
# ==========================================================================================
CLOSURE_OUTCOMES = ["MAPPED_TO_LEARNER_SCREEN", "MAPPED_TO_RUNTIME_STATE",
                    "COVERED_BY_COMPOSITE_ASSET_GROUP", "MERGED_WITH_NAMED_OBLIGATION",
                    "NOT_A_SEPARATE_ASSET_WITH_REASON"]
FORBIDDEN_OUTCOME = "UNMAPPED_WITHOUT_REASON"

COMPLEXITY_TIERS = ["SIMPLE_ICONIC", "SIMPLE_DIAGRAM", "PROCEDURAL_ILLUSTRATION",
                    "COMPOSITE_PROCESS_DIAGRAM", "COMPARISON_VISUAL",
                    "SAFETY_COMPLIANCE_VISUAL", "SOURCE_GROUNDED_PHOTO_DIRECTION",
                    "COMPLEX_CUSTOM_ILLUSTRATION"]

_L, _R = "MAPPED_TO_LEARNER_SCREEN", "MAPPED_TO_RUNTIME_STATE"
_C, _M = "COVERED_BY_COMPOSITE_ASSET_GROUP", "MERGED_WITH_NAMED_OBLIGATION"
_N = "NOT_A_SEPARATE_ASSET_WITH_REASON"

_GROUPING_REASON = (
    "A grouping heading with no body text of its own. Its four management topics each carry "
    "their own obligation and their own visual; a separate visual for the header would have "
    "to invent a subject the source does not supply. Class is PENDING_HUMAN precisely because "
    "no subject can be derived.")

# obligation_id -> (outcome, screen, state, asset_group, unique_asset, composite, tier,
#                   complexity, rationale)
_CLOSURE = {
    # --- A. six process nodes: one runtime state each on the process screen ---------------
    "T04-VO-001": (_R, "T04-S03", "ST-01", "AG-01", "UA-01-01", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "MEDIUM",
                   "One step visual per node, revealed as the learner steps the flow. Node "
                   "identity and order are D-05 invariants."),
    "T04-VO-002": (_R, "T04-S03", "ST-02", "AG-01", "UA-01-02", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "MEDIUM", "As T04-VO-001."),
    "T04-VO-003": (_R, "T04-S03", "ST-03", "AG-01", "UA-01-03", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "MEDIUM", "As T04-VO-001."),
    "T04-VO-004": (_R, "T04-S03", "ST-04", "AG-01", "UA-01-04", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "MEDIUM", "As T04-VO-001."),
    "T04-VO-005": (_R, "T04-S03", "ST-05", "AG-01", "UA-01-05", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "MEDIUM", "As T04-VO-001."),
    "T04-VO-006": (_R, "T04-S03", "ST-06", "AG-01", "UA-01-06", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "MEDIUM",
                   "The least concrete of the six; a simple diagram rather than an activity "
                   "illustration."),
    # --- B. Landskap Lembut ---------------------------------------------------------------
    "T04-VO-007": (_L, "T04-S04", None, "AG-02", "UA-02-01", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW",
                   "The category-establishing visual and the screen's persistent main visual."),
    # --- Siram -----------------------------------------------------------------------------
    "T04-VO-008": (_L, "T04-S05", None, "AG-03", "UA-03-01", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Main explanation visual for the operation."),
    "T04-VO-009": (_C, "T04-S06", None, "AG-03", None, "COMPOSITE",
                   "COMPARISON_VISUAL", "LOW",
                   "'Kaedah Pelaksanaan' has no subject beyond the methods it groups. The "
                   "composite IS the two method visuals shown together, so it consumes no "
                   "additional asset. The heading still receives a visual — the composite."),
    "T04-VO-010": (_R, "T04-S06", "ST-01", "AG-03", "UA-03-02", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Hose and spray nozzle — the equipment the source names."),
    "T04-VO-011": (_R, "T04-S06", "ST-02", "AG-03", "UA-03-03", "COMPOSITE",
                   "COMPARISON_VISUAL", "MEDIUM",
                   "Sprinkler against drip in one frame. The two systems are LIST_ITEM rows, "
                   "not headings, so they were never separate obligations; they are the two "
                   "halves of this one."),
    "T04-VO-012": (_N, None, None, "AG-03", None, "NOT_APPLICABLE",
                   "SIMPLE_ICONIC", "NONE", _GROUPING_REASON),
    "T04-VO-013": (_R, "T04-S07", "ST-01", "AG-03", "UA-03-04", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW",
                   "Watering schedule with early-morning and late-afternoon slots."),
    "T04-VO-014": (_R, "T04-S07", "ST-02", "AG-03", "UA-03-05", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "MEDIUM",
                   "Site-wide water supply, pressure, pump and timer."),
    "T04-VO-015": (_R, "T04-S07", "ST-03", "AG-03", "UA-03-06", "COMPOSITE",
                   "COMPARISON_VISUAL", "MEDIUM",
                   "Under-watering against over-watering; both failure directions must be in "
                   "one frame or the teaching point is lost."),
    "T04-VO-016": (_R, "T04-S07", "ST-04", "AG-03", "UA-03-07", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW", "Water cost against watering method."),
    # --- Baja ------------------------------------------------------------------------------
    "T04-VO-017": (_L, "T04-S08", None, "AG-04", "UA-04-01", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Main explanation visual for the operation."),
    "T04-VO-018": (_C, "T04-S09", None, "AG-04", None, "COMPOSITE",
                   "COMPARISON_VISUAL", "LOW",
                   "As T04-VO-009 — the composite is the three method visuals shown together "
                   "and consumes no additional asset."),
    "T04-VO-019": (_R, "T04-S09", "ST-01", "AG-04", "UA-04-02", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Granular fertiliser spread evenly — the broadcasting action."),
    "T04-VO-020": (_R, "T04-S09", "ST-02", "AG-04", "UA-04-03", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "MEDIUM",
                   "Dig, place, cover — a three-step action needing sequence in one frame."),
    "T04-VO-021": (_R, "T04-S09", "ST-03", "AG-04", "UA-04-04", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Liquid fertiliser onto foliage — distinguishes leaf from soil application."),
    "T04-VO-022": (_N, None, None, "AG-04", None, "NOT_APPLICABLE",
                   "SIMPLE_ICONIC", "NONE", _GROUPING_REASON),
    "T04-VO-023": (_R, "T04-S10", "ST-01", "AG-04", "UA-04-05", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW",
                   "Programme sheet with the fields the source names — type, NPK, quantity, "
                   "schedule."),
    "T04-VO-024": (_R, "T04-S10", "ST-02", "AG-04", "UA-04-06", "INDIVIDUAL",
                   "SAFETY_COMPLIANCE_VISUAL", "MEDIUM",
                   "Specification check and S.O. approval shown as a gate."),
    "T04-VO-025": (_R, "T04-S10", "ST-03", "AG-04", "UA-04-07", "INDIVIDUAL",
                   "SAFETY_COMPLIANCE_VISUAL", "MEDIUM",
                   "Dry, secure, away from water. Deliberately NOT reused for pesticide "
                   "storage, which is locked, labelled and ventilated."),
    "T04-VO-026": (_R, "T04-S10", "ST-04", "AG-04", "UA-04-08", "INDIVIDUAL",
                   "SAFETY_COMPLIANCE_VISUAL", "MEDIUM",
                   "Gloves and face mask for chemical fertiliser. Deliberately NOT reused for "
                   "pesticide PPE, which is a materially heavier set."),
    "T04-VO-027": (_R, "T04-S10", "ST-05", "AG-04", "UA-04-09", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW",
                   "The record as evidence for a payment claim, which is the reason the "
                   "source gives."),
    # --- Racun ------------------------------------------------------------------------------
    "T04-VO-028": (_L, "T04-S11", None, "AG-05", "UA-05-01", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW",
                   "The three threats — insect pests, fungal disease, weeds."),
    "T04-VO-029": (_L, "T04-S12", None, "AG-05", "UA-05-02", "COMPOSITE",
                   "COMPOSITE_PROCESS_DIAGRAM", "MEDIUM",
                   "The IPM priority ORDER is the teaching point, so it is the screen's "
                   "persistent main visual rather than a reveal."),
    "T04-VO-030": (_R, "T04-S12", "ST-01", "AG-05", "UA-05-03", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Prevention through correct watering and balanced fertilising — connects "
                   "back to the two operations already taught."),
    "T04-VO-031": (_R, "T04-S12", "ST-02", "AG-05", "UA-05-04", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW", "Manual removal and weeding."),
    "T04-VO-032": (_R, "T04-S12", "ST-03", "AG-05", "UA-05-05", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "MEDIUM",
                   "A pest's natural enemy — no obvious photograph, so a relationship diagram."),
    "T04-VO-033": (_R, "T04-S12", "ST-04", "AG-05", "UA-05-06", "INDIVIDUAL",
                   "PROCEDURAL_ILLUSTRATION", "LOW",
                   "Controlled and targeted application, not blanket spraying."),
    "T04-VO-034": (_L, "T04-S13", None, "AG-05", "UA-05-07", "COMPOSITE",
                   "COMPARISON_VISUAL", "MEDIUM",
                   "Type paired with target for all three. This is the screen's main visual."),
    "T04-VO-035": (_C, "T04-S13", None, "AG-05", None, "COMPOSITE",
                   "COMPARISON_VISUAL", "NONE",
                   "Insecticide and its target are one labelled panel inside T04-VO-034's "
                   "comparison. Splitting the three apart would destroy the pairing the "
                   "source teaches. The obligation is discharged by that panel."),
    "T04-VO-036": (_C, "T04-S13", None, "AG-05", None, "COMPOSITE",
                   "COMPARISON_VISUAL", "NONE", "As T04-VO-035 — fungicide panel."),
    "T04-VO-037": (_C, "T04-S13", None, "AG-05", None, "COMPOSITE",
                   "COMPARISON_VISUAL", "NONE", "As T04-VO-035 — herbicide panel."),
    "T04-VO-038": (_N, None, None, "AG-06", None, "NOT_APPLICABLE",
                   "SIMPLE_ICONIC", "NONE", _GROUPING_REASON),
    "T04-VO-039": (_L, "T04-S14", None, "AG-06", "UA-06-01", "INDIVIDUAL",
                   "SAFETY_COMPLIANCE_VISUAL", "HIGH",
                   "Statutory control and a licensed operator's credential. The unit's "
                   "highest-consequence visual; accuracy matters more than style here."),
    "T04-VO-040": (_L, "T04-S15", None, "AG-06", "UA-06-02", "COMPOSITE",
                   "SAFETY_COMPLIANCE_VISUAL", "HIGH",
                   "Full pesticide PPE. Base-visible under D-04 and may not be moved behind "
                   "a reveal."),
    "T04-VO-041": (_L, "T04-S16", None, "AG-06", "UA-06-03", "COMPOSITE",
                   "SAFETY_COMPLIANCE_VISUAL", "HIGH",
                   "Calm-weather spraying, signage and the spray record — three separate "
                   "obligations in one frame."),
    # --- C. Landskap Kejur -------------------------------------------------------------------
    "T04-VO-042": (_L, "T04-S17", None, "AG-07", "UA-07-01", "INDIVIDUAL",
                   "SIMPLE_DIAGRAM", "LOW",
                   "The category and its contrast with soft landscape."),
    "T04-VO-043": (_R, "T04-S18", "ST-01", "AG-07", "UA-07-02", "COMPOSITE",
                   "SIMPLE_DIAGRAM", "MEDIUM",
                   "Space-making and circulation are one function group in the source."),
    "T04-VO-044": (_R, "T04-S18", "ST-02", "AG-07", "UA-07-03", "COMPOSITE",
                   "SIMPLE_DIAGRAM", "MEDIUM",
                   "Retaining wall and drainage — both engineering roles in one image."),
    "T04-VO-045": (_R, "T04-S18", "ST-03", "AG-07", "UA-07-04", "INDIVIDUAL",
                   "SOURCE_GROUNDED_PHOTO_DIRECTION", "MEDIUM",
                   "Usability is shown by people using the space; the only obligation in the "
                   "unit where photo direction is the natural treatment."),
    "T04-VO-046": (_R, "T04-S18", "ST-04", "AG-07", "UA-07-05", "COMPOSITE",
                   "COMPARISON_VISUAL", "MEDIUM",
                   "Contrast needs two things in one frame — that is the source's own point."),
}

_REUSE_POLICY = {
    "T04-VO-025": ("DO_NOT_REUSE", "Fertiliser storage is dry, secure and away from water. "
                                   "Pesticide storage is locked, labelled and ventilated. One "
                                   "asset would understate the pesticide requirement."),
    "T04-VO-026": ("DO_NOT_REUSE", "Fertiliser PPE is gloves and a face mask. Pesticide PPE "
                                   "is respirator, goggles, chemical gloves and suit. One "
                                   "asset would understate the pesticide requirement."),
    "T04-VO-040": ("DO_NOT_REUSE", "See T04-VO-025 and T04-VO-026 — this is the heavier "
                                   "pesticide set that must not be shared with the Baja "
                                   "screens."),
}


def _obligation_closure():
    out = []
    for v in VISUAL_OBLIGATIONS:
        vid = v["visual_obligation_id"]
        if vid not in _CLOSURE:
            raise RuntimeError(f"obligation not closed: {vid}")
        outcome, screen, state, ag, ua, comp, tier, cplx, why = _CLOSURE[vid]
        if outcome not in CLOSURE_OUTCOMES:
            raise RuntimeError(f"{vid}: illegal closure outcome {outcome}")
        if tier not in COMPLEXITY_TIERS:
            raise RuntimeError(f"{vid}: illegal complexity tier {tier}")
        reuse, reuse_note = _REUSE_POLICY.get(vid, ("NOT_YET_ASSESSED", ""))
        serves = []
        if screen:
            serves.append(screen + (f"/{state}" if state else " (base)"))
        out.append(dict(
            obligation_id=vid,
            source_row_ids=list(v["source_row_ids"]),
            source_heading=v["governed_display_heading"],
            visual_subject=v["learner_facing_subject"],
            requirement_authority=REQUIREMENT_AUTHORITY,
            population_derivation_authority=POPULATION_DERIVATION_AUTHORITY,
            subject_authority=SUBJECT_AUTHORITY,
            closure_outcome=outcome,
            proposed_learner_screen_id=screen,
            proposed_runtime_state_id=state,
            proposed_asset_group_id=ag,
            unique_asset_candidate_id=ua,
            composite_or_individual=comp,
            reuse_policy=reuse,
            reuse_note=reuse_note,
            screens_or_states_served="; ".join(serves) or "none — see rationale",
            visual_class=v["proposed_visual_class"],
            complexity_tier=tier,
            production_complexity=cplx,
            mmd_dependency="MMD_ASSET_PRODUCTION_NOT_STARTED",
            approval_status=APPROVAL_STATUS,
            rationale=why))
    return out


OBLIGATION_CLOSURE = _obligation_closure()
CLOSURE_FIELDS = [
    "obligation_id", "source_row_ids", "source_heading", "visual_subject",
    "requirement_authority", "population_derivation_authority", "subject_authority",
    "closure_outcome", "proposed_learner_screen_id", "proposed_runtime_state_id",
    "proposed_asset_group_id", "unique_asset_candidate_id", "composite_or_individual",
    "reuse_policy", "screens_or_states_served", "visual_class", "complexity_tier",
    "production_complexity", "mmd_dependency", "approval_status", "rationale",
]

VISUAL_OBLIGATIONS_TOTAL = len(OBLIGATION_CLOSURE)
VISUAL_OBLIGATIONS_CLOSED = len([r for r in OBLIGATION_CLOSURE
                                 if r["closure_outcome"] in CLOSURE_OUTCOMES])
ORPHAN_OBLIGATIONS = len([r for r in OBLIGATION_CLOSURE
                          if r["closure_outcome"] not in CLOSURE_OUTCOMES
                          or (r["closure_outcome"] in (_L, _R)
                              and not r["proposed_learner_screen_id"])])

CLOSURE_BY_OUTCOME = {o: len([r for r in OBLIGATION_CLOSURE if r["closure_outcome"] == o])
                      for o in CLOSURE_OUTCOMES}

# ==========================================================================================
# PART 3 — ASSET GROUPING PLAN v2
# ==========================================================================================
def _ag_rows(gid):
    return [r for r in OBLIGATION_CLOSURE if r["proposed_asset_group_id"] == gid]


def _ag_assets(gid):
    return sorted({r["unique_asset_candidate_id"] for r in _ag_rows(gid)
                   if r["unique_asset_candidate_id"]})


_AG_META = {
    "AG-01": ("Aliran proses enam langkah",
              "The six supervisory activities as a linear flow, each step given its own "
              "visual on top of the source diagram.",
              "COMPOSITE_PROCESS_DIAGRAM", ["T04-S03"],
              "T04-DGM-01 exists as vector SmartArt and supplies the six node labels; it "
              "supplies no step illustration.", True, "HIGH"),
    "AG-02": ("Landskap Lembut — kategori",
              "The living elements the source names, shown as one category.",
              "SIMPLE_DIAGRAM", ["T04-S04", "T04-S02"],
              "Source definition row only; no image in the module.", False, "LOW"),
    "AG-03": ("Siram — operasi dan sub-topik",
              "Watering: the operation, its two implementation routes and its four "
              "management topics.",
              "PROCEDURAL_ILLUSTRATION", ["T04-S05", "T04-S06", "T04-S07"],
              "Source text only; no image in the module.", False, "MEDIUM"),
    "AG-04": ("Baja — operasi dan sub-topik",
              "Fertilising: the operation, its three application methods and its five "
              "management topics.",
              "PROCEDURAL_ILLUSTRATION", ["T04-S08", "T04-S09", "T04-S10"],
              "Source text only; no image in the module.", False, "MEDIUM"),
    "AG-05": ("Racun — IPM, kawalan dan jenis racun",
              "Pest control: the three threats, the IPM priority order, the four control "
              "methods and the three pesticide types.",
              "COMPARISON_VISUAL", ["T04-S11", "T04-S12", "T04-S13"],
              "Source text only; no image in the module.", False, "MEDIUM"),
    "AG-06": ("Racun — perundangan, HSE dan risiko",
              "Statutory control, licensed operator, full PPE, storage, SDS, spray "
              "conditions, signage and records.",
              "SAFETY_COMPLIANCE_VISUAL", ["T04-S14", "T04-S15", "T04-S16"],
              "Source text only. The 1974 Act citation is quoted, never asserted.", False,
              "HIGH"),
    "AG-07": ("Landskap Kejur — kategori dan empat fungsi",
              "Hard landscape as a category and its four functional groups.",
              "SIMPLE_DIAGRAM", ["T04-S17", "T04-S18"],
              "Source text only; no image in the module.", False, "MEDIUM"),
}

# AG-08 covers no obligation, and that is deliberate: the Slide 2 scenario visual arrives
# from BR-C3 (a dialogue ruling), not from BR-L1..L6 (the visual ruling over content
# headings). Declared empty rather than padded.
AG08 = dict(
    asset_group_id="AG-08",
    label="Slide 2 — senario pengenalan",
    obligations_covered=[],
    obligations_covered_empty_by_design=True,
    empty_reason="The Slide 2 scenario visual is NOT one of the 46 obligations. Bariah's "
                 "visual ruling (BR-L1…BR-L6) covers content headings; the scenario screen "
                 "arrives from the separate dialogue ruling BR-C3. Counting it among the 46 "
                 "would inflate a population she ruled over.",
    visual_concept="A completed planting area with built landscape elements visible, two "
                   "characters on site.",
    composite_or_individual="INDIVIDUAL",
    proposed_unique_assets=2,
    unique_asset_candidate_ids=["UA-08-01", "UA-08-02"],
    reuse_conditions="Character models may reuse the approved B02 Alya and Encik Rahman "
                     "designs IF Bariah confirms the cast; the site backdrop is T04-specific.",
    source_grounding="Rows T04-ROW-002, T04-ROW-005 and T04-ROW-080 describe the setting; no "
                     "image exists in the module.",
    complexity_tier="SOURCE_GROUNDED_PHOTO_DIRECTION",
    affected_screens=["T04-S02"],
    mmd_production_status="NOT_STARTED",
    bariah_approval_requirement="CAST_AND_SETTING_APPROVAL_REQUIRED",
    effort_band="MEDIUM")


# Assets a group needs that are NOT tied to any of the 46 obligations.
_AG_EXTRA = {
    "AG-01": (1, "UA-01-00 — the controlled redraw of T04-DGM-01 required by D-05. The "
                 "diagram itself is a distinct asset from the six step visuals drawn on top "
                 "of it, and it belongs to no single obligation."),
}


def _asset_groups():
    out = []
    for gid, (label, concept, tier, screens, grounding, has_source, effort) in _AG_META.items():
        rows = _ag_rows(gid)
        assets = _ag_assets(gid)
        extra_n, extra_why = _AG_EXTRA.get(gid, (0, None))
        composite = "MIXED" if len({r["composite_or_individual"] for r in rows}) > 1 else \
            (rows[0]["composite_or_individual"] if rows else "NOT_APPLICABLE")
        dnr = [r["obligation_id"] for r in rows if r["reuse_policy"] == "DO_NOT_REUSE"]
        out.append(dict(
            asset_group_id=gid, label=label,
            obligations_covered=[r["obligation_id"] for r in rows],
            obligations_covered_empty_by_design=False, empty_reason=None,
            visual_concept=concept,
            composite_or_individual=composite,
            proposed_unique_assets=len(assets) + extra_n,
            assets_from_obligations=len(assets),
            additional_assets=extra_n,
            additional_assets_reason=extra_why,
            unique_asset_candidate_ids=assets,
            reuse_conditions=("DO_NOT_REUSE applies to " + ", ".join(dnr)) if dnr else
                             "No cross-group reuse assessed yet.",
            do_not_reuse_obligations=dnr,
            source_grounding=grounding,
            source_reference_available=has_source,
            complexity_tier=tier,
            affected_screens=screens,
            mmd_production_status="NOT_STARTED",
            bariah_approval_requirement="SUBJECT_AND_STYLE_APPROVAL_REQUIRED",
            effort_band=effort))
    ag8 = dict(AG08)
    ag8.update(do_not_reuse_obligations=[], source_reference_available=False,
               assets_from_obligations=0,
               additional_assets=AG08["proposed_unique_assets"],
               additional_assets_reason="Scenario backdrop and character video for the Slide "
                                        "2 dialogue; neither is one of the 46 obligations.")
    out.append(ag8)
    return out


ASSET_GROUPS = _asset_groups()
ASSET_GROUP_FIELDS = [
    "asset_group_id", "obligations_covered", "visual_concept", "composite_or_individual",
    "proposed_unique_assets", "reuse_conditions", "source_grounding", "complexity_tier",
    "affected_screens", "mmd_production_status", "bariah_approval_requirement",
]

UNIQUE_ASSET_COUNT = "PROPOSED_NOT_APPROVED"


def _asset_totals():
    rows = OBLIGATION_CLOSURE
    return dict(
        visual_obligation_count=len(rows),
        asset_group_count=len(ASSET_GROUPS),
        composite_asset_candidate_count=len([r for r in rows
                                             if r["composite_or_individual"] == "COMPOSITE"]),
        individual_asset_candidate_count=len([r for r in rows
                                              if r["composite_or_individual"] == "INDIVIDUAL"]),
        unique_asset_count_confirmed=0,
        unique_asset_count_undetermined=sum(g["proposed_unique_assets"] for g in ASSET_GROUPS),
        proposed_unique_assets=sum(g["proposed_unique_assets"] for g in ASSET_GROUPS),
        do_not_reuse_group_count=len([g for g in ASSET_GROUPS
                                      if g["do_not_reuse_obligations"]]),
        do_not_reuse_obligation_count=len([r for r in rows
                                           if r["reuse_policy"] == "DO_NOT_REUSE"]),
        unique_asset_count_status=UNIQUE_ASSET_COUNT,
        obligations_are_not_assets=(
            f"{len(rows)} obligations resolve to {len(ASSET_GROUPS)} asset groups and a "
            f"PROPOSED {sum(g['proposed_unique_assets'] for g in ASSET_GROUPS)} unique "
            f"assets. The numbers differ in both directions: "
            f"{len([r for r in rows if r['closure_outcome'] == _C])} obligations are "
            f"discharged by a composite another obligation already pays for and "
            f"{len([r for r in rows if r['closure_outcome'] == _N])} grouping headings need "
            "no asset at all, while the D-05 diagram redraw and the Slide 2 scenario need "
            f"{sum(g.get('additional_assets', 0) for g in ASSET_GROUPS)} assets that belong "
            "to no obligation. 46 was never a production figure."))


ASSET_TOTALS = _asset_totals()

# ==========================================================================================
# PART 4 — PROPOSED LEARNER-SCREEN SEQUENCE
# ==========================================================================================
def _rows_range(a, b):
    return [f"T04-ROW-{i:03d}" for i in range(a, b + 1)]


def _vo_for_screen(sid):
    return [r["obligation_id"] for r in OBLIGATION_CLOSURE
            if r["proposed_learner_screen_id"] == sid]


def _ag_for_screen(sid):
    return sorted({r["proposed_asset_group_id"] for r in OBLIGATION_CLOSURE
                   if r["proposed_learner_screen_id"] == sid})


_SCREENS = [
    ("T04-S01", "Tajuk dan Mula", [], "TITLE",
     "Open the unit and give the learner the topic and Bahagian before anything else.",
     "The learner knows which Topik and Bahagian they are in.",
     "Title, unit name and a MULA button, all visible.", ["BASE only"], "screen viewed",
     "One short screen-level VO naming the course, Topik and Bahagian.",
     "NON_SPOKEN_CONTEXT: unit provenance. SPOKEN_CONTENT_VO: the welcome line.",
     "The MULA button must be keyboard reachable and labelled.", "none"),
    ("T04-S02", "Pengenalan — perbualan di tapak",
     ["T04-ROW-001", "T04-ROW-002", "T04-ROW-003", "T04-ROW-004", "T04-ROW-005",
      "T04-ROW-079", "T04-ROW-080"], "DIALOGUE_SCENARIO",
     "Open from the site at the moment construction ends and maintenance begins, so the six "
     "activities arrive as work rather than as a diagram.",
     "The learner can say what the maintenance phase covers and that it splits into soft and "
     "hard landscape.",
     "Site visual with both characters; dialogue plays as character video, full text in Notes.",
     ["BASE — dialogue plays"], "dialogue complete",
     "Dialogue is the audio. No separate narrator VO.",
     "NON_SPOKEN_CONTEXT: unit provenance. SPOKEN_CONTENT_VO: the five turns. "
     "PRODUCTION_INSTRUCTION_NOT_SPOKEN: character direction and the compliance-exclusion rule.",
     "Full dialogue must exist as attributed text, not audio only.", "none"),
    ("T04-S03", "Aliran proses penjagaan dan penyelenggaraan",
     ["T04-ROW-001", "T04-ROW-002", "T04-ROW-003"], "PROCESS_FLOW_STEPPED",
     "Present the six supervisory activities in source order and give each one a visual, as "
     "Bariah ruled.",
     "The learner can name the six activities and place them in order.",
     "The source-bound six-step diagram with all six labels visible from the start.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ST-05", "ST-06", "ALL_VIEWED"],
     "all six steps viewed; the six labels are already in the base state",
     "One screen-level VO plus a short line per step.",
     "PRODUCTION_INSTRUCTION_NOT_SPOKEN: D-05 redraw rule — six nodes, linear, no hierarchy.",
     "The six labels must be selectable text, not only pixels inside an image.",
     "none"),
    ("T04-S04", "Landskap Lembut — pengenalan", _rows_range(4, 5), "CONTENT_STATIC",
     "Establish the soft-landscape category before its three operations are taught.",
     "The learner can say what soft landscape includes.",
     "Category visual and the source definition, both visible.", ["BASE only"],
     "screen viewed", "One screen-level VO.",
     "NON_SPOKEN_CONTEXT plus one SPOKEN_CONTENT_VO block.",
     "Standard reading order.", "none"),
    ("T04-S05", "Siram — penerangan utama", _rows_range(6, 7), "CONTENT_STATIC",
     "Give watering a concrete image and its purpose before methods are broken down.",
     "The learner can state why watering is done.",
     "Operation visual and the source definition.", ["BASE only"], "screen viewed",
     "One screen-level VO.", "NON_SPOKEN_CONTEXT plus SPOKEN_CONTENT_VO.",
     "Standard reading order.", "none"),
    ("T04-S06", "Siram — kaedah pelaksanaan", _rows_range(8, 15), "CLICK_TO_REVEAL",
     "Contrast manual watering with automatic irrigation, and inside automatic, sprinkler "
     "with drip.",
     "The learner can choose an irrigation method for a given situation.",
     "Both method labels visible; the comparison composite is the persistent visual.",
     ["BASE", "ST-01", "ST-02", "ALL_VIEWED"], "both methods revealed",
     "Screen-level instruction plus one line per method.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "Reveals keyboard reachable and state announced; stacked fallback loses nothing.",
     "none"),
    ("T04-S07", "Siram — aspek pengurusan untuk kontraktor", _rows_range(16, 25),
     "CLICK_TO_REVEAL",
     "Cover the four management topics the source groups under contractor responsibility.",
     "The learner can state the contractor's watering-management duties.",
     "Four topic labels visible before any interaction.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ALL_VIEWED"], "all four revealed",
     "Screen-level instruction plus one line per topic.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "As T04-S06.", "none"),
    ("T04-S08", "Baja — penerangan utama", _rows_range(26, 27), "CONTENT_STATIC",
     "Give fertilising a concrete image and its purpose.",
     "The learner can state why fertiliser is applied.",
     "Operation visual and the source definition.", ["BASE only"], "screen viewed",
     "One screen-level VO.", "NON_SPOKEN_CONTEXT plus SPOKEN_CONTENT_VO.",
     "Standard reading order.", "none"),
    ("T04-S09", "Baja — kaedah pelaksanaan", _rows_range(28, 34), "CLICK_TO_REVEAL",
     "Distinguish the three application methods the source names.",
     "The learner can match an application method to a planting situation.",
     "Three method labels visible; the comparison composite is the persistent visual.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ALL_VIEWED"], "all three revealed",
     "Screen-level instruction plus one line per method.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "As T04-S06.", "none"),
    ("T04-S10", "Baja — aspek pengurusan untuk kontraktor", _rows_range(35, 45),
     "CLICK_TO_REVEAL",
     "Cover the five management topics the source groups under contractor responsibility.",
     "The learner can state the contractor's fertilising-management duties.",
     "Five topic labels visible before any interaction.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ST-05", "ALL_VIEWED"], "all five revealed",
     "Screen-level instruction plus one line per topic.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "As T04-S06.",
     "T04-ROW-039 names the Pegawai Penguasa (S.O.) approval requirement — quoted, not "
     "asserted."),
    ("T04-S11", "Racun — penerangan utama", _rows_range(46, 47), "CONTENT_STATIC",
     "Establish that pest control addresses three different problems, not one.",
     "The learner can name the three threats pest control addresses.",
     "Three-threat visual and the source definition.", ["BASE only"], "screen viewed",
     "One screen-level VO.", "NON_SPOKEN_CONTEXT plus SPOKEN_CONTENT_VO.",
     "Standard reading order.", "none"),
    ("T04-S12", "Racun — pendekatan IPM", _rows_range(48, 56), "CLICK_TO_REVEAL",
     "Teach the IPM priority order — that chemical control is not the first response.",
     "The learner can place chemical control last in the IPM priority order.",
     "The priority-order diagram persistent, with all four control names visible.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ALL_VIEWED"], "all four revealed",
     "Screen-level instruction plus one line per control.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "The order must be conveyed by text and structure, not by colour alone.", "none"),
    ("T04-S13", "Racun — jenis racun", _rows_range(57, 63), "CLICK_TO_REVEAL",
     "Pair each pesticide type with the problem it controls.",
     "The learner can match pesticide type to target.",
     "The three-type comparison visible as the persistent visual.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ALL_VIEWED"], "all three revealed",
     "Screen-level instruction plus one line per type.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "As T04-S06.", "none"),
    ("T04-S14", "Racun — perundangan dan pelesenan", _rows_range(64, 67), "CONTENT_STATIC",
     "Carry the statutory control and the licensed-operator requirement, both base-visible.",
     "The learner can state who may legally carry out pesticide spraying.",
     "Statute and licensed-operator requirement verbatim, both visible. NOTHING on this "
     "screen is behind an interaction.",
     ["BASE only"], "screen viewed",
     "One screen-level VO; the obligations are spoken as written.",
     "PRODUCTION_INSTRUCTION_NOT_SPOKEN: this screen carries legal content and must not be "
     "abbreviated in MMD.",
     "Legal content reachable without interaction, and not dependent on colour or hover.",
     "T04-CLM-01 Akta Racun Makhluk Perosak 1974 and T04-CLM-02 licensed operator — both "
     "EXTERNAL_VERIFICATION_REQUIRED, quoted verbatim, never paraphrased."),
    ("T04-S15", "Racun — keselamatan dan kesihatan (HSE)", _rows_range(68, 74),
     "CONTENT_WITH_CONFIRMED_REVEAL",
     "Carry full PPE on the base screen, with storage and SDS detail reveal-eligible under "
     "the D-04 ruling.",
     "The learner can state the PPE required and where pesticide must be stored.",
     "PPE Lengkap and its item list VISIBLE — Bariah placed PPE on the base screen.",
     ["BASE (PPE visible)", "REVEAL_STORAGE", "REVEAL_SDS", "ALL_VIEWED"],
     "screen viewed; the base state already discharges the PPE disclosure",
     "Screen-level VO; PPE spoken on the base state.",
     "PRODUCTION_INSTRUCTION_NOT_SPOKEN: D-04 split — PPE may not be moved behind a reveal.",
     "PPE reachable without interaction.",
     "T04-CLM-03 PPE and T04-CLM-04 SDS — quoted verbatim."),
    ("T04-S16", "Racun — pengurusan risiko", _rows_range(75, 78),
     "CONTENT_WITH_CONFIRMED_REVEAL",
     "Carry the risk-management heading on the base screen with spray conditions, "
     "notification and reporting reveal-eligible under the D-04 ruling.",
     "The learner can state the conditions under which spraying may proceed.",
     "The Pengurusan Risiko heading visible so the learner knows the topic exists.",
     ["BASE", "REVEAL_SPRAY_CONDITIONS", "REVEAL_NOTIFICATION", "REVEAL_REPORTING",
      "ALL_VIEWED"], "all three revealed",
     "Screen-level instruction plus one line per obligation.",
     "PRODUCTION_INSTRUCTION_NOT_SPOKEN: D-04 made these three reveal-eligible; a "
     "non-interacting learner will not see them, which is recorded as a residual risk.",
     "Reveals keyboard reachable and state announced.",
     "T04-CLM-05 spray drift — quoted verbatim."),
    ("T04-S17", "Landskap Kejur — pengenalan", _rows_range(79, 80), "CONTENT_STATIC",
     "Establish the hard-landscape category and its contrast with soft landscape.",
     "The learner can distinguish soft from hard landscape.",
     "Category visual and the source definition.", ["BASE only"], "screen viewed",
     "One screen-level VO.", "NON_SPOKEN_CONTEXT plus SPOKEN_CONTENT_VO.",
     "Standard reading order.", "none"),
    ("T04-S18", "Landskap Kejur — empat kumpulan fungsi", _rows_range(81, 100),
     "CLICK_TO_REVEAL",
     "Present the four functions hard landscape performs, each with its two source sub-items.",
     "The learner can name the four functions and give an example of each.",
     "Four group labels visible before any interaction.",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ALL_VIEWED"], "all four revealed",
     "Screen-level instruction plus one line per group.",
     "SPOKEN_INTERACTION_INSTRUCTION plus per-reveal SPOKEN_CONTENT_VO.",
     "As T04-S06.", "none"),
    ("T04-S19", "Rumusan", [], "RUMUSAN",
     "Recap the unit in four points, in the Topik 3 Bahagian 2 style Bariah instructed.",
     "The learner can restate the unit's structure and the contractor's responsibilities.",
     "Heading and four recap points, all visible.", ["BASE only"], "screen viewed",
     "One screen-level VO reading the recap.",
     "NON_SPOKEN_CONTEXT plus SPOKEN_CONTENT_VO.",
     "Standard reading order.",
     "None — the Rumusan deliberately says 'perundangan' rather than naming an Act."),
    ("T04-S20", "Kuiz", [], "QUIZ",
     "Assess the unit with four MCQ and one Multiple Response, at a 60 percent pass mark.",
     "The learner demonstrates recall and application across the unit's coverage.",
     "Five items presented in sequence.",
     ["Q1", "Q2", "Q3", "Q4", "Q5", "RESULT"], "all five submitted",
     "Screen-level instruction only; no VO reads the questions aloud.",
     "PRODUCTION_INSTRUCTION_NOT_SPOKEN: pass mark 60 percent, scope all PLs in the Kursus.",
     "Options keyboard reachable; feedback not conveyed by colour alone.",
     "Q5 draws on rows carrying EXTERNAL_VERIFICATION_REQUIRED claims; no option names the "
     "Act."),
    ("T04-S21", "Tamat Bahagian", [], "CLOSING",
     "Close the unit and confirm completion.",
     "The learner knows the Bahagian is complete.",
     "Closing statement, visible.", ["BASE only"], "screen viewed",
     "One short closing VO.", "NON_SPOKEN_CONTEXT plus SPOKEN_CONTENT_VO.",
     "Standard reading order.", "none"),
]


def _screen_sequence():
    out = []
    for (sid, title, rows, treatment, purpose, outcome, base, states, completion,
         narration, notes, access, claim) in _SCREENS:
        for r in rows:
            if r not in BY_ID:
                raise RuntimeError(f"{sid}: row not in the controlled extract: {r}")
        out.append(dict(
            screen_id=sid, working_title=title, source_row_ids=list(rows),
            instructional_purpose=purpose, learner_outcome=outcome,
            treatment=treatment, base_state=base, interaction_states=list(states),
            visual_obligations_served=_vo_for_screen(sid),
            asset_groups_used=_ag_for_screen(sid),
            narration_treatment=narration, speaker_notes_treatment=notes,
            completion_condition=completion, accessibility_treatment=access,
            technical_claim_dependency=claim,
            bariah_review_status=APPROVAL_STATUS))
    return out


SCREEN_SEQUENCE = _screen_sequence()
SCREEN_FIELDS = ["screen_id", "working_title", "source_row_ids", "instructional_purpose",
                 "learner_outcome", "treatment", "base_state", "interaction_states",
                 "visual_obligations_served", "asset_groups_used", "narration_treatment",
                 "speaker_notes_treatment", "completion_condition", "accessibility_treatment",
                 "technical_claim_dependency", "bariah_review_status"]

PROPOSED_LEARNER_SCREEN_COUNT = len(SCREEN_SEQUENCE)
FINAL_LEARNER_SCREEN_COUNT = "PENDING_BARIAH_APPROVAL"

# Every controlled content population the brief requires the sequence to account for.
REQUIRED_POPULATIONS = [
    dict(population="introductory dialogue", screens=["T04-S02"]),
    dict(population="six-step process", screens=["T04-S03"]),
    dict(population="Landskap Lembut main explanation", screens=["T04-S04"]),
    dict(population="Siram", screens=["T04-S05", "T04-S06", "T04-S07"]),
    dict(population="Baja", screens=["T04-S08", "T04-S09", "T04-S10"]),
    dict(population="Racun", screens=["T04-S11", "T04-S12", "T04-S13", "T04-S14", "T04-S15",
                                      "T04-S16"]),
    dict(population="every ruled descendant subtopic",
         screens=["T04-S06", "T04-S07", "T04-S09", "T04-S10", "T04-S12", "T04-S13",
                  "T04-S14", "T04-S15", "T04-S16", "T04-S18"]),
    dict(population="Landskap Kejur main explanation", screens=["T04-S17"]),
    dict(population="four named Landskap Kejur groups", screens=["T04-S18"]),
    dict(population="legal and compliance treatment",
         screens=["T04-S14", "T04-S15", "T04-S16"]),
    dict(population="Rumusan", screens=["T04-S19"]),
    dict(population="quiz", screens=["T04-S20"]),
    dict(population="Tamat", screens=["T04-S21"]),
]

SOURCE_ROW_COVERAGE = dict(
    total_rows=len(ROWS),
    rows_on_at_least_one_screen=len({r for s in SCREEN_SEQUENCE for r in s["source_row_ids"]}),
    uncovered_rows=sorted({r["row_id"] for r in ROWS}
                          - {x for s in SCREEN_SEQUENCE for x in s["source_row_ids"]}))

SCREEN_COUNT_NOTE = (
    f"{PROPOSED_LEARNER_SCREEN_COUNT} proposed learner screens. This is NOT derived from "
    "B02's 29 — B02 is a different unit with 14 extracted photographs and a different "
    "structure. T04's count falls out of its own source: three operations with two "
    "sub-screens each, three compliance screens forced apart by the D-04 split, and one "
    "stepped process screen.")

# ==========================================================================================
# PART 5 — CONTEXTUAL FIT v2
# ==========================================================================================
ALLOWED_FIT_RESULTS = ["ALYA_ENCIK_RAHMAN_CONTEXTUALLY_SUITABLE",
                       "NEW_CHARACTER_REQUIRED_WITH_REASON"]

CONTEXTUAL_FIT = dict(
    assessment_id="T04-CFA-02",
    supersedes="T04-CFA-01",
    scope=UNIT_ID, slide="SLIDE_2",
    dialogue_purpose=["process overview", "introductory scenario", "learner orientation"],
    dialogue_purpose_excludes="Any statutory, licensing, PPE, storage, SDS, spraying, "
                              "notification or reporting obligation.",
    source_row_bindings=["T04-ROW-001", "T04-ROW-002", "T04-ROW-003", "T04-ROW-004",
                         "T04-ROW-005", "T04-ROW-079", "T04-ROW-080"],
    alya=dict(character="Alya", established_role="Kontraktor Junior",
              role_in_dialogue="ENQUIRER — carries the learner's question",
              fits=True, risk="LOW",
              reasoning="The same shape she already plays in the approved B02 S02, where she "
                        "asks what remains after planting work. T04 opens on exactly that "
                        "hinge. She asks; she does not assert."),
    encik_rahman=dict(character="Encik Rahman", established_role="Mentor / Kontraktor Senior",
                      role_in_dialogue="EXPLAINER — names the process and the two categories",
                      fits=True, risk="MEDIUM_IF_UNSCOPED",
                      conditional_on="the dialogue staying at process-overview level",
                      reasoning="Naming six supervisory activities and distinguishing soft "
                                "from hard landscape is ordinary senior-contractor knowledge "
                                "and is the register he uses in the approved B02 S02. None of "
                                "it requires a credential."),
    roles_source="reviews/source-completion/generator/v0_4/b02_proof_content_v0_4.py, S02 cast",
    specialist_expertise_required_for_slide_2=False,
    specialist_expertise_required_in_unit=True,
    specialist_expertise_detail="The unit contains regulated content — pesticide use under "
                                "statute, a licensed-operator requirement, SDS handling and "
                                "spray-drift control. That material needs a licensed "
                                "operator's competence. Slide 2 does not touch it, and the "
                                "screens that do carry it as source quotation on "
                                "T04-S14/S15/S16 rather than as anyone's speech.",
    unsupported_expertise_risk=dict(
        level="MEDIUM",
        description="If Slide 2 were extended into the Racun material, Encik Rahman would be "
                    "voicing statutory and licensing obligations no source attributes to him. "
                    "The source itself says the person who sprays must be a licensed "
                    "operator — a competence the character bank does not give him.",
        mitigation="Slide 2 is bound to seven process-and-category rows and nothing else. A "
                   "gate scans every dialogue line for the source's own compliance vocabulary "
                   "and fails on a hit.",
        residual_after_mitigation="LOW"),
    recommendation="ALYA_ENCIK_RAHMAN_CONTEXTUALLY_SUITABLE",
    recommendation_condition="For SLIDE 2 ONLY, with the dialogue scoped to the process "
                             "overview and the two landscape categories. This is not a "
                             "finding that the pair suits the whole unit.",
    new_character_would_be_required_if="Bariah wants the dialogue to carry pesticide "
                                       "licensing, PPE or spray-safety content — in which "
                                       "case the honest move is a licensed-operator character.",
    authority="CAIR_ASSESSMENT_NOT_A_BARIAH_RULING",
    status=APPROVAL_STATUS,
    instance_mapping_status="PROPOSED_PENDING_BARIAH_APPROVAL")

# ==========================================================================================
# PART 6 — SLIDE 2 DIALOGUE
# ==========================================================================================
COMPLIANCE_EXCLUSIONS = ["Akta obligation", "licensed-operator obligation", "PPE mandate",
                         "SDS instruction", "chemical-storage instruction",
                         "statutory spraying condition"]

DIALOGUE = dict(
    screen_id="T04-S02", contract_id="T04-CT-07",
    content_status=CONTENT_STATUS,
    instructional_authority=INSTRUCTIONAL_AUTHORITY,
    approval_status=APPROVAL_STATUS,
    cast=[("Alya", "Kontraktor Junior"), ("Encik Rahman", "Mentor / Kontraktor Senior")],
    cast_status="PROPOSED_SUBJECT_TO_BARIAH_APPROVAL",
    fit_assessment_id=CONTEXTUAL_FIT["assessment_id"],
    fit_result=CONTEXTUAL_FIT["recommendation"],
    level="PROCESS_OVERVIEW_ONLY",
    compliance_exclusions=COMPLIANCE_EXCLUSIONS,
    compliance_exclusion_rule="No dialogue line may state a legal, licensing, PPE, storage, "
                              "SDS, spraying, notification or reporting obligation. Those "
                              "live on T04-S14, T04-S15 and T04-S16 as source quotation.",
    lines=[
        dict(dialogue_line_id="T04-DLG-01", speaker="Alya",
             text="Encik Rahman, kerja pembinaan dan tanaman di tapak ini dah siap. Selepas "
                  "ini apa yang perlu diuruskan?",
             source_row_ids=["T04-ROW-002"],
             instructional_function="Opens the hinge the module itself opens on — what "
                                    "follows construction.",
             factual_risk_status="LOW — restates the framing of T04-ROW-002",
             vo_status="SPOKEN_CONTENT_VO"),
        dict(dialogue_line_id="T04-DLG-02", speaker="Encik Rahman",
             text="Sekarang masuk fasa penjagaan dan penyelenggaraan. Ada enam aktiviti "
                  "penyeliaan yang perlu berjalan, daripada koordinasi kerja sampailah kepada "
                  "perancangan sumber manusia.",
             source_row_ids=["T04-ROW-001", "T04-ROW-002", "T04-ROW-003"],
             instructional_function="Names the phase and its six-activity flow, previewing "
                                    "T04-S03.",
             factual_risk_status="LOW — the six activities and their order are measured from "
                                 "T04-DGM-01",
             vo_status="SPOKEN_CONTENT_VO"),
        dict(dialogue_line_id="T04-DLG-03", speaker="Alya",
             text="Semua elemen di tapak diselenggara sama caranya?",
             source_row_ids=["T04-ROW-005", "T04-ROW-080"],
             instructional_function="Sets up the soft/hard distinction as a learner question.",
             factual_risk_status="LOW — a question, asserts nothing",
             vo_status="SPOKEN_CONTENT_VO"),
        dict(dialogue_line_id="T04-DLG-04", speaker="Encik Rahman",
             text="Tidak. Landskap lembut itu elemen hidup — pokok, rumput, tanaman. Landskap "
                  "kejur pula elemen binaan yang kekal. Keperluan penyelenggaraannya berbeza.",
             source_row_ids=["T04-ROW-004", "T04-ROW-005", "T04-ROW-079", "T04-ROW-080"],
             instructional_function="Draws the organising contrast of the whole unit.",
             factual_risk_status="LOW — both definitions are compressions of their source rows",
             vo_status="SPOKEN_CONTENT_VO"),
        dict(dialogue_line_id="T04-DLG-05", speaker="Alya",
             text="Jadi saya kena faham keperluan kedua-duanya sebelum susun jadual "
                  "penyelenggaraan.",
             source_row_ids=["T04-ROW-002"],
             instructional_function="Closes on the learner's own next step, mirroring the "
                                    "approved B02 S02 closing move.",
             factual_risk_status="LOW",
             vo_status="SPOKEN_CONTENT_VO"),
    ],
    length_note="Five turns, one learner screen. The approved B02 S02 dialogue is also five "
                "turns.",
    drafting_basis="Bariah ruled that Slide 2 takes a dialogue scenario (BR-C3). The lines "
                   "are CAIR_ASSISTED_DRAFT on the same footing as the Rumusan — proposed, "
                   "not approved, and hers to rewrite.")

# ==========================================================================================
# PART 7 — RUMUSAN v3
# ==========================================================================================
RUMUSAN_STYLE_RULES = B06.RUMUSAN_STYLE_RULES
RUMUSAN_STYLE_SOURCE = B06.RUMUSAN_STYLE_SOURCE

RUMUSAN = dict(
    version="v3",
    supersedes="v2",
    change_from_v2="The four statements are carried forward UNCHANGED. v3 adds the explicit "
                   "ACCEPT / EDIT / REMOVE / COMMENT field per point that this stage "
                   "requires. Rewording text that already satisfies the style rules, purely "
                   "to justify a version bump, would churn content Bariah has not yet seen.",
    content_status=CONTENT_STATUS,
    instructional_authority=INSTRUCTIONAL_AUTHORITY,
    approval_status=APPROVAL_STATUS,
    heading=B06.RUMUSAN_V2["heading"],
    provenance=B06.RUMUSAN_V2["provenance"],
    points=[dict(point_id=s["statement_id"], draft_text=s["draft_text"],
                 source_row_ids=list(s["source_row_ids"]), source_heading=s["source_heading"],
                 style_rule_applied=list(s["style_rule_applied"]),
                 style_deviation=s["style_deviation"],
                 factual_risk_status=s["factual_risk_status"],
                 bariah_review=dict(accept=None, edit=None, remove=None, comment=None))
            for s in B06.RUMUSAN_V2["statements"]],
    medium_risk_point_id="T04-RUM2-04",
    consolidation_note=B06.RUMUSAN_CONSOLIDATION_NOTE,
    v1_to_v2_mapping=B06.RUMUSAN_V1_TO_V2)

# ==========================================================================================
# PART 8 — FIVE QUIZ ITEM DRAFTS
# ==========================================================================================
QUIZ = dict(
    content_status=CONTENT_STATUS,
    final_instructional_authority=INSTRUCTIONAL_AUTHORITY,
    approval_status=APPROVAL_STATUS,
    answer_key_status="PROPOSED_ANSWER_KEY",
    answer_key_approval="PENDING_BARIAH_APPROVAL",
    composition="4 MCQ + 1 MULTIPLE_RESPONSE",
    pass_threshold="60_PERCENT",
    scope="ALL_PLS_IN_KURSUS",
    coverage_accounting=dict(
        blueprint_points=["T04-QB-01", "T04-QB-02", "T04-QB-03", "T04-QB-04", "T04-QB-05",
                          "T04-QB-06"],
        slots=5, discarded=0,
        merged=dict(into="Q5", from_points=["T04-QB-03", "T04-QB-04"],
                    disclosure="The two compliance blueprint points are the same cluster split "
                               "by heading, not by concept, and the source presents their "
                               "controls as co-applying. As one Multiple Response item they "
                               "test what the source actually says.",
                    cost="The statute's NAME has no stem of its own. No option names the Act. "
                         "If Bariah wants it tested by name, it must displace another slot.")),
    items=[
        dict(question_id="Q1", question_type="MCQ",
             draft_stem="Apakah tiga operasi utama penyelenggaraan landskap lembut yang "
                        "dinyatakan dalam modul?",
             draft_options=[
                 ("A", "Siram, baja dan racun"),
                 ("B", "Siram, potong dan tanam"),
                 ("C", "Baja, racun dan turap"),
                 ("D", "Racun, siram dan pembinaan")],
             proposed_correct_answer=["A"],
             distractor_rationale="B, C and D each keep one or two of the real operations and "
                                  "substitute an activity the module places outside soft-"
                                  "landscape maintenance — turap and pembinaan belong to "
                                  "landskap kejur. All four options are three-item lists of "
                                  "similar length, so no option is correct on shape alone.",
             source_row_ids=["T04-ROW-006", "T04-ROW-026", "T04-ROW-046"],
             correct_answer_evidence="Three Heading-3 operations sit under Landskap Lembut: "
                                     "Siram (T04-ROW-006), Baja (T04-ROW-026), Racun "
                                     "(T04-ROW-046).",
             cognitive_demand="RECALL",
             misconception_assessed="that soft-landscape maintenance is only watering",
             overlap_check="Q2 assumes Siram is known; no answer overlap.",
             visual_dependency="T04-VO-008, T04-VO-017, T04-VO-028",
             feedback_proposal=dict(correct="Pilihan jawapan tepat.",
                                    incorrect="Pilihan jawapan tidak tepat."),
             factual_risk_status="LOW"),
        dict(question_id="Q2", question_type="MCQ",
             draft_stem="Sebuah projek memerlukan pengairan automatik bagi kawasan rumput "
                        "yang luas. Mengikut modul, sistem manakah yang paling sesuai?",
             draft_options=[
                 ("A", "Sistem Semburan (Sprinkler System)"),
                 ("B", "Sistem Titis (Drip Irrigation System)"),
                 ("C", "Penyiraman manual menggunakan hos getah"),
                 ("D", "Semburan folia menggunakan baja cecair")],
             proposed_correct_answer=["A"],
             distractor_rationale="B is what the module recommends for individual trees and "
                                  "shrubs, not broad turf. C is manual, so it fails the "
                                  "'automatic' condition in the stem. D is a fertilising "
                                  "method, not irrigation. Every distractor is a real thing "
                                  "the module names, placed in the wrong situation.",
             source_row_ids=["T04-ROW-012", "T04-ROW-013", "T04-ROW-014", "T04-ROW-015"],
             correct_answer_evidence="T04-ROW-013 states the sprinkler system is 'sesuai untuk "
                                     "kawasan rumput yang luas'; T04-ROW-015 states drip is "
                                     "for individual trees and shrubs.",
             cognitive_demand="APPLICATION",
             misconception_assessed="that sprinkler and drip irrigation are interchangeable",
             overlap_check="Draws on Siram only; no overlap with Q3, Q4 or Q5.",
             visual_dependency="T04-VO-011",
             feedback_proposal=dict(correct="Pilihan jawapan tepat.",
                                    incorrect="Pilihan jawapan tidak tepat."),
             factual_risk_status="LOW"),
        dict(question_id="Q3", question_type="MCQ",
             draft_stem="Mengikut susunan keutamaan IPM dalam modul, kaedah kawalan manakah "
                        "yang disenaraikan paling akhir?",
             draft_options=[
                 ("A", "Kawalan Kultur"),
                 ("B", "Kawalan Fizikal"),
                 ("C", "Kawalan Biologi"),
                 ("D", "Kawalan Kimia")],
             proposed_correct_answer=["D"],
             distractor_rationale="A, B and C are the three controls the module lists ahead of "
                                  "chemical control. A learner who believes chemicals come "
                                  "first will not pick D. The options are single terms of "
                                  "equal length.",
             source_row_ids=["T04-ROW-048", "T04-ROW-049", "T04-ROW-051", "T04-ROW-053",
                             "T04-ROW-055"],
             correct_answer_evidence="T04-ROW-048 introduces the priority list and the module "
                                     "then gives Kawalan Kultur, Kawalan Fizikal, Kawalan "
                                     "Biologi and Kawalan Kimia in that order.",
             cognitive_demand="UNDERSTANDING",
             misconception_assessed="that chemical control is the first response to a pest "
                                    "problem",
             overlap_check="Q5 tests the controls that apply WHEN chemicals are used; Q3 "
                           "tests what comes before. Disclosed, not accidental.",
             visual_dependency="T04-VO-029",
             feedback_proposal=dict(correct="Pilihan jawapan tepat.",
                                    incorrect="Pilihan jawapan tidak tepat."),
             factual_risk_status="LOW — the stem asks about the module's own listing order, "
                                 "which is exactly what the source supports. Bariah may "
                                 "prefer a 'which comes first' framing; that is an edit, not "
                                 "a correction."),
        dict(question_id="Q4", question_type="MCQ",
             draft_stem="Modul menyenaraikan empat kumpulan fungsi landskap kejur. Kumpulan "
                        "manakah yang merangkumi kerja menstabilkan tanah dan menguruskan "
                        "aliran air?",
             draft_options=[
                 ("A", "Pengurusan Ruang dan Sirkulasi"),
                 ("B", "Fungsi Struktur dan Kejuruteraan"),
                 ("C", "Kebolehgunaan dan Kemudahan"),
                 ("D", "Estetika dan Reka Bentuk")],
             proposed_correct_answer=["B"],
             distractor_rationale="A, C and D are the module's other three function groups, so "
                                  "every distractor is a real category rather than an invented "
                                  "one. A learner who thinks hard landscape is decorative will "
                                  "be drawn to D.",
             source_row_ids=["T04-ROW-081", "T04-ROW-086", "T04-ROW-087", "T04-ROW-089",
                             "T04-ROW-091", "T04-ROW-096"],
             correct_answer_evidence="T04-ROW-086 Fungsi Struktur dan Kejuruteraan has exactly "
                                     "two sub-headings: Menstabilkan Tanah (T04-ROW-087) and "
                                     "Pengurusan Air (T04-ROW-089).",
             cognitive_demand="RECALL",
             misconception_assessed="that hard landscape is decorative only",
             overlap_check="Only item drawing on Landskap Kejur.",
             visual_dependency="T04-VO-044",
             feedback_proposal=dict(correct="Pilihan jawapan tepat.",
                                    incorrect="Pilihan jawapan tidak tepat."),
             factual_risk_status="LOW"),
        dict(question_id="Q5", question_type="MULTIPLE_RESPONSE",
             draft_stem="Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa "
                        "aktiviti semburan racun, mengikut modul.",
             draft_options=[
                 ("A", "Pengendali semburan mesti berlesen atau telah menerima latihan"),
                 ("B", "Pekerja mesti memakai PPE yang lengkap dan bersesuaian"),
                 ("C", "Semburan hanya dilakukan semasa cuaca tenang"),
                 ("D", "Salinan Helaian Data Keselamatan (SDS) disimpan di tapak"),
                 ("E", "Baja disimpan di tempat yang kering dan jauh dari sumber air"),
                 ("F", "Rekod pembajaan disimpan sebagai bukti kerja untuk tuntutan "
                       "bayaran")],
             proposed_correct_answer=["A", "B", "C", "D"],
             distractor_rationale="E and F are BOTH TRUE STATEMENTS IN THE MODULE — and both "
                                  "belong to Baja, not to pesticide spraying. T04-ROW-041 is "
                                  "fertiliser storage; T04-ROW-045 is fertiliser "
                                  "record-keeping. A learner must attribute a control to the "
                                  "right operation rather than recognise an obviously absurd "
                                  "statement. See Q5_DISTRACTOR_REVIEW for what this "
                                  "replaced and what it costs.",
             source_row_ids=["T04-ROW-067", "T04-ROW-069", "T04-ROW-070", "T04-ROW-074",
                             "T04-ROW-076", "T04-ROW-041", "T04-ROW-045"],
             correct_answer_evidence="A — T04-ROW-067 licensed or trained operator. "
                                     "B — T04-ROW-069 and T04-ROW-070 full PPE. "
                                     "C — T04-ROW-076 calm weather only. "
                                     "D — T04-ROW-074 SDS copy kept on site. "
                                     "E is true of fertiliser storage (T04-ROW-041), not of "
                                     "pesticide spraying. "
                                     "F is true of fertiliser records (T04-ROW-045); the "
                                     "spraying record duty is a different row.",
             cognitive_demand="RECALL",
             misconception_assessed="that PPE alone, or a licence alone, is sufficient "
                                    "compliance",
             overlap_check="Absorbs the whole compliance cluster — blueprint points T04-QB-03 "
                           "and T04-QB-04, merged and disclosed. No other item touches it.",
             visual_dependency="T04-VO-039, T04-VO-040, T04-VO-041",
             feedback_proposal=dict(correct="Pilihan jawapan tepat.",
                                    incorrect="Pilihan jawapan tidak tepat."),
             factual_risk_status="LOW — no option names the Act, so nothing depends on the "
                                 "EXTERNAL_VERIFICATION_REQUIRED citation being right"),
    ])

# Part 10 of Stage 4.2F-B0.8A: Q5 distractor review, recorded rather than applied silently.
Q5_DISTRACTOR_REVIEW = dict(
    reviewed_at_stage="4.2F-B0.8A",
    concern="Options E and F were direct negations of stated duties — empty containers may be "
            "reused, spraying needs no notification. Both are refutable without understanding "
            "the material, which lowers discrimination.",
    search_scope="The controlled T04 extract only. No external knowledge, no invented fact.",
    outcome="REVISED",
    option_mapping=[
        dict(option="A", change="UNCHANGED"),
        dict(option="B", change="UNCHANGED"),
        dict(option="C", change="UNCHANGED"),
        dict(option="D", change="UNCHANGED"),
        dict(option="E",
             old="Bekas racun kosong boleh digunakan semula untuk kegunaan lain",
             old_basis="contradicted by T04-ROW-072",
             new="Baja disimpan di tempat yang kering dan jauh dari sumber air",
             new_basis="T04-ROW-041 — TRUE of fertiliser storage, not a pesticide-spraying "
                       "control"),
        dict(option="F",
             old="Semburan boleh dijalankan tanpa memaklumkan penduduk sekitar",
             old_basis="contradicted by T04-ROW-077",
             new="Rekod pembajaan disimpan sebagai bukti kerja untuk tuntutan bayaran",
             new_basis="T04-ROW-045 — TRUE of fertiliser records, not a pesticide-spraying "
                       "control"),
    ],
    correct_answer_count_before=4, correct_answer_count_after=4,
    difficulty_before="LOW_DISTRACTOR_DIFFICULTY",
    difficulty_after="MODERATE_DISTRACTOR_DIFFICULTY",
    trade_off="The old distractors could be eliminated by anyone who noticed they were absurd. "
              "The new ones require the learner to attribute a control to the correct "
              "operation. That is better discrimination, but option F is a fine distinction — "
              "'rekod pembajaan' against the spraying record duty in T04-ROW-078 — and a "
              "reviewer could reasonably call it a trick. Flagged for Bariah rather than "
              "decided.",
    bariah_note_ms="Pilihan E dan F ialah kenyataan yang BETUL dalam modul, tetapi ia "
                   "berkaitan baja, bukan kawalan semasa semburan racun. Tujuannya supaya "
                   "pelajar perlu membezakan kawalan mengikut operasi. Jika Bariah rasa ini "
                   "terlalu halus, kedua-dua pilihan boleh ditukar.",
    status=CONTENT_STATUS, approval_status=APPROVAL_STATUS)

QUIZ_ITEM_FIELDS = ["question_id", "question_type", "draft_stem", "draft_options",
                    "proposed_correct_answer", "distractor_rationale", "source_row_ids",
                    "correct_answer_evidence", "cognitive_demand", "misconception_assessed",
                    "overlap_check", "visual_dependency", "feedback_proposal",
                    "factual_risk_status"]

# ==========================================================================================
# PART 10 — PRELIMINARY MMD DEMAND FORECAST
# ==========================================================================================
EFFORT_BANDS = ["LOW", "MEDIUM", "HIGH", "VERY_HIGH"]

MMD_FORECAST = dict(
    status="PRELIMINARY_DEMAND_FORECAST",
    commitment="NOT_A_PRODUCTION_COMMITMENT",
    gate="PENDING_BARIAH_SCREEN_APPROVAL",
    production_status="NOT_STARTED",
    hours_note="No production hours are estimated. No measured MMD baseline exists for this "
               "toolchain, so an hour figure would be invented. Effort bands only.",
    groups=[dict(asset_group_id=g["asset_group_id"], label=g["label"],
                 complexity_tier=g["complexity_tier"],
                 proposed_asset_count=g["proposed_unique_assets"],
                 reuse_count=len(g["do_not_reuse_obligations"]),
                 affected_screens=g["affected_screens"],
                 source_reference_available=g["source_reference_available"],
                 illustration_or_photo_direction=(
                     "PHOTO_DIRECTION" if g["complexity_tier"] ==
                     "SOURCE_GROUNDED_PHOTO_DIRECTION" else "ILLUSTRATION"),
                 estimated_mmd_effort_band=g["effort_band"],
                 mmd_production_status="NOT_STARTED")
            for g in ASSET_GROUPS])

MMD_TOTALS = dict(
    total_proposed_asset_groups=len(ASSET_GROUPS),
    total_proposed_unique_assets=sum(g["proposed_unique_assets"] for g in ASSET_GROUPS),
    composite_assets=len([r for r in OBLIGATION_CLOSURE
                          if r["composite_or_individual"] == "COMPOSITE"]),
    individual_assets=len([r for r in OBLIGATION_CLOSURE
                           if r["composite_or_individual"] == "INDIVIDUAL"]),
    high_complexity_groups=len([g for g in ASSET_GROUPS if g["effort_band"] in ("HIGH",
                                                                               "VERY_HIGH")]),
    reusable_groups=len([g for g in ASSET_GROUPS if not g["do_not_reuse_obligations"]]),
    non_reusable_groups=len([g for g in ASSET_GROUPS if g["do_not_reuse_obligations"]]),
    unresolved_groups=len([g for g in ASSET_GROUPS if g["proposed_unique_assets"] == 0]))

# ==========================================================================================
# PART 11 — READINESS SEMANTICS
# ==========================================================================================
READINESS = dict(
    STRUCTURAL_POLICY_RESOLVED="YES",
    INSTANCE_MAPPING_PROPOSED_COMPLETE=("YES" if ORPHAN_OBLIGATIONS == 0
                                        and VISUAL_OBLIGATIONS_CLOSED == 46 else "NO"),
    CONTRACT_PROPOSED_COMPLETE=("YES" if len(SCREEN_SEQUENCE) == PROPOSED_LEARNER_SCREEN_COUNT
                                and not SOURCE_ROW_COVERAGE["uncovered_rows"] else "NO"),
    FINAL_CONTENT_APPROVED="NO",
    STORYBOARD_BUILD_AUTHORISED="NO",
    forbidden_term="INSTANCE_MAPPING_COMPLETE",
    forbidden_term_reason="'Proposed complete' means CAIR has closed every record. "
                          "'Complete' would mean Bariah has approved the mapping, and she has "
                          "not seen it.")

REMAINING_BARIAH_APPROVALS = [
    dict(approval_id="BA-1", item="Slide 2 cast and dialogue",
         what="Confirm Alya and Encik Rahman, then accept, edit or replace the five turns."),
    dict(approval_id="BA-2", item="Rumusan — four points",
         what="Accept, edit or remove each point; confirm the four-point consolidation."),
    dict(approval_id="BA-3", item="Quiz — five items",
         what="Accept, edit or rewrite the stems, options and proposed answer key."),
    dict(approval_id="BA-4", item="Proposed screen sequence and visual grouping",
         what="Confirm the 21-screen shape and the eight asset groups, or regroup."),
]

# ==========================================================================================
# PART 9 — WHATSAPP
# ==========================================================================================
WHATSAPP = dict(
    language="Malay", channel="WhatsApp", status="DRAFT_NOT_SENT",
    sending_authority="FIRDAUS", audience="BARIAH",
    text="""Terima kasih Bariah. Semua keputusan struktur Topik 4 sudah dimasukkan — visual, kuiz 4 MCQ + 1 Multiple Response dengan markah lulus 60%, kandungan Akta, rajah enam langkah, dan perbualan di Slide 2.

Kami sudah siapkan draf kandungan penuh untuk semakan Bariah:

1. Perbualan Slide 2 — 5 baris antara Alya dan Encik Rahman. Perbualan ini hanya mengenai aliran proses dan perbezaan landskap lembut dengan landskap kejur. Kami sengaja tidak letak apa-apa kandungan racun, PPE atau undang-undang dalam perbualan ini.
2. Rumusan — 4 ayat mengikut gaya Topik 3 Bahagian 2.
3. Kuiz — 5 soalan penuh dengan cadangan jawapan. Ini cadangan sahaja, bukan jawapan muktamad.
4. Susunan skrin dan kumpulan visual — kami cadangkan 21 skrin dan 8 kumpulan visual.

Untuk makluman:
• Papan cerita Topik 4 masih belum dijana.
• Belum ada aset visual dihasilkan.
• Semua kandungan di atas masih draf dan menunggu semakan Bariah.

Mohon Bariah semak dan beritahu mana yang boleh diterima, mana yang perlu diubah, dan mana yang perlu dibuang.

Terima kasih.""",
    constraints_honoured=["states structural decisions have been incorporated",
                          "states no storyboard PPTX has been generated",
                          "states the attached content remains draft",
                          "asks Bariah to review the dialogue, Rumusan, five quiz items and "
                          "the proposed visual/screen grouping",
                          "no gate counts, no mutation terminology, no repository paths, "
                          "no hashes"])

# ==========================================================================================
PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
MMD_PRODUCTION_STARTED = 0
B02_FAMILIES_PROPAGATED = 0
B02_SCREEN_COUNT_INHERITED = False

VERDICT = "T04_CONTENT_AND_INSTANCE_MAPPING_READY_FOR_BARIAH_APPROVAL"
ALLOWED_VERDICTS = [VERDICT, "T04_CONTENT_AND_INSTANCE_MAPPING_BLOCKED"]

if __name__ == "__main__":
    print(json.dumps(dict(
        obligations=dict(total=VISUAL_OBLIGATIONS_TOTAL, closed=VISUAL_OBLIGATIONS_CLOSED,
                         orphans=ORPHAN_OBLIGATIONS, by_outcome=CLOSURE_BY_OUTCOME),
        assets=ASSET_TOTALS, mmd=MMD_TOTALS,
        screens=dict(proposed=PROPOSED_LEARNER_SCREEN_COUNT,
                     final=FINAL_LEARNER_SCREEN_COUNT, coverage=SOURCE_ROW_COVERAGE),
        readiness=READINESS, fit=CONTEXTUAL_FIT["recommendation"],
        quiz=dict(items=len(QUIZ["items"]),
                  mcq=len([i for i in QUIZ["items"] if i["question_type"] == "MCQ"]),
                  mr=len([i for i in QUIZ["items"]
                          if i["question_type"] == "MULTIPLE_RESPONSE"]))),
        ensure_ascii=False, indent=1))
