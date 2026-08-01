# -*- coding: utf-8 -*-
"""Regression replay: known-bad artifacts and temporary mutation fixtures.

A mutation fixture proves GATE SENSITIVITY only. It does not prove that the corrected
value is right — that is the oracle's job, and where no frozen oracle exists the record
says so. Fixtures are written to a temp directory and never touch a committed deck.
"""
import json, os, re, shutil, sys, tempfile, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(os.path.dirname(HERE), "v0_4")
sys.path.insert(0, V4); sys.path.insert(0, os.path.dirname(HERE))
import b02_model_adapter_v0_4 as ADAPT
import b02_regression_qa_v0_4_1 as QA

R = "reviews/source-completion"
GOOD = f"{R}/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx"
SUPERSEDED = f"{R}/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx"


def _page_index():
    M = ADAPT.Model()
    return {p["id"]: (i + 1, p) for i, p in enumerate(ADAPT.all_pages(M))}, M


def mutate(src, out, edits):
    """Copy a package, applying (part, fn) edits. Never modifies the source."""
    zin = zipfile.ZipFile(src)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zin.infolist():
            data = zin.read(it.filename)
            for part, fn in edits:
                if it.filename == part:
                    data = fn(data.decode("utf-8")).encode("utf-8")
            zo.writestr(it, data)
    return out


# ---------------------------------------------------------------- mutations
def _sub_text(xml, old, new, count=1):
    assert old in xml, f"mutation anchor not found: {old[:60]!r}"
    return xml.replace(old, new, count)


def _drop_shape(xml, name, count=1):
    """Remove the first <p:sp> whose cNvPr name matches."""
    pat = re.compile(r"<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?</p:sp>" % re.escape(name), re.S)
    m = pat.search(xml)
    assert m, f"shape not found for removal: {name}"
    return xml[:m.start()] + xml[m.end():]


def _clone_shape(xml, name):
    pat = re.compile(r"(<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?</p:sp>)" % re.escape(name), re.S)
    m = pat.search(xml)
    assert m, f"shape not found for cloning: {name}"
    return xml[:m.end()] + m.group(1) + xml[m.end():]


def _push_offstage(xml, name):
    """Move the first named shape below the bottom of the 7.5in stage."""
    pat = re.compile(r"(<p:sp>(?:(?!</p:sp>).)*?name=\"%s\".*?<a:off x=\"(\d+)\" y=\")(\d+)(\")"
                     % re.escape(name), re.S)
    m = pat.search(xml)
    assert m, f"shape not found for off-stage move: {name}"
    return xml[:m.start(3)] + "7000560" + xml[m.end(3):]


FIXTURES = []


def fixture(rid, title, gate, part_fn, kind="MUTATION"):
    FIXTURES.append(dict(regression_id=rid, title=title, gate=gate, build=part_fn, kind=kind))


def build_all(tmp):
    idx, M = _page_index()
    def slide(pid): return f"ppt/slides/slide{idx[pid][0]}.xml"
    def notes(pid): return f"ppt/notesSlides/notesSlide{idx[pid][0]}.xml"
    # locate representative pages by model, not by guessing numbers
    prom = next(p for p in idx if idx[p][1]["state_id"] == "ST_STRUKTUR_PERSISIR_AIR_POPUP_01")
    s01 = next(p for p in idx if idx[p][1]["screen_id"] == "SCR_S01")
    perab = next(p for p in idx if idx[p][1]["screen_id"] == "SCR_PERABOT_OVERVIEW")
    df6 = next(p for p in idx if idx[p][1]["state_id"] == "ST_DRINKING_FOUNTAIN_EX01_BASE")
    q1 = next(p for p in idx if idx[p][1]["state_id"] == "ST_KUIZ_Q1")
    tam = next(p for p in idx if idx[p][1]["screen_id"] == "SCR_TAMAT")
    gm = next(p for p in idx if idx[p][1]["state_id"] == "ST_GM_STRUKTUR_BASE")
    spec = next(p for p in idx if idx[p][1]["state_id"] == "ST_PAPAN_TANDA_CAT01")
    exs = next(p for p in idx if idx[p][1]["state_id"] == "ST_STRUKTUR_PERSISIR_AIR_EXAMPLES_BASE")

    out = []

    def add(rid, title, gate, edits, kind="MUTATION"):
        path = os.path.join(tmp, f"{rid}.pptx")
        mutate(GOOD, path, edits)
        out.append(dict(regression_id=rid, title=title, gate=gate, fixture=path, kind=kind))

    add("R-001", "Promenade direction replaced by the generic fallback",
        "GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES",
        [(slide(prom), lambda x: _sub_text(
            x, "Promenade Tasik Titiwangsa, KL",
            "Arahan visual untuk Promenade — spesifikasi teks sahaja, modul ms 238."))])
    add("R-002", "FAMILY_P1 injected into the learner canvas",
        "TECHNICAL_METADATA_ON_LEARNER_CANVAS",
        [(slide(perab), lambda x: _sub_text(x, "Kerusi Taman", "Kerusi Taman FAMILY_P1"))])
    add("R-003", "italic property stripped from a Notes run",
        "NOTES_GLOSSARY_ITALIC_MISSES",
        [(notes(perab), lambda x: x.replace(' i="1"', "", 1))])
    add("R-004", "sixth card removed from a six-item grid",
        "CARDS_DROPPED_OR_INVENTED",
        [(slide(df6), lambda x: _drop_shape(x, "ItemCard"))])
    add("R-005", "one quiz answer key removed",
        "QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY",
        [(slide(q1), lambda x: _drop_shape(_drop_shape(x, "AnswerKeyBody"), "AnswerKeyBox"))])
    add("R-006", "superseded Tamat close-window copy restored",
        "TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT",
        [(slide(tam), lambda x: _sub_text(x, "Teruskan pembelajaran ke bahagian seterusnya.",
                                          "Tutup tetingkap pelajaran untuk keluar."))])
    add("R-007", "confirmed screen-level Klik instruction removed from spoken VO",
        "ACTION_INSTRUCTIONS_MISSING_FROM_NOTES",
        [(notes(exs), lambda x: _sub_text(
            x, "Klik pada setiap contoh untuk penjelasan lanjut.", "", 1))])
    # R-008 injects a real Tick shape onto a page the path has not completed. The first
    # attempt cloned an ItemCard instead and was NOT detected — that miss is what exposed
    # the missing universal tick-identity gate. See the replay report.
    av = next(p for p in idx if idx[p][1]["state_id"] == "ST_STRUKTUR_PERSISIR_AIR_ALL_VIEWED")
    tickxml = re.search(r"<p:sp>(?:(?!</p:sp>).)*?name=\"Tick\".*?</p:sp>",
                        zipfile.ZipFile(GOOD).read(
                            "ppt/slides/slide%d.xml" % idx[av][0]).decode(), re.S).group(0)
    add("R-008", "uncompleted sibling marked as ticked (Family S base page)",
        "COMPLETION_TICKS_NOT_MATCHING_PATH",
        [(slide(exs), lambda x: x.replace("</p:spTree>", tickxml + "</p:spTree>"))])
    add("R-008b", "uncompleted component marked as ticked (Struktur group master)",
        "COMPLETION_TICKS_NOT_MATCHING_PATH",
        [(slide(gm), lambda x: x.replace("</p:spTree>", tickxml + "</p:spTree>"))])
    add("R-009", "forced visual panel added to a specification popup",
        "SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL",
        [(slide(spec), lambda x: _sub_text(x, 'name="PopupPanel"', 'name="VisualPanel"'))])
    add("R-010", "S01 duplicated standalone component title re-introduced",
        "S01_DUPLICATE_STANDALONE_COMPONENT_TITLE",
        [(slide(s01), lambda x: _sub_text(
            x, "<a:t>KURSUS KERJA BANGUNAN – PEMBINAAN LANDSKAP LUAR</a:t>",
            "<a:t>Komponen Landskap</a:t>"))])
    add("R-011", "canvas object moved below the stage boundary",
        "CANVAS_SHAPES_OUTSIDE_STAGE",
        [(slide(gm), lambda x: _push_offstage(x, "ItemCard"))])
    return out


def run_suite(pptx):
    try:
        return {k: ok for k, v, e, ok in QA.run(pptx)}
    except Exception as exc:                      # a fixture may break a parser outright
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}


def main():
    tmp = tempfile.mkdtemp(prefix="b02_replay_")
    try:
        good = run_suite(GOOD)
        results = []
        for f in build_all(tmp):
            res = run_suite(f["fixture"])
            gates = f["gate"].split("|")
            detected = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in gates)
            which = [g for g in gates if res.get(g) is False] or (
                ["<parser exception>"] if "__EXCEPTION__" in res else [])
            newly = [k for k, ok in res.items() if not ok and good.get(k, True)]
            results.append(dict(regression_id=f["regression_id"], title=f["title"],
                                designated_gate=f["gate"], kind=f["kind"],
                                detected=detected, failing_designated_gates=which,
                                total_newly_failing=len(newly),
                                newly_failing_sample=sorted(newly)[:6]))
        superseded = run_suite(SUPERSEDED)
        return dict(good_pass=sum(1 for v in good.values() if v), good_total=len(good),
                    corrected_false_failures=sum(1 for v in good.values() if not v),
                    superseded_deck_failures=sorted(k for k, v in superseded.items() if not v),
                    fixtures=results)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
