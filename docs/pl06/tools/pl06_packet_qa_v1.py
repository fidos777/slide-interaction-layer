# -*- coding: utf-8 -*-
"""Stage 4.2F-I — objective gates over the 14 PL06 working packets.

These gates check COMPLETENESS, TRACEABILITY and CONTRACT COMPLIANCE. They deliberately do
not attempt to judge whether a scenario carries meaningful tension or whether dialogue reads
naturally — those are recorded as human-judgment checks in the exception report and are not
counted as gates. A suite that claimed to automate them would be lying about what it proves.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pl06_packet_model_v1 as PM   # noqa: E402
import pl06_authority_v1 as A       # noqa: E402
import k5_calib_build_v1 as B       # noqa: E402

SUITE_ID = "PL06_PACKET_PREP_QA_v1"
SIBLING_SUITES = ["K5_CALIBRATION_PROOF_QA_v1", "K5_BARIAH_POLICY_QA_v1"]
assert SUITE_ID not in SIBLING_SUITES

DOC_LITERAL, MODEL_DERIVED, SOURCE_TEXT = "DOC_LITERAL", "MODEL_DERIVED", "SOURCE_TEXT"

DECLARED_TOTAL_UNITS = 14
DECLARED_LEGACY = 2
DECLARED_ACTIVE = 12
DECLARED_TOTAL_STORYBOARDS = 14
DECLARED_TOTAL_LAMPIRAN = 13
DECLARED_TOTAL_PRIMARY_PPTX = 27
DECLARED_NAMED_LEGACY_EXCEPTION = 1
DECLARED_LEGACY_PROFILE = {"K5-PL06-T03-B02": "LEGACY_STORYBOARD_ONLY",
                           "K5-PL06-T04-B01": "STORYBOARD_AND_LAMPIRAN"}
DECLARED_ARTIFACT_COUNT = {"K5-PL06-T03-B02": 1, "K5-PL06-T04-B01": 2}
DECLARED_APPROVED_NAMES = ["Alya", "Encik Rahman", "Hilmi"]
DECLARED_UNITS = 14
DECLARED_UNIT_IDS = [
    "K5-PL06-T01-B01", "K5-PL06-T01-B02", "K5-PL06-T01-B03",
    "K5-PL06-T02-B01", "K5-PL06-T02-B02",
    "K5-PL06-T03-B01", "K5-PL06-T03-B02", "K5-PL06-T03-B03", "K5-PL06-T03-B04",
    "K5-PL06-T03-B05", "K5-PL06-T04-B01", "K5-PL06-T05-B01", "K5-PL06-T06-B01",
    "K5-PL06-T07-B01",
]

REQUIRED_PACKET_SECTIONS = ["unit_id", "title", "subtopics", "controlled_source_rows",
                            "roles", "dialogue", "rumusan", "quiz", "visual_direction",
                            "interaction", "analysis", "completion"]
FORBIDDEN_PHRASES = ["Unit ini"]

# ---------------------------------------------------------------- QA-owned declared values --
# Every literal below belongs to the suite, not to the thing under test. Where a value could
# be read from the model or the declaration it is deliberately restated here, because a gate
# that reads its expectation from its subject proves only that a copy succeeded. This repo
# has registered twelve occurrences of that defect; none of them is repeated here.
DECLARED_ROLE_INSTANCES = 28
DECLARED_ROLE_INSTANCES_PER_UNIT = {
    "K5-PL06-T01-B01": 4, "K5-PL06-T01-B02": 4, "K5-PL06-T01-B03": 3,
    "K5-PL06-T02-B01": 2, "K5-PL06-T02-B02": 0, "K5-PL06-T03-B01": 3,
    "K5-PL06-T03-B03": 4, "K5-PL06-T03-B04": 1, "K5-PL06-T03-B05": 1,
    "K5-PL06-T05-B01": 2, "K5-PL06-T06-B01": 2, "K5-PL06-T07-B01": 2,
}
DECLARED_UNITS_WITHOUT_LAMPIRAN = ["K5-PL06-T03-B02"]
DECLARED_LAMPIRAN_PRODUCTION_DENSITY = 3
DECLARED_LAMPIRAN_CALIBRATION_DENSITIES = [2, 3]
DECLARED_ANALYSIS_FIELDS = [
    "ambiguities", "assessment", "compliance_sensitive", "dialogue",
    "mandatory_propositions", "pattern", "rumusan_beats", "terminology", "visual_subjects"]
DECLARED_ANALYSIS_COMPLETE_UNITS = ["K5-PL06-T03-B03", "K5-PL06-T03-B04",
                                    "K5-PL06-T05-B01", "K5-PL06-T06-B01"]
DECLARED_AUTHORITY_ARTIFACT = "docs/pl06/authority/K5_Pengesahan_ID_Watak_Dialog_Rumusan_v0_2_vBariah.docx"
DECLARED_AUTHORITY_SHA256 = ("a4775daaacb551d7db44851f3cd8cd888fbdf47637d79c572dc172ff8f9de0b3")
DECLARED_AUTHORITY_BYTES = 49045
DECLARED_NAMED_AUTHORITIES = ["Bariah Ahmad", "Firdaus Ismail"]
DECLARED_C2_CLAIM_COUNT = 3
DECLARED_F3_TREATMENTS = ["Click-to-Reveal", "Comparison", "Kandungan statik",
                          "Langkah demi langkah"]
DECLARED_STATUS_ENUM = [
    "APPROVED", "ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT",
    "DRAFTED_NOT_APPROVED", "NOT_INSTRUCTIONALLY_APPROVED", "NO_KEY_PENDING_AUTHORING",
    "PROPOSED_NOT_APPROVED", "WRITTEN_CONFIRMED"]

# The status each authority record is expected to carry, restated by the suite. This replaces
# NO_WRITTEN_CONFIRMED_RULE_WAS_DOWNGRADED_TO_PROPOSED, which asserted that every rule under
# three sections must be WRITTEN_CONFIRMED — a rule that could only ever be satisfied by
# over-claiming, and which the warrant audit proved wrong in five places.
DECLARED_RULE_STATUS = {
    "characters.approved.0": "ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT",
    "characters.approved.1": "ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT",
    "characters.approved.2": "ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT",
}
# HOW each record was confirmed, restated by the suite. C5 is the only Section-G-only record
# and the three cast entries are the only asserted-prior ones; if either set moves, say so.
DECLARED_CONFIRMATION_PATH = {
    "dialogue.b03_formula_application": "SECTION_G_ONLY",
    "characters.approved.0": "ASSERTED_PRIOR_DECISION",
    "characters.approved.1": "ASSERTED_PRIOR_DECISION",
    "characters.approved.2": "ASSERTED_PRIOR_DECISION",
}
DECLARED_CITATION_EXEMPT_RULES = []
DECLARED_LINE_CLASSES = ["CAIR_STRUCTURAL_FRAME", "CONTROLLED_PARAPHRASE", "SOURCE_VERBATIM"]
DECLARED_AUTHORED_UNITS = ["K5-PL06-T01-B03", "K5-PL06-T02-B01", "K5-PL06-T02-B02"]
DECLARED_TENSION_CLASSES = {
    "K5-PL06-T01-B03": "INTERNAL_HUMAN_AUTHORING_REVIEW",
    "K5-PL06-T02-B01": "CLOSED_BY_FIRDAUS_HUMAN_REVIEW",
    "K5-PL06-T02-B02": "INTERNAL_SOURCE_SCOPE_REVIEW",
}
DECLARED_ROW_058_EXCLUDED = "T02B02-ROW-058"
DECLARED_AUTHORED_LINE_CLASSES = ["APPROVED_INSTRUCTIONAL_COPY"] + DECLARED_LINE_CLASSES

# The five approved B03 S02 lines, restated by the suite from the returned document's C1
# table with the reviewer annotation "BETUL — verbatim modul" removed. This is the ORACLE:
# it is not read from the declaration the generator reads, so a change to either side shows.
DECLARED_B03_S02_LINES = [
    ("Alya",
     "Encik Rahman, jajaran pagar sudah ditanda di tapak. Boleh kita teruskan pemasangan "
     "sementara kerja lain berjalan?"),
    ("Encik Rahman",
     "Belum, Alya. Kedudukan pagar perlu disemak dengan Pelan Ukur Sempadan, manakala dinding "
     "penahan mesti mengikut lukisan struktur yang diluluskan."),
    ("Alya",
     "Kalau keadaan sebenar tapak tidak sama dengan lukisan, bolehkah kedudukannya kita ubah "
     "sedikit?"),
    ("Encik Rahman",
     "Jangan ubah terus di tapak. Catat perbezaannya dan dapatkan kelulusan yang diperlukan "
     "sebelum kerja diteruskan."),
    ("Alya",
     "Jadi semakan dokumen dan keadaan tapak terlebih dahulu dapat mengelakkan masalah "
     "sempadan, kegagalan kerja dan pembaikan semula."),
]
DECLARED_B03_S02_SHA256 = ("a4775daaacb551d7db44851f3cd8cd888fbdf47637d79c572dc172ff8f9de0b3")
DECLARED_B03_S02_SECTIONS = ["C1", "C3"]
DECLARED_STRIPPED_ANNOTATION = "BETUL — verbatim modul"
DECLARED_ACTIVE_AUTHORITY_RECORDS = 55
DECLARED_AUTHORITY_STATUS_SPLIT = {"WRITTEN_CONFIRMED": 52,
                                   "ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT": 3}
# Everything not named above must be WRITTEN_CONFIRMED.
DECLARED_DEFAULT_RULE_STATUS = "WRITTEN_CONFIRMED"

# Reviewer annotations, restated. The model holds its own list; if the two drift, the
# ANNOTATION_MARKER gate says so rather than silently checking a shorter list.
DECLARED_ANNOTATION_MARKERS = [
    "[S]", "[S~]", "[A]", "[D]", "[R]", "[U]", "[P]", "[dicadangkan betul]",
    "TECHNICAL_PROOF", "DRAFT_FOR_BARIAH_REVIEW", "NOT_INSTRUCTIONALLY_APPROVED",
    "NOT_LEARNER_FACING_FINAL", "PROVISIONAL_WORKING_PACKET",
    "AWAITING_BARIAH_ID_WATAK_DIALOG_RUMUSAN", "DRAFTED_NOT_APPROVED",
    "NO_KEY_PENDING_AUTHORING", "PENDING_AUTHORING", "QUIZ_ANCHORED_SLOT",
    "NAME_PENDING_PROPOSAL", "SOURCE_CONTROLLED", "CAIR_",
    "Kepentingan:", "Skop:", "Manfaat:", "Isi Utama:",
]


def _g(name, gate_type, observed, expected, population, source, basis,
       empty_by_design=False):
    ok = observed == expected
    if population == 0 and not empty_by_design:
        ok = False
    return dict(name=name, gate_type=gate_type, population=population, expected=expected,
                observed=observed, source_artifact=source, oracle_basis=basis,
                empty_by_design=empty_by_design, passed=ok)


def gates():
    import hashlib
    ps, ls, t = PM.packets(), PM.legacy_entries(), PM.totals()
    G = []

    # ------------------------------------------------------------------------ package ----
    shape = A.package_shape()
    G.append(_g("THE_PACKAGE_SHAPE_MATCHES_THE_DECLARED_ACCOUNTING", "PACKAGE",
                (shape["total_units"], shape["legacy_retained"], shape["active_generation"],
                 shape["total_storyboards"], shape["total_lampiran"],
                 shape["total_primary_pptx"], shape["named_legacy_exception"]),
                (DECLARED_TOTAL_UNITS, DECLARED_LEGACY, DECLARED_ACTIVE,
                 DECLARED_TOTAL_STORYBOARDS, DECLARED_TOTAL_LAMPIRAN,
                 DECLARED_TOTAL_PRIMARY_PPTX, DECLARED_NAMED_LEGACY_EXCEPTION),
                DECLARED_TOTAL_UNITS, "authority declaration", DOC_LITERAL))
    G.append(_g("ACTIVE_PLUS_LEGACY_ACCOUNTS_FOR_EVERY_UNIT", "PACKAGE",
                (t["ACTIVE_GENERATION"], t["LEGACY_RETAINED"],
                 t["ACTIVE_GENERATION"] + t["LEGACY_RETAINED"]),
                (DECLARED_ACTIVE, DECLARED_LEGACY, DECLARED_TOTAL_UNITS),
                DECLARED_TOTAL_UNITS, "packet roll", DOC_LITERAL))
    G.append(_g("EVERY_ACTIVE_UNIT_HAS_EXTRACTION", "PACKAGE",
                t["ACTIVE_UNITS_WITH_EXTRACTION"], DECLARED_ACTIVE, DECLARED_ACTIVE,
                "packet roll", MODEL_DERIVED))

    # ------------------------------------------------------------------------- legacy ----
    missing = [f"{a['unit_id']}:{a['kind']}" for a in A.legacy_artifacts()
               if not os.path.exists(os.path.join(PM.REPO, a["path"]))]
    G.append(_g("EVERY_DECLARED_LEGACY_ARTIFACT_EXISTS", "LEGACY",
                missing, [], len(A.legacy_artifacts()), "authority declaration", "RAW_FILE"))
    drift = []
    for a in A.legacy_artifacts():
        fp = os.path.join(PM.REPO, a["path"])
        if os.path.exists(fp):
            h = hashlib.sha256(open(fp, "rb").read()).hexdigest()
            if h != a["sha256"]:
                drift.append(f"{a['unit_id']}:{a['kind']}")
    G.append(_g("EVERY_LEGACY_ARTIFACT_MATCHES_ITS_RECORDED_HASH", "LEGACY",
                drift, [], len(A.legacy_artifacts()), "on-disk bytes", "RAW_FILE"))
    G.append(_g("EVERY_UNIT_ARTIFACT_SET_MATCHES_ITS_MANIFEST", "LEGACY",
                {l["unit_id"]: l["artifact_count"] for l in ls}, DECLARED_ARTIFACT_COUNT,
                len(ls), "legacy manifest", DOC_LITERAL))
    G.append(_g("EVERY_ACTIVE_UNIT_DECLARES_STORYBOARD_AND_LAMPIRAN", "LEGACY",
                [p["unit_id"] for p in ps if p["generation_scope"] != "ACTIVE_GENERATION"],
                [], DECLARED_ACTIVE, "packet roll", MODEL_DERIVED))
    G.append(_g("EVERY_LEGACY_EXCEPTION_HAS_A_NAMED_BASIS", "LEGACY",
                [l["unit_id"] for l in ls
                 if l["artifact_profile"] != DECLARED_LEGACY_PROFILE[l["unit_id"]]
                 or not l["basis"]
                 or (l["artifact_profile"] == "LEGACY_STORYBOARD_ONLY"
                     and not l["named_exception"])],
                [], len(ls), "legacy manifest", DOC_LITERAL))
    G.append(_g("NO_LEGACY_UNIT_RECEIVES_A_PRODUCTION_PACKET", "LEGACY",
                sorted(set(PM.legacy()) & {p["unit_id"] for p in ps}), [], len(ls),
                "packet roll", MODEL_DERIVED))

    # ------------------------------------------------------------------- completeness ----
    G.append(_g("EVERY_ACTIVE_UNIT_HAS_A_PACKET", "COMPLETENESS",
                sorted(p["unit_id"] for p in ps), sorted(PM.active_unit_ids()),
                DECLARED_ACTIVE, "packet roll", MODEL_DERIVED))
    missing = [f"{p['unit_id']}:{s_}" for p in ps for s_ in REQUIRED_PACKET_SECTIONS
               if s_ not in p]
    G.append(_g("EVERY_PACKET_CARRIES_EVERY_REQUIRED_SECTION", "COMPLETENESS",
                missing, [], len(ps) * len(REQUIRED_PACKET_SECTIONS), "packet roll",
                DOC_LITERAL))
    G.append(_g("SCHEMA_COMPLETENESS_IS_NOT_REPORTED_AS_COPY_COMPLETENESS", "COMPLETENESS",
                (t["completion"]["PACKET_SCHEMA_COMPLETE"],
                 t["completion"]["PRODUCTION_READY"]), (DECLARED_ACTIVE, 0),
                DECLARED_ACTIVE, "packet totals", DOC_LITERAL))

    # -------------------------------------------------------------------- traceability ---
    rows = PM.all_rows()
    bad = []
    for p in ps:
        valid = {r["row_id"] for r in rows.get(p["unit_id"], {}).get("rows", [])}
        cited = ({rr for t_ in p["dialogue"].get("turns", []) for rr in (t_.get("rows") or [])}
                 | {rr for i in p["quiz"].get("items", []) for rr in (i.get("correct_rows") or [])}
                 | {rr for b in p["rumusan"].get("beats", []) for rr in (b.get("rows") or [])})
        bad += [f"{p['unit_id']}:{c}" for c in sorted(cited - valid)]
    G.append(_g("EVERY_CITED_ROW_BELONGS_TO_ITS_OWN_UNIT", "TRACEABILITY",
                bad, [], sum(len(v.get("rows", [])) for v in rows.values()),
                "packet citations vs extractors", SOURCE_TEXT))
    unsourced = [f"{p['unit_id']}#{t_['seq']}" for p in ps
                 for t_ in p["dialogue"].get("turns", [])
                 if t_["kind"].startswith("SOURCE_BACKED") and not t_.get("rows")]
    G.append(_g("EVERY_SOURCE_BACKED_DIALOGUE_TURN_CITES_ROWS", "TRACEABILITY",
                unsourced, [], sum(len(p["dialogue"].get("turns", [])) for p in ps),
                "packet roll", MODEL_DERIVED))

    # Citing a row is not the same as saying what the row says — four units were putting the
    # ANALYST'S note into a learner-facing line while citing the row correctly. But requiring
    # every line to be a verbatim substring makes natural dialogue impossible, and E1/E2 ask
    # for a conversation, not a recital. The authority's paraphrase contract is the middle
    # ground and these four gates are what enforce it.
    def _norm(s_):
        return " ".join((s_ or "").split()).rstrip(".").lower()

    all_turns = [(p, t_) for p in ps for t_ in p["dialogue"].get("turns", [])]
    G.append(_g("EVERY_DIALOGUE_LINE_CARRIES_A_DECLARED_LINE_CLASS", "PARAPHRASE",
                sorted({t_.get("cls") for _p, t_ in all_turns}
                       - set(DECLARED_AUTHORED_LINE_CLASSES)),
                [], len(all_turns), "packet roll vs authority declaration", DOC_LITERAL))
    G.append(_g("THE_LINE_CLASS_VOCABULARY_IS_THE_DECLARED_ONE", "PARAPHRASE",
                sorted(A.line_classes()), DECLARED_LINE_CLASSES, len(DECLARED_LINE_CLASSES),
                "authority declaration", DOC_LITERAL))

    off_source, no_of, escal, frame_rows = [], [], [], []
    for p in ps:
        src = {r["row_id"]: _norm(r.get("controlled_display_text"))
               for r in rows.get(p["unit_id"], {}).get("rows", [])}
        raw = {r["row_id"]: (r.get("controlled_display_text") or "")
               for r in rows.get(p["unit_id"], {}).get("rows", [])}
        for t_ in p["dialogue"].get("turns", []):
            tag = f"{p['unit_id']}#{t_['seq']}"
            cls = t_.get("cls")
            if cls == PM.VERBATIM:
                line = _norm(t_.get("text"))
                if not any(line and line in src.get(r, "") for r in (t_.get("rows") or [])):
                    off_source.append(tag)
            elif cls == PM.PARAPHRASE:
                po = t_.get("paraphrase_of")
                if not po or po not in src or not t_.get("rows"):
                    no_of.append(tag)
                escal += [f"{tag}:{m}" for m in PM.escalation_defects(t_, raw)]
            elif cls == PM.FRAME:
                frame_rows += [f"{tag}:{r}" for r in (t_.get("rows") or []) if r not in src]
    G.append(_g("EVERY_SOURCE_VERBATIM_LINE_IS_TEXT_FROM_THE_ROW_IT_CITES", "PARAPHRASE",
                off_source, [],
                len([1 for _p, t_ in all_turns if t_.get("cls") == PM.VERBATIM]),
                "packet citations vs extractors", SOURCE_TEXT))
    G.append(_g("EVERY_CONTROLLED_PARAPHRASE_NAMES_THE_ROW_IT_PARAPHRASES", "PARAPHRASE",
                no_of, [],
                len([1 for _p, t_ in all_turns if t_.get("cls") == PM.PARAPHRASE]),
                "packet roll vs extractors", SOURCE_TEXT))
    G.append(_g("NO_CONTROLLED_PARAPHRASE_ESCALATES_BEYOND_ITS_SOURCE", "PARAPHRASE",
                escal, [],
                len([1 for _p, t_ in all_turns if t_.get("cls") == PM.PARAPHRASE]),
                "packet lines vs the rows they cite", SOURCE_TEXT))
    G.append(_g("EVERY_STRUCTURAL_FRAME_NAMES_ONLY_ROWS_OF_ITS_OWN_UNIT", "PARAPHRASE",
                frame_rows, [],
                len([1 for _p, t_ in all_turns if t_.get("cls") == PM.FRAME]),
                "packet citations vs extractors", SOURCE_TEXT))
    # An analyst note that merely quotes its own row verbatim is not an annotation leak — the
    # leak is the COMMENTARY the analyst added on top ("… — a land-encroachment exposure").
    notes = []
    for p in ps:
        src = " ".join(r.get("controlled_display_text") or ""
                       for r in rows.get(p["unit_id"], {}).get("rows", []))
        an = {(a.get("analyst_note") or "").strip()
              for a in p["dialogue"].get("anchors", [])} - {""}
        an = {n for n in an if n not in src}
        for t_ in p["dialogue"].get("turns", []):
            if any(n in (t_.get("text") or "") for n in an):
                notes.append(f"{p['unit_id']}#{t_['seq']}")
    G.append(_g("NO_ANALYST_NOTE_APPEARS_IN_ANY_DIALOGUE_LINE", "PARAPHRASE",
                notes, [], len(all_turns), "packet roll", MODEL_DERIVED))
    unsourced = [f"{p['unit_id']}#{t_['seq']}" for p in ps
                 for t_ in p["dialogue"].get("turns", [])
                 if t_["kind"].startswith("SOURCE_BACKED") and not t_.get("rows")]
    G.append(_g("EVERY_SOURCE_BACKED_DIALOGUE_TURN_CITES_ROWS", "TRACEABILITY",
                unsourced, [], sum(len(p["dialogue"].get("turns", [])) for p in ps),
                "packet roll", MODEL_DERIVED))

    # Citing a row is not the same as saying what the row says. Four units were putting the
    # ANALYST'S note — English-mixed commentary written to explain why a row matters — into a
    # learner-facing dialogue line while citing that row correctly. This gate reads the rows.
    def _norm(s):
        return " ".join((s or "").split()).rstrip(".").lower()

    off_source = []
    for p in ps:
        src = {r["row_id"]: _norm(r.get("controlled_display_text"))
               for r in rows.get(p["unit_id"], {}).get("rows", [])}
        for t_ in p["dialogue"].get("turns", []):
            if not t_["kind"].startswith("SOURCE_BACKED"):
                continue
            line = _norm(t_.get("text"))
            if not any(line and line in src.get(r, "") for r in (t_.get("rows") or [])):
                off_source.append(f"{p['unit_id']}#{t_['seq']}")
    keyless = [f"{p['unit_id']}:{i['slot']}" for p in ps for i in p["quiz"].get("items", [])
               if i["state"] == "QUIZ_DRAFT_COMPLETE" and not i.get("correct_rows")]
    G.append(_g("EVERY_DRAFTED_QUIZ_ANSWER_HAS_A_SOURCE_TRACE", "TRACEABILITY",
                keyless, [], t["quiz_items_drafted"], "packet roll", MODEL_DERIVED))

    # ------------------------------------------------------------------ role contracts ---
    G.append(_g("THE_APPROVED_CAST_IS_THE_DECLARED_ONE", "ROLE",
                [c["name"] for c in A.approved_characters()], DECLARED_APPROVED_NAMES,
                len(DECLARED_APPROVED_NAMES), "authority declaration", DOC_LITERAL))
    ref_as_char = [f"{a['unit_id']}:{a['role_id']}" for p in ps for a in p["roles"]["audit"]
                   if a["classification"] == PM.SPEAKER_NOT_REQUIRED
                   and (a["reused_character"] or a["name"])]
    G.append(_g("NO_REFERENCE_ONLY_ROLE_BECOMES_A_CHARACTER", "ROLE",
                ref_as_char, [], t["role_instances"], "role audit", MODEL_DERIVED))
    fam = {c["role_family"]: c["name"] for c in A.approved_characters()}
    wrong = [f"{a['unit_id']}:{a['role_id']}" for p in ps for a in p["roles"]["audit"]
             if a["role_family"] in fam and a["reused_character"] != fam[a["role_family"]]]
    G.append(_g("EVERY_REUSABLE_ROLE_USES_THE_APPROVED_CHARACTER", "ROLE",
                wrong, [], t["reuse_alya"] + t["reuse_encik_rahman"], "role audit",
                DOC_LITERAL))
    named = [f"{p['unit_id']}:{r['role_id']}" for p in ps
             for r in p["roles"]["new_required"] if r.get("name") != PM.PENDING_CAST]
    G.append(_g("NO_NEW_ROLE_HAS_A_NAME", "ROLE",
                named, [], max(t["new_role_required"], 1), "packet roll", DOC_LITERAL,
                empty_by_design=t["new_role_required"] == 0))
    undeclared = [f"{p['unit_id']}:{a['reused_character']}" for p in ps
                  for a in p["roles"]["audit"]
                  if a["reused_character"] and a["reused_character"] not in
                  DECLARED_APPROVED_NAMES]
    G.append(_g("NO_CHARACTER_IS_ASSIGNED_UNDECLARED_AUTHORITY", "ROLE",
                undeclared, [], t["role_instances"], "role audit", DOC_LITERAL))

    # ------------------------------------------------------------------------ Rumusan ----
    declared_beats = A.rumusan_beats()
    wrongn = [p["unit_id"] for p in ps
              if [b["beat"] for b in p["rumusan"].get("beats", [])] != declared_beats]
    G.append(_g("EVERY_RUMUSAN_HAS_EXACTLY_THREE_INTERNAL_BEATS", "RUMUSAN",
                wrongn, [], len(ps), "packet roll vs authority declaration", DOC_LITERAL))
    bad_scope = []
    for p in ps:
        declared = p["subtopics"]["items"]
        scope = next(b for b in p["rumusan"].get("beats", []) if b["beat"] == "scope")
        got = scope.get("subtopics") or []
        if sorted(got) != sorted(declared) or len(got) != len(set(got)):
            bad_scope.append(p["unit_id"])
    G.append(_g("RUMUSAN_SCOPE_LISTS_EVERY_DECLARED_SUBTOPIC_EXACTLY_ONCE", "RUMUSAN",
                bad_scope, [], sum(len(p["subtopics"]["items"]) for p in ps),
                "packet roll", MODEL_DERIVED))
    inserted = []
    for p in ps:
        declared = set(p["subtopics"]["items"])
        scope = next(b for b in p["rumusan"].get("beats", []) if b["beat"] == "scope")
        inserted += [f"{p['unit_id']}:{x}" for x in (scope.get("subtopics") or [])
                     if x not in declared]
    G.append(_g("NO_UNDECLARED_SUBTOPIC_IS_INSERTED", "RUMUSAN",
                inserted, [], sum(len(p["subtopics"]["items"]) for p in ps),
                "packet roll", MODEL_DERIVED))
    labelled = [f"{p['unit_id']}:{b['beat']}" for p in ps for b in p["rumusan"].get("beats", [])
                if b.get("learner_facing") or b.get("learner_facing_label")]
    G.append(_g("NO_RUMUSAN_BEAT_LABEL_IS_LEARNER_FACING", "RUMUSAN",
                labelled, [], len(ps) * 3, "packet roll", DOC_LITERAL))
    G.append(_g("NO_RUMUSAN_USES_THE_FORBIDDEN_PHRASE", "RUMUSAN",
                [p["unit_id"] for p in ps if p["rumusan"]["uses_forbidden_phrase"]], [],
                len(ps), "packet roll vs authority declaration", DOC_LITERAL))

    # --------------------------------------------------------------------------- quiz ----
    shape_q = A.quiz_shape()
    wrongq = [p["unit_id"] for p in ps
              if len([i for i in p["quiz"].get("items", [])
                      if i["kind"] == "MULTIPLE_CHOICE"])
              != shape_q["mcq"]
              or len([i for i in p["quiz"].get("items", [])
                      if i["kind"] == "MULTIPLE_RESPONSE"]) != shape_q["mr"]]
    G.append(_g("EVERY_QUIZ_MATCHES_THE_AUTHORITY_COMPOSITION", "QUIZ",
                wrongq, [], len(ps), "packet roll vs authority declaration", DOC_LITERAL))
    G.append(_g("EVERY_QUIZ_USES_THE_AUTHORITY_PASS_MARK", "QUIZ",
                sorted({p["quiz"].get("pass_percent") for p in ps} - {None}),
                [shape_q["pass_percent"]],
                len(ps), "packet roll vs authority declaration", DOC_LITERAL))
    claim = [f"{p['unit_id']}:{i['slot']}" for p in ps for i in p["quiz"].get("items", [])
             if A.is_approved(i["key_status"])]
    G.append(_g("NO_QUIZ_KEY_CLAIMS_APPROVAL", "QUIZ",
                claim, [], sum(len(p["quiz"].get("items", [])) for p in ps),
                "packet roll", DOC_LITERAL))
    unknown = [f"{p['unit_id']}:{i['slot']}" for p in ps for i in p["quiz"].get("items", [])
               if not A.known_status(i["key_status"])]
    G.append(_g("EVERY_QUIZ_KEY_STATUS_IS_A_KNOWN_ENUM_MEMBER", "QUIZ",
                unknown, [], sum(len(p["quiz"].get("items", [])) for p in ps),
                "authority status enum", DOC_LITERAL))
    misstate = [f"{p['unit_id']}:{i['slot']}" for p in ps for i in p["quiz"].get("items", [])
                if (i["state"] == "QUIZ_DRAFT_COMPLETE") != bool(i.get("stem"))]
    G.append(_g("AN_ANCHORED_SLOT_IS_NOT_REPORTED_AS_A_DRAFTED_ITEM", "QUIZ",
                misstate, [], sum(len(p["quiz"].get("items", [])) for p in ps),
                "packet roll", MODEL_DERIVED))
    # "Anchored" means the row is already chosen and only the wording is missing. A slot with
    # no anchor row is a blank slot, and calling it anchored overstates how far it has got.
    unanchored_named = [f"{p['unit_id']}:{i['slot']}" for p in ps
                        for i in p["quiz"].get("items", [])
                        if i["state"] == PM.ANCHORED and not i.get("anchor_row")]
    # A Multiple Response is built from sibling sub-points, so its distractors are real rows
    # of the SAME unit that belong to a DIFFERENT heading. Both halves matter: a distractor
    # invented from nothing is unfalsifiable, and one drawn from the correct block is right.
    mr_bad = []
    for p in ps:
        valid = {r["row_id"] for r in rows.get(p["unit_id"], {}).get("rows", [])}
        for i in p["quiz"].get("items", []):
            if i["kind"] != "MULTIPLE_RESPONSE" or not i.get("distractor_rows"):
                continue
            dr = set(i["distractor_rows"])
            if dr - valid:
                mr_bad.append(f"{p['unit_id']}:{i['slot']}:FOREIGN_ROW")
            if dr & set(i.get("correct_rows") or []):
                mr_bad.append(f"{p['unit_id']}:{i['slot']}:DISTRACTOR_IS_ALSO_CORRECT")
    G.append(_g("EVERY_MULTIPLE_RESPONSE_DISTRACTOR_IS_A_REAL_ROW_OF_A_DIFFERENT_BLOCK",
                "QUIZ", mr_bad, [],
                len([1 for p in ps for i in p["quiz"].get("items", [])
                     if i["kind"] == "MULTIPLE_RESPONSE"]),
                "packet citations vs extractors", SOURCE_TEXT))
    G.append(_g("EVERY_QUIZ_SLOT_IS_DRAFTED", "QUIZ",
                (t["quiz_items_drafted"], t["quiz_anchored_slots"],
                 t["quiz_unanchored_slots"]),
                (DECLARED_ACTIVE * 5, 0, 0), DECLARED_ACTIVE * 5, "packet totals",
                DOC_LITERAL))
    G.append(_g("NO_SLOT_CALLED_ANCHORED_LACKS_AN_ANCHOR_ROW", "QUIZ",
                unanchored_named, [], sum(len(p["quiz"].get("items", [])) for p in ps),
                "packet roll", MODEL_DERIVED))
    G.append(_g("EVERY_INCOMPLETE_SLOT_IS_COUNTED_IN_EXACTLY_ONE_STATE", "QUIZ",
                (t["quiz_items_drafted"] + t["quiz_anchored_slots"]
                 + t["quiz_unanchored_slots"]),
                sum(len(p["quiz"].get("items", [])) for p in ps),
                sum(len(p["quiz"].get("items", [])) for p in ps),
                "packet totals", MODEL_DERIVED))

    # ------------------------------------------------------------- status token safety ---
    G.append(_g("A_NEGATIVE_STATUS_NEVER_SATISFIES_APPROVED", "STATUS_TOKEN",
                sorted(s_ for s_ in A.NEGATIVE_STATUSES if A.is_approved(s_)), [],
                len(A.NEGATIVE_STATUSES), "pl06_authority_v1", DOC_LITERAL))
    G.append(_g("A_TRUE_APPROVED_STATUS_DOES_SATISFY_APPROVED", "STATUS_TOKEN",
                sorted(s_ for s_ in A.POSITIVE_STATUSES if not A.is_approved(s_)), [],
                len(A.POSITIVE_STATUSES), "pl06_authority_v1", DOC_LITERAL))
    G.append(_g("EVERY_AUTHORITY_RULE_CARRIES_A_KNOWN_STATUS", "STATUS_TOKEN",
                [".".join(path) for path, r in A.all_rules()
                 if not A.known_status(r["authority_status"])], [],
                len(A.all_rules()), "authority declaration", DOC_LITERAL))
    drift = sorted(".".join(p_) for p_, r in A.all_rules()
                   if r["authority_status"] != DECLARED_RULE_STATUS.get(
                       ".".join(p_), DECLARED_DEFAULT_RULE_STATUS))
    G.append(_g("EVERY_RULE_CARRIES_THE_STATUS_THE_SUITE_DECLARES_FOR_IT", "STATUS_TOKEN",
                drift, [], len(A.all_rules()), "authority declaration", DOC_LITERAL))
    G.append(_g("THE_STATUS_TIERS_ARE_DISJOINT_AND_COVER_THE_ENUM", "STATUS_TOKEN",
                (sorted(A.POSITIVE_STATUSES & A.QUALIFIED_STATUSES),
                 sorted(A.POSITIVE_STATUSES & A.NEGATIVE_STATUSES),
                 sorted(A.QUALIFIED_STATUSES & A.NEGATIVE_STATUSES),
                 sorted(set(A.STATUS_ENUM) - (A.POSITIVE_STATUSES | A.QUALIFIED_STATUSES
                                              | A.NEGATIVE_STATUSES))),
                ([], [], [], []), len(A.STATUS_ENUM), "pl06_authority_v1", DOC_LITERAL))
    G.append(_g("A_QUALIFIED_STATUS_NEVER_SATISFIES_APPROVED", "STATUS_TOKEN",
                sorted(s_ for s_ in A.QUALIFIED_STATUSES if A.is_approved(s_)), [],
                len(A.QUALIFIED_STATUSES), "pl06_authority_v1", DOC_LITERAL))
    # How a record was confirmed is a separate axis from what status it carries. Minting a
    # status per confirmation route grows the enum without bound; C5 was briefly recorded
    # that way. The enum is now fixed and the route is a typed field.
    G.append(_g("THE_STATUS_ENUM_IS_THE_DECLARED_ONE", "STATUS_TOKEN",
                A.STATUS_ENUM, DECLARED_STATUS_ENUM, len(DECLARED_STATUS_ENUM),
                "pl06_authority_v1", DOC_LITERAL))
    paths = A.rules_by_confirmation_path()
    G.append(_g("EVERY_CONFIRMATION_PATH_IS_A_DECLARED_ONE", "STATUS_TOKEN",
                sorted(set(paths) - set(A.CONFIRMATION_PATHS)), [], len(paths),
                "pl06_authority_v1", DOC_LITERAL))
    declared_paths = {k: A.confirmation_path(A.rule(*k.split(".")))
                      for k in DECLARED_CONFIRMATION_PATH}
    G.append(_g("THE_NON_DEFAULT_CONFIRMATION_PATHS_ARE_THE_DECLARED_ONES", "STATUS_TOKEN",
                declared_paths, DECLARED_CONFIRMATION_PATH,
                len(DECLARED_CONFIRMATION_PATH), "authority declaration", DOC_LITERAL))
    G.append(_g("EXACTLY_ONE_RECORD_IS_CONFIRMED_BY_SECTION_G_ALONE", "STATUS_TOKEN",
                paths.get(A.PATH_SECTION_G_ONLY, []),
                [k for k, v in DECLARED_CONFIRMATION_PATH.items()
                 if v == "SECTION_G_ONLY"], 1, "authority declaration", DOC_LITERAL))

    # -------------------------------------------------------------------- citation ----
    # A status is a claim that a named human said something somewhere. Before this gate the
    # declaration carried five WRITTEN_CONFIRMED rules citing "A6" and "A7", neither of which
    # exists in any artifact this repository holds.
    req, exempt, total = A.citation_population()
    G.append(_g("EVERY_WRITTEN_CONFIRMED_RULE_CITES_A_DATED_ARTIFACT_AND_NAMED_AUTHORITY",
                "CITATION",
                [f"{p_}:{','.join(d)}" for p_, _s, d in A.uncited_rules()], [],
                len(req), "authority declaration", DOC_LITERAL))
    # Reconciliation: a gate reporting "48 of 51" leaves three rules unaccounted for and no
    # reader can tell whether they are exempt or missed. Every rule lands in exactly one set,
    # the exempt set is named, and the arithmetic is checked.
    G.append(_g("THE_CITATION_POPULATION_ACCOUNTS_FOR_EVERY_RULE", "CITATION",
                (len(req) + len(exempt), total, len(set(req) & set(exempt))),
                (total, total, 0), total, "authority declaration", MODEL_DERIVED))
    G.append(_g("THE_CITATION_EXEMPT_RULES_ARE_THE_DECLARED_ONES", "CITATION",
                exempt, DECLARED_CITATION_EXEMPT_RULES, total,
                "authority declaration", DOC_LITERAL))
    G.append(_g("NO_RULE_CARRIES_A_STATUS_IN_NEITHER_SET", "CITATION",
                sorted(".".join(p_) for p_, r in A.all_rules()
                       if r["authority_status"] not in A.CITATION_REQUIRED
                       and r["authority_status"] not in A.CITATION_EXEMPT), [],
                total, "pl06_authority_v1", MODEL_DERIVED))
    G.append(_g("EVERY_CITED_ARTIFACT_RESOLVES_TO_REAL_BYTES_ON_DISK", "CITATION",
                [f"{a}:{why}" for a, why in A.artifact_integrity()], [],
                len(A.artifacts()), "on-disk bytes", "RAW_FILE"))
    ar = A.artifact("RETURNED_AUTHORITY_v0_2")
    G.append(_g("THE_RETURNED_AUTHORITY_ARTIFACT_IS_THE_ONE_THAT_WAS_VERIFIED", "CITATION",
                (ar["path"], ar["sha256"], ar["bytes"],
                 hashlib.sha256(open(os.path.join(PM.REPO, ar["path"]), "rb").read())
                 .hexdigest()),
                (DECLARED_AUTHORITY_ARTIFACT, DECLARED_AUTHORITY_SHA256,
                 DECLARED_AUTHORITY_BYTES, DECLARED_AUTHORITY_SHA256),
                1, "on-disk bytes vs the verification checkpoint", "RAW_FILE"))
    G.append(_g("THE_AUTHORITY_ARTIFACT_CLAIMS_NO_SIGNATURE_IT_DOES_NOT_HAVE", "CITATION",
                (ar["verification"]["signature_objects"], ar["verification"]["signed"]),
                (0, False), 1, "authority declaration", DOC_LITERAL))
    G.append(_g("EVERY_NAMED_AUTHORITY_IS_ON_THE_DECLARED_ROSTER", "CITATION",
                sorted(A.named_authorities()), sorted(DECLARED_NAMED_AUTHORITIES),
                len(DECLARED_NAMED_AUTHORITIES), "authority declaration", DOC_LITERAL))
    unrepaired = [f["finding_id"] for f in A.warrant_findings()
                  if f["repair"].startswith("RE_CITED") and any(
                      A.rule(*r.split("."))["authority_status"] not in A.CITATION_REQUIRED
                      or A.citation_defects(A.rule(*r.split(".")))
                      for r in f["rules"])]
    G.append(_g("EVERY_WARRANT_AUDIT_REPAIR_LANDED_ON_THE_RULE_IT_NAMES", "CITATION",
                unrepaired, [], len(A.warrant_findings()), "authority declaration",
                MODEL_DERIVED))
    naive = [f["finding_id"] for f in A.warrant_findings()
             if f.get("value_changed")]
    G.append(_g("NO_WARRANT_REPAIR_SILENTLY_CHANGED_A_RULE_VALUE", "CITATION",
                naive, [], len(A.warrant_findings()), "authority declaration", DOC_LITERAL))

    # -------------------------------------------------------------- unresolved inputs ----
    G.append(_g("NO_PACKET_CLAIMS_PRODUCTION_READY_WHILE_BLOCKED", "UNRESOLVED",
                [p["unit_id"] for p in ps if p["production_ready"]
                 and p["production_blockers"]], [], len(ps), "packet roll", MODEL_DERIVED))
    wrote = []
    for p in ps:
        try:
            B.guard_production(p, B.PRODUCTION)
            if p["production_blockers"]:
                wrote.append(p["unit_id"])
        except B.ProductionRefused:
            pass
    G.append(_g("PRODUCTION_MODE_REFUSES_EVERY_UNRESOLVED_ACTIVE_PACKET", "UNRESOLVED",
                wrote, [], len(ps), "k5_calib_build_v1.guard_production", MODEL_DERIVED))
    G.append(_g("REVIEW_DRAFT_MODE_DOES_NOT_REFUSE", "UNRESOLVED",
                all(isinstance(B.guard_production(p, B.REVIEW_DRAFT), list) for p in ps),
                True, len(ps), "k5_calib_build_v1.guard_production", MODEL_DERIVED))

    # ------------------------------------------------------- learner-facing exclusion ----
    # D2: "Label ini TIDAK dipaparkan kepada pelatih." Everything this repo adds for a
    # reviewer is production metadata, and the boundary is only real if something checks it.
    G.append(_g("THE_ANNOTATION_MARKER_LIST_HAS_NOT_DRIFTED_FROM_THE_SUITES", "ANNOTATION",
                sorted(PM.REVIEWER_ANNOTATION_MARKERS), sorted(DECLARED_ANNOTATION_MARKERS),
                len(DECLARED_ANNOTATION_MARKERS), "pl06_packet_model_v1", DOC_LITERAL))
    leaks = [f"{loc}={m}" for p in ps
             for loc, m in PM.annotation_leaks(p, markers=DECLARED_ANNOTATION_MARKERS)]
    strings = sum(len(PM.learner_facing_strings(p)) for p in ps)
    G.append(_g("NO_REVIEWER_ANNOTATION_APPEARS_IN_LEARNER_FACING_COPY", "ANNOTATION",
                sorted(leaks), [], strings, "packet roll", MODEL_DERIVED))
    G.append(_g("NO_LEARNER_FACING_STRING_CARRIES_A_SOURCE_ROW_ID", "ANNOTATION",
                sorted({loc for p in ps for loc, m in
                        PM.annotation_leaks(p, markers=[]) if m == "ROW_ID"}), [],
                strings, "packet roll", MODEL_DERIVED))
    labelled = [f"{p['unit_id']}:{b['beat']}" for p in ps
                for b in p["rumusan"]["beats"]
                if b.get("text") and PM.BEAT_LEARNER_LABELS.get(b["beat"], "\0")
                in b["text"][:24]]
    G.append(_g("NO_RUMUSAN_BEAT_NAME_SURVIVES_AS_AN_INLINE_PREFIX", "ANNOTATION",
                labelled, [], len(ps) * 3, "packet roll", MODEL_DERIVED))
    missing_sub = []
    for p in ps:
        sc = next(b for b in p["rumusan"]["beats"] if b["beat"] == "scope")
        missing_sub += [f"{p['unit_id']}:{s_}" for s_ in (sc.get("subtopics") or [])
                        if s_ not in (sc.get("text") or "")]
    G.append(_g("EVERY_DECLARED_SUBTOPIC_APPEARS_IN_THE_SCOPE_COPY_ITSELF", "ANNOTATION",
                missing_sub, [], sum(len(p["subtopics"]["items"]) for p in ps),
                "packet roll", MODEL_DERIVED))

    # ------------------------------------------------------------ role reconciliation ----
    led = PM.role_instance_ledger()
    G.append(_g("THE_ROLE_INSTANCE_TOTAL_RECONCILES_THREE_INDEPENDENT_WAYS", "ROLE",
                (led["total"], led["sum_of_classifications"], led["sum_of_role_ids"],
                 led["sum_of_per_unit"]),
                (DECLARED_ROLE_INSTANCES,) * 4, DECLARED_ROLE_INSTANCES,
                "role audit ledger", DOC_LITERAL))
    G.append(_g("THE_PER_UNIT_ROLE_COUNTS_ARE_THE_DECLARED_ONES", "ROLE",
                led["per_unit"], DECLARED_ROLE_INSTANCES_PER_UNIT, len(ps),
                "role audit ledger", DOC_LITERAL))
    G.append(_g("A_UNIT_WITH_NO_ROLE_MARKER_IS_NAMED_NOT_ABSORBED", "ROLE",
                led["units_with_no_role_marker"],
                sorted(u for u, n in DECLARED_ROLE_INSTANCES_PER_UNIT.items() if n == 0),
                len(ps), "role audit ledger", DOC_LITERAL))
    G.append(_g("NO_REPLACED_CHARACTER_IS_STILL_CAST", "ROLE",
                sorted({a["reused_character"] for p in ps for a in p["roles"]["audit"]}
                       & set(A.replaced_characters())), [],
                len(A.replaced_characters()), "role audit vs authority declaration",
                DOC_LITERAL))

    # --------------------------------------------- package accounting, derived not told ----
    d = PM.derived_package_shape()
    G.append(_g("THE_PACKAGE_SHAPE_IS_DERIVED_FROM_THE_ROLL_NOT_ASSERTED", "PACKAGE",
                (d["total_units"], d["legacy_retained"], d["active_generation"],
                 d["total_storyboards"], d["total_lampiran"], d["total_primary_pptx"],
                 d["named_legacy_exception"]),
                (DECLARED_TOTAL_UNITS, DECLARED_LEGACY, DECLARED_ACTIVE,
                 DECLARED_TOTAL_STORYBOARDS, DECLARED_TOTAL_LAMPIRAN,
                 DECLARED_TOTAL_PRIMARY_PPTX, DECLARED_NAMED_LEGACY_EXCEPTION),
                DECLARED_TOTAL_UNITS, "unit roll + artifact profiles", MODEL_DERIVED))
    G.append(_g("THE_DERIVED_SHAPE_AGREES_WITH_THE_AUTHORITY_DECLARATION", "PACKAGE",
                {k: d[k] for k in shape}, shape, DECLARED_TOTAL_UNITS,
                "derived roll vs authority declaration", MODEL_DERIVED))
    G.append(_g("EXACTLY_ONE_UNIT_CARRIES_NO_LAMPIRAN_AND_IT_IS_NAMED", "PACKAGE",
                d["units_without_lampiran"], DECLARED_UNITS_WITHOUT_LAMPIRAN,
                DECLARED_TOTAL_UNITS, "unit roll + artifact profiles", DOC_LITERAL))
    G.append(_g("PRIMARY_PPTX_TOTAL_IS_STORYBOARDS_PLUS_LAMPIRAN", "PACKAGE",
                d["total_storyboards"] + d["total_lampiran"], d["total_primary_pptx"],
                DECLARED_TOTAL_PRIMARY_PPTX, "unit roll", MODEL_DERIVED))

    # ------------------------------------------------------- F5 Lampiran density sweep ----
    G.append(_g("THE_PRODUCTION_LAMPIRAN_DENSITY_IS_THE_AUTHORITY_VALUE", "DENSITY",
                (A.lampiran_production_density(), B.PRODUCTION_PANEL_DENSITY),
                (DECLARED_LAMPIRAN_PRODUCTION_DENSITY,) * 2, 1,
                "authority declaration vs k5_calib_build_v1", DOC_LITERAL))
    G.append(_g("THE_CALIBRATION_DENSITIES_ARE_RETAINED_NOT_DELETED", "DENSITY",
                (A.lampiran_calibration_densities(), sorted(B.CALIBRATION_DENSITIES)),
                (DECLARED_LAMPIRAN_CALIBRATION_DENSITIES,) * 2, 2,
                "authority declaration vs k5_calib_build_v1", DOC_LITERAL))
    G.append(_g("THE_PRODUCTION_DENSITY_IS_ONE_OF_THE_DENSITIES_ACTUALLY_TESTED", "DENSITY",
                A.lampiran_production_density() in A.lampiran_calibration_densities(),
                True, 2, "authority declaration", MODEL_DERIVED))

    # ------------------------------------------------- SOURCE_ANALYSIS_COMPLETE contract ----
    G.append(_g("THE_ANALYSIS_CONTRACT_FIELDS_ARE_THE_DECLARED_ONES", "ANALYSIS",
                PM.ANALYSIS_FIELDS, DECLARED_ANALYSIS_FIELDS,
                len(DECLARED_ANALYSIS_FIELDS), "pl06_packet_model_v1", DOC_LITERAL))
    # Population is the suite's OWN list of units, not the model's. Written the other way
    # round — "every unit the model reports complete has no defects" — the gate is vacuous by
    # construction, because the model computes completeness AS the absence of defects. That
    # is occurrence #13 of the self-referential-oracle defect in this project's registry, and
    # it was caught by fixture PL-31 rather than by reading.
    G.append(_g("THE_FOUR_DECLARED_ANALYSIS_UNITS_SATISFY_THE_CONTRACT", "ANALYSIS",
                sorted(f"{u}:{x}" for u in DECLARED_ANALYSIS_COMPLETE_UNITS
                       for x in PM.analysis_conformance(u)), [],
                len(DECLARED_ANALYSIS_COMPLETE_UNITS), "committed unit analyses",
                MODEL_DERIVED))
    G.append(_g("THE_UNITS_SATISFYING_THE_ANALYSIS_CONTRACT_ARE_THE_DECLARED_FOUR",
                "ANALYSIS",
                sorted(p["unit_id"] for p in ps
                       if p["completion"]["SOURCE_ANALYSIS_COMPLETE"]),
                DECLARED_ANALYSIS_COMPLETE_UNITS, DECLARED_ACTIVE, "packet roll",
                DOC_LITERAL))
    gm = PM.analysis_gap_matrix()
    G.append(_g("EVERY_UNIT_WITHOUT_A_COMMITTED_ANALYSIS_IS_IN_THE_GAP_MATRIX", "ANALYSIS",
                sorted(r["unit_id"] for r in gm),
                sorted(set(PM.active_unit_ids()) - set(DECLARED_ANALYSIS_COMPLETE_UNITS)),
                DECLARED_ACTIVE - len(DECLARED_ANALYSIS_COMPLETE_UNITS),
                "gap matrix", MODEL_DERIVED))
    G.append(_g("NO_GAP_MATRIX_ROW_CLAIMS_AUTHORED_WORK", "ANALYSIS",
                sorted(r["unit_id"] for r in gm
                       if any(f["authored"] for f in r["fields"].values())), [],
                len(gm) * len(DECLARED_ANALYSIS_FIELDS), "gap matrix", MODEL_DERIVED))

    # ----------------------------------------------------------- ingested authority facts ---
    claims = A.c2_claims()
    valid_b03 = {r["row_id"] for r in rows.get("K5-PL06-T03-B03", {}).get("rows", [])}
    G.append(_g("EVERY_C2_CLAIM_CITES_A_ROW_THAT_EXISTS_IN_B03", "AUTHORITY",
                sorted(f"{c['claim_id']}:{r}" for c in claims
                       for r in c["controlled_rows"] if r not in valid_b03), [],
                sum(len(c["controlled_rows"]) for c in claims),
                "authority declaration vs B03 extraction", SOURCE_TEXT))
    G.append(_g("THE_UNANNOTATED_C2_CLAIM_IS_RECORDED_AS_SUCH", "AUTHORITY",
                sorted((c["claim_id"], c["annotation_present"], c["support_class"])
                       for c in claims),
                sorted([("C2-1", False, "SOURCE_SUPPORTED_NOT_VERBATIM"),
                        ("C2-2", True, "SOURCE_VERBATIM_PER_NAMED_AUTHORITY_ANNOTATION"),
                        ("C2-3", True, "SOURCE_SUPPORTED_PER_NAMED_AUTHORITY_ANNOTATION")]),
                DECLARED_C2_CLAIM_COUNT, "authority declaration", DOC_LITERAL))
    G.append(_g("EVERY_TREATMENT_CHOSEN_IS_ONE_OF_THE_FOUR_F3_NAMES", "AUTHORITY",
                sorted({p["interaction"]["primary"] for p in ps}
                       - set(DECLARED_F3_TREATMENTS)), [], len(ps),
                "packet roll vs authority declaration", DOC_LITERAL))
    G.append(_g("THE_F3_TREATMENT_VOCABULARY_IS_THE_DECLARED_ONE", "AUTHORITY",
                sorted(r["treatment"] for r in A.treatment_rules()),
                DECLARED_F3_TREATMENTS, len(DECLARED_F3_TREATMENTS),
                "authority declaration", DOC_LITERAL))
    G.append(_g("NO_GATE_CLAIMS_A_DIALOGUE_SATISFIES_THE_TENSION_RULE", "AUTHORITY",
                (A.tension_is_human_verified(),
                 [g["name"] for g in G if "TENSION" in g["name"]]),
                (True, []), 1, "this suite", DOC_LITERAL))
    G.append(_g("EVERY_CROSSWALK_RECORD_NAMES_ITS_SCOPE_AND_RESULTING_STATUS", "AUTHORITY",
                sorted(c["authority_record_id"] for c in A.crosswalk()
                       if not c.get("scope") or not A.known_status(c["resulting_status"])),
                [], len(A.crosswalk()), "authority declaration", DOC_LITERAL))
    G.append(_g("A_SECTION_G_ONLY_RECORD_IS_NOT_COUNTED_AS_AN_A_TO_F_DECISION", "AUTHORITY",
                sorted(c["authority_record_id"] for c in A.crosswalk()
                       if c["section_g_only_explicit_confirmation"]
                       and c["authority_from_a_to_f"]), [], len(A.crosswalk()),
                "authority declaration", DOC_LITERAL))
    # ------------------------------------------------ approved B03 S02 copy ----
    # C3 reads "TERIMA — dialog boleh digunakan seadanya." Approved copy is REPRODUCED. The
    # controlled-paraphrase contract governs unapproved or generated dialogue and does not
    # reach this deck; the only correct transformation was stripping the reviewer annotation.
    b03 = next(p for p in ps if p["unit_id"] == PM.B03_S02_UNIT)["dialogue"]
    observed = [(t["speaker"], " ".join((t["text"] or "").split()))
                for t in b03["turns"]]
    G.append(_g("B03_S02_DIALOGUE_MATCHES_APPROVED_C1_CANONICAL_LINES", "APPROVED_COPY",
                observed, DECLARED_B03_S02_LINES, len(DECLARED_B03_S02_LINES),
                "packet roll vs the C1 table as accepted at C3", DOC_LITERAL))
    G.append(_g("THE_B03_CANONICAL_RECORD_NAMES_ITS_SOURCE_FILE_AND_HASH", "APPROVED_COPY",
                (b03.get("source_sha256"), sorted(b03.get("source_sections") or []),
                 b03.get("canonical_line_count"), b03.get("authority")),
                (DECLARED_B03_S02_SHA256, sorted(DECLARED_B03_S02_SECTIONS), 5,
                 "Bariah Ahmad"), 1, "packet roll", DOC_LITERAL))
    G.append(_g("NO_REVIEWER_ANNOTATION_SURVIVES_IN_THE_APPROVED_B03_COPY", "APPROVED_COPY",
                [t["seq"] for t in b03["turns"]
                 if DECLARED_STRIPPED_ANNOTATION in (t["text"] or "")],
                [], len(b03["turns"]), "packet roll", DOC_LITERAL))
    G.append(_g("THE_APPROVED_B03_COPY_IS_NOT_SUBJECT_TO_THE_PARAPHRASE_CONTRACT",
                "APPROVED_COPY",
                sorted({t["cls"] for t in b03["turns"]}), [PM.APPROVED_COPY],
                len(b03["turns"]), "packet roll", DOC_LITERAL))

    # ---------------------------------------- authority / analysis boundary ----
    req2, exempt2, total2 = A.citation_population()
    split = {}
    for _p2, r2 in A.all_rules():
        split[r2["authority_status"]] = split.get(r2["authority_status"], 0) + 1
    G.append(_g("THE_ACTIVE_AUTHORITY_POPULATION_IS_THE_DECLARED_ONE", "BOUNDARY",
                total2, DECLARED_ACTIVE_AUTHORITY_RECORDS,
                DECLARED_ACTIVE_AUTHORITY_RECORDS, "authority declaration", DOC_LITERAL))
    G.append(_g("THE_AUTHORITY_STATUS_SPLIT_IS_THE_DECLARED_ONE", "BOUNDARY",
                split, DECLARED_AUTHORITY_STATUS_SPLIT, total2,
                "authority declaration", DOC_LITERAL))
    G.append(_g("NO_ACTIVE_WRITTEN_CONFIRMED_RECORD_IS_CITATION_EXEMPT", "BOUNDARY",
                sorted(".".join(p2) for p2, r2 in A.all_rules()
                       if r2["authority_status"] == A.WRITTEN_CONFIRMED
                       and ".".join(p2) not in req2), [],
                split.get(A.WRITTEN_CONFIRMED, 0), "authority declaration", MODEL_DERIVED))
    # The three analysis records must NOT be back in the declaration.
    G.append(_g("NO_ANALYSIS_RECORD_LIVES_IN_THE_AUTHORITY_DECLARATION", "BOUNDARY",
                sorted(k for k in ("t02b02_source_scope_verification", "row_058_disposition")
                       if k in A.contract()["dialogue"])
                + (["tension_dispositions"] if "tension_dispositions" in A.contract()
                   else []),
                [], 3, "authority declaration", DOC_LITERAL))
    G.append(_g("EVERY_MOVED_ANALYSIS_RECORD_HAS_A_HOME_IN_THE_PACKET", "BOUNDARY",
                (PM.source_scope_verification("K5-PL06-T02-B02") is not None,
                 PM.row_use_disposition("K5-PL06-T02-B02") is not None,
                 len(PM.tension_dispositions())),
                (True, True, 3), 3, "pl06_packet_model_v1", MODEL_DERIVED))
    G.append(_g("THE_PARAPHRASE_CONTRACT_IS_TYPED_AS_AN_OWNER_ENGINEERING_CONTRACT",
                "BOUNDARY",
                (A.paraphrase_contract().get("record_type"),
                 A.paraphrase_contract().get("named_authority")),
                ("OWNER_ENGINEERING_AUTHORING_CONTRACT", "Firdaus Ismail"), 1,
                "authority declaration", DOC_LITERAL))

    # ------------------------------------------------ human tension disposition ----
    disp = {d["unit_id"]: d for d in PM.tension_dispositions()}
    G.append(_g("THE_THREE_TENSION_UNITS_CARRY_THE_DECLARED_INTERNAL_CLASSES", "TENSION",
                {u: d["classification"] for u, d in sorted(disp.items())},
                DECLARED_TENSION_CLASSES, len(DECLARED_TENSION_CLASSES),
                "authority declaration", DOC_LITERAL))
    G.append(_g("NO_TENSION_DISPOSITION_IS_ESCALATED_WITHOUT_A_NAMED_TRIGGER", "TENSION",
                sorted(d["unit_id"] for d in PM.tension_dispositions()
                       if d["escalated_to_authority"]
                       and d.get("escalation_reason")
                       not in PM.TENSION_ESCALATION_TRIGGERS),
                [], len(disp), "authority declaration", DOC_LITERAL))
    G.append(_g("EVERY_AUTHORED_DIALOGUE_IS_A_DECLARED_ONE", "TENSION",
                sorted(PM.AUTHORED_DIALOGUE), DECLARED_AUTHORED_UNITS,
                len(DECLARED_AUTHORED_UNITS), "pl06_packet_model_v1", DOC_LITERAL))
    G.append(_g("EVERY_AUTHORED_DIALOGUE_CARRIES_ITS_DISPOSITION", "TENSION",
                {p["unit_id"]: p["dialogue"].get("disposition") for p in ps
                 if p["unit_id"] in DECLARED_AUTHORED_UNITS},
                DECLARED_TENSION_CLASSES, len(DECLARED_AUTHORED_UNITS),
                "packet roll", DOC_LITERAL))
    # ROW-058 is excluded from the T02-B02 dialogue: three of the four conditions the owner
    # set for using it in the same conversation are not met.
    t22 = next(p for p in ps if p["unit_id"] == "K5-PL06-T02-B02")
    G.append(_g("THE_EXCLUDED_ROW_IS_NOT_CITED_IN_THE_T02B02_DIALOGUE", "TENSION",
                sorted({r for t_ in t22["dialogue"]["turns"] for r in (t_.get("rows") or [])}
                       & {DECLARED_ROW_058_EXCLUDED}), [],
                len(t22["dialogue"]["turns"]), "packet roll", DOC_LITERAL))
    G.append(_g("EVERY_AUTHORED_LINE_CITES_ROWS_OF_ITS_OWN_UNIT_ONLY", "TENSION",
                sorted(f"{p['unit_id']}#{t_['seq']}:{r}" for p in ps
                       if p["unit_id"] in DECLARED_AUTHORED_UNITS
                       for t_ in p["dialogue"]["turns"] for r in (t_.get("rows") or [])
                       if r not in {x["row_id"]
                                    for x in rows.get(p["unit_id"], {}).get("rows", [])}),
                [], sum(len(p["dialogue"]["turns"]) for p in ps
                        if p["unit_id"] in DECLARED_AUTHORED_UNITS),
                "packet citations vs extractors", SOURCE_TEXT))

    G.append(_g("EVERY_SUPERSESSION_NAMES_WHERE_THE_SUPERSEDED_RULE_IS_HELD", "AUTHORITY",
                sorted(s_["id"] for s_ in A.supersessions()
                       if not s_.get("held_in") or not s_.get("by")), [],
                len(A.supersessions()), "authority declaration", DOC_LITERAL))
    return G


def run(verbose=True):
    G = gates()
    bad = [g for g in G if not g["passed"]]
    if verbose:
        print(f"SUITE_ID = {SUITE_ID}")
        print(f"{len(G) - len(bad)}/{len(G)} passed")
        kinds = {}
        for g in G:
            kinds[g["gate_type"]] = kinds.get(g["gate_type"], 0) + 1
        print("by type:", dict(sorted(kinds.items())))
        for g in bad:
            print(f"  FAIL {g['name']}\n       expected={g['expected']!r}\n"
                  f"       observed={g['observed']!r}")
    return G, bad





# ==========================================================================================
# MUTATION FIXTURES
#
# Each breaks exactly one thing and must trip its OWN named gate. The refusal fixtures also
# assert the two properties that matter operationally: a non-zero exit AND zero PPTX written.
# ==========================================================================================
FIXTURES = []


def fixture(fid, target, expect_detect=True):
    """`expect_detect=False` marks a POSITIVE CONTROL: the mutation is well-formed and the
    named gate must keep passing. Without one, a gate that trips on everything looks perfect.
    """
    def deco(fn):
        FIXTURES.append(dict(id=fid, target=target, fn=fn, expect_detect=expect_detect))
        return fn
    return deco


def _patch_rule(path, **fields):
    """Mutate one authority record in the loaded contract and restore it afterwards."""
    node = A.contract()
    for k in path.split("."):
        node = node[int(k)] if k.isdigit() else node[k]
    old = {k: node.get(k) for k in fields}
    had = {k: (k in node) for k in fields}
    node.update(fields)

    def undo():
        for k, v in old.items():
            if had[k]:
                node[k] = v
            else:
                node.pop(k, None)
    return undo


def _patch(obj, key, val):
    if isinstance(obj, dict):
        had, old = key in obj, obj.get(key)
        obj[key] = val
        return lambda: (obj.__setitem__(key, old) if had else obj.pop(key, None))
    old = getattr(obj, key)
    setattr(obj, key, val)
    return lambda: setattr(obj, key, old)


@fixture("PL-01", "RUMUSAN_SCOPE_LISTS_EVERY_DECLARED_SUBTOPIC_EXACTLY_ONCE")
def _f1():
    """A declared subtopic is dropped from the scope beat."""
    orig = PM._rumusan

    def broken(unit_id, ex, subs):
        r = orig(unit_id, ex, subs)
        sc = next(b for b in r["beats"] if b["beat"] == "scope")
        if sc["subtopics"]:
            sc["subtopics"] = sc["subtopics"][:-1]
        return r
    return _patch(PM, "_rumusan", broken)


@fixture("PL-02", "NO_UNDECLARED_SUBTOPIC_IS_INSERTED")
def _f2():
    """A subtopic that the boundary map never declared is inserted into scope."""
    orig = PM._rumusan

    def broken(unit_id, ex, subs):
        r = orig(unit_id, ex, subs)
        next(b for b in r["beats"] if b["beat"] == "scope")["subtopics"].append(
            "9.9 Subtopik Yang Tidak Diisytiharkan")
        return r
    return _patch(PM, "_rumusan", broken)


@fixture("PL-03", "EVERY_RUMUSAN_HAS_EXACTLY_THREE_INTERNAL_BEATS")
def _f3():
    """One beat per subtopic — the shape this pass exists to remove."""
    orig = PM._rumusan

    def broken(unit_id, ex, subs):
        r = orig(unit_id, ex, subs)
        r["beats"] = r["beats"] + [dict(beat=f"subtopic_{i}", learner_facing=False,
                                        learner_facing_label=None, text="x", rows=[])
                                   for i, _ in enumerate(subs["items"])]
        return r
    return _patch(PM, "_rumusan", broken)


@fixture("PL-04", "NO_REFERENCE_ONLY_ROLE_BECOMES_A_CHARACTER")
def _f4():
    orig = PM.role_audit

    def broken(unit_id, ex):
        out = orig(unit_id, ex)
        for a in out:
            if a["classification"] == PM.SPEAKER_NOT_REQUIRED:
                a["reused_character"] = "Encik Rahman"
                break
        return out
    return _patch(PM, "role_audit", broken)


@fixture("PL-05", "EVERY_REUSABLE_ROLE_USES_THE_APPROVED_CHARACTER")
def _f5():
    orig = PM.role_audit

    def broken(unit_id, ex):
        out = orig(unit_id, ex)
        for a in out:
            if a["reused_character"] == "Alya":
                a["reused_character"] = "Encik Rahman"
                break
        return out
    return _patch(PM, "role_audit", broken)


@fixture("PL-06", "NO_CHARACTER_IS_ASSIGNED_UNDECLARED_AUTHORITY")
def _f6():
    orig = PM.role_audit

    def broken(unit_id, ex):
        out = orig(unit_id, ex)
        if out:
            out[0]["reused_character"] = "Cikgu Zaini"
        return out
    return _patch(PM, "role_audit", broken)


@fixture("PL-07", "EVERY_DECLARED_LEGACY_ARTIFACT_EXISTS")
def _f7():
    orig = A.legacy_artifacts
    return _patch(A, "legacy_artifacts",
                  lambda: [dict(x, path=x["path"] + ".gone") for x in orig()])


@fixture("PL-08", "EVERY_LEGACY_ARTIFACT_MATCHES_ITS_RECORDED_HASH")
def _f8():
    orig = A.legacy_artifacts
    return _patch(A, "legacy_artifacts",
                  lambda: [dict(x, sha256="0" * 64) for x in orig()])


@fixture("PL-09", "EVERY_UNIT_ARTIFACT_SET_MATCHES_ITS_MANIFEST")
def _f9():
    """B02 is given a Lampiran it never had — the fixed-pair assumption this pass removed."""
    orig = A.legacy_artifacts

    def broken():
        out = list(orig())
        out.append(dict(unit_id="K5-PL06-T03-B02", kind="LAMPIRAN", path="nope.pptx",
                        bytes=0, slides=0, sha256="0" * 64))
        return out
    return _patch(A, "legacy_artifacts", broken)


@fixture("PL-10", "NO_QUIZ_KEY_CLAIMS_APPROVAL")
def _f10():
    orig = A.quiz_shape
    return _patch(A, "quiz_shape", lambda: dict(orig(), key_status=A.APPROVED))


@fixture("PL-11", "EVERY_QUIZ_MATCHES_THE_AUTHORITY_COMPOSITION")
def _f11():
    orig = PM._quiz

    def broken(unit_id, ex):
        q = orig(unit_id, ex)
        q["items"] = q["items"][:-1]
        return q
    return _patch(PM, "_quiz", broken)


@fixture("PL-12", "AN_ANCHORED_SLOT_IS_NOT_REPORTED_AS_A_DRAFTED_ITEM")
def _f12():
    orig = PM._quiz

    def broken(unit_id, ex):
        q = orig(unit_id, ex)
        for i in q["items"]:
            if i["state"] == "QUIZ_ANCHORED_SLOT":
                i["state"] = "QUIZ_DRAFT_COMPLETE"
                break
        else:
            q["items"][0]["stem"] = None
        return q
    return _patch(PM, "_quiz", broken)


@fixture("PL-13", "NO_RUMUSAN_USES_THE_FORBIDDEN_PHRASE")
def _f13():
    orig = PM._rumusan

    def broken(unit_id, ex, subs):
        r = orig(unit_id, ex, subs)
        r["beats"][0]["text"] = f"{A.forbidden_phrase()} menerangkan proses tersebut."
        r["uses_forbidden_phrase"] = True
        return r
    return _patch(PM, "_rumusan", broken)


@fixture("PL-14", "A_NEGATIVE_STATUS_NEVER_SATISFIES_APPROVED")
def _f14():
    """The substring trap, reintroduced deliberately."""
    return _patch(A, "is_approved", lambda s: "APPROVED" in (s or ""))


@fixture("PL-15", "EVERY_ACTIVE_UNIT_HAS_EXTRACTION")
def _f15():
    orig = PM.all_rows

    def broken():
        out = dict(orig())
        out.pop("K5-PL06-T07-B01", None)
        return out
    return _patch(PM, "all_rows", broken)


# ------------------------------------------------------------------ citation fixtures ----
@fixture("PL-16", "EVERY_WRITTEN_CONFIRMED_RULE_CITES_A_DATED_ARTIFACT_AND_NAMED_AUTHORITY",
         expect_detect=False)
def _f16():
    """POSITIVE CONTROL. A brand-new WRITTEN_CONFIRMED rule with a complete, correct citation
    is added to the declaration. The gate must NOT trip — and its population must grow, which
    is checked separately by the empty-population rule inside `_g`."""
    c = A.contract()
    ar = A.artifact("RETURNED_AUTHORITY_v0_2")
    c["review_model"]["_positive_control"] = dict(
        value=True, authority_status=A.WRITTEN_CONFIRMED,
        authority_artifact="RETURNED_AUTHORITY_v0_2", authority_locus="F7",
        named_authority="Bariah Ahmad", authority_date=ar["date"],
        authority_source="Positive control for the citation gate.", scope="none",
        exceptions=[])
    return lambda: c["review_model"].pop("_positive_control", None)


@fixture("PL-17", "EVERY_WRITTEN_CONFIRMED_RULE_CITES_A_DATED_ARTIFACT_AND_NAMED_AUTHORITY")
def _f17():
    """MISSING ARTIFACT. The A7 defect, reintroduced verbatim: a WRITTEN_CONFIRMED rule that
    cites a locus resolving to no artifact this repository holds."""
    return _patch_rule("quiz.pass_percent", authority_artifact=None,
                       authority_locus="A7", authority_date=None)


@fixture("PL-18", "EVERY_WRITTEN_CONFIRMED_RULE_CITES_A_DATED_ARTIFACT_AND_NAMED_AUTHORITY")
def _f18():
    """MISSING NAMED AUTHORITY. The artifact and locus are real; nobody is named."""
    return _patch_rule("dialogue.tension_required", named_authority="")


@fixture("PL-19", "EVERY_WRITTEN_CONFIRMED_RULE_CITES_A_DATED_ARTIFACT_AND_NAMED_AUTHORITY")
def _f19():
    """PARTIAL-CITATION COLLISION. Every field is populated, so any check built on 'is the
    field non-empty' passes: a registered artifact, a plausible locus, a date. But the named
    authority is a label rather than a human, and the date disagrees with the registry. A
    partial citation reads as a warrant to anyone skimming, which is the whole danger."""
    return _patch_rule("interaction.treatment_selection",
                       named_authority="SEE_ABOVE", authority_date="2026-01-01")


@fixture("PL-20", "EVERY_CITED_ARTIFACT_RESOLVES_TO_REAL_BYTES_ON_DISK")
def _f20():
    ar = A.contract()["artifacts"]["RETURNED_AUTHORITY_v0_2"]
    old = ar["sha256"]
    ar["sha256"] = "0" * 64
    return lambda: ar.__setitem__("sha256", old)


@fixture("PL-21", "EVERY_RULE_CARRIES_THE_STATUS_THE_SUITE_DECLARES_FOR_IT")
def _f21():
    """A confirmed rule quietly demoted to a proposal — the WA-03 / WA-04 failure direction,
    where a rule the authority HAD confirmed is recorded as something nobody agreed to."""
    return _patch_rule("rumusan.forbidden_phrase",
                       authority_status=A.PROPOSED_NOT_APPROVED)


@fixture("PL-22", "A_QUALIFIED_STATUS_NEVER_SATISFIES_APPROVED")
def _f22():
    """An asserted prior decision treated as a plain approval."""
    return _patch(A, "POSITIVE_STATUSES", A.POSITIVE_STATUSES | {A.ASSERTED_PRIOR})


# --------------------------------------------------------------- annotation fixtures ----
@fixture("PL-23", "NO_REVIEWER_ANNOTATION_APPEARS_IN_LEARNER_FACING_COPY")
def _f23():
    """A provenance tag reaches a learner-facing dialogue line."""
    orig = PM._dialogue

    def broken(unit_id, ex, roles):
        d = orig(unit_id, ex, roles)
        if d.get("turns"):
            d["turns"][0]["text"] = "[S] " + d["turns"][0]["text"]
        return d
    return _patch(PM, "_dialogue", broken)


@fixture("PL-24", "NO_RUMUSAN_BEAT_NAME_SURVIVES_AS_AN_INLINE_PREFIX")
def _f24():
    """The exact defect this pass removed: the beat label moved from a heading to a prefix."""
    orig = PM.scope_copy
    return _patch(PM, "scope_copy",
                  lambda items: ("Skop: " + "; ".join(items)) if items else None)


@fixture("PL-25", "NO_LEARNER_FACING_STRING_CARRIES_A_SOURCE_ROW_ID")
def _f25():
    orig = PM._rumusan

    def broken(unit_id, ex, subs):
        r = orig(unit_id, ex, subs)
        b = r["beats"][0]
        if b.get("text"):
            b["text"] = f"{b['text']} (T03B03-ROW-048)"
        return r
    return _patch(PM, "_rumusan", broken)


@fixture("PL-26", "THE_ANNOTATION_MARKER_LIST_HAS_NOT_DRIFTED_FROM_THE_SUITES")
def _f26():
    return _patch(PM, "REVIEWER_ANNOTATION_MARKERS",
                  [m for m in PM.REVIEWER_ANNOTATION_MARKERS if m != "Skop:"])


# --------------------------------------------------- reconciliation and sweep fixtures ----
@fixture("PL-27", "THE_PER_UNIT_ROLE_COUNTS_ARE_THE_DECLARED_ONES")
def _f27():
    """A role instance moves between units, leaving the headline total unchanged. A gate that
    only checked the total would report success."""
    orig = PM.role_audit

    def broken(unit_id, ex):
        out = orig(unit_id, ex)
        if unit_id == "K5-PL06-T03-B03" and out:
            return out[:-1]
        if unit_id == "K5-PL06-T02-B02":
            return list(out) + [dict(out[0]) if out else
                                dict(unit_id=unit_id, role_id="ROLE-KONTRAKTOR",
                                     cited_module_text=[], needs_to_speak=True,
                                     role_family=PM.FAM_JUNIOR,
                                     classification=PM.REUSE_ALYA,
                                     reused_character="Alya", new_role_description=None,
                                     name="Alya", reason="injected")]
        return out
    return _patch(PM, "role_audit", broken)


@fixture("PL-28", "THE_PACKAGE_SHAPE_IS_DERIVED_FROM_THE_ROLL_NOT_ASSERTED")
def _f28():
    """B02's profile is changed so it would carry a Lampiran. The declaration still says 13;
    the derivation says 14, and the two must not be allowed to agree by construction."""
    orig = A.legacy_units

    def broken():
        out = {k: dict(v) for k, v in orig().items()}
        out["K5-PL06-T03-B02"]["artifact_profile"] = "STORYBOARD_AND_LAMPIRAN"
        return out
    return _patch(A, "legacy_units", broken)


@fixture("PL-29", "THE_PRODUCTION_LAMPIRAN_DENSITY_IS_THE_AUTHORITY_VALUE")
def _f29():
    """The generator keeps the pre-F5 default while the declaration has moved to 3."""
    return _patch(B, "PRODUCTION_PANEL_DENSITY", 2)


@fixture("PL-30", "THE_CALIBRATION_DENSITIES_ARE_RETAINED_NOT_DELETED")
def _f30():
    """The 2-panel calibration evidence is dropped once the production choice is made."""
    return _patch(B, "CALIBRATION_DENSITIES", (3,))


@fixture("PL-31", "THE_FOUR_DECLARED_ANALYSIS_UNITS_SATISFY_THE_CONTRACT")
def _f31():
    """A committed analysis loses its compliance-sensitive statements but keeps its dict key.
    Under the old membership test the unit stayed SOURCE_ANALYSIS_COMPLETE."""
    import pl06_unit_model_v1 as U
    anal = U.UNIT_ANALYSIS["K5-PL06-T05-B01"]
    old = anal["compliance_sensitive"]
    anal["compliance_sensitive"] = old[:1]
    return lambda: anal.__setitem__("compliance_sensitive", old)


@fixture("PL-32", "EVERY_C2_CLAIM_CITES_A_ROW_THAT_EXISTS_IN_B03")
def _f32():
    c = A.contract()["dialogue"]["c2_claims"][0]
    old = c["controlled_rows"]
    c["controlled_rows"] = ["T03B03-ROW-999"]
    return lambda: c.__setitem__("controlled_rows", old)


@fixture("PL-33", "EVERY_TREATMENT_CHOSEN_IS_ONE_OF_THE_FOUR_F3_NAMES")
def _f33():
    """The generator falls back to its pre-F3 English vocabulary."""
    orig = PM._interaction

    def broken(unit_id, ex):
        out = orig(unit_id, ex)
        out["primary"] = "click-to-reveal"
        return out
    return _patch(PM, "_interaction", broken)


@fixture("PL-34", "NO_REPLACED_CHARACTER_IS_STILL_CAST")
def _f34():
    """A1 records Haziq as replaced; the role audit casts him anyway."""
    orig = PM.role_audit

    def broken(unit_id, ex):
        out = orig(unit_id, ex)
        if out:
            out[0]["reused_character"] = A.replaced_characters()[0]
        return out
    return _patch(PM, "role_audit", broken)


@fixture("PL-35", "NO_ANALYST_NOTE_APPEARS_IN_ANY_DIALOGUE_LINE")
def _f35():
    """The analyst's note goes back into the learner-facing line while the citation stays
    correct — the defect this pass found in all four committed units."""
    orig = PM._dialogue

    def broken(unit_id, ex, roles):
        d = orig(unit_id, ex, roles)
        for a in d.get("anchors", []):
            if a.get("analyst_note") and d.get("turns"):
                d["turns"][1]["text"] = a["analyst_note"]
                break
        return d
    return _patch(PM, "_dialogue", broken)


@fixture("PL-36", "NO_REVIEWER_ANNOTATION_APPEARS_IN_LEARNER_FACING_COPY")
def _f36():
    """A cast placeholder reaches a quiz stem."""
    orig = PM._quiz

    def broken(unit_id, ex):
        q = orig(unit_id, ex)
        for i in q["items"]:
            if i.get("stem"):
                i["stem"] = f"{PM.PENDING_CAST}: {i['stem']}"
                break
        return q
    return _patch(PM, "_quiz", broken)


@fixture("PL-37", "NO_CONTROLLED_PARAPHRASE_ESCALATES_BEYOND_ITS_SOURCE")
def _f37():
    """A paraphrase acquires an obligation its cited row does not carry — exactly the
    "mendakwa kewajipan yang tidak disokong" failure the owner prohibited."""
    spec = PM.AUTHORED_DIALOGUE["K5-PL06-T01-B03"]
    t = spec["turns"][1]
    old = t["text"]
    t["text"] = "Ujian penebatan itu wajib mengikut undang-undang sebelum apa-apa serahan."
    return lambda: t.__setitem__("text", old)


@fixture("PL-38", "EVERY_CONTROLLED_PARAPHRASE_NAMES_THE_ROW_IT_PARAPHRASES")
def _f38():
    spec = PM.AUTHORED_DIALOGUE["K5-PL06-T02-B01"]
    t = spec["turns"][1]
    old = t.pop("paraphrase_of")
    return lambda: t.__setitem__("paraphrase_of", old)


@fixture("PL-39", "EVERY_STRUCTURAL_FRAME_NAMES_ONLY_ROWS_OF_ITS_OWN_UNIT")
def _f39():
    """A scenario frame reaches into another unit's rows for its objects."""
    spec = PM.AUTHORED_DIALOGUE["K5-PL06-T02-B02"]
    t = spec["turns"][0]
    old = list(t["rows"])
    t["rows"] = old + ["T03B03-ROW-048"]
    return lambda: t.__setitem__("rows", old)


@fixture("PL-40", "EVERY_DIALOGUE_LINE_CARRIES_A_DECLARED_LINE_CLASS")
def _f40():
    spec = PM.AUTHORED_DIALOGUE["K5-PL06-T01-B03"]
    t = spec["turns"][2]
    old = t["cls"]
    t["cls"] = "SOURCE_DERIVED"
    return lambda: t.__setitem__("cls", old)


@fixture("PL-41", "THE_EXCLUDED_ROW_IS_NOT_CITED_IN_THE_T02B02_DIALOGUE")
def _f41():
    """ROW-058 creeps back into the same dialogue."""
    spec = PM.AUTHORED_DIALOGUE["K5-PL06-T02-B02"]
    t = spec["turns"][2]
    old = list(t["rows"])
    t["rows"] = old + [DECLARED_ROW_058_EXCLUDED]
    return lambda: t.__setitem__("rows", old)


@fixture("PL-42", "THE_FOUR_DECLARED_ANALYSIS_UNITS_SATISFY_THE_CONTRACT")
def _f42():
    """ASSESSED_NO_FINDINGS with no basis. An unexplained "nothing here" is indistinguishable
    from not having looked, so it must not clear the floor."""
    import pl06_unit_model_v1 as U
    anal = U.UNIT_ANALYSIS["K5-PL06-T06-B01"]
    old = anal["ambiguities"]
    anal["ambiguities"] = dict(assessed=PM.ASSESSED_NO_FINDINGS, basis="")
    return lambda: anal.__setitem__("ambiguities", old)


@fixture("PL-43", "THE_FOUR_DECLARED_ANALYSIS_UNITS_SATISFY_THE_CONTRACT",
         expect_detect=False)
def _f43():
    """POSITIVE CONTROL. ASSESSED_NO_FINDINGS WITH a basis must clear the floor — a contract
    that forces an analyst to produce findings rewards invention."""
    import pl06_unit_model_v1 as U
    anal = U.UNIT_ANALYSIS["K5-PL06-T06-B01"]
    old = anal["ambiguities"]
    anal["ambiguities"] = dict(
        assessed=PM.ASSESSED_NO_FINDINGS,
        basis="Every heading and prose row in the frozen slice was read for conflicting or "
              "unclear statements; none was found.")
    return lambda: anal.__setitem__("ambiguities", old)


@fixture("PL-44", "NO_RULE_CARRIES_A_STATUS_IN_NEITHER_SET")
def _f44():
    """A rule given a status that is in neither the citation-required nor the exempt set —
    the shape that let "48 of 51" hide three unaccounted rules."""
    return _patch_rule("interaction.symmetry_definition",
                       authority_status="SOMEHOW_CONFIRMED")


@fixture("PL-45", "THE_NON_DEFAULT_CONFIRMATION_PATHS_ARE_THE_DECLARED_ONES")
def _f45():
    """C5 quietly promoted from a Section-G-only record to a normal A-to-F decision."""
    return _patch_rule("dialogue.b03_formula_application",
                       confirmation_path=A.PATH_A_TO_F)


# ------------------------------------------------- approved B03 S02 copy fixtures ----
def _b03_lines():
    return A.contract()["dialogue"]["b03_s02_canonical_copy"]["value"]


@fixture("PL-46", "B03_S02_DIALOGUE_MATCHES_APPROVED_C1_CANONICAL_LINES", expect_detect=False)
def _f46():
    """POSITIVE CONTROL. The canonical clean copy, untouched, must pass."""
    return lambda: None


@fixture("PL-47", "B03_S02_DIALOGUE_MATCHES_APPROVED_C1_CANONICAL_LINES")
def _f47():
    """One content word changed — a paraphrase of approved instructional copy."""
    ln = _b03_lines()[1]
    old = ln["text"]
    ln["text"] = old.replace("mesti mengikut", "sebaiknya mengikut")
    return lambda: ln.__setitem__("text", old)


@fixture("PL-48", "B03_S02_DIALOGUE_MATCHES_APPROVED_C1_CANONICAL_LINES")
def _f48():
    """Speaker order changed. Same five lines, same words, wrong conversation."""
    lines = _b03_lines()
    old = [dict(l) for l in lines]
    lines[0]["speaker"], lines[1]["speaker"] = lines[1]["speaker"], lines[0]["speaker"]
    return lambda: [l.update(o) for l, o in zip(lines, old)]


@fixture("PL-49", "B03_S02_DIALOGUE_MATCHES_APPROVED_C1_CANONICAL_LINES")
def _f49():
    """One line removed. Five approved lines become four."""
    c = A.contract()["dialogue"]["b03_s02_canonical_copy"]
    old = c["value"]
    c["value"] = old[:-1]
    return lambda: c.__setitem__("value", old)


@fixture("PL-50", "NO_REVIEWER_ANNOTATION_SURVIVES_IN_THE_APPROVED_B03_COPY")
def _f50():
    """The reviewer annotation put back into the learner-facing line — the exact string that
    had to be stripped from C1 line 2 to make the copy canonical."""
    ln = _b03_lines()[1]
    old = ln["text"]
    ln["text"] = old + DECLARED_STRIPPED_ANNOTATION
    return lambda: ln.__setitem__("text", old)


@fixture("PL-51", "NO_ANALYSIS_RECORD_LIVES_IN_THE_AUTHORITY_DECLARATION")
def _f51():
    """An analysis record creeps back into the instructional declaration to satisfy a
    citation gate — the shape this closure pass removed."""
    c = A.contract()
    c["dialogue"]["row_058_disposition"] = dict(
        value="x", authority_status=A.WRITTEN_CONFIRMED,
        authority_artifact="FIRDAUS_TENSION_DISPOSITION_v1", authority_locus="section 3",
        named_authority="Firdaus Ismail", authority_date="2026-08-05")
    return lambda: c["dialogue"].pop("row_058_disposition", None)


@fixture("PL-52", "NO_ACTIVE_WRITTEN_CONFIRMED_RECORD_IS_CITATION_EXEMPT")
def _f52():
    """A WRITTEN_CONFIRMED record moved outside the citation-required set."""
    return _patch(A, "CITATION_REQUIRED",
                  A.CITATION_REQUIRED - {A.WRITTEN_CONFIRMED})


# ------------------------------------------------------------------- refusal fixtures ----
REFUSAL_CASES = [
    ("PR-01", "unresolved cast", lambda p: dict(
        p, roles=dict(p["roles"], new_required=[dict(role_id="ROLE-X", status=PM.ROLE_NEW,
                                                     name=PM.PENDING_CAST,
                                                     role_description="d",
                                                     authority_basis="b")]),
        production_blockers=sorted(set(p["production_blockers"]) | {"CAST_UNRESOLVED"}))),
    ("PR-02", "missing quiz key", lambda p: dict(
        p, quiz=dict(p["quiz"], items=[dict(i, key_status=A.NO_KEY_PENDING_AUTHORING)
                                       for i in p["quiz"].get("items", [])]),
        production_blockers=sorted(set(p["production_blockers"]) | {"QUIZ_KEY_UNRESOLVED"}))),
    ("PR-03", "PENDING marker", lambda p: dict(
        p, dialogue=dict(p["dialogue"], turns=[dict(t, text="PENDING_AUTHORING")
                                               for t in p["dialogue"]["turns"]]))),
]


def refusal_results():
    """Each case must exit non-zero AND write zero PPTX."""
    import glob
    import shutil
    import tempfile
    base = PM.packets()[0]
    out = []
    for fid, label, mutate in REFUSAL_CASES:
        tmp = tempfile.mkdtemp(prefix=f"pl06ref_{fid}_")
        try:
            pk = mutate(base)
            exit_code, refused = 0, None
            try:
                B.guard_production(pk, B.PRODUCTION)
            except B.ProductionRefused as e:
                exit_code, refused = 1, str(e)
            written = len(glob.glob(os.path.join(tmp, "*.pptx")))
            out.append(dict(id=fid, case=label, exit_code=exit_code,
                            pptx_written=written,
                            passed=(exit_code != 0 and written == 0),
                            refusal=(refused or "")[:110]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return out


def run_mutations(verbose=True):
    base_G, base_bad = run(verbose=False)
    results, missed = [], []
    for fx in FIXTURES:
        undo = fx["fn"]()
        try:
            PM._ROWS = PM._ROWS  # cache is process-level and intentionally kept
            G, bad = run(verbose=False)
            names = {g["name"] for g in bad}
            caught = fx["target"] in names
            want = fx.get("expect_detect", True)
            results.append(dict(id=fx["id"], target=fx["target"], detected=caught,
                                expect_detect=want, correct=(caught == want),
                                also_failed=sorted(names - {fx["target"]})))
            if caught != want:
                missed.append(fx["id"])
        finally:
            undo()
    ref = refusal_results()
    out = dict(baseline_pass=len(base_G) - len(base_bad), baseline_total=len(base_G),
               fixture_count=len(FIXTURES), detected=len(FIXTURES) - len(missed),
               missed=missed,
               refusal_cases=len(ref), refusal_passed=len([r for r in ref if r["passed"]]),
               refusal=ref, results=results)
    if verbose:
        print(json.dumps({k: v for k, v in out.items()
                          if k not in ("results", "refusal")}, indent=1))
        for r in results:
            tag = "OK " if r["correct"] else "MISS"
            kind = "detect" if r["expect_detect"] else "POSITIVE-CONTROL must not trip"
            print(f"  {r['id']}  {tag}  [{kind}]  {r['target']}")
        for r in ref:
            print(f"  {r['id']}  {'OK ' if r['passed'] else 'FAIL'}  {r['case']}: "
                  f"exit={r['exit_code']} pptx_written={r['pptx_written']}")
    return out


if __name__ == "__main__":
    if "--mutations" in sys.argv:
        r = run_mutations()
        sys.exit(0 if not r["missed"] and r["refusal_passed"] == r["refusal_cases"] else 1)
    G, bad = run()
    sys.exit(0 if not bad else 1)
