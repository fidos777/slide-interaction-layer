# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.9.1 — filtered-population predicate audit over the B0.9 suite.

THE DEFECT CLASS
----------------
Fixture `C-05` got past Stage 4.2F-B0.9's suite. It relabelled the delegated Q3 decision as
`ACCEPTED_AS_PROPOSED`. The gate meant to protect that claim was:

    unsettled = [d for d in REG if not d["settled"]]
    assert {d["decision_class"] for d in unsettled} == {"DELEGATED_..."}

Relabelling the record made it settled, so it LEFT the population — and a gate that filters by
property P and then checks P cannot see a record leave the filter. The population shrank from
two to one, every remaining member still had the right class, and the gate passed while the
very claim it existed to protect had been reversed.

THE RULE
--------
Wherever a gate's population is selected by a mutable property, three assertions are needed,
not one:

    FILTERED PROPERTY GATE     — what is in the population is correct
  + NAMED MEMBERSHIP ASSERTION — these specific IDs are in it
  + POPULATION DELTA ASSERTION — the count has not moved

This module audits every B0.9 gate against that rule, reports the selector, the expected and
observed named members, additions, removals and counts, and documents every deliberate
exclusion.

WHAT IS DELIBERATELY EXCLUDED
-----------------------------
Naming members is only meaningful for a CLOSED population — one whose membership is itself a
governed fact. For genuinely open-ended populations (every string in a record set, every file
in a directory, every gate in this suite) a named-member list would be noise that has to be
edited on every unrelated change, and would train the reader to ignore it. Those are excluded
by name below, each with a reason.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import t04_authority_data_v1 as D    # noqa: E402
import t04_authority_qa_v1 as QA     # noqa: E402

STAGE = "4.2F-B0.9.1"

# ==========================================================================================
# CLOSED POPULATIONS — membership is a governed fact and is asserted by name.
# ==========================================================================================
# (population_id, selector, live member function, expected named members)
CLOSED_POPULATIONS = [
    dict(population_id="POP-01",
         selector='decision_class == "DELEGATED_PENDING_AUTHORITY_CONFIRMATION"',
         mutable_property="decision_class",
         members=lambda: sorted(d["decision_id"] for d in D._decision_register()
                                if d["decision_class"]
                                == "DELEGATED_PENDING_AUTHORITY_CONFIRMATION"),
         expected=["T04-DEC-X01", "T04-DEC-X02"],
         guarded_by=["THE_Q3_DELEGATION_KEEPS_ITS_DELEGATED_CLASS",
                     "UNSETTLED_DECISIONS_ARE_ONLY_THE_DELEGATED_CLASS"],
         origin_fixture="C-05"),
    dict(population_id="POP-02",
         selector="settled is False",
         mutable_property="settled",
         members=lambda: sorted(d["decision_id"] for d in D._decision_register()
                                if not d["settled"]),
         expected=["T04-DEC-X01", "T04-DEC-X02"],
         guarded_by=["THE_TWO_NAMED_DELEGATIONS_REMAIN_UNSETTLED"],
         origin_fixture="C-05"),
    dict(population_id="POP-03",
         selector='scope == "ALL_PLS_IN_KURSUS"',
         mutable_property="scope",
         members=lambda: sorted(D.course_wide_decisions()),
         expected=["T04-DEC-E06", "T04-DEC-E07"],
         guarded_by=["ONLY_TWO_DECISIONS_ARE_COURSE_WIDE",
                     "NO_RUMUSAN_DECISION_IS_COURSE_WIDE",
                     "NO_DIALOGUE_DECISION_IS_COURSE_WIDE"],
         origin_fixture="G-03 / G-04"),
    dict(population_id="POP-04",
         selector='change_type contains "TREATMENT_CHANGED"',
         mutable_property="change_type",
         members=lambda: sorted(s["screen_id"] for s in D._final_sequence()
                                if "TREATMENT_CHANGED" in s["change_type"]),
         expected=["T04-S12", "T04-S13", "T04-S16", "T04-S17"],
         guarded_by=["FOUR_TREATMENTS_CHANGED",
                     "EVERY_TREATMENT_CHANGE_ACTUALLY_CHANGES_THE_TREATMENT"],
         origin_fixture="D-08"),
    dict(population_id="POP-05",
         selector='change_type == "INSERTED"',
         mutable_property="change_type",
         members=lambda: sorted(D.inserted_screens()),
         expected=["T04-S14"],
         guarded_by=["EXACTLY_ONE_SCREEN_INSERTED", "INSERTED_SCREEN_IS_SOURCE_BOUND"],
         origin_fixture="D-01"),
    dict(population_id="POP-06",
         selector='change_type == "RENUMBERED"',
         mutable_property="change_type",
         members=lambda: sorted(s["screen_id"] for s in D._final_sequence()
                                if s["change_type"] == "RENUMBERED"),
         expected=["T04-S15", "T04-S19"],
         guarded_by=["RENUMBER_ONLY_SCREENS_KEEP_THEIR_TREATMENT", "EIGHT_SCREENS_RENUMBERED"],
         origin_fixture="D-09"),
    dict(population_id="POP-07",
         selector='question_type == "MULTIPLE_RESPONSE"',
         mutable_property="question_type",
         members=lambda: sorted(q["question_id"] for q in D.quiz_items()
                                if q["question_type"] == "MULTIPLE_RESPONSE"),
         expected=["T04-QZ-Q5"],
         guarded_by=["MULTIPLE_RESPONSE_OPTIONS_USE_CHECKBOXES",
                     "MULTIPLE_RESPONSE_OPTIONS_CARRY_NO_LETTER",
                     "MULTIPLE_RESPONSE_HAS_MORE_THAN_ONE_KEY", "Q5_HAS_SIX_OPTIONS"],
         origin_fixture="F-03"),
    dict(population_id="POP-08",
         selector='question_type == "MCQ"',
         mutable_property="question_type",
         members=lambda: sorted(q["question_id"] for q in D.quiz_items()
                                if q["question_type"] == "MCQ"),
         expected=["T04-QZ-Q1", "T04-QZ-Q2", "T04-QZ-Q3", "T04-QZ-Q4"],
         guarded_by=["MCQ_OPTIONS_KEEP_THEIR_LETTERS", "MCQ_ITEMS_HAVE_EXACTLY_ONE_KEY"],
         origin_fixture="F-03"),
    dict(population_id="POP-09",
         selector='treatment == "CONTENT_STATIC"',
         mutable_property="treatment",
         members=lambda: sorted(s["screen_id"] for s in D._final_sequence()
                                if s["treatment"] == "CONTENT_STATIC"),
         expected=["T04-S04", "T04-S05", "T04-S08", "T04-S11", "T04-S12", "T04-S13",
                   "T04-S15", "T04-S17", "T04-S18"],
         guarded_by=["STATIC_SCREENS_HAVE_NO_REVEAL_STATES"],
         origin_fixture="D-10"),
    dict(population_id="POP-10",
         selector="named_reveal_items is non-empty",
         mutable_property="named_reveal_items",
         members=lambda: sorted(s["screen_id"] for s in D._final_sequence()
                                if s["named_reveal_items"]),
         expected=["T04-S14", "T04-S16"],
         guarded_by=["NAMED_REVEAL_ITEMS_PRESENT_ON_BOTH_SCREENS",
                     "REVEAL_SCREENS_HAVE_A_STATE_PER_NAMED_ITEM",
                     "PPE_LENGKAP_IS_A_NAMED_REVEAL_ON_S16"],
         origin_fixture="D-07"),
    dict(population_id="POP-11",
         selector="named_aspect_list is non-empty",
         mutable_property="named_aspect_list",
         members=lambda: sorted(k for k, v in D.NAMED_ASPECT_LISTS.items() if v),
         expected=["T04-S05", "T04-S08", "T04-S11"],
         guarded_by=["ASPECT_LISTS_ON_THE_THREE_MAIN_EXPLANATION_SCREENS"],
         origin_fixture="D-15"),
    dict(population_id="POP-12",
         selector='decision_class == "AMENDED_WITH_AUTHORITY_INSTRUCTION_EXECUTED_BY_CAIR"',
         mutable_property="decision_class",
         members=lambda: sorted(
             d["decision_id"] for d in D._decision_register()
             if d["decision_class"]
             == "AMENDED_WITH_AUTHORITY_INSTRUCTION_EXECUTED_BY_CAIR"),
         expected=["T04-DEC-A12", "T04-DEC-A13", "T04-DEC-A16", "T04-DEC-A17",
                   "T04-DEC-A18", "T04-DEC-A22", "T04-DEC-B06", "T04-DEC-C03",
                   "T04-DEC-E08"],
         guarded_by=["CAIR_EXECUTED_DECISIONS_ARE_NOT_AUTHORITY_AUTHORED"],
         origin_fixture="C-02"),
    dict(population_id="POP-13",
         selector='decision_class == "AMENDED_WITH_AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"',
         mutable_property="decision_class",
         members=lambda: sorted(
             d["decision_id"] for d in D._decision_register()
             if d["decision_class"]
             == "AMENDED_WITH_AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"),
         expected=["T04-DEC-C01", "T04-DEC-D01", "T04-DEC-E01", "T04-DEC-E02",
                   "T04-DEC-E03", "T04-DEC-E04", "T04-DEC-E05"],
         guarded_by=["AUTHORITY_SUPPLIED_TEXT_IS_MARKED_AUTHORITY_AUTHORED"],
         origin_fixture="C-01"),
    dict(population_id="POP-14",
         selector='source_artifact == "AUTH-EV-02"  (the WhatsApp evidence)',
         mutable_property="source_artifact",
         members=lambda: sorted(d["decision_id"] for d in D._decision_register()
                                if d["source_artifact"] == "AUTH-EV-02"),
         # T04-DEC-E09 joined this population when the E-07 selection was ingested. The
         # audit caught the change, which is what it is for.
         expected=["T04-DEC-E09", "T04-DEC-X01"],
         guarded_by=["WHATSAPP_RECORDS_ARE_GRADED_BY_HOW_THEY_WERE_READ"],
         origin_fixture="C-04"),
    dict(population_id="POP-15",
         selector="settled is False, among the ten final states",
         mutable_property="settled",
         members=lambda: sorted(s["state_id"] for s in D.final_states() if not s["settled"]),
         # FS-07 left this population when Bariah selected Set B. Only the answer key is
         # still unsettled.
         expected=["FS-08"],
         guarded_by=["ONE_CLASS_IS_FROZEN_BUT_NOT_SETTLED",
                     "Q5_OPTIONS_STATE_IS_SELECTED_BY_THE_AUTHORITY",
                     "ANSWER_KEY_STATE_IS_PROPOSED_NOT_FINAL"],
         origin_fixture="K-01 / K-02"),
    dict(population_id="POP-16",
         selector="supplied_in_this_run is False, among the evidence records",
         mutable_property="supplied_in_this_run",
         members=lambda: sorted(r["evidence_id"] for r in D.EVIDENCE
                                if not r["supplied_in_this_run"]),
         expected=["AUTH-EV-02"],
         guarded_by=["SUPPLEMENTARY_EVIDENCE_MARKED_NOT_SUPPLIED",
                     "NO_FABRICATED_HASH_FOR_UNSUPPLIED_EVIDENCE"],
         origin_fixture="A-02"),
    dict(population_id="POP-17",
         selector='restriction == "REUSE_NOT_ALLOWED"',
         mutable_property="restriction",
         members=lambda: sorted(x["obligation_id"] for x in D._do_not_reuse_items()
                                if x["restriction"] == "REUSE_NOT_ALLOWED"),
         # Corrected in Stage 4.2F-B1: the HSE item is T04-VO-040, not T04-VO-039. See
         # T04-COR-05. The audit flagged the membership change, which is its job.
         expected=["T04-VO-025", "T04-VO-026", "T04-VO-040"],
         guarded_by=["THREE_DO_NOT_REUSE_ITEMS", "ALL_THREE_BASES_ARE_BOTH_LENSES",
                     "RESTRICTIONS_ARE_ITEM_LEVEL_NOT_GROUP_LEVEL",
                     "DO_NOT_REUSE_IDS_AGREE_WITH_THE_CLOSURE"],
         origin_fixture="H-03 / H-05"),
    dict(population_id="POP-18",
         selector="open items carried past this stage",
         mutable_property="membership of OPEN_AFTER_THIS_STAGE",
         members=lambda: sorted(o["open_id"] for o in D.OPEN_AFTER_THIS_STAGE),
         # E-01, E-03 and E-07 closed in the Stage 4.2F-B0.9.1 re-run, each naming what
         # closed it. E-02 and E-04 are still open and are still asserted open.
         expected=["E-02", "E-04", "E-05", "E-06"],
         guarded_by=["E02_AND_E04_ARE_NOT_CLOSED", "FOUR_ITEMS_STAY_OPEN_AFTER_THIS_STAGE",
                     "EVERY_CLOSURE_NAMES_WHAT_CLOSED_IT"],
         origin_fixture="K-04"),
]

# ==========================================================================================
# DOCUMENTED EXCLUSIONS — open-ended populations where naming members would be noise.
# ==========================================================================================
EXCLUDED_POPULATIONS = [
    dict(exclusion_id="EXC-01",
         selector="every substantive string in the record set",
         used_by=["FORBIDDEN_LABELS_ABSENT_FROM_EVERY_RECORD",
                  "CAIR_NOT_NAMED_INSTRUCTIONAL_DESIGNER",
                  "FINAL_CONTENT_IS_NOT_MARKED_SOURCE_UNSUPPORTED"],
         why=("Population size is in the thousands and changes with any prose edit. The gate "
              "asserts an empty result over everything, which is the strongest form already "
              "— nothing can leave the population without leaving the model entirely."),
         delta_guard="the gate fails if the population reaches zero (NO_VACUOUS_GATES)"),
    dict(exclusion_id="EXC-02",
         selector="every file in docs/pl06/t04/",
         used_by=["NO_T04_PPTX_ON_DISK"],
         why=("Directory contents legitimately grow every stage. Naming the members would "
              "require editing this list on every unrelated artifact addition, which trains "
              "the reader to ignore it."),
         delta_guard="the assertion is an empty result over all files, not over a subset"),
    dict(exclusion_id="EXC-03",
         selector="every gate record emitted by this suite",
         used_by=["EVERY_GATE_IS_TYPED", "NO_DUPLICATE_GATE_IDS", "NO_VACUOUS_GATES",
                  "EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT",
                  "EVERY_GATE_DECLARES_A_POPULATION"],
         why="Self-referential and open by design — the suite grows. Membership is the whole "
             "suite, so nothing can leave it without being deleted, which the count catches.",
         delta_guard="ACTIVE_GATE_COUNT is reported and compared stage to stage"),
    dict(exclusion_id="EXC-04",
         selector="every controlled source row referenced by the sequence or the quiz",
         used_by=["EVERY_SOURCE_ROW_RESOLVES", "EVERY_QUIZ_SOURCE_ROW_RESOLVES"],
         why=("The row set is large and is governed by the extraction stage's own suite, not "
              "this one. Duplicating 100 row IDs here would create a second source of truth."),
         delta_guard="SOURCE_BINDINGS_NOT_REMOVED_FROM_THE_MODEL asserts the prior row set "
                     "is still fully covered — a genuine delta assertion"),
    dict(exclusion_id="EXC-05",
         selector="every emitted artifact scanned for stale facts",
         used_by=["NO_EMITTED_ARTIFACT_ASSERTS_A_STALE_FACT_AS_CURRENT"],
         why="Artifact list grows per stage; membership is asserted separately by "
             "EVERY_DECLARED_ARTIFACT_WAS_EMITTED and TWENTY_FOUR_ARTIFACTS_DECLARED.",
         delta_guard="STALE_FACT_SCAN_ACTUALLY_MATCHED_SOMETHING prevents the scan going "
                     "vacuously green"),
]


def audit():
    rows = []
    for p in CLOSED_POPULATIONS:
        observed = p["members"]()
        expected = list(p["expected"])
        rows.append(dict(
            population_id=p["population_id"],
            selector=p["selector"],
            mutable_property=p["mutable_property"],
            expected_members=expected,
            observed_members=observed,
            unexpected_additions=sorted(set(observed) - set(expected)),
            unexpected_removals=sorted(set(expected) - set(observed)),
            expected_count=len(expected),
            observed_count=len(observed),
            count_delta=len(observed) - len(expected),
            guarded_by=list(p["guarded_by"]),
            origin_fixture=p["origin_fixture"],
            ok=(observed == expected)))
    return rows


def summary():
    rows = audit()
    return dict(
        stage=STAGE,
        closed_populations=len(rows),
        excluded_populations=len(EXCLUDED_POPULATIONS),
        failing=[r["population_id"] for r in rows if not r["ok"]],
        total_unexpected_additions=sum(len(r["unexpected_additions"]) for r in rows),
        total_unexpected_removals=sum(len(r["unexpected_removals"]) for r in rows),
        rows=rows,
        exclusions=EXCLUDED_POPULATIONS)


if __name__ == "__main__":
    import json
    s = summary()
    w = max(len(r["selector"]) for r in s["rows"])
    for r in s["rows"]:
        flag = "OK  " if r["ok"] else "FAIL"
        print(f"{flag}  {r['population_id']}  {r['selector']:<{w}}  "
              f"n={r['observed_count']}/{r['expected_count']}  "
              f"+{len(r['unexpected_additions'])} -{len(r['unexpected_removals'])}")
    print()
    print(f"closed populations   = {s['closed_populations']}")
    print(f"excluded populations = {s['excluded_populations']} (documented)")
    print(f"failing              = {s['failing']}")
    sys.exit(1 if s["failing"] else 0)
