# -*- coding: utf-8 -*-
"""Stage 4.2E-B mutation replay: every prior fixture rebased onto v0.4.4, plus fixtures for
the rulings implemented at this stage.

New at 4.2E-B (Part 8):
  C-01 Papan Tanda overview reduced from two subjects to one
  C-02 a Papan Tanda subject replaced with an invented subject
  C-03 a Papan Tanda subject replaced with a cross-component subject
  C-04 BBQ Pit given a duplicated second visual
  C-05 BBQ Pit given an invented second subject
  C-06 the sole BBQ Pit overview visual removed
  C-07 Papan Tanda Informasi / Penunjuk Arah bindings swapped onto unrelated figures
       while the shape COUNT is preserved
  C-08 overview removed from an all-viewed state
  C-09 overview removed from a specification-popup state (outside base classification)
  C-10 a Slide 5 bullet changed
  C-11 trailing full stops added to the Slide 5 bullets
  C-12 Slide 5 content removed from the spoken VO
  C-13 the two S01 trailing periods restored
  C-14 detailed rationale inserted into Speaker Notes
  C-15 a quiz feedback string changed
  C-16 a micro-control instruction added to spoken VO
  C-17 a confirmed screen-level Klik instruction removed from VO
  C-18 Alya inserted into an unrelated screen
  C-19 automatic Tamat navigation claimed
  C-20 spoken_as "PL enam" activated
  C-21 a specification popup given a visual panel

Fixtures are built in a temp directory and discarded. No committed artifact is mutated.
"""
import json, os, re, shutil, sys, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(os.path.dirname(HERE), "v0_4")
sys.path.insert(0, V4); sys.path.insert(0, HERE)
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_4 as QA
import b02_replay_v0_4_2 as P42
import b02_replay_v0_4_3 as P43
from b02_replay_v0_4_2 import mutate, _sub_text, _drop_shape

R = os.path.dirname(os.path.dirname(HERE))
GOOD = os.path.join(R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4.pptx")
PRIOR_DECKS = {
    "v0_4": os.path.join(R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx"),
    "v0_4_1": os.path.join(R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx"),
    "v0_4_2": os.path.join(R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_2.pptx"),
    "v0_4_3": os.path.join(R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx"),
}


def _drop_named(xml, name, nth=0):
    pat = re.compile(r"<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?</p:sp>" % re.escape(name), re.S)
    ms = list(pat.finditer(xml))
    assert len(ms) > nth, f"{name}: wanted #{nth}, found {len(ms)}"
    m = ms[nth]
    return xml[:m.start()] + xml[m.end():]


def _clone_named(xml, name):
    pat = re.compile(r"(<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?</p:sp>)" % re.escape(name), re.S)
    m = pat.search(xml)
    assert m, f"shape not found: {name}"
    return xml[:m.end()] + m.group(1) + xml[m.end():]


def build_all(tmp):
    P42.GOOD = GOOD
    P43.GOOD = GOOD
    out = P43.build_all(tmp)                    # 18 defect-shape fixtures, rebased

    M = ADAPT.Model(); pages = ADAPT.all_pages(M)
    idx = {p["state_id"]: i + 1 for i, p in enumerate(pages)}
    def slide(s): return f"ppt/slides/slide{idx[s]}.xml"
    def notes(s): return f"ppt/notesSlides/notesSlide{idx[s]}.xml"

    def add(fid, title, gate, edits):
        path = os.path.join(tmp, f"{fid}.pptx")
        mutate(GOOD, path, edits)
        out.append(dict(regression_id=fid, title=title, gate=gate, fixture=path,
                        kind="MUTATION"))

    PT, BQ = "ST_PAPAN_TANDA_MAIN_BASE", "ST_BBQ_PIT_MAIN_BASE"

    add("C-01", "Papan Tanda overview reduced from two subjects to one",
        "PAPAN_TANDA_OVERVIEW_VISUAL_COUNT|OVERVIEW_CARDINALITY_MAPPING_MISMATCHES",
        [(slide(PT), lambda x: _drop_named(x, "OverviewSubject", 1))])
    add("C-02", "a Papan Tanda subject replaced with an invented subject",
        "PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT|UNAUTHORISED_OVERVIEW_SUBJECTS",
        [(slide(PT), lambda x: _sub_text(x, "<a:t>Papan Tanda Informasi</a:t>",
                                         "<a:t>Pelbagai Papan Tanda</a:t>"))])
    add("C-03", "a Papan Tanda subject replaced with a cross-component subject",
        "PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT|UNAUTHORISED_OVERVIEW_SUBJECTS",
        [(slide(PT), lambda x: _sub_text(x, "<a:t>Papan Tanda Penunjuk Arah</a:t>",
                                         "<a:t>BBQ Pit Struktur Kekal</a:t>"))])
    add("C-04", "BBQ Pit given a duplicated second visual",
        "BBQ_PIT_OVERVIEW_VISUAL_COUNT|BBQ_PIT_OVERVIEW_SUBJECT_NOT_DUPLICATED",
        [(slide(BQ), lambda x: _clone_named(x, "OverviewSubject"))])
    add("C-05", "BBQ Pit given an invented second subject",
        "BBQ_PIT_OVERVIEW_VISUAL_COUNT|OVERVIEW_COUNTS_BY_COMPONENT",
        [(slide(BQ), lambda x: _sub_text(
            x, "<a:t> Struktur Kekal</a:t>",
            "<a:t> Struktur Kekal</a:t></a:r></a:p></p:txBody></p:sp>"
            "<p:sp><p:nvSpPr><p:cNvPr id=\"901\" name=\"OverviewSubject\"/><p:cNvSpPr txBox=\"1\"/>"
            "<p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x=\"3200400\" y=\"5300000\"/>"
            "<a:ext cx=\"2194560\" cy=\"310896\"/></a:xfrm><a:prstGeom prst=\"rect\">"
            "<a:avLst/></a:prstGeom></p:spPr><p:txBody><a:bodyPr wrap=\"square\"/><a:lstStyle/>"
            "<a:p><a:r><a:rPr lang=\"ms-MY\" sz=\"900\"/><a:t>BBQ Pit Mudah Alih</a:t>"))])
    add("C-06", "the sole BBQ Pit overview visual removed",
        "BBQ_PIT_OVERVIEW_VISUAL_COUNT|COMPONENT_MAIN_OVERVIEWS_RENDERED",
        [(slide(BQ), lambda x: _drop_named(x, "OverviewSubject"))])
    add("C-07", "Papan Tanda subject bindings swapped onto unrelated figures, count preserved",
        "PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT|UNAUTHORISED_OVERVIEW_SUBJECTS",
        [(slide(PT), lambda x: _sub_text(
            _sub_text(x, "<a:t>Papan Tanda Informasi</a:t>", "<a:t>__PT_A__</a:t>"),
            "<a:t>Papan Tanda Penunjuk Arah</a:t>", "<a:t>Papan Tanda Informasi</a:t>")
            .replace("<a:t>__PT_A__</a:t>", "<a:t>Papan Tanda Penunjuk Arah</a:t>"))])
    add("C-08", "overview removed from an all-viewed state",
        "BASE_TO_ALL_VIEWED_OVERVIEW_IDENTITY_MISMATCHES|PERSISTENCE_TARGET_PAGES_MISSING_VISUALS",
        [(slide("ST_PAPAN_TANDA_ALL_CATEGORIES_VIEWED"),
          lambda x: _drop_named(x, "OverviewSubject"))])
    add("C-09", "overview removed from a specification-popup state outside base classification",
        "BASE_TO_RETURN_OVERVIEW_IDENTITY_MISMATCHES|PERSISTENCE_TARGET_PAGES_MISSING_VISUALS",
        [(slide("ST_PAPAN_TANDA_CAT02"), lambda x: _drop_named(x, "OverviewSubject"))])
    add("C-10", "a Slide 5 bullet changed",
        "SLIDE5_BULLET_2_EXACT",
        [(slide("ST_STRUKTUR_PERSISIR_AIR_MAIN_BASE"), lambda x: _sub_text(
            x, "Pemilihan bahan permukaan bergantung pada fungsi utama",
            "Pemilihan bahan permukaan mengikut belanjawan projek"))])
    add("C-11", "trailing full stops added to the Slide 5 bullets",
        "SLIDE5_BULLET_TRAILING_PERIODS",
        [(slide("ST_STRUKTUR_PERSISIR_AIR_MAIN_BASE"), lambda x: _sub_text(
            x, "Pemilihan bahan permukaan bergantung pada fungsi utama</a:t>",
            "Pemilihan bahan permukaan bergantung pada fungsi utama.</a:t>"))])
    add("C-12", "Slide 5 content removed from the spoken VO",
        "SLIDE5_VO_IN_PACKAGE_NOTES|SLIDE5_CANVAS_VO_MISMATCHES",
        [(notes("ST_STRUKTUR_PERSISIR_AIR_MAIN_BASE"), lambda x: _sub_text(
            x, "Asas pembinaannya:", "Nota dalaman:"))])
    add("C-13", "the two S01 trailing periods restored",
        "S01_LINE_1_TRAILING_PERIOD|SHOT_S01_PACKAGE_NOTES_EXACT",
        [(notes("ST_S01_BASE"), lambda x: _sub_text(
            x, "<a:t>PL06: Pengurusan Operasi Pembinaan Landskap</a:t>",
            "<a:t>PL06: Pengurusan Operasi Pembinaan Landskap.</a:t>"))])
    add("C-14", "detailed rationale inserted into Speaker Notes",
        "QUIZ_RATIONALE_IN_SPEAKER_NOTES",
        [(notes("ST_KUIZ_Q1"), lambda x: _sub_text(
            x, "</a:t></a:r>",
            "</a:t></a:r><a:r><a:rPr lang=\"ms-MY\"/><a:t>Modul ms 238 menyatakan asas "
            "yang sangat stabil dan rata dengan sistem</a:t></a:r>"))])
    add("C-15", "a quiz feedback string changed",
        "QUIZ_CORRECT_FEEDBACK_EXACT_MATCH",
        [(slide("ST_KUIZ_Q3"), lambda x: _sub_text(
            x, "<a:t>Pilihan jawapan tepat.</a:t>", "<a:t>Jawapan anda betul.</a:t>"))])
    add("C-16", "a micro-control instruction added to spoken VO",
        "MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES|MICRO_CONTROL_INSTRUCTIONS_IN_SPOKEN_VO",
        [(notes("ST_KUIZ_RESULT"), lambda x: _sub_text(
            x, "</a:t></a:r>",
            "</a:t></a:r><a:r><a:rPr lang=\"ms-MY\"/><a:t>Klik Semak Jawapan untuk "
            "meneruskan.</a:t></a:r>"))])
    add("C-17", "a confirmed screen-level Klik instruction removed from VO",
        "ACTION_INSTRUCTIONS_MISSING_FROM_NOTES|CONFIRMED_SCREEN_LEVEL_CLICK_MISMATCHES",
        [(notes("ST_KEMUDAHAN_AWAM_EXAMPLES_BASE"), lambda x: _sub_text(
            x, "Klik pada setiap contoh untuk penjelasan lanjut.", "", 1))])
    add("C-18", "Alya inserted into an unrelated screen",
        "CAST_NAMES_ON_UNRELATED_SCREENS",
        [(slide("ST_BBQ_PIT_MAIN_BASE"), lambda x: _sub_text(
            x, "<a:t>BBQ Pit</a:t>", "<a:t>Alya — BBQ Pit</a:t>"))])
    add("C-19", "automatic Tamat navigation claimed",
        "TAMAT_MECHANISM_ON_LEARNER_CANVAS",
        [(slide("ST_TAMAT_BASE"), lambda x: _sub_text(
            x, "<a:t>Teruskan pembelajaran ke bahagian seterusnya.</a:t>",
            "<a:t>Anda akan dibawa secara automatik ke bahagian seterusnya.</a:t>"))])
    add("C-20", "spoken_as PL enam activated",
        "UNRATIFIED_PL06_PRONUNCIATION_IMPLEMENTED",
        [(notes("ST_S01_BASE"), lambda x: _sub_text(
            x, "<a:t>PL06: Pengurusan Operasi Pembinaan Landskap</a:t>",
            "<a:t>PL enam: Pengurusan Operasi Pembinaan Landskap</a:t>"))])
    add("C-21", "a specification popup given a visual panel",
        "SPECIFICATION_POPUPS_WITH_FORCED_VISUAL_PANEL|"
        "SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL",
        [(slide("ST_PAPAN_TANDA_CAT01"), lambda x: _sub_text(
            x, 'name="PopupPanel"', 'name="VisualPanel"'))])
    return out


def run_suite(pptx):
    try:
        return {k: ok for k, v, e, ok in QA.run(pptx)}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}


def main():
    tmp = tempfile.mkdtemp(prefix="b02_replay_v044_")
    try:
        good = run_suite(GOOD)
        out = []
        for f in build_all(tmp):
            res = run_suite(f["fixture"])
            gates = f["gate"].split("|")
            detected = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in gates)
            which = [g for g in gates if res.get(g) is False] or (
                ["<parser exception>"] if "__EXCEPTION__" in res else [])
            newly = [k for k, ok in res.items() if not ok and good.get(k, True)]
            out.append(dict(regression_id=f["regression_id"], title=f["title"],
                            designated_gate=f["gate"], detected=detected,
                            failing_designated_gates=which,
                            total_newly_failing=len(newly),
                            newly_failing_sample=sorted(newly)[:6]))
        hist = {k: sorted(g for g, ok in run_suite(p).items() if not ok)
                for k, p in PRIOR_DECKS.items()}
        return dict(good_pass=sum(1 for v in good.values() if v), good_total=len(good),
                    corrected_false_failures=sum(1 for v in good.values() if not v),
                    fixture_count=len(out),
                    detected=sum(1 for r in out if r["detected"]),
                    missed=sum(1 for r in out if not r["detected"]),
                    fixtures=out,
                    historical={k: len(v) for k, v in hist.items()},
                    historical_gates=hist)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
