# -*- coding: utf-8 -*-
"""Stage 4.2D — classification-scope sensitivity fixtures.

Every fixture here mutates a record that lies OUTSIDE the classification-selected
population of the gate that owns the property, but INSIDE the true semantic population.
That is the exact blind spot CLASSIFICATION_SCOPED_POPULATION describes.

Fixtures are built in a temp directory from the committed v0.4.3 deck and discarded.
No committed artifact is mutated and the deck is never rewritten.
"""
import json, os, re, shutil, sys, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(os.path.dirname(HERE), "v0_4")
sys.path.insert(0, V4); sys.path.insert(0, HERE)
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_3 as QA
from b02_replay_v0_4_2 import mutate, _sub_text, _drop_shape

R = os.path.dirname(os.path.dirname(HERE))
GOOD = os.path.join(R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx")


def _drop_named(xml, name, nth=0):
    pat = re.compile(r"<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?</p:sp>" % re.escape(name), re.S)
    ms = list(pat.finditer(xml))
    assert len(ms) > nth, f"{name}: wanted #{nth}, found {len(ms)}"
    m = ms[nth]
    return xml[:m.start()] + xml[m.end():]


def _clone_named(xml, name, dx=0.0):
    pat = re.compile(r"(<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?</p:sp>)" % re.escape(name), re.S)
    m = pat.search(xml)
    assert m, f"shape not found for cloning: {name}"
    return xml[:m.end()] + m.group(1) + xml[m.end():]


def build_all(tmp):
    M = ADAPT.Model()
    pages = ADAPT.all_pages(M)
    idx = {p["state_id"]: i + 1 for i, p in enumerate(pages)}
    src = zipfile.ZipFile(GOOD)

    def slide(state): return f"ppt/slides/slide{idx[state]}.xml"
    def notes(state): return f"ppt/notesSlides/notesSlide{idx[state]}.xml"
    def read(part): return src.read(part).decode("utf-8")

    # a real Tick element, lifted from a page that legitimately has one
    tick_xml = re.search(r"<p:sp>(?:(?!</p:sp>).)*?name=\"Tick\".*?</p:sp>",
                         read(slide("ST_STRUKTUR_PERSISIR_AIR_ALL_VIEWED")), re.S).group(0)

    F = []

    def add(fid, group, title, blind_gate, semantic_population, edits):
        path = os.path.join(tmp, f"{fid}.pptx")
        mutate(GOOD, path, edits)
        F.append(dict(fixture_id=fid, group=group, title=title,
                      gate_whose_population_excludes_it=blind_gate,
                      true_semantic_population=semantic_population, fixture=path))

    # ---- 1. example-selection state persistence -----------------------------------
    add("F-101", "EXAMPLE_SELECTION_STATE_PERSISTENCE",
        "card visual removed from a POPUP state of a selection screen",
        "EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL (selects 4 base pages only)",
        "all 24 state pages of the 4 COMPONENT_EXAMPLE_SELECTION screens",
        [(slide("ST_STRUKTUR_PERSISIR_AIR_POPUP_01"), lambda x: _drop_named(x, "VisualDir"))])
    add("F-102", "EXAMPLE_SELECTION_STATE_PERSISTENCE",
        "card visual removed from the ALL_VIEWED state of a selection screen",
        "EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL",
        "all 24 state pages of the 4 COMPONENT_EXAMPLE_SELECTION screens",
        [(slide("ST_STRUKTUR_PERSISIR_AIR_ALL_VIEWED"), lambda x: _drop_named(x, "VisualDir"))])
    add("F-103", "EXAMPLE_SELECTION_STATE_PERSISTENCE",
        "card visual removed from the return/completion state of a second selection screen",
        "EXAMPLE_SELECTION_SCREENS_WITH_PER_EXAMPLE_VISUAL",
        "all 24 state pages of the 4 COMPONENT_EXAMPLE_SELECTION screens",
        [(slide("ST_STRUKTUR_TEDUHAN_ALL_VIEWED"), lambda x: _drop_named(x, "VisualDir", 2))])

    # ---- 2. Family S completion ticks ---------------------------------------------
    add("F-201", "FAMILY_S_COMPLETION_TICKS",
        "false tick injected into an example POPUP state",
        "TICK_IDENTITY_MISMATCHES / COMPLETION_TICKS_NOT_MATCHING_PATH",
        "every state page of a screen that owns interaction items",
        [(slide("ST_STRUKTUR_TEDUHAN_POPUP_01"),
          lambda x: x.replace("</p:spTree>", tick_xml + "</p:spTree>"))])
    add("F-202", "FAMILY_S_COMPLETION_TICKS",
        "extra tick injected into an ALL_VIEWED state where every item is already ticked",
        "TICK_IDENTITY_MISMATCHES (identity-based, may not see a duplicate)",
        "every state page of a screen that owns interaction items",
        [(slide("ST_KEMUDAHAN_AWAM_ALL_VIEWED"),
          lambda x: _clone_named(x, "Tick"))])
    add("F-203", "FAMILY_S_COMPLETION_TICKS",
        "extra tick injected into the Struktur Taman group-master return state",
        "TICK_IDENTITY_MISMATCHES",
        "every state page of the group master",
        [(slide("ST_GM_STRUKTUR_GROUP_COMPLETE"),
          lambda x: _clone_named(x, "Tick"))])

    # ---- 3. notes policy population -------------------------------------------------
    add("F-301", "NOTES_POLICY_POPULATION",
        "spoken-looking Notes inserted into a SILENT_STATE_NOTES completion state",
        "SILENT_STATES_WITH_NOTES_BLOCKS (model-derived; cannot see a package edit)",
        "every runtime state whose notes_policy is SILENT_STATE_NOTES",
        [(notes("ST_GM_STRUKTUR_GROUP_COMPLETE"),
          lambda x: _sub_text(
              x, '<a:p><a:endParaRPr lang="en-MY" dirty="0"/></a:p>',
              '<a:p><a:r><a:rPr lang="ms-MY"/><a:t>Kini anda telah melengkapkan '
              'Struktur Taman.</a:t></a:r></a:p>'))])

    # ---- 4. internal metadata denylist ---------------------------------------------
    add("F-401", "INTERNAL_METADATA_DENYLIST",
        "FAMILY_P1 injected into a DERIVED state page, not the base Perabot overview",
        "TECHNICAL_METADATA_ON_LEARNER_CANVAS",
        "every learner-canvas page, not only base pages",
        [(slide("ST_KERUSI_TAMAN_ALL_EXAMPLES_VIEWED"),
          lambda x: _sub_text(x, "<a:t>Kerusi Kayu Keras</a:t>",
                              "<a:t>Kerusi Kayu Keras FAMILY_P1</a:t>"))])

    # ---- 5. visual subtype persistence ----------------------------------------------
    add("F-501", "VISUAL_SUBTYPE_PERSISTENCE",
        "example-card visual removed from a popup-state rendering of a selection screen",
        "EXAMPLE_SELECTION_SCREEN_LEVEL_INVENTED_DIRECTION / REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL",
        "all 24 state pages of the 4 selection screens",
        [(slide("ST_KEMUDAHAN_AWAM_POPUP_02"), lambda x: _drop_named(x, "VisualDir", 1))])
    add("F-502", "VISUAL_SUBTYPE_PERSISTENCE",
        "example-card visual removed from a state whose review_page_role differs from base",
        "REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL (selects REQUIRED-classified pages only)",
        "all state pages of a screen whose base page is REQUIRED",
        [(slide("ST_WATER_FEATURE_ALL_VIEWED"), lambda x: _drop_named(x, "VisualDir"))])

    # ---- 6. quiz review overlay -------------------------------------------------------
    add("F-601", "QUIZ_REVIEW_OVERLAY",
        "one answer removed from the Semak Jawapan review state",
        "QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY / ANSWER_KEYS_EVALUATED "
        "(select AnswerKeyBody on the 5 question pages only)",
        "every page carrying a question-review obligation, including STATE_QUIZ_REVIEW",
        [(slide("ST_KUIZ_REVIEW"), lambda x: _drop_named(x, "RvA", 2))])
    return F


def run_suite(pptx):
    try:
        return {k: ok for k, v, e, ok in QA.run(pptx)}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}


def main():
    tmp = tempfile.mkdtemp(prefix="b02_clsscope_")
    try:
        good = run_suite(GOOD)
        out = []
        for f in build_all(tmp):
            res = run_suite(f["fixture"])
            newly = sorted(k for k, ok in res.items() if not ok and good.get(k, True))
            out.append(dict(fixture_id=f["fixture_id"], group=f["group"], title=f["title"],
                            gate_whose_population_excludes_it=f["gate_whose_population_excludes_it"],
                            true_semantic_population=f["true_semantic_population"],
                            detected=bool(newly) or "__EXCEPTION__" in res,
                            detecting_gates=newly))
        return dict(
            harness="b02_classification_scope_fixtures_v0_4_3",
            deck=os.path.basename(GOOD),
            CLASSIFICATION_SCOPE_FIXTURES=len(out),
            FIXTURES_DETECTED=sum(1 for r in out if r["detected"]),
            FIXTURES_MISSED=sum(1 for r in out if not r["detected"]),
            CORRECTED_DECK_FALSE_FAILURES=sum(1 for v in good.values() if not v),
            fixtures=out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
