# -*- coding: utf-8 -*-
"""Stage 4.2C regression replay: the twelve Stage 4.2B fixtures re-run against the v0.4.3
artifact and the v0.4.3 suite, plus six new fixtures for the rulings this stage introduced.

A mutation fixture proves GATE SENSITIVITY only. It does not prove that the corrected value
is right — that is the oracle's job. Fixtures are written to a temp directory and never
touch a committed deck.

The six new fixtures each attack one thing the latest Bariah screenshots settled:
  R-012  the removed S01 orientation sentence is put back in the spoken VO
  R-013  the S01 PL06 title reverts to the superseded "Pakej Latihan 06" long form
  R-014  the S01 Mula instruction reverts to the superseded wording
  R-015  an example card loses its per-example visual direction
  R-016  an example card is given ANOTHER example's visual direction
  R-017  the superseded Rajah 23 component-main direction is restored as active
"""
import json, os, re, shutil, sys, tempfile, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(os.path.dirname(HERE), "v0_4")
sys.path.insert(0, V4); sys.path.insert(0, HERE)
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_3 as QA
import b02_replay_v0_4_2 as PRIOR
from b02_replay_v0_4_2 import mutate, _sub_text, _drop_shape, _push_offstage

R = os.path.dirname(os.path.dirname(HERE))          # reviews/source-completion, absolute
GOOD = f"{R}/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx"
PRIOR_V4_2 = f"{R}/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_2.pptx"
PRIOR_V4_1 = f"{R}/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx"
SUPERSEDED = f"{R}/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx"


def build_all(tmp):
    """The Stage 4.2B fixtures, rebuilt from the v0.4.3 deck, plus the six new ones."""
    PRIOR.GOOD = GOOD                       # rebase the inherited fixtures onto v0.4.3
    out = PRIOR.build_all(tmp)

    idx, M = PRIOR._page_index()
    def slide(pid): return f"ppt/slides/slide{idx[pid][0]}.xml"
    def notes(pid): return f"ppt/notesSlides/notesSlide{idx[pid][0]}.xml"

    s01 = next(p for p in idx if idx[p][1]["screen_id"] == "SCR_S01")
    exs = next(p for p in idx if idx[p][1]["state_id"] == "ST_STRUKTUR_PERSISIR_AIR_EXAMPLES_BASE")
    spm = next(p for p in idx if idx[p][1]["screen_id"] == "SCR_STRUKTUR_PERSISIR_AIR_MAIN")

    def add(rid, title, gate, edits, kind="MUTATION"):
        path = os.path.join(tmp, f"{rid}.pptx")
        mutate(GOOD, path, edits)
        out.append(dict(regression_id=rid, title=title, gate=gate, fixture=path, kind=kind))

    add("R-012", "removed S01 orientation sentence restored to the spoken VO",
        "SHOT_S01_PACKAGE_NOTES_EXACT|S01_ORIENTATION_SENTENCE_REMOVED",
        [(notes(s01), lambda x: _sub_text(
            x, "<a:t>Topik 3 Bahagian 2: Komponen Landskap.</a:t>",
            "<a:t>Topik 3 Bahagian 2: Komponen Landskap.</a:t></a:r><a:r><a:t>"
            "Dalam bahagian ini, anda akan mempelajari tentang komponen landskap.</a:t>"))])

    add("R-013", "S01 PL06 title reverted to the superseded long form",
        "SHOT_S01_PACKAGE_NOTES_EXACT|S01_PL06_TITLE_SPOKEN|S01_PL06_TITLE_LONG_FORM_WITHDRAWN",
        [(notes(s01), lambda x: _sub_text(
            x, "<a:t>PL06: Pengurusan Operasi Pembinaan Landskap.</a:t>",
            "<a:t>Pakej Latihan 06: Pengurusan Operasi Pembinaan Landskap.</a:t>"))])

    add("R-014", "S01 Mula instruction reverted to the superseded wording",
        "SHOT_S01_PACKAGE_NOTES_EXACT|S01_MULA_INSTRUCTION_SPOKEN|"
        "S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN",
        [(notes(s01), lambda x: _sub_text(
            x, "Klik butang “Mula” untuk memulakan pembelajaran.",
            "Klik Mula untuk meneruskan."))])

    add("R-015", "an example card loses its per-example visual direction",
        "EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED",
        [(slide(exs), lambda x: _drop_shape(x, "VisualDir"))])

    add("R-016", "an example card is given another example's visual direction",
        "EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED",
        [(slide(exs), lambda x: _sub_text(
            x, "<a:t>[Visual: Jeti Lumut, Perak]</a:t>",
            "<a:t>[Visual: Promenade Tasik Titiwangsa, KL]</a:t>"))])

    add("R-017", "superseded Rajah 23 component-main direction restored as active",
        "SHOT_PERSISIR_ACTIVE_DIRECTION_RENDERED|SHOT_PERSISIR_SUPERSEDED_DIRECTION_NOT_ON_CANVAS|"
        "SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE",
        [(slide(spm), lambda x: _sub_text(
            x, "<a:t>[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]</a:t>",
            "<a:t>[Visual: Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, modul ms 239. "
            "Tidak dibenamkan.]</a:t>"))])
    return out


def run_suite(pptx):
    try:
        return {k: ok for k, v, e, ok in QA.run(pptx)}
    except Exception as exc:                      # a fixture may break a parser outright
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}


def main():
    tmp = tempfile.mkdtemp(prefix="b02_replay_v043_")
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
        return dict(
            good_pass=sum(1 for v in good.values() if v), good_total=len(good),
            corrected_false_failures=sum(1 for v in good.values() if not v),
            fixtures=results,
            detected=sum(1 for r in results if r["detected"]), fixture_count=len(results),
            superseded_deck_failures=sorted(
                k for k, v in run_suite(SUPERSEDED).items() if not v),
            v0_4_1_failures=sorted(k for k, v in run_suite(PRIOR_V4_1).items() if not v),
            v0_4_2_failures=sorted(k for k, v in run_suite(PRIOR_V4_2).items() if not v))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
