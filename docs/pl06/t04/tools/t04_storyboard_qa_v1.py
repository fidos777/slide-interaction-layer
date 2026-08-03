# -*- coding: utf-8 -*-
"""Stage 4.2F-B1 QA — structural and rendered checks over the built T04 storyboard.

    SUITE_ID = T04_STORYBOARD_QA_v1
    python3 docs/pl06/t04/tools/t04_storyboard_qa_v1.py

The PPTX is re-opened FROM DISK and its text re-extracted, so a sentence that exists only in
the builder cannot pass. The preview PNGs are re-opened too and measured, so a page that
rendered blank or truncated cannot pass either.

What this suite cannot do: tell you the deck looks right in Microsoft PowerPoint. No Impress
filter exists in this environment. That is recorded as NOT_CHECKED, not glossed.

Separate from T04_AUTHORITY_DECISION_INGESTION_QA_v1 (251) and
T04_SUPPLEMENTARY_EVIDENCE_QA_v1 (133). Never add the totals.
"""
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_storyboard_model_v1 as M        # noqa: E402
import t04_storyboard_build_v1 as B        # noqa: E402
import t04_authority_data_v1 as A          # noqa: E402
import t04_content_data_v1 as C            # noqa: E402
import t04_supplementary_evidence_v1 as S  # noqa: E402

SUITE_ID = "T04_STORYBOARD_QA_v1"
PRIOR_SUITE_ID = "T04_SUPPLEMENTARY_EVIDENCE_QA_v1"

SEQUENCE = "SEQUENCE"
TEXT_PROVENANCE = "TEXT_PROVENANCE"
SOURCE_TRACE = "SOURCE_TRACE"
AUTHORITY_TRACE = "AUTHORITY_TRACE"
INTERACTION = "INTERACTION"
VISUAL_SCOPE = "VISUAL_SCOPE"
ASSESSMENT = "ASSESSMENT"
EVIDENCE = "EVIDENCE"
PPTX_STRUCTURE = "PPTX_STRUCTURE"
RENDER = "RENDER"
PRODUCTION_GUARD = "PRODUCTION_GUARD"
ACCOUNTING = "ACCOUNTING"

GATE_TYPES = {SEQUENCE, TEXT_PROVENANCE, SOURCE_TRACE, AUTHORITY_TRACE, INTERACTION,
              VISUAL_SCOPE, ASSESSMENT, EVIDENCE, PPTX_STRUCTURE, RENDER,
              PRODUCTION_GUARD, ACCOUNTING}

NOT_CHECKED = [
    "how Microsoft PowerPoint paginates, autofits or font-substitutes this deck — no "
    "Impress filter exists here, so no native render was performed",
    "whether the deck reads well to a native Malay speaker",
    "whether the storyboard is instructionally effective",
    "whether any visual placeholder describes an achievable asset — no artwork exists",
    "whether the five answer keys are correct — none is final",
    "whether Bariah will accept this storyboard",
    "the true identity of the supplementary screenshot — still no binary",
]

PPTX_PATH = os.path.join(M.PPTX_DIR, M.PPTX_NAME)
PREVIEW_DIR = os.path.join(T04, "storyboard_preview")

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"


def _pptx_slide_texts():
    """Every <a:t> string per slide, read back from the saved package."""
    import xml.etree.ElementTree as ET
    z = zipfile.ZipFile(PPTX_PATH)
    names = sorted((n for n in z.namelist()
                    if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                   key=lambda n: int(re.search(r"(\d+)", n).group(1)))
    out = []
    for n in names:
        root = ET.fromstring(z.read(n))
        out.append([(t.text or "") for t in root.iter(f"{{{A_NS}}}t")])
    return out


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

    SCR = M.screens()
    SLD = M.slides()
    PAG = M.pagination_report()
    ST = M.source_traceability()
    AT = M.authority_traceability()
    IM = M.interaction_model()
    VM = M.visual_mapping()
    VT = M.visual_totals()
    ASX = M.assessment_status()
    EV = M.evidence_status()
    pptx_present = os.path.exists(PPTX_PATH)
    slide_texts = _pptx_slide_texts() if pptx_present else []
    deck_text = " ".join(t for s in slide_texts for t in s)

    # ==================== 1. SEQUENCE ====================
    chk("EXACTLY_TWENTY_TWO_SCREENS", SEQUENCE, len(SCR), 22, len(SCR),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("SCREEN_IDS_ARE_CONTIGUOUS", SEQUENCE,
        [s["screen_id"] for s in SCR], [f"T04-S{i:02d}" for i in range(1, 23)], len(SCR),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("TITLES_MATCH_THE_FIXED_LIST", SEQUENCE,
        [s["title_ms"] for s in SCR], M.EXPECTED_TITLES, len(SCR),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("THE_FINAL_SCREEN_IS_TAMAT_TOPIK", SEQUENCE, SCR[-1]["title_ms"], "Tamat Topik", 1,
        "T04_STORYBOARD_MODEL_v1.json")
    chk("SCREENS_AGREE_WITH_THE_FROZEN_SEQUENCE", SEQUENCE,
        [s["screen_id"] for s in SCR], [s["screen_id"] for s in A._final_sequence()],
        len(SCR), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("TITLES_AGREE_WITH_THE_FROZEN_SEQUENCE", SEQUENCE,
        [s["title_ms"] for s in SCR], [s["working_title"] for s in A._final_sequence()],
        len(SCR), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("INTERNAL_UNIT_ID_IS_TRACEABLE", SEQUENCE,
        sorted({s["internal_unit_id"] for s in SCR}), ["K5-PL06-T04-B01"], len(SCR),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("LEARNER_DISPLAY_UNIT_IS_TOPIK_4", SEQUENCE,
        sorted({s["learner_display_unit"] for s in SCR}), ["Topik 4"], len(SCR),
        "T04_STORYBOARD_MODEL_v1.json")
    # The word must not appear anywhere a learner can see it, deck included.
    leaks = [f"{s['screen_id']}:{b['text'][:40]}" for s in SCR for b in s["content_blocks"]
             for t in M.BANNED_LEARNER_TERMS if t in b["text"]]
    leaks += [f"title:{s['screen_id']}" for s in SCR
              for t in M.BANNED_LEARNER_TERMS if t in s["title_ms"]]
    chk("NO_LEARNER_FACING_BAHAGIAN", SEQUENCE, sorted(set(leaks)), [],
        sum(len(s["content_blocks"]) for s in SCR), "T04_STORYBOARD_MODEL_v1.json")
    chk("NO_BAHAGIAN_ANYWHERE_IN_THE_DECK", SEQUENCE,
        [t for t in M.BANNED_LEARNER_TERMS if t in deck_text], [],
        len(deck_text.split()), M.PPTX_NAME)

    # The ban is on the capitalised unit-label sense only. The module's own lowercase
    # "bahagian" — a part of a plant — must survive, or a gate would be deleting real content
    # to satisfy itself.
    chk("THE_BAN_IS_CASE_SENSITIVE", SEQUENCE,
        M.BANNED_TERM_IS_CASE_SENSITIVE, True, 1, "t04_storyboard_model_v1.py")
    chk("THE_MODULES_LOWERCASE_BAHAGIAN_SURVIVES", SEQUENCE,
        "Membuang bahagian berpenyakit" in deck_text, True, 1, M.PPTX_NAME)
    chk("THE_COMMON_NOUN_EXCEPTION_IS_DOCUMENTED", SEQUENCE,
        bool(M.BANNED_TERM_COMMON_NOUN_NOTE), True, 1, "t04_storyboard_model_v1.py")

    # Pagination: more slides than screens is fine; losing a block is not.
    chk("PAGINATION_LOSES_NOTHING", SEQUENCE,
        [p["screen_id"] for p in PAG if not p["no_block_lost"]], [], len(PAG),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("EVERY_PAGE_FITS", SEQUENCE,
        [p["screen_id"] for p in PAG if not p["fits"]], [], len(PAG),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("THE_PAGE_BUDGET_STAYS_WITHIN_THE_RENDERER_CAPACITY", SEQUENCE,
        [p["screen_id"] for p in PAG if not p["budget_within_capacity"]], [], len(PAG),
        "t04_storyboard_model_v1.py")
    chk("SLIDE_COUNT_IS_THE_SUM_OF_PAGES", SEQUENCE,
        len(SLD), sum(p["pages"] for p in PAG), len(SLD),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("SCREEN_COUNT_IS_NOT_CONFLATED_WITH_SLIDE_COUNT", SEQUENCE,
        len(SCR) != len(SLD), True, 2, "T04_STORYBOARD_MODEL_v1.json")
    chk("EVERY_CONTINUATION_IS_LABELLED", SEQUENCE,
        [s["screen_id"] for s in SLD if s["page_count"] > 1 and not s["title_suffix"]], [],
        len(SLD), "T04_STORYBOARD_MODEL_v1.json")

    # ==================== 2. TEXT PROVENANCE ====================
    blocks = [b for s in SCR for b in s["content_blocks"]]
    chk("EVERY_BLOCK_CARRIES_A_PROVENANCE", TEXT_PROVENANCE,
        [b["text"][:40] for b in blocks if b["provenance"] not in M.PROVENANCE], [],
        len(blocks), "T04_STORYBOARD_MODEL_v1.json")
    chk("NO_CAIR_INSTRUCTIONAL_CONTENT_CATEGORY", TEXT_PROVENANCE,
        [b["text"][:40] for b in blocks
         if b["provenance"] == M.FORBIDDEN_PROVENANCE], [], len(blocks),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("ALL_FIVE_PROVENANCES_ARE_USED", TEXT_PROVENANCE,
        sorted({b["provenance"] for b in blocks}), sorted(M.PROVENANCE), len(blocks),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("ASSESSMENT_OPTIONS_ARE_NOT_CLAIMED_AS_MODULE_TEXT", TEXT_PROVENANCE,
        [b["text"][:40] for b in blocks
         if b["content_type"] == "QUIZ_OPTION"
         and b["provenance"] == "SOURCE_CONTROLLED"], [],
        len([b for b in blocks if b["content_type"] == "QUIZ_OPTION"]),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("SOURCE_BLOCKS_CARRY_A_ROW_ID", TEXT_PROVENANCE,
        [b["text"][:40] for b in blocks
         if b["provenance"] == "SOURCE_CONTROLLED" and not b["row_id"]], [], len(blocks),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("AUTHORITY_BLOCKS_CARRY_A_REFERENCE", TEXT_PROVENANCE,
        [b["text"][:40] for b in blocks
         if b["provenance"] in ("AUTHORITY_SUPPLIED", "AUTHORITY_SELECTED")
         and not b.get("authority_ref")], [], len(blocks),
        "T04_STORYBOARD_MODEL_v1.json")
    # Structural furniture may not teach. If a UI string is long enough to be a sentence of
    # content, it is not furniture.
    long_ui = [b["text"] for b in blocks
               if b["provenance"] == "CAIR_STRUCTURAL" and len(b["text"]) > 60]
    chk("STRUCTURAL_FURNITURE_STAYS_SHORT", TEXT_PROVENANCE, long_ui, [],
        len([b for b in blocks if b["provenance"] == "CAIR_STRUCTURAL"]),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("EVERY_MODEL_BLOCK_APPEARS_IN_THE_DECK", TEXT_PROVENANCE,
        [b["text"][:50] for b in blocks
         if b["text"] and b["text"] not in deck_text], [], len(blocks), M.PPTX_NAME)

    # ==================== 3. SOURCE TRACEABILITY ====================
    chk("SOURCE_STRINGS_ARE_VERBATIM", SOURCE_TRACE,
        [x["row_id"] for x in ST if not x["verbatim"]], [], len(ST),
        "T04_STORYBOARD_SOURCE_TRACEABILITY_v1.json")
    chk("EVERY_TRACED_ROW_EXISTS", SOURCE_TRACE,
        sorted({x["row_id"] for x in ST if x["row_id"] not in C.BY_ID}), [], len(ST),
        "T04_SOURCE_EXTRACT_v1.json")
    chk("EVERY_TRACED_ROW_IS_MODULE_ATTESTED", SOURCE_TRACE,
        sorted({x["authority_class"] for x in ST}), ["MODULE_SOURCE_ATTESTED"], len(ST),
        "T04_SOURCE_EXTRACT_v1.json")
    # Three screens carry source rows but show authority-written replacement text instead.
    # They are named, so a fourth cannot join them silently.
    chk("EVERY_CONTENT_SCREEN_HAS_SOURCE_STRINGS", SOURCE_TRACE,
        [s["screen_id"] for s in SCR if s["source_row_ids"]
         and s["screen_id"] not in M.AUTHORITY_REPLACED_CONTENT_SCREENS
         and not any(x["screen_id"] == s["screen_id"] for x in ST)], [], len(SCR),
        "T04_STORYBOARD_SOURCE_TRACEABILITY_v1.json")
    chk("THE_AUTHORITY_REPLACED_SCREENS_ARE_NAMED", SOURCE_TRACE,
        sorted(s["screen_id"] for s in SCR if s["source_row_ids"]
               and not any(x["screen_id"] == s["screen_id"] for x in ST)),
        sorted(M.AUTHORITY_REPLACED_CONTENT_SCREENS), len(SCR),
        "T04_STORYBOARD_MODEL_v1.json")
    chk("SCREEN_ROW_SETS_MATCH_THE_FROZEN_SEQUENCE", SOURCE_TRACE,
        {s["screen_id"]: s["source_row_ids"] for s in SCR},
        {s["screen_id"]: s["source_row_ids"] for s in A._final_sequence()}, len(SCR),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")

    # The B0.8 -> B0.9 renumbering translation must actually have been applied.
    ren = M.renumbering_applied()
    chk("THE_RENUMBERING_TRANSLATION_WAS_APPLIED", SOURCE_TRACE,
        (ren["obligations_translated"], ren["asset_groups_translated"]), (8, 2), 2,
        "T04_STORYBOARD_MODEL_v1.json")
    chk("HARD_LANDSCAPE_GROUP_LANDS_ON_HARD_LANDSCAPE_SCREENS", SOURCE_TRACE,
        sorted(x["screen_id"] for x in VM if "AG-07" in x["asset_group_ids"]),
        ["T04-S18", "T04-S19"], len(VM),
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("RACUN_COMPLIANCE_GROUP_LANDS_ON_THE_RACUN_COMPLIANCE_SCREENS", SOURCE_TRACE,
        sorted(x["screen_id"] for x in VM if "AG-06" in x["asset_group_ids"]),
        ["T04-S14", "T04-S15", "T04-S16", "T04-S17"], len(VM),
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")

    # ==================== 4. AUTHORITY TRACEABILITY ====================
    ids = {d["decision_id"] for d in A._decision_register()}
    chk("EVERY_SCREEN_HAS_AN_AUTHORITY_BINDING", AUTHORITY_TRACE,
        [s["screen_id"] for s in SCR
         if not any(x["screen_id"] == s["screen_id"] for x in AT)], [], len(SCR),
        "T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.json")
    chk("EVERY_BOUND_DECISION_EXISTS", AUTHORITY_TRACE,
        sorted({x["decision_id"] for x in AT if x["decision_id"] not in ids}), [], len(AT),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_BINDING_CARRIES_ITS_QUOTE", AUTHORITY_TRACE,
        [x["decision_id"] for x in AT if not x["authority_quote"]], [], len(AT),
        "T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.json")
    # Every screen binding traces to the DOCX. Nothing on a learner screen rests on the
    # WhatsApp exchange, which is the weaker evidence — worth asserting, not assuming.
    chk("EVERY_BINDING_CARRIES_AN_EVIDENCE_GRADE", AUTHORITY_TRACE,
        sorted({x["evidence_grade"] for x in AT}), ["VERIFIED_PRIMARY_ARTIFACT"], len(AT),
        "T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.json")
    chk("NO_SCREEN_IS_BOUND_TO_A_NON_AUTHORITY_RECORD", AUTHORITY_TRACE,
        sorted({x["decision_id"] for x in AT if x["authority"] != "BARIAH_AHMAD"}), [],
        len(AT), "T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.json")

    # ==================== 5. INTERACTION ====================
    chk("EVERY_SCREEN_HAS_AT_LEAST_ONE_STATE", INTERACTION,
        [x["screen_id"] for x in IM if x["state_count"] < 1], [], len(IM),
        "T04_STORYBOARD_INTERACTION_MODEL_v1.json")
    chk("STATIC_SCREENS_HAVE_ONE_STATE", INTERACTION,
        [x["screen_id"] for x in IM
         if x["treatment"] == "CONTENT_STATIC" and x["state_count"] != 1], [],
        len([x for x in IM if x["treatment"] == "CONTENT_STATIC"]),
        "T04_STORYBOARD_INTERACTION_MODEL_v1.json")
    chk("REVEAL_SCREENS_HAVE_MORE_THAN_ONE_STATE", INTERACTION,
        [x["screen_id"] for x in IM
         if x["treatment"] == "CLICK_TO_REVEAL" and x["state_count"] < 3], [],
        len([x for x in IM if x["treatment"] == "CLICK_TO_REVEAL"]),
        "T04_STORYBOARD_INTERACTION_MODEL_v1.json")
    chk("STATES_AGREE_WITH_THE_FROZEN_SEQUENCE", INTERACTION,
        {x["screen_id"]: x["states"] for x in IM},
        {s["screen_id"]: s["interaction_states"] for s in A._final_sequence()}, len(IM),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("THE_HSE_REVEAL_RISK_IS_CARRIED_WITH_ITS_OWNER", INTERACTION,
        [(x["screen_id"], x["risk_owner"]) for x in IM if x["risk_owner"]],
        [("T04-S16", "BARIAH_AHMAD")], len(IM),
        "T04_STORYBOARD_INTERACTION_MODEL_v1.json")
    chk("EVERY_REVEAL_SCREEN_STATES_ITS_RESIDUAL_RISK", INTERACTION,
        [x["screen_id"] for x in IM if x["reveal_count"] and not x["residual_risk"]], [],
        len(IM), "T04_STORYBOARD_INTERACTION_MODEL_v1.json")

    # ==================== 6. VISUAL SCOPE ====================
    chk("FORTY_SIX_VISUAL_OBLIGATIONS", VISUAL_SCOPE, VT["visual_obligations"], 46, 46,
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("EIGHT_ASSET_GROUPS", VISUAL_SCOPE, VT["asset_groups"], 8, 8,
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("FORTY_ONE_PROPOSED_UNIQUE_ASSETS", VISUAL_SCOPE, VT["proposed_unique_assets"], 41,
        41, "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("THREE_DO_NOT_REUSE_ITEMS", VISUAL_SCOPE, VT["do_not_reuse_items"], 3, 3,
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("NO_ARTWORK_WAS_PRODUCED", VISUAL_SCOPE, VT["artwork_produced"], 0, 1,
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("EVERY_VISUAL_SLOT_IS_A_PLACEHOLDER", VISUAL_SCOPE,
        [x["screen_id"] for x in VM if x["asset_group_ids"]
         and (x["artwork_status"] != "NOT_PRODUCED" or not x["placeholder_only"])], [],
        len(VM), "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("S14_REUSES_AG06_AND_ADDS_NOTHING", VISUAL_SCOPE,
        [(x["asset_group_ids"], x["adds_unique_assets"], x["reuses_existing_group"])
         for x in VM if x["screen_id"] == "T04-S14"], [(["AG-06"], 0, True)], len(VM),
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    dnr_screens = sorted({x["screen_id"] for x in VM if x["do_not_reuse_obligations"]})
    chk("DO_NOT_REUSE_RESTRICTIONS_APPEAR_ON_THEIR_SCREENS", VISUAL_SCOPE,
        dnr_screens, ["T04-S10", "T04-S16"], len(VM),
        "T04_STORYBOARD_VISUAL_MAPPING_v1.json")
    chk("EVERY_DO_NOT_REUSE_ITEM_LANDS_SOMEWHERE", VISUAL_SCOPE,
        sorted({o for x in VM for o in x["do_not_reuse_obligations"]}),
        sorted(x["obligation_id"] for x in A._do_not_reuse_items()), len(VM),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("THE_DO_NOT_REUSE_WARNING_IS_IN_THE_DECK", VISUAL_SCOPE,
        "TIDAK BOLEH DIKONGSI" in deck_text, True, 1, M.PPTX_NAME)
    chk("THE_NO_ARTWORK_NOTICE_IS_IN_THE_DECK", VISUAL_SCOPE,
        "ASET BELUM DIHASILKAN" in deck_text, True, 1, M.PPTX_NAME)

    # ==================== 7. ASSESSMENT ====================
    chk("FOUR_MCQ_AND_ONE_MULTIPLE_RESPONSE", ASSESSMENT,
        (ASX["mcq_count"], ASX["multiple_response_count"]), (4, 1), 5,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("PASS_MARK_IS_SIXTY_PERCENT", ASSESSMENT, ASX["pass_mark"], "60 peratus", 1,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("Q5_USES_CHECKBOXES_NOT_LETTERS", ASSESSMENT,
        [x["option_marker_style"] for x in ASX["items"]
         if x["question_type"] == "MULTIPLE_RESPONSE"], ["CHECKBOX"], 5,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("MCQ_ITEMS_KEEP_LETTERS", ASSESSMENT,
        sorted({x["option_marker_style"] for x in ASX["items"]
                if x["question_type"] == "MCQ"}), ["LETTER"], 4,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("NO_ABC_LABEL_ON_ANY_Q5_OPTION_IN_THE_DECK", ASSESSMENT,
        [o["text_ms"] for q in A.quiz_items() if q["question_id"] == "T04-QZ-Q5"
         for o in q["options"]
         if re.search(r"(?:^|\s)[A-F]\.\s" + re.escape(o["text_ms"][:20]), deck_text)], [],
        6, M.PPTX_NAME)
    q5 = [q for q in A.quiz_items() if q["question_id"] == "T04-QZ-Q5"][0]
    chk("THE_FINAL_SET_B_DISTRACTORS_ARE_IN_THE_DECK", ASSESSMENT,
        [x["text_ms"] for x in S.SET_B_FROZEN if x["text_ms"] not in deck_text], [],
        len(S.SET_B_FROZEN), M.PPTX_NAME)
    chk("THE_REJECTED_SET_A_IS_NOT_IN_THE_DECK", ASSESSMENT,
        [x["text_ms"] for x in S.SET_A_REJECTED if x["text_ms"] in deck_text], [],
        len(S.SET_A_REJECTED), M.PPTX_NAME)
    chk("THE_SUPERSEDED_CAIR_DRAFT_IS_NOT_IN_THE_DECK", ASSESSMENT,
        [x["superseded_b09_text"] for x in S.SET_B_FROZEN
         if x["superseded_b09_text"] in deck_text], [], len(S.SET_B_FROZEN), M.PPTX_NAME)
    chk("ANSWER_KEYS_ARE_NOT_BARIAH_DIRECT_APPROVED", ASSESSMENT,
        (ASX["answer_key_status"], ASX["answer_key_is_bariah_direct_approved"]),
        ("PROPOSED_NOT_FINAL", False), 2,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("Q5_DISTRACTORS_ARE_NOT_BARIAH_DIRECT_AUTHORED", ASSESSMENT,
        (ASX["q5_distractor_provenance"],
         ASX["q5_distractors_are_bariah_direct_authored"]),
        ("AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS", False), 2,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("EXACTLY_ONE_STEM_IS_NOT_AUTHORITY_AUTHORED", ASSESSMENT,
        sorted(x["question_id"] for x in ASX["items"]
               if not x["stem_is_authority_authored"]), ["T04-QZ-Q5"], 5,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("EVERY_ITEM_KEEPS_ITS_SOURCE_BINDINGS", ASSESSMENT,
        [x["question_id"] for x in ASX["items"] if not x["source_row_ids"]], [], 5,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("NO_RUNTIME_ASSESSMENT_PACKET_WAS_GENERATED", ASSESSMENT,
        ASX["runtime_packet_generated"], False, 1,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")
    chk("E07_IS_REFLECTED_IN_THE_ASSESSMENT_REGISTER", ASSESSMENT,
        (ASX["e07_status"], ASX["e07_selected_set"]), ("CLOSED", "SET_B"), 2,
        "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json")

    # ==================== 8. EVIDENCE ====================
    chk("PRIMARY_EVIDENCE_IS_VERIFIED", EVIDENCE,
        (EV["primary_authority_evidence"]["verified"],
         EV["primary_authority_evidence"]["sha256"]),
        (True, A.PRIMARY_DOCX_SHA256), 2,
        "T04_STORYBOARD_EVIDENCE_STATUS_v1.json")
    chk("SUPPLEMENTARY_EVIDENCE_IS_STILL_UNVERIFIED", EVIDENCE,
        (EV["supplementary_authority_evidence"]["verified"],
         EV["supplementary_authority_evidence"]["sha256"]), (False, "NOT_SUPPLIED"), 2,
        "T04_STORYBOARD_EVIDENCE_STATUS_v1.json")
    # Asserted against the literal tokens, not against S.RELEASE_DECISION — comparing the
    # register to the object it was built from proves only that the copy succeeded.
    chk("THE_RELEASE_DECISION_IS_CARRIED_FORWARD", EVIDENCE,
        EV["release_decision"],
        ["T04_ASSESSMENT_DIVERGENCE_CLOSED", "STORYBOARD_LAYOUT_READY",
         "SUPPLEMENTARY_CNF_MAPPING_PARTIALLY_OPEN"], 3,
        "T04_STORYBOARD_EVIDENCE_STATUS_v1.json")
    chk("THE_FULL_APPROVAL_VERDICT_IS_NOT_CLAIMED", EVIDENCE,
        [t for t in EV["release_decision"]
         if t == "T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD"], [],
        len(EV["release_decision"]), "T04_STORYBOARD_EVIDENCE_STATUS_v1.json")
    chk("OPEN_ITEMS_ARE_CARRIED_FORWARD", EVIDENCE,
        sorted(o["open_id"] for o in EV["open_items"]),
        ["E-02", "E-04", "E-05", "E-06", "E-08"], len(EV["open_items"]),
        "T04_STORYBOARD_EVIDENCE_STATUS_v1.json")
    chk("THE_SOURCE_RISK_TOKEN_IS_UNCHANGED", EVIDENCE,
        EV["source_risk_token"],
        "SOURCE_REPRODUCIBILITY_OPEN_NONBLOCKING_FOR_T04_STORYBOARD_BUILD", 1,
        "T04_STORYBOARD_EVIDENCE_STATUS_v1.json")
    chk("THE_AUTHORITY_DOCX_IS_STILL_BYTE_IDENTICAL", EVIDENCE,
        os.path.getsize(os.path.join(REPO, A.EVIDENCE_DIR, A.PRIMARY_DOCX_NAME)),
        A.PRIMARY_DOCX_BYTES, 1, os.path.join(A.EVIDENCE_DIR, A.PRIMARY_DOCX_NAME))

    # ==================== 9. PPTX STRUCTURE ====================
    chk("THE_PPTX_EXISTS", PPTX_STRUCTURE, pptx_present, True, 1, M.PPTX_NAME)
    chk("THE_PPTX_IS_A_VALID_PACKAGE", PPTX_STRUCTURE,
        zipfile.ZipFile(PPTX_PATH).testzip() if pptx_present else "missing", None, 1,
        M.PPTX_NAME)
    chk("SLIDE_COUNT_MATCHES_THE_MODEL", PPTX_STRUCTURE,
        len(slide_texts), len(SLD) + 1, len(slide_texts), M.PPTX_NAME)
    chk("EVERY_SLIDE_HAS_TEXT", PPTX_STRUCTURE,
        [i + 1 for i, t in enumerate(slide_texts) if not any(x.strip() for x in t)], [],
        len(slide_texts), M.PPTX_NAME)
    chk("EVERY_SCREEN_ID_APPEARS_IN_THE_DECK", PPTX_STRUCTURE,
        [s["screen_id"] for s in SCR if s["screen_id"] not in deck_text], [], len(SCR),
        M.PPTX_NAME)
    chk("EVERY_TITLE_APPEARS_IN_THE_DECK", PPTX_STRUCTURE,
        [s["title_ms"] for s in SCR if s["title_ms"] not in deck_text], [], len(SCR),
        M.PPTX_NAME)
    chk("NO_MEDIA_IS_EMBEDDED", PPTX_STRUCTURE,
        [n for n in (zipfile.ZipFile(PPTX_PATH).namelist() if pptx_present else [])
         if n.startswith("ppt/media/")], [],
        len(zipfile.ZipFile(PPTX_PATH).namelist()) if pptx_present else 0, M.PPTX_NAME)
    chk("NO_EXTERNAL_RELATIONSHIP", PPTX_STRUCTURE,
        [n for n in (zipfile.ZipFile(PPTX_PATH).namelist() if pptx_present else [])
         if n.endswith(".rels")
         and b'TargetMode="External"' in zipfile.ZipFile(PPTX_PATH).read(n)], [],
        len(zipfile.ZipFile(PPTX_PATH).namelist()) if pptx_present else 0, M.PPTX_NAME)
    chk("SIXTEEN_BY_NINE_SLIDE_SIZE", PPTX_STRUCTURE,
        (int(B.SLIDE_W), int(B.SLIDE_H)), (12192000, 6858000), 2, M.PPTX_NAME)
    chk("NO_REPOSITORY_PATH_LEAKS_INTO_THE_DECK", PPTX_STRUCTURE,
        [p for p in ("docs/pl06", "reviews/storyboard", "/home/user") if p in deck_text],
        [], 3, M.PPTX_NAME)
    chk("NO_SHA256_LEAKS_INTO_THE_DECK", PPTX_STRUCTURE,
        bool(re.search(r"\b[0-9a-f]{64}\b", deck_text)), False, 1, M.PPTX_NAME)

    # ==================== 10. RENDER ====================
    previews = sorted(f for f in os.listdir(PREVIEW_DIR)) if os.path.isdir(PREVIEW_DIR) \
        else []
    chk("A_PREVIEW_EXISTS_FOR_EVERY_SLIDE", RENDER,
        len([f for f in previews if f.endswith(".png")]), len(SLD), len(previews),
        "docs/pl06/t04/storyboard_preview/")
    chk("NO_STALE_PREVIEW_PAGES", RENDER,
        sorted(f for f in previews if not f.endswith(".png")), [], len(previews),
        "docs/pl06/t04/storyboard_preview/")
    if previews:
        from PIL import Image
        sizes, blanks = set(), []
        for f in previews:
            if not f.endswith(".png"):
                continue
            im = Image.open(os.path.join(PREVIEW_DIR, f)).convert("L")
            sizes.add(im.size)
            if min(im.getdata()) > 200:      # nothing darker than near-white was drawn
                blanks.append(f)
    else:
        sizes, blanks = set(), ["no-previews"]
    chk("EVERY_PREVIEW_PAGE_HAS_INK", RENDER, blanks, [], len(previews),
        "docs/pl06/t04/storyboard_preview/")
    chk("EVERY_PREVIEW_PAGE_IS_THE_SAME_SIZE", RENDER, sorted(sizes), [(1280, 720)],
        len(previews), "docs/pl06/t04/storyboard_preview/")
    chk("NATIVE_RENDER_IS_DECLARED_NOT_CHECKED", RENDER,
        B.RENDER_STATUS.startswith("NOT_CHECKED"), True, 1,
        "t04_storyboard_build_v1.py")
    chk("THE_RENDER_LIMITATION_IS_STATED", RENDER,
        "layout approximation" in B.RENDER_NOTE, True, 1, "t04_storyboard_build_v1.py")
    chk("NO_POWERPOINT_EQUIVALENCE_IS_CLAIMED", RENDER,
        "MICROSOFT_POWERPOINT_EQUIVALENCE" in B.RENDER_STATUS, False, 1,
        "t04_storyboard_build_v1.py")

    # ==================== 11. PRODUCTION GUARDS ====================
    chk("NO_MMD_PRODUCTION", PRODUCTION_GUARD, M.MMD_PRODUCTION_STARTED, 0, 1,
        "t04_storyboard_model_v1.py")
    chk("NO_REACT_WORK", PRODUCTION_GUARD, M.REACT_STARTED, 0, 1,
        "t04_storyboard_model_v1.py")
    chk("NO_SCORM_WORK", PRODUCTION_GUARD, M.SCORM_STARTED, 0, 1,
        "t04_storyboard_model_v1.py")
    chk("NO_LMS_UPLOAD", PRODUCTION_GUARD, M.LMS_UPLOAD_STARTED, 0, 1,
        "t04_storyboard_model_v1.py")
    chk("NO_OTHER_PL_TOUCHED", PRODUCTION_GUARD, M.OTHER_PL_TOUCHED, 0, 1,
        "t04_storyboard_model_v1.py")
    chk("AUTHORITY_ARTIFACTS_UNMODIFIED", PRODUCTION_GUARD,
        M.AUTHORITY_ARTIFACTS_MODIFIED, 0, 1, "t04_storyboard_model_v1.py")
    chk("PRODUCTION_GENERATOR_UNTOUCHED", PRODUCTION_GUARD,
        M.PRODUCTION_GENERATOR_TOUCHED, 0, 1, "t04_storyboard_model_v1.py")
    chk("ONLY_T04_ARTIFACTS_WERE_EMITTED", PRODUCTION_GUARD,
        [n for n in M.NEW_ARTIFACTS if not n.startswith("T04_")], [],
        len(M.NEW_ARTIFACTS), "docs/pl06/t04/")
    chk("EVERY_DECLARED_ARTIFACT_EXISTS", PRODUCTION_GUARD,
        [n for n in M.NEW_ARTIFACTS if not os.path.exists(os.path.join(T04, n))], [],
        len(M.NEW_ARTIFACTS), "docs/pl06/t04/")
    chk("VERDICT_IS_FROM_THE_ALLOWED_SET", PRODUCTION_GUARD,
        M.VERDICT in M.ALLOWED_VERDICTS, True, len(M.ALLOWED_VERDICTS),
        "t04_storyboard_model_v1.py")

    # ==================== 12. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "T04_STORYBOARD_QA_v1", 1,
        "t04_storyboard_qa_v1.py")
    chk("SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE", ACCOUNTING, SUITE_ID != PRIOR_SUITE_ID,
        True, 2, "t04_storyboard_qa_v1.py")
    chk("NOT_CHECKED_IS_PUBLISHED", ACCOUNTING, len(NOT_CHECKED) >= 5, True,
        len(NOT_CHECKED), "t04_storyboard_qa_v1.py")
    chk("EVERY_GATE_IS_TYPED", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res),
        "t04_storyboard_qa_v1.py")
    chk("EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT", ACCOUNTING,
        [r["gate_id"] for r in res if not r["source_artifact"]], [], len(res),
        "t04_storyboard_qa_v1.py")
    chk("NO_DUPLICATE_GATE_IDS", ACCOUNTING,
        len({r["gate_id"] for r in res}), len(res), len(res), "t04_storyboard_qa_v1.py")
    chk("NO_VACUOUS_GATES", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res),
        "t04_storyboard_qa_v1.py")

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
