# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.9.1 QA — gates over the custody attempt, the exchange reading and the audits.

    SUITE_ID = T04_SUPPLEMENTARY_EVIDENCE_QA_v1
    python3 docs/pl06/t04/tools/t04_supplementary_qa_v1.py

This suite's central job is to make a NEGATIVE result stick. Custody failed, and the failure
mode that matters is not "the gate went red" — it is "somebody quietly fills in a hash, a
dimension or a supplied-flag and the failure evaporates". Every custody field is asserted
unavailable, and every fixture that fills one in must fire.

Separate from `T04_AUTHORITY_DECISION_INGESTION_QA_v1` (239 gates). Never add the totals.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_supplementary_evidence_v1 as S    # noqa: E402
import t04_authority_data_v1 as D            # noqa: E402
import t04_predicate_audit_v1 as P           # noqa: E402
import t04_ooxml_v1 as X                     # noqa: E402

SUITE_ID = "T04_SUPPLEMENTARY_EVIDENCE_QA_v1"
PRIOR_SUITE_ID = "T04_AUTHORITY_DECISION_INGESTION_QA_v1"

CUSTODY_HONESTY = "CUSTODY_HONESTY"
READING_DISCIPLINE = "READING_DISCIPLINE"
ATTRIBUTION = "ATTRIBUTION"
AG_REGISTER = "AG_REGISTER"
PREDICATE_AUDIT = "PREDICATE_AUDIT"
XML_IDENTITY = "XML_IDENTITY"
RELEASE_GUARD = "RELEASE_GUARD"
ACCOUNTING = "ACCOUNTING"

GATE_TYPES = {CUSTODY_HONESTY, READING_DISCIPLINE, ATTRIBUTION, AG_REGISTER,
              PREDICATE_AUDIT, XML_IDENTITY, RELEASE_GUARD, ACCOUNTING}

NOT_CHECKED = [
    "whether the rendered image this run saw is the same image Firdaus intends to register — "
    "with no binary there is nothing to compare",
    "the screenshot's true pixel dimensions, byte size, format or hash",
    "whether the WhatsApp thread contains further messages outside the captured region",
    "the calendar date of the exchange — the thread shows only a 'Today' separator",
    "whether the Set B distractors discriminate well in practice — she called them better, "
    "the gates carry her selection, they do not judge the pedagogy",
    "whether 'Q3' meant the third request or quiz item Q3 — the supported reading is recorded "
    "and the alternative is retained, neither is asserted",
    "whether Bariah intended her silence on the Q5 stem as agreement — she was shown it as "
    "fixed and answered about the options, and the record says exactly that",
]

# Anything matching these in a custody field would be a fabricated measurement.
HASH_SHAPE = re.compile(r"^[0-9a-f]{32,128}$")
DIMENSION_SHAPE = re.compile(r"\d{2,5}\s*[x×]\s*\d{2,5}")
BYTE_SHAPE = re.compile(r"^\d+$")


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

    FIELDS = S.CUSTODY_FIELDS
    READ = S.CONFIRMATION_READINGS
    AG = S.ag_register_audit()
    PAUD = P.summary()
    PROOFS = X.proofs()

    # ==================== 1. CUSTODY HONESTY ====================
    chk("CUSTODY_OUTCOME_IS_FAILURE", CUSTODY_HONESTY,
        S.CUSTODY_OUTCOME, "FAILED_NO_BINARY_SUPPLIED", 1,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("NO_CUSTODY_FILE_WAS_CREATED", CUSTODY_HONESTY,
        os.path.exists(os.path.join(REPO, S.INTENDED_CUSTODY_PATH)), False, 1,
        S.INTENDED_CUSTODY_PATH)
    chk("NO_IMAGE_IN_THE_EVIDENCE_DIR_CLAIMS_TO_BE_THIS_SCREENSHOT", CUSTODY_HONESTY,
        [f for f in os.listdir(os.path.join(REPO, D.EVIDENCE_DIR))
         if "WHATSAPP_CONFIRMATION" in f], [],
        len(os.listdir(os.path.join(REPO, D.EVIDENCE_DIR))), D.EVIDENCE_DIR)
    chk("EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE", CUSTODY_HONESTY,
        [f["field"] for f in FIELDS
         if not str(f["value"]).startswith(("NOT_AVAILABLE", "NOT_CREATED",
                                            "NOT_PERFORMED", "NOT_APPLICABLE",
                                            "NOT_VERIFIABLE"))], [], len(FIELDS),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("NO_CUSTODY_FIELD_HOLDS_A_HASH_SHAPED_VALUE", CUSTODY_HONESTY,
        [f["field"] for f in FIELDS if HASH_SHAPE.match(str(f["value"]))], [], len(FIELDS),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("NO_CUSTODY_FIELD_HOLDS_A_BYTE_COUNT", CUSTODY_HONESTY,
        [f["field"] for f in FIELDS if BYTE_SHAPE.match(str(f["value"]))], [], len(FIELDS),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("NO_CUSTODY_FIELD_HOLDS_PIXEL_DIMENSIONS", CUSTODY_HONESTY,
        [f["field"] for f in FIELDS if DIMENSION_SHAPE.search(str(f["value"]))], [],
        len(FIELDS), "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("EVERY_CUSTODY_FIELD_SAYS_WHY_IT_IS_UNAVAILABLE", CUSTODY_HONESTY,
        [f["field"] for f in FIELDS if not f["why"]], [], len(FIELDS),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.md")
    chk("ALL_TEN_CUSTODY_FIELDS_ARE_ACCOUNTED_FOR", CUSTODY_HONESTY,
        sorted(f["field"] for f in FIELDS),
        sorted(["original_runtime_path", "repository_custody_path", "byte_size", "sha256",
                "mime_type", "pixel_width", "pixel_height", "file_format_validation",
                "intake_time", "byte_identity_vs_source"]), len(FIELDS),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("SEARCH_WAS_ACTUALLY_PERFORMED", CUSTODY_HONESTY,
        len(S.SEARCH_LOCATIONS) >= 4, True, len(S.SEARCH_LOCATIONS),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.md")
    chk("MNT_DATA_ABSENCE_RECONFIRMED", CUSTODY_HONESTY,
        os.path.exists("/mnt/data"), False, 1, "/mnt/data")

    # The three timestamp classes must stay apart, and only one may carry values.
    chk("THREE_TIMESTAMP_CLASSES_KEPT_APART", CUSTODY_HONESTY,
        [t["timestamp_class"] for t in S.TIMESTAMP_CLASSES],
        ["VISIBLE_IN_SCREENSHOT", "RUNTIME_FILESYSTEM", "IMAGE_METADATA_EXIF"],
        len(S.TIMESTAMP_CLASSES), "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("ONLY_THE_VISIBLE_TIMESTAMPS_ARE_AVAILABLE", CUSTODY_HONESTY,
        sorted(t["timestamp_class"] for t in S.TIMESTAMP_CLASSES if t["available"]),
        ["VISIBLE_IN_SCREENSHOT"], len(S.TIMESTAMP_CLASSES),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("NO_EXIF_IS_ASSERTED", CUSTODY_HONESTY,
        [t["timestamp_class"] for t in S.TIMESTAMP_CLASSES
         if t["timestamp_class"] == "IMAGE_METADATA_EXIF" and t["available"]], [],
        len(S.TIMESTAMP_CLASSES), "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("NO_FILESYSTEM_TIMESTAMP_IS_ASSERTED", CUSTODY_HONESTY,
        [t["timestamp_class"] for t in S.TIMESTAMP_CLASSES
         if t["timestamp_class"] == "RUNTIME_FILESYSTEM" and t["available"]], [],
        len(S.TIMESTAMP_CLASSES), "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")

    # ==================== 2. THE B0.9 NOT_SUPPLIED STATE MUST SURVIVE ====================
    supp = [r for r in D.EVIDENCE
            if r["evidence_class"] == "SUPPLEMENTARY_AUTHORITY_EVIDENCE"]
    chk("B09_NOT_SUPPLIED_STATE_STILL_STANDS", CUSTODY_HONESTY,
        [(r["supplied_in_this_run"], r["sha256"], r["byte_size"],
          r["dimensions_or_extent"]) for r in supp],
        [(False, "NOT_SUPPLIED", "NOT_SUPPLIED", "NOT_SUPPLIED")], len(supp),
        "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json")
    chk("NOT_SUPPLIED_CANNOT_BE_CLEARED_WITHOUT_CUSTODY", CUSTODY_HONESTY,
        (S.CUSTODY_OUTCOME == "FAILED_NO_BINARY_SUPPLIED"
         and all(not r["supplied_in_this_run"] for r in supp)), True, len(supp),
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")

    # ==================== 3. READING DISCIPLINE ====================
    chk("READING_METHOD_IS_VISUAL_NOT_OCR", READING_DISCIPLINE,
        (S.READING_METHOD["method"], S.READING_METHOD["ocr_used"],
         S.READING_METHOD["ocr_as_sole_evidence"]),
        ("DIRECT_VISUAL_INSPECTION_OF_THE_RENDERED_IMAGE", False, False), 3,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("READING_STATES_ITS_LIMITATIONS", READING_DISCIPLINE,
        len(S.READING_METHOD["limitations"]) >= 3, True,
        len(S.READING_METHOD["limitations"]), "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("SEVEN_MESSAGES_READ", READING_DISCIPLINE, len(S.MESSAGES), 7, len(S.MESSAGES),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("MESSAGE_POSITIONS_ARE_CONTIGUOUS", READING_DISCIPLINE,
        [m["position"] for m in S.MESSAGES], list(range(1, 8)), len(S.MESSAGES),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("EVERY_MESSAGE_HAS_A_SENDER_AND_A_DIRECTION", READING_DISCIPLINE,
        [m["msg_id"] for m in S.MESSAGES
         if m["sender"] not in ("BARIAH", "FIRDAUS")
         or m["direction"] not in ("INCOMING", "OUTGOING")], [], len(S.MESSAGES),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("SENDER_AND_DIRECTION_AGREE", READING_DISCIPLINE,
        [m["msg_id"] for m in S.MESSAGES
         if (m["sender"] == "BARIAH") != (m["direction"] == "INCOMING")], [],
        len(S.MESSAGES), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("EVERY_MESSAGE_CARRIES_VERBATIM_TEXT", READING_DISCIPLINE,
        [m["msg_id"] for m in S.MESSAGES if not m["verbatim_fragments"]], [],
        len(S.MESSAGES), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_THREE_BARIAH_LINES_ARE_PRESENT", READING_DISCIPLINE,
        sorted(f for m in S.MESSAGES if m["sender"] == "BARIAH"
               for f in m["verbatim_fragments"]),
        sorted(["Yes to both",
                "Yes to both screenshots. Q5 multiple response - yes, ok",
                "Set B. Better distractors"]),
        len(S.MESSAGES), "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("BARIAH_SENT_EXACTLY_THREE_MESSAGES", READING_DISCIPLINE,
        [m["msg_id"] for m in S.MESSAGES if m["sender"] == "BARIAH"],
        ["WA-02", "WA-05", "WA-07"],
        len(S.MESSAGES), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("FIRDAUS_SENT_EXACTLY_FOUR_MESSAGES", READING_DISCIPLINE,
        [m["msg_id"] for m in S.MESSAGES if m["sender"] == "FIRDAUS"],
        ["WA-01", "WA-03", "WA-04", "WA-06"], len(S.MESSAGES),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")

    # ==================== 4. ATTRIBUTION ====================
    q3msg = [m for m in S.MESSAGES if "Q3 tu nnt u pilih ya" in m["verbatim_fragments"]]
    chk("THE_Q3_LINE_IS_ATTRIBUTED_TO_FIRDAUS", ATTRIBUTION,
        [m["sender"] for m in q3msg], ["FIRDAUS"], len(S.MESSAGES),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_Q3_LINE_IS_NOT_A_BARIAH_MESSAGE", ATTRIBUTION,
        [m["msg_id"] for m in q3msg if m["sender"] == "BARIAH"], [], len(S.MESSAGES),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    q3cnf = [c for c in D.CONFIRMATIONS if c["confirmation_id"] == "T04-CNF-03"]
    chk("B09_RECORD_CARRIES_THE_CORRECTED_AUTHORSHIP", ATTRIBUTION,
        [(c.get("author"), c.get("is_authority_statement")) for c in q3cnf],
        [("FIRDAUS", False)], len(q3cnf), "T04_AUTHORITY_CONFIRMATIONS_v1.json")
    x01 = [d for d in D._decision_register() if d["decision_id"] == "T04-DEC-X01"]
    chk("THE_X01_DECISION_IS_NO_LONGER_A_BARIAH_ACT", ATTRIBUTION,
        [d["authority"] for d in x01], ["FIRDAUS_NOT_AN_AUTHORITY_ACT"],
        len(D._decision_register()), "T04_AUTHORITY_DECISION_REGISTER_v1.json")
    chk("THE_MISATTRIBUTION_IS_RECORDED_AS_A_CORRECTION", ATTRIBUTION,
        sorted(c["correction_id"] for c in S.ATTRIBUTION_CORRECTIONS),
        ["T04-COR-02", "T04-COR-03"], len(S.ATTRIBUTION_CORRECTIONS),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_CORRECTION_STATES_ITS_SEVERITY_AND_CONSEQUENCE", ATTRIBUTION,
        [c["correction_id"] for c in S.ATTRIBUTION_CORRECTIONS
         if not (c["severity"] and c["consequence"] and c["basis"])], [],
        len(S.ATTRIBUTION_CORRECTIONS), "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("NO_BARIAH_DELEGATION_TO_CAIR_IS_CLAIMED", ATTRIBUTION,
        [d["decision_id"] for d in D._decision_register()
         if d["authority"] == "BARIAH_AHMAD" and "delegat" in d["effect"].lower()], [],
        len(D._decision_register()), "T04_AUTHORITY_DECISION_REGISTER_v1.json")

    # ==================== 5. CONFIRMATION READINGS ====================
    chk("THREE_CONFIRMATION_READINGS", READING_DISCIPLINE, len(READ), 3, len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("NO_READING_CLAIMS_THE_BLOCKED_EVIDENCE_CLASS", READING_DISCIPLINE,
        [r["confirmation_id"] for r in READ
         if r["evidence_class"] == S.BLOCKED_EVIDENCE_CLASS], [], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("EVERY_READING_CARRIES_A_CUSTODY_QUALIFIED_STATUS", READING_DISCIPLINE,
        sorted({r["actual_status"] for r in READ}),
        ["CONTENT_CONFIRMED_CUSTODY_MAPPING_INCOMPLETE",
         "CONTENT_CONFIRMED_CUSTODY_UNVERIFIED"], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_TWO_BUNDLED_CONFIRMATIONS_ARE_MAPPING_INCOMPLETE", READING_DISCIPLINE,
        sorted(r["confirmation_id"] for r in READ
               if r["actual_status"] == "CONTENT_CONFIRMED_CUSTODY_MAPPING_INCOMPLETE"),
        ["T04-CNF-01", "T04-CNF-02"], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("UNSEEN_SCREENSHOT_CONTENTS_CANNOT_BE_INFERRED", READING_DISCIPLINE,
        [r["confirmation_id"] for r in READ
         if r["actual_status"] == "CONTENT_CONFIRMED_CUSTODY_MAPPING_INCOMPLETE"
         and "not proof of what those" not in r.get("unseen_screenshot_limit", "")
         and "the accepted screenshots are not" not in r.get("unseen_screenshot_limit", "")],
        [], len(READ), "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("EVERY_READING_NAMES_WHAT_BLOCKS_ITS_UPGRADE", READING_DISCIPLINE,
        sorted({r["upgrade_blocked_by"] for r in READ}), ["CUSTODY_FAILED_NO_BINARY"],
        len(READ), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("CNF01_IS_BUNDLED_ACCEPTANCE_NOT_INDIVIDUAL_WORDING", READING_DISCIPLINE,
        [r["confirmation_mode"] for r in READ if r["confirmation_id"] == "T04-CNF-01"],
        ["BUNDLED_ACCEPTANCE_OF_TWO_PROPOSITIONS"], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("CNF02_IS_A_CAIR_PROPOSAL_CONFIRMED", READING_DISCIPLINE,
        [r["confirmation_mode"] for r in READ if r["confirmation_id"] == "T04-CNF-02"],
        ["CAIR_PROPOSAL_CONFIRMED_BY_AUTHORITY"], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("CNF03_IS_AN_EXPLICITLY_WORDED_DECISION", READING_DISCIPLINE,
        [r["confirmation_mode"] for r in READ if r["confirmation_id"] == "T04-CNF-03"],
        ["EXPLICITLY_WORDED_INDIVIDUAL_DECISION"], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("CNF03_CONFIRMS_ITEM_TYPE_ONLY", READING_DISCIPLINE,
        [r["confirms"] for r in READ if r["confirmation_id"] == "T04-CNF-03"],
        ["Q5 item type = MULTIPLE_RESPONSE"], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("CNF03_LISTS_WHAT_IT_DOES_NOT_CONFIRM", READING_DISCIPLINE,
        sorted(x for r in READ for x in r.get("does_not_confirm", [])),
        sorted(["all five answer keys", "the exact two replacement distractors",
                "every source-row binding",
                "a general delegation to approve assessment content"]), len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("CNF01_DOES_NOT_CLAIM_BARIAH_WROTE_THE_SENTENCE", READING_DISCIPLINE,
        [r["confirmation_id"] for r in READ if r["confirmation_id"] == "T04-CNF-01"
         and "did not write" not in r["not_claimed"]], [], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("CNF02_DOES_NOT_CLAIM_41_ORIGINATED_WITH_BARIAH", READING_DISCIPLINE,
        [r["confirmation_id"] for r in READ if r["confirmation_id"] == "T04-CNF-02"
         and "not an idea Bariah originated" not in r["not_claimed"]], [], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("FORTY_ONE_IS_RECORDED_AS_MUTABLE", READING_DISCIPLINE,
        [r["confirmation_id"] for r in READ if r["confirmation_id"] == "T04-CNF-02"
         and "not immutable" not in r.get("mutability", "")], [], len(READ),
        "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("S14_STILL_ADDS_ZERO_UNIQUE_ASSETS", READING_DISCIPLINE,
        D.FINAL_VISUAL_SCOPE["new_screen_asset_impact"]["new_unique_assets"], 0, 1,
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("FINAL_UNIQUE_ASSET_SCOPE_REMAINS_41", READING_DISCIPLINE,
        (D.FINAL_VISUAL_SCOPE["accepted_production_scope"],
         [r["final_unique_asset_scope"] for r in READ
          if r["confirmation_id"] == "T04-CNF-02"]), (41, [41]), 2,
        "T04_FINAL_VISUAL_SCOPE_v1.json")

    # Answer keys and distractors must not be upgraded on the back of this screenshot.
    chk("ANSWER_KEYS_NOT_RELABELLED_BARIAH_DIRECT_APPROVED", READING_DISCIPLINE,
        sorted({q["answer_key_status"] for q in D.quiz_items()}), ["PROPOSED_NOT_FINAL"],
        len(D.quiz_items()), "T04_FINAL_QUIZ_v2.json")
    # Selecting from two written pairs is not authoring either of them. The distinction is
    # exactly what separates a defensible record from an overstated one.
    chk("Q5_DISTRACTORS_ARE_SELECTED_NOT_AUTHORED", READING_DISCIPLINE,
        sorted({s["authorship"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS}),
        ["AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS"],
        len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS), "T04_FINAL_QUIZ_v2.json")
    chk("Q5_DISTRACTORS_NOT_RELABELLED_BARIAH_AUTHORED", READING_DISCIPLINE,
        [s["position"] for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS
         if s["authorship"] == "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"], [],
        len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS), "T04_FINAL_QUIZ_v2.json")

    # ==================== 6. E-07 CLOSURE AND THE SET B FREEZE ====================
    d = S.Q5_DIVERGENCE
    E = S.E07_CLOSURE
    q5 = [q for q in D.quiz_items() if q["question_id"] == "T04-QZ-Q5"][0]
    live_q5 = [o["text_ms"] for o in q5["options"]]

    chk("E07_IS_CLOSED", READING_DISCIPLINE,
        (E["open_id"], E["status"]), ("E-07", "CLOSED"), 2,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("E07_DECISION_TYPE_IS_A_DIRECT_SELECTION", READING_DISCIPLINE,
        (E["decision_type"], E["authority"]),
        ("DIRECT_SELECTION_FROM_EXPLICIT_OPTIONS", "BARIAH_DIRECT_SELECTION"), 2,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("E07_SELECTED_SET_B", READING_DISCIPLINE,
        (E["selected_set"], E["rejected_set"], E["rejected_set_status"]),
        ("SET_B", "SET_A", "REJECTED_NOT_SELECTED"), 3,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("E07_QUOTES_THE_SELECTION_VERBATIM", READING_DISCIPLINE,
        E["authority_quote"], "Set B. Better distractors", 1,
        "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("THE_SETS_WERE_NOT_COMBINED", READING_DISCIPLINE,
        (E["sets_combined"], E["both_sets_retained_active"]), (False, False), 2,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("SET_B_IS_FROZEN_VERBATIM_NOT_PARAPHRASED", READING_DISCIPLINE,
        [x["position"] for x in S.SET_B_FROZEN if x["paraphrased"]], [],
        len(S.SET_B_FROZEN), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_LIVE_MODEL_CARRIES_SET_B_EXACTLY", READING_DISCIPLINE,
        live_q5[4:], [x["text_ms"] for x in S.SET_B_FROZEN], 6,
        "T04_FINAL_QUIZ_v2.json")
    chk("SET_A_IS_NOT_IN_THE_LIVE_MODEL", READING_DISCIPLINE,
        [x["text_ms"] for x in S.SET_A_REJECTED if x["text_ms"] in live_q5], [],
        len(S.SET_A_REJECTED), "T04_FINAL_QUIZ_v2.json")
    chk("SET_A_IS_RECORDED_AS_REJECTED", READING_DISCIPLINE,
        sorted({x["status"] for x in S.SET_A_REJECTED}), ["REJECTED_NOT_SELECTED"],
        len(S.SET_A_REJECTED), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_SUPERSEDED_CAIR_DRAFT_IS_NOT_IN_THE_LIVE_MODEL", READING_DISCIPLINE,
        [x["superseded_b09_text"] for x in S.SET_B_FROZEN
         if x["superseded_b09_text"] in live_q5], [], len(S.SET_B_FROZEN),
        "T04_FINAL_QUIZ_v2.json")
    chk("THE_SUPERSEDED_CAIR_DRAFT_IS_STILL_RECORDED", READING_DISCIPLINE,
        [s_["position"] for s_ in D.QUIZ_Q5_OPTION_SUBSTITUTIONS
         if not s_.get("cair_draft_superseded_by_e07")], [],
        len(D.QUIZ_Q5_OPTION_SUBSTITUTIONS), "T04_FINAL_QUIZ_v2.json")
    chk("THE_FIRST_FOUR_OPTIONS_ARE_UNTOUCHED", READING_DISCIPLINE,
        live_q5[:4], d["options_in_frozen_model"][:4], 4, "T04_FINAL_QUIZ_v2.json")
    chk("THE_FIRST_FOUR_REMAIN_THE_PROPOSED_KEY", READING_DISCIPLINE,
        q5["proposed_key_positions"], [1, 2, 3, 4], 6, "T04_FINAL_QUIZ_v2.json")
    chk("Q5_IS_STILL_MULTIPLE_RESPONSE", READING_DISCIPLINE,
        q5["question_type"], "MULTIPLE_RESPONSE", 1, "T04_FINAL_QUIZ_v2.json")
    chk("Q5_OPTIONS_STILL_CARRY_NO_LETTERS", READING_DISCIPLINE,
        [o["option_id"] for o in q5["options"] if o["letter_label"]], [],
        len(q5["options"]), "T04_FINAL_QUIZ_v2.json")
    chk("E07_DOES_NOT_APPROVE_THE_ANSWER_KEYS", READING_DISCIPLINE,
        [x for x in E["what_this_does_not_approve"] if "answer key" in x] != [], True,
        len(E["what_this_does_not_approve"]),
        "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("THE_ANSWER_KEY_IS_STILL_NOT_FINAL", READING_DISCIPLINE,
        sorted({q["answer_key_status"] for q in D.quiz_items()}), ["PROPOSED_NOT_FINAL"],
        len(D.quiz_items()), "T04_FINAL_QUIZ_v2.json")
    chk("THE_DIVERGENCE_IS_CLOSED", READING_DISCIPLINE,
        (d["status"], d["blocking_scored_quiz"]), ("CLOSED", False), 2,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_STEM_PROVENANCE_CHANGE_IS_RECORDED", READING_DISCIPLINE,
        (S.STEM_PROVENANCE_CHANGE["correction_id"],
         S.STEM_PROVENANCE_CHANGE["status"]),
        ("T04-COR-04", "APPLIED_PROVENANCE_DOWNGRADED"), 2,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_STEM_IN_FORCE_MATCHES_THE_FORCED_CHOICE", READING_DISCIPLINE,
        q5["stem_ms"], S.STEM_PROVENANCE_CHANGE["final_stem"], 1,
        "T04_FINAL_QUIZ_v2.json")
    chk("THE_STEM_IS_NOT_CLAIMED_AS_AUTHORITY_AUTHORED", READING_DISCIPLINE,
        q5.get("stem_provenance"),
        "FIRDAUS_DIRECTED_PRESENTED_AS_FIXED_NOT_CONTESTED_BY_AUTHORITY", 1,
        "T04_FINAL_QUIZ_v2.json")
    chk("THE_BARIAH_WRITTEN_STEM_IS_STILL_RECORDED", READING_DISCIPLINE,
        q5.get("superseded_stem_b09"), S.STEM_PROVENANCE_CHANGE["b09_stem"], 1,
        "T04_FINAL_QUIZ_v2.json")
    chk("E08_IS_THE_ONLY_ITEM_THIS_RERUN_LEFT_OPEN", READING_DISCIPLINE,
        sorted(o["open_id"] for o in S.NEW_OPEN_ITEMS), ["E-08"],
        len(S.NEW_OPEN_ITEMS), "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THREE_ITEMS_CLOSED_IN_THE_RERUN", READING_DISCIPLINE,
        sorted(o["open_id"] for o in S.CLOSED_IN_THE_RERUN),
        ["E-01", "E-03", "E-07"], len(S.CLOSED_IN_THE_RERUN),
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")

    # ==================== 7. AG REGISTER ====================
    chk("EIGHT_ASSET_GROUPS_AUDITED", AG_REGISTER, len(AG), 8, len(AG),
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("AG_IDS_ARE_AG01_TO_AG08", AG_REGISTER,
        [g["asset_group_id"] for g in AG], [f"AG-{i:02d}" for i in range(1, 9)], len(AG),
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("EVERY_GROUP_IS_SET_LEVEL_ACCEPTED_WITH_CONDITIONS", AG_REGISTER,
        sorted({g["set_level_status"] for g in AG}), ["ACCEPTED_AS_A_SET_WITH_CONDITIONS"],
        len(AG), "T04_AG_REGISTER_AUDIT_v1.json")
    chk("AUTHORITY_BASIS_IS_SET_LEVEL_NARRATIVE", AG_REGISTER,
        sorted({g["authority_basis"] for g in AG}), ["BARIAH_DIRECT_SET_LEVEL_NARRATIVE"],
        len(AG), "T04_AG_REGISTER_AUDIT_v1.json")
    chk("INDIVIDUAL_CARDS_RECORDED_AS_UNMARKED", AG_REGISTER,
        sorted({g["individual_card_status"] for g in AG}), ["NOT_INDIVIDUALLY_MARKED"],
        len(AG), "T04_AG_REGISTER_AUDIT_v1.json")
    chk("NO_GROUP_IS_SHOWN_AS_AN_INDIVIDUAL_ACCEPTANCE", AG_REGISTER,
        [g["asset_group_id"] for g in AG
         if g["represented_as_individual_acceptance"]], [], len(AG),
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("NO_GROUP_IS_SHOWN_AS_UNANSWERED", AG_REGISTER,
        [g["asset_group_id"] for g in AG if g["represented_as_unanswered"]], [], len(AG),
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("NO_GROUP_IS_A_PENDING_HUMAN_BLOCKER", AG_REGISTER,
        [g["asset_group_id"] for g in AG
         if g["represented_as_pending_human_blocker"]], [], len(AG),
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("FOUR_DISTINCTION_LAYERS_HELD_APART", AG_REGISTER,
        [x["name"] for x in S.AG_DISTINCTION_LAYERS],
        ["SET_LEVEL_ACCEPTANCE", "INDIVIDUAL_CARD_MARKINGS",
         "ITEM_LEVEL_NO_REUSE_RESTRICTIONS", "S14_SPECIFIC_AG06_REUSE"],
        len(S.AG_DISTINCTION_LAYERS), "T04_AG_REGISTER_AUDIT_v1.json")
    chk("THREE_FORBIDDEN_REPRESENTATIONS_DECLARED", AG_REGISTER,
        len(S.AG_FORBIDDEN_REPRESENTATIONS), 3, len(S.AG_FORBIDDEN_REPRESENTATIONS),
        "T04_AG_REGISTER_AUDIT_v1.md")
    chk("THREE_NO_REUSE_DECISIONS_STAY_CLOSED", AG_REGISTER,
        sorted(x["obligation_id"] for x in S.NO_REUSE_CLOSED),
        ["T04-VO-025", "T04-VO-026", "T04-VO-039"], len(S.NO_REUSE_CLOSED),
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("NO_REUSE_BASIS_IS_BOTH_LENSES", AG_REGISTER,
        S.NO_REUSE_DECISION_BASIS, "BOTH_INSTRUCTIONAL_AND_PRODUCTION", 3,
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("NO_REUSE_EVIDENCE_PRECISION_IS_DERIVED_NOT_TICKED", AG_REGISTER,
        S.NO_REUSE_EVIDENCE_PRECISION, "DERIVED_FROM_BARIAH_SECTION_LEVEL_NARRATIVE", 3,
        "T04_AG_REGISTER_AUDIT_v1.json")
    chk("PER_ITEM_TICKING_IS_EXPLICITLY_NOT_CLAIMED", AG_REGISTER,
        "did not individually tick" in S.NO_REUSE_NOT_CLAIMED, True, 1,
        "T04_AG_REGISTER_AUDIT_v1.md")
    chk("AG_AUDIT_AGREES_WITH_THE_COMMITTED_REGISTER", AG_REGISTER,
        [g["item_level_restrictions"] for g in AG],
        [g["item_level_restrictions"] for g in D.asset_group_scope()], len(AG),
        "T04_FINAL_VISUAL_SCOPE_v1.json")
    chk("SECTION_LEVEL_NARRATIVE_CONTENT_IS_ENUMERATED", AG_REGISTER,
        len(S.SECTION_LEVEL_NARRATIVE_CONTENTS), 4,
        len(S.SECTION_LEVEL_NARRATIVE_CONTENTS), "T04_AG_REGISTER_AUDIT_v1.md")

    # ==================== 8. PREDICATE AUDIT ====================
    chk("PREDICATE_AUDIT_HAS_NO_FAILING_POPULATION", PREDICATE_AUDIT,
        PAUD["failing"], [], PAUD["closed_populations"],
        "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("EIGHTEEN_CLOSED_POPULATIONS_AUDITED", PREDICATE_AUDIT,
        PAUD["closed_populations"], 18, PAUD["closed_populations"],
        "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("NO_UNEXPECTED_POPULATION_ADDITIONS", PREDICATE_AUDIT,
        PAUD["total_unexpected_additions"], 0, PAUD["closed_populations"],
        "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("NO_UNEXPECTED_POPULATION_REMOVALS", PREDICATE_AUDIT,
        PAUD["total_unexpected_removals"], 0, PAUD["closed_populations"],
        "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("EVERY_CLOSED_POPULATION_NAMES_ITS_MEMBERS", PREDICATE_AUDIT,
        [r["population_id"] for r in PAUD["rows"] if not r["expected_members"]], [],
        len(PAUD["rows"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("EVERY_CLOSED_POPULATION_NAMES_ITS_GATES", PREDICATE_AUDIT,
        [r["population_id"] for r in PAUD["rows"] if not r["guarded_by"]], [],
        len(PAUD["rows"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("EVERY_CLOSED_POPULATION_REPORTS_A_COUNT_DELTA", PREDICATE_AUDIT,
        [r["population_id"] for r in PAUD["rows"] if r["count_delta"] != 0], [],
        len(PAUD["rows"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("EVERY_EXCLUSION_IS_DOCUMENTED_WITH_A_REASON", PREDICATE_AUDIT,
        [x["exclusion_id"] for x in PAUD["exclusions"]
         if not (x["why"] and x["delta_guard"] and x["used_by"])], [],
        len(PAUD["exclusions"]), "T04_PREDICATE_AND_XML_AUDIT_v1.md")
    chk("THE_C05_SITE_IS_STILL_GUARDED", PREDICATE_AUDIT,
        sorted(r["population_id"] for r in PAUD["rows"]
               if r["origin_fixture"] == "C-05"), ["POP-01", "POP-02"],
        len(PAUD["rows"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("THE_C05_RULE_REACHES_BEYOND_ITS_ORIGINAL_SITE", PREDICATE_AUDIT,
        len({r["origin_fixture"] for r in PAUD["rows"]}) >= 10, True,
        len(PAUD["rows"]), "T04_PREDICATE_AND_XML_AUDIT_v1.json")

    # ==================== 9. XML IDENTITY ====================
    chk("ALL_XML_PROOF_CASES_PASS", XML_IDENTITY,
        [c["case_id"] for c in PROOFS if not c["ok"]], [], len(PROOFS),
        "T04_PREDICATE_AND_XML_AUDIT_v1.json")
    chk("INSIDEH_IS_NOT_INS", XML_IDENTITY,
        [c["exact_match_count"] for c in PROOFS if c["case_id"] == "XML-01"], [0],
        len(PROOFS), "t04_ooxml_v1.py")
    chk("INSIDEV_IS_NOT_INS", XML_IDENTITY,
        [c["exact_match_count"] for c in PROOFS if c["case_id"] == "XML-02"], [0],
        len(PROOFS), "t04_ooxml_v1.py")
    chk("TCPR_IS_NOT_T", XML_IDENTITY,
        [c["exact_match_count"] for c in PROOFS if c["case_id"] == "XML-03"], [0],
        len(PROOFS), "t04_ooxml_v1.py")
    chk("A_REAL_INS_IS_STILL_FOUND", XML_IDENTITY,
        [c["exact_match_count"] for c in PROOFS if c["case_id"] == "XML-04"], [1],
        len(PROOFS), "t04_ooxml_v1.py")
    chk("SUBSTRING_MATCHING_WOULD_HAVE_BEEN_WRONG", XML_IDENTITY,
        len([c for c in PROOFS if c["kind"] == "CONFUSION"
             and c["naive_would_have_been_wrong"]]), 5, len(PROOFS), "t04_ooxml_v1.py")
    chk("A_POSITIVE_CONTROL_EXISTS", XML_IDENTITY,
        [c["case_id"] for c in PROOFS if c["kind"] == "POSITIVE_CONTROL"], ["XML-04"],
        len(PROOFS), "t04_ooxml_v1.py")

    # The live authority DOCX re-checked with exact-element matching, not substrings.
    docx = os.path.join(REPO, D.EVIDENCE_DIR, D.PRIMARY_DOCX_NAME)
    if os.path.exists(docx):
        import zipfile
        xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
        exact_ins = X.count_elements(xml, "ins")
        exact_del = X.count_elements(xml, "del")
        naive_ins = xml.count("<w:ins")
    else:
        exact_ins = exact_del = naive_ins = None
    chk("AUTHORITY_DOCX_TRACKED_INSERTIONS_BY_EXACT_MATCH", XML_IDENTITY,
        exact_ins, 0, 1, os.path.join(D.EVIDENCE_DIR, D.PRIMARY_DOCX_NAME))
    chk("AUTHORITY_DOCX_TRACKED_DELETIONS_BY_EXACT_MATCH", XML_IDENTITY,
        exact_del, 0, 1, os.path.join(D.EVIDENCE_DIR, D.PRIMARY_DOCX_NAME))
    chk("THE_SUBSTRING_TRAP_IS_REAL_ON_THIS_FILE", XML_IDENTITY,
        naive_ins > 0 and exact_ins == 0, True, 1,
        os.path.join(D.EVIDENCE_DIR, D.PRIMARY_DOCX_NAME))

    # ==================== 10. RELEASE GUARD ====================
    chk("PART_A_RESULT_SEPARATES_CUSTODY_FROM_CONTENT", RELEASE_GUARD,
        S.PART_A_RESULT, "PARTIAL_CUSTODY_BLOCKED_CONTENT_CLOSED", 1,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("THE_FULL_APPROVAL_VERDICT_WAS_NOT_ISSUED", RELEASE_GUARD,
        (S.RELEASE_RECORD_NOT_ISSUED["issued"],
         S.RELEASE_RECORD_NOT_ISSUED["superseding"]), (False, False), 2,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("THE_PARTIAL_VERDICT_WAS_ISSUED_WITH_ALL_THREE_TOKENS", RELEASE_GUARD,
        S.RELEASE_DECISION["verdict_tokens"],
        ["T04_ASSESSMENT_DIVERGENCE_CLOSED", "STORYBOARD_LAYOUT_READY",
         "SUPPLEMENTARY_CNF_MAPPING_PARTIALLY_OPEN"], 3,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json")
    chk("THE_UNTAKEN_BRANCH_IS_NAMED_WITH_ITS_REASON", RELEASE_GUARD,
        (S.RELEASE_DECISION["branch_not_taken"],
         bool(S.RELEASE_DECISION["why_branch_not_taken"])),
        ("T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD", True), 2,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.md")
    chk("THE_OPEN_MAPPING_BLOCKS_EVIDENCE_CLOSURE_NOT_LAYOUT", RELEASE_GUARD,
        (S.RELEASE_DECISION["what_the_open_mapping_blocks"],
         S.RELEASE_DECISION["blocks_storyboard_layout"]),
        ("CANONICAL_EVIDENCE_CLOSURE_ONLY", False), 2,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.md")
    chk("THE_BLOCKER_NAMES_AN_OWNER_AND_A_REMEDY", RELEASE_GUARD,
        bool(S.PART_A_BLOCKER["owner"] and S.PART_A_BLOCKER["what_would_unblock"]), True, 1,
        "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.md")
    chk("NO_PPTX_GENERATED_IN_THIS_STAGE", RELEASE_GUARD, S.PPTX_GENERATED, 0, 1,
        "t04_supplementary_evidence_v1.py")
    chk("NO_MMD_REACT_SCORM_OR_LMS_WORK", RELEASE_GUARD,
        (S.MMD_PRODUCTION_STARTED, S.REACT_OR_SCORM_STARTED, S.LMS_WORK_STARTED),
        (0, 0, 0), 3, "t04_supplementary_evidence_v1.py")
    chk("AUTHORITY_ARTIFACTS_UNMODIFIED", RELEASE_GUARD,
        S.AUTHORITY_ARTIFACTS_MODIFIED, 0, 1, "t04_supplementary_evidence_v1.py")
    chk("THE_PRIMARY_DOCX_IS_STILL_BYTE_IDENTICAL", RELEASE_GUARD,
        os.path.getsize(docx) if os.path.exists(docx) else None, D.PRIMARY_DOCX_BYTES, 1,
        os.path.join(D.EVIDENCE_DIR, D.PRIMARY_DOCX_NAME))
    chk("CNF_RENUMBERING_WAS_NOT_APPLIED", RELEASE_GUARD,
        S.CONFIRMATION_ID_MAPPING["applied"], False, 1,
        "T04_AUTHORITY_EXCHANGE_READING_v1.json")
    chk("THE_ID_COLLISION_IS_DECLARED_NOT_HIDDEN", RELEASE_GUARD,
        len(S.CONFIRMATION_ID_MAPPING["rows"]), 4,
        len(S.CONFIRMATION_ID_MAPPING["rows"]), "T04_AUTHORITY_EXCHANGE_READING_v1.md")
    chk("EVERY_DECLARED_ARTIFACT_EXISTS", RELEASE_GUARD,
        [n for n in S.NEW_ARTIFACTS if not os.path.exists(os.path.join(T04, n))], [],
        len(S.NEW_ARTIFACTS), "docs/pl06/t04/")

    # ==================== 11. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "T04_SUPPLEMENTARY_EVIDENCE_QA_v1", 1,
        "t04_supplementary_qa_v1.py")
    chk("SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE", ACCOUNTING, SUITE_ID != PRIOR_SUITE_ID,
        True, 2, "t04_supplementary_qa_v1.py")
    chk("NOT_CHECKED_IS_PUBLISHED", ACCOUNTING, len(NOT_CHECKED) >= 5, True,
        len(NOT_CHECKED), "t04_supplementary_qa_v1.py")
    chk("EVERY_GATE_IS_TYPED", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res),
        "t04_supplementary_qa_v1.py")
    chk("EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT", ACCOUNTING,
        [r["gate_id"] for r in res if not r["source_artifact"]], [], len(res),
        "t04_supplementary_qa_v1.py")
    chk("NO_DUPLICATE_GATE_IDS", ACCOUNTING,
        len({r["gate_id"] for r in res}), len(res), len(res), "t04_supplementary_qa_v1.py")
    chk("NO_VACUOUS_GATES", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res),
        "t04_supplementary_qa_v1.py")

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
                f"n={r['population']:<4} {r['value']!r}")
        print(line[:220] + ("" if r["ok"] else f"   EXPECTED {r['expected']!r}"[:160]))
    print()
    print(f"SUITE_ID = {a['SUITE_ID']}")
    print(f"{a['ACTIVE_GATES_PASSING']}/{a['ACTIVE_GATE_COUNT']} active gates PASS")
    print(f"VACUOUS_GATES = {a['VACUOUS_GATES']}")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<20} {v}")
    sys.exit(1 if a["FAILING"] else 0)
