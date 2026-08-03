# -*- coding: utf-8 -*-
"""Stage 4.2F-B1.1 Lane A QA — state inventory, coverage, source audit, namespaces, oracles.

    SUITE_ID = T04_STATE_COVERAGE_QA_v1
    python3 docs/pl06/t04/tools/t04_state_qa_v1.py

The appendix deck is re-opened from disk and its text re-extracted. A panel that exists only
in the builder cannot pass, and a state whose trigger or return behaviour never reached the
page cannot be counted as review-covered.

Separate from T04_STORYBOARD_QA_v1 (114), T04_AUTHORITY_DECISION_INGESTION_QA_v1 (251) and
T04_SUPPLEMENTARY_EVIDENCE_QA_v1 (133). Never add the totals.
"""
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_state_model_v1 as SM       # noqa: E402
import t04_state_coverage_v1 as CV    # noqa: E402
import t04_state_emit_v1 as SE        # noqa: E402
import t04_storyboard_model_v1 as SB  # noqa: E402
import t04_authority_data_v1 as A     # noqa: E402
import t04_content_data_v1 as C       # noqa: E402

SUITE_ID = "T04_STATE_COVERAGE_QA_v1"
PRIOR_SUITE_ID = "T04_STORYBOARD_QA_v1"

STATE_INVENTORY = "STATE_INVENTORY"
COVERAGE = "COVERAGE"
APPENDIX = "APPENDIX"
SOURCE_AUDIT = "SOURCE_AUDIT"
NAMESPACE = "NAMESPACE"
ORACLE = "ORACLE"
STATUS_GUARD = "STATUS_GUARD"
ACCOUNTING = "ACCOUNTING"

GATE_TYPES = {STATE_INVENTORY, COVERAGE, APPENDIX, SOURCE_AUDIT, NAMESPACE, ORACLE,
              STATUS_GUARD, ACCOUNTING}

NOT_CHECKED = [
    "whether the interaction design is instructionally sound — Bariah has never been shown a "
    "state-level model, which is T04-OPEN-05",
    "whether the reveal and reset behaviours match what the runtime will actually do — they "
    "are CAIR-specified, not authority-ruled",
    "how either deck renders in Microsoft PowerPoint — still no Impress filter here",
    "whether the six process-step labels match the SmartArt artwork, which carries no "
    "extractable text (T04-EXT-02)",
    "whether Bariah agrees the appendix format is readable",
]

APPENDIX_PATH = os.path.join(CV.APPENDIX_DIR, CV.APPENDIX_NAME)
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"


def _appendix_texts():
    import xml.etree.ElementTree as ET
    z = zipfile.ZipFile(APPENDIX_PATH)
    names = sorted((n for n in z.namelist()
                    if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                   key=lambda n: int(re.search(r"(\d+)", n).group(1)))
    return [[(t.text or "") for t in ET.fromstring(z.read(n)).iter(f"{{{A_NS}}}t")]
            for n in names]


def run():
    res = []

    def chk(gid, gtype, value, expected, population, source_artifact, empty_by_design=None):
        assert gtype in GATE_TYPES, gtype
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source_artifact,
                        empty_by_design=empty_by_design, vacuous=vacuous,
                        ok=ok and not vacuous))

    ST = SM.states()
    T = SM.totals()
    VER = SM.verification()
    MTX = CV.matrix(True)
    REP = CV.coverage_report(True)
    BEFORE = CV.coverage_report(False)
    PAGES = CV.appendix_pages()
    AUD = CV.source_row_audit()
    AL = CV.alias_map_report()
    OA = CV.oracle_audit()
    ROLL = SM.roll_audit()
    PLAN = CV.frozen_plan_audit()
    present = os.path.exists(APPENDIX_PATH)
    slides = _appendix_texts() if present else []
    deck = " ".join(t for s in slides for t in s)

    # ==================== 1. STATE INVENTORY ====================
    chk("SIXTY_FIVE_RUNTIME_STATES", STATE_INVENTORY, T["total_runtime_states"], 65,
        len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("TWENTY_TWO_BASE_STATES_ONE_PER_SCREEN", STATE_INVENTORY,
        (T["base_states"], T["learner_screens"]), (22, 22), len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("THIRTY_FIVE_TRIGGERED_STATES", STATE_INVENTORY, T["triggered_states"], 35,
        len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EIGHT_COMPLETION_FLAGS", STATE_INVENTORY, T["completion_flags"], 8, len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("INTERACTION_COUNT_EQUALS_TRIGGERED_STATES", STATE_INVENTORY,
        T["interactions"], T["triggered_states"], len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    # The inventory is derived from the frozen model, so it must equal the labels that model
    # already declares. Counting off the deck would prove nothing.
    chk("TOTAL_EQUALS_THE_DECLARED_STATE_LABELS", STATE_INVENTORY,
        T["total_runtime_states"],
        sum(len(s["interaction_states"]) for s in SB.screens()), len(SB.screens()),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("STATE_IDS_ARE_UNIQUE", STATE_INVENTORY,
        len({x["state_id"] for x in ST}), len(ST), len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_STATE_IS_TYPED", STATE_INVENTORY,
        [x["state_id"] for x in ST if x["state_kind"] not in SM.STATE_KINDS], [], len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_NON_BASE_STATE_HAS_A_TRIGGER", STATE_INVENTORY,
        [x["state_id"] for x in ST if x["state_kind"] != "BASE" and not x["trigger_id"]],
        [], len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_NON_BASE_STATE_NAMES_ITS_PARENT", STATE_INVENTORY,
        [x["state_id"] for x in ST if x["state_kind"] != "BASE" and not x["parent_state_id"]],
        [], len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_PARENT_RESOLVES", STATE_INVENTORY,
        sorted({x["parent_state_id"] for x in ST if x["parent_state_id"]}
               - {y["state_id"] for y in ST}), [], len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_STATE_STATES_ITS_RETURN_BEHAVIOUR", STATE_INVENTORY,
        [x["state_id"] for x in ST if not x["return_behaviour"]], [], len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_STATE_HAS_REVIEWER_FACING_MALAY", STATE_INVENTORY,
        [x["state_id"] for x in ST
         if not x.get("return_behaviour_ms") or not x.get("differs_from_base_ms")], [],
        len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_LIMITATION_HAS_REVIEWER_FACING_MALAY", STATE_INVENTORY,
        [x["state_id"] for x in ST
         if x.get("binding_limitation") and not x.get("binding_limitation_ms")], [],
        len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("ONLY_COMPLETION_FLAGS_ARE_CONTENTLESS", STATE_INVENTORY,
        sorted({x["state_kind"] for x in ST if x["content_record_count"] == 0}),
        ["COMPLETION"], len(ST), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_STATE_CARRIES_EVERY_FIELD", STATE_INVENTORY,
        sorted({f for x in ST for f in SM.STATE_FIELDS if f not in x}), [],
        len(ST) * len(SM.STATE_FIELDS), "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_SOURCE_ROW_IN_A_STATE_RESOLVES", STATE_INVENTORY,
        sorted({r for x in ST for r in x["source_row_ids"] if r not in C.BY_ID}), [],
        len({r for x in ST for r in x["source_row_ids"]}), "T04_SOURCE_EXTRACT_v1.json")
    chk("EVERY_DECISION_IN_A_STATE_RESOLVES", STATE_INVENTORY,
        sorted({d for x in ST for d in x["decision_ids"]}
               - {d["decision_id"] for d in A._decision_register()}), [],
        len({d for x in ST for d in x["decision_ids"]}),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")

    # Declared reveal targets, verified against the screens' own controlled rows.
    chk("REVEAL_TARGET_COUNTS_AGREE_WITH_THE_FROZEN_STATES", STATE_INVENTORY,
        [v["screen_id"] for v in VER if not v["counts_agree"]], [], len(VER),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("NO_REVEAL_TARGET_ROW_BELONGS_TO_ANOTHER_SCREEN", STATE_INVENTORY,
        [v["screen_id"] for v in VER if v["rows_outside_the_screen"]], [], len(VER),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")
    chk("EVERY_TRIGGER_IS_A_HEADING_OR_LIST_ROW", STATE_INVENTORY,
        [v["screen_id"] for v in VER if v["triggers_are_heading_or_list_rows"]], [],
        len(VER), "T04_SOURCE_EXTRACT_v1.json")
    chk("THE_DIAGRAM_STEP_LIMITATION_IS_DECLARED", STATE_INVENTORY,
        sorted({x["state_id"] for x in ST
                if x["binding_kind"] == "DIAGRAM_OBLIGATION_NOT_A_TEXT_ROW"}),
        [f"T04-S03-ST-{i:02d}" for i in range(1, 7)], len(ST),
        "T04_RUNTIME_STATE_INVENTORY_v1.json")

    # ==================== 2. COVERAGE ====================
    chk("FIVE_COVERAGE_CRITERIA_DECLARED", COVERAGE, len(CV.COVERAGE_CRITERIA), 5, 5,
        "T04_STATE_REVIEW_COVERAGE_v1.md")
    chk("THE_B1_DECK_ALONE_DOES_NOT_COVER_THE_STATES", COVERAGE,
        BEFORE["unrepresented_count"], 52, BEFORE["total_states"],
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("THE_DECISION_BEFORE_THE_APPENDIX_REQUIRED_ONE", COVERAGE,
        CV.decision(False), "T04_LAYOUT_READY_STATE_REVIEW_APPENDIX_REQUIRED", 1,
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("EVERY_STATE_IS_COVERED_AFTER_THE_APPENDIX", COVERAGE,
        REP["unrepresented_count"], 0, REP["total_states"],
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("THE_DECISION_AFTER_THE_APPENDIX_IS_PROVEN", COVERAGE,
        CV.decision(True), "T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN", 1,
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("EVERY_STATE_MEETS_ALL_FIVE_CRITERIA", COVERAGE,
        [r["state_id"] for r in MTX if r["criteria_met_count"] != 5], [], len(MTX),
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("NO_DUPLICATE_REPRESENTATIONS", COVERAGE, REP["duplicate_representations"], [],
        len(MTX), "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("NO_ORPHAN_REVIEW_PANELS", COVERAGE, REP["orphan_review_panels"], [], len(MTX),
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("EVERY_STATE_IS_UNIQUELY_MAPPED", COVERAGE, REP["every_state_uniquely_mapped"],
        True, len(MTX), "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("ONLY_THE_COVER_PAGE_CARRIES_NO_STATE", COVERAGE,
        REP["unmapped_pages_excluding_cover"], [], len(SB.slides()) + 1,
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("NOTHING_IS_COUNTED_AS_NOTES_ONLY", COVERAGE,
        REP["by_class"]["NOTES_ONLY"], 0, REP["total_states"],
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("NOTHING_REMAINS_METADATA_ONLY", COVERAGE,
        REP["by_class"]["METADATA_ONLY"], 0, REP["total_states"],
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("THIRTEEN_STATES_WERE_ALREADY_FULL_PAGE_VISIBLE", COVERAGE,
        REP["by_class"]["FULL_PAGE_VISIBLE"], 13, REP["total_states"],
        "T04_STATE_REVIEW_COVERAGE_v1.json")

    # ==================== 3. APPENDIX ====================
    chk("THE_APPENDIX_EXISTS", APPENDIX, present, True, 1, CV.APPENDIX_NAME)
    chk("THE_APPENDIX_IS_A_VALID_PACKAGE", APPENDIX,
        zipfile.ZipFile(APPENDIX_PATH).testzip() if present else "missing", None, 1,
        CV.APPENDIX_NAME)
    chk("APPENDIX_SLIDE_COUNT_MATCHES_THE_PLAN", APPENDIX,
        len(slides), len(PAGES) + 1, len(slides), CV.APPENDIX_NAME)
    # Checked against the literal budget, not against CV.PANELS_PER_PAGE: pages are built
    # from that constant, so comparing them to it proved only that the loop counted.
    chk("EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO_PANELS", APPENDIX,
        [p["page_no"] for p in PAGES if len(p["states"]) > 2], [],
        len(PAGES), "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("THE_PANEL_BUDGET_MATCHES_THE_DECLARED_REVIEW_POLICY", APPENDIX,
        [CV.PANELS_PER_PAGE, CV.PANEL_BUDGET_LITERAL], [2, 2], 2,
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("THE_PANEL_BUDGET_STAYS_WITHIN_THE_RENDERER_CAPACITY", APPENDIX,
        CV.PANELS_PER_PAGE <= SE.renderer_panel_capacity(), True, 1,
        "docs/pl06/t04/state_appendix_preview/")
    chk("THE_RENDERER_CAPACITY_IS_MEASURED_NOT_ASSERTED", APPENDIX,
        SE.renderer_panel_capacity(), 4, SE.PANEL_CAPACITY_PROBE_MAX,
        "docs/pl06/t04/state_appendix_preview/")
    chk("NO_APPENDIX_PAGE_MIXES_TWO_SCREENS", APPENDIX,
        [p["page_no"] for p in PAGES
         if len({s["screen_id"] for s in p["states"]}) > 1], [], len(PAGES),
        "T04_STATE_REVIEW_COVERAGE_v1.json")
    chk("EVERY_APPENDIX_STATE_ID_IS_IN_THE_DECK", APPENDIX,
        [s for p in PAGES for s in p["state_ids"] if s not in deck], [],
        sum(len(p["state_ids"]) for p in PAGES), CV.APPENDIX_NAME)
    # Named membership and population delta against the frozen roll. The three gates above
    # compare the deck with the plan that generated it; fixture A-03 deleted a state and
    # both sides agreed about its absence. These four anchor on SM.DECLARED_STATE_IDS,
    # which no generator can rewrite.
    chk("THE_FROZEN_STATE_ROLL_HOLDS_SIXTY_FIVE_IDS", APPENDIX,
        [len(SM.DECLARED_STATE_IDS), SM.DECLARED_TOTAL_RUNTIME_STATES], [65, 65], 65,
        "docs/pl06/t04/tools/t04_state_model_v1.py")
    chk("THE_LIVE_STATE_INVENTORY_AGREES_WITH_THE_FROZEN_ROLL", APPENDIX,
        {k: v for k, v in ROLL.items()
         if k in ("missing_from_live", "added_to_live", "duplicate_live_ids")},
        {"missing_from_live": [], "added_to_live": [], "duplicate_live_ids": []},
        ROLL["frozen_count"], "T04_STATE_ROLL_AUDIT_v1.json")
    chk("EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_PLAN", APPENDIX,
        [PLAN["missing_from_the_plan"], PLAN["added_to_the_plan"]], [[], []],
        PLAN["frozen_panel_count"], "T04_STATE_ROLL_AUDIT_v1.json")
    chk("EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_DECK", APPENDIX,
        [s for s in CV.DECLARED_PANEL_STATE_IDS if s not in deck], [],
        len(CV.DECLARED_PANEL_STATE_IDS), CV.APPENDIX_NAME)
    chk("THE_APPENDIX_SLIDE_COUNT_MATCHES_THE_FROZEN_ROLL", APPENDIX,
        len(slides), PLAN["pages_expected_from_the_frozen_roll"] + 1, len(slides),
        CV.APPENDIX_NAME)
    chk("THE_TWO_FROZEN_ROLLS_PARTITION_THE_STATE_ROLL", APPENDIX,
        [PLAN["rolls_are_disjoint"], PLAN["rolls_cover_the_state_roll"],
         PLAN["frozen_roll_total"]], [True, True, 65], 65,
        "T04_STATE_ROLL_AUDIT_v1.json")
    chk("EVERY_FROZEN_FULL_PAGE_STATE_IS_IN_THE_B1_DECK_NOT_THE_APPENDIX", APPENDIX,
        [s for s in CV.DECLARED_FULL_PAGE_STATE_IDS
         if s in {i for p in PAGES for i in p["state_ids"]}], [],
        len(CV.DECLARED_FULL_PAGE_STATE_IDS), CV.APPENDIX_NAME)
    chk("EVERY_APPENDIX_TRIGGER_LABEL_IS_IN_THE_DECK", APPENDIX,
        [s["state_id"] for p in PAGES for s in p["states"]
         if s["trigger_label"] and s["trigger_label"] not in deck], [],
        sum(len(p["states"]) for p in PAGES), CV.APPENDIX_NAME)
    chk("EVERY_APPENDIX_RETURN_BEHAVIOUR_IS_IN_THE_DECK", APPENDIX,
        sorted({s["return_behaviour_ms"] for p in PAGES for s in p["states"]
                if s["return_behaviour_ms"] not in deck}), [],
        sum(len(p["states"]) for p in PAGES), CV.APPENDIX_NAME)
    chk("EVERY_APPENDIX_DIFFERENCE_LINE_IS_IN_THE_DECK", APPENDIX,
        sorted({s["state_id"] for p in PAGES for s in p["states"]
                if s["differs_from_base_ms"] not in deck}), [],
        sum(len(p["states"]) for p in PAGES), CV.APPENDIX_NAME)
    chk("THE_APPENDIX_IS_IN_MALAY_NOT_ENGLISH", APPENDIX,
        [t for t in ("Panel closes on", "Entry state.", "Displays nothing of its own")
         if t in deck], [], 3, CV.APPENDIX_NAME)
    chk("NO_MEDIA_IN_THE_APPENDIX", APPENDIX,
        [n for n in (zipfile.ZipFile(APPENDIX_PATH).namelist() if present else [])
         if n.startswith("ppt/media/")], [],
        len(zipfile.ZipFile(APPENDIX_PATH).namelist()) if present else 0,
        CV.APPENDIX_NAME)
    chk("NO_REPOSITORY_PATH_IN_THE_APPENDIX", APPENDIX,
        [p for p in ("docs/pl06", "/home/user", "reviews/storyboard") if p in deck], [],
        3, CV.APPENDIX_NAME)
    # The B1 deck was not touched.
    chk("THE_B1_DECK_IS_A_SEPARATE_FILE", APPENDIX,
        CV.APPENDIX_NAME != SB.PPTX_NAME, True, 2, CV.APPENDIX_NAME)
    chk("THE_B1_DECK_STILL_HAS_ITS_OWN_SLIDE_COUNT", APPENDIX,
        len(SB.slides()) + 1, 27, 27, SB.PPTX_NAME)

    previews = sorted(f for f in os.listdir(SE.PREVIEW_DIR)
                      if f.endswith(".png")) if os.path.isdir(SE.PREVIEW_DIR) else []
    chk("A_PREVIEW_EXISTS_FOR_EVERY_APPENDIX_PAGE", APPENDIX,
        len(previews), len(PAGES), len(previews) or 1,
        "docs/pl06/t04/state_appendix_preview/")
    if previews:
        from PIL import Image
        blanks, sizes = [], set()
        for f in previews:
            im = Image.open(os.path.join(SE.PREVIEW_DIR, f)).convert("L")
            sizes.add(im.size)
            if min(im.getdata()) > 200:
                blanks.append(f)
    else:
        blanks, sizes = ["no-previews"], set()
    chk("EVERY_APPENDIX_PREVIEW_HAS_INK", APPENDIX, blanks, [], len(previews) or 1,
        "docs/pl06/t04/state_appendix_preview/")
    chk("EVERY_APPENDIX_PREVIEW_IS_THE_SAME_SIZE", APPENDIX, sorted(sizes), [(1280, 720)],
        len(previews) or 1, "docs/pl06/t04/state_appendix_preview/")

    # ==================== 4. SOURCE ROW AUDIT ====================
    chk("THREE_ROWS_AUDITED", SOURCE_AUDIT, len(AUD), 3, len(AUD),
        "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("THE_AUDITED_IDS_ARE_THE_BRIEFS_IDS", SOURCE_AUDIT,
        [r["row_id"] for r in AUD], ["T04-ROW-074", "T04-ROW-076", "T04-ROW-077"],
        len(AUD), "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("ALL_THREE_EXIST_IN_THE_CONTROLLED_EXTRACT", SOURCE_AUDIT,
        [r["row_id"] for r in AUD if not r["exists"]], [], len(AUD),
        "T04_SOURCE_EXTRACT_v1.json")
    chk("EVERY_AUDITED_ROW_QUOTES_ITS_SOURCE_TEXT", SOURCE_AUDIT,
        [r["row_id"] for r in AUD if r["exists"] and not r["controlled_source_text"]], [],
        len(AUD), "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("EVERY_AUDITED_ROW_REPORTS_ITS_PAGE_AND_POSITION", SOURCE_AUDIT,
        [r["row_id"] for r in AUD
         if r["exists"] and (not r["module_page"] or not r["source_position"])], [],
        len(AUD), "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("NO_REPLACEMENT_BINDING_WAS_MANUFACTURED", SOURCE_AUDIT,
        [r["row_id"] for r in AUD if r["replacement_manufactured"]], [], len(AUD),
        "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("THE_NOT_FOUND_TOKEN_IS_DECLARED", SOURCE_AUDIT,
        CV.NOT_FOUND_TOKEN, "BRIEF_REFERENCE_NOT_FOUND_IN_CONTROLLED_EXTRACT", 1,
        "T04_SOURCE_ROW_AUDIT_v1.md")
    chk("EVERY_BINDING_IS_CLASSIFIED", SOURCE_AUDIT,
        sorted({r["semantic_binding"] for r in AUD if r["exists"]}), ["CONTRADICTORY"],
        len(AUD), "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("ROW_076_CONTRADICTS_THE_LIVE_SET_B_DISTRACTOR", SOURCE_AUDIT,
        [(l["option_set"], l["position"]) for r in AUD if r["row_id"] == "T04-ROW-076"
         for l in r["q5_links"] if l["relation"] == "CONTRADICTS"],
        [("LIVE_SET_B", 5)], len(AUD), "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("ROW_074_SUPPORTS_A_PROPOSED_KEY", SOURCE_AUDIT,
        [(l["position"], l["is_proposed_key"]) for r in AUD if r["row_id"] == "T04-ROW-074"
         for l in r["q5_links"]
         if l["option_set"] == "LIVE_SET_B" and l["relation"] == "SUPPORTS"],
        [(4, True)], len(AUD), "T04_SOURCE_ROW_AUDIT_v1.json")
    chk("ROW_077_BEARS_ONLY_ON_THE_REJECTED_SET_A", SOURCE_AUDIT,
        sorted({l["option_set"] for r in AUD if r["row_id"] == "T04-ROW-077"
                for l in r["q5_links"]}), ["REJECTED_SET_A"], len(AUD),
        "T04_SOURCE_ROW_AUDIT_v1.json")

    # ==================== 5. NAMESPACE ====================
    chk("TWO_LIVE_REGISTERS", NAMESPACE, AL["registers"], ["T04-EXT", "T04-OPEN"], 2,
        "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("EVERY_HISTORICAL_E_ID_IS_ACCOUNTED_FOR", NAMESPACE,
        AL["every_historical_id_accounted"], True, len(AL["alias_rows"]),
        "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("NO_TWO_REGISTERS_SHARE_AN_UNQUALIFIED_ID", NAMESPACE,
        AL["unqualified_collisions"], [], AL["live_count"],
        "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("HISTORICAL_RECORDS_WERE_NOT_REWRITTEN", NAMESPACE,
        AL["historical_records_rewritten"], False, 1,
        "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("EVERY_LIVE_ID_CARRIES_ITS_REGISTER_PREFIX", NAMESPACE,
        [i for i in AL["live_ids"] if not any(i.startswith(r + "-")
                                              for r in AL["registers"])], [],
        AL["live_count"], "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("THREE_HISTORICAL_ITEMS_CLOSED_BEFORE_THE_SPLIT", NAMESPACE,
        sorted(AL["closed_before_the_split"]), ["E-01", "E-03", "E-07"],
        len(AL["alias_rows"]), "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("EVERY_CLOSED_ALIAS_NAMES_WHAT_CLOSED_IT", NAMESPACE,
        [a["historical_id"] for a in AL["alias_rows"]
         if not a["live_id"] and not a.get("closed_by")], [], len(AL["alias_rows"]),
        "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("THE_ONLY_EXTRACTION_ITEM_INHERITED_IS_E05", NAMESPACE,
        [a["historical_id"] for a in AL["alias_rows"] if a["register"] == "T04-EXT"],
        ["E-05"], len(AL["alias_rows"]), "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("EVERY_LIVE_ID_SITS_INSIDE_ITS_REGISTER_BLOCK", NAMESPACE,
        AL["ids_outside_their_block"], [], AL["live_count"],
        "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("THE_BLOCKS_DO_NOT_OVERLAP", NAMESPACE,
        AL["register_blocks"]["T04-EXT"][1] < AL["register_blocks"]["T04-OPEN"][0], True,
        len(AL["register_blocks"]), "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")
    chk("THIS_STAGE_RAISED_TWO_NEW_LIVE_ITEMS", NAMESPACE,
        sorted(n["live_id"] for n in AL["new_items"]), ["T04-EXT-02", "T04-OPEN-55"],
        len(AL["new_items"]), "T04_LIVE_NAMESPACE_ALIAS_MAP_v1.json")

    # ==================== 6. ORACLE INDEPENDENCE ====================
    chk("EVERY_RELEASE_CRITICAL_GATE_IS_AUDITED", ORACLE,
        OA["release_critical_gates"] >= 10, True, OA["release_critical_gates"],
        "T04_ORACLE_INDEPENDENCE_AUDIT_v1.json")
    chk("EVERY_EXPECTED_SOURCE_IS_FROM_THE_DECLARED_SET", ORACLE,
        [r["gate_id"] for r in OA["rows"]
         if r["expected_value_source"] not in CV.EXPECTED_SOURCE_KINDS], [],
        len(OA["rows"]), "T04_ORACLE_INDEPENDENCE_AUDIT_v1.json")
    chk("EVERY_SHARED_GENERATOR_GATE_IS_JUSTIFIED", ORACLE,
        sorted(set(OA["shared_generator"]) - set(OA["shared_generator_justified"])), [],
        len(OA["rows"]), "T04_ORACLE_INDEPENDENCE_AUDIT_v1.json")
    chk("AT_MOST_ONE_GATE_SHARES_A_GENERATOR", ORACLE,
        len(OA["shared_generator"]) <= 1, True, len(OA["rows"]),
        "T04_ORACLE_INDEPENDENCE_AUDIT_v1.json")
    chk("EVERY_GATE_CAN_SEE_A_MUTATION_OF_THE_GENERATED_SIDE", ORACLE,
        [r["gate_id"] for r in OA["rows"]
         if not r["mutation_of_generated_side_detectable"]], [], len(OA["rows"]),
        "T04_ORACLE_INDEPENDENCE_AUDIT_v1.json")
    # Two came from earlier suites; two more were found by this suite's own fixtures A-01
    # and A-03, which is the only reason they are on the list at all.
    chk("EVERY_SELF_REFERENTIAL_GATE_IS_RECORDED_AS_FIXED", ORACLE,
        sorted(OA["fixed_after_a_fixture"]),
        ["EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO_PANELS",
         "EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_DECK",
         "THE_PAGE_BUDGET_STAYS_WITHIN_THE_RENDERER_CAPACITY",
         "THE_RELEASE_DECISION_IS_CARRIED_FORWARD"], len(OA["rows"]),
        "T04_ORACLE_INDEPENDENCE_AUDIT_v1.md")
    chk("THE_TWO_LANE_A_ORACLE_DEFECTS_ARE_ATTRIBUTED_TO_THEIR_FIXTURES", ORACLE,
        sorted(r["gate_id"] for r in OA["rows"]
               if r["history"] and r["suite"] == SUITE_ID),
        ["EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO_PANELS",
         "EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_DECK"], len(OA["rows"]),
        "T04_ORACLE_INDEPENDENCE_AUDIT_v1.md")
    chk("THE_FILTERED_POPULATION_PROTECTION_IS_PRESERVED", ORACLE,
        any("filtered-population" in x for x in OA["preserved_protections"]), True,
        len(OA["preserved_protections"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("THE_EXACT_XML_ELEMENT_PROTECTION_IS_PRESERVED", ORACLE,
        any("exact namespace" in x for x in OA["preserved_protections"]), True,
        len(OA["preserved_protections"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")

    # ==================== 7. STATUS GUARD ====================
    chk("THE_B1_ARTIFACT_IS_A_LAYOUT_STORYBOARD", STATUS_GUARD,
        SM.CURRENT_STATUS, "T04_LAYOUT_STORYBOARD_BUILT", 1,
        "t04_state_model_v1.py")
    chk("THE_STRONGER_CLAIMS_ARE_NOT_MADE", STATUS_GUARD,
        [c for c in SM.FORBIDDEN_STATUS_CLAIMS if c == SM.CURRENT_STATUS], [],
        len(SM.FORBIDDEN_STATUS_CLAIMS), "t04_state_model_v1.py")
    chk("THREE_FORBIDDEN_CLAIMS_ARE_DECLARED", STATUS_GUARD,
        sorted(SM.FORBIDDEN_STATUS_CLAIMS),
        ["T04_CANONICAL_PRODUCTION_TEMPLATE", "T04_INTERACTION_REVIEW_COMPLETE",
         "T04_STORYBOARD_FROZEN"], len(SM.FORBIDDEN_STATUS_CLAIMS),
        "t04_state_model_v1.py")
    chk("NO_FORBIDDEN_CLAIM_APPEARS_IN_THE_APPENDIX", STATUS_GUARD,
        [c for c in SM.FORBIDDEN_STATUS_CLAIMS if c in deck], [],
        len(SM.FORBIDDEN_STATUS_CLAIMS), CV.APPENDIX_NAME)
    chk("THE_INSPECTION_PACKAGE_FORBIDS_HAND_PATCHING", STATUS_GUARD,
        "never hand-patched" in CV.CORRECTION_POLICY, True, 1,
        "T04_NATIVE_POWERPOINT_INSPECTION_PACKAGE_v1.md")
    chk("THE_CORRECTION_TEMPLATE_HAS_ITS_FIELDS", STATUS_GUARD,
        len(CV.CORRECTION_INTAKE_FIELDS) >= 10, True,
        len(CV.CORRECTION_INTAKE_FIELDS),
        "T04_NATIVE_POWERPOINT_INSPECTION_PACKAGE_v1.json")
    chk("NO_MMD_REACT_SCORM_OR_LMS", STATUS_GUARD,
        (SB.MMD_PRODUCTION_STARTED, SB.REACT_STARTED, SB.SCORM_STARTED,
         SB.LMS_UPLOAD_STARTED), (0, 0, 0, 0), 4, "t04_storyboard_model_v1.py")
    chk("EVERY_DECLARED_ARTIFACT_EXISTS", STATUS_GUARD,
        [n for n in SE.NEW_ARTIFACTS if not os.path.exists(os.path.join(T04, n))], [],
        len(SE.NEW_ARTIFACTS), "docs/pl06/t04/")

    # ==================== 8. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "T04_STATE_COVERAGE_QA_v1", 1,
        "t04_state_qa_v1.py")
    chk("SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE", ACCOUNTING, SUITE_ID != PRIOR_SUITE_ID,
        True, 2, "t04_state_qa_v1.py")
    chk("NOT_CHECKED_IS_PUBLISHED", ACCOUNTING, len(NOT_CHECKED) >= 5, True,
        len(NOT_CHECKED), "t04_state_qa_v1.py")
    chk("EVERY_GATE_IS_TYPED", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res),
        "t04_state_qa_v1.py")
    chk("EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT", ACCOUNTING,
        [r["gate_id"] for r in res if not r["source_artifact"]], [], len(res),
        "t04_state_qa_v1.py")
    chk("NO_DUPLICATE_GATE_IDS", ACCOUNTING,
        len({r["gate_id"] for r in res}), len(res), len(res), "t04_state_qa_v1.py")
    chk("NO_VACUOUS_GATES", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res), "t04_state_qa_v1.py")
    return res


def accounting(rows):
    by = {}
    for r in rows:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    return dict(SUITE_ID=SUITE_ID, ACTIVE_GATE_COUNT=len(rows),
                ACTIVE_GATES_PASSING=len([r for r in rows if r["ok"]]),
                VACUOUS_GATES=[r["gate_id"] for r in rows if r["vacuous"]],
                BY_TYPE=dict(sorted(by.items())), NOT_CHECKED=NOT_CHECKED,
                FAILING=[r["gate_id"] for r in rows if not r["ok"]])


if __name__ == "__main__":
    rows = run()
    a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows)
    t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        flag = "VACU" if r["vacuous"] else ("PASS" if r["ok"] else "FAIL")
        line = (f"{flag}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  "
                f"n={r['population']:<5} {r['value']!r}")
        print(line[:230] + ("" if r["ok"] else f"   EXPECTED {r['expected']!r}"[:180]))
    print()
    print(f"SUITE_ID = {a['SUITE_ID']}")
    print(f"{a['ACTIVE_GATES_PASSING']}/{a['ACTIVE_GATE_COUNT']} active gates PASS")
    print(f"VACUOUS_GATES = {a['VACUOUS_GATES']}")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<20} {v}")
    sys.exit(1 if a["FAILING"] else 0)
