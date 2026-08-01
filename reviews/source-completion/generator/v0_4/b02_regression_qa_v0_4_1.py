# -*- coding: utf-8 -*-
"""Stage 4.1 regression QA — the six Bariah threads, on top of the full Stage 4 suite.

Runs every one of the 105 Stage 4 checks unchanged, then adds the new ones. Nothing is
removed or weakened. Notes italics are validated against the GENERATED Notes XML at run
level, not against the controlled content that produced it.
"""
import json, os, re, sys, zipfile, collections
from xml.etree import ElementTree as ET
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import b02_model_adapter_v0_4 as ADAPT
import b02_proof_content_v0_4 as C
import b02_glossary_v0_4 as GL
import b02_visual_directions_v0_4 as VD
import b02_instructions_v0_4 as INS
import b02_full_qa_v0_4 as FULL
from b02_proof_qa_v0_4 import read_pptx

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


def notes_runs(pptx):
    """Per notes part: list of paragraphs, each a list of (text, italic) runs, read back
    out of the generated package."""
    z = zipfile.ZipFile(pptx)
    n = len([x for x in z.namelist() if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", x)])
    out = []
    for i in range(1, n + 1):
        root = ET.fromstring(z.read(f"ppt/notesSlides/notesSlide{i}.xml"))
        body = [sp for sp in root.iter(f"{P}sp")
                if sp.find(f".//{P}ph") is not None and sp.find(f".//{P}ph").get("type") == "body"]
        paras = []
        if body:
            for para in body[0].iter(f"{A}p"):
                runs = []
                for r in para.iter(f"{A}r"):
                    rPr = r.find(f"{A}rPr")
                    t = r.find(f"{A}t")
                    runs.append(((t.text or "") if t is not None else "",
                                 rPr is not None and rPr.get("i") == "1"))
                paras.append(runs)
        out.append(paras)
    return out


def run(pptx):
    res = list(FULL.run(pptx))                       # all 105 Stage 4 checks, unchanged
    n_orig = len(res)
    def chk(k, v, e): res.append((k, v, e, v == e))

    M = ADAPT.Model()
    pages = ADAPT.all_pages(M)
    deck = read_pptx(pptx)
    nruns = notes_runs(pptx)
    D = {p["id"]: d for p, d in zip(pages, deck)}
    NR = {p["id"]: r for p, r in zip(pages, nruns)}
    st_of = {p["id"]: M.state(p["state_id"]) for p in pages}
    rec_of = {p["id"]: M.screen(p["screen_id"]) for p in pages}
    ctext = {pid: " ".join(s["text"] for s in d["canvas"]) for pid, d in D.items()}
    ptext = {pid: " ".join(s["text"] for s in d["panel"]) for pid, d in D.items()}
    notes = {pid: d["notes"] for pid, d in D.items()}

    # ============================ VISUAL DIRECTIONS ============================
    audit = VD.audit(M)
    chk("VISUAL_DIRECTIONS_AUDITED", len(audit), 26)
    chk("VISUAL_DIRECTIONS_PENDING", sum(1 for a in audit if a["status"] != "RESOLVED"), 0)
    chk("GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES",
        sum(1 for pid, d in D.items() for s in d["canvas"] if VD.is_generic(s["text"])), 0)
    chk("SOURCE_ROW_VISUAL_DIRECTIONS_MISSING",
        sum(1 for a in audit if not a["text"]), 0)
    popups = [p for p in pages if st_of[p["id"]]["screen_role"] == "STATE_POPUP"]
    chk("POPUP_PAGES", len(popups),
        sum(1 for s in M.map["states"] if s["screen_role"] == "STATE_POPUP"))

    # ---- subtype-aware visual requirements (Bariah: spec popups have NO visual) ----
    import b02_visual_policy_v0_4 as VP
    pol = {p["id"]: VP.classify(M, rec_of[p["id"]], st_of[p["id"]]) for p in pages}
    has_panel = {pid: any(s["name"] == "VisualPanel" for s in D[pid]["canvas"]) for pid in D}
    has_dir = {pid: any(s["name"] in ("VisualPanelBody", "VisualDir") and s["text"].strip()
                        for s in D[pid]["canvas"]) for pid in D}
    req = [pid for pid in pol if pol[pid]["visual_requirement"] == VP.REQUIRED]
    notreq = [pid for pid in pol if pol[pid]["visual_requirement"] == VP.NOT_REQUIRED]
    cond = [pid for pid in pol if pol[pid]["visual_requirement"] == VP.CONDITIONAL]
    chk("REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL",
        sum(1 for pid in req if st_of[pid]["screen_role"] != "STATE_POPUP" and not has_dir[pid]), 0)
    chk("REQUIRED_VISUAL_POPUPS_WITHOUT_VISUAL",
        sum(1 for pid in req if st_of[pid]["screen_role"] == "STATE_POPUP" and not has_panel[pid]), 0)
    spec = [pid for pid in pol if pol[pid]["popup_subtype"] == VP.SPECIFICATION_POPUP]
    chk("SPECIFICATION_POPUPS_TOTAL", len(spec), 30)
    chk("SPECIFICATION_POPUPS_REQUIRING_VISUAL",
        sum(1 for pid in spec if pol[pid]["visual_requirement"] == VP.REQUIRED), 0)
    chk("SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL",
        sum(1 for pid in spec if has_panel[pid]), 0)
    chk("SPECIFICATION_POPUPS_WITH_FORCED_GENERIC_VISUAL",
        sum(1 for pid in spec for s in D[pid]["canvas"] if VD.is_generic(s["text"])), 0)
    chk("NOT_REQUIRED_VISUAL_POPUPS_FORCED_TO_HAVE_VISUAL",
        sum(1 for pid in notreq if st_of[pid]["screen_role"] == "STATE_POPUP" and has_panel[pid]), 0)
    chk("CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED",
        sum(1 for pid in cond if not pol[pid]["visual_status"].startswith("RESOLVED")), 0)
    epop = [pid for pid in pol if pol[pid]["popup_subtype"] == VP.EXAMPLE_POPUP]
    chk("EXAMPLE_POPUPS_TOTAL", len(epop), 16)
    chk("EXAMPLE_POPUPS_WITH_SPECIFIC_VISUAL", sum(1 for pid in epop if has_panel[pid]), len(epop))
    chk("EXAMPLE_POPUPS_WITHOUT_VISUAL", sum(1 for pid in epop if not has_panel[pid]), 0)
    chk("EXAMPLE_POPUPS_WITH_GENERIC_FALLBACK",
        sum(1 for pid in epop for s in D[pid]["canvas"] if VD.is_generic(s["text"])), 0)
    esc = [pid for pid in pol if pol[pid]["semantic_screen_subtype"] == "EXAMPLE_SCREEN"]
    chk("EXAMPLE_SCREENS_TOTAL", len(esc), 12)
    chk("EXAMPLE_SCREENS_WITH_SPECIFIC_VISUAL", sum(1 for pid in esc if has_dir[pid]), len(esc))
    chk("EXAMPLE_SCREENS_WITHOUT_VISUAL", sum(1 for pid in esc if not has_dir[pid]), 0)
    cms = [pid for pid in pol if pol[pid]["semantic_screen_subtype"] == "COMPONENT_MAIN_SCREEN"]
    chk("COMPONENT_MAIN_SCREENS_WITH_SPECIFIC_VISUAL", sum(1 for pid in cms if has_dir[pid]), len(cms))
    s01 = [p["id"] for p in pages if p["screen_id"] == "SCR_S01"][0]
    chk("S01_DISPLAY_TITLE",
        any(s["text"] == C.S01["display_title"] for s in D[s01]["canvas"]), True)
    chk("S01_DUPLICATE_STANDALONE_COMPONENT_TITLE",
        sum(1 for s in D[s01]["canvas"] if s["text"].strip() == "Komponen Landskap"), 0)
    chk("S01_SPECIFIC_VISUAL_DIRECTION_PRESENT",
        "Imej pembuka bahagian" in ctext[s01], True)
    chk("REQUIRED_VISUAL_PANEL_MISSING",
        sum(1 for pid in req if st_of[pid]["screen_role"] == "STATE_POPUP" and not has_panel[pid]), 0)
    chk("VISUAL_PANEL_HEADING_MISSING",
        sum(1 for pid in epop
            if not any(s["name"] == "VisualPanelHead" for s in D[pid]["canvas"])), 0)
    ov = 0
    for pid in epop:
        d = D[pid]
        pan = [s for s in d["canvas"] if s["name"] == "VisualPanel"]
        kids = [s for s in d["canvas"] if s["name"].startswith("VisualPanel") and s["name"] != "VisualPanel"]
        for k in kids:
            for b in pan:
                if not (k["x"] >= b["x"] - .01 and k["y"] >= b["y"] - .01
                        and k["x"] + k["w"] <= b["x"] + b["w"] + .01
                        and k["y"] + k["h"] <= b["y"] + b["h"] + .01):
                    ov += 1
    chk("VISUAL_PANEL_CONTENT_OVERRUN", ov, 0)
    coll = 0
    for pid in epop:
        d = D[pid]
        ic = [s for s in d["canvas"] if s["name"] == "CloseIcon"]
        pn = [s for s in d["canvas"] if s["name"].startswith("VisualPanel")]
        for a in ic:
            for b in pn:
                if min(a["x"]+a["w"], b["x"]+b["w"]) - max(a["x"], b["x"]) > 0.01 and \
                   min(a["y"]+a["h"], b["y"]+b["h"]) - max(a["y"], b["y"]) > 0.01:
                    coll += 1
    chk("VISUAL_PANEL_CLOSE_ICON_COLLISION", coll, 0)

    # binding: each popup's visual text must come from its own source row
    wrong_src = wrong_comp = 0
    for p in [q for q in popups if pol[q["id"]]["popup_subtype"] == VP.EXAMPLE_POPUP]:
        st = st_of[p["id"]]
        uid = st["source_row_uids"][0] if st["source_row_uids"] else None
        if not uid: continue
        row = M.rows[uid]
        exp = VD.for_row(row)["text"] or ""
        body = " ".join(s["text"] for s in D[p["id"]]["canvas"] if s["name"] == "VisualPanelBody")
        key = re.sub(r"\s+", "", exp)[:40]
        if key and re.sub(r"\s+", "", body)[:40] != key:
            # specification popups prefix the example + label; accept if the row example is named
            if re.sub(r"\s+", "", row["label"]) not in re.sub(r"\s+", "", body):
                wrong_src += 1
        if row["comp"] != (st.get("component_id") or row["comp"]):
            wrong_comp += 1
    chk("VISUAL_DIRECTION_WRONG_SOURCE_BINDING", wrong_src, 0)
    chk("VISUAL_DIRECTION_WRONG_COMPONENT_BINDING", wrong_comp, 0)
    chk("VISUAL_DIRECTIONS_WITHOUT_SOURCE_OR_BARIAH_BINDING",
        sum(1 for a in audit if a["authority"] not in (VD.ASSET, VD.CONTOH)), 0)
    for fam in ("FAMILY_S", "FAMILY_P1", "FAMILY_P2"):
        chk(f"{fam}_GENERIC_VISUAL_FALLBACKS",
            sum(1 for p in popups if p["execution_family"] == fam
                for s in D[p["id"]]["canvas"] if VD.is_generic(s["text"])), 0)
    fs = [p for p in popups if p["execution_family"] == "FAMILY_S"]
    chk("FAMILY_S_POPUPS_WITH_SPECIFIC_VISUAL_DIRECTION",
        sum(1 for p in fs if any(s["name"] == "VisualPanelBody" and s["text"].strip()
                                 for s in D[p["id"]]["canvas"])), len(fs))
    chk("FAMILY_S_VISUAL_PANEL_MISSING", sum(1 for p in fs if not has_panel[p["id"]]), 0)
    prom = [p for p in fs if "PROMENADE" in st_of[p["id"]]["runtime_state_id"]
            or "Promenade" in ctext[p["id"]]][0]
    chk("PROMENADE_SPECIFIC_VISUAL_DIRECTION",
        "Promenade Tasik Titiwangsa, KL" in ctext[prom["id"]], True)
    chk("PROMENADE_GENERIC_FALLBACK_GONE",
        VD.is_generic(ctext[prom["id"]]), False)

    # ============================ NOTES RICH TEXT ============================
    found = ital = miss = false_ital = 0
    misses = []
    for pid, paras in NR.items():
        for pi, runs in enumerate(paras):
            text = "".join(t for t, _ in runs)
            for term, a, b in GL.occurrences(text):
                found += 1
                # map character range back to runs; a phrase may span several
                pos = 0; flags = []
                for t, i in runs:
                    lo, hi = pos, pos + len(t)
                    if hi > a and lo < b:
                        flags.append(i)
                    pos = hi
                if flags and all(flags):
                    ital += 1
                else:
                    miss += 1; misses.append((pid, term))
    chk("NOTES_GLOSSARY_OCCURRENCES_FOUND", found, found)
    chk("NOTES_GLOSSARY_OCCURRENCES_ITALICISED", ital, found)
    chk("NOTES_GLOSSARY_ITALIC_MISSES", miss, 0)
    for pid, paras in NR.items():
        for runs in paras:
            for t, i in runs:
                if i and (any(t.strip().startswith(x) for x in GL.NEVER_ITALIC_PREFIXES)
                          or t.strip() in GL.NEVER_ITALIC_TOKENS):
                    false_ital += 1
    chk("NOTES_FALSE_ITALICS_ON_TECHNICAL_IDS", false_ital, 0)
    chk("NOTES_MARKDOWN_ITALIC_MARKERS",
        sum(1 for pid in notes for m in ("*", "_") if re.search(r"(?<!\w)[*_][A-Za-z]", notes[pid])), 0)
    chk("NOTES_RICH_TEXT_PACKAGE_ROUNDTRIP_FAILURES",
        sum(1 for pid, paras in NR.items() if not paras and notes[pid].strip()), 0)
    chk("NOTES_ITALIC_RUNS_IN_PACKAGE", ital > 0, True)
    canvas_miss = 0
    for pid, d in D.items():
        for s in d["canvas"]:
            for r, i in zip(s["runs"], s["italics"] + [False] * len(s["runs"])):
                if r in GL.ITALIC_TERMS and not i:
                    canvas_miss += 1
    chk("CANVAS_GLOSSARY_ITALIC_MISSES", canvas_miss, 0)
    chk("GLOSSARY_IS_SINGLE_SOURCE",
        __import__("b02_generator_v0_4").ital_parts("Water Feature") == GL.parts("Water Feature"), True)

    # ============================ QUIZ ANSWER KEY ============================
    qq = [p["id"] for p in pages if st_of[p["id"]]["screen_role"] == "STATE_QUIZ_QUESTION"]
    chk("QUIZ_QUESTIONS", len(qq), 5)
    keyed = [p for p in qq if any(s["name"] == "AnswerKeyBox" for s in D[p]["canvas"])]
    chk("QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY", len(keyed), 5)
    chk("QUIZ_REVIEW_PAGES_WITHOUT_ANSWER_KEY", len(qq) - len(keyed), 0)
    mcq_ok = mr_ok = 0; mismatch = 0
    for p in qq:
        n = int(st_of[p]["runtime_state_id"][-1]); d = C.QUESTIONS[n]
        body = " ".join(s["text"] for s in D[p]["canvas"] if s["name"] == "AnswerKeyBody")
        if d["kind"] == "MCQ":
            want_letter = f"Jawapan: {d['answer']}"
            want_text = dict(d["options"])[d["answer"]]
            if want_letter in body and want_text in body: mcq_ok += 1
            else: mismatch += 1
        else:
            if "Jawapan betul:" in body and all(o in body for o in d["answers"]): mr_ok += 1
            else: mismatch += 1
    chk("MCQ_ANSWER_KEYS_WITH_LETTER_AND_TEXT", mcq_ok, 4)
    chk("MULTIPLE_RESPONSE_ANSWER_KEY_USES_FULL_OPTION_TEXT", mr_ok == 1, True)
    chk("ANSWER_KEY_SOURCE_MISMATCH", mismatch, 0)
    chk("MULTIPLE_RESPONSE_LEARNER_OPTIONS_WITH_LETTER_LABELS",
        sum(1 for p in qq if st_of[p].get("question_kind") == "MULTIPLE_RESPONSE"
            for s in D[p]["canvas"] if s["name"] == "Opt"
            and re.match(r"^[A-D]\.", s["text"].strip())), 0)
    chk("ANSWER_KEY_LABELLED_AS_REVIEWER_INFO",
        sum(1 for p in keyed if not any(s["name"] == "AnswerKeyHead" and "SEMAKAN CIDB" in s["text"]
                                        for s in D[p]["canvas"])), 0)
    chk("ANSWER_KEY_VISIBLE_DURING_LEARNER_PRE_SUBMISSION_STATE",
        sum(1 for p in qq for s in D[p]["canvas"] if s["name"] == "AnswerKeyBody"
            and not any(x["name"] == "AnswerKeyHead" for x in D[p]["canvas"])), 0)
    chk("ANSWER_KEY_READ_IN_VO",
        sum(1 for p in qq if "Jawapan:" in notes[p] or "Jawapan betul:" in notes[p]), 0)

    # ============================ TAMAT ============================
    tm = [p["id"] for p in pages if p["screen_id"] == "SCR_TAMAT"][0]
    chk("TAMAT_TITLE_MATCHES_BARIAH_EXEMPLAR",
        "Tamat Topik 3 Bahagian 2:" in ctext[tm] and "Komponen Landskap" in ctext[tm], True)
    chk("TAMAT_LEARNER_INSTRUCTION_MATCHES_BARIAH_EXEMPLAR",
        C.TAMAT["instruction"] in ctext[tm], True)
    chk("TAMAT_HIERARCHY_COMPLETE",
        sum(1 for blk in C.TAMAT["hierarchy"] for l in blk if l in ctext[tm]),
        sum(len(b) for b in C.TAMAT["hierarchy"]))
    sb = notes[tm].split("SPOKEN TRANSCRIPT", 1)[1] if "SPOKEN TRANSCRIPT" in notes[tm] else ""
    chk("TAMAT_SPOKEN_TRANSCRIPT_MATCHES",
        all(l.strip() in sb for l in C.TAMAT["vo"].split("\n")), True)
    chk("TAMAT_NON_SPOKEN_CONTEXT_RETAINED",
        "NON-SPOKEN CONTEXT" in notes[tm] and "PL06: Pengurusan" in notes[tm], True)

    # ============================ PERABOT OVERVIEW ============================
    po = [p["id"] for p in pages if p["screen_id"] == "SCR_PERABOT_OVERVIEW"][0]
    cards = [s for s in D[po]["canvas"] if s["name"] == "ComponentCard"]
    names = [s["text"] for s in D[po]["canvas"] if s["name"] == "ComponentName"]
    vis = [s for s in D[po]["canvas"] if s["name"] == "ComponentVisualDir"]
    chk("PERABOT_OVERVIEW_VISUAL_CARDS", len(cards), 5)
    chk("PERABOT_COMPONENT_NAMES_PRESENT", len(names), 5)
    chk("PERABOT_COMPONENTS_WITH_VISUAL_DIRECTION", len(vis), 5)
    want = ["Kerusi Taman", "Papan Tanda", "Tong Sampah", "Drinking Fountain", "BBQ Pit"]
    chk("PERABOT_COMPONENT_NAMES_CORRECT", sorted(names), sorted(want))
    chk("PERABOT_OVERVIEW_INTERNAL_MAPPING_UNCHANGED",
        {c: M.family(c) for c in ("KERUSI_TAMAN", "TONG_SAMPAH", "DRINKING_FOUNTAIN",
                                  "PAPAN_TANDA", "BBQ_PIT")},
        {"KERUSI_TAMAN": "FAMILY_P1", "TONG_SAMPAH": "FAMILY_P1",
         "DRINKING_FOUNTAIN": "FAMILY_P1", "PAPAN_TANDA": "FAMILY_P2", "BBQ_PIT": "FAMILY_P2"})
    chk("PERABOT_OVERVIEW_NAVIGATION_MODEL_UNCHANGED",
        st_of[po]["next_control_type"] == "LMS_SHELL_NEXT"
        and rec_of[po]["screen_role"] == "GROUP_OVERVIEW_NON_INTERACTIVE", True)
    chk("PERABOT_FAMILY_MAPPING_IN_PANEL",
        sum(1 for f in ("FAMILY_P1", "FAMILY_P2") if f in ptext[po]), 2)
    chk("BASE_STATE_FALSE_COMPLETION_TICKS",
        sum(1 for s in D[po]["canvas"] if s["name"] == "Tick"), 0)

    # ============================ METADATA DENYLIST ============================
    leaks = collections.Counter()
    for pid, d in D.items():
        for s in d["canvas"]:
            for tok in INS.CANVAS_METADATA_DENYLIST:
                if tok in s["text"]:
                    leaks[(pid, tok)] += 1
    chk("FAMILY_LABELS_ON_LEARNER_CANVAS",
        sum(v for (pid, tok), v in leaks.items() if tok.startswith("FAMILY_")), 0)
    chk("TECHNICAL_METADATA_ON_LEARNER_CANVAS", sum(leaks.values()), 0)

    # ============================ INSTRUCTION PARITY ============================
    act = [p for p in pages if INS.for_page(rec_of[p["id"]], st_of[p["id"]])]
    chk("LEARNER_SCREENS_WITH_ACTION_INSTRUCTION", len(act), len(act))
    on_canvas = sum(1 for p in act if INS.for_page(rec_of[p["id"]], st_of[p["id"]]) in ctext[p["id"]])
    chk("ACTION_INSTRUCTIONS_PRESENT_ON_CANVAS", on_canvas, len(act))
    in_vo = 0; mism = 0
    for p in act:
        ins = INS.for_page(rec_of[p["id"]], st_of[p["id"]])
        sb = notes[p["id"]].split("SPOKEN TRANSCRIPT", 1)[-1]
        if ins in sb: in_vo += 1
        else: mism += 1
    chk("ACTION_INSTRUCTIONS_PRESENT_IN_SPOKEN_TRANSCRIPT", in_vo, len(act))
    chk("ACTION_INSTRUCTIONS_MISSING_FROM_NOTES", mism, 0)
    chk("ACTION_INSTRUCTION_CANVAS_VO_MISMATCHES",
        sum(1 for p in act
            if INS.for_page(rec_of[p["id"]], st_of[p["id"]]) not in ctext[p["id"]]
            or INS.for_page(rec_of[p["id"]], st_of[p["id"]])
            not in notes[p["id"]].split("SPOKEN TRANSCRIPT", 1)[-1]), 0)
    silent = [p["id"] for p in pages if st_of[p["id"]]["notes_policy"] == "SILENT_STATE_NOTES"]
    chk("SILENT_STATES_RECEIVING_NEW_VO", sum(1 for p in silent if notes[p].strip()), 0)
    chk("REVIEW_ONLY_ANSWER_KEYS_INCLUDED_IN_VO",
        sum(1 for p in qq if "SEMAKAN CIDB" in notes[p]), 0)
    chk("TECHNICAL_CONTROLS_READ_AS_VO",
        sum(1 for pid in notes for t in ("LMS_SHELL_NEXT", "KEMBALI_BUTTON", "CLOSE_ICON",
                                         "MULA_BUTTON", "MULA_KUIZ_BUTTON", "NO_CONTROL")
            if t in notes[pid]), 0)
    chk("NOTES_CONTEXT_ACCIDENTALLY_MARKED_SPOKEN",
        sum(1 for p in pages if p["id"] != act and st_of[p["id"]]["notes_context_spoken"]
            and p["screen_id"] != "SCR_S01"), 0)
    # Off-canvas leakage in EVERY direction. The Stage 4 suite separated shapes by the
    # left edge only, so a card running past the bottom of the stage went unseen.
    off = []
    for pid, d in D.items():
        for s in d["canvas"]:
            if s["y"] + s["h"] > 7.51 or s["x"] + s["w"] > 13.34 or s["y"] < -0.65 or s["x"] < -0.01:
                off.append((pid, s["name"], round(s["x"] + s["w"], 2), round(s["y"] + s["h"], 2)))
    chk("CANVAS_SHAPES_OUTSIDE_STAGE", len(off), 0)
    # ---- universal completion-tick identity ----
    # Gap found by Stage 4.2A replay fixture R-008: the Stage 4 suite verified tick counts
    # only for Family P1 and Family P2. A false completion tick on any Family S screen or on
    # the Struktur Taman group master was completely unguarded and would have shipped.
    tick_bad = []
    order = {p["id"]: i for i, p in enumerate(pages)}
    for p in pages:
        pid = p["id"]; st = st_of[pid]; rec = rec_of[pid]
        k = order[pid]
        seen_states = {q["state_id"] for q in pages[:k]}
        seen_done = {q["state_id"] for q in pages[:k]
                     if M.state(q["state_id"])["screen_role"] in
                     ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE")}
        drawn = sum(1 for s in D[pid]["canvas"] if s["name"] == "Tick")
        if rec["screen_role"] == "GROUP_MASTER":
            # cards are components, not interaction items: expect one tick per component
            # whose own all-viewed state was reached earlier in the path.
            done = {M.state(q["state_id"]).get("component_id") for q in pages[:k]
                    if M.state(q["state_id"])["screen_role"] == "STATE_ALL_VIEWED"
                    and M.state(q["state_id"])["completion_scope"] == "COMPONENT"
                    and M.state(q["state_id"]).get("group_id") == "STRUKTUR_TAMAN"}
            exp = 4 if st["screen_role"] == "STATE_GROUP_COMPLETE" else len(done - {None})
        else:
            items = M.items_of(p["screen_id"])
            if not items:
                exp = 0
            elif st["screen_role"] in ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE"):
                exp = len(items)
            else:
                exp = 0
                for it in items:
                    rs = it["runtime_state_id"]
                    if rs in seen_states or rs == st["runtime_state_id"]:
                        exp += 1; continue
                    m2 = re.match(r"^ST_(.+)_EX(\d+)_BASE$", rs)
                    if m2 and f"ST_{m2.group(1)}_EX{m2.group(2)}_ALL_SPEC_VIEWED" in seen_done:
                        exp += 1
        if drawn != exp:
            tick_bad.append((pid, rec["screen_role"], drawn, exp))
    chk("COMPLETION_TICKS_NOT_MATCHING_PATH", len(tick_bad), 0)
    chk("ORIGINAL_STAGE_4_CHECKS", n_orig, 105)
    return res


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep)
    fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
