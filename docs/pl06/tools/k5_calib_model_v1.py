# -*- coding: utf-8 -*-
"""Stage 4.2F-H — the K5 PL06 calibration model for ONE unit, derived from committed models.

WHAT THIS IS
------------
A provisional calibration model. It projects a single K5 PL06 unit into screens, content
blocks and runtime states so that a Storyboard PPTX and a Lampiran Keadaan PPTX can be
generated for Bariah to review. Nothing here is instructionally approved.

WHERE EVERY STRING COMES FROM
-----------------------------
Three committed sources, and no fourth:

  * `pl06_extract_v1`        — the controlled source rows (verbatim module text, row IDs)
  * `pl06_unit_model_v1`     — the unit's committed content analysis: mandatory propositions,
                               quiz items, Rumusan beats, visual subjects, grouping
  * `k5_pattern_policy_v1`   — Bariah's rulings A1-A7, B1-B4, C1-C2, D1-D4

No T04 content is imported. T04 supplies GEOMETRY and MECHANISM only, and that import lives
in the builder, not here.

PROVISIONAL, AND SAID SO
------------------------
Three things are provisional by construction and are labelled on the face of every artifact:

  * the scenario screen carries no proper names — D1 leaves the cast to per-unit review, so
    the screen uses the cast-free SITUASI frame with an explicit WATAK placeholder;
  * the Rumusan montage is a positional mapping of the unit's three committed beats onto
    A6's three labels — mechanical, not interpreted, and pending Bariah's unit review;
  * the on-screen condensed lines are first-sentence reductions of source rows. They add no
    claim. The full row text still appears on screen inside the reveal panel, which is what
    A1 requires.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pl06_extract_v1 as EX           # noqa: E402
import pl06_unit_model_v1 as U         # noqa: E402
import k5_pattern_policy_v1 as P       # noqa: E402
import k5_policy_apply_v1 as AP        # noqa: E402

STAGE = "4.2F-H"
SUITE_ID = "K5_CALIBRATION_PROOF_QA_v1"
GENERATED_BY = "docs/pl06/tools/k5_calib_build_v1.py"

# ------------------------------------------------------------------ the one authorised unit
UNIT_ID = "K5-PL06-T03-B03"
SHORT = "T03B03"
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PPTX_DIR = os.path.join(REPO, "reviews", "storyboard-bariah", "k5_calibration")

STORYBOARD_NAME = "K5PL06T03B03_STORYBOARD_KALIBRASI_DRAF_v0_1.pptx"
LAMPIRAN_NAME = "K5PL06T03B03_LAMPIRAN_KEADAAN_DRAF_v0_1_{n}panel.pptx"

# ------------------------------------------------------------------------------ status marks
STATUS_MARKS = ["DRAFT_FOR_BARIAH_REVIEW",
                "NOT_INSTRUCTIONALLY_APPROVED",
                "NOT_LEARNER_FACING_FINAL"]
FORBIDDEN_STATUS_CLAIMS = ["BARIAH_APPROVED", "INSTRUCTIONALLY_APPROVED",
                           "LEARNER_FACING_FINAL", "STORYBOARD_FROZEN",
                           "ANSWER_KEY_APPROVED", "CANONICAL_PRODUCTION_TEMPLATE"]

# Provenance vocabulary. Deliberately NOT T04's list: K5 adds a condensed class and a
# provisional class, and drops T04's AUTHORITY_SUPPLIED, because Bariah wrote no K5 screen
# text — she ruled on patterns.
PROVENANCE = ["SOURCE_CONTROLLED",          # verbatim controlled row text
              "SOURCE_CONDENSED",           # first sentence of a committed source-derived
                                            # proposition; adds no word
              "COURSE_RULE_APPROVED",       # a string Bariah's ruling itself fixes
              "CAIR_DRAFTED_ASSESSMENT",    # quiz stem or distractor, drafted, unapproved
              "CAIR_DRAFTED_RUMUSAN_BEAT",  # a committed unit-model beat, not a row
              "CAIR_STRUCTURAL",            # interface furniture
              "PROVISIONAL_PLACEHOLDER"]    # a named gap, never content
FORBIDDEN_PROVENANCE = "CAIR_INSTRUCTIONAL_CONTENT"
FORBIDDEN_PROVENANCE_REASON = (
    "No teaching claim may enter a K5 screen except from a controlled source row. A block "
    "with no row and no Bariah ruling behind it is a placeholder, not content.")

# ------------------------------------------------------------------- provisional placeholders
PLACEHOLDER_CAST = "WATAK: PENDING_UNIT_REVIEW — D1 menetapkan watak dipilih per unit"
PLACEHOLDER_CAST_A = "WATAK A — PENDING_UNIT_REVIEW"
PLACEHOLDER_CAST_B = "WATAK B — PENDING_UNIT_REVIEW"
PLACEHOLDER_VISUAL = "ASET VISUAL BELUM DIHASILKAN — NOT_MMD_ASSET"
PLACEHOLDER_SUBJECT = "SUBJEK VISUAL: PENDING_BARIAH_UNIT_REVIEW"
MONTAGE_MARKS = ["PROVISIONAL_VISUAL_DIRECTION", "PENDING_BARIAH_UNIT_REVIEW",
                 "NOT_MMD_ASSET"]

UI_MULA = "MULA"
UI_SETERUSNYA = "SETERUSNYA"
UI_REVEAL_HINT = "Klik setiap tajuk untuk memaparkan maklumat."

# ==========================================================================================
# CACHED INPUTS
# ==========================================================================================
_EX = None
_MODEL = None
_CACHE = {}


def _cached(key, fn):
    """Memoise a derivation. `reset()` clears it, which the mutation fixtures rely on."""
    if key not in _CACHE:
        _CACHE[key] = fn()
    return _CACHE[key]


def reset():
    """Drop every derived cache. Called by a mutation fixture after it edits an input."""
    _CACHE.clear()


def extract():
    global _EX
    if _EX is None:
        _EX = EX.extract_all()[UNIT_ID]
    return _EX


def unit_model():
    global _MODEL
    if _MODEL is None:
        _MODEL = U.model(UNIT_ID, extract())
    return _MODEL


def _rows_by_id_uncached():
    return {r["row_id"]: r for r in extract()["rows"]}


def _txt(row):
    return (row["controlled_display_text"] or "").strip()


def decision(did):
    return next(d for d in P.DECISIONS if d["id"] == did)


def _policy_unit():
    # `AP.calibration_units()` rebuilds all four unit records on every call (~1.4s). The
    # builder asks for this unit once per slide, which is where the storyboard's build time
    # was going.
    return _cached("policy_unit",
                   lambda: next(u for u in AP.calibration_units()["units"]
                                if u["unit_id"] == UNIT_ID))


# ==========================================================================================
# GROUP PARSING — mechanical, from the module's own repeated markers
# ==========================================================================================
_MARKERS = set(U.COMPONENT_MARKERS)


def _marker(row):
    return _txt(row).strip() in _MARKERS


def _groups_uncached():
    """One record per content group, with its Fungsi block and its reveal targets.

    The split is the module's own: a group heading, an optional intro paragraph, the module's
    `Fungsi` marker, then the module's `Fokus Utama Kontraktor` marker under which each
    structural sub-heading owns the non-structural rows that follow it. Nothing is declared
    by hand — a change in the source changes the groups.
    """
    ex = extract()
    rows = ex["rows"]
    idx = {r["row_id"]: i for i, r in enumerate(rows)}
    gdefs = unit_model()["grouping"]["groups"]
    out = []
    for gi, g in enumerate(gdefs):
        start = idx[g["row_id"]]
        end = idx[gdefs[gi + 1]["row_id"]] if gi + 1 < len(gdefs) else len(rows)
        span = rows[start:end]
        head, rest = span[0], span[1:]

        f_i = next((i for i, r in enumerate(rest)
                    if _marker(r) and _txt(r).rstrip(":") == "Fungsi"), None)
        k_i = next((i for i, r in enumerate(rest)
                    if _marker(r) and _txt(r).startswith("Fokus Utama")), None)
        intro = rest[:f_i] if f_i is not None else []
        fungsi = rest[f_i + 1:k_i] if (f_i is not None and k_i is not None) else []
        fokus = rest[k_i + 1:] if k_i is not None else []

        reveals, cur = [], None
        for r in fokus:
            if U.is_structural(r):
                cur = dict(trigger_row=r["row_id"], trigger_label=_txt(r), content_rows=[])
                reveals.append(cur)
            elif cur is not None:
                cur["content_rows"].append(r["row_id"])
        reveals = [rv for rv in reveals if rv["content_rows"]]

        out.append(dict(
            group_id=g["group_id"], covers=g["covers"], head_row=head["row_id"],
            module_page=head["module_page"],
            intro_rows=[r["row_id"] for r in intro],
            fungsi_marker_row=rest[f_i]["row_id"] if f_i is not None else None,
            fokus_marker_row=rest[k_i]["row_id"] if k_i is not None else None,
            fungsi_rows=[r["row_id"] for r in fungsi],
            reveals=reveals,
            marker_basis="MODULE_OWN_FUNGSI_AND_FOKUS_MARKERS"))
    return out


# ==========================================================================================
# CONDENSATION — mechanical reduction, never a new claim
# ==========================================================================================
CONDENSE_BASIS = "FIRST_SENTENCE_OF_THE_CONTROLLED_ROW_NO_WORDS_ADDED"


def condense(text):
    """First sentence of a controlled row. Adds nothing, reorders nothing."""
    t = " ".join(text.split())
    m = re.search(r"(?<=[.!?])\s", t)
    return (t[:m.start()] if m else t).strip()


def _prop_for_group(g):
    """The unit's own mandatory propositions whose rows fall inside this group."""
    owned = {g["head_row"], *g["intro_rows"], *g["fungsi_rows"]}
    for rv in g["reveals"]:
        owned.add(rv["trigger_row"])
        owned.update(rv["content_rows"])
    return [p for p in unit_model()["mandatory_propositions"]["propositions"]
            if any(r in owned for r in p["rows"])]


# ==========================================================================================
# SCENARIO — cast-free, source-bound, provisional
# ==========================================================================================
SCENARIO_FORMAT_BASIS = (
    "The committed unit model records dialogue verdict NOT_JUSTIFIED for this unit, so the "
    "cast-free SITUASI frame is used. D3 still makes the screen mandatory, and D1 leaves the "
    "cast to unit review, so a WATAK placeholder is carried instead of any proper name.")


def scenario():
    by = rows_by_id()
    um = unit_model()
    stmts = um["compliance_sensitive"]["statements"]
    items = []
    for s in stmts:
        for rid in s["rows"]:
            r = by.get(rid)
            if r and _txt(r):
                items.append(dict(row_id=rid, text=_txt(r), why=s["why"],
                                  module_page=r["module_page"]))
            break
    return dict(
        format="SITUASI_CAST_FREE",
        format_basis=SCENARIO_FORMAT_BASIS,
        dialogue_verdict=um["dialogue"]["verdict"],
        cast_placeholder=PLACEHOLDER_CAST,
        alternate_cast_placeholders=[PLACEHOLDER_CAST_A, PLACEHOLDER_CAST_B],
        items=items,
        source_row_ids=[i["row_id"] for i in items],
        marks=list(STATUS_MARKS),
        decision_ids=["D3", "A5", "D1"])


# ==========================================================================================
# RUMUSAN — A6's three labels, the unit's own three beats, mapped positionally
# ==========================================================================================
A6_LABELS = ["Kepentingan", "Skop dan Isi Utama", "Manfaat"]
MONTAGE_MAPPING_BASIS = "POSITIONAL_A6_LABEL_ORDER_TO_COMMITTED_UNIT_BEAT_ORDER"
RUMUSAN_SUPERSESSION = (
    "The committed unit model proposes RP-007 (contractor perspective, no Kepentingan / Isi "
    "Utama / Manfaat labels). A6 is Bariah's ruling and supersedes that CAIR proposal. The "
    "BEAT TEXT stays the unit's own; only the three labels come from A6.")


def rumusan():
    beats = unit_model()["rumusan"]["beats"]
    montage = [dict(component_id=f"MT-{i + 1:02d}", label=A6_LABELS[i], beat=b,
                    points_at_beat_index=i + 1, marks=list(MONTAGE_MARKS))
               for i, b in enumerate(beats[:len(A6_LABELS)])]
    return dict(labels=list(A6_LABELS), beats=list(beats),
                beat_count=len(beats),
                montage=montage,
                mapping_basis=MONTAGE_MAPPING_BASIS,
                supersedes=RUMUSAN_SUPERSESSION,
                decision_ids=["A6"])


# ==========================================================================================
# A4 — COMPARISON EVIDENCE
# ==========================================================================================
# The policy record names comparison as this unit's SECONDARY pattern and the committed unit
# model names it as a `secondary_candidate`. Both are candidacies. This builder applied
# neither: every content screen is click-to-reveal, and the word "comparison" appears nowhere
# in any generated file. The evidence below exists so the candidacy can be judged on the
# source rather than carried forward on a label.
A4_COMPARISON = dict(
    applied_in_this_deck=False,
    treatments_actually_used=["click-to-reveal", "static content",
                              "scenario/dialogue only where justified"],
    where_the_label_lives=["k5_policy_apply_v1 screen_pattern_plan.secondary",
                           "pl06_unit_model_v1 pattern_family.secondary_candidate"],
    objects_compared=["Swale / Natural Drain", "Parit konkrit (concrete drain)"],
    scope="ONE content group of six — G5 (Swale). No other group carries a comparison.",
    supporting_rows=["T03B03-ROW-056", "T03B03-ROW-061"],
    explicit_relationships=[
        dict(row="T03B03-ROW-056", relationship="ALTERNATIVE_TO",
             quoted="Ia merupakan alternatif mesra alam kepada parit konkrit.",
             axis="environmental character"),
        dict(row="T03B03-ROW-061", relationship="CONTRASTED_GEOMETRY",
             quoted="satu lekukan yang landai dan lebar, bukannya parit yang dalam dan curam.",
             axis="cross-sectional geometry")],
    source_states_an_explicit_comparison=True,
    asymmetry=("The swale side carries four to five source-backed attributes (ROW-056, "
               "ROW-058, ROW-063). The concrete-drain side carries two, and both exist only "
               "as negations inside the swale's own rows — 'deep and steep', and 'not the "
               "environmentally friendly option'. No row in this unit describes a concrete "
               "drain in its own right."),
    verdict=("A4 IS SUPPORTABLE BUT NOT APPLIED. The source does compare the two objects "
             "explicitly, so a comparison would not be invented. It would however be a "
             "one-group, two-axis comparison with one column built entirely from negations, "
             "which is why click-to-reveal was used instead. Promoting it is Bariah's call, "
             "not this builder's."))


# ==========================================================================================
# SCREENS
# ==========================================================================================
def _screens_uncached():
    by = rows_by_id()
    um = unit_model()
    pol = _policy_unit()
    gs = groups()
    out, pos = [], 0

    def add(**kw):
        nonlocal pos
        pos += 1
        kw["position"] = pos
        kw["screen_id"] = f"{SHORT}-S{pos:02d}"
        kw.setdefault("source_row_ids", [])
        kw.setdefault("reveals", [])
        kw.setdefault("vo", "")
        kw.setdefault("visual", None)
        out.append(kw)
        return kw

    # ---- S01 shell: entry ----------------------------------------------------------------
    add(kind="SHELL_ENTRY", treatment="static content",
        title_ms=extract()["lesson_title"],
        blocks=[dict(text=_txt(extract()["rows"][0]), provenance="SOURCE_CONTROLLED",
                     row_id=extract()["rows"][0]["row_id"]),
                dict(text=f"Narator: {pol['narrator']['name']}",
                     provenance="COURSE_RULE_APPROVED", decision="D2"),
                dict(text=UI_MULA, provenance="CAIR_STRUCTURAL")],
        source_row_ids=[extract()["rows"][0]["row_id"]],
        vo=f"Selamat datang. Saya {pol['narrator']['name']}.",
        decision_ids=["D2", "D4"])

    # ---- S02 shell: scenario (D3 mandatory) ----------------------------------------------
    sc = scenario()
    add(kind="SCENARIO", treatment="scenario/dialogue only where justified",
        title_ms="Situasi di tapak",
        blocks=([dict(text="SITUASI", provenance="CAIR_STRUCTURAL"),
                 dict(text=sc["cast_placeholder"], provenance="PROVISIONAL_PLACEHOLDER")]
                + [dict(text=i["text"], provenance="SOURCE_CONTROLLED", row_id=i["row_id"])
                   for i in sc["items"]]
                + [dict(text=" · ".join(STATUS_MARKS),
                        provenance="PROVISIONAL_PLACEHOLDER")]),
        source_row_ids=sc["source_row_ids"],
        vo=" ".join(i["text"] for i in sc["items"]),
        decision_ids=sc["decision_ids"], scenario=sc)

    # ---- S03 shell: orientation ----------------------------------------------------------
    by = rows_by_id()
    add(kind="SHELL_ORIENTATION", treatment="static content",
        title_ms="Apa yang anda akan pelajari",
        blocks=([dict(text=UI_REVEAL_HINT, provenance="CAIR_STRUCTURAL")]
                + [dict(text=_txt(by[g["head_row"]]), provenance="SOURCE_CONTROLLED",
                        row_id=g["head_row"]) for g in gs]),
        source_row_ids=[g["head_row"] for g in gs],
        vo="Bahagian ini merangkumi " + str(len(gs)) + " komponen.",
        decision_ids=["A1"])

    # ---- content screens, one per group --------------------------------------------------
    for g in gs:
        props = _prop_for_group(g)
        blocks = [dict(text=_txt(by[g["head_row"]]), provenance="SOURCE_CONTROLLED",
                       row_id=g["head_row"])]
        for rid in g["intro_rows"]:
            blocks.append(dict(text=_txt(by[rid]), provenance="SOURCE_CONTROLLED",
                               row_id=rid))
        if props:
            blocks.append(dict(text=condense(props[0]["proposition"]),
                               provenance="SOURCE_CONDENSED",
                               row_id=props[0]["rows"][0],
                               condensed_from=props[0]["proposition"]))
        blocks.append(dict(text=_txt(by[g["fungsi_marker_row"]]),
                           provenance="SOURCE_CONTROLLED", row_id=g["fungsi_marker_row"]))
        for rid in g["fungsi_rows"]:
            blocks.append(dict(text=_txt(by[rid]), provenance="SOURCE_CONTROLLED",
                               row_id=rid, list_level=1))
        blocks.append(dict(text=_txt(by[g["fokus_marker_row"]]),
                           provenance="SOURCE_CONTROLLED", row_id=g["fokus_marker_row"]))
        for ri, rv in enumerate(g["reveals"], start=1):
            blocks.append(dict(text=rv["trigger_label"], provenance="SOURCE_CONTROLLED",
                               row_id=rv["trigger_row"], list_level=1, reveal_index=ri))
            # The revealed text is placed on the storyboard page too. The page is the review
            # inventory of the whole screen; which of these the learner sees only after a
            # click is the Lampiran's question, and the state model still hides them from the
            # base state. A storyboard showing trigger labels alone is not reviewable.
            for rid in rv["content_rows"]:
                blocks.append(dict(text=_txt(by[rid]), provenance="SOURCE_CONTROLLED",
                                   row_id=rid, list_level=2, reveal_index=ri,
                                   revealed=True))
        blocks.append(dict(text=UI_REVEAL_HINT, provenance="CAIR_STRUCTURAL"))

        srows = ([g["head_row"]] + g["intro_rows"]
                 + [g["fungsi_marker_row"], g["fokus_marker_row"]] + g["fungsi_rows"]
                 + [rv["trigger_row"] for rv in g["reveals"]]
                 + [r for rv in g["reveals"] for r in rv["content_rows"]])
        srows = [r for r in srows if r]
        subj = next((v for v in um["visual_obligations"]["subjects"]
                     if any(r in srows for r in v["rows"])), None)
        add(kind="CONTENT", treatment=pol["screen_pattern_plan"]["primary"],
            title_ms=g["covers"], group=g, blocks=blocks, source_row_ids=srows,
            reveals=g["reveals"],
            vo=" ".join(p["proposition"] for p in props) or _txt(by[g["head_row"]]),
            visual=dict(subject=subj["subject"] if subj else None,
                        rows=subj["rows"] if subj else [],
                        has_source_figure=bool(subj and subj["has_source_figure"]),
                        status=PLACEHOLDER_VISUAL, note=PLACEHOLDER_SUBJECT),
            propositions=props, decision_ids=["A1", "A2"])

    # ---- Rumusan -------------------------------------------------------------------------
    rm = rumusan()
    add(kind="RUMUSAN", treatment="static content", title_ms="Rumusan",
        blocks=([dict(text=f"{c['label']}: {c['beat']}",
                      provenance="CAIR_DRAFTED_RUMUSAN_BEAT",
                      montage_id=c["component_id"]) for c in rm["montage"]]
                + [dict(text="MONTAJ RUMUSAN · " + " · ".join(MONTAGE_MARKS),
                        provenance="PROVISIONAL_PLACEHOLDER")]),
        vo=" ".join(rm["beats"]), rumusan=rm,
        visual=dict(subject="Montaj tiga komponen mengikut tiga beat Rumusan",
                    rows=[], has_source_figure=False,
                    status=PLACEHOLDER_VISUAL, note=" · ".join(MONTAGE_MARKS)),
        decision_ids=["A6"])

    # ---- Kuiz ----------------------------------------------------------------------------
    items = um["assessment"]["items"]
    qblocks = []
    for q in items:
        qblocks.append(dict(text=f"{q['slot']} · {q['stem']}",
                            provenance="CAIR_DRAFTED_ASSESSMENT",
                            cites_rows=list(q["correct_rows"])))
        for opt in ([q["correct"]] if isinstance(q["correct"], str) else q["correct"]):
            qblocks.append(dict(text=f"[dicadangkan betul] {opt}",
                                provenance="CAIR_DRAFTED_ASSESSMENT",
                                cites_rows=list(q["correct_rows"]), list_level=1))
        for d in q["distractors"]:
            qblocks.append(dict(text=d, provenance="CAIR_DRAFTED_ASSESSMENT",
                                list_level=1))
    qblocks.append(dict(text=f"Markah lulus {P.POLICY.get('quiz_pass_percent', 60)} peratus",
                        provenance="COURSE_RULE_APPROVED", decision="A7"))
    qblocks.append(dict(text=f"KUNCI JAWAPAN: {um['assessment']['key_status']}",
                        provenance="PROVISIONAL_PLACEHOLDER"))
    add(kind="KUIZ", treatment="static content", title_ms="Kuiz",
        blocks=qblocks, quiz=items,
        source_row_ids=sorted({r for q in items for r in q["correct_rows"]}),
        vo="Jawab kelima-lima soalan.", decision_ids=["A7"])

    # ---- closing -------------------------------------------------------------------------
    cl = pol["closing_screen"]
    add(kind="TAMAT", treatment="static content", title_ms="Tamat Bahagian",
        blocks=[dict(text=cl["closing_text"], provenance="COURSE_RULE_APPROVED",
                     decision="D4"),
                dict(text=UI_SETERUSNYA, provenance="CAIR_STRUCTURAL")],
        vo=cl["closing_text"], closing=cl, decision_ids=["D4"])
    return out


# ==========================================================================================
# RUNTIME STATES — T04's state grammar, K5's own inventory
# ==========================================================================================
# The grammar (kinds, ID shape, the five panel fields, the return-behaviour vocabulary) is
# T04's proven one and is reused deliberately. The COUNT is derived here and owes nothing to
# T04's 65.
STATE_KINDS = ["BASE", "REVEAL", "QUIZ_ITEM", "QUIZ_RESULT", "COMPLETION"]

RETURN_MS = {
    "BASE": "Keadaan masuk. Pelajar meneruskan dengan SETERUSNYA setelah syarat selesai "
            "dipenuhi.",
    "REVEAL": "Panel tertutup apabila ditekan sekali lagi atau apabila panel lain dibuka. "
              "Keadaan asas kembali dan sentiasa boleh dicapai. Tiada navigasi berlaku.",
    "QUIZ_ITEM": "Menghantar jawapan membawa pelajar ke item berikutnya. Tiada navigasi "
                 "kembali antara item kuiz.",
    "QUIZ_RESULT": "Keadaan akhir bagi skrin ini. Pelajar meneruskan dengan SETERUSNYA.",
    "COMPLETION": "Bukan keadaan yang dipaparkan. Penanda yang menjadi benar setelah semua "
                  "pendedahan dilihat, dan inilah yang membuka SETERUSNYA.",
}
RETURN_EN = {
    "BASE": "Entry state. The learner continues with SETERUSNYA once the completion "
            "condition is met.",
    "REVEAL": "The panel closes on a second activation or when another opens; the base state "
              "is restored and remains reachable. No navigation occurs.",
    "QUIZ_ITEM": "Submitting the item advances to the next item.",
    "QUIZ_RESULT": "Terminal state for the screen.",
    "COMPLETION": "Not a displayed state. A flag that unlocks SETERUSNYA.",
}


def _st(sid, screen, kind, **kw):
    base = dict(state_id=sid, screen_id=screen["screen_id"], position=screen["position"],
                state_kind=kind, trigger_id=None, trigger_label="screen entry",
                parent_state_id=None, resulting_state_id=sid,
                return_behaviour=RETURN_EN[kind], return_behaviour_ms=RETURN_MS[kind],
                content_block_texts=[], source_row_ids=[], authority_refs=[],
                decision_ids=list(screen["decision_ids"]), visual_obligations=[],
                differs_from_base="— this is the base state —",
                differs_from_base_ms="— ini keadaan asas —",
                binding_kind="STRUCTURAL")
    base.update(kw)
    base["content_record_count"] = len(base["content_block_texts"])
    base["declared_state_label"] = base.get("declared_state_label") or sid.split("-")[-1]
    return base


def _states_uncached():
    by = rows_by_id()
    out = []
    for sc in screens():
        sid = sc["screen_id"]
        if sc["kind"] == "KUIZ":
            for i, q in enumerate(sc["quiz"], start=1):
                opts = ([q["correct"]] if isinstance(q["correct"], str) else list(q["correct"]))
                out.append(_st(f"{sid}-ST-{i:02d}", sc, "QUIZ_ITEM",
                               trigger_id=f"{sid}-TRG-{i:02d}",
                               trigger_label=f"{q['slot']} · {q['kind']}",
                               content_block_texts=[q["stem"]] + opts + q["distractors"],
                               source_row_ids=list(q["correct_rows"]),
                               differs_from_base=f"Item {i} of {len(sc['quiz'])}.",
                               differs_from_base_ms=f"Item {i} daripada {len(sc['quiz'])}.",
                               binding_kind="SOURCE_ROWS",
                               binding_limitation="Answer key drafted, approved by nobody.",
                               binding_limitation_ms="Kunci jawapan draf — belum disahkan."))
            out.append(_st(f"{sid}-ST-RESULT", sc, "QUIZ_RESULT",
                           trigger_id=f"{sid}-TRG-RESULT",
                           trigger_label="item terakhir dihantar",
                           content_block_texts=["Markah lulus 60 peratus"],
                           differs_from_base="Score shown after the fifth item.",
                           differs_from_base_ms="Markah dipaparkan selepas item kelima.",
                           parent_state_id=f"{sid}-ST-01"))
            continue

        hidden = {r for rv in sc["reveals"] for r in rv["content_rows"]}
        base_blocks = [b for b in sc["blocks"] if b.get("row_id") not in hidden]
        base_id = f"{sid}-ST-BASE"
        out.append(_st(base_id, sc, "BASE",
                       content_block_texts=[b["text"] for b in base_blocks],
                       source_row_ids=[b["row_id"] for b in base_blocks if b.get("row_id")],
                       binding_kind="SOURCE_ROWS" if sc["source_row_ids"] else "STRUCTURAL",
                       visual_obligations=([sc["visual"]["subject"]]
                                           if sc.get("visual") and sc["visual"]["subject"]
                                           else [])))
        for i, rv in enumerate(sc["reveals"], start=1):
            texts = [_txt(by[r]) for r in rv["content_rows"] if _txt(by[r])]
            out.append(_st(f"{sid}-ST-{i:02d}", sc, "REVEAL",
                           trigger_id=f"{sid}-TRG-{i:02d}",
                           trigger_label=rv["trigger_label"],
                           parent_state_id=base_id,
                           content_block_texts=texts,
                           source_row_ids=list(rv["content_rows"]),
                           differs_from_base=f"Adds {len(texts)} record(s) hidden in base.",
                           differs_from_base_ms=f"Menambah {len(texts)} rekod yang "
                                                f"tersembunyi dalam keadaan asas.",
                           binding_kind="SOURCE_ROWS"))
        if sc["reveals"]:
            out.append(_st(f"{sid}-ST-ALL_VIEWED", sc, "COMPLETION",
                           trigger_id=f"{sid}-TRG-ALL",
                           trigger_label=f"semua {len(sc['reveals'])} panel dilihat",
                           parent_state_id=base_id,
                           differs_from_base="Not displayed; unlocks SETERUSNYA.",
                           differs_from_base_ms="Tidak dipaparkan; membuka SETERUSNYA."))
    return out


def _panel_states_uncached():
    """States the Lampiran must carry: every state on a screen with more than one state."""
    sts = states()
    counts = {}
    for s in sts:
        counts[s["screen_id"]] = counts.get(s["screen_id"], 0) + 1
    return [s for s in sts if counts[s["screen_id"]] > 1]


def _lampiran_pages_uncached(panels_per_page):
    """Panels laid out N per page, never mixing two screens on one page."""
    pages, cur, screen, no = [], [], None, 0
    for st in panel_states():
        if screen is not None and (st["screen_id"] != screen
                                   or len(cur) >= panels_per_page):
            no += 1
            pages.append(dict(page_no=no, screen_id=screen, states=cur,
                              state_ids=[x["state_id"] for x in cur]))
            cur = []
        screen = st["screen_id"]
        cur.append(st)
    if cur:
        no += 1
        pages.append(dict(page_no=no, screen_id=screen, states=cur,
                          state_ids=[x["state_id"] for x in cur]))
    return pages


# ==========================================================================================
# TRACEABILITY AND TOTALS
# ==========================================================================================
def notes_for(sc):
    """Speaker Notes = VO plus the source rows behind it. Never a new claim."""
    pol = _policy_unit()
    lines = [f"VO ({pol['narrator']['name']}): {sc['vo']}",
             "",
             "Baris sumber: " + (", ".join(sc["source_row_ids"]) or "tiada — skrin struktur"),
             "Keputusan Bariah: " + (", ".join(sc["decision_ids"]) or "—"),
             "",
             " · ".join(STATUS_MARKS)]
    return "\n".join(lines)


def _source_traceability_uncached():
    by = rows_by_id()
    out = []
    for sc in screens():
        for b in sc["blocks"]:
            rid = b.get("row_id")
            if not rid or rid not in by:
                continue
            src = _txt(by[rid])
            out.append(dict(screen_id=sc["screen_id"], row_id=rid,
                            module_page=by[rid]["module_page"],
                            provenance=b["provenance"],
                            verbatim=(b["text"] == src),
                            condensed=(b["provenance"] == "SOURCE_CONDENSED"),
                            learner_text=b["text"]))
    return out


def _totals_uncached():
    scs, sts = screens(), states()
    pol = _policy_unit()["screen_pattern_plan"]
    return dict(
        unit_id=UNIT_ID,
        screens=len(scs),
        policy_minimum_screens=pol["minimum_total_after"],
        content_screens=len([s for s in scs if s["kind"] == "CONTENT"]),
        content_groups=pol["content_groups"],
        reveals=sum(len(s["reveals"]) for s in scs),
        runtime_states=len(sts),
        states_by_kind={k: len([s for s in sts if s["state_kind"] == k])
                        for k in STATE_KINDS},
        panel_states=len(panel_states()),
        quiz_items=len(unit_model()["assessment"]["items"]),
        mcq=len([q for q in unit_model()["assessment"]["items"]
                 if q["kind"] == "MULTIPLE_CHOICE"]),
        multiple_response=len([q for q in unit_model()["assessment"]["items"]
                               if q["kind"] == "MULTIPLE_RESPONSE"]),
        source_rows_available=len(extract()["rows"]),
        source_rows_bound=len({t["row_id"] for t in source_traceability()}),
        t04_state_count_inherited=False,
        t04_screen_count_inherited=False)



# --- memoised public entry points ------------------------------------------------------


def rows_by_id():
    return _cached("rows_by_id", _rows_by_id_uncached)


def groups():
    return _cached("groups", _groups_uncached)


def screens():
    return _cached("screens", _screens_uncached)


def states():
    return _cached("states", _states_uncached)


def panel_states():
    return _cached("panel_states", _panel_states_uncached)


def source_traceability():
    return _cached("source_traceability", _source_traceability_uncached)


def totals():
    return _cached("totals", _totals_uncached)


def lampiran_pages(panels_per_page):
    return _cached(f"lampiran_pages:{panels_per_page}",
                   lambda: _lampiran_pages_uncached(panels_per_page))

if __name__ == "__main__":
    t = totals()
    for k, v in t.items():
        print(f"{k:28} {v}")
    for n in (2, 3):
        print(f"lampiran pages @{n}/page      {len(lampiran_pages(n))}")
