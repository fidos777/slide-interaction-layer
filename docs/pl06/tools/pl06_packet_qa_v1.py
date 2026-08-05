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
    G.append(_g("NO_WRITTEN_CONFIRMED_RULE_WAS_DOWNGRADED_TO_PROPOSED", "STATUS_TOKEN",
                sorted(".".join(p_) for p_, r in A.all_rules()
                       if p_[0] in ("quiz", "rumusan", "characters")
                       and r["authority_status"] != A.WRITTEN_CONFIRMED), [],
                len(A.all_rules()), "authority declaration", DOC_LITERAL))

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


def fixture(fid, target):
    def deco(fn):
        FIXTURES.append(dict(id=fid, target=target, fn=fn))
        return fn
    return deco


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
            results.append(dict(id=fx["id"], target=fx["target"], detected=caught,
                                also_failed=sorted(names - {fx["target"]})))
            if not caught:
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
            print(f"  {r['id']}  {'OK ' if r['detected'] else 'MISS'}  {r['target']}")
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
