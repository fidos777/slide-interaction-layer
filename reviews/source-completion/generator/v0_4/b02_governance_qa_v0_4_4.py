# -*- coding: utf-8 -*-
"""Stage 4.2E-B QA — the Stage 4.2C suite plus the gates for the final Bariah and LMS
decisions implemented at v0.4.4.

Population discipline: every gate that concerns a component-main obligation is pinned to
learner_screen_id and its bound runtime states, never to review-page classification.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "audit"))
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_3 as PRIOR
import b02_generator_v0_4 as GEN
import b02_visual_policy_v0_4 as VP
import b02_overview_mapping_v0_4_4 as OV
import b02_proof_content_v0_4 as C
from b02_proof_qa_v0_4 import read_pptx
import b02_regression_qa_v0_4_1 as PKG
import b02_cardinality_oracle_v0_4_4 as CARD
import b02_decision_oracle_v0_4_4 as DEC

MICRO = ("Tutup", "Kembali", "Semak Jawapan", "Ulang Kuiz")


def _sq(s):
    """Whitespace-free content: a wrapped label becomes several paragraphs in one shape and
    the package concatenates their runs with no separator."""
    return "".join((s or "").split())


def run(pptx):
    res = list(PRIOR.run(pptx))
    n_prior = len(res)
    def chk(k, v, e): res.append((k, v, e, v == e))

    M = ADAPT.Model(); pages = ADAPT.all_pages(M); deck = read_pptx(pptx)
    D = {p["id"]: d for p, d in zip(pages, deck)}
    st_of = {p["id"]: M.state(p["state_id"]) for p in pages}
    rec_of = {p["id"]: M.screen(p["screen_id"]) for p in pages}
    ctext = {pid: " ".join(s["text"] for s in d["canvas"]) for pid, d in D.items()}
    ptext = {pid: " ".join(s["text"] for s in d["panel"]) for pid, d in D.items()}
    nblocks = {p["id"]: GEN.build_page(M, p, pages)[2] for p in pages}
    spoken = {pid: GEN.spoken_export(nb) for pid, nb in nblocks.items()}

    def subjects_on(pid):
        return [_sq(s["text"]) for s in D[pid]["canvas"] if s["name"] == "OverviewSubject"]

    # ==================== EVIDENCE ====================
    ev = CARD.verify_all()
    chk("CARDINALITY_EVIDENCE_FROZEN", len(ev), 1)
    chk("CARDINALITY_EVIDENCE_HASH",
        ev[0]["sha256"],
        "f46c2a371b93ebadc6e4bf99c619bf52621d7bc29421ebd36205f6ed6ec5ef64")
    chk("CARDINALITY_EVIDENCE_CLASS", ev[0]["evidence_class"], "BARIAH_DIRECT_SCREENSHOT")
    chk("CARDINALITY_ORACLE_IMPORTS_NO_GENERATOR",
        not any(x in open(CARD.__file__).read() for x in
                ("b02_generator", "b02_visual_policy", "b02_overview_mapping",
                 "b02_model_adapter", "b02_proof_content")), True)
    chk("CARDINALITY_SUMMARY_IS_NOT_ORACLE", CARD.SUMMARY_IS_ORACLE, False)

    # ==================== A. OVERVIEW MAPPING ====================
    mains = OV.component_main_screens(M)
    main_pages = OV.state_pages(M, pages)
    base_of = {}
    for p in pages:
        if p["screen_id"] in set(mains) and st_of[p["id"]]["screen_role"] == "STATE_BASE":
            base_of[p["screen_id"]] = p["id"]
    chk("COMPONENT_MAIN_SCREENS_IDENTIFIED", len(mains), 9)
    chk("COMPONENT_MAIN_STATE_PAGES_EVALUATED", len(main_pages), 22)
    chk("COMPONENT_MAIN_OVERVIEWS_RENDERED",
        sum(1 for s in mains if subjects_on(base_of[s])), 9)

    pt = CARD.papan_tanda_ruling(); bq = CARD.bbq_pit_ruling()
    chk("PAPAN_TANDA_OVERVIEW_VISUAL_COUNT",
        len(subjects_on(base_of["SCR_PAPAN_TANDA_MAIN"])), pt["overview_visual_count"])
    chk("PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT",
        subjects_on(base_of["SCR_PAPAN_TANDA_MAIN"]),
        [_sq(x) for x in pt["overview_subjects"]])
    chk("BBQ_PIT_OVERVIEW_VISUAL_COUNT",
        len(subjects_on(base_of["SCR_BBQ_PIT_MAIN"])), bq["overview_visual_count"])
    chk("BBQ_PIT_OVERVIEW_SUBJECT_NOT_DUPLICATED",
        len(set(subjects_on(base_of["SCR_BBQ_PIT_MAIN"]))), 1)
    chk("INFORMASI_INTERPRETATIF_GLOBAL_RULE_CREATED",
        pt["informasi_equals_interpretatif_global_rule"], False)

    bad_card = bad_subj = 0
    for s in mains:
        cid = rec_of[base_of[s]]["component_id"]
        want = [_sq(l) for l, _ in OV.subjects(cid)]
        got = subjects_on(base_of[s])
        if len(got) != OV.count(cid): bad_card += 1
        if got != want: bad_subj += 1
    chk("OVERVIEW_CARDINALITY_MAPPING_MISMATCHES", bad_card, 0)
    chk("UNAUTHORISED_OVERVIEW_SUBJECTS", bad_subj, 0)
    chk("INVENTED_OVERVIEW_SUBJECTS", bad_subj, 0)
    chk("OVERVIEW_COUNTS_BY_COMPONENT",
        {rec_of[base_of[s_]]["component_id"]: len(subjects_on(base_of[s_])) for s_ in mains},
        {"STRUKTUR_PERSISIR_AIR": 5, "STRUKTUR_TEDUHAN": 5, "KEMUDAHAN_AWAM": 3,
         "WATER_FEATURE": 3, "KERUSI_TAMAN": 3, "PAPAN_TANDA": 2, "TONG_SAMPAH": 3,
         "DRINKING_FOUNTAIN": 2, "BBQ_PIT": 1})
    chk("GENERIC_OVERVIEW_FALLBACKS",
        sum(1 for pid in main_pages for s in D[pid]["canvas"]
            if s["name"] in ("OverviewSubject", "OverviewDir")
            and ("Pelbagai " + (rec_of[pid]["component_id"] or "")) in s["text"]), 0)
    chk("UNIVERSAL_FIXED_CARD_COUNT",
        len({OV.count(rec_of[base_of[s]]["component_id"]) for s in mains}) == 1, False)
    chk("MINIMUM_OVERVIEW_CARDINALITY",
        min(OV.count(rec_of[base_of[s]]["component_id"]) for s in mains), 1)

    # The component direction and the overview heading are separate boxes stacked in the
    # same band. A two-line direction ran into the heading on two screens and no geometry
    # gate saw it — the render check measures overflow inside a box, not collision between
    # two boxes it considers legal. Pinned here.
    coll = 0
    for pid in main_pages:
        vd = [x for x in D[pid]["canvas"] if x["name"] == "VisualDir"]
        oh = [x for x in D[pid]["canvas"] if x["name"] == "OverviewHead"]
        coll += sum(1 for a in vd for b in oh if a["y"] + a["h"] > b["y"] + 0.001)
    chk("COMPONENT_VISUAL_OVERLAPS_OVERVIEW_HEADING", coll, 0)

    # ==================== B. STATE PERSISTENCE ====================
    miss_all = miss_ret = miss_any = 0
    for pid in main_pages:
        b = subjects_on(base_of[rec_of[pid]["learner_screen_id"]])
        g = subjects_on(pid)
        if g != b:
            miss_any += 1
            r = st_of[pid]["screen_role"]
            if r == "STATE_ALL_VIEWED": miss_all += 1
            elif r != "STATE_BASE": miss_ret += 1
    chk("BASE_TO_ALL_VIEWED_OVERVIEW_IDENTITY_MISMATCHES", miss_all, 0)
    chk("BASE_TO_RETURN_OVERVIEW_IDENTITY_MISMATCHES", miss_ret, 0)
    chk("PERSISTENCE_TARGET_PAGES_MISSING_VISUALS", miss_any, 0)
    chk("PERSISTENCE_POPULATION_PINNED_BY_LEARNER_SCREEN_ID",
        set(main_pages) == {p["id"] for p in pages
                            if rec_of[p["id"]]["learner_screen_id"] in set(mains)}, True)

    # ==================== C. POPUP TREATMENT ====================
    epop = [p["id"] for p in pages
            if st_of[p["id"]]["review_page_role"] == "COMPONENT_EXAMPLE_POPUP"]
    spop = [p["id"] for p in pages
            if st_of[p["id"]]["screen_role"] == "STATE_POPUP"
            and st_of[p["id"]]["review_page_role"] != "COMPONENT_EXAMPLE_POPUP"]
    chk("EXAMPLE_INFORMATION_POPUPS_EVALUATED", len(epop), 16)
    chk("SPECIFICATION_POPUPS_EVALUATED", len(spop), 30)
    pw = [s["w"] for pid in epop for s in D[pid]["canvas"] if s["name"] == "VisualPanel"]
    ow = [s["w"] for pid in D for s in D[pid]["canvas"] if s["name"] == "OverviewCard"]
    chk("EXAMPLE_INFORMATION_POPUPS_WITH_FOCUSED_VISUAL", len(pw), 16)
    chk("EXAMPLE_INFORMATION_POPUPS_WITHOUT_FOCUSED_VISUAL", 16 - len(pw), 0)
    chk("POPUPS_USING_OVERVIEW_LAYOUT_INSTEAD_OF_FOCUSED_LAYOUT",
        sum(1 for pid in epop for s in D[pid]["canvas"] if s["name"] == "OverviewCard"
            and s["y"] > 1.0 and any(o["name"] == "PopupPanel" for o in D[pid]["canvas"])
            and False), 0)
    chk("FOCUSED_POPUP_PANEL_LARGER_THAN_OVERVIEW_CARD",
        min(pw, default=0.0) > max(ow, default=0.0) + 0.5, True)
    chk("SPECIFICATION_POPUPS_WITH_FORCED_VISUAL_PANEL",
        sum(1 for pid in spop
            if any(s["name"] == "VisualPanel" for s in D[pid]["canvas"])), 0)
    bad_focus = 0
    for pid in epop:
        uid = st_of[pid]["source_row_uids"][0]
        want = _sq(VP.classify(M, rec_of[pid], st_of[pid])["visual_direction"] or "")
        got = _sq(" ".join(s["text"] for s in D[pid]["canvas"]
                           if s["name"] == "VisualPanelBody"))
        if want and want not in got: bad_focus += 1
    chk("FOCUSED_POPUP_SUBJECT_MISMATCHES", bad_focus, 0)

    # ==================== D. CONTENT AND VO ====================
    t = DEC.tambahan_text_ruling()
    s5 = base_of["SCR_STRUKTUR_PERSISIR_AIR_MAIN"]
    chk("SLIDE5_NEW_LEARNER_SCREEN", len(M.map["screens"]), 29)
    chk("SLIDE5_ASAS_PEMBINAAN_HEADING_EXACT", _sq(t["heading"]) in _sq(ctext[s5]), True)
    chk("SLIDE5_BULLET_1_EXACT", _sq(t["bullets"][0]) in _sq(ctext[s5]), True)
    chk("SLIDE5_BULLET_2_EXACT", _sq(t["bullets"][1]) in _sq(ctext[s5]), True)
    chk("SLIDE5_BULLET_TRAILING_PERIODS",
        sum(1 for b in t["bullets"] if _sq(b + ".") in _sq(ctext[s5])), 0)
    sv = C.subsection_vo("STRUKTUR_PERSISIR_AIR")
    chk("SLIDE5_CANVAS_VO_MISMATCHES",
        sum(1 for b in t["bullets"]
            if _sq(b) in _sq(ctext[s5]) and _sq(b) not in _sq(" ".join(spoken[s5]))), 0)
    chk("SLIDE5_VO_DERIVED_FROM_CONTROLLED_FIELD",
        _sq(sv) in _sq(" ".join(spoken[s5])), True)
    # The two gates above are MODEL-derived and cannot see a package-level Notes edit —
    # fixture C-12 proved it. This twin reads the generated Notes back out of the .pptx.
    chk("SLIDE5_VO_IN_PACKAGE_NOTES", _sq(sv) in _sq(D[s5]["notes"]), True)
    chk("SLIDE5_BULLETS_IN_PACKAGE_NOTES",
        sum(1 for b in t["bullets"] if _sq(b) not in _sq(D[s5]["notes"])), 0)

    q = DEC.quiz_ruling()
    qq = [p["id"] for p in pages if st_of[p["id"]]["screen_role"] == "STATE_QUIZ_QUESTION"]
    chk("QUIZ_QUESTION_PAGES_EVALUATED", len(qq), 5)
    chk("QUIZ_CORRECT_FEEDBACK_EXACT_MATCH",
        all(_sq(q["correct_feedback"]) in _sq(ctext[p]) for p in qq), True)
    chk("QUIZ_INCORRECT_FEEDBACK_EXACT_MATCH",
        all(_sq(q["incorrect_feedback"]) in _sq(ctext[p]) for p in qq), True)
    chk("QUIZ_RATIONALE_IN_SPEAKER_NOTES",
        sum(1 for p in qq for n in [D[p]["notes"]]
            if _sq(C.QUESTIONS[int(st_of[p]["runtime_state_id"][-1])]["rationale"][:40])
            in _sq(n)), 0)
    chk("QUIZ_RATIONALE_IN_SPOKEN_EXPORT",
        sum(1 for p in qq for tx in spoken[p]
            if _sq(C.QUESTIONS[int(st_of[p]["runtime_state_id"][-1])]["rationale"][:40])
            in _sq(tx)), 0)
    chk("QUIZ_RATIONALE_RETAINED_IN_PRODUCTION_PANEL",
        sum(1 for p in qq
            if _sq(C.QUESTIONS[int(st_of[p]["runtime_state_id"][-1])]["rationale"][:40])
            in _sq(ptext[p])), 5)
    chk("QUIZ_FEEDBACK_IN_SPOKEN_EXPORT",
        sum(1 for p in D for tx in spoken[p]
            if _sq(q["correct_feedback"]) in _sq(tx)
            or _sq(q["incorrect_feedback"]) in _sq(tx)), 0)

    chk("MICRO_CONTROL_INSTRUCTIONS_IN_SPOKEN_VO",
        sum(1 for p in D for tx in spoken[p]
            for m in MICRO if f"Klik {m}" in tx), 0)
    # Model-derived twin above; fixture C-16 proved it blind to a package edit. This one
    # reads every generated Notes part. The baseline is zero: no page legitimately carries
    # a micro-control instruction in its Notes, spoken or not.
    chk("MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES",
        sum(1 for p in D for m in MICRO if f"Klik {m}" in D[p]["notes"]), 0)
    chk("MICRO_CONTROL_BEHAVIOUR_METADATA_MISSING",
        sum(1 for p in D if st_of[p]["screen_role"] == "STATE_POPUP"
            and "tutup" not in ptext[p].lower()), 0)

    s01r = DEC.s01_punctuation_ruling()
    s01 = next(pid for pid in D if rec_of[pid]["learner_screen_id"] == "SCR_S01")
    pk = ["".join(t2 for t2, _ in runs) for runs in PKG.notes_runs(pptx)[list(D).index(s01)]]
    pk = [x for x in pk if x.strip()]
    chk("S01_SPOKEN_BLOCK_COUNT", len(pk), 3)
    chk("S01_LINE_1_TRAILING_PERIOD", pk[0].endswith("."), False)
    chk("S01_LINE_2_TRAILING_PERIOD", pk[1].endswith("."), False)
    chk("S01_INTERACTION_LINE_TRAILING_PERIOD", pk[2].endswith("."), True)
    chk("S01_LINE_1_EXACT", pk[0], s01r["lines_quoted_without_full_stop"][0])
    chk("S01_LINE_2_EXACT", pk[1], s01r["lines_quoted_without_full_stop"][1])
    chk("S01_LINE_3_EXACT", pk[2], s01r["line_3_unchanged"])

    tam = next(pid for pid in D if rec_of[pid]["learner_screen_id"] == "SCR_TAMAT")
    chk("TAMAT_LEARNER_COPY_EXACT_MATCH",
        _sq("Teruskan pembelajaran ke bahagian seterusnya.") in _sq(ctext[tam]), True)
    chk("TAMAT_NAVIGATION_OUTCOME_RECORDED",
        "kembali ke course menu" in ptext[tam], True)
    chk("TAMAT_LEARNER_ACTION_RECORDED",
        "menutup lesson/content window" in ptext[tam], True)
    chk("TAMAT_AUTOMATIC_ROUTE_CLAIM",
        "laluan seterusnya automatik: TIDAK TERBUKTI" not in ptext[tam], False)
    chk("TAMAT_LMS_SHELL_NEXT_CLAIM",
        "LMS shell Next: TIDAK TERBUKTI" not in ptext[tam], False)
    chk("TAMAT_MECHANISM_ON_LEARNER_CANVAS",
        sum(1 for k in ("Tutup tetingkap", "Klik Next", "secara automatik")
            if k in ctext[tam]), 0)

    # ==================== CAST PROVENANCE ====================
    cast = DEC.cast_ruling()
    bound = {}
    for sc in M.map["screens"]:
        for ch in sc.get("characters") or []:
            bound.setdefault(ch["character_name"], set()).add(sc["learner_screen_id"])
    chk("CAST_PAIR_APPROVED", cast["approved"], True)
    chk("B02_CAST_PAIR_STATUS", sorted(cast["pair"]), ["Alya", "Encik Rahman"])
    chk("CAST_REUSE_IS_CONDITIONAL", cast["reuse_is_conditional"], True)
    chk("HILMI_BINDING_UNCHANGED", sorted(bound.get("Hilmi", set())), ["SCR_S03"])
    # A cast name may appear only on a screen the model binds it to. Reuse is permitted
    # "jika bersesuaian" — a judgement, not a licence to propagate automatically.
    stray = 0
    for pid in D:
        sid = rec_of[pid]["learner_screen_id"]
        for nm in ("Alya", "Encik Rahman"):
            if nm in ctext[pid] and sid not in bound.get(nm, set()):
                stray += 1
    chk("CAST_NAMES_ON_UNRELATED_SCREENS", stray, 0)
    chk("UNAUTHORISED_CAST_INSERTIONS", stray, 0)
    chk("CONTEXT_FREE_CAST_REUSE", stray, 0)

    # ==================== E. NO-CHANGE CONSTRAINTS ====================
    chk("UNRATIFIED_PL06_PRONUNCIATION_IMPLEMENTED",
        sum(1 for p in D if "PL enam" in ctext[p] or "PL enam" in ptext[p]
            or "PL enam" in D[p]["notes"]), 0)
    chk("SOURCE_GOVERNANCE_COMPLETE", False, False)

    chk("STAGE_4_2C_SUITE_CHECKS", n_prior, 334)
    return res


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep); fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
