# -*- coding: utf-8 -*-
"""Stage 4.2E-C regression replay.

The 39 Stage 4.2E-B fixtures re-run against the v0.4.4.1 artifact and the v0.4.4.1 suite,
plus twelve new ones for what this stage changed.

A mutation fixture proves GATE SENSITIVITY only. It never proves the corrected value is
right — that is the oracle's and the frozen contract's job. Fixtures are written to a temp
directory and never touch a committed deck.

  M-01  a panel version line reverted to v0.4
  M-02  a panel status token reverted to REVIEW_READY
  M-03  PENDING_TARGETED_CONFIRMATION reinserted on one page
  M-04  a component-main visual requirement set back to CONDITIONAL
  M-05  a component-main mapping status set back to PENDING_HUMAN
  M-06  PROVISIONAL_VISUAL_PROPOSAL reinserted on a component main
  M-07  a component main's subject provenance promoted to BARIAH_DIRECT on the page
  M-08  the registered title-placeholder exemption removed from the registry
  M-09  an ordinary shape placed at the placeholder's exact negative coordinates
  M-10  an ordinary shape renamed "Title 1" without the title placeholder type
  M-11  a registered exemption widened by moving the placeholder it covers
  M-12  a subject promoted to BARIAH_DIRECT in the frozen mapping contract itself
"""
import copy, json, os, re, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(os.path.dirname(HERE), "v0_4")
sys.path.insert(0, V4); sys.path.insert(0, HERE)
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_4_1 as QA
import b02_artifact_identity_v0_4_4_1 as IDENT
import b02_geometry_exemptions_v0_4_4_1 as GEX
import b02_overview_mapping_v0_4_4 as OV
import b02_replay_v0_4_2 as P42
import b02_replay_v0_4_3 as P43
import b02_replay_v0_4_4 as P44
from b02_replay_v0_4_2 import mutate, _sub_text

R = os.path.dirname(os.path.dirname(HERE))
GOOD = os.path.join(R, IDENT.DECK_FILENAME)
PRIOR_DECKS = dict(P44.PRIOR_DECKS)
PRIOR_DECKS["v0_4_4"] = os.path.join(
    R, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4.pptx")

# An ordinary text box — no <p:ph> — at the title placeholder's exact geometry.
OFFSTAGE_SP = (
    '<p:sp><p:nvSpPr><p:cNvPr id="950" name="%s"/><p:cNvSpPr txBox="1"/><p:nvPr/>'
    '</p:nvSpPr><p:spPr><a:xfrm><a:off x="0" y="-577078"/>'
    '<a:ext cx="12191970" cy="523220"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/>'
    '</a:prstGeom></p:spPr><p:txBody><a:bodyPr wrap="square"/><a:lstStyle/><a:p><a:r>'
    '<a:rPr lang="ms-MY" sz="900"/><a:t>nota dalaman</a:t></a:r></a:p></p:txBody></p:sp>')


def _inject(xml, sp):
    i = xml.rindex("</p:spTree>")
    return xml[:i] + sp + xml[i:]


def build_all(tmp):
    for mod in (P42, P43, P44):
        mod.GOOD = GOOD
    out = P44.build_all(tmp)                    # 39 fixtures, rebased onto v0.4.4.1

    M = ADAPT.Model(); pages = ADAPT.all_pages(M)
    idx = {p["state_id"]: i + 1 for i, p in enumerate(pages)}
    def slide(s): return f"ppt/slides/slide{idx[s]}.xml"

    PT = "ST_PAPAN_TANDA_MAIN_BASE"
    S01 = "ST_S01_BASE" if "ST_S01_BASE" in idx else pages[0]["state_id"]

    def add(fid, title, gate, edits, kind="MUTATION"):
        path = os.path.join(tmp, f"{fid}.pptx")
        mutate(GOOD, path, edits)
        out.append(dict(regression_id=fid, title=title, gate=gate, fixture=path, kind=kind))

    def code(fid, title, gate, patch):
        out.append(dict(regression_id=fid, title=title, gate=gate, fixture=GOOD,
                        kind="REGISTRY_MUTATION", patch=patch))

    # ---------------- identity and release status ----------------
    add("M-01", "a panel version line reverted to v0.4",
        "PANEL_VERSION_MANIFEST_MISMATCHES|SUPERSEDED_VERSION_LINES_IN_PANEL|"
        "PANEL_VERSION_EQUALS_RUN_MANIFEST_VERSION|ACTIVE_PANEL_VERSION",
        [(slide(S01), lambda x: _sub_text(
            x, f"<a:t>{IDENT.VERSION_LINE}</a:t>",
            "<a:t>K5 PL06 T03 B02 — PAPAN CERITA v0.4</a:t>"))])

    add("M-02", "a panel status token reverted to REVIEW_READY",
        "STALE_RELEASE_TOKENS|PANEL_STATUS_MANIFEST_MISMATCHES|"
        "PANEL_STATUS_EQUALS_ACTIVE_PACKAGE_STATUS|STALE_STATUS_TOKEN_REVIEW_READY",
        [(slide(S01), lambda x: _sub_text(x, "REVIEW_CANDIDATE", "REVIEW_READY"))])

    add("M-03", "PENDING_TARGETED_CONFIRMATION reinserted on one page",
        "STALE_RELEASE_TOKENS_ANYWHERE_IN_PANEL|"
        "STALE_STATUS_TOKEN_PENDING_TARGETED_CONFIRMATION",
        [(slide(S01), lambda x: _sub_text(
            x, "<a:t>NOT_FOR_MMD_BUILD</a:t>",
            "<a:t>NOT_FOR_MMD_BUILD · PENDING_TARGETED_CONFIRMATION</a:t>"))])

    # ---------------- component-main visual governance ----------------
    add("M-04", "a component-main visual requirement set back to CONDITIONAL",
        "COMPONENT_MAIN_VISUAL_REQUIREMENT_REQUIRED|"
        "COMPONENT_MAIN_ACTIVE_VISUAL_GOVERNANCE_CURRENT|"
        "COMPONENT_MAIN_STALE_GOVERNANCE_STRINGS_IN_VISUAL_BLOCK",
        [(slide(PT), lambda x: _sub_text(
            x, "<a:t>  keperluan visual: REQUIRED</a:t>",
            "<a:t>  keperluan visual: CONDITIONAL</a:t>"))])

    add("M-05", "a component-main mapping status set back to PENDING_HUMAN",
        "COMPONENT_MAIN_MAPPING_STATUS_RESOLVED|"
        "COMPONENT_MAIN_ACTIVE_VISUAL_GOVERNANCE_CURRENT|"
        "COMPONENT_MAIN_STALE_GOVERNANCE_STRINGS_IN_VISUAL_BLOCK",
        [(slide(PT), lambda x: _sub_text(
            x, "<a:t>  status pemetaan: RESOLVED</a:t>",
            "<a:t>  status pemetaan: PENDING_HUMAN</a:t>"))])

    add("M-06", "PROVISIONAL_VISUAL_PROPOSAL reinserted on a component main",
        "COMPONENT_MAIN_PROVISIONAL_VISUAL_PROPOSALS|"
        "COMPONENT_MAIN_ACTIVE_VISUAL_GOVERNANCE_CURRENT",
        [(slide(PT), lambda x: _sub_text(
            x, "<a:t>  rawatan: SOURCE_BOUND_OVERVIEW</a:t>",
            "<a:t>  rawatan: SOURCE_BOUND_OVERVIEW</a:t></a:r></a:p>"
            "<a:p><a:r><a:rPr lang=\"ms-MY\" sz=\"900\"/>"
            "<a:t>  kelas cadangan: PROVISIONAL_VISUAL_PROPOSAL</a:t>"))])

    add("M-07", "a component main's subject provenance promoted to BARIAH_DIRECT on the page",
        "COMPONENT_MAIN_SUBJECT_PROVENANCE_ON_PAGE",
        [(slide(PT), lambda x: _sub_text(
            x, "<a:t>  sumber subjek: MODULE_SOURCE_ATTESTED 2</a:t>",
            "<a:t>  sumber subjek: BARIAH_DIRECT 2</a:t>"))])

    # ---------------- geometry exemption ----------------
    def _without_gex001():
        return [e for e in GEX.OFF_CANVAS_EXEMPTIONS if e["exemption_id"] != "GEX-001"]

    code("M-08", "the registered title-placeholder exemption removed from the registry",
         "OFF_CANVAS_PLACEHOLDER_EXEMPTION_REGISTERED|SHAPES_BEYOND_TOP_EDGE|"
         "UNREGISTERED_OFF_CANVAS_EXEMPTIONS|GEOMETRY_EXEMPTION_REGISTRY_MATCHES_CODE",
         _without_gex001)

    add("M-09", "an ordinary shape placed at the placeholder's exact negative coordinates",
        "SHAPES_BEYOND_TOP_EDGE|UNREGISTERED_OFF_CANVAS_EXEMPTIONS|"
        "ORDINARY_OFF_CANVAS_SHAPES_ALLOWED",
        [(slide(S01), lambda x: _inject(x, OFFSTAGE_SP % "NotaDalaman"))])

    add("M-10", "an ordinary shape renamed \"Title 1\" without the title placeholder type",
        "SHAPES_BEYOND_TOP_EDGE|UNREGISTERED_OFF_CANVAS_EXEMPTIONS|"
        "ORDINARY_OFF_CANVAS_SHAPES_ALLOWED|TITLE_PLACEHOLDER_IS_A_REAL_PLACEHOLDER",
        [(slide(S01), lambda x: _inject(x, OFFSTAGE_SP % "Title 1"))])

    add("M-11", "the registered placeholder moved, so the exemption no longer covers it",
        "SHAPES_BEYOND_TOP_EDGE|UNREGISTERED_OFF_CANVAS_EXEMPTIONS|"
        "EXEMPTED_SHAPES_EVALUATED",
        [(slide(S01), lambda x: x.replace('<a:off x="0" y="-577078"/>',
                                          '<a:off x="0" y="-800000"/>', 1))])

    # ---------------- frozen contract ----------------
    def _promote_subject():
        m = copy.deepcopy(OV.mapping())
        m["components"][1]["subjects"][0]["provenance"] = "BARIAH_DIRECT"
        return m

    out.append(dict(regression_id="M-12",
                    title="a subject promoted to BARIAH_DIRECT in the frozen mapping contract",
                    gate="UNAUTHORISED_SUBJECT_AUTHORITY_PROMOTIONS",
                    fixture=GOOD, kind="CONTRACT_MUTATION", patch=_promote_subject))
    return out


def run_suite(pptx):
    try:
        return {k: ok for k, v, e, ok in QA.run(pptx)}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}


def run_fixture(f):
    """A fixture may live in the package, in the exemption registry or in the frozen
    mapping contract. Whichever it is, the patch is reverted before the next one runs."""
    if f["kind"] == "REGISTRY_MUTATION":
        keep = GEX.OFF_CANVAS_EXEMPTIONS
        try:
            GEX.OFF_CANVAS_EXEMPTIONS = f["patch"]()
            return run_suite(f["fixture"])
        finally:
            GEX.OFF_CANVAS_EXEMPTIONS = keep
    if f["kind"] == "CONTRACT_MUTATION":
        keep = OV._M
        try:
            OV._M = f["patch"]()
            return run_suite(f["fixture"])
        finally:
            OV._M = keep
    return run_suite(f["fixture"])


def main():
    tmp = tempfile.mkdtemp(prefix="b02_replay_v0441_")
    try:
        good = run_suite(GOOD)
        out = []
        for f in build_all(tmp):
            res = run_fixture(f)
            gates = f["gate"].split("|")
            detected = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in gates)
            which = [g for g in gates if res.get(g) is False] or (
                ["<parser exception>"] if "__EXCEPTION__" in res else [])
            newly = [k for k, ok in res.items() if not ok and good.get(k, True)]
            out.append(dict(regression_id=f["regression_id"], title=f["title"],
                            kind=f["kind"], designated_gate=f["gate"], detected=detected,
                            failing_designated_gates=which,
                            total_newly_failing=len(newly),
                            newly_failing_sample=sorted(newly)[:6]))
        hist = {k: sorted(g for g, ok in run_suite(p).items() if not ok)
                for k, p in PRIOR_DECKS.items()}
        return dict(good_pass=sum(1 for v in good.values() if v), good_total=len(good),
                    corrected_false_failures=sum(1 for v in good.values() if not v),
                    fixture_count=len(out),
                    detected=sum(1 for r in out if r["detected"]),
                    missed=sorted(r["regression_id"] for r in out if not r["detected"]),
                    fixtures=out,
                    historical={k: len(v) for k, v in hist.items()},
                    historical_gates=hist)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
