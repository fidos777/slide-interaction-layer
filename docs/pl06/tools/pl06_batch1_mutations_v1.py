# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-B2 Lane B.

    SUITE_ID = PL06_AUTHORITY_HARVEST_BATCH1_QA_v1
    python3 docs/pl06/tools/pl06_batch1_mutations_v1.py

The defects this suite exists to catch are all forms of *asking Bariah to approve something
that is not there*: a fifth unit slipped into the batch, a T04 decision quietly generalised,
a learning outcome or quiz stem written for a unit nobody has read, a screen that maps to no
heading, a decision with nowhere to answer it, a GABUNG with no target, an answer key given
an authority it does not have, a shared boundary that goes quiet, a visual obligation
conflated with an asset, a population that shrinks without anyone noticing, or one of the
two projections drifting from the other.

Fixtures marked `rebuild` regenerate the DOCX from the mutated model and leave the corrupted
file on disk for the suite to re-read. The real package is rebuilt in the `finally`, and
`docx_rebuilt_clean` compares the extracted text digest back to the baseline.
"""
import copy
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pl06_batch1_data_v1 as B   # noqa: E402
import pl06_batch1_emit_v1 as E   # noqa: E402
import pl06_docx_v1 as D          # noqa: E402
import pl06_batch1_qa_v1 as QA    # noqa: E402

TARGETS = {"B": B, "E": E, "D": D, "QA": QA}

_BASE_UNITS = _BASE_DEC = _BASE_TRACE = None


def _units(fn):
    """Patch the unit projection so every consumer sees the mutation."""
    def apply():
        def patched():
            rows = copy.deepcopy(_BASE_UNITS)
            fn(rows)
            return rows
        return dict(units=patched)
    return apply


def _dec(fn):
    def apply():
        def patched():
            rows = copy.deepcopy(_BASE_DEC)
            fn(rows)
            return rows
        return dict(decisions=patched)
    return apply


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


FIXTURES = [
    # ================= batch membership =================
    dict(fid="U-01", title="a fifth unit joins the batch", target="B",
         gates=["EXACTLY_FOUR_UNITS", "THE_FOUR_UNITS_ARE_THE_ONES_ASKED_FOR"],
         patch=lambda: dict(BATCH_UNITS=B.BATCH_UNITS + ["K5-PL06-T07-B01"])),
    dict(fid="U-02", title="a batch unit is swapped for a neighbour", target="B",
         gates=["THE_FOUR_UNITS_ARE_THE_ONES_ASKED_FOR"],
         patch=lambda: dict(BATCH_UNITS=["K5-PL06-T03-B03", "K5-PL06-T03-B05",
                                         "K5-PL06-T05-B01", "K5-PL06-T06-B01"])),
    dict(fid="U-03", title="one unit is carded twice", target="B",
         gates=["NO_UNIT_APPEARS_TWICE_IN_THE_MODEL"],
         patch=_units(lambda r: r.append(copy.deepcopy(r[0])))),
    dict(fid="U-04", title="a unit loses its card in the DOCX", target="B", rebuild=True,
         gates=["EVERY_UNIT_APPEARS_EXACTLY_ONCE_IN_THE_DOCX"],
         patch=_units(lambda r: r.remove(_find(r, "unit_id", "K5-PL06-T05-B01")))),
    dict(fid="U-05", title="a foreign unit is discussed without being named as allowed",
         target="B", rebuild=True,
         gates=["NO_UNIT_OUTSIDE_THE_BATCH_IS_MENTIONED_UNNAMED"],
         patch=_units(lambda r: r[0]["points"]["reuse"]["candidates"].append(
             "Reuse the K5-PL06-T02-B01 sequence wholesale"))),
    dict(fid="U-06", title="the section letters collapse onto one", target="B",
         gates=["EVERY_UNIT_HAS_ITS_OWN_SECTION_LETTER"],
         patch=lambda: dict(_SECTION_LETTER={u: "C" for u in B.BATCH_UNITS})),
    dict(fid="U-07", title="a section is dropped from A to H", target="B",
         gates=["EIGHT_SECTIONS_A_TO_H"],
         patch=lambda: dict(SECTIONS=[s for s in B.SECTIONS if s["letter"] != "G"])),

    # ================= boundaries =================
    dict(fid="BD-01", title="the frozen boundary map hash is loosened", target="B",
         gates=["THE_BOUNDARY_MAP_HASH_IS_PINNED_AND_VERIFIED"],
         patch=lambda: dict(BOUNDARY_MAP_SHA256="0" * 64)),
    dict(fid="BD-02", title="a unit loses its page range", target="B",
         gates=["EVERY_UNIT_CARRIES_ITS_FROZEN_PAGE_RANGE"],
         patch=_units(lambda r: r[0]["points"]["boundary"].update(module_page_range=""))),
    dict(fid="BD-03", title="a unit loses its stop anchor", target="B",
         gates=["EVERY_UNIT_CARRIES_ITS_NAMED_START_AND_STOP_ANCHOR"],
         patch=_units(lambda r: r[1]["points"]["boundary"].update(end_before=""))),
    dict(fid="BD-04", title="a paragraph span goes backwards", target="B",
         gates=["PARAGRAPH_SPANS_ARE_POSITIVE"],
         patch=_units(lambda r: r[2]["points"]["boundary"].update(paragraph_span=-3))),
    # The defect this suite actually found on its first run.
    dict(fid="BD-05", title="a shared boundary goes quiet", target="B",
         gates=["THE_TWO_SHARED_BOUNDARY_UNITS_ARE_NAMED",
                "SHARED_BOUNDARY_RISK_AGREES_WITH_THE_RAW_FROZEN_MAP"],
         patch=_units(lambda r: [x["points"]["shared_page_risk"].update(
             shared_start=False, shared_end=False) for x in r])),
    dict(fid="BD-06", title="one shared boundary of one unit goes quiet", target="B",
         gates=["SHARED_BOUNDARY_RISK_AGREES_WITH_THE_RAW_FROZEN_MAP"],
         patch=_units(lambda r: _find(r, "unit_id", "K5-PL06-T03-B04")
                      ["points"]["shared_page_risk"].update(shared_start=False))),
    dict(fid="BD-07", title="the flag reader reverts to the string-only comparison",
         target="B", gates=["THE_FLAG_READER_HANDLES_BOTH_MAP_PROJECTIONS"],
         patch=lambda: dict(flag=lambda v: v == "True")),
    dict(fid="BD-08", title="the split-by-anchor warning is softened away", target="B",
         gates=["EVERY_SHARED_BOUNDARY_UNIT_CARRIES_A_SPLIT_BY_ANCHOR_WARNING"],
         patch=_units(lambda r: [x["points"]["shared_page_risk"].update(
             risk="Minor formatting difference only.") for x in r])),
    dict(fid="BD-09", title="the shared page loses its cross-unit exception", target="B",
         gates=["THE_SHARED_PAGE_IS_NAMED_IN_A_CROSS_UNIT_EXCEPTION"],
         patch=lambda: dict(cross_unit_exceptions=lambda: [
             x for x in _BASE_XU if x["exception_id"] != "XU-02"])),
    dict(fid="BD-10", title="every boundary image is claimed as ingested", target="B",
         gates=["BOUNDARY_IMAGE_CUSTODY_IS_TYPED_PER_UNIT",
                "ONLY_THE_INGESTED_IMAGE_CARRIES_A_HASH"],
         patch=_units(lambda r: [x["points"]["boundary"].update(
             boundary_image_custody="INGESTED_IN_THIS_REPOSITORY") for x in r])),

    # ================= course rules =================
    dict(fid="R-01", title="an auto-applied rule is dropped", target="B",
         gates=["SIX_AUTO_APPLIED_RULES"],
         patch=lambda: dict(AUTO_APPLIED_RULES=B.AUTO_APPLIED_RULES[:5])),
    dict(fid="R-02", title="the quiz composition rule is removed", target="B",
         gates=["THE_QUIZ_COMPOSITION_RULE_IS_APPLIED", "SIX_AUTO_APPLIED_RULES"],
         patch=lambda: dict(AUTO_APPLIED_RULES=[r for r in B.AUTO_APPLIED_RULES
                                                if r["rule_id"] != "AR-01"])),
    dict(fid="R-03", title="the pass threshold is removed", target="B",
         gates=["THE_PASS_THRESHOLD_RULE_IS_APPLIED", "SIX_AUTO_APPLIED_RULES"],
         patch=lambda: dict(AUTO_APPLIED_RULES=[r for r in B.AUTO_APPLIED_RULES
                                                if r["rule_id"] != "AR-02"])),
    dict(fid="R-04", title="a unit quiz becomes five MCQ", target="B",
         gates=["EVERY_UNIT_QUIZ_IS_FOUR_MCQ_AND_ONE_MR"],
         patch=_units(lambda r: r[0]["points"]["quiz_stems"]["slots"][4].update(
             kind="MULTIPLE_CHOICE"))),
    dict(fid="R-05", title="a unit quiz loses an item", target="B",
         gates=["EVERY_UNIT_HAS_EXACTLY_FIVE_QUIZ_SLOTS"],
         patch=_units(lambda r: r[1]["points"]["quiz_stems"]["slots"].pop())),
    dict(fid="R-06", title="the VERIFY caveats are quietly dropped", target="B",
         gates=["THE_TWO_VERIFY_FLAGGED_RULES_KEEP_THEIR_CAVEAT"],
         patch=lambda: dict(AUTO_APPLIED_RULES=[dict(r, caveat="None.")
                                                for r in B.AUTO_APPLIED_RULES])),
    dict(fid="R-07", title="a banned learner phrase reaches a quiz stem", target="B",
         gates=["NO_BANNED_LEARNER_PHRASE_IS_PROPOSED_AS_LEARNER_TEXT",
                "NO_QUIZ_STEM_TEXT_IS_INVENTED"],
         patch=_units(lambda r: r[0]["points"]["quiz_stems"]["slots"][0].update(
             stem="Apakah yang dinyatakan dalam modul tentang infrastruktur?"))),
    dict(fid="R-08", title="a treatment outside the vocabulary is proposed", target="B",
         gates=["EVERY_PROPOSED_TREATMENT_IS_IN_THE_SUPPORTED_VOCABULARY"],
         patch=_units(lambda r: r[0]["points"]["treatment"].update(
             proposal="branching simulation"))),
    dict(fid="R-09", title="the treatment vocabulary is widened", target="B",
         gates=["FIVE_SUPPORTED_TREATMENTS_DECLARED"],
         patch=lambda: dict(SUPPORTED_TREATMENTS=B.SUPPORTED_TREATMENTS
                            + ["branching simulation"])),

    # ================= T04 generalisation =================
    dict(fid="G-01", title="a no-reuse item is dropped", target="B",
         gates=["SEVEN_NO_REUSE_ITEMS", "THE_NAMED_T04_NO_REUSE_ITEMS_ARE_ALL_PRESENT"],
         patch=lambda: dict(NO_REUSE=[n for n in B.NO_REUSE if n["item_id"] != "NR-02"])),
    dict(fid="G-02", title="T04's three-beat Rumusan is generalised", target="B",
         gates=["NO_UNIT_INHERITS_THE_T04_THREE_BEAT_RUMUSAN"],
         patch=_units(lambda r: [x["points"]["rumusan"].update(beat_count=3) for x in r])),
    dict(fid="G-03", title="a character pair is proposed for a unit dialogue", target="B",
         gates=["NO_UNIT_DIALOGUE_PROPOSAL_NAMES_A_CHARACTER"],
         patch=_units(lambda r: _find(r, "unit_id", "K5-PL06-T05-B01")
                      ["points"]["dialogue"].update(
                          reason="Alya and Encik Rahman open the quality scenario."))),
    dict(fid="G-04", title="a character name reaches a unit card in the DOCX", target="B",
         rebuild=True, gates=["NO_CHARACTER_NAME_APPEARS_INSIDE_A_UNIT_CARD"],
         patch=_units(lambda r: _find(r, "unit_id", "K5-PL06-T06-B01")
                      ["points"]["dialogue"].update(
                          reason="Haziq walks the site with the environmental officer."))),
    dict(fid="G-05", title="the character names vanish from the no-reuse record entirely",
         target="B", rebuild=True,
         gates=["THE_CHARACTER_NAMES_DO_APPEAR_WHERE_THEY_SHOULD"],
         patch=lambda: dict(NO_REUSE=[
             dict(n, item="the B02 cast", reason="B02-specific.",
                  what_is_portable="Nothing yet.") if n["item_id"] == "NR-02" else n
             for n in B.NO_REUSE])),
    dict(fid="G-06", title="T04's screen count is adopted", target="B",
         gates=["NO_UNIT_INHERITS_THE_T04_SCREEN_COUNT",
                "THE_SCREEN_FLOOR_EQUALS_ITS_OWN_TERMS"],
         patch=_units(lambda r: [x["points"]["screen_sequence"]["arithmetic"].update(
             minimum_total_screens=22) for x in r])),
    dict(fid="G-07", title="T04's 65 runtime states are adopted", target="B",
         gates=["NO_UNIT_INHERITS_THE_T04_RUNTIME_STATE_TOTAL"],
         patch=_units(lambda r: [x["points"]["runtime_states"].update(
             total_runtime_states=65) for x in r])),
    dict(fid="G-08", title="T04's visual totals are adopted", target="B",
         gates=["NO_UNIT_INHERITS_A_T04_VISUAL_TOTAL"],
         patch=_units(lambda r: [x["points"]["visual_obligations"].update(count=46)
                                 for x in r])),
    # Conflating obligations with assets, in the direction that looks harmless.
    dict(fid="G-09", title="visual obligations are recorded as zero rather than unknown",
         target="B",
         gates=["VISUAL_OBLIGATIONS_ARE_UNKNOWN_NOT_ZERO",
                "NO_UNIT_INHERITS_A_T04_VISUAL_TOTAL"],
         patch=_units(lambda r: [x["points"]["visual_obligations"].update(count=0)
                                 for x in r])),

    # ================= cards =================
    dict(fid="C-01", title="a card point is dropped from the schema", target="B",
         gates=["SIXTEEN_CARD_POINTS_DECLARED", "CARD_POINTS_ARE_NUMBERED_ONE_TO_SIXTEEN",
                "EVERY_UNIT_ANSWERS_ALL_SIXTEEN_POINTS"],
         patch=lambda: dict(CARD_POINTS=B.CARD_POINTS[:15])),
    dict(fid="C-02", title="a unit skips a card point", target="B",
         gates=["EVERY_UNIT_ANSWERS_ALL_SIXTEEN_POINTS"],
         patch=_units(lambda r: r[0]["points"].pop("visual_obligations"))),
    dict(fid="C-03", title="a point loses its provenance label", target="B",
         gates=["EVERY_POINT_CARRIES_A_DECLARED_PROVENANCE"],
         patch=_units(lambda r: r[1]["points"]["treatment"].pop("provenance"))),
    dict(fid="C-04", title="a provenance class is retired", target="B",
         gates=["FIVE_PROVENANCE_CLASSES_DECLARED", "EVERY_PROVENANCE_LABEL_APPEARS_IN_THE_DOCX"],
         patch=lambda: dict(PROVENANCE_CLASSES=[p for p in B.PROVENANCE_CLASSES
                                                if p["code"] != "OPEN"])),
    dict(fid="C-05", title="a screen group covers something no heading names", target="B",
         gates=["EVERY_PROPOSED_SCREEN_GROUP_MAPS_TO_A_NAMED_SUBTOPIC"],
         patch=_units(lambda r: r[0]["points"]["grouping"]["proposal"].append(
             dict(group_id="G9", covers="Penyelenggaraan berkala infrastruktur")))),
    dict(fid="C-06", title="a subtopic is invented into the mandatory list", target="B",
         gates=["EVERY_NAMED_SUBTOPIC_COMES_FROM_THE_FROZEN_MAP",
                "THE_CONTENT_FLOOR_EQUALS_THE_NAMED_SUBTOPIC_COUNT"],
         patch=_units(lambda r: r[0]["points"]["mandatory_content"]
                      ["named_subtopics"].append("3.5.1 Sistem Perparitan"))),
    dict(fid="C-07", title="a quiz slot binds to nothing in the unit", target="B",
         gates=["EVERY_QUIZ_SLOT_BINDS_TO_A_NAMED_SUBTOPIC"],
         patch=_units(lambda r: r[2]["points"]["quiz_stems"]["slots"][3].update(
             draws_from="5.9 Audit Kualiti Luaran"))),
    dict(fid="C-08", title="a learning outcome is written for an unextracted unit",
         target="B", gates=["NO_LEARNING_OUTCOME_IS_WRITTEN_FOR_AN_UNEXTRACTED_UNIT"],
         patch=_units(lambda r: r[3]["points"]["mandatory_content"].update(
             status="LEARNING_OUTCOMES_DRAFTED"))),
    dict(fid="C-09", title="quiz stems are written from the headings", target="B",
         gates=["NO_QUIZ_STEM_TEXT_IS_INVENTED"],
         patch=_units(lambda r: [s.update(stem="Apakah tujuan " + s["draws_from"] + "?")
                                 for s in r[2]["points"]["quiz_stems"]["slots"]])),
    dict(fid="C-10", title="a unit's rows are declared extracted", target="B",
         gates=["EVERY_UNIT_RECORDS_ITS_ROWS_AS_NOT_EXTRACTED"],
         patch=_units(lambda r: r[0]["points"]["controlled_rows"].update(
             status="EXTRACTED", row_count=94))),
    dict(fid="C-11", title="a blocked point stops naming its stop condition", target="B",
         gates=["EVERY_BLOCKED_POINT_NAMES_ITS_STOP_CONDITION"],
         patch=_units(lambda r: r[1]["points"]["answer_keys"].pop("blocking_stop"))),
    dict(fid="C-12", title="an answer key is given an authority", target="B",
         gates=["NO_ANSWER_KEY_CLAIMS_ANY_AUTHORITY"],
         patch=_units(lambda r: r[0]["points"]["answer_keys"].update(
             authority="BARIAH_APPROVED"))),
    dict(fid="C-13", title="answer keys are softened to pending approval", target="B",
         rebuild=True,
         gates=["ANSWER_KEYS_ARE_NOT_DRAFTED_NOT_MERELY_PENDING",
                "NO_STATUS_LINE_CLAIMS_AN_APPROVED_OR_PENDING_ANSWER_KEY",
                "THE_ANSWER_KEY_STATUS_LINES_SAY_NOT_DRAFTED"],
         patch=_units(lambda r: [x["points"]["answer_keys"].update(
             status="PENDING_APPROVAL") for x in r])),
    dict(fid="C-14", title="a maximum screen count is guessed", target="B",
         gates=["NO_UNIT_CLAIMS_A_MAXIMUM_SCREEN_COUNT"],
         patch=_units(lambda r: r[0]["points"]["screen_sequence"]["arithmetic"].update(
             maximum_total_screens=14))),
    dict(fid="C-15", title="the screen floor stops adding up", target="B",
         gates=["THE_SCREEN_FLOOR_EQUALS_ITS_OWN_TERMS",
                "THE_CARD_ARITHMETIC_AGREES_WITH_THE_LIVE_DERIVATION"],
         patch=_units(lambda r: r[1]["points"]["screen_sequence"]["arithmetic"].update(
             closing_screens=1))),
    dict(fid="C-16", title="the arithmetic is replaced by a bare number", target="B",
         gates=["EVERY_UNIT_EXPOSES_ITS_SCREEN_ARITHMETIC"],
         patch=_units(lambda r: r[0]["points"]["screen_sequence"].update(
             arithmetic=dict(minimum_total_screens=6)))),
    dict(fid="C-17", title="a second unit quietly acquires a dialogue screen", target="B",
         gates=["ONLY_THE_DIALOGUE_UNIT_CARRIES_A_THIRD_SHELL_SCREEN"],
         patch=lambda: dict(_UNIT_NOTES={
             k: (dict(v, dialogue_proposal="REQUIRED")
                 if k == "K5-PL06-T06-B01" else v)
             for k, v in B._UNIT_NOTES.items()})),
    dict(fid="C-18", title="a dialogue answer outside the three allowed values", target="B",
         gates=["EVERY_DIALOGUE_ANSWER_IS_FROM_THE_THREE_ALLOWED_VALUES"],
         patch=_units(lambda r: r[0]["points"]["dialogue"].update(proposal="MAYBE_LATER"))),

    # ================= decisions =================
    dict(fid="D-01", title="a decision is dropped", target="B",
         gates=["TWENTY_NINE_DECISIONS_REQUESTED", "DECISION_IDS_ARE_CONTIGUOUS_FROM_ONE"],
         patch=_dec(lambda r: r.pop())),
    dict(fid="D-02", title="one unit loses a decision", target="B",
         gates=["SIX_DECISIONS_PER_UNIT", "TWENTY_NINE_DECISIONS_REQUESTED"],
         patch=_dec(lambda r: r.remove(_find(r, "decision_id", "PL06-B1-D-03")))),
    dict(fid="D-03", title="a batch-level decision is removed", target="B",
         gates=["FIVE_BATCH_LEVEL_DECISIONS", "TWENTY_NINE_DECISIONS_REQUESTED"],
         patch=_dec(lambda r: r.remove(_find(r, "decision_id", "PL06-B1-D-29")))),
    dict(fid="D-04", title="two decisions share an ID", target="B",
         gates=["NO_DUPLICATE_DECISION_IDS"],
         patch=_dec(lambda r: r[5].update(decision_id=r[4]["decision_id"]))),
    dict(fid="D-05", title="a decision ID escapes the PL06-B1 namespace", target="B",
         gates=["NO_DECISION_ID_COLLIDES_WITH_A_T04_REGISTER",
                "DECISION_IDS_ARE_CONTIGUOUS_FROM_ONE"],
         patch=_dec(lambda r: r[0].update(decision_id="T04-DEC-E09"))),
    dict(fid="D-06", title="an undeclared response option appears", target="B",
         gates=["EVERY_DECISION_OFFERS_ONLY_DECLARED_RESPONSE_OPTIONS"],
         patch=_dec(lambda r: r[1]["options"].append("TANGGUH"))),
    dict(fid="D-07", title="a decision becomes open-ended", target="B",
         gates=["EVERY_DECISION_IS_BOUNDED_NOT_OPEN_ENDED"],
         patch=_dec(lambda r: r[2].update(options=["ESCALATE"]))),
    # GABUNG without a target is the specific defect the brief calls out.
    dict(fid="D-08", title="a GABUNG decision stops requiring a target ID", target="B",
         gates=["EVERY_GABUNG_DECISION_REQUIRES_A_TARGET_ID"],
         patch=_dec(lambda r: [x.update(requires_target_id=False) for x in r
                               if "GABUNG" in x["options"]])),
    dict(fid="D-09", title="a non-GABUNG decision demands a target ID", target="B",
         gates=["NO_NON_GABUNG_DECISION_DEMANDS_A_TARGET_ID"],
         patch=_dec(lambda r: _find(r, "decision_id", "PL06-B1-D-01").update(
             requires_target_id=True))),
    dict(fid="D-10", title="GABUNG is declared not to need a target", target="B",
         gates=["THE_GABUNG_OPTION_IS_DECLARED_TARGET_REQUIRING"],
         patch=lambda: dict(RESPONSE_OPTIONS=[dict(o, requires_target_id=False)
                                              for o in B.RESPONSE_OPTIONS])),
    # D-11 walked past the suite on the first run: the gate looked for
    # B.GABUNG_TARGET_FIELD, and blanking that constant made the needle the empty string,
    # which is in every line. The gate now uses a literal.
    dict(fid="D-11", title="the GABUNG target field never reaches the page", target="B",
         rebuild=True,
         gates=["EVERY_GABUNG_DECISION_PRINTS_A_TARGET_ID_FIELD_IN_THE_DOCX",
                "THE_TARGET_FIELD_LABEL_IS_THE_DECLARED_ONE"],
         patch=lambda: dict(GABUNG_TARGET_FIELD="")),
    dict(fid="D-12", title="a decision loses its response location", target="B",
         gates=["EVERY_DECISION_DECLARES_A_RESPONSE_LOCATION"],
         patch=_dec(lambda r: r[3].update(response_location="lihat kad"))),
    dict(fid="D-13", title="a decision loses its evidence reference", target="B",
         gates=["EVERY_DECISION_DECLARES_AN_EVIDENCE_LOCATION"],
         patch=_dec(lambda r: r[4].update(card_reference=""))),
    dict(fid="D-14", title="a decision exists in the model but never reaches the DOCX",
         target="E", rebuild=True,
         gates=["EVERY_DECISION_APPEARS_IN_THE_DOCX"],
         patch=lambda: dict(blocks=_blocks_without_decision("PL06-B1-D-20"))),
    dict(fid="D-15", title="the option field is dropped from the sheet", target="E",
         rebuild=True, gates=["EVERY_DECISION_HAS_AN_OPTION_FIELD_IN_THE_DOCX"],
         patch=lambda: dict(blocks=_blocks_without("Pilihan: "))),
    dict(fid="D-16", title="the free-note field is dropped from the sheet", target="E",
         rebuild=True, gates=["EVERY_DECISION_HAS_A_FREE_NOTE_FIELD_IN_THE_DOCX"],
         patch=lambda: dict(blocks=_blocks_without("Catatan: "))),
    dict(fid="D-17", title="the extraction authorisation is never asked", target="B",
         gates=["THE_EXTRACTION_AUTHORISATION_IS_ASKED",
                "TWENTY_NINE_DECISIONS_REQUESTED"],
         patch=_dec(lambda r: r.remove(_find(r, "point_key", "extraction")))),
    dict(fid="D-18", title="the merge question moves to a unit", target="B",
         gates=["THE_MERGE_QUESTION_IS_ASKED_ONCE_AT_BATCH_LEVEL"],
         patch=_dec(lambda r: _find(r, "point_key", "merge_t03").update(
             decision_id="PL06-B1-D-02"))),
    dict(fid="D-20", title="the language policy question is never asked", target="B",
         gates=["THE_LANGUAGE_POLICY_IS_DECLARED_AND_ASKED",
                "TWENTY_NINE_DECISIONS_REQUESTED"],
         patch=_dec(lambda r: r.remove(_find(r, "point_key", "language")))),
    dict(fid="D-21", title="the language policy silently flips to English throughout",
         target="B", gates=["THE_LANGUAGE_POLICY_IS_DECLARED_AND_ASKED"],
         patch=lambda: dict(LANGUAGE_POLICY=dict(B.LANGUAGE_POLICY,
                                                 decision_surface="ENGLISH"))),
    dict(fid="D-22", title="the Malay policy statement never reaches the page", target="B",
         rebuild=True, gates=["THE_LANGUAGE_POLICY_STATEMENT_REACHES_THE_DOCX_IN_MALAY",
                              "THE_LANGUAGE_POLICY_STATEMENT_IS_THE_DECLARED_ONE"],
         patch=lambda: dict(LANGUAGE_POLICY=dict(B.LANGUAGE_POLICY,
                                                 statement_ms="Dasar bahasa tidak dinyatakan."))),
    dict(fid="D-19", title="the cast question forgets its stop condition", target="B",
         gates=["THE_CAST_QUESTION_RESTATES_AN_EXISTING_STOP_CONDITION"],
         patch=_dec(lambda r: _find(r, "point_key", "cast").update(
             why="A fresh question about characters."))),

    # ================= projections =================
    dict(fid="P-01", title="a section heading never reaches the DOCX", target="E",
         rebuild=True, gates=["EVERY_SECTION_HEADING_REACHES_THE_DOCX"],
         patch=lambda: dict(blocks=_blocks_without_heading("G. Pengecualian"))),
    dict(fid="P-02", title="an auto-applied rule never reaches the DOCX", target="E",
         rebuild=True, gates=["EVERY_AUTO_APPLIED_RULE_TEXT_REACHES_THE_DOCX"],
         patch=lambda: dict(blocks=_blocks_without_rule("AR-04"))),
    # P-03 and P-04 walked past the suite on the first run: the gates compared the model
    # list against the document the same list had just generated, so a shortened list
    # matched a shortened document. They now designate the literal-ID gates.
    dict(fid="P-03", title="an exposure is dropped from the package", target="B",
         rebuild=True, gates=["THE_SEVEN_EXPOSURE_IDS_ARE_THE_DECLARED_SET",
                              "EVERY_EXPOSURE_ID_REACHES_THE_DOCX"],
         patch=lambda: dict(exposures=lambda: _BASE_EX[:-1])),
    dict(fid="P-04", title="a cross-unit exception is dropped", target="B", rebuild=True,
         gates=["THE_FIVE_CROSS_UNIT_EXCEPTION_IDS_ARE_THE_DECLARED_SET",
                "EVERY_CROSS_UNIT_EXCEPTION_ID_REACHES_THE_DOCX"],
         patch=lambda: dict(cross_unit_exceptions=lambda: _BASE_XU[:-1])),
    dict(fid="P-10", title="an exposure statement is rewritten after the DOCX is built",
         target="B", gates=["EVERY_EXPOSURE_STATEMENT_REACHES_THE_DOCX"],
         patch=lambda: dict(exposures=lambda: [
             dict(e, statement="Nothing of concern.") if e["exposure_id"] == "EX-03" else e
             for e in _BASE_EX])),
    dict(fid="P-11", title="a cross-unit exception statement is softened after the build",
         target="B", gates=["EVERY_CROSS_UNIT_EXCEPTION_STATEMENT_REACHES_THE_DOCX"],
         patch=lambda: dict(cross_unit_exceptions=lambda: [
             dict(x, statement="No action needed.") if x["exception_id"] == "XU-02" else x
             for x in _BASE_XU])),
    dict(fid="P-05", title="a start anchor never reaches the DOCX", target="B",
         rebuild=True, gates=["EVERY_START_ANCHOR_REACHES_THE_DOCX",
                              "EVERY_UNIT_CARRIES_ITS_NAMED_START_AND_STOP_ANCHOR"],
         patch=_units(lambda r: r[2]["points"]["boundary"].update(start_anchor=""))),
    dict(fid="P-06", title="a repository path is printed into the DOCX", target="B",
         rebuild=True, gates=["NO_REPOSITORY_PATH_IN_THE_DOCX"],
         patch=_units(lambda r: r[0]["points"]["controlled_rows"].update(
             note="See docs/pl06/tools for the extractor."))),
    dict(fid="P-07", title="the Markdown loses a decision the DOCX keeps", target="E",
         gates=["EVERY_DECISION_APPEARS_IN_THE_MARKDOWN_TOO"],
         patch=lambda: dict(MD_NAME="PL06_HARVEST_BATCH1_QA_REPORT_v1.md")),
    dict(fid="P-08", title="the Markdown stops naming its generator", target="B",
         gates=["THE_MARKDOWN_NAMES_ITS_GENERATOR"],
         patch=lambda: dict(GENERATED_BY="somewhere")),
    dict(fid="P-09", title="the preview is relabelled a Word render", target="D",
         gates=["THE_PREVIEW_IS_LABELLED_AN_APPROXIMATION"],
         patch=lambda: dict(PREVIEW_KIND="NATIVE_MICROSOFT_WORD_RENDER")),

    # ================= traceability =================
    dict(fid="T-01", title="a trace row loses its evidence", target="E",
         gates=["EVERY_TRACE_ROW_NAMES_ITS_EVIDENCE"],
         patch=lambda: dict(traceability=lambda: dict(
             _BASE_TRACE, rows=[dict(r, evidence="") if i == 0 else r
                                for i, r in enumerate(_BASE_TRACE["rows"])]))),
    dict(fid="T-02", title="a trace row gets an untyped evidence class", target="E",
         gates=["EVERY_TRACE_ROW_IS_TYPED"],
         patch=lambda: dict(traceability=lambda: dict(
             _BASE_TRACE, rows=[dict(r, evidence_class="PROBABLY_FINE") if i == 1 else r
                                for i, r in enumerate(_BASE_TRACE["rows"])]))),
    dict(fid="T-03", title="a unit loses all its trace rows", target="E",
         gates=["EVERY_UNIT_HAS_TRACE_ROWS"],
         patch=lambda: dict(traceability=lambda: dict(
             _BASE_TRACE, rows=[r for r in _BASE_TRACE["rows"]
                                if r["unit_id"] != "K5-PL06-T06-B01"]))),
    dict(fid="T-04", title="a frozen row carries the wrong map hash", target="E",
         gates=["EVERY_FROZEN_ROW_CARRIES_THE_PINNED_MAP_HASH"],
         patch=lambda: dict(traceability=lambda: dict(
             _BASE_TRACE, rows=[dict(r, evidence_sha256="f" * 64)
                                if r["evidence_class"] == "FROZEN_HASH_VERIFIED" else r
                                for r in _BASE_TRACE["rows"]]))),
    # The blocked claims are the ones a tidy-looking package would silently drop.
    dict(fid="T-05", title="the blocked claims are dropped from traceability", target="E",
         gates=["THE_BLOCKED_CLAIMS_ARE_NOT_SILENTLY_DROPPED"],
         patch=lambda: dict(traceability=lambda: dict(
             _BASE_TRACE,
             rows=[r for r in _BASE_TRACE["rows"]
                   if r["evidence_class"] != "BLOCKED_NOT_EXTRACTED"],
             totals=dict(_BASE_TRACE["totals"], blocked_not_extracted=0)))),
    dict(fid="T-06", title="the module DOCX is claimed to be in the repository",
         target="B", gates=["THE_MODULE_DOCX_IS_RECORDED_AS_EXTERNAL"],
         patch=lambda: dict(MODULE_DOCX_IN_THIS_REPOSITORY=True)),
    dict(fid="T-07", title="the module DOCX hash is retyped", target="B",
         gates=["THE_MODULE_DOCX_HASH_IS_CARRIED_NOT_INVENTED"],
         patch=lambda: dict(MODULE_DOCX_SHA256="a" * 64)),

    # ================= guards =================
    dict(fid="X-01", title="a forbidden status claim is retired", target="B",
         gates=["FOUR_FORBIDDEN_STATUS_CLAIMS_DECLARED"],
         patch=lambda: dict(FORBIDDEN_STATUS_CLAIMS=B.FORBIDDEN_STATUS_CLAIMS[:3])),
    dict(fid="X-02", title="the batch declares itself approved", target="B",
         gates=["THE_BATCH_STATUS_IS_AWAITING_NOT_APPROVED"],
         patch=lambda: dict(BATCH_STATUS="BATCH_APPROVED")),
    dict(fid="X-03", title="a forbidden claim is printed into the DOCX", target="B",
         rebuild=True, gates=["NO_FORBIDDEN_CLAIM_APPEARS_IN_THE_DOCX"],
         patch=_units(lambda r: r[0]["points"]["controlled_rows"].update(
             note="CONTENT_EXTRACTED for this unit."))),
    dict(fid="X-04", title="an MMD artifact is declared", target="E",
         gates=["NO_MMD_REACT_SCORM_OR_LMS_ARTIFACT"],
         patch=lambda: dict(ARTIFACTS=E.ARTIFACTS + ["PL06_BATCH1_MMD_ASSETS_v1.json"])),
    dict(fid="X-05", title="CAIR is named Instructional Designer in the DOCX", target="B",
         rebuild=True, gates=["CAIR_IS_NOT_NAMED_INSTRUCTIONAL_DESIGNER"],
         patch=_units(lambda r: r[0]["points"]["grouping"].update(
             note="CAIR is the Instructional Designer for this grouping."))),
    dict(fid="X-06", title="a blocking stop is dropped from the reference list", target="B",
         gates=["THE_FOUR_BLOCKING_STOPS_ARE_REFERENCED_NOT_REMINTED"],
         patch=lambda: dict(BLOCKING_STOPS=B.BLOCKING_STOPS[:3])),
    dict(fid="X-07", title="the stale register divergence is quietly forgotten", target="B",
         gates=["THE_STALE_T04_ENTRY_ON_THE_REGISTER_IS_RECORDED_NOT_REWRITTEN"],
         patch=lambda: dict(cross_unit_exceptions=lambda: [
             x for x in _BASE_XU if x["exception_id"] != "XU-05"])),
    dict(fid="X-08", title="a declared artifact is never written", target="E",
         gates=["EVERY_DECLARED_ARTIFACT_EXISTS"],
         patch=lambda: dict(ARTIFACTS=E.ARTIFACTS + ["PL06_HARVEST_BATCH1_GHOST_v1.md"])),

    # ================= accounting =================
    dict(fid="A-01", title="the suite loses its identity", target="QA",
         gates=["SUITE_ID_DECLARED"], patch=lambda: dict(SUITE_ID="")),
    dict(fid="A-02", title="the suite adopts the Lane A identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE"],
         patch=lambda: dict(SUITE_ID="T04_STATE_COVERAGE_QA_v1")),
    dict(fid="A-03", title="the NOT_CHECKED list is emptied", target="QA",
         gates=["NOT_CHECKED_IS_PUBLISHED"], patch=lambda: dict(NOT_CHECKED=[])),
]


def _blocks_without(prefix):
    def patched():
        return [b for b in _BASE_BLOCKS
                if not (b["kind"] == "field" and b["text"].startswith(prefix))]
    return patched


def _blocks_without_heading(prefix):
    def patched():
        return [b for b in _BASE_BLOCKS
                if not (b["kind"] == "heading" and b["text"].startswith(prefix))]
    return patched


def _blocks_without_rule(rule_id):
    rule = next(r["rule"] for r in B.AUTO_APPLIED_RULES if r["rule_id"] == rule_id)

    def patched():
        out = []
        for b in _BASE_BLOCKS:
            if b["kind"] == "table":
                out.append(dict(b, rows=[r for r in b["rows"] if rule not in r]))
            else:
                out.append(b)
        return out
    return patched


def _blocks_without_decision(decision_id):
    """Drop one decision's heading and its two response fields from the printed sheet.

    The model still lists the decision, so this is the model-versus-artifact divergence
    EVERY_DECISION_APPEARS_IN_THE_DOCX exists to catch.
    """
    def patched():
        out, skip = [], 0
        for b in _BASE_BLOCKS:
            if skip:
                skip -= 1
                continue
            if b.get("text", "").startswith(decision_id + " ·"):
                skip = 3          # provenance line + two field lines
                continue
            out.append(b)
        return out
    return patched


_BASE_BLOCKS = _BASE_EX = _BASE_XU = None


def _docx_digest():
    import zipfile
    import xml.etree.ElementTree as ET
    z = zipfile.ZipFile(QA.DOCX_PATH)
    root = ET.fromstring(z.read("word/document.xml"))
    txt = "\n".join("".join(t.text or "" for t in p.iter(f"{{{QA.W_NS}}}t"))
                    for p in root.iter(f"{{{QA.W_NS}}}p"))
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()


def _run_suite():
    return {r["gate_id"]: r["ok"] for r in QA.run()}


def run_fixture(f):
    tgt = TARGETS[f.get("target", "B")]
    patch = dict(f["patch"]())
    saved = {k: getattr(tgt, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(tgt, k, v)
        if f.get("rebuild"):
            E.emit_all()
        return _run_suite()
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)
        if f.get("rebuild"):
            E.emit_all()


def main():
    global _BASE_UNITS, _BASE_DEC, _BASE_TRACE, _BASE_BLOCKS, _BASE_EX, _BASE_XU
    _BASE_UNITS = B.units()
    _BASE_DEC = B.decisions()
    _BASE_TRACE = E.traceability()
    _BASE_BLOCKS = E.blocks()
    _BASE_EX = B.exposures()
    _BASE_XU = B.cross_unit_exceptions()
    before = _docx_digest()
    good = _run_suite()
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"],
                        target=f.get("target", "B"),
                        rebuilds_docx=bool(f.get("rebuild")),
                        designated_gates=f["gates"], detected=det, fired=fired,
                        note=res.get("__MSG__")))
    after = _docx_digest()
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v),
                baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out),
                detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                docx_rebuilt_clean=(before == after),
                rebuild_fixtures=len([r for r in out if r["rebuilds_docx"]]),
                by_target={t: sum(1 for r in out if r["target"] == t)
                           for t in sorted({r["target"] for r in out})},
                fixtures=out)


def emit_report(r):
    md = ["<!-- GENERATED by docs/pl06/tools/pl06_batch1_mutations_v1.py -->", "",
          "# PL06 harvest batch 1 — mutation report", "", "```",
          f"SUITE_ID            = {r['suite_id']}",
          f"FIXTURES            = {r['fixture_count']}",
          f"DETECTED            = {r['detected']}",
          f"MISSED              = {len(r['missed'])}",
          f"BASELINE            = {r['baseline_pass']}/{r['baseline_total']}",
          f"DOCX_REBUILT_CLEAN  = {str(r['docx_rebuilt_clean']).lower()}",
          f"REBUILD_FIXTURES    = {r['rebuild_fixtures']}", "```", "",
          "Each fixture breaks the package in one specific way and names the gates that must "
          "fire. A fixture that walks past its gates is a hole in the suite, not a pass.", "",
          "| fixture | what it breaks | rebuilds DOCX | gates that fired |",
          "|---|---|---|---|"]
    md += [f"| `{f['fixture_id']}` | {f['title']} | "
           f"{'yes' if f['rebuilds_docx'] else 'no'} | "
           f"{', '.join('`' + g + '`' for g in f['fired']) or '**NONE — MISSED**'} |"
           for f in r["fixtures"]]
    md += [""]
    path = os.path.join(B.PL06, "PL06_HARVEST_BATCH1_MUTATION_REPORT_v1.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return path


if __name__ == "__main__":
    r = main()
    print(json.dumps({k: v for k, v in r.items() if k != "fixtures"},
                     ensure_ascii=False, indent=1))
    for f in r["fixtures"]:
        if not f["detected"]:
            print("MISS", f["fixture_id"], "|", f["title"], "|", f["designated_gates"],
                  "|", f["note"])
    print("report   :", emit_report(r))
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]
                   or not r["docx_rebuilt_clean"]) else 0)
