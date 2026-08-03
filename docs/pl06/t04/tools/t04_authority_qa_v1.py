# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.9 QA — typed gates over the ingested authority decisions.

    SUITE_ID = T04_AUTHORITY_DECISION_INGESTION_QA_v1
    python3 docs/pl06/t04/tools/t04_authority_qa_v1.py

Harness rules carried forward, each of which exists because a defect got past an earlier
suite:

1. Every gate declares the POPULATION it examined. Population 0 FAILS unless the gate
   declares `empty_by_design` with a reason.
2. Every gate names the SOURCE ARTIFACT it read. A gate that cannot say where its observed
   value came from is not evidence of anything.
3. Nothing derived is read from a module-level constant. Three stages running, a fixture
   caught a gate comparing against a value cached at import — a total, then a count, then a
   whole projection. Every quantity below is recomputed inside the gate.

A green suite measures the suite, not the artifact. Nothing here can tell you whether
Bariah's replacement dialogue reads well, or whether the two CAIR-written Q5 distractors are
good distractors.
"""
import json
import os
import re
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_authority_data_v1 as D      # noqa: E402
import t04_content_data_v1 as C        # noqa: E402
import t04_authority_emit_v1 as EMIT   # noqa: E402

SUITE_ID = "T04_AUTHORITY_DECISION_INGESTION_QA_v1"
PRIOR_SUITE_ID = "T04_BARIAH_REVIEW_ARTIFACT_QA_v1"

EVIDENCE_INTEGRITY = "EVIDENCE_INTEGRITY"
CONFIRMATION_DISCIPLINE = "CONFIRMATION_DISCIPLINE"
DECISION_TYPING = "DECISION_TYPING"
SEQUENCE_INTEGRITY = "SEQUENCE_INTEGRITY"
CONTENT_FIDELITY = "CONTENT_FIDELITY"
ASSESSMENT_INTEGRITY = "ASSESSMENT_INTEGRITY"
GLOBAL_RULE_SCOPE = "GLOBAL_RULE_SCOPE"
VISUAL_SCOPE = "VISUAL_SCOPE"
SOURCE_STATUS = "SOURCE_STATUS"
RECONCILIATION = "RECONCILIATION"
FREEZE_HONESTY = "FREEZE_HONESTY"
PRODUCTION_GUARD = "PRODUCTION_GUARD"
REPORTING = "REPORTING"
ACCOUNTING = "ACCOUNTING"

GATE_TYPES = {EVIDENCE_INTEGRITY, CONFIRMATION_DISCIPLINE, DECISION_TYPING,
              SEQUENCE_INTEGRITY, CONTENT_FIDELITY, ASSESSMENT_INTEGRITY, GLOBAL_RULE_SCOPE,
              VISUAL_SCOPE, SOURCE_STATUS, RECONCILIATION, FREEZE_HONESTY, PRODUCTION_GUARD,
              REPORTING, ACCOUNTING}

NOT_CHECKED = [
    "whether Bariah's replacement dialogue reads naturally to a native Malay speaker",
    "whether the three-beat Rumusan is instructionally better than the four points it "
    "replaced — she ruled it, the gates carry it, they do not judge it",
    "whether the two CAIR-written Q5 distractors are good distractors, or whether Bariah "
    "will accept them",
    "whether the proposed answer keys are correct — no key is final and none is asserted",
    "whether 'Q3' in the WhatsApp line means quiz Q3 — the referent is unresolved and the "
    "suite records it as unresolved rather than picking one",
    "whether the pembajaan-to-racun correction matches Bariah's intent — the correction is "
    "recorded, not validated",
    "whether the inserted screen sits at the right point in the sequence for learning",
    "whether 22 screens is the right length",
    "whether the original module DOCX still matches the controlled extract — that round trip "
    "was not run in this session and is recorded as OPEN",
    "any rendered output — no PPTX exists for T04 and none was generated",
]

AUTHORITY_DOCX = os.path.join(
    REPO, D.EVIDENCE_DIR, D.PRIMARY_DOCX_NAME)
UPLOAD_DOCX = ("/root/.claude/uploads/12837c42-b6ab-597b-8301-85c5b457471b/"
               "698bf575-T04_Pakej_Semakan_Bariah_v3_vBariah.docx")

# Malay compliance vocabulary a character may not utter, from Stage 4.2F-B0.6.
DIALOGUE_BANNED = ("akta", "berlesen", "lesen", "ppe", "sds", "helaian data keselamatan",
                   "stor berkunci", "pelupusan", "papan tanda amaran")
# The contrast framing Bariah banned from the dialogue.
CONTRAST_PATTERNS = (r"beza(?:nya)?\s+(?:antara\s+)?(?:landskap\s+)?(?:lembut|kejur)",
                     r"berbeza\s+daripada\s+landskap",
                     r"membezakan\s+(?:antara\s+)?landskap")

# A superseded fact may still appear in an emitted artifact — but only where the surrounding
# text marks it as history. Rather than allowlisting whole files, each occurrence is checked
# for one of these markers within a 120-character window on either side. An accidental stale
# claim written as ordinary prose carries none of them.
SUPERSESSION_MARKERS = ("superseded", "Superseded", "SUPERSEDED", "retired", "stale_claim",
                        "No longer true", "fact_id", "SF-0", "\"detect\"", "was labelled",
                        "archived", "ARCHIVED", "dropped from")
STALE_CONTEXT_WINDOW = 120


def _parses(text):
    try:
        json.loads(text)
        return True
    except Exception:
        return False


def _read(name):
    with open(os.path.join(T04, name), encoding="utf-8") as f:
        return f.read()


def _strings(blob):
    out = []

    def walk(o):
        if isinstance(o, str):
            out.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)

    walk(blob)
    return out


def _docx_text(path):
    z = zipfile.ZipFile(path)
    xml = z.read("word/document.xml").decode("utf-8")
    # Runs are joined with NO separator. Word splits a single word across runs at formatting
    # and proofing boundaries, so joining with a space would insert spaces mid-word and make
    # a verbatim comparison fail on text that is in fact verbatim.
    parts = re.findall(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", xml, re.S)
    txt = "".join(parts)
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                 ("&apos;", "'")):
        txt = txt.replace(a, b)
    return re.sub(r"\s+", " ", txt)


def _docx_markup(path):
    return zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")


def _sha(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def run():
    res = []

    def chk(gid, gtype, value, expected, population, source_artifact,
            empty_by_design=None):
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        assert gtype in GATE_TYPES, gtype
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source_artifact,
                        empty_by_design=empty_by_design, vacuous=vacuous,
                        ok=ok and not vacuous))

    # Everything is recomputed here, not read from a module constant.
    REG = D._decision_register()
    SEQ = D._final_sequence()
    QUIZ = D.quiz_items()
    DNR = D._do_not_reuse_items()
    AGS = D.asset_group_scope()
    STATES = D.final_states()
    IDS = {d["decision_id"] for d in REG}

    docx_path = AUTHORITY_DOCX if os.path.exists(AUTHORITY_DOCX) else UPLOAD_DOCX
    docx_present = os.path.exists(docx_path)
    DOCX_SRC = os.path.relpath(docx_path, REPO) if docx_path.startswith(REPO) else docx_path

    artifacts = {n: _read(n) for n in D.NEW_ARTIFACTS
                 if os.path.exists(os.path.join(T04, n))}

    # ==================== 1. EVIDENCE INTEGRITY ====================
    chk("EVIDENCE_HIERARCHY_HAS_FOUR_LEVELS", EVIDENCE_INTEGRITY,
        [r["evidence_class"] for r in D.EVIDENCE], D.EVIDENCE_CLASSES,
        len(D.EVIDENCE), "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("EVERY_EVIDENCE_RECORD_CARRIES_EVERY_FIELD", EVIDENCE_INTEGRITY,
        sorted({f for r in D.EVIDENCE for f in D.EVIDENCE_FIELDS if f not in r}), [],
        len(D.EVIDENCE) * len(D.EVIDENCE_FIELDS),
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("PRIMARY_EVIDENCE_IS_THE_ANNOTATED_V3_DOCX", EVIDENCE_INTEGRITY,
        [r["filename"] for r in D.EVIDENCE
         if r["evidence_class"] == "PRIMARY_AUTHORITY_EVIDENCE"],
        [D.PRIMARY_DOCX_NAME], 1, "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("AUTHORITY_DOCX_PRESENT_ON_DISK", EVIDENCE_INTEGRITY,
        docx_present, True, 1, DOCX_SRC)
    chk("AUTHORITY_DOCX_BYTE_SIZE_MATCHES", EVIDENCE_INTEGRITY,
        os.path.getsize(docx_path) if docx_present else None, D.PRIMARY_DOCX_BYTES, 1,
        DOCX_SRC)
    chk("AUTHORITY_DOCX_SHA256_MATCHES", EVIDENCE_INTEGRITY,
        _sha(docx_path) if docx_present else None, D.PRIMARY_DOCX_SHA256, 1, DOCX_SRC)
    chk("AUTHORITY_DOCX_IS_A_VALID_PACKAGE", EVIDENCE_INTEGRITY,
        (zipfile.ZipFile(docx_path).testzip() if docx_present else "missing"), None, 1,
        DOCX_SRC)

    markup = _docx_markup(docx_path) if docx_present else ""
    dtext = _docx_text(docx_path) if docx_present else ""
    chk("NO_TRACKED_INSERTIONS", EVIDENCE_INTEGRITY,
        len(re.findall(r"<w:ins[ >]", markup)), 0, 1, DOCX_SRC)
    chk("NO_TRACKED_DELETIONS", EVIDENCE_INTEGRITY,
        len(re.findall(r"<w:del[ >]", markup)), 0, 1, DOCX_SRC)
    chk("NO_TRACKED_FORMAT_CHANGES", EVIDENCE_INTEGRITY,
        len(re.findall(r"<w:(?:rPrChange|pPrChange)[ >]", markup)), 0, 1, DOCX_SRC)
    chk("NO_WORD_COMMENTS_PART", EVIDENCE_INTEGRITY,
        [n for n in (zipfile.ZipFile(docx_path).namelist() if docx_present else [])
         if "comments" in n], [], 1, DOCX_SRC)
    chk("TRACKED_CHANGES_NOT_CLAIMED", EVIDENCE_INTEGRITY,
        (D.PRIMARY_ARTIFACT_MECHANISM["tracked_changes_present"],
         D.PRIMARY_ARTIFACT_MECHANISM["word_comments_present"]), (False, False), 2,
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("DECISION_MECHANISM_STATED", EVIDENCE_INTEGRITY,
        D.PRIMARY_ARTIFACT_MECHANISM["decision_mechanism"],
        "TICKED_DECISION_BOXES_AND_TYPED_TEXT_IN_DOCUMENT_FIELDS", 1,
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.md")
    chk("SUBSTRING_COUNTING_TRAP_DISCLOSED", EVIDENCE_INTEGRITY,
        "insideH" in D.PRIMARY_ARTIFACT_MECHANISM["counting_trap"], True, 1,
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.md")
    chk("AUTHORITY_NAME_IN_THE_DOCUMENT", EVIDENCE_INTEGRITY,
        "Bariah Ahmad" in dtext, True, 1, DOCX_SRC)
    chk("AUTHORITY_VERDICT_IN_THE_DOCUMENT", EVIDENCE_INTEGRITY,
        "LULUS DENGAN PINDAAN DINYATAKAN" in dtext, True, 1, DOCX_SRC)

    # The supplementary screenshot was not supplied. It must be recorded as absent, never
    # invented.
    supp = [r for r in D.EVIDENCE
            if r["evidence_class"] == "SUPPLEMENTARY_AUTHORITY_EVIDENCE"]
    chk("SUPPLEMENTARY_EVIDENCE_MARKED_NOT_SUPPLIED", EVIDENCE_INTEGRITY,
        [r["supplied_in_this_run"] for r in supp], [False], len(supp),
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("SUPPLEMENTARY_HASH_IS_NOT_SUPPLIED_NOT_A_VALUE", EVIDENCE_INTEGRITY,
        [(r["sha256"], r["byte_size"], r["dimensions_or_extent"]) for r in supp],
        [("NOT_SUPPLIED", "NOT_SUPPLIED", "NOT_SUPPLIED")], len(supp) * 3,
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("NO_FABRICATED_HASH_FOR_UNSUPPLIED_EVIDENCE", EVIDENCE_INTEGRITY,
        [r["evidence_id"] for r in D.EVIDENCE
         if not r["supplied_in_this_run"] and re.fullmatch(r"[0-9a-f]{64}", str(r["sha256"]))],
        [], len(D.EVIDENCE), "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("SUPPLEMENTARY_LIMITATION_STATED_IN_THE_MARKDOWN", EVIDENCE_INTEGRITY,
        "NOT_SUPPLIED" in artifacts.get("T04_AUTHORITY_EVIDENCE_REGISTER_v1.md", ""), True, 1,
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.md")
    chk("EVERY_EVIDENCE_RECORD_STATES_ITS_LIMITATIONS", EVIDENCE_INTEGRITY,
        [r["evidence_id"] for r in D.EVIDENCE if not r["limitations"]], [],
        len(D.EVIDENCE), "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("EVERY_EVIDENCE_RECORD_STATES_ITS_PROVENANCE", EVIDENCE_INTEGRITY,
        [r["evidence_id"] for r in D.EVIDENCE if not r["provenance_chain"]], [],
        len(D.EVIDENCE), "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("V2_RECORDED_AS_SUPERSEDED_NOT_AUTHORITY", EVIDENCE_INTEGRITY,
        [s["path"] for s in D.SUPERSEDED_ARTIFACTS if "v2.docx" in s["path"]],
        [D.EVIDENCE_DIR + "/T04_Pakej_Semakan_Bariah_v2.docx"],
        len(D.SUPERSEDED_ARTIFACTS), "T04_AUTHORITY_RECONCILIATION_v1.json")

    # ==================== 2. CONFIRMATION DISCIPLINE ====================
    CNF = D.CONFIRMATIONS
    chk("THREE_CONFIRMATION_RECORDS", CONFIRMATION_DISCIPLINE, len(CNF), 3, len(CNF),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("CONFIRMATION_IDS_ARE_TYPED", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF], ["T04-CNF-01", "T04-CNF-02", "T04-CNF-03"],
        len(CNF), "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("Q3_IS_NOT_USED_AS_A_DECISION_ID", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF if c["confirmation_id"] in ("Q3", "T04-Q3")]
        + [d["decision_id"] for d in REG if d["decision_id"] in ("Q3", "T04-DEC-Q3")], [],
        len(CNF) + len(REG), "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    q3 = [c for c in CNF if c.get("ambiguous_label_as_written") == "Q3"]
    chk("Q3_AMBIGUITY_RECORDED_AS_AMBIGUOUS", CONFIRMATION_DISCIPLINE,
        [c["status"] for c in q3], ["AMBIGUOUS_REFERENT_NOT_ACTIONABLE"], len(q3),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("Q3_CANDIDATE_REFERENTS_BOTH_LISTED", CONFIRMATION_DISCIPLINE,
        [len(c["candidate_referents"]) for c in q3], [2], len(q3),
        "T04_AUTHORITY_CONFIRMATIONS_v1.md")
    chk("Q3_CHANGES_NO_CONTENT", CONFIRMATION_DISCIPLINE,
        [c["applied_to_content"] for c in q3], [False], len(q3),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("Q3_NOT_LABELLED_AN_AUTHORITY_ORIGINATED_RULE", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF
         if "BARIAH_ORIGINATED_RULE" in json.dumps(c, ensure_ascii=False)], [], len(CNF),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("Q3_DELEGATION_RECORDED_AS_DELEGATION", CONFIRMATION_DISCIPLINE,
        [c.get("secondary_status") for c in q3],
        ["DELEGATED_TO_CAIR_PENDING_BARIAH_CONFIRMATION"], len(q3),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("EVERY_CONFIRMATION_CARRIES_ITS_QUOTE", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF if not c["authority_quote"]], [], len(CNF),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("EVERY_CONFIRMATION_IS_GRADED_DEGRADED", CONFIRMATION_DISCIPLINE,
        sorted({c["evidence_grade"] for c in CNF}),
        ["DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED"], len(CNF),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("EVERY_CONFIRMATION_STATES_ITS_LIMIT", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF if not c["what_this_does_not_establish"]], [],
        len(CNF), "T04_AUTHORITY_CONFIRMATIONS_v1.md")
    chk("ONLY_Q5_TYPE_IS_APPLIED_FROM_WHATSAPP", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF if c["applied_to_content"]], ["T04-CNF-02"],
        len(CNF), "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("NO_CONFIRMATION_IS_BLOCKING", CONFIRMATION_DISCIPLINE,
        [c["confirmation_id"] for c in CNF if c["blocking"]], [], len(CNF),
        "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    chk("CONFIRMATION_STATUSES_ARE_FROM_THE_DECLARED_SET", CONFIRMATION_DISCIPLINE,
        [c["status"] for c in CNF if c["status"] not in D.CONFIRMATION_STATUSES], [],
        len(CNF), "T04_AUTHORITY_CONFIRMATIONS_v1.json")

    # ==================== 3. DECISION TYPING ====================
    by_class = D.decisions_by_class()
    chk("ALL_SEVEN_DECISION_CLASSES_DECLARED", DECISION_TYPING,
        len(D.DECISION_CLASSES), 7, len(D.DECISION_CLASSES),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_DECISION_CLASS_IS_POPULATED", DECISION_TYPING,
        [c for c in D.DECISION_CLASSES if not by_class[c]], [], len(D.DECISION_CLASSES),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_DECISION_CLASS_HAS_A_STATED_MEANING", DECISION_TYPING,
        [c for c in D.DECISION_CLASSES if not D.DECISION_CLASS_MEANING.get(c)], [],
        len(D.DECISION_CLASSES), "T04_AUTHORITY_DECISION_REGISTER_v1.md")
    chk("NO_GENERIC_ACCEPTED_BUCKET", DECISION_TYPING,
        [c for c in D.DECISION_CLASSES if c in ("ACCEPTED", "APPROVED", "OK")], [],
        len(D.DECISION_CLASSES), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("DECISIONS_NOT_FLATTENED_INTO_ONE_CLASS", DECISION_TYPING,
        len({d["decision_class"] for d in REG}), 7, len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_DECISION_CARRIES_ITS_AUTHORITY_QUOTE", DECISION_TYPING,
        [d["decision_id"] for d in REG if not d["authority_quote"]], [], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_DECISION_NAMES_ITS_SOURCE_ARTIFACT", DECISION_TYPING,
        sorted({d["source_artifact"] for d in REG}), ["AUTH-EV-01", "AUTH-EV-02"], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_DECISION_CARRIES_EVERY_FIELD", DECISION_TYPING,
        sorted({f for d in REG for f in D.DECISION_FIELDS if f not in d}), [],
        len(REG) * len(D.DECISION_FIELDS), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("DECISION_IDS_ARE_UNIQUE", DECISION_TYPING, len(IDS), len(REG), len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_DECISION_APPLIES_TO_SOMETHING", DECISION_TYPING,
        [d["decision_id"] for d in REG if not d["applies_to"]], [], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("WHATSAPP_DECISIONS_CARRY_THE_DEGRADED_GRADE", DECISION_TYPING,
        sorted({d["evidence_grade"] for d in REG if d["source_artifact"] == "AUTH-EV-02"}),
        ["DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED"],
        len([d for d in REG if d["source_artifact"] == "AUTH-EV-02"]),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("DOCX_DECISIONS_CARRY_THE_VERIFIED_GRADE", DECISION_TYPING,
        sorted({d["evidence_grade"] for d in REG if d["source_artifact"] == "AUTH-EV-01"}),
        ["VERIFIED_PRIMARY_ARTIFACT"],
        len([d for d in REG if d["source_artifact"] == "AUTH-EV-01"]),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    cair_exec = [d for d in REG
                 if d["decision_class"] == "AMENDED_WITH_AUTHORITY_INSTRUCTION_EXECUTED_BY_CAIR"]
    chk("CAIR_EXECUTED_DECISIONS_ARE_NOT_AUTHORITY_AUTHORED", DECISION_TYPING,
        [d["decision_id"] for d in cair_exec if d["authored_by_authority"]], [],
        len(cair_exec), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    supplied = [d for d in REG
                if d["decision_class"] == "AMENDED_WITH_AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"]
    chk("AUTHORITY_SUPPLIED_TEXT_IS_MARKED_AUTHORITY_AUTHORED", DECISION_TYPING,
        [d["decision_id"] for d in supplied if not d["authored_by_authority"]], [],
        len(supplied), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    unsettled = [d for d in REG if not d["settled"]]
    chk("UNSETTLED_DECISIONS_ARE_ONLY_THE_DELEGATED_CLASS", DECISION_TYPING,
        sorted({d["decision_class"] for d in unsettled}),
        ["DELEGATED_PENDING_AUTHORITY_CONFIRMATION"], len(unsettled),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    # C-05 got past the suite: relabelling the delegated Q3 decision as ACCEPTED removed it
    # from the unsettled population, and a gate that only inspects the unsettled population
    # cannot see something leave it. The named delegations are asserted directly.
    chk("THE_TWO_NAMED_DELEGATIONS_REMAIN_UNSETTLED", DECISION_TYPING,
        sorted(d["decision_id"] for d in REG if not d["settled"]),
        ["T04-DEC-X01", "T04-DEC-X02"], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("THE_Q3_DELEGATION_KEEPS_ITS_DELEGATED_CLASS", DECISION_TYPING,
        [d["decision_class"] for d in REG if d["decision_id"] == "T04-DEC-X01"],
        ["DELEGATED_PENDING_AUTHORITY_CONFIRMATION"], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_WORDING_CORRECTION_IS_RECORDED", DECISION_TYPING,
        [c["correction_id"] for c in D.AUTHORITY_WORDING_CORRECTIONS
         if not (c["as_written_by_authority"] and c["as_applied"] and c["basis"])], [],
        len(D.AUTHORITY_WORDING_CORRECTIONS), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("NO_CORRECTION_IS_SILENT", DECISION_TYPING,
        [c["correction_id"] for c in D.AUTHORITY_WORDING_CORRECTIONS
         if c["as_written_by_authority"] == c["as_applied"]], [],
        len(D.AUTHORITY_WORDING_CORRECTIONS), "T04_AUTHORITY_DECISION_REGISTER_v1.md")
    chk("CORRECTIONS_ARE_PENDING_NOT_APPROVED", DECISION_TYPING,
        sorted({c["status"] for c in D.AUTHORITY_WORDING_CORRECTIONS}),
        ["APPLIED_PENDING_BARIAH_CONFIRMATION"], len(D.AUTHORITY_WORDING_CORRECTIONS),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("PEMBAJAAN_CORRECTION_PRESENT", DECISION_TYPING,
        [c["correction_id"] for c in D.AUTHORITY_WORDING_CORRECTIONS
         if "pembajaan" in c["as_written_by_authority"] and "racun" in c["as_applied"]],
        ["T04-COR-01"], len(D.AUTHORITY_WORDING_CORRECTIONS),
        "T04_FINAL_SCREEN_SEQUENCE_v2.md")
    chk("EVERY_SUPERSESSION_NAMES_ITS_RISK_OWNER", DECISION_TYPING,
        [s["supersession_id"] for s in D.SUPERSESSIONS if not s["risk_owner"]], [],
        len(D.SUPERSESSIONS), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_SUPERSESSION_RESOLVES_TO_A_REAL_DECISION", DECISION_TYPING,
        [s["supersession_id"] for s in D.SUPERSESSIONS if s["superseded_by"] not in IDS], [],
        len(D.SUPERSESSIONS), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("CLOSED_DECISIONS_ARE_NOT_REOPENED", DECISION_TYPING,
        [d["decision_id"] for d in REG
         if d["decision_class"] == "ACCEPTED_AS_PROPOSED" and not d["settled"]], [],
        len([d for d in REG if d["decision_class"] == "ACCEPTED_AS_PROPOSED"]),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")

    # ==================== 4. SEQUENCE INTEGRITY ====================
    chk("FINAL_SCREEN_COUNT_IS_TWENTY_TWO", SEQUENCE_INTEGRITY,
        len(SEQ), 22, len(SEQ), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("SCREEN_COUNT_DERIVED_LIVE", SEQUENCE_INTEGRITY,
        D.final_screen_count(), len(D._final_sequence()), len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("SCREEN_IDS_ARE_CONTIGUOUS", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ], [f"T04-S{i:02d}" for i in range(1, 23)], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("POSITIONS_ARE_CONTIGUOUS", SEQUENCE_INTEGRITY,
        [s["position"] for s in SEQ], list(range(1, 23)), len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EXACTLY_ONE_SCREEN_INSERTED", SEQUENCE_INTEGRITY,
        D.inserted_screens(), ["T04-S14"], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EIGHT_SCREENS_RENUMBERED", SEQUENCE_INTEGRITY,
        len(D.renumbering_map()), 8, len(SEQ), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("RENUMBERING_IS_A_PLUS_ONE_SHIFT", SEQUENCE_INTEGRITY,
        sorted({int(v[-2:]) - int(k[-2:]) for k, v in D.renumbering_map().items()}), [1],
        len(D.renumbering_map()), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EVERY_PRIOR_SCREEN_SURVIVES", SEQUENCE_INTEGRITY,
        sorted({s["previous_screen_id"] for s in SEQ if s["previous_screen_id"]}),
        sorted({s["screen_id"] for s in C.SCREEN_SEQUENCE}), len(C.SCREEN_SEQUENCE),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("NO_PRIOR_SCREEN_MAPS_TWICE", SEQUENCE_INTEGRITY,
        len([s for s in SEQ if s["previous_screen_id"]]),
        len({s["previous_screen_id"] for s in SEQ if s["previous_screen_id"]}), len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("INSERTED_SCREEN_IS_SOURCE_BOUND", SEQUENCE_INTEGRITY,
        [s["source_row_ids"] for s in SEQ if s["change_type"] == "INSERTED"],
        [["T04-ROW-064"]], 1, "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EVERY_SOURCE_ROW_RESOLVES", SEQUENCE_INTEGRITY,
        sorted({r for s in SEQ for r in s["source_row_ids"] if r not in C.BY_ID}), [],
        len({r for s in SEQ for r in s["source_row_ids"]}),
        "T04_SOURCE_EXTRACT_v1.json")
    chk("EVERY_SCREEN_IS_SOURCE_BOUND_OR_STRUCTURAL", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ if not s["source_binding_present"]], [], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EVERY_SCREEN_NAMES_ITS_DECISIONS", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ if not s["decision_ids"]], [], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EVERY_SCREEN_DECISION_RESOLVES", SEQUENCE_INTEGRITY,
        sorted({d for s in SEQ for d in s["decision_ids"] if d not in IDS}), [],
        len({d for s in SEQ for d in s["decision_ids"]}),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("EVERY_CHANGE_TYPE_IS_DECLARED", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ if s["change_type"] not in D.CHANGE_TYPES], [],
        len(SEQ), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("CLOSING_SCREEN_READS_TAMAT_TOPIK", SEQUENCE_INTEGRITY,
        SEQ[-1]["working_title"], "Tamat Topik", 1, "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("NO_SCREEN_TITLE_SAYS_TAMAT_BAHAGIAN", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ if "Tamat Bahagian" in s["working_title"]], [],
        len(SEQ), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("INTERNAL_UNIT_ID_UNCHANGED", SEQUENCE_INTEGRITY,
        sorted({s["internal_unit_id"] for s in SEQ}), ["K5-PL06-T04-B01"], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("LEARNER_DISPLAY_UNIT_IS_TOPIK_4", SEQUENCE_INTEGRITY,
        sorted({s["learner_display_unit"] for s in SEQ}), ["Topik 4"], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("INTERNAL_ID_AND_DISPLAY_LABEL_ARE_DISTINCT", SEQUENCE_INTEGRITY,
        D.INTERNAL_UNIT_ID != D.LEARNER_DISPLAY_UNIT, True, 2,
        "T04_FINAL_SCREEN_SEQUENCE_v2.md")
    changed = [s for s in SEQ if "TREATMENT_CHANGED" in s["change_type"]]
    chk("FOUR_TREATMENTS_CHANGED", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in changed],
        ["T04-S12", "T04-S13", "T04-S16", "T04-S17"], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EVERY_TREATMENT_CHANGE_ACTUALLY_CHANGES_THE_TREATMENT", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in changed if s["treatment"] == s["previous_treatment"]], [],
        len(changed), "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("RENUMBER_ONLY_SCREENS_KEEP_THEIR_TREATMENT", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ
         if s["change_type"] == "RENUMBERED" and s["treatment"] != s["previous_treatment"]],
        [], len([s for s in SEQ if s["change_type"] == "RENUMBERED"]),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("NAMED_REVEAL_ITEMS_PRESENT_ON_BOTH_SCREENS", SEQUENCE_INTEGRITY,
        {s["screen_id"]: len(s["named_reveal_items"]) for s in SEQ
         if s["named_reveal_items"]}, {"T04-S14": 3, "T04-S16": 3}, len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("PPE_LENGKAP_IS_A_NAMED_REVEAL_ON_S16", SEQUENCE_INTEGRITY,
        "PPE Lengkap" in D.NAMED_REVEAL_ITEMS["T04-S16"], True, 3,
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("D04_PPE_SUPERSESSION_RECORDED_WITH_ITS_RISK", SEQUENCE_INTEGRITY,
        [s["supersession_id"] for s in D.SUPERSESSIONS
         if "PPE" in s["superseded_ruling"] and s["risk_owner"] == "BARIAH_AHMAD"],
        ["T04-SUP-01"], len(D.SUPERSESSIONS), "T04_FINAL_SCREEN_SEQUENCE_v2.md")
    chk("REVEAL_SCREENS_HAVE_A_STATE_PER_NAMED_ITEM", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ if s["named_reveal_items"]
         and len(s["interaction_states"]) < len(s["named_reveal_items"]) + 2], [],
        len([s for s in SEQ if s["named_reveal_items"]]),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("STATIC_SCREENS_HAVE_NO_REVEAL_STATES", SEQUENCE_INTEGRITY,
        [s["screen_id"] for s in SEQ
         if s["treatment"] == "CONTENT_STATIC" and s["interaction_states"] != ["BASE only"]],
        [], len([s for s in SEQ if s["treatment"] == "CONTENT_STATIC"]),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("ASPECT_LISTS_ON_THE_THREE_MAIN_EXPLANATION_SCREENS", SEQUENCE_INTEGRITY,
        sorted(k for k, v in D.NAMED_ASPECT_LISTS.items() if v),
        ["T04-S05", "T04-S08", "T04-S11"], len(SEQ),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    chk("EVERY_SCREEN_IS_FROZEN", SEQUENCE_INTEGRITY,
        sorted({s["content_status"] for s in SEQ}), ["FROZEN_UNDER_AUTHORITY_DECISION"],
        len(SEQ), "T04_FINAL_SCREEN_SEQUENCE_v2.json")

    # ==================== 5. CONTENT FIDELITY ====================
    DLG = D.FINAL_DIALOGUE
    chk("DIALOGUE_HAS_FOUR_LINES", CONTENT_FIDELITY, len(DLG["lines"]), 4,
        len(DLG["lines"]), "T04_FINAL_DIALOGUE_v1.json")
    chk("DIALOGUE_IDS_ARE_THE_FINAL_SERIES", CONTENT_FIDELITY,
        [x["line_id"] for x in DLG["lines"]],
        ["T04-DLG-F01", "T04-DLG-F02", "T04-DLG-F03", "T04-DLG-F04"], len(DLG["lines"]),
        "T04_FINAL_DIALOGUE_v1.json")
    chk("DIALOGUE_IS_AUTHORITY_AUTHORED", CONTENT_FIDELITY,
        sorted({x["authorship"] for x in DLG["lines"]}),
        ["AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"], len(DLG["lines"]),
        "T04_FINAL_DIALOGUE_v1.json")
    if docx_present:
        norm = re.sub(r"\s+", " ", dtext)
        missing = [x["line_id"] for x in DLG["lines"]
                   if re.sub(r"\s+", " ", x["text_ms"]) not in norm]
    else:
        missing = ["docx-unavailable"]
    chk("EVERY_DIALOGUE_LINE_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX", CONTENT_FIDELITY,
        missing, [], len(DLG["lines"]), DOCX_SRC)
    chk("DIALOGUE_SPEAKERS_ARE_THE_APPROVED_CAST", CONTENT_FIDELITY,
        sorted({x["speaker"] for x in DLG["lines"]}), ["Alya", "Encik Rahman"],
        len(DLG["lines"]), "T04_FINAL_DIALOGUE_v1.json")
    chk("NO_COMPLIANCE_DUTY_IN_THE_DIALOGUE", CONTENT_FIDELITY,
        sorted({t for x in DLG["lines"] for t in DIALOGUE_BANNED
                if re.search(rf"\b{re.escape(t)}\b", x["text_ms"], re.I)}), [],
        len(DLG["lines"]) * len(DIALOGUE_BANNED), "T04_FINAL_DIALOGUE_v1.json")
    chk("NO_SOFT_VERSUS_HARD_CONTRAST_IN_THE_DIALOGUE", CONTENT_FIDELITY,
        [x["line_id"] for x in DLG["lines"]
         for p in CONTRAST_PATTERNS if re.search(p, x["text_ms"], re.I)], [],
        len(DLG["lines"]) * len(CONTRAST_PATTERNS), "T04_FINAL_DIALOGUE_v1.json")
    chk("DIALOGUE_LINE_COUNT_DROPPED_FROM_FIVE", CONTENT_FIDELITY,
        (DLG["superseded_line_count"], DLG["line_count"]), (5, 4), 2,
        "T04_FINAL_DIALOGUE_v1.md")

    RUM = D.FINAL_RUMUSAN
    chk("RUMUSAN_HAS_THREE_BEATS", CONTENT_FIDELITY, len(RUM["points"]), 3,
        len(RUM["points"]), "T04_FINAL_RUMUSAN_v1.json")
    chk("RUMUSAN_BEATS_ARE_THE_NAMED_THREE", CONTENT_FIDELITY,
        [x["beat"] for x in RUM["points"]], ["Kepentingan", "Skop/Isi Utama", "Manfaat"],
        len(RUM["points"]), "T04_FINAL_RUMUSAN_v1.json")
    chk("RUMUSAN_IDS_ARE_THE_FINAL_SERIES", CONTENT_FIDELITY,
        [x["point_id"] for x in RUM["points"]],
        ["T04-RUM-F01", "T04-RUM-F02", "T04-RUM-F03"], len(RUM["points"]),
        "T04_FINAL_RUMUSAN_v1.json")
    if docx_present:
        rmiss = [x["point_id"] for x in RUM["points"]
                 if re.sub(r"\s+", " ", x["text_ms"]) not in re.sub(r"\s+", " ", dtext)]
    else:
        rmiss = ["docx-unavailable"]
    chk("EVERY_RUMUSAN_BEAT_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX", CONTENT_FIDELITY,
        rmiss, [], len(RUM["points"]), DOCX_SRC)
    chk("RUMUSAN_POINT_COUNT_DROPPED_FROM_FOUR", CONTENT_FIDELITY,
        (RUM["superseded_point_count"], RUM["point_count"]), (4, 3), 2,
        "T04_FINAL_RUMUSAN_v1.md")
    chk("THREE_BEAT_RULE_IS_NOT_INFERRED_COURSE_WIDE", CONTENT_FIDELITY,
        RUM["scope_of_the_three_beat_structure"]["applies_to"], "T04_ONLY", 1,
        "T04_FINAL_RUMUSAN_v1.json")
    chk("THREE_BEAT_SCOPE_EXPLAINS_ITSELF", CONTENT_FIDELITY,
        "Global keseluruhan kursus" in RUM["scope_of_the_three_beat_structure"]["why"], True,
        1, "T04_FINAL_RUMUSAN_v1.md")
    dep = D.ARCHIVED_DEPENDENCIES
    chk("DEP_RUM04_Q5_IS_ARCHIVED_NOT_DELETED", CONTENT_FIDELITY,
        [d["dependency_id"] for d in dep if d["status"] == "ARCHIVED_RESOLVED"],
        ["DEP-RUM04-Q5"], len(dep), "T04_FINAL_RUMUSAN_v1.json")
    chk("ARCHIVED_DEPENDENCY_NAMES_WHAT_RESOLVED_IT", CONTENT_FIDELITY,
        sorted({r for d in dep for r in d["resolved_by"] if r not in IDS}), [],
        len({r for d in dep for r in d["resolved_by"]}),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("ARCHIVED_DEPENDENCY_STATES_ITS_REOPEN_CONDITION", CONTENT_FIDELITY,
        [d["dependency_id"] for d in dep if not d.get("reopens_if")], [], len(dep),
        "T04_FINAL_RUMUSAN_v1.md")
    chk("RUMUSAN_04_GENERALISATION_IS_GONE", CONTENT_FIDELITY,
        [x["point_id"] for x in RUM["points"]
         if "pengendali berlesen" in x["text_ms"] or "penyimpanan berkunci" in x["text_ms"]],
        [], len(RUM["points"]), "T04_FINAL_RUMUSAN_v1.json")

    # ==================== 6. ASSESSMENT INTEGRITY ====================
    chk("QUIZ_HAS_FIVE_ITEMS", ASSESSMENT_INTEGRITY, len(QUIZ), 5, len(QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    chk("QUIZ_COMPOSITION_IS_FOUR_MCQ_AND_ONE_MR", ASSESSMENT_INTEGRITY,
        [q["question_type"] for q in QUIZ],
        ["MCQ", "MCQ", "MCQ", "MCQ", "MULTIPLE_RESPONSE"], len(QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    if docx_present:
        smiss = [q["question_id"] for q in QUIZ
                 if re.sub(r"\s+", " ", q["stem_ms"]) not in re.sub(r"\s+", " ", dtext)]
    else:
        smiss = ["docx-unavailable"]
    chk("EVERY_QUIZ_STEM_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX", ASSESSMENT_INTEGRITY,
        smiss, [], len(QUIZ), DOCX_SRC)
    chk("EVERY_STEM_IS_AUTHORITY_AUTHORED", ASSESSMENT_INTEGRITY,
        sorted({q["stem_authorship"] for q in QUIZ}),
        ["AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"], len(QUIZ), "T04_FINAL_QUIZ_v2.json")
    chk("EVERY_STEM_CHANGED", ASSESSMENT_INTEGRITY,
        [q["question_id"] for q in QUIZ if q["stem_ms"] == q["superseded_stem_ms"]], [],
        len(QUIZ), "T04_FINAL_QUIZ_v2.json")
    banned = [p for r in D.QUIZ_GLOBAL_RULES for p in r.get("banned_phrases", [])]
    chk("NO_MODULE_ATTRIBUTION_IN_ANY_STEM", ASSESSMENT_INTEGRITY,
        sorted({f"{q['question_id']}:{p}" for q in QUIZ for p in banned
                if p.lower() in q["stem_ms"].lower()}), [], len(QUIZ) * len(banned),
        "T04_FINAL_QUIZ_v2.json")
    chk("SUPERSEDED_STEMS_DID_CARRY_THE_ATTRIBUTION", ASSESSMENT_INTEGRITY,
        len({q["question_id"] for q in QUIZ for p in banned
             if p.lower() in q["superseded_stem_ms"].lower()}), 5, len(QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    mr = [q for q in QUIZ if q["question_type"] == "MULTIPLE_RESPONSE"]
    mcq = [q for q in QUIZ if q["question_type"] == "MCQ"]
    chk("MULTIPLE_RESPONSE_OPTIONS_USE_CHECKBOXES", ASSESSMENT_INTEGRITY,
        sorted({o["display_marker"] for q in mr for o in q["options"]}), ["checkbox"],
        sum(len(q["options"]) for q in mr), "T04_FINAL_QUIZ_v2.json")
    chk("MULTIPLE_RESPONSE_OPTIONS_CARRY_NO_LETTER", ASSESSMENT_INTEGRITY,
        [o["option_id"] for q in mr for o in q["options"] if o["letter_label"]], [],
        sum(len(q["options"]) for q in mr), "T04_FINAL_QUIZ_v2.json")
    chk("MCQ_OPTIONS_KEEP_THEIR_LETTERS", ASSESSMENT_INTEGRITY,
        [o["option_id"] for q in mcq for o in q["options"] if not o["letter_label"]], [],
        sum(len(q["options"]) for q in mcq), "T04_FINAL_QUIZ_v2.json")
    chk("Q5_HAS_SIX_OPTIONS", ASSESSMENT_INTEGRITY,
        [q["option_count"] for q in mr], [6], len(mr), "T04_FINAL_QUIZ_v2.json")
    chk("TWO_Q5_OPTIONS_WERE_SUBSTITUTED", ASSESSMENT_INTEGRITY,
        len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS), 2, len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS),
        "T04_FINAL_QUIZ_v2.json")
    chk("SUBSTITUTED_OPTIONS_ARE_AT_POSITIONS_FIVE_AND_SIX", ASSESSMENT_INTEGRITY,
        [s["position"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS], [5, 6],
        len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS), "T04_FINAL_QUIZ_v2.json")
    live_q5 = [o["text_ms"] for q in mr for o in q["options"]]
    chk("SUPERSEDED_FERTILISER_DISTRACTORS_ARE_GONE", ASSESSMENT_INTEGRITY,
        [s["superseded_text"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS
         if s["superseded_text"] in live_q5], [], len(live_q5),
        "T04_FINAL_QUIZ_v2.json")
    chk("REPLACEMENT_DISTRACTORS_ARE_IN_THE_LIVE_OPTION_SET", ASSESSMENT_INTEGRITY,
        [s["replacement_text"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS
         if s["replacement_text"] not in live_q5], [], len(live_q5),
        "T04_FINAL_QUIZ_v2.json")
    chk("REPLACEMENT_DISTRACTORS_ARE_NOT_ABOUT_BAJA", ASSESSMENT_INTEGRITY,
        [s["position"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS
         if re.search(r"\bbaja|pembajaan\b", s["replacement_text"], re.I)], [],
        len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS), "T04_FINAL_QUIZ_v2.json")
    chk("REPLACEMENT_DISTRACTORS_ARE_NOT_AUTHORITY_AUTHORED", ASSESSMENT_INTEGRITY,
        sorted({s["authorship"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS}),
        ["CAIR_DRAFTED_UNDER_AUTHORITY_INSTRUCTION"], len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS),
        "T04_FINAL_QUIZ_v2.json")
    chk("REPLACEMENT_DISTRACTORS_ARE_PENDING_CONFIRMATION", ASSESSMENT_INTEGRITY,
        sorted({s["approval_status"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS}),
        ["PENDING_BARIAH_CONFIRMATION"], len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS),
        "T04_FINAL_QUIZ_v2.json")
    chk("THE_ROUTE_CHOICE_IS_ATTRIBUTED_TO_CAIR", ASSESSMENT_INTEGRITY,
        (D.QUIZ_Q5_ROUTE_CHOICE["chosen_by"], D.QUIZ_Q5_ROUTE_CHOICE["route_taken"]),
        ("CAIR", "CHANGE_THE_TWO_OPTIONS"), 2, "T04_FINAL_QUIZ_v2.md")
    chk("ANSWER_KEY_IS_NOT_FINAL", ASSESSMENT_INTEGRITY,
        sorted({q["answer_key_status"] for q in QUIZ}), ["PROPOSED_NOT_FINAL"], len(QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    chk("EVERY_OPTION_KEY_FLAG_IS_MARKED_PROPOSED", ASSESSMENT_INTEGRITY,
        sorted({o["key_status"] for q in QUIZ for o in q["options"]}),
        ["PROPOSED_NOT_FINAL"], sum(len(q["options"]) for q in QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    chk("EVERY_ITEM_HAS_AT_LEAST_ONE_PROPOSED_KEY", ASSESSMENT_INTEGRITY,
        [q["question_id"] for q in QUIZ if not q["proposed_key_positions"]], [], len(QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    chk("MCQ_ITEMS_HAVE_EXACTLY_ONE_KEY", ASSESSMENT_INTEGRITY,
        [q["question_id"] for q in mcq if len(q["proposed_key_positions"]) != 1], [],
        len(mcq), "T04_FINAL_QUIZ_v2.json")
    chk("MULTIPLE_RESPONSE_HAS_MORE_THAN_ONE_KEY", ASSESSMENT_INTEGRITY,
        [q["question_id"] for q in mr if len(q["proposed_key_positions"]) < 2], [], len(mr),
        "T04_FINAL_QUIZ_v2.json")
    chk("EVERY_QUIZ_ITEM_IS_SOURCE_BOUND", ASSESSMENT_INTEGRITY,
        [q["question_id"] for q in QUIZ if not q["source_row_ids"]], [], len(QUIZ),
        "T04_FINAL_QUIZ_v2.json")
    chk("EVERY_QUIZ_SOURCE_ROW_RESOLVES", ASSESSMENT_INTEGRITY,
        sorted({r for q in QUIZ for r in q["source_row_ids"] if r not in C.BY_ID}), [],
        len({r for q in QUIZ for r in q["source_row_ids"]}), "T04_SOURCE_EXTRACT_v1.json")
    chk("PASS_MARK_UNCHANGED", ASSESSMENT_INTEGRITY,
        D.FINAL_QUIZ["pass_mark"], "60 peratus", 1, "T04_FINAL_QUIZ_v2.json")
    chk("QUIZ_SCOPE_IS_THE_WHOLE_KURSUS", ASSESSMENT_INTEGRITY,
        D.FINAL_QUIZ["scope"], "ALL_PLS_IN_KURSUS", 1, "T04_FINAL_QUIZ_v2.json")
    chk("NO_QUIZ_OPTION_NAMES_THE_ACT", ASSESSMENT_INTEGRITY,
        [o["option_id"] for q in QUIZ for o in q["options"]
         if re.search(r"\bakta\b", o["text_ms"], re.I)], [],
        sum(len(q["options"]) for q in QUIZ), "T04_FINAL_QUIZ_v2.json")

    # ==================== 7. GLOBAL RULE SCOPE ====================
    GR = D.QUIZ_GLOBAL_RULES
    chk("TWO_COURSE_WIDE_QUIZ_RULES", GLOBAL_RULE_SCOPE, len(GR), 2, len(GR),
        "T04_QUIZ_GLOBAL_RULES_v1.json")
    chk("GLOBAL_RULE_IDS", GLOBAL_RULE_SCOPE,
        [r["rule_id"] for r in GR], ["QUIZ-GLOBAL-01", "QUIZ-GLOBAL-02"], len(GR),
        "T04_QUIZ_GLOBAL_RULES_v1.json")
    chk("BOTH_GLOBAL_RULES_SCOPE_ALL_PLS", GLOBAL_RULE_SCOPE,
        sorted({r["scope"] for r in GR}), ["ALL_PLS_IN_KURSUS"], len(GR),
        "T04_QUIZ_GLOBAL_RULES_v1.json")
    chk("BOTH_GLOBAL_RULES_QUOTE_GLOBAL_KESELURUHAN_KURSUS", GLOBAL_RULE_SCOPE,
        [r["rule_id"] for r in GR
         if "Global keseluruhan kursus" not in r["authority_quote"]], [], len(GR),
        "T04_QUIZ_GLOBAL_RULES_v1.json")
    chk("ONLY_TWO_DECISIONS_ARE_COURSE_WIDE", GLOBAL_RULE_SCOPE,
        D.course_wide_decisions(), ["T04-DEC-E06", "T04-DEC-E07"], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("NO_RUMUSAN_DECISION_IS_COURSE_WIDE", GLOBAL_RULE_SCOPE,
        [d["decision_id"] for d in REG
         if d["source_section"] == "D" and d["scope"] == "ALL_PLS_IN_KURSUS"], [],
        len([d for d in REG if d["source_section"] == "D"]),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("NO_DIALOGUE_DECISION_IS_COURSE_WIDE", GLOBAL_RULE_SCOPE,
        [d["decision_id"] for d in REG
         if d["source_section"] == "C" and d["scope"] == "ALL_PLS_IN_KURSUS"], [],
        len([d for d in REG if d["source_section"] == "C"]),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("GLOBAL_RULES_STATE_THEIR_ENFORCEMENT", GLOBAL_RULE_SCOPE,
        [r["rule_id"] for r in GR if not r["enforcement"]], [], len(GR),
        "T04_QUIZ_GLOBAL_RULES_v1.md")
    chk("GLOBAL_RULES_NAME_THE_T04_ITEMS_THEY_TOUCHED", GLOBAL_RULE_SCOPE,
        [r["rule_id"] for r in GR if not r["applied_to_t04_items"]], [], len(GR),
        "T04_QUIZ_GLOBAL_RULES_v1.json")
    chk("GLOBAL_RULE_TARGETS_RESOLVE_TO_REAL_ITEMS", GLOBAL_RULE_SCOPE,
        sorted({i for r in GR for i in r["applied_to_t04_items"]
                if i not in {q["question_id"] for q in QUIZ}}), [],
        len({i for r in GR for i in r["applied_to_t04_items"]}),
        "T04_FINAL_QUIZ_v2.json")
    chk("NO_OTHER_UNIT_MODIFIED_BY_THIS_STAGE", GLOBAL_RULE_SCOPE,
        sorted({n for n in D.NEW_ARTIFACTS if not n.startswith("T04_")}), [],
        len(D.NEW_ARTIFACTS), "T04_AUTHORITY_RECONCILIATION_v1.json")

    # ==================== 8. VISUAL SCOPE ====================
    V = D.FINAL_VISUAL_SCOPE
    chk("VISUAL_SCOPE_STATUS_IS_ACCEPTED_WITH_CONDITIONS", VISUAL_SCOPE,
        V["status"], "ACCEPTED_AS_A_SET_WITH_CONDITIONS", 1,
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("VISUAL_GOVERNANCE_ID", VISUAL_SCOPE, V["governance_id"], "T04-VIS-GOV-01", 1,
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("FORTY_SIX_IS_NOT_FORTY_ONE", VISUAL_SCOPE,
        (V["visual_obligation_count"], V["proposed_unique_assets"]), (46, 41), 2,
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("ACCEPTED_PRODUCTION_SCOPE_IS_FORTY_ONE", VISUAL_SCOPE,
        V["accepted_production_scope"], 41, 1, "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("ASSET_TOTALS_DERIVED_LIVE_FROM_THE_CONTENT_MODEL", VISUAL_SCOPE,
        (V["proposed_unique_assets"], V["asset_group_count"]),
        (C._asset_totals()["proposed_unique_assets"],
         C._asset_totals()["asset_group_count"]), 2,
        "T04_VISUAL_ASSET_GROUPING_PLAN_v2.json")
    chk("THREE_DO_NOT_REUSE_ITEMS", VISUAL_SCOPE, len(DNR), 3, len(DNR),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("EVERY_DO_NOT_REUSE_ITEM_CARRIES_A_DECISION_BASIS", VISUAL_SCOPE,
        [x["obligation_id"] for x in DNR
         if x["decision_basis"] not in D.DECISION_BASIS_VALUES], [], len(DNR),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("ALL_THREE_BASES_ARE_BOTH_LENSES", VISUAL_SCOPE,
        sorted({x["decision_basis"] for x in DNR}),
        ["BOTH_INSTRUCTIONAL_AND_PRODUCTION"], len(DNR),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("EVERY_DO_NOT_REUSE_ITEM_GIVES_BOTH_GROUNDS", VISUAL_SCOPE,
        [x["obligation_id"] for x in DNR
         if not (x["instructional_ground"] and x["production_ground"])], [], len(DNR),
        "T04_FINAL_VISUAL_SCOPE_v1.md")
    chk("RESTRICTIONS_ARE_ITEM_LEVEL_NOT_GROUP_LEVEL", VISUAL_SCOPE,
        sorted({x["restriction_scope"] for x in DNR}), ["NAMED_ITEM_NOT_WHOLE_GROUP"],
        len(DNR), "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("NO_GROUP_IS_RESTRICTED_AS_A_WHOLE", VISUAL_SCOPE,
        [g["asset_group_id"] for g in AGS if g["restriction_applies_to_whole_group"]], [],
        len(AGS), "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("EIGHT_ASSET_GROUPS", VISUAL_SCOPE, len(AGS), 8, len(AGS),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("EVERY_GROUP_IS_REUSE_WITH_CONDITIONS", VISUAL_SCOPE,
        sorted({g["reuse_decision"] for g in AGS}), ["REUSE_WITH_CONDITIONS"], len(AGS),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("RESTRICTED_ITEMS_MAP_TO_THEIR_GROUPS", VISUAL_SCOPE,
        sorted({i for g in AGS for i in g["item_level_restrictions"]}),
        sorted({x["obligation_id"] for x in DNR}), len(AGS),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("PRECEDENCE_RULE_IS_INSTRUCTIONAL_OVER_PRODUCTION", VISUAL_SCOPE,
        "instruksional mengatasi" in V["precedence_rule"]["authority_quote"], True, 1,
        "T04_FINAL_VISUAL_SCOPE_v1.md")
    chk("PRECEDENCE_RULE_IS_BINDING_NOT_ADVISORY", VISUAL_SCOPE,
        bool(V["precedence_rule"]["binding_on"]), True, 1,
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("THE_INSERTED_SCREEN_ADDS_NO_ASSET", VISUAL_SCOPE,
        V["new_screen_asset_impact"]["new_unique_assets"], 0, 1,
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("INSERTED_SCREEN_OBLIGATION_CLOSURE_UNCHANGED", VISUAL_SCOPE,
        [r["closure_outcome"] for r in C._obligation_closure()
         if r["obligation_id"] == V["new_screen_asset_impact"]["obligation_id"]],
        ["NOT_A_SEPARATE_ASSET_WITH_REASON"], len(C._obligation_closure()),
        "T04_VISUAL_OBLIGATION_CLOSURE_v1.json")
    chk("NO_ARTWORK_IS_APPROVED", VISUAL_SCOPE,
        "did not approve any specific artwork" in V["what_is_not_approved"], True, 1,
        "T04_FINAL_VISUAL_SCOPE_v1.md")
    chk("NO_MMD_PRODUCTION_HAS_STARTED", VISUAL_SCOPE,
        sorted({g["mmd_production_status"] for g in AGS}), ["NOT_STARTED"], len(AGS),
        "T04_FINAL_VISUAL_SCOPE_v1.json")

    # ==================== 9. SOURCE STATUS ====================
    chk("SOURCE_BINDINGS_PRESENT", SOURCE_STATUS,
        D.SOURCE_STATUS["CONTROLLED_EXTRACT_SOURCE_BINDINGS"], "PRESENT", 1,
        "T04_SOURCE_STATUS_v1.json")
    chk("ROUND_TRIP_REPRODUCIBILITY_OPEN", SOURCE_STATUS,
        D.SOURCE_STATUS["ORIGINAL_DOCX_ROUND_TRIP_REPRODUCIBILITY"], "OPEN", 1,
        "T04_SOURCE_STATUS_v1.json")
    chk("RETRIEVAL_AND_HASH_PROOF_OPEN", SOURCE_STATUS,
        D.SOURCE_STATUS["SOURCE_DOCX_RETRIEVAL_AND_HASH_PROOF"], "OPEN", 1,
        "T04_SOURCE_STATUS_v1.json")
    chk("RISK_TOKEN_IS_THE_DECLARED_ONE", SOURCE_STATUS,
        D.SOURCE_RISK_TOKEN,
        "SOURCE_REPRODUCIBILITY_OPEN_NONBLOCKING_FOR_T04_STORYBOARD_BUILD", 1,
        "T04_SOURCE_STATUS_v1.json")
    chk("FINAL_CONTENT_IS_NOT_MARKED_SOURCE_UNSUPPORTED", SOURCE_STATUS,
        [s for s in _strings([SEQ, D.FINAL_DIALOGUE, D.FINAL_RUMUSAN, D.FINAL_QUIZ, V])
         if "SOURCE_UNSUPPORTED" in s], [],
        len(_strings([SEQ, D.FINAL_DIALOGUE, D.FINAL_RUMUSAN, D.FINAL_QUIZ, V])),
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("SOURCE_UNSUPPORTED_IS_DECLARED_FORBIDDEN", SOURCE_STATUS,
        D.SOURCE_STATUS_DETAIL["must_not_be_recorded_as"], "SOURCE_UNSUPPORTED", 1,
        "T04_SOURCE_STATUS_v1.md")
    chk("OPEN_RISK_IS_NON_BLOCKING", SOURCE_STATUS,
        D.SOURCE_STATUS_DETAIL["blocking"], False, 1, "T04_SOURCE_STATUS_v1.json")
    chk("OPEN_RISK_NAMES_ITS_OWNER", SOURCE_STATUS,
        bool(D.SOURCE_STATUS_DETAIL["risk_owner"]), True, 1, "T04_SOURCE_STATUS_v1.json")
    chk("OPEN_RISK_SAYS_WHAT_WOULD_CLOSE_IT", SOURCE_STATUS,
        bool(D.SOURCE_STATUS_DETAIL["what_would_close_it"]), True, 1,
        "T04_SOURCE_STATUS_v1.md")
    prior_rows = {r for s in C.SCREEN_SEQUENCE for r in s["source_row_ids"]}
    now_rows = {r for s in SEQ for r in s["source_row_ids"]}
    chk("SOURCE_BINDINGS_NOT_REMOVED_FROM_THE_MODEL", SOURCE_STATUS,
        sorted(prior_rows - now_rows), [], len(prior_rows),
        "T04_FINAL_SCREEN_SEQUENCE_v2.json")
    # T04-ROW-064 moved from the old S14 to the inserted screen. It must still be bound.
    chk("THE_INSERTED_SCREENS_ROW_WAS_REASSIGNED_NOT_DUPLICATED", SOURCE_STATUS,
        sorted(s["screen_id"] for s in SEQ if "T04-ROW-064" in s["source_row_ids"]),
        ["T04-S14"], len(SEQ), "T04_FINAL_SCREEN_SEQUENCE_v2.json")

    # ==================== 10. RECONCILIATION ====================
    chk("EVERY_DECLARED_ARTIFACT_WAS_EMITTED", RECONCILIATION,
        sorted(set(D.NEW_ARTIFACTS) - set(artifacts)), [], len(D.NEW_ARTIFACTS),
        "docs/pl06/t04/")
    stale_hits, stale_occurrences = [], 0
    for name, text in artifacts.items():
        for f in D.SUPERSEDED_FACTS:
            for pat in f["detect"]:
                for m in re.finditer(re.escape(pat), text):
                    stale_occurrences += 1
                    a = max(0, m.start() - STALE_CONTEXT_WINDOW)
                    b = min(len(text), m.end() + STALE_CONTEXT_WINDOW)
                    if not any(k in text[a:b] for k in SUPERSESSION_MARKERS):
                        stale_hits.append(f"{name}:{f['fact_id']}:{pat}")
    chk("NO_EMITTED_ARTIFACT_ASSERTS_A_STALE_FACT_AS_CURRENT", RECONCILIATION,
        sorted(set(stale_hits)), [],
        len(artifacts) * len(D.SUPERSEDED_FACTS), "docs/pl06/t04/")
    # Vacuity guard: if nothing matched at all, the gate above proved nothing.
    chk("STALE_FACT_SCAN_ACTUALLY_MATCHED_SOMETHING", RECONCILIATION,
        stale_occurrences > 0, True, stale_occurrences, "docs/pl06/t04/")
    chk("SEVEN_STALE_FACTS_NAMED", RECONCILIATION,
        len(D.SUPERSEDED_FACTS), 7, len(D.SUPERSEDED_FACTS),
        "T04_AUTHORITY_RECONCILIATION_v1.json")
    chk("EVERY_STALE_FACT_NAMES_ITS_DECISION", RECONCILIATION,
        [f["fact_id"] for f in D.SUPERSEDED_FACTS if f["decision_id"] not in IDS], [],
        len(D.SUPERSEDED_FACTS), "T04_AUTHORITY_RECONCILIATION_v1.json")
    chk("EVERY_STALE_FACT_STATES_WHAT_REPLACED_IT", RECONCILIATION,
        [f["fact_id"] for f in D.SUPERSEDED_FACTS if not f["now"]], [],
        len(D.SUPERSEDED_FACTS), "T04_AUTHORITY_RECONCILIATION_v1.md")
    chk("EVERY_SUPERSEDED_ARTIFACT_POINTS_AT_ITS_REPLACEMENT", RECONCILIATION,
        [s["path"] for s in D.SUPERSEDED_ARTIFACTS if not s["superseded_by"]], [],
        len(D.SUPERSEDED_ARTIFACTS), "T04_AUTHORITY_RECONCILIATION_v1.json")
    chk("EVERY_SUPERSEDED_ARTIFACT_EXISTS", RECONCILIATION,
        [s["path"] for s in D.SUPERSEDED_ARTIFACTS
         if not os.path.exists(os.path.join(REPO, s["path"]))], [],
        len(D.SUPERSEDED_ARTIFACTS), "repository")
    chk("EVERY_REPLACEMENT_ARTIFACT_EXISTS", RECONCILIATION,
        [s["superseded_by"] for s in D.SUPERSEDED_ARTIFACTS
         if not os.path.exists(os.path.join(REPO, s["superseded_by"]))], [],
        len(D.SUPERSEDED_ARTIFACTS), "repository")
    chk("EVERY_STALE_FACT_REFERENCE_RESOLVES", RECONCILIATION,
        sorted({x for s in D.SUPERSEDED_ARTIFACTS for x in s["stale_facts"]
                if x not in {f["fact_id"] for f in D.SUPERSEDED_FACTS}}), [],
        len(D.SUPERSEDED_ARTIFACTS), "T04_AUTHORITY_RECONCILIATION_v1.json")
    chk("SUPERSESSION_MARKER_SET_IS_NOT_EMPTY", RECONCILIATION,
        len(SUPERSESSION_MARKERS) >= 8, True, len(SUPERSESSION_MARKERS),
        "t04_authority_qa_v1.py")
    chk("TWENTY_FOUR_ARTIFACTS_DECLARED", RECONCILIATION,
        len(D.NEW_ARTIFACTS), 24, len(D.NEW_ARTIFACTS),
        "T04_AUTHORITY_RECONCILIATION_v1.json")
    chk("EVERY_EMITTED_ARTIFACT_IS_NON_EMPTY", RECONCILIATION,
        [n for n, t in artifacts.items() if len(t.strip()) < 200], [], len(artifacts),
        "docs/pl06/t04/")
    chk("EVERY_EMITTED_MARKDOWN_CARRIES_THE_GENERATOR_BANNER", RECONCILIATION,
        [n for n, t in artifacts.items()
         if n.endswith(".md") and EMIT.BANNER not in t], [],
        len([n for n in artifacts if n.endswith(".md")]), "docs/pl06/t04/")
    chk("EVERY_EMITTED_JSON_PARSES", RECONCILIATION,
        [n for n, t in artifacts.items() if n.endswith(".json")
         and not _parses(t)], [],
        len([n for n in artifacts if n.endswith(".json")]), "docs/pl06/t04/")

    # ==================== 11. FREEZE HONESTY ====================
    chk("TEN_FINAL_STATES", FREEZE_HONESTY, len(STATES), 10, len(STATES),
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("EVERY_FINAL_STATE_IS_FROM_THE_DECLARED_SET", FREEZE_HONESTY,
        [s["state_id"] for s in STATES if s["final_state"] not in D.FINAL_STATE_VALUES], [],
        len(STATES), "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("FINAL_STATE_IDS_ARE_UNIQUE", FREEZE_HONESTY,
        len({s["state_id"] for s in STATES}), len(STATES), len(STATES),
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("TWO_CLASSES_ARE_FROZEN_BUT_NOT_SETTLED", FREEZE_HONESTY,
        sorted([s["state_id"] for s in STATES if not s["settled"]]), ["FS-07", "FS-08"],
        len(STATES), "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("Q5_OPTIONS_STATE_IS_PENDING_CONFIRMATION", FREEZE_HONESTY,
        [s["final_state"] for s in STATES if s["state_id"] == "FS-07"],
        ["CAIR_EXECUTED_UNDER_AUTHORITY_INSTRUCTION_PENDING_CONFIRMATION"], len(STATES),
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("ANSWER_KEY_STATE_IS_PROPOSED_NOT_FINAL", FREEZE_HONESTY,
        [s["final_state"] for s in STATES if s["state_id"] == "FS-08"],
        ["PROPOSED_NOT_FINAL"], len(STATES), "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("EVERY_SETTLED_STATE_NAMES_ITS_DECISIONS", FREEZE_HONESTY,
        [s["state_id"] for s in STATES
         if s["settled"] and not s["decision_ids"] and s["state_id"] != "FS-10"], [],
        len(STATES), "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("EVERY_FINAL_STATE_DECISION_RESOLVES", FREEZE_HONESTY,
        sorted({d for s in STATES for d in s["decision_ids"] if d not in IDS}), [],
        len({d for s in STATES for d in s["decision_ids"]}),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("COURSE_WIDE_STATE_IS_SEPARATE_FROM_THE_TEN", FREEZE_HONESTY,
        D.COURSE_WIDE_STATE["state_id"] in {s["state_id"] for s in STATES}, False, 1,
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("SIX_ITEMS_STAY_OPEN_AFTER_THIS_STAGE", FREEZE_HONESTY,
        len(D.OPEN_AFTER_THIS_STAGE), 6, len(D.OPEN_AFTER_THIS_STAGE),
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("E01_TO_E04_ARE_NOT_CLOSED", FREEZE_HONESTY,
        sorted({o["open_id"] for o in D.OPEN_AFTER_THIS_STAGE}
               & {"E-01", "E-02", "E-03", "E-04"}),
        ["E-01", "E-02", "E-03", "E-04"], len(D.OPEN_AFTER_THIS_STAGE),
        "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("EVERY_OPEN_ITEM_NAMES_AN_OWNER", FREEZE_HONESTY,
        [o["open_id"] for o in D.OPEN_AFTER_THIS_STAGE if not o["owner"]], [],
        len(D.OPEN_AFTER_THIS_STAGE), "T04_FINAL_CONTENT_MODEL_v1.md")
    chk("FROZEN_IS_NOT_STATED_AS_APPROVED", FREEZE_HONESTY,
        [s for s in _strings([D.FINAL_QUIZ["q5_option_substitutions"]])
         if "BARIAH_APPROVED" in s], [],
        len(_strings([D.FINAL_QUIZ["q5_option_substitutions"]])),
        "T04_FINAL_QUIZ_v2.json")
    chk("VERDICT_IS_FROM_THE_ALLOWED_SET", FREEZE_HONESTY,
        D.VERDICT in D.ALLOWED_VERDICTS, True, len(D.ALLOWED_VERDICTS),
        "t04_authority_data_v1.py")

    # ==================== 12. PRODUCTION GUARDS ====================
    chk("NO_PPTX_GENERATED", PRODUCTION_GUARD, D.PPTX_GENERATED, 0, 1,
        "t04_authority_data_v1.py")
    chk("PRODUCTION_GENERATOR_UNTOUCHED", PRODUCTION_GUARD, D.GENERATOR_TOUCHED, 0, 1,
        "t04_authority_data_v1.py")
    chk("NO_MMD_PRODUCTION_STARTED", PRODUCTION_GUARD, D.MMD_PRODUCTION_STARTED, 0, 1,
        "t04_authority_data_v1.py")
    chk("NO_REACT_OR_SCORM_WORK", PRODUCTION_GUARD, D.REACT_OR_SCORM_STARTED, 0, 1,
        "t04_authority_data_v1.py")
    chk("AUTHORITY_ARTIFACTS_NOT_MODIFIED", PRODUCTION_GUARD,
        D.AUTHORITY_ARTIFACTS_MODIFIED, 0, 1, "t04_authority_data_v1.py")
    chk("NO_T04_PPTX_ON_DISK", PRODUCTION_GUARD,
        [f for f in os.listdir(T04) if f.lower().endswith(".pptx")], [],
        len(os.listdir(T04)), "docs/pl06/t04/")
    guard_blob = _strings([SEQ, D.FINAL_DIALOGUE, D.FINAL_RUMUSAN, D.FINAL_QUIZ, V,
                           D.EVIDENCE, REG, D.CONFIRMATIONS, STATES])
    chk("FORBIDDEN_LABELS_ABSENT_FROM_EVERY_RECORD", PRODUCTION_GUARD,
        sorted({lbl for lbl in D.FORBIDDEN_LABELS for s in guard_blob if lbl in s}), [],
        len(guard_blob), "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("FORBIDDEN_LABEL_DECLARATION_INTACT", PRODUCTION_GUARD,
        len(D.FORBIDDEN_LABELS), 8, len(D.FORBIDDEN_LABELS), "t04_authority_data_v1.py")
    chk("CAIR_NOT_NAMED_INSTRUCTIONAL_DESIGNER", PRODUCTION_GUARD,
        [s for s in guard_blob
         if re.search(r"CAIR[^.]{0,40}instructional designer", s, re.I)], [],
        len(guard_blob), "T04_FINAL_CONTENT_MODEL_v1.json")
    chk("AUTHORITY_IS_ALWAYS_BARIAH", PRODUCTION_GUARD,
        sorted({d["authority"] for d in REG}), ["BARIAH_AHMAD"], len(REG),
        "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    try:
        touched = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                                 capture_output=True, text=True, timeout=60).stdout
        gen_touched = [ln for ln in touched.splitlines()
                       if "reviews/source-completion/generator" in ln]
    except Exception:
        gen_touched = ["git-unavailable"]
    chk("FROZEN_TOOLCHAIN_UNMODIFIED_IN_THE_WORKING_TREE", PRODUCTION_GUARD,
        gen_touched, [], 1, "git status")

    # ==================== 13. REPORTING ====================
    chk("SUITE_ID_DECLARED", REPORTING, SUITE_ID,
        "T04_AUTHORITY_DECISION_INGESTION_QA_v1", 1, "t04_authority_qa_v1.py")
    chk("SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE", REPORTING, SUITE_ID != PRIOR_SUITE_ID,
        True, 2, "t04_authority_qa_v1.py")
    chk("NOT_CHECKED_IS_PUBLISHED", REPORTING, len(NOT_CHECKED) >= 8, True,
        len(NOT_CHECKED), "t04_authority_qa_v1.py")
    chk("NOT_CHECKED_NAMES_THE_UNRESOLVED_Q3", REPORTING,
        any("Q3" in x for x in NOT_CHECKED), True, len(NOT_CHECKED),
        "t04_authority_qa_v1.py")
    chk("NOT_CHECKED_NAMES_THE_OPEN_ROUND_TRIP", REPORTING,
        any("round trip" in x for x in NOT_CHECKED), True, len(NOT_CHECKED),
        "t04_authority_qa_v1.py")
    chk("EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT", REPORTING,
        [r["gate_id"] for r in res if not r["source_artifact"]], [], len(res),
        "t04_authority_qa_v1.py")
    chk("EVERY_GATE_DECLARES_A_POPULATION", REPORTING,
        [r["gate_id"] for r in res if r["population"] is None], [], len(res),
        "t04_authority_qa_v1.py")

    # ==================== 14. LIVE DERIVATION ====================
    # Three stages running, a fixture caught a gate reading a value cached at import: a
    # total (W-22), then a count (V-03), then a whole projection (X-34). Every snapshot this
    # module publishes for the emitter is therefore asserted equal to its live recomputation,
    # so an edit to the underlying data cannot pass unseen.
    chk("DECISION_REGISTER_SNAPSHOT_AGREES_WITH_LIVE", ACCOUNTING,
        D.DECISION_REGISTER == D._decision_register(), True, len(REG),
        "t04_authority_data_v1.py")
    chk("SCREEN_SEQUENCE_SNAPSHOT_AGREES_WITH_LIVE", ACCOUNTING,
        D.FINAL_SCREEN_SEQUENCE == D._final_sequence(), True, len(SEQ),
        "t04_authority_data_v1.py")
    chk("QUIZ_SNAPSHOT_AGREES_WITH_LIVE", ACCOUNTING,
        D.FINAL_QUIZ["items"] == D.quiz_items(), True, len(QUIZ),
        "t04_authority_data_v1.py")
    chk("DO_NOT_REUSE_SNAPSHOT_AGREES_WITH_LIVE", ACCOUNTING,
        D.FINAL_VISUAL_SCOPE["do_not_reuse_items"] == D._do_not_reuse_items(), True,
        len(DNR), "t04_authority_data_v1.py")
    chk("ASSET_GROUP_SNAPSHOT_AGREES_WITH_LIVE", ACCOUNTING,
        D.FINAL_VISUAL_SCOPE["asset_groups"] == D.asset_group_scope(), True, len(AGS),
        "t04_authority_data_v1.py")
    chk("FINAL_STATES_SNAPSHOT_AGREES_WITH_LIVE", ACCOUNTING,
        D.FINAL_STATES == D.final_states(), True, len(STATES),
        "t04_authority_data_v1.py")

    # ==================== 15. ACCOUNTING ====================
    chk("EVERY_GATE_IS_TYPED", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res),
        "t04_authority_qa_v1.py")
    chk("NO_DUPLICATE_GATE_IDS", ACCOUNTING,
        len({r["gate_id"] for r in res}), len(res), len(res), "t04_authority_qa_v1.py")
    chk("NO_VACUOUS_GATES", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res),
        "t04_authority_qa_v1.py")

    return res


def accounting(rows):
    by = {}
    for r in rows:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    return dict(SUITE_ID=SUITE_ID,
                ACTIVE_GATE_COUNT=len(rows),
                ACTIVE_GATES_PASSING=len([r for r in rows if r["ok"]]),
                TOTAL_EMITTED_GATE_RECORDS=len(rows),
                VACUOUS_GATES=[r["gate_id"] for r in rows if r["vacuous"]],
                DECLARED_EMPTY_GATES=[r["gate_id"] for r in rows if r["empty_by_design"]],
                POPULATION_TOTALS={r["gate_id"]: r["population"] for r in rows},
                SOURCE_ARTIFACTS=sorted({r["source_artifact"] for r in rows}),
                BY_TYPE=dict(sorted(by.items())),
                NOT_CHECKED=NOT_CHECKED,
                FAILING=[r["gate_id"] for r in rows if not r["ok"]])


if __name__ == "__main__":
    rows = run()
    a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows)
    t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        flag = "VACU" if r["vacuous"] else ("PASS" if r["ok"] else "FAIL")
        line = (f"{flag}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  "
                f"n={r['population']:<5} src={r['source_artifact']:<44} {r['value']!r}")
        print(line[:250] + ("" if r["ok"] else f"   EXPECTED {r['expected']!r}"[:200]))
    print()
    print(f"SUITE_ID = {a['SUITE_ID']}")
    print(f"{a['ACTIVE_GATES_PASSING']}/{a['ACTIVE_GATE_COUNT']} active gates PASS  ·  "
          f"{a['TOTAL_EMITTED_GATE_RECORDS']} emitted records")
    print(f"VACUOUS_GATES = {a['VACUOUS_GATES']}")
    print(f"DECLARED_EMPTY_GATES = {a['DECLARED_EMPTY_GATES']}")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<26} {v}")
    print()
    print("NOT_CHECKED:")
    for x in a["NOT_CHECKED"]:
        print(f"  - {x}")
    sys.exit(1 if a["FAILING"] else 0)
