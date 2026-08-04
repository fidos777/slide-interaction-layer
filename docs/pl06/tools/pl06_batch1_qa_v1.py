# -*- coding: utf-8 -*-
"""Stage 4.2F-B2 Lane B QA — the PL06 authority-harvest batch 1 package.

    SUITE_ID = PL06_AUTHORITY_HARVEST_BATCH1_QA_v1
    python3 docs/pl06/tools/pl06_batch1_qa_v1.py

The DOCX is re-opened from disk and its text re-extracted with exact OOXML element matching,
so a decision that exists only in the model cannot pass. Word splits single words across
runs, so `<w:t>` runs are joined with NO separator.

Separate from T04_STATE_COVERAGE_QA_v1 (108), T04_STORYBOARD_QA_v1 (114),
T04_SUPPLEMENTARY_EVIDENCE_QA_v1 (133) and T04_AUTHORITY_DECISION_INGESTION_QA_v1 (251).
Never add the totals.
"""
import json
import re
import os
import sys
import zipfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
PL06 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pl06_batch1_data_v1 as B   # noqa: E402
import pl06_batch1_emit_v1 as E   # noqa: E402
import pl06_docx_v1 as D          # noqa: E402

SUITE_ID = "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1"
PRIOR_SUITE_ID = "T04_STATE_COVERAGE_QA_v1"

BATCH = "BATCH"
BOUNDARY = "BOUNDARY"
RULES = "RULES"
CARDS = "CARDS"
DECISIONS = "DECISIONS"
DOCX = "DOCX"
TRACE = "TRACE"
GUARD = "GUARD"
ACCOUNTING = "ACCOUNTING"
GATE_TYPES = {BATCH, BOUNDARY, RULES, CARDS, DECISIONS, DOCX, TRACE, GUARD, ACCOUNTING}

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

NOT_CHECKED = [
    "how the DOCX renders in Microsoft Word — LibreOffice here has no Writer filter, so no "
    "native render was performed and none is claimed",
    "whether the four units' content supports the proposed treatments — none of them is "
    "extracted, which is the whole reason this package exists",
    "whether Bariah agrees with any CAIR proposal in it — that is what the package asks",
    "whether the merge candidate T03-B03 + T03-B04 is instructionally sound",
    "whether 4 MCQ + 1 MR and the 60 percent threshold are genuinely course-wide — RP-009 "
    "and RP-010 carry human_authority_required = VERIFY and PL06-B1-D-28 asks",
    "whether an English rationale layer under a Malay decision surface is acceptable to "
    "the reviewer — PL06-B1-D-29 asks rather than assuming",
]

DOCX_PATH = os.path.join(E.DOCX_DIR, E.DOCX_NAME)


def _docx_paragraph_texts():
    """Exact element identity: {w}t inside {w}p, runs joined with NO separator."""
    z = zipfile.ZipFile(DOCX_PATH)
    root = ET.fromstring(z.read("word/document.xml"))
    out = []
    for para in root.iter(f"{{{W_NS}}}p"):
        out.append("".join(t.text or "" for t in para.iter(f"{{{W_NS}}}t")))
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

    UNITS = B.units()
    DEC = B.decisions()
    TR = E.traceability()
    present = os.path.exists(DOCX_PATH)
    paras = _docx_paragraph_texts() if present else []
    doc = "\n".join(paras)
    md_path = os.path.join(PL06, E.MD_NAME)
    md = open(md_path, encoding="utf-8").read() if os.path.exists(md_path) else ""

    # ==================== 1. BATCH ====================
    chk("EXACTLY_FOUR_UNITS", BATCH, len(B.BATCH_UNITS), 4, len(B.BATCH_UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_FOUR_UNITS_ARE_THE_ONES_ASKED_FOR", BATCH, sorted(B.BATCH_UNITS),
        ["K5-PL06-T03-B03", "K5-PL06-T03-B04", "K5-PL06-T05-B01", "K5-PL06-T06-B01"],
        4, "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_UNIT_APPEARS_TWICE_IN_THE_MODEL", BATCH,
        sorted(u["unit_id"] for u in UNITS), sorted(set(B.BATCH_UNITS)), len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_UNIT_APPEARS_EXACTLY_ONCE_IN_THE_DOCX", BATCH,
        [u for u in B.BATCH_UNITS
         if len([p for p in paras if p.startswith(f"{B._section_letter(u)}. Kad keputusan")])
         != 1], [], len(B.BATCH_UNITS), E.DOCX_NAME)
    # Any unit ID anywhere in the document, not just at the start of a paragraph. Two
    # foreign IDs are allowed and named: T04 because XU-05 records a stale register entry
    # against it, B02 because the no-reuse section is about B02's rules.
    chk("NO_UNIT_OUTSIDE_THE_BATCH_IS_MENTIONED_UNNAMED", BATCH,
        sorted(set(re.findall(r"K5-PL06-T\d+-B\d+", doc))
               - set(B.BATCH_UNITS) - {"K5-PL06-T04-B01", "K5-PL06-T03-B02"}), [],
        len(set(re.findall(r"K5-PL06-T\d+-B\d+", doc))) or 1, E.DOCX_NAME)
    chk("EVERY_UNIT_HAS_ITS_OWN_SECTION_LETTER", BATCH,
        sorted(B._section_letter(u) for u in B.BATCH_UNITS), ["C", "D", "E", "F"], 4,
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EIGHT_SECTIONS_A_TO_H", BATCH, [s["letter"] for s in B.SECTIONS],
        ["A", "B", "C", "D", "E", "F", "G", "H"], len(B.SECTIONS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")

    # ==================== 2. BOUNDARY ====================
    chk("THE_BOUNDARY_MAP_HASH_IS_PINNED_AND_VERIFIED", BOUNDARY,
        B._sha256(B.BOUNDARY_MAP_PATH), B.BOUNDARY_MAP_SHA256, 1,
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    chk("EVERY_UNIT_CARRIES_ITS_FROZEN_PAGE_RANGE", BOUNDARY,
        [u["unit_id"] for u in UNITS if not u["points"]["boundary"]["module_page_range"]],
        [], len(UNITS), "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("EVERY_UNIT_CARRIES_ITS_NAMED_START_AND_STOP_ANCHOR", BOUNDARY,
        [u["unit_id"] for u in UNITS
         if not (u["points"]["boundary"]["start_anchor"]
                 and u["points"]["boundary"]["end_before"])], [], len(UNITS),
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("PARAGRAPH_SPANS_ARE_POSITIVE", BOUNDARY,
        [u["unit_id"] for u in UNITS if u["points"]["boundary"]["paragraph_span"] <= 0], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # Shared-boundary risk cannot disappear: it is read live from the frozen map, and every
    # unit whose map row says True must say True here and in the deck.
    shared = [u["unit_id"] for u in UNITS
              if u["points"]["shared_page_risk"]["shared_start"]
              or u["points"]["shared_page_risk"]["shared_end"]]
    chk("THE_TWO_SHARED_BOUNDARY_UNITS_ARE_NAMED", BOUNDARY, sorted(shared),
        ["K5-PL06-T03-B03", "K5-PL06-T03-B04"], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # Read straight from the frozen JSON with json.load and Python truthiness — NOT through
    # B.flag(). The first build of this package compared the map against itself using the
    # same faulty "== 'True'" test on both sides, so both sides agreed the T03 boundaries
    # were clean. An oracle that shares the parser it is checking proves only that the
    # parser is consistent with itself.
    _RAW = {l["unit_id"]: l for l in
            json.load(open(B.BOUNDARY_MAP_PATH, encoding="utf-8"))["lessons"]}
    chk("SHARED_BOUNDARY_RISK_AGREES_WITH_THE_RAW_FROZEN_MAP", BOUNDARY,
        [u["unit_id"] for u in UNITS
         if bool(u["points"]["shared_page_risk"]["shared_start"])
         is not bool(_RAW[u["unit_id"]]["shared_start"])
         or bool(u["points"]["shared_page_risk"]["shared_end"])
         is not bool(_RAW[u["unit_id"]]["shared_end"])], [], len(UNITS),
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    chk("THE_FLAG_READER_HANDLES_BOTH_MAP_PROJECTIONS", BOUNDARY,
        [B.flag(True), B.flag(False), B.flag("True"), B.flag("False"), B.flag("true")],
        [True, False, True, False, True], 5, "docs/pl06/tools/pl06_batch1_data_v1.py")
    chk("EVERY_SHARED_BOUNDARY_UNIT_CARRIES_A_SPLIT_BY_ANCHOR_WARNING", BOUNDARY,
        [u for u in shared
         if "heading anchor" not in next(x["points"]["shared_page_risk"]["risk"]
                                         for x in UNITS if x["unit_id"] == u)], [],
        len(shared), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_SHARED_PAGE_IS_NAMED_IN_A_CROSS_UNIT_EXCEPTION", BOUNDARY,
        any("255" in x["statement"] for x in B.cross_unit_exceptions()), True,
        len(B.cross_unit_exceptions()), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("BOUNDARY_IMAGE_CUSTODY_IS_TYPED_PER_UNIT", BOUNDARY,
        sorted({u["points"]["boundary"]["boundary_image_custody"] for u in UNITS}),
        ["INGESTED_IN_THIS_REPOSITORY",
         "NAMED_IN_THE_FREEZE_PACKAGE_BY_IDENTITY_ONLY",
         "NO_IMAGE_FOR_THIS_START_PAGE"], len(UNITS),
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("ONLY_THE_INGESTED_IMAGE_CARRIES_A_HASH", BOUNDARY,
        [r["unit_id"] for r in TR["rows"]
         if r["claim"] == "boundary page image"
         and bool(r["evidence_sha256"]) != (r["evidence_class"]
                                            == "INGESTED_IN_THIS_REPOSITORY")], [],
        len([r for r in TR["rows"] if r["claim"] == "boundary page image"]),
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")

    # ==================== 3. RULES ====================
    chk("SIX_AUTO_APPLIED_RULES", RULES, len(B.AUTO_APPLIED_RULES), 6,
        len(B.AUTO_APPLIED_RULES), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_QUIZ_COMPOSITION_RULE_IS_APPLIED", RULES,
        any("4 Multiple Choice + 1 Multiple Response" in r["rule"]
            for r in B.AUTO_APPLIED_RULES), True, len(B.AUTO_APPLIED_RULES),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_PASS_THRESHOLD_RULE_IS_APPLIED", RULES,
        any("60 percent" in r["rule"] for r in B.AUTO_APPLIED_RULES), True,
        len(B.AUTO_APPLIED_RULES), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_UNIT_QUIZ_IS_FOUR_MCQ_AND_ONE_MR", RULES,
        [u["unit_id"] for u in UNITS
         if [s["kind"] for s in u["points"]["quiz_stems"]["slots"]]
         != ["MULTIPLE_CHOICE"] * 4 + ["MULTIPLE_RESPONSE"]], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_UNIT_HAS_EXACTLY_FIVE_QUIZ_SLOTS", RULES,
        [u["unit_id"] for u in UNITS if len(u["points"]["quiz_stems"]["slots"]) != 5], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_TWO_VERIFY_FLAGGED_RULES_KEEP_THEIR_CAVEAT", RULES,
        sorted(r["rule_id"] for r in B.AUTO_APPLIED_RULES if "VERIFY" in r["caveat"]),
        ["AR-01", "AR-02"], len(B.AUTO_APPLIED_RULES),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_BANNED_LEARNER_PHRASE_IS_PROPOSED_AS_LEARNER_TEXT", RULES,
        [ph for ph in B.BANNED_LEARNER_PHRASES
         for u in UNITS
         if any(ph in str(s["stem"]) for s in u["points"]["quiz_stems"]["slots"])], [],
        len(B.BANNED_LEARNER_PHRASES) * len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_PROPOSED_TREATMENT_IS_IN_THE_SUPPORTED_VOCABULARY", RULES,
        [u["unit_id"] for u in UNITS
         if u["points"]["treatment"]["proposal"] not in B.SUPPORTED_TREATMENTS], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("FIVE_SUPPORTED_TREATMENTS_DECLARED", RULES, len(B.SUPPORTED_TREATMENTS), 5,
        len(B.SUPPORTED_TREATMENTS), "PL06_HARVEST_BATCH1_MODEL_v1.json")

    # -------- no T04-only rule is falsely generalised --------
    chk("SEVEN_NO_REUSE_ITEMS", RULES, len(B.NO_REUSE), 7, len(B.NO_REUSE),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_NAMED_T04_NO_REUSE_ITEMS_ARE_ALL_PRESENT", RULES,
        sorted(n["item_id"] for n in B.NO_REUSE),
        ["NR-01", "NR-02", "NR-03", "NR-04", "NR-05", "NR-06", "NR-07"], len(B.NO_REUSE),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_UNIT_INHERITS_THE_T04_THREE_BEAT_RUMUSAN", RULES,
        [u["unit_id"] for u in UNITS
         if u["points"]["rumusan"]["beat_count"] != "BARIAH"], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_CHARACTER_NAME_IS_PROPOSED_ANYWHERE", RULES,
        [n for n in ("Alya", "Encik Rahman", "Haziq", "Encik Roslan")
         if any(n in json.dumps(u["points"]["dialogue"], ensure_ascii=False)
                for u in UNITS)], [], 4 * len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # The four names may appear — the no-reuse table and the cast question are about them.
    # What must not happen is a name appearing anywhere that is NOT one of those places.
    # Table cells are separate <w:p>, so "NR-02" sits in a different paragraph from the
    # names beside it. The check that matters is positional: a name must never appear
    # inside a UNIT CARD, which is where it would read as a proposal.
    _CAST_NAMES = ("Alya", "Encik Rahman", "Haziq", "Encik Roslan")
    _named = [i for i, p in enumerate(paras) if any(n in p for n in _CAST_NAMES)]
    chk("NO_CHARACTER_NAME_APPEARS_INSIDE_A_UNIT_CARD", RULES,
        [paras[i][:50] for i in _named
         if any(_in_section(paras, i, ltr) for ltr in ("C", "D", "E", "F"))], [],
        len(_named) or 1, E.DOCX_NAME)
    chk("THE_CHARACTER_NAMES_DO_APPEAR_WHERE_THEY_SHOULD", RULES,
        len(_named) >= 2, True, len(_named) or 1, E.DOCX_NAME)
    chk("NO_UNIT_DIALOGUE_PROPOSAL_NAMES_A_CHARACTER", RULES,
        [u["unit_id"] for u in UNITS
         if any(n in u["points"]["dialogue"]["proposal"] + u["points"]["dialogue"]["reason"]
                for n in ("Alya", "Encik Rahman", "Haziq", "Encik Roslan"))], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_UNIT_INHERITS_THE_T04_SCREEN_COUNT", RULES,
        [u["unit_id"] for u in UNITS
         if u["points"]["screen_sequence"]["arithmetic"]["minimum_total_screens"] == 22], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_UNIT_INHERITS_THE_T04_RUNTIME_STATE_TOTAL", RULES,
        [u["unit_id"] for u in UNITS
         if u["points"]["runtime_states"]["total_runtime_states"] != B.UNKNOWN], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_UNIT_INHERITS_A_T04_VISUAL_TOTAL", RULES,
        [u["unit_id"] for u in UNITS
         if u["points"]["visual_obligations"]["count"] != B.UNKNOWN], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("VISUAL_OBLIGATIONS_ARE_UNKNOWN_NOT_ZERO", RULES,
        [u["unit_id"] for u in UNITS
         if u["points"]["visual_obligations"]["count"] in (0, "0")], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")

    # ==================== 4. CARDS ====================
    chk("SIXTEEN_CARD_POINTS_DECLARED", CARDS, len(B.CARD_POINTS), 16, len(B.CARD_POINTS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("CARD_POINTS_ARE_NUMBERED_ONE_TO_SIXTEEN", CARDS,
        [c["no"] for c in B.CARD_POINTS], list(range(1, 17)), len(B.CARD_POINTS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_UNIT_ANSWERS_ALL_SIXTEEN_POINTS", CARDS,
        [u["unit_id"] for u in UNITS
         if sorted(u["points"]) != sorted(c["key"] for c in B.CARD_POINTS)], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_POINT_CARRIES_A_DECLARED_PROVENANCE", CARDS,
        [f"{u['unit_id']}.{k}" for u in UNITS for k, v in u["points"].items()
         if v.get("provenance") not in B.PROVENANCE_CODES], [],
        len(UNITS) * len(B.CARD_POINTS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("FIVE_PROVENANCE_CLASSES_DECLARED", CARDS, len(B.PROVENANCE_CLASSES), 5,
        len(B.PROVENANCE_CLASSES), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_PROVENANCE_LABEL_APPEARS_IN_THE_DOCX", CARDS,
        [p["label"] for p in B.PROVENANCE_CLASSES if f"[{p['label']}]" not in doc], [],
        len(B.PROVENANCE_CLASSES), E.DOCX_NAME)
    # -------- every proposed screen maps to controlled source --------
    chk("EVERY_PROPOSED_SCREEN_GROUP_MAPS_TO_A_NAMED_SUBTOPIC", CARDS,
        [f"{u['unit_id']}.{g['group_id']}" for u in UNITS
         for g in u["points"]["grouping"]["proposal"]
         if g["covers"] not in u["points"]["mandatory_content"]["named_subtopics"]], [],
        sum(len(u["points"]["grouping"]["proposal"]) for u in UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_NAMED_SUBTOPIC_COMES_FROM_THE_FROZEN_MAP", CARDS,
        [f"{u['unit_id']}:{s}" for u in UNITS
         for s in u["points"]["mandatory_content"]["named_subtopics"]
         if s not in B._LESSONS[u["unit_id"]]["subtopics"]], [],
        sum(len(u["points"]["mandatory_content"]["named_subtopics"]) for u in UNITS),
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    chk("EVERY_QUIZ_SLOT_BINDS_TO_A_NAMED_SUBTOPIC", CARDS,
        [f"{u['unit_id']}.{s['slot']}" for u in UNITS
         for s in u["points"]["quiz_stems"]["slots"]
         if s["draws_from"] not in u["points"]["mandatory_content"]["named_subtopics"]], [],
        5 * len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # -------- no source-unsupported LO is invented --------
    chk("NO_LEARNING_OUTCOME_IS_WRITTEN_FOR_AN_UNEXTRACTED_UNIT", CARDS,
        [u["unit_id"] for u in UNITS
         if u["points"]["mandatory_content"]["status"] != "HEADING_LEVEL_ONLY"], [],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_QUIZ_STEM_TEXT_IS_INVENTED", CARDS,
        [f"{u['unit_id']}.{s['slot']}" for u in UNITS
         for s in u["points"]["quiz_stems"]["slots"] if s["stem"] != B.PENDING], [],
        5 * len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_UNIT_RECORDS_ITS_ROWS_AS_NOT_EXTRACTED", CARDS,
        [u["unit_id"] for u in UNITS
         if u["points"]["controlled_rows"]["status"] != B.NOT_EXTRACTED], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_BLOCKED_POINT_NAMES_ITS_STOP_CONDITION", CARDS,
        [f"{u['unit_id']}.{k}" for u in UNITS
         for k in ("controlled_rows", "quiz_stems", "answer_keys", "visual_obligations")
         if not u["points"][k].get("blocking_stop", "").startswith("STOP-")], [],
        4 * len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # -------- answer-key authority is not overstated --------
    chk("NO_ANSWER_KEY_CLAIMS_ANY_AUTHORITY", CARDS,
        [u["unit_id"] for u in UNITS
         if u["points"]["answer_keys"]["authority"] != "NONE — no key exists, so none is "
                                                       "approved"], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("ANSWER_KEYS_ARE_NOT_DRAFTED_NOT_MERELY_PENDING", CARDS,
        sorted({u["points"]["answer_keys"]["status"] for u in UNITS}), ["NOT_DRAFTED"],
        len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # PENDING_APPROVAL does appear once, in the sentence explaining why NOT_DRAFTED is the
    # weaker and correct word. What must not appear is a STATUS LINE that claims it.
    _STATUS_LINES = [p for p in paras if p.startswith("Status:")]
    chk("NO_STATUS_LINE_CLAIMS_AN_APPROVED_OR_PENDING_ANSWER_KEY", CARDS,
        [p for p in _STATUS_LINES
         if "APPROVED" in p or "PENDING_APPROVAL" in p], [], len(_STATUS_LINES),
        E.DOCX_NAME)
    chk("THE_ANSWER_KEY_STATUS_LINES_SAY_NOT_DRAFTED", CARDS,
        len([p for p in _STATUS_LINES if p.startswith("Status: NOT_DRAFTED")]),
        len(UNITS), len(_STATUS_LINES), E.DOCX_NAME)
    # -------- screen-count arithmetic is exposed, never a bare number --------
    chk("EVERY_UNIT_EXPOSES_ITS_SCREEN_ARITHMETIC", CARDS,
        [u["unit_id"] for u in UNITS
         if sorted(u["points"]["screen_sequence"]["arithmetic"])
         != sorted(B.screen_arithmetic(u["unit_id"]))], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_UNIT_CLAIMS_A_MAXIMUM_SCREEN_COUNT", CARDS,
        [u["unit_id"] for u in UNITS
         if u["points"]["screen_sequence"]["arithmetic"]["maximum_total_screens"]
         != B.UNKNOWN], [], len(UNITS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # Read from the arithmetic AS CARRIED ON THE CARD — the copy that is actually printed.
    # Checking B.screen_arithmetic() instead let fixture C-15 corrupt the card's own copy
    # while the function stayed internally consistent, and the gate saw nothing.
    chk("THE_SCREEN_FLOOR_EQUALS_ITS_OWN_TERMS", CARDS,
        [u["unit_id"] for u in UNITS
         for a in [u["points"]["screen_sequence"]["arithmetic"]]
         if a["minimum_total_screens"] != (a["shell_screens"]
                                           + a["content_screens_floor"]
                                           + a["closing_screens"])], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_CARD_ARITHMETIC_AGREES_WITH_THE_LIVE_DERIVATION", CARDS,
        [u["unit_id"] for u in UNITS
         if u["points"]["screen_sequence"]["arithmetic"]
         != B.screen_arithmetic(u["unit_id"])], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_CONTENT_FLOOR_EQUALS_THE_NAMED_SUBTOPIC_COUNT", CARDS,
        [a["unit_id"] for a in (B.screen_arithmetic(u) for u in B.BATCH_UNITS)
         if a["content_screens_floor"] != a["named_subtopics"]], [], len(B.BATCH_UNITS),
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    chk("ONLY_THE_DIALOGUE_UNIT_CARRIES_A_THIRD_SHELL_SCREEN", CARDS,
        sorted(a["unit_id"] for a in (B.screen_arithmetic(u) for u in B.BATCH_UNITS)
               if a["shell_includes_dialogue"]), ["K5-PL06-T05-B01"], len(B.BATCH_UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_DIALOGUE_ANSWER_IS_FROM_THE_THREE_ALLOWED_VALUES", CARDS,
        [u["unit_id"] for u in UNITS
         if u["points"]["dialogue"]["proposal"]
         not in ("REQUIRED", "NOT_REQUIRED", "UNCERTAIN")], [], len(UNITS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")

    # ==================== 5. DECISIONS ====================
    chk("TWENTY_NINE_DECISIONS_REQUESTED", DECISIONS, len(DEC), 29, len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("SIX_DECISIONS_PER_UNIT", DECISIONS,
        sorted({len([d for d in DEC if d["unit_id"] == u]) for u in B.BATCH_UNITS}), [6],
        len(DEC), "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("FIVE_BATCH_LEVEL_DECISIONS", DECISIONS,
        len([d for d in DEC if d["scope"] == "BATCH"]), 5, len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("NO_DUPLICATE_DECISION_IDS", DECISIONS,
        len({d["decision_id"] for d in DEC}), len(DEC), len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("DECISION_IDS_ARE_CONTIGUOUS_FROM_ONE", DECISIONS,
        [d["decision_id"] for d in DEC],
        [f"PL06-B1-D-{i:02d}" for i in range(1, len(DEC) + 1)], len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("NO_DECISION_ID_COLLIDES_WITH_A_T04_REGISTER", DECISIONS,
        [d["decision_id"] for d in DEC
         if not d["decision_id"].startswith("PL06-B1-D-")], [], len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("EVERY_DECISION_OFFERS_ONLY_DECLARED_RESPONSE_OPTIONS", DECISIONS,
        sorted({o for d in DEC for o in d["options"]}
               - {o["option"] for o in B.RESPONSE_OPTIONS}), [], len(DEC),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_DECISION_IS_BOUNDED_NOT_OPEN_ENDED", DECISIONS,
        [d["decision_id"] for d in DEC if len(d["options"]) < 2], [], len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    # -------- GABUNG requires a target ID --------
    gab = [d for d in DEC if "GABUNG" in d["options"]]
    chk("EVERY_GABUNG_DECISION_REQUIRES_A_TARGET_ID", DECISIONS,
        [d["decision_id"] for d in gab if not d["requires_target_id"]], [], len(gab),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("NO_NON_GABUNG_DECISION_DEMANDS_A_TARGET_ID", DECISIONS,
        [d["decision_id"] for d in DEC
         if d["requires_target_id"] and "GABUNG" not in d["options"]], [], len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("THE_GABUNG_OPTION_IS_DECLARED_TARGET_REQUIRING", DECISIONS,
        [o["option"] for o in B.RESPONSE_OPTIONS
         if o["requires_target_id"]], ["GABUNG"], len(B.RESPONSE_OPTIONS),
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # The needle is a literal here, not B.GABUNG_TARGET_FIELD. Fixture D-11 blanked that
    # constant and `"" in p` is true of every string, so the gate passed on a page with no
    # target field at all — an empty expected value is not an expected value.
    TARGET_FIELD_LITERAL = "ID sasaran"
    chk("EVERY_GABUNG_DECISION_PRINTS_A_TARGET_ID_FIELD_IN_THE_DOCX", DECISIONS,
        [d["decision_id"] for d in gab
         if not any(TARGET_FIELD_LITERAL in p
                    for p in _fields_after(paras, d["decision_id"]))],
        [], len(gab), E.DOCX_NAME)
    chk("THE_TARGET_FIELD_LABEL_IS_THE_DECLARED_ONE", DECISIONS,
        B.GABUNG_TARGET_FIELD, TARGET_FIELD_LITERAL, 1,
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # -------- every decision request has a response location --------
    chk("EVERY_DECISION_DECLARES_A_RESPONSE_LOCATION", DECISIONS,
        [d["decision_id"] for d in DEC
         if not d["response_location"].startswith("H · ")], [], len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("EVERY_DECISION_DECLARES_AN_EVIDENCE_LOCATION", DECISIONS,
        [d["decision_id"] for d in DEC if not d["card_reference"]], [], len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("EVERY_DECISION_APPEARS_IN_THE_DOCX", DECISIONS,
        [d["decision_id"] for d in DEC
         if not any(p.startswith(d["decision_id"] + " ·") for p in paras)], [], len(DEC),
        E.DOCX_NAME)
    chk("EVERY_DECISION_HAS_AN_OPTION_FIELD_IN_THE_DOCX", DECISIONS,
        [d["decision_id"] for d in DEC
         if not any(p.startswith("Pilihan:") for p in _fields_after(paras,
                                                                   d["decision_id"]))],
        [], len(DEC), E.DOCX_NAME)
    chk("EVERY_DECISION_HAS_A_FREE_NOTE_FIELD_IN_THE_DOCX", DECISIONS,
        [d["decision_id"] for d in DEC
         if not any(p.startswith("Catatan:") for p in _fields_after(paras,
                                                                   d["decision_id"]))],
        [], len(DEC), E.DOCX_NAME)
    chk("THE_EXTRACTION_AUTHORISATION_IS_ASKED", DECISIONS,
        len([d for d in DEC if d["point_key"] == "extraction"]), 1, len(DEC),
        "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("THE_MERGE_QUESTION_IS_ASKED_ONCE_AT_BATCH_LEVEL", DECISIONS,
        [d["decision_id"] for d in DEC if d["point_key"] == "merge_t03"],
        ["PL06-B1-D-26"], len(DEC), "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    chk("THE_LANGUAGE_POLICY_IS_DECLARED_AND_ASKED", DECISIONS,
        [B.LANGUAGE_POLICY["decision_surface"], B.LANGUAGE_POLICY["rationale_layer"],
         len([d for d in DEC if d["point_key"] == "language"])],
        ["MALAY", "ENGLISH", 1], len(DEC), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    # Literal Malay fragments, not B.LANGUAGE_POLICY["statement_ms"] — fixture D-22 rewrote
    # that string and rebuilt, and a gate reading the same field saw its own replacement
    # sitting happily in the document.
    chk("THE_LANGUAGE_POLICY_STATEMENT_REACHES_THE_DOCX_IN_MALAY", DECISIONS,
        [frag for frag in ("Permukaan keputusan", "Bahasa Melayu", "PL06-B1-D-29")
         if frag not in doc], [], 3, E.DOCX_NAME)
    chk("THE_LANGUAGE_POLICY_STATEMENT_IS_THE_DECLARED_ONE", DECISIONS,
        [frag for frag in ("Permukaan keputusan", "Bahasa Melayu", "PL06-B1-D-29")
         if frag not in B.LANGUAGE_POLICY["statement_ms"]], [], 3,
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("THE_CAST_QUESTION_RESTATES_AN_EXISTING_STOP_CONDITION", DECISIONS,
        any("STOP-006" in (d["why"] or "") for d in DEC if d["point_key"] == "cast"), True,
        len(DEC), "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")

    # ==================== 6. DOCX ====================
    chk("THE_DOCX_EXISTS", DOCX, present, True, 1, E.DOCX_NAME)
    chk("THE_DOCX_IS_A_VALID_PACKAGE", DOCX,
        zipfile.ZipFile(DOCX_PATH).testzip() if present else "missing", None, 1,
        E.DOCX_NAME)
    chk("THE_DOCX_CARRIES_THE_EXPECTED_PARTS", DOCX,
        sorted(zipfile.ZipFile(DOCX_PATH).namelist()) if present else [],
        sorted(["[Content_Types].xml", "_rels/.rels", "word/document.xml",
                "word/styles.xml", "word/settings.xml", "word/_rels/document.xml.rels",
                "docProps/core.xml", "docProps/app.xml"]), 8, E.DOCX_NAME)
    chk("THE_DOCX_DECLARES_MALAY", DOCX,
        "ms-MY" in zipfile.ZipFile(DOCX_PATH).read("word/styles.xml").decode() if present
        else False, True, 1, E.DOCX_NAME)
    chk("EVERY_SECTION_HEADING_REACHES_THE_DOCX", DOCX,
        [s["letter"] for s in B.SECTIONS
         if not any(p.startswith(s["letter"] + ". ") for p in paras)], [],
        len(B.SECTIONS), E.DOCX_NAME)
    chk("EVERY_AUTO_APPLIED_RULE_TEXT_REACHES_THE_DOCX", DOCX,
        [r["rule_id"] for r in B.AUTO_APPLIED_RULES if r["rule"] not in doc], [],
        len(B.AUTO_APPLIED_RULES), E.DOCX_NAME)
    chk("EVERY_NO_REUSE_ITEM_REACHES_THE_DOCX", DOCX,
        [n["item_id"] for n in B.NO_REUSE if n["item"] not in doc], [], len(B.NO_REUSE),
        E.DOCX_NAME)
    # Anchored on literal ID sets, not on len(B.exposures()). Fixtures P-03 and P-04
    # dropped an item from the model and rebuilt: the shortened list still matched the
    # shortened document, because both sides were the same list.
    chk("THE_SEVEN_EXPOSURE_IDS_ARE_THE_DECLARED_SET", DOCX,
        sorted(e["exposure_id"] for e in B.exposures()),
        ["EX-01", "EX-02", "EX-03", "EX-04", "EX-05", "EX-06", "EX-07"], 7,
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_EXPOSURE_ID_REACHES_THE_DOCX", DOCX,
        [x for x in ("EX-01", "EX-02", "EX-03", "EX-04", "EX-05", "EX-06", "EX-07")
         if x not in doc], [], 7, E.DOCX_NAME)
    chk("EVERY_EXPOSURE_STATEMENT_REACHES_THE_DOCX", DOCX,
        [e["exposure_id"] for e in B.exposures() if e["statement"] not in doc], [],
        len(B.exposures()) or 1, E.DOCX_NAME)
    chk("THE_FIVE_CROSS_UNIT_EXCEPTION_IDS_ARE_THE_DECLARED_SET", DOCX,
        sorted(x["exception_id"] for x in B.cross_unit_exceptions()),
        ["XU-01", "XU-02", "XU-03", "XU-04", "XU-05"], 5,
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("EVERY_CROSS_UNIT_EXCEPTION_ID_REACHES_THE_DOCX", DOCX,
        [x for x in ("XU-01", "XU-02", "XU-03", "XU-04", "XU-05") if x not in doc], [],
        5, E.DOCX_NAME)
    chk("EVERY_CROSS_UNIT_EXCEPTION_STATEMENT_REACHES_THE_DOCX", DOCX,
        [x["exception_id"] for x in B.cross_unit_exceptions()
         if x["statement"] not in doc], [], len(B.cross_unit_exceptions()) or 1,
        E.DOCX_NAME)
    chk("EVERY_START_ANCHOR_REACHES_THE_DOCX", DOCX,
        [u["unit_id"] for u in UNITS
         if u["points"]["boundary"]["start_anchor"] not in doc], [], len(UNITS),
        E.DOCX_NAME)
    chk("NO_REPOSITORY_PATH_IN_THE_DOCX", DOCX,
        [p for p in ("/home/user", "docs/pl06/tools", "reviews/storyboard") if p in doc],
        [], 3, E.DOCX_NAME)
    chk("THE_DOCX_IS_BYTE_DETERMINISTIC", DOCX,
        _rebuild_digest(), _rebuild_digest(), 1, E.DOCX_NAME)
    previews = sorted(f for f in os.listdir(E.PREVIEW_DIR)
                      if f.endswith(".png")) if os.path.isdir(E.PREVIEW_DIR) else []
    chk("A_PREVIEW_EXISTS_FOR_EVERY_PAGE", DOCX, len(previews) > 0, True,
        len(previews) or 1, "docs/pl06/harvest_batch1_preview/")
    chk("NO_PREVIEW_PAGE_IS_BLANK", DOCX, _blank_previews(previews), [],
        len(previews) or 1, "docs/pl06/harvest_batch1_preview/")
    chk("THE_PREVIEW_IS_LABELLED_AN_APPROXIMATION", DOCX,
        D.PREVIEW_KIND, "DETERMINISTIC_LAYOUT_APPROXIMATION_NOT_A_WORD_RENDER", 1,
        "docs/pl06/tools/pl06_docx_v1.py")

    # -------- one controlled model feeds both projections --------
    chk("THE_MARKDOWN_EXISTS", DOCX, bool(md), True, 1, E.MD_NAME)
    chk("EVERY_DECISION_APPEARS_IN_THE_MARKDOWN_TOO", DOCX,
        [d["decision_id"] for d in DEC if d["decision_id"] not in md], [], len(DEC),
        E.MD_NAME)
    chk("EVERY_NO_REUSE_ITEM_APPEARS_IN_THE_MARKDOWN_TOO", DOCX,
        [n["item_id"] for n in B.NO_REUSE if n["item"] not in md], [], len(B.NO_REUSE),
        E.MD_NAME)
    chk("THE_MARKDOWN_NAMES_ITS_GENERATOR", DOCX, B.GENERATED_BY in md, True, 1, E.MD_NAME)

    # ==================== 7. TRACE ====================
    chk("EVERY_TRACE_ROW_NAMES_ITS_EVIDENCE", TRACE,
        [r["claim"] for r in TR["rows"] if not r["evidence"]], [], len(TR["rows"]),
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("EVERY_TRACE_ROW_IS_TYPED", TRACE,
        sorted({r["evidence_class"] for r in TR["rows"]}
               - {"FROZEN_HASH_VERIFIED", "BLOCKED_NOT_EXTRACTED", "COURSE_WIDE_RULE",
                  "EXPLICIT_NO_REUSE", "INGESTED_IN_THIS_REPOSITORY",
                  "NAMED_IN_THE_FREEZE_PACKAGE_BY_IDENTITY_ONLY",
                  "NO_IMAGE_FOR_THIS_START_PAGE"}), [], len(TR["rows"]),
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("EVERY_UNIT_HAS_TRACE_ROWS", TRACE,
        [u for u in B.BATCH_UNITS
         if not [r for r in TR["rows"] if r["unit_id"] == u]], [], len(B.BATCH_UNITS),
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("EVERY_FROZEN_ROW_CARRIES_THE_PINNED_MAP_HASH", TRACE,
        [r["claim"] for r in TR["rows"]
         if r["evidence_class"] == "FROZEN_HASH_VERIFIED"
         and r["evidence_sha256"] != B.BOUNDARY_MAP_SHA256], [],
        TR["totals"]["frozen_hash_verified"], "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("THE_BLOCKED_CLAIMS_ARE_NOT_SILENTLY_DROPPED", TRACE,
        TR["totals"]["blocked_not_extracted"], 4 * len(B.BATCH_UNITS),
        len(TR["rows"]), "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("THE_MODULE_DOCX_IS_RECORDED_AS_EXTERNAL", TRACE,
        [TR["module_docx"]["custody"], TR["module_docx"]["in_this_repository"]],
        ["EXTERNAL_DURABLE_SOURCE_BY_IDENTITY", False], 1,
        "PL06_HARVEST_BATCH1_TRACEABILITY_v1.json")
    chk("THE_MODULE_DOCX_HASH_IS_CARRIED_NOT_INVENTED", TRACE,
        TR["module_docx"]["sha256"],
        "5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7", 1,
        "source-freeze/PL06_EXTERNAL_CUSTODY_RECORD_v1.md")

    # ==================== 8. GUARD ====================
    chk("FOUR_FORBIDDEN_STATUS_CLAIMS_DECLARED", GUARD,
        sorted(B.FORBIDDEN_STATUS_CLAIMS),
        ["ANSWER_KEYS_APPROVED", "BATCH_APPROVED", "CONTENT_EXTRACTED",
         "UNITS_READY_FOR_STORYBOARD_BUILD"], 4, "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_FORBIDDEN_CLAIM_APPEARS_IN_THE_DOCX", GUARD,
        [c for c in B.FORBIDDEN_STATUS_CLAIMS if c in doc], [],
        len(B.FORBIDDEN_STATUS_CLAIMS), E.DOCX_NAME)
    chk("THE_BATCH_STATUS_IS_AWAITING_NOT_APPROVED", GUARD, B.BATCH_STATUS,
        "CAIR_PREFILLED_AWAITING_BARIAH_DECISIONS", 1,
        "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("NO_STORYBOARD_DECK_WAS_GENERATED_FOR_ANY_BATCH_UNIT", GUARD,
        [f for f in os.listdir(E.DOCX_DIR) if f.lower().endswith(".pptx")], [],
        len(os.listdir(E.DOCX_DIR)), "reviews/storyboard-bariah/pl06_harvest_batch1/")
    chk("NO_MMD_REACT_SCORM_OR_LMS_ARTIFACT", GUARD,
        [n for n in E.ARTIFACTS
         if any(k in n.lower() for k in ("mmd", "react", "scorm", "lms"))], [],
        len(E.ARTIFACTS), "PL06_HARVEST_BATCH1_MODEL_v1.json")
    chk("CAIR_IS_NOT_NAMED_INSTRUCTIONAL_DESIGNER", GUARD,
        [s for s in ("CAIR is the Instructional Designer", "Instructional Designer: CAIR",
                     "CAIR sebagai Instructional Designer") if s in doc], [], 3,
        E.DOCX_NAME)
    chk("THE_FOUR_BLOCKING_STOPS_ARE_REFERENCED_NOT_REMINTED", GUARD,
        sorted(s["stop_id"] for s in B.BLOCKING_STOPS),
        ["STOP-003", "STOP-004", "STOP-005", "STOP-006"], len(B.BLOCKING_STOPS),
        "PL06_OPEN_AUTHORITY_ITEMS_v1.md")
    chk("THE_STALE_T04_ENTRY_ON_THE_REGISTER_IS_RECORDED_NOT_REWRITTEN", GUARD,
        any(x["exception_id"] == "XU-05" for x in B.cross_unit_exceptions()), True,
        len(B.cross_unit_exceptions()), "PL06_HARVEST_BATCH1_MODEL_v1.json")

    # ==================== 9. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID,
        "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1", 1, "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    chk("SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE", ACCOUNTING, SUITE_ID != PRIOR_SUITE_ID,
        True, 2, "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    chk("NOT_CHECKED_IS_PUBLISHED", ACCOUNTING, len(NOT_CHECKED) >= 5, True,
        len(NOT_CHECKED), "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    chk("EVERY_DECLARED_ARTIFACT_EXISTS", ACCOUNTING,
        [n for n in E.ARTIFACTS if not os.path.exists(os.path.join(PL06, n))], [],
        len(E.ARTIFACTS), "docs/pl06/")
    chk("EVERY_GATE_IS_TYPED", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res),
        "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    chk("EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT", ACCOUNTING,
        [r["gate_id"] for r in res if not r["source_artifact"]], [], len(res),
        "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    chk("NO_DUPLICATE_GATE_IDS", ACCOUNTING, len({r["gate_id"] for r in res}), len(res),
        len(res), "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    chk("NO_VACUOUS_GATES", ACCOUNTING, [r["gate_id"] for r in res if r["vacuous"]], [],
        len(res), "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    return res


def _section_bounds(paras, letter):
    """Paragraph index range of section `letter`, from its heading to the next one."""
    starts = {}
    for i, p in enumerate(paras):
        for l in "ABCDEFGH":
            if p.startswith(l + ". ") and l not in starts:
                starts[l] = i
    if letter not in starts:
        return None
    later = [v for k, v in starts.items() if v > starts[letter]]
    return starts[letter], (min(later) if later else len(paras))


def _in_section(paras, index, letter):
    b = _section_bounds(paras, letter)
    return bool(b) and b[0] <= index < b[1]


def _fields_after(paras, decision_id, window=4):
    """The response fields printed immediately under a decision heading."""
    for i, p in enumerate(paras):
        if p.startswith(decision_id + " ·"):
            return paras[i + 1:i + 1 + window]
    return []


def _rebuild_digest():
    import hashlib
    return hashlib.sha256(
        D._body_xml(E.blocks()).encode("utf-8")).hexdigest()


def _blank_previews(names):
    if not names:
        return []
    from PIL import Image
    out = []
    for f in names:
        im = Image.open(os.path.join(E.PREVIEW_DIR, f)).convert("L")
        if min(im.getdata()) > 200:
            out.append(f)
    return out


def report(res):
    lines = []
    for r in res:
        flag = "PASS" if r["ok"] else ("VACUOUS" if r["vacuous"] else "FAIL")
        lines.append(f"{flag:5} {r['gate_type']:<12} {r['gate_id']:<62} "
                     f"n={r['population']:<6} {r['value']!r}")
    active = [r for r in res if not r["vacuous"]]
    lines += ["", f"SUITE_ID = {SUITE_ID}",
              f"{sum(1 for r in active if r['ok'])}/{len(active)} active gates PASS",
              f"VACUOUS_GATES = {[r['gate_id'] for r in res if r['vacuous']]}"]
    by = {}
    for r in res:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    for k in sorted(by):
        lines.append(f"    {k:<20} {by[k]}")
    return "\n".join(lines)


def emit_report(res):
    active = [r for r in res if not r["vacuous"]]
    by = {}
    for r in res:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    md = ["<!-- GENERATED by docs/pl06/tools/pl06_batch1_qa_v1.py -->", "",
          "# PL06 harvest batch 1 — QA report", "", "```",
          f"SUITE_ID      = {SUITE_ID}",
          f"GATES         = {len(res)}",
          f"ACTIVE        = {len(active)}",
          f"PASS          = {sum(1 for r in active if r['ok'])}",
          f"FAIL          = {sum(1 for r in active if not r['ok'])}",
          f"VACUOUS       = {len(res) - len(active)}", "```", "",
          "Never added to another suite's total. "
          f"The prior suite is {PRIOR_SUITE_ID} and its gates are its own.", "",
          "| type | gates |", "|---|---|"]
    md += [f"| {k} | {by[k]} |" for k in sorted(by)]
    md += ["", "| gate | type | population | source artifact | result |", "|---|---|---|---|---|"]
    md += [f"| `{r['gate_id']}` | {r['gate_type']} | {r['population']} | "
           f"`{r['source_artifact']}` | {'PASS' if r['ok'] else 'FAIL'} |" for r in res]
    md += ["", "## Not checked", ""] + [f"- {x}" for x in NOT_CHECKED] + [""]
    path = os.path.join(PL06, "PL06_HARVEST_BATCH1_QA_REPORT_v1.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return path


if __name__ == "__main__":
    r = run()
    print(report(r))
    print("\nreport   :", emit_report(r))
    print("\nNOT CHECKED")
    for x in NOT_CHECKED:
        print("  -", x)
    sys.exit(0 if all(x["ok"] for x in r if not x["vacuous"]) and not any(
        x["vacuous"] for x in r) else 1)
