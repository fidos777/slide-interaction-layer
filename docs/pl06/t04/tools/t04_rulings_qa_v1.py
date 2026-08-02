# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.6 QA — typed gates over the incorporation of Bariah's partial rulings.

Every record carries an explicit `gate_type`; nothing is classified by ID substring.

    python3 docs/pl06/t04/tools/t04_rulings_qa_v1.py

A green suite measures the suite, not the artifact. What these gates hold is that the
rulings were transcribed without inflation, that the derived populations match the source,
and that nothing unresolved was quietly promoted to approved.
"""
import hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_rulings_data_v1 as D
import t04_data_v1 as SRC
import t04_rulings_emit_v1 as EMIT

EVIDENCE_INTEGRITY = "EVIDENCE_INTEGRITY"
DECISION_INTEGRITY = "DECISION_INTEGRITY"
POPULATION_COMPLETENESS = "POPULATION_COMPLETENESS"
AUTHORITY_DISCIPLINE = "AUTHORITY_DISCIPLINE"
INVENTION_GUARD = "INVENTION_GUARD"
ASSESSMENT_INTEGRITY = "ASSESSMENT_INTEGRITY"
AUTHORSHIP_GUARD = "AUTHORSHIP_GUARD"
SAFETY_DISCLOSURE = "SAFETY_DISCLOSURE"
MAPPING_INTEGRITY = "MAPPING_INTEGRITY"
PROPAGATION_GUARD = "PROPAGATION_GUARD"
ARTIFACT_AGREEMENT = "ARTIFACT_AGREEMENT"
ACCOUNTING = "ACCOUNTING"
SUPERSESSION_MARKER = "SUPERSESSION_MARKER"

GATE_TYPES = {EVIDENCE_INTEGRITY, DECISION_INTEGRITY, POPULATION_COMPLETENESS,
              AUTHORITY_DISCIPLINE, INVENTION_GUARD, ASSESSMENT_INTEGRITY, AUTHORSHIP_GUARD,
              SAFETY_DISCLOSURE, MAPPING_INTEGRITY, PROPAGATION_GUARD, ARTIFACT_AGREEMENT,
              ACCOUNTING, SUPERSESSION_MARKER}

# The six SmartArt nodes in source order. Frozen so a reorder or a seventh step fires.
EXPECTED_NODES = [
    "Koordinasi dan Demonstrasi Penyelenggaraan Taman",
    "Penyeliaan Penyelenggaraan Taman",
    "Penyeliaan Operasi Nurseri",
    "Penyeliaan Alatan dan Mesin Penyelenggaraan Taman",
    "Penyeliaan Inventori Taman",
    "Perancangan Sumber Manusia dan Kebajikan Pekerja",
]
# The four Landskap Kejur groups Bariah named, verbatim from the requirement sheet.
BARIAH_KEJUR_NAMES = ["Pengurusan Ruang dan Sirkulasi", "Fungsi Struktur dan Kejuruteraan",
                      "Kebolehgunaan dan Kemudahan", "Estetika dan Reka Bentuk"]

# Descendant heading rows, computed independently of the data module's own helpers so the
# gate is a second opinion rather than a restatement.
def _independent_descendants(op_row_id):
    rows = SRC.ROWS
    idx = {r["row_id"]: i for i, r in enumerate(rows)}
    out = []
    for r in rows[idx[op_row_id] + 1:]:
        if r["content_type"] == "HEADING_2":
            break
        if r["content_type"] == "HEADING_3" and r.get("list_level") == 2:
            break
        if r["content_type"].startswith("HEADING"):
            out.append(r["row_id"])
    return out


VAGUE_PHRASES = ["their sub", "their subtopics", "its subtopics", "and their subs",
                 "sub-topics beneath", "subtopik mereka"]
FINAL_QUIZ_MARKERS = ("apakah", "yang manakah", "pilih jawapan", "jawapan yang betul",
                      "answer:", "correct answer", "jawapan:")
ANSWER_KEY_MARKERS = ("answer_key", "answer key", "jawapan_betul", "correct_option", "key=",
                      "kunci jawapan")
OPTION_MARKER = re.compile(r"^\s*[a-dA-D][).]\s")
# A confirmation word must sit CLOSE to the threshold mention to count. A sentence that
# reports "composition is confirmed; the threshold was not mentioned" is the opposite of the
# defect, and a bare co-occurrence test read it as the defect at Stage 4.2F-B0.5 too.
THRESHOLD_CONFIRMED = re.compile(
    r"(60\s*(?:percent|%|peratus)[^.]{0,40}?\b(?:confirmed|approved|settled|is the pass)\b"
    r"|\b(?:confirmed|approved|settled)\b[^.]{0,40}?60\s*(?:percent|%|peratus))", re.I)
QUIZ_NOT_PRODUCED = ["final stems", "final answer options", "final answer key",
                     "final rationale", "approved feedback", "a pass mark"]

CONTROLLED_ARTIFACTS = [
    "T04_BARIAH_PARTIAL_RULINGS_v1.md", "T04_BARIAH_PARTIAL_RULINGS_v1.json",
    "T04_VISUAL_DIRECTION_INVENTORY_v1.md", "T04_VISUAL_DIRECTION_INVENTORY_v1.csv",
    "T04_VISUAL_DIRECTION_INVENTORY_v1.json",
    "T04_SOURCE_TO_SCREEN_MAPPING_v2.md", "T04_SOURCE_TO_SCREEN_MAPPING_v2.json",
    "T04_SCREEN_CONTRACTS_DRAFT_v2.md", "T04_SCREEN_CONTRACTS_DRAFT_v2.json",
    "T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v2.md", "T04_QUIZ_BLUEPRINT_v2.md",
    "T04_LEGAL_CONTENT_CLARIFICATION_v1.md", "T04_REMAINING_BARIAH_DECISIONS_v1.md",
    "T04_BARIAH_WHATSAPP_FOLLOWUP_DRAFT_v1.md",
]


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


def _strings(blob, drop=()):
    """Every string inside a blob, minus verbatim source rows and any dict key in `drop`.

    A verbatim source row is EVIDENCE, not a claim. Scanning it as though it were a claim
    produced two false positives at Stage 4.2F-B0 and the same category error is excluded
    here by construction rather than by adjusting a fixture.
    """
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


ANALYSIS_BLOBS = ("EVIDENCE", "RULING_LOCATORS", "DECISIONS", "VISUAL_OBLIGATIONS",
                  "MAPPING_V2", "MAPPING_IMPACT", "CONTRACTS_V2", "RUMUSAN_V2",
                  "RUMUSAN_STYLE_RULES", "QUIZ_V2", "LEGAL_CLARIFICATION", "D03_FOLLOWUP",
                  "D05_FOLLOWUP", "REMAINING", "WHATSAPP")
# `not_produced` is a DECLARATION of what was withheld. Scanning it for the very tokens it
# exists to disclaim marks honest disclosure as a defect — the Stage 4.2F-B0.5 bug, repeated.
# It is excluded here and asserted intact by QUIZ_NOT_PRODUCED_LIST_INTACT.
ANALYSIS_DROP = ("not_produced",)


def _analysis_text():
    out = []
    for name in ANALYSIS_BLOBS:
        out += _strings(getattr(D, name), drop=ANALYSIS_DROP)
    return out


def _inventory_text():
    """The controlled inventory records only — where a vague phrase would be a real defect.

    Bariah's own words 'Their sub – perlu visual' are quoted verbatim in the evidence
    register, which is exactly where they belong. Flagging that quotation would punish
    faithful transcription.
    """
    return (_strings(D.VISUAL_OBLIGATIONS) + _strings(D.MAPPING_V2)
            + _strings(D.CONTRACTS_V2) + _strings(D.LEGAL_GROUPS))


def _quiz_text():
    """Quiz records only, minus the withheld-items declaration."""
    return _strings(D.QUIZ_V2, drop=ANALYSIS_DROP)


def run():
    res = []

    def chk(gid, gtype, value, expected):
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        ok=value == expected))

    VO = D.VISUAL_OBLIGATIONS
    DEC = {d["decision_id"]: d for d in D.DECISIONS}
    Q = D.QUIZ_V2
    R = D.RUMUSAN_V2
    ANALYSIS = _analysis_text()
    ANALYSIS_LC = [s.lower() for s in ANALYSIS]

    # ==================== 1. EVIDENCE ====================
    chk("EVIDENCE_ITEMS", EVIDENCE_INTEGRITY, len(D.EVIDENCE), 2)
    missing = [e["evidence_id"] for e in D.EVIDENCE
               if not os.path.exists(os.path.join(REPO, e["frozen_path"]))]
    chk("EVIDENCE_FILES_PRESENT", EVIDENCE_INTEGRITY, missing, [])
    chk("EVIDENCE_FROZEN_BYTE_IDENTICALLY", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE
         if os.path.exists(os.path.join(REPO, e["frozen_path"]))
         and (_sha256(os.path.join(REPO, e["frozen_path"])) != e["sha256"]
              or os.path.getsize(os.path.join(REPO, e["frozen_path"])) != e["byte_size"])],
        [])
    chk("EVIDENCE_SHA256_RECORDED", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE
         if not (isinstance(e["sha256"], str) and len(e["sha256"]) == 64
                 and re.fullmatch(r"[0-9a-f]{64}", e["sha256"]))], [])
    chk("EVIDENCE_CLASS", EVIDENCE_INTEGRITY,
        sorted({e["evidence_class"] for e in D.EVIDENCE}), ["BARIAH_DIRECT_SCREENSHOT"])
    chk("EVIDENCE_REVIEWER", EVIDENCE_INTEGRITY,
        sorted({e["reviewer"] for e in D.EVIDENCE}), ["BARIAH"])
    chk("EVIDENCE_SCOPE", EVIDENCE_INTEGRITY,
        sorted({e["scope"] for e in D.EVIDENCE}), [D.UNIT_ID])
    chk("EVIDENCE_UNMODIFIED", EVIDENCE_INTEGRITY,
        [e["evidence_id"] for e in D.EVIDENCE if not e["modification"].startswith("NONE")], [])
    chk("EVIDENCE_IN_EXISTING_HIERARCHY", EVIDENCE_INTEGRITY,
        D.EVIDENCE_DIR.startswith("reviews/storyboard-bariah/")
        and os.path.isdir(os.path.join(REPO, "reviews/storyboard-bariah")), True)
    chk("EVERY_RULING_BINDS_TO_FROZEN_EVIDENCE", EVIDENCE_INTEGRITY,
        sorted({r["locator"] for r in D.RULING_LOCATORS
                if r["evidence_id"] not in {e["evidence_id"] for e in D.EVIDENCE}}), [])
    chk("EVERY_EVIDENCE_LOCATOR_DECLARED", EVIDENCE_INTEGRITY,
        sorted({loc for e in D.EVIDENCE for loc in e["ruling_locators"]}
               ^ {r["locator"] for r in D.RULING_LOCATORS}), [])

    # ==================== 2. DECISION STATUS ====================
    chk("DECISIONS_REGISTERED", DECISION_INTEGRITY,
        sorted(DEC), ["D-01", "D-02A", "D-02B", "D-02C", "D-03", "D-04", "D-05"])
    chk("UNKNOWN_DECISION_STATUSES", DECISION_INTEGRITY,
        sorted({d["status"] for d in D.DECISIONS
                if d["status"] not in D.DECISION_STATUSES}), [])
    chk("D01_CONFIRMED_WITH_EXPANSION", DECISION_INTEGRITY,
        DEC["D-01"]["status"], "CONFIRMED_WITH_EXPANSION")
    chk("D01_NEW_RULING", DECISION_INTEGRITY,
        DEC["D-01"]["ruling"], "VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION")
    chk("D01_OLD_BLANKET_RULING_MARKED_SUPERSEDED", DECISION_INTEGRITY,
        DEC["D-01"]["superseded_recommendation"], "TEXT_AND_DIAGRAM_LED")
    chk("TEXT_AND_DIAGRAM_LED_NOT_PRESENTED_AS_FINAL", DECISION_INTEGRITY,
        [d["decision_id"] for d in D.DECISIONS
         if d["ruling"] == "TEXT_AND_DIAGRAM_LED"], [])
    chk("D02A_CONFIRMED_BARIAH_DIRECT", DECISION_INTEGRITY,
        DEC["D-02A"]["status"], "CONFIRMED_BARIAH_DIRECT")
    chk("D02A_SCOPE_NOT_REDUCED", DECISION_INTEGRITY,
        DEC["D-02A"]["scope"], "ALL_PLS_IN_KURSUS")
    chk("D02B_UNRESOLVED", DECISION_INTEGRITY, DEC["D-02B"]["status"], "UNRESOLVED")
    chk("D02C_DRAFT_AUTHORISED_ONLY", DECISION_INTEGRITY,
        DEC["D-02C"]["status"], "DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW")
    chk("D03_UNRESOLVED", DECISION_INTEGRITY, DEC["D-03"]["status"], "UNRESOLVED")
    chk("D04_CLARIFICATION_REQUIRED", DECISION_INTEGRITY,
        DEC["D-04"]["status"], "CLARIFICATION_REQUIRED")
    chk("D05_PARTIALLY_RESOLVED", DECISION_INTEGRITY,
        DEC["D-05"]["status"], "PARTIALLY_RESOLVED")
    chk("D05_CONFIRMED_PART_IS_THE_PER_STEP_VISUAL", DECISION_INTEGRITY,
        DEC["D-05"]["ruling"], "EVERY_PROCESS_STEP_REQUIRES_A_VISUAL")
    chk("D05_THREE_ITEMS_STILL_UNCONFIRMED", DECISION_INTEGRITY,
        sorted({c["status"] for c in D.D05_FOLLOWUP["confirmations_required"]}),
        ["NOT_CONFIRMED"])
    chk("APPROVED_ITEMS", DECISION_INTEGRITY, D.APPROVED_ITEMS, 0)
    chk("CAST_REMAINS_UNRESOLVED", DECISION_INTEGRITY,
        (DEC["D-03"]["status"], D.D03_FOLLOWUP["status"],
         D.D03_FOLLOWUP["prior_recommendation_status"]),
        ("UNRESOLVED", "UNRESOLVED", "SUPERSEDED_NOT_APPROVED"))
    # Structural, not prose-scanning. Prose that says Hilmi is NOT approved is the desired
    # state; a keyword co-occurrence test read it as the defect. Hilmi may appear ONLY inside
    # the D-03 record and its follow-up, and D-03 must carry no ruling.
    chk("HILMI_CONFINED_TO_THE_UNRESOLVED_D03_RECORD", DECISION_INTEGRITY,
        sorted({name for name in ANALYSIS_BLOBS
                if any("hilmi" in s.lower() for s in _strings(getattr(D, name)))}
               - {"DECISIONS", "D03_FOLLOWUP"}), [])
    chk("D03_CARRIES_NO_RULING", DECISION_INTEGRITY, DEC["D-03"]["ruling"], None)
    chk("HILMI_NOT_ASSIGNED_IN_ANY_CONTRACT_OR_OBLIGATION", DECISION_INTEGRITY,
        [s for s in _strings(D.CONTRACTS_V2) + _strings(VO) + _strings(D.MAPPING_V2)
         if "hilmi" in s.lower()], [])

    # ==================== 3. VISUAL OBLIGATION POPULATION ====================
    chk("VISUAL_OBLIGATIONS_TOTAL", POPULATION_COMPLETENESS, len(VO), 46)
    vids = [v["visual_obligation_id"] for v in VO]
    chk("DUPLICATE_VISUAL_OBLIGATION_IDS", POPULATION_COMPLETENESS,
        sorted({i for i in vids if vids.count(i) > 1}), [])
    chk("ALL_SIX_PROCESS_NODES_HAVE_SEPARATE_OBLIGATIONS", POPULATION_COMPLETENESS,
        [v["raw_source_heading"] for v in VO
         if v["population_group"] == "A_PROCESS_NODES"], EXPECTED_NODES)
    chk("NO_SEVENTH_PROCESS_STEP", POPULATION_COMPLETENESS,
        len([v for v in VO if v["population_group"] == "A_PROCESS_NODES"]), 6)
    chk("PROCESS_NODE_ORDER_PRESERVED", POPULATION_COMPLETENESS,
        [v["raw_source_heading"] for v in VO
         if v["population_group"] == "A_PROCESS_NODES"], SRC.ASSETS[0]["source_subject_nodes"])
    for op, name in ((D.OP_SIRAM, "SIRAM"), (D.OP_BAJA, "BAJA"), (D.OP_RACUN, "RACUN")):
        want = _independent_descendants(op)
        got = [v["source_row_ids"][0] for v in VO
               if v["population_group"] == "B_OPERATION_DESCENDANT"
               and v["parent_topic"] == SRC.BY_ID[op]["raw_source_text"]]
        chk(f"ALL_{name}_DESCENDANTS_REPRESENTED", POPULATION_COMPLETENESS, got, want)
        chk(f"{name}_MAIN_EXPLANATION_HAS_AN_OBLIGATION", POPULATION_COMPLETENESS,
            len([v for v in VO if v["population_group"] == "B_OPERATION_MAIN"
                 and v["source_row_ids"][0] == op]), 1)
    chk("LEMBUT_MAIN_EXPLANATION_HAS_AN_OBLIGATION", POPULATION_COMPLETENESS,
        len([v for v in VO if v["population_group"] == "B_LEMBUT_MAIN"]), 1)
    chk("KEJUR_MAIN_EXPLANATION_HAS_AN_OBLIGATION", POPULATION_COMPLETENESS,
        len([v for v in VO if v["population_group"] == "C_KEJUR_MAIN"]), 1)
    chk("ALL_FOUR_NAMED_KEJUR_SUBTOPICS_REPRESENTED", POPULATION_COMPLETENESS,
        [v["raw_source_heading"] for v in VO if v["population_group"] == "C_KEJUR_GROUP"],
        BARIAH_KEJUR_NAMES)
    chk("EVERY_OBLIGATION_BINDS_TO_A_BARIAH_RULING", POPULATION_COMPLETENESS,
        sorted({v["bariah_ruling_locator"] for v in VO}
               - {r["locator"] for r in D.RULING_LOCATORS}), [])
    chk("EVERY_OBLIGATION_BINDS_TO_REAL_SOURCE_ROWS", POPULATION_COMPLETENESS,
        sorted({r for v in VO for r in v["source_row_ids"] if r not in SRC.BY_ID}), [])
    chk("NO_VAGUE_SUBTOPIC_PHRASE_IN_CONTROLLED_RECORDS", POPULATION_COMPLETENESS,
        sorted({p for p in VAGUE_PHRASES
                for s in (x.lower() for x in _inventory_text()) if p in s}), [])
    # The other half of the same rule: Bariah's vague phrase must survive verbatim in the
    # evidence register, so the enumeration can be audited against what she actually wrote.
    chk("BARIAH_VAGUE_PHRASE_PRESERVED_VERBATIM_IN_EVIDENCE", POPULATION_COMPLETENESS,
        [r["verbatim"] for r in D.RULING_LOCATORS if r["locator"] == "BR-L4"],
        ["Their sub – perlu visual"])

    # ==================== 4. AUTHORITY DISCIPLINE ====================
    chk("TREATMENT_AUTHORITY_IS_BARIAH_DIRECT", AUTHORITY_DISCIPLINE,
        sorted({v["treatment_authority"] for v in VO}), ["BARIAH_DIRECT_SCREENSHOT"])
    chk("SUBJECT_AUTHORITY_NEVER_BARIAH_DIRECT", AUTHORITY_DISCIPLINE,
        [v["visual_obligation_id"] for v in VO
         if v["subject_authority"] != "MODULE_SOURCE_ATTESTED"], [])
    chk("SOURCE_AUTHORITY_IS_MODULE_ATTESTED", AUTHORITY_DISCIPLINE,
        sorted({v["source_authority"] for v in VO}), ["MODULE_SOURCE_ATTESTED"])
    chk("CONTRACT_SUBJECT_AUTHORITY_NEVER_BARIAH_DIRECT", AUTHORITY_DISCIPLINE,
        [c["contract_id"] for c in D.CONTRACTS_V2
         if c["visual_subject_authority"] != "MODULE_SOURCE_ATTESTED"], [])
    chk("BARIAH_REMAINS_INSTRUCTIONAL_AUTHORITY", AUTHORITY_DISCIPLINE,
        (D.INSTRUCTIONAL_AUTHORITY, R["instructional_authority"],
         Q["final_instructional_authority"]), ("BARIAH", "BARIAH", "BARIAH"))
    chk("CAIR_NOT_NAMED_INSTRUCTIONAL_DESIGNER", AUTHORITY_DISCIPLINE,
        [s for s in ANALYSIS
         if re.search(r"CAIR[^.]{0,40}(instructional designer|instructional author)", s, re.I)],
        [])

    # ==================== 5. INVENTION GUARD ====================
    chk("NO_UNKNOWN_VISUAL_CLASS", INVENTION_GUARD,
        sorted({v["proposed_visual_class"] for v in VO
                if v["proposed_visual_class"] not in D.ALLOWED_VISUAL_CLASSES}), [])
    # An image is only ever claimed to exist where the source actually holds one.
    chk("MISSING_SOURCE_IMAGE_NOT_REPORTED_AS_EXISTING", INVENTION_GUARD,
        [v["visual_obligation_id"] for v in VO
         if v["existing_source_asset_available"] not in (D.NO_SOURCE_IMAGE,
                                                         D.SMARTART_LABEL_ONLY)], [])
    chk("SOURCE_ASSET_ID_ONLY_WHERE_AN_ASSET_EXISTS", INVENTION_GUARD,
        [v["visual_obligation_id"] for v in VO
         if v["source_asset_id"] is not None
         and v["source_asset_id"] not in {a["asset_id"] for a in SRC.ASSETS}], [])
    chk("SMARTART_REFERENCE_ONLY_ON_PROCESS_NODES", INVENTION_GUARD,
        sorted({v["population_group"] for v in VO if v["source_asset_id"]}),
        ["A_PROCESS_NODES"])
    chk("RASTER_SOURCE_IMAGES", INVENTION_GUARD, SRC.TOTALS["raster_images"], 0)
    chk("NEW_ASSETS_LABELLED_NEW_MMD_ASSET_REQUIRED", INVENTION_GUARD,
        [v["visual_obligation_id"] for v in VO
         if v["production_requirement"] != "NEW_MMD_ASSET_REQUIRED"], [])
    chk("NO_MMD_ASSET_PRODUCTION_CLAIMED", INVENTION_GUARD,
        sorted({v["mmd_dependency"] for v in VO}), ["MMD_ASSET_PRODUCTION_NOT_STARTED"])
    chk("SMARTART_PRODUCTION_NOT_STARTED", INVENTION_GUARD,
        D.D05_FOLLOWUP["production_status"], "NOT_STARTED")
    chk("SIX_NODE_LABELS_UNCHANGED", INVENTION_GUARD,
        [n["label"] for n in D.D05_FOLLOWUP["six_nodes_in_order"]], EXPECTED_NODES)
    chk("KEJUR_SUB_ITEMS_NOT_SILENTLY_ADDED", INVENTION_GUARD,
        sorted({r for v in VO if v["population_group"] == "C_KEJUR_GROUP"
                for r in v["source_row_ids"]}
               & set(D.SCOPE_ASYMMETRY["kejur_sub_items_not_covered"])
               & {v["source_row_ids"][0] for v in VO}), [])

    # ==================== 6. ASSESSMENT ====================
    chk("QUIZ_COMPOSITION_CONFIRMED", ASSESSMENT_INTEGRITY,
        Q["quiz_composition"], "CONFIRMED_BARIAH_DIRECT")
    chk("QUIZ_SLOT_COUNT", ASSESSMENT_INTEGRITY, len(Q["slots"]), 5)
    chk("QUIZ_COMPOSITION_EXACTLY_4_MCQ_1_MR", ASSESSMENT_INTEGRITY,
        (len([s for s in Q["slots"] if s["item_type"] == "MCQ"]),
         len([s for s in Q["slots"] if s["item_type"] == "MULTIPLE_RESPONSE"]),
         Q["mcq_count"], Q["mr_count"]), (4, 1, 4, 1))
    chk("QUIZ_SLOT_ORDER", ASSESSMENT_INTEGRITY,
        [s["slot"] for s in Q["slots"]], ["Q1", "Q2", "Q3", "Q4", "Q5"])
    chk("QUIZ_SCOPE_ALL_PLS_IN_KURSUS", ASSESSMENT_INTEGRITY, Q["scope"], "ALL_PLS_IN_KURSUS")
    chk("PASS_THRESHOLD_UNRESOLVED", ASSESSMENT_INTEGRITY, Q["pass_threshold"], "UNRESOLVED")
    chk("SIXTY_PERCENT_NOT_CONFIRMED", ASSESSMENT_INTEGRITY,
        [s for s in ANALYSIS if THRESHOLD_CONFIRMED.search(s)], [])
    chk("QUIZ_CONTENT_BLUEPRINT_ONLY", ASSESSMENT_INTEGRITY, Q["quiz_content"],
        "BLUEPRINT_ONLY")
    chk("NO_FINAL_QUIZ_STEM", ASSESSMENT_INTEGRITY,
        sorted({m for m in FINAL_QUIZ_MARKERS for s in ANALYSIS_LC if m in s}), [])
    # Scoped to the quiz records. A/B/C option markers are used throughout this pack for
    # DECISION options — D-01's three requirement groups, D-03's cast options, D-05's three
    # confirmations. Those are not quiz answers, and a repository-wide scan called them one.
    chk("NO_FINAL_ANSWER_OPTION", ASSESSMENT_INTEGRITY,
        [s for s in _quiz_text() if OPTION_MARKER.match(s)], [])
    chk("NO_FINAL_ANSWER_KEY", ASSESSMENT_INTEGRITY,
        sorted({m for m in ANSWER_KEY_MARKERS
                for s in (x.lower() for x in ANALYSIS) if m in s}), [])
    chk("QUIZ_NOT_PRODUCED_LIST_INTACT", ASSESSMENT_INTEGRITY,
        sorted(Q["not_produced"]), sorted(QUIZ_NOT_PRODUCED))
    # Six coverage points in, five slots out, nothing discarded.
    covered = sorted({b for s in Q["slots"] for b in s["from_blueprint"]})
    chk("ALL_SIX_COVERAGE_POINTS_CARRIED", ASSESSMENT_INTEGRITY, covered,
        ["T04-QB-01", "T04-QB-02", "T04-QB-03", "T04-QB-04", "T04-QB-05", "T04-QB-06"])
    chk("CONSOLIDATION_DECLARED_NOT_SILENT", ASSESSMENT_INTEGRITY,
        (Q["consolidation"]["merged"]["into"],
         sorted(Q["consolidation"]["merged"]["from_points"])),
        ("Q5", ["T04-QB-03", "T04-QB-04"]))
    chk("QUIZ_SLOT_ROWS_IN_EXTRACT", ASSESSMENT_INTEGRITY,
        sorted({r for s in Q["slots"] for r in s["source_row_ids"] if r not in SRC.BY_ID}), [])

    # ==================== 7. AUTHORSHIP ====================
    chk("RUMUSAN_REMAINS_CAIR_ASSISTED_DRAFT", AUTHORSHIP_GUARD,
        (R["content_status"], R["approval_status"]),
        ("CAIR_ASSISTED_DRAFT", "PENDING_BARIAH_REVIEW"))
    chk("RUMUSAN_STATEMENT_COUNT", AUTHORSHIP_GUARD, len(R["statements"]), 4)
    chk("RUMUSAN_ROWS_IN_EXTRACT", AUTHORSHIP_GUARD,
        sorted({r for s in R["statements"] for r in s["source_row_ids"]
                if r not in SRC.BY_ID}), [])
    chk("MEDIUM_RISK_GENERALISATION_PRESERVED_AND_FLAGGED", AUTHORSHIP_GUARD,
        [s["statement_id"] for s in R["statements"]
         if s["factual_risk_status"].startswith("MEDIUM")], ["T04-RUM2-04"])
    chk("EVERY_RUMUSAN_STATEMENT_HAS_A_REVIEW_FIELD", AUTHORSHIP_GUARD,
        [s["statement_id"] for s in R["statements"]
         if s["bariah_review"]["decision"] is not None], [])
    chk("EVERY_RUMUSAN_STATEMENT_CITES_A_STYLE_RULE", AUTHORSHIP_GUARD,
        [s["statement_id"] for s in R["statements"] if not s["style_rule_applied"]], [])
    chk("STYLE_RULES_REFERENCED_EXIST", AUTHORSHIP_GUARD,
        sorted({x for s in R["statements"] for x in s["style_rule_applied"]}
               - {r["rule_id"] for r in D.RUMUSAN_STYLE_RULES}), [])
    chk("V1_STATEMENTS_ALL_ACCOUNTED_FOR", AUTHORSHIP_GUARD,
        sorted({m["v1"] for m in D.RUMUSAN_V1_TO_V2}),
        ["T04-RUM-01", "T04-RUM-02", "T04-RUM-03", "T04-RUM-04", "T04-RUM-05"])
    chk("FORBIDDEN_AUTHORSHIP_LABELS", AUTHORSHIP_GUARD,
        sorted({lbl for lbl in ("ID_AUTHORED", "BARIAH_APPROVED",
                                "FINAL_INSTRUCTIONAL_CONTENT")
                for s in ANALYSIS if lbl in s}), [])

    # ==================== 8. SAFETY AND LEGAL DISCLOSURE ====================
    chk("LEGAL_GROUPS", SAFETY_DISCLOSURE, len(D.LEGAL_GROUPS), 9)
    chk("LEGAL_ROWS_LISTED_INDIVIDUALLY", SAFETY_DISCLOSURE,
        D.LEGAL_TOTALS["rows"], sum(len(g["rows"]) for g in D.LEGAL_GROUPS))
    chk("LEGAL_ROWS_IN_EXTRACT", SAFETY_DISCLOSURE,
        sorted({r["source_row_id"] for g in D.LEGAL_GROUPS for r in g["rows"]
                if r["source_row_id"] not in SRC.BY_ID}), [])
    chk("NO_DUPLICATE_LEGAL_ROWS", SAFETY_DISCLOSURE,
        sorted({r["source_row_id"] for g in D.LEGAL_GROUPS for r in g["rows"]
                if [x["source_row_id"] for gg in D.LEGAL_GROUPS
                    for x in gg["rows"]].count(r["source_row_id"]) > 1}), [])
    chk("LEGAL_SPLIT_REMAINS_PENDING_CONFIRMATION", SAFETY_DISCLOSURE,
        (D.LEGAL_CLARIFICATION["status"],
         D.LEGAL_CLARIFICATION["recommendation_status"],
         D.LEGAL_CLARIFICATION["applied_to_a_contract"]),
        ("PENDING_BARIAH_CONFIRMATION", "PROPOSED_NOT_APPROVED", False))
    chk("NO_MANDATORY_ROW_PROPOSED_FOR_REVEAL_ONLY", SAFETY_DISCLOSURE,
        [r["source_row_id"] for g in D.LEGAL_GROUPS for r in g["rows"]
         if r["mandatory_or_supplementary"] == "MANDATORY"
         and r["proposed_optional_reveal_treatment"] != "none"], [])
    chk("SUPPLEMENTARY_CANDIDATES_ARE_DECLARED", SAFETY_DISCLOSURE,
        sorted(D.LEGAL_CLARIFICATION["supplementary_candidates"]),
        sorted(r["source_row_id"] for g in D.LEGAL_GROUPS for r in g["rows"]
               if r["mandatory_or_supplementary"] == "SUPPLEMENTARY"))
    chk("EVERY_LEGAL_ROW_HAS_A_CONFIRMATION_FIELD", SAFETY_DISCLOSURE,
        [r["source_row_id"] for g in D.LEGAL_GROUPS for r in g["rows"]
         if r["bariah_confirmation"]["decision"] is not None], [])
    # The five hand-typed obligation ids that were wrong on the first pass.
    chk("LEGAL_VISUAL_REFERENCES_RESOLVE", SAFETY_DISCLOSURE,
        [r["source_row_id"] for g in D.LEGAL_GROUPS for r in g["rows"]
         if r["visual_requirement"].startswith("T04-VO-")
         and r["source_row_id"] not in
         next(v["source_row_ids"] for v in VO
              if v["visual_obligation_id"] == r["visual_requirement"].split(" ")[0])], [])

    # ==================== 9. MAPPING ====================
    chk("MAPPING_CANDIDATES", MAPPING_INTEGRITY, len(D.MAPPING_V2), 6)
    chk("CONTRACTS_V2", MAPPING_INTEGRITY, len(D.CONTRACTS_V2), 6)
    chk("FINAL_SCREEN_COUNT_NOT_CLAIMED", MAPPING_INTEGRITY,
        (D.FINAL_SCREEN_COUNT, D.MAPPING_IMPACT["final_screen_count"]),
        ("NOT_CLAIMED", "NOT_CLAIMED"))
    chk("MAPPING_OBLIGATION_IDS_RESOLVE", MAPPING_INTEGRITY,
        sorted({i for m in D.MAPPING_V2 for i in m["visual_obligation_ids"]} - set(vids)), [])
    chk("REQUIRED_VISUAL_STATES_MATCH_OBLIGATION_COUNTS", MAPPING_INTEGRITY,
        [m["screen_candidate_id"] for m in D.MAPPING_V2
         if m["required_visual_states"] != len(m["visual_obligation_ids"])], [])
    chk("UNMAPPED_OBLIGATIONS_DECLARED", MAPPING_INTEGRITY,
        (D.MAPPING_IMPACT["obligations_with_no_home"], len(D.UNMAPPED_VO)), (28, 28))
    chk("MAPPING_ACCOUNTING_ADDS_UP", MAPPING_INTEGRITY,
        D.MAPPING_IMPACT["obligations_mapped_to_existing_candidates"]
        + D.MAPPING_IMPACT["obligations_with_no_home"], len(VO))
    chk("EVERY_CONTRACT_CARRIES_ITS_SUPERSEDED_VISUAL_TREATMENT", MAPPING_INTEGRITY,
        [c["contract_id"] for c in D.CONTRACTS_V2
         if not c.get("superseded_visual_treatment")], [])
    chk("NO_CONTRACT_MARKED_APPROVED", MAPPING_INTEGRITY,
        sorted({c["bariah_approval"]["status"] for c in D.CONTRACTS_V2}),
        ["PENDING_BARIAH_REVIEW"])

    # ==================== 10. PROPAGATION ====================
    chk("B02_FAMILIES_PROPAGATED", PROPAGATION_GUARD, D.B02_FAMILIES_PROPAGATED, 0)
    chk("NO_B02_FAMILY_TOKEN_IN_CONTROLLED_RECORDS", PROPAGATION_GUARD,
        [s for s in ANALYSIS
         if re.search(r"\bFAMILY_(S|P1|P2)\b", s)
         or re.search(r"\bFamily (S|P1|P2)\b", s) and "NOT" not in s.upper()], [])
    chk("SCREEN_COUNT_NOT_DERIVED_FROM_B02", PROPAGATION_GUARD,
        D.MAPPING_IMPACT["derived_from_b02"], False)
    chk("NO_B02_FACT_IN_RUMUSAN", PROPAGATION_GUARD,
        sorted({t for t in ("Struktur Persisir Air", "Struktur Teduhan", "Kemudahan Awam",
                            "Water Feature", "Kerusi Taman", "Papan Tanda", "Tong Sampah",
                            "Drinking Fountain", "BBQ Pit", "Perabot Taman", "Struktur Taman")
                for s in R["statements"] if t.lower() in s["draft_text"].lower()}), [])
    chk("RUMUSAN_STYLE_SOURCE_IS_STYLE_ONLY", PROPAGATION_GUARD,
        D.RUMUSAN_STYLE_SOURCE["authority"], "APPROVED_B02_TREATMENT — style reference only")

    # ==================== 11. ARTIFACT AGREEMENT ====================
    for name in CONTROLLED_ARTIFACTS:
        pass
    chk("ALL_CONTROLLED_ARTIFACTS_PRESENT", ARTIFACT_AGREEMENT,
        [n for n in CONTROLLED_ARTIFACTS if not os.path.exists(os.path.join(T04, n))], [])
    inv_json = json.load(open(os.path.join(T04, "T04_VISUAL_DIRECTION_INVENTORY_v1.json"),
                              encoding="utf-8"))
    chk("INVENTORY_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        len(inv_json["obligations"]), len(VO))
    csv_lines = open(os.path.join(T04, "T04_VISUAL_DIRECTION_INVENTORY_v1.csv"),
                     encoding="utf-8").read().strip().splitlines()
    chk("INVENTORY_CSV_ROW_COUNT", ARTIFACT_AGREEMENT, len(csv_lines) - 1, len(VO))
    chk("INVENTORY_CSV_HEADER", ARTIFACT_AGREEMENT,
        csv_lines[0].split(","), D.VISUAL_OBLIGATION_FIELDS)
    inv_md = open(os.path.join(T04, "T04_VISUAL_DIRECTION_INVENTORY_v1.md"),
                  encoding="utf-8").read()
    chk("INVENTORY_MD_CONTAINS_EVERY_OBLIGATION", ARTIFACT_AGREEMENT,
        [i for i in vids if i not in inv_md], [])
    rul_json = json.load(open(os.path.join(T04, "T04_BARIAH_PARTIAL_RULINGS_v1.json"),
                              encoding="utf-8"))
    chk("RULINGS_JSON_MATCHES_DATA", ARTIFACT_AGREEMENT,
        ({d["decision_id"]: d["status"] for d in rul_json["decisions"]},
         len(rul_json["evidence"])),
        ({d["decision_id"]: d["status"] for d in D.DECISIONS}, len(D.EVIDENCE)))
    map_json = json.load(open(os.path.join(T04, "T04_SOURCE_TO_SCREEN_MAPPING_v2.json"),
                              encoding="utf-8"))
    chk("MAPPING_MD_JSON_AGREEMENT", ARTIFACT_AGREEMENT,
        map_json["impact"]["obligations_with_no_home"],
        D.MAPPING_IMPACT["obligations_with_no_home"])
    ct_json = json.load(open(os.path.join(T04, "T04_SCREEN_CONTRACTS_DRAFT_v2.json"),
                             encoding="utf-8"))
    chk("CONTRACTS_MD_JSON_AGREEMENT", ARTIFACT_AGREEMENT,
        [c["contract_id"] for c in ct_json["contracts"]],
        [c["contract_id"] for c in D.CONTRACTS_V2])
    wa = open(os.path.join(T04, "T04_BARIAH_WHATSAPP_FOLLOWUP_DRAFT_v1.md"),
              encoding="utf-8").read()
    chk("WHATSAPP_DRAFT_NOT_SENT", ARTIFACT_AGREEMENT,
        D.WHATSAPP["status"] == "DRAFT_NOT_SENT" and "DRAFT_NOT_SENT" in wa, True)
    chk("WHATSAPP_LISTS_ONLY_UNRESOLVED_ITEMS", ARTIFACT_AGREEMENT, len(D.REMAINING), 6)
    chk("WHATSAPP_STATES_NO_STORYBOARD", ARTIFACT_AGREEMENT,
        "belum dijana" in D.WHATSAPP["text"], True)
    chk("WHATSAPP_STATES_DRAFT_STATUS", ARTIFACT_AGREEMENT,
        "masih draf" in D.WHATSAPP["text"], True)
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, timeout=60).stdout.split()
    except Exception:
        tracked = []
    chk("GIT_INDEX_READ", ARTIFACT_AGREEMENT, len(tracked) > 100, True)
    chk("NO_PPTX_GENERATED", ARTIFACT_AGREEMENT,
        (D.PPTX_GENERATED,
         [t for t in tracked if t.lower().endswith(".pptx") and "/pl06/" in t]), (0, []))
    try:
        gen = subprocess.run(["git", "status", "--porcelain",
                              "reviews/source-completion"], cwd=REPO,
                             capture_output=True, text=True, timeout=60).stdout.strip()
    except Exception:
        gen = ""
    chk("NO_PRODUCTION_GENERATOR_MODIFIED", ARTIFACT_AGREEMENT,
        (gen, D.GENERATOR_TOUCHED), ("", 0))
    chk("VERDICT_IS_ALLOWED", ARTIFACT_AGREEMENT, D.VERDICT in D.ALLOWED_VERDICTS, True)

    # ==================== 12. ACCOUNTING ====================
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
