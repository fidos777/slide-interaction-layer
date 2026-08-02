# -*- coding: utf-8 -*-
"""Negative mutations for the T04 extraction gates.

Two kinds:

  DATA_MUTATION       patches the loaded extract or analysis layer in memory and re-runs the
                      suite. Permanent — runs whenever the repository is checked out.

  EXTRACTION_MUTATION calls the extractor itself with a corrupted anchor or index and
                      requires it to FAIL CLOSED. These need the DOCX, which is deleted at
                      the end of the stage, so they run once at extraction time and are
                      reported as SKIPPED_NO_DOCX afterwards. That is disclosed rather than
                      quietly dropped: a skipped fixture is not a passing one.

    python3 t04_mutations_v1.py [path-to-docx]
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_data_v1 as D
import t04_qa_v1 as QA
import t04_extract_v1 as EXTRACT

DOCX = sys.argv[1] if len(sys.argv) > 1 else None


def _rows(fn):
    def apply():
        r = copy.deepcopy(D.ROWS)
        fn(r)
        return dict(ROWS=r, BY_ID={x["row_id"]: x for x in r})
    return apply


def _totals(**kw):
    def apply():
        t = dict(D.TOTALS); t.update(kw); return dict(TOTALS=t)
    return apply


DATA_FIXTURES = [
    dict(fid="X-01", title="one T04 paragraph is removed from the extract",
         gates=["EVERY_ELEMENT_ACCOUNTED", "CONTENT_ROWS", "SEQUENCE_IS_CONTIGUOUS",
                "CONTENT_TYPE_TOTALS_SUM"],
         patch=_rows(lambda r: r.pop(50))),
    dict(fid="X-02", title="a T05 paragraph is pulled inside the boundary",
         gates=["T05_CONTENT_EXCLUDED", "CONTENT_ROWS"],
         patch=_rows(lambda r: r.append(dict(
             r[10], row_id="T04-ROW-101", sequence=101, module_page=284,
             raw_source_text="Pengurusan Kualiti Projek dalam konteks pembinaan landskap "
                             "adalah pendekatan sistematik. Project Quality Plan (PQP).",
             controlled_display_text="Pengurusan Kualiti Projek …")))),
    dict(fid="X-03", title="a row is attributed to a page outside 276-283",
         gates=["ROWS_OUTSIDE_THE_PAGE_RANGE"],
         patch=_rows(lambda r: r[30].update(module_page=290))),
    dict(fid="X-04", title="a source row is duplicated",
         gates=["DUPLICATE_ROW_IDS", "SEQUENCE_IS_CONTIGUOUS", "CONTENT_ROWS"],
         patch=_rows(lambda r: r.append(copy.deepcopy(r[20])))),
    dict(fid="X-05", title="an asset ID is duplicated",
         gates=["DUPLICATE_ASSET_IDS", "ASSET_INVENTORY_MATCHES_TOTAL"],
         patch=lambda: dict(ASSETS=D.ASSETS + [copy.deepcopy(D.ASSETS[0])])),
    dict(fid="X-06", title="a Rumusan statement is invented into a controlled row",
         gates=["INVENTED_RUMUSAN", "INVENTED_QUIZ_TEXT"],
         patch=_rows(lambda r: r[60].update(
             controlled_display_text="Rumusan: penjagaan landskap lembut dan kejur "
                                     "memerlukan jadual penyelenggaraan yang sistematik."))),
    dict(fid="X-07", title="an answer key is invented into a controlled row",
         gates=["INVENTED_QUIZ_TEXT"],
         patch=_rows(lambda r: r[70].update(
             controlled_display_text="Jawapan: B — kawalan biologi."))),
    dict(fid="X-08", title="quiz options are invented into a controlled row",
         gates=["INVENTED_QUIZ_OPTION_MARKERS"],
         patch=_rows(lambda r: r[71].update(
             controlled_display_text="a) Siram   b) Baja   c) Racun"))),
    dict(fid="X-09", title="the Rumusan coverage status is upgraded to available",
         gates=["RUMUSAN_STATUS"],
         patch=lambda: dict(QUIZ_COVERAGE=[
             dict(q, status="SOURCE_AVAILABLE") if q["item"] == "Rumusan" else q
             for q in copy.deepcopy(D.QUIZ_COVERAGE)])),
    dict(fid="X-10", title="the 4 MCQ + 1 MR composition is assumed for T04",
         gates=["QUIZ_COMPOSITION_NOT_ASSUMED"],
         patch=lambda: dict(QUIZ_COVERAGE=[
             dict(q, status="SOURCE_AVAILABLE")
             if q["item"] == "4 MCQ + 1 MR composition" else q
             for q in copy.deepcopy(D.QUIZ_COVERAGE)])),
    dict(fid="X-11", title="the 60 percent pass threshold is assumed for T04",
         gates=["PASS_THRESHOLD_NOT_ASSUMED"],
         patch=lambda: dict(QUIZ_COVERAGE=[
             dict(q, status="SOURCE_AVAILABLE")
             if q["item"] == "60 percent pass threshold" else q
             for q in copy.deepcopy(D.QUIZ_COVERAGE)])),
    dict(fid="X-12", title="a source row is promoted to BARIAH_DIRECT",
         gates=["ALL_ROWS_MODULE_SOURCE_ATTESTED",
                "SOURCE_DERIVED_PROMOTED_TO_BARIAH_DIRECT"],
         patch=_rows(lambda r: r[15].update(authority_class="BARIAH_DIRECT_SCREENSHOT"))),
    dict(fid="X-13", title="the diagram's subjects are replaced with invented ones",
         gates=["INVENTED_VISUAL_SUBJECTS", "DIAGRAM_NODE_COUNT"],
         patch=lambda: dict(ASSETS=[dict(D.ASSETS[0], source_subject_nodes=[], node_count=6)])),
    dict(fid="X-14", title="an asset subject is labelled BARIAH_DIRECT",
         gates=["ASSET_SUBJECTS_NOT_BARIAH_DIRECT", "ASSET_SOURCE_BOUND_STATUS_VALID"],
         patch=lambda: dict(ASSETS=[dict(D.ASSETS[0],
                                         source_bound_status="BARIAH_DIRECT_CONFIRMED")])),
    dict(fid="X-15", title="an interaction candidate is promoted with no source rows",
         gates=["CANDIDATE_WITH_NO_ROWS_IS_PENDING_HUMAN"],
         patch=lambda: dict(SCREEN_CANDIDATES=[
             dict(c, candidate="EXAMPLE_SELECTION")
             if c["candidate_id"] == "T04-SC-06" else c
             for c in copy.deepcopy(D.SCREEN_CANDIDATES)])),
    dict(fid="X-16", title="a candidate cites a row that is not in the extract",
         gates=["CANDIDATE_ROWS_NOT_IN_EXTRACT"],
         patch=lambda: dict(SCREEN_CANDIDATES=[
             dict(c, source_rows=c["source_rows"] + ["T04-ROW-999"])
             if c["candidate_id"] == "T04-SC-02" else c
             for c in copy.deepcopy(D.SCREEN_CANDIDATES)])),
    dict(fid="X-17", title="a B02 execution family is propagated into a candidate",
         gates=["B02_PROPAGATION_FAMILY_S"],
         patch=lambda: dict(SCREEN_CANDIDATES=[
             dict(c, reusable_capability="FAMILY_S selection screen, reused wholesale")
             if c["candidate_id"] == "T04-SC-02" else c
             for c in copy.deepcopy(D.SCREEN_CANDIDATES)])),
    dict(fid="X-18", title="a B02 component name enters the analysis layer",
         gates=["B02_COMPONENTS_IN_ANALYSIS"],
         patch=lambda: dict(SCREEN_CANDIDATES=[
             dict(c, reason="treat as per Struktur Teduhan in B02")
             if c["candidate_id"] == "T04-SC-05" else c
             for c in copy.deepcopy(D.SCREEN_CANDIDATES)])),
    dict(fid="X-19", title="the misspelled heading is silently corrected in the raw field",
         gates=["H1_RAW_TEXT_PRESERVED", "FIRST_ROW_IS_THE_START_ANCHOR",
                "RAW_AND_GOVERNED_HELD_SEPARATELY"],
         patch=_rows(lambda r: r[0].update(
             raw_source_text="PENJAGAAN DAN PENYELENGGARAAN"))),
    dict(fid="X-20", title="a row is rewritten without recording a normalisation",
         gates=["UNSUPPORTED_NORMALISATION"],
         patch=_rows(lambda r: r[25].update(
             controlled_display_text=r[25]["raw_source_text"] + " (dikemas kini)"))),
    dict(fid="X-21", title="the normalisation status is downgraded to a silent fix",
         gates=["NORMALISATION_STATUS"],
         patch=lambda: dict(BOUNDARY=dict(D.BOUNDARY,
                                          normalisation_status="CORRECTED"))),
    dict(fid="X-22", title="the table total disagrees with the table inventory",
         gates=["TABLE_INVENTORY_MATCHES_TOTAL", "CONTENT_TYPE_TOTALS_SUM"],
         patch=_totals(tables=2)),
    dict(fid="X-23", title="the list inventory disagrees with the numbered-paragraph total",
         gates=["LIST_INVENTORY_MATCHES_TOTAL"],
         patch=lambda: dict(LISTS=copy.deepcopy(D.LISTS)[:-1])),
    dict(fid="X-24", title="a raster image is claimed where none exists",
         gates=["RASTER_IMAGES"], patch=_totals(raster_images=3)),
    dict(fid="X-25", title="the READY verdict is claimed while unit blockers are open",
         gates=["READY_VERDICT_WITH_BLOCKING_GAPS"],
         patch=lambda: dict(VERDICT="T04_SOURCE_COMPLETE_READY_FOR_STORYBOARD_MODEL")),
    dict(fid="X-26", title="a forbidden verdict is claimed",
         gates=["VERDICT_IS_ALLOWED", "FORBIDDEN_VERDICT_CLAIMED"],
         patch=lambda: dict(VERDICT="T04_READY_FOR_MMD")),
    dict(fid="X-27", title="the DOCX identity record is altered",
         gates=["DOCX_BYTES", "DOCX_IDENTITY_RECORDED"],
         patch=lambda: dict(PROBE=dict(D.PROBE, bytes=16832860,
                                       identity_matches_expected=False))),
    dict(fid="X-28", title="the recorded start paragraph is changed",
         gates=["START_PARAGRAPH_IS_5220", "START_MATCHES_FROZEN_MAP", "PARAGRAPH_SPAN"],
         patch=lambda: dict(PROBE=dict(
             D.PROBE, paragraph_enumeration=dict(D.PROBE["paragraph_enumeration"],
                                                 start_index=5219, span=141,
                                                 start_matches_expected=False)))),
    dict(fid="X-29", title="the recorded stop paragraph is changed",
         gates=["STOP_BEFORE_PARAGRAPH_5360", "STOP_MATCHES_FROZEN_MAP", "PARAGRAPH_SPAN"],
         patch=lambda: dict(PROBE=dict(
             D.PROBE, paragraph_enumeration=dict(D.PROBE["paragraph_enumeration"],
                                                 stop_index=5370, span=150,
                                                 stop_matches_expected=False)))),
    dict(fid="X-30", title="the canonical spelling is recorded as a usable body anchor",
         gates=["CANONICAL_ONLY_ANCHOR_NOT_USED"],
         patch=lambda: dict(PROBE=dict(
             D.PROBE, anchor_search=dict(D.PROBE["anchor_search"],
                                         governed_label_body_hits=[5220])))),
]

# ---- extraction-time fixtures: the extractor itself must fail closed ----
EXTRACTION_FIXTURES = [
    dict(fid="E-01", title="extraction anchors on the canonical spelling only",
         expect="ExtractionError",
         call=lambda p: EXTRACT.extract(p, raw_start_anchor="PENJAGAAN DAN PENYELENGGARAAN")),
    dict(fid="E-02", title="the expected start paragraph is changed",
         expect="ExtractionError",
         call=lambda p: EXTRACT.extract(p, expected_start=5219)),
    dict(fid="E-03", title="the expected stop paragraph is changed",
         expect="ExtractionError",
         call=lambda p: EXTRACT.extract(p, expected_stop=5370)),
    dict(fid="E-04", title="the stop anchor is changed to a heading in another Topik",
         expect="ExtractionError",
         call=lambda p: EXTRACT.extract(p, raw_stop_anchor="DEMOBILISASI")),
]


def run_data(f):
    patch = f["patch"]()
    saved = {k: getattr(D, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(D, k, v)
        return {r["gate_id"]: r["ok"] for r in QA.run()}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(D, k, v)


def main():
    good = {r["gate_id"]: r["ok"] for r in QA.run()}
    out = []
    for f in DATA_FIXTURES:
        res = run_data(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], kind="DATA_MUTATION", title=f["title"],
                        designated_gates=f["gates"], detected=det, fired=fired))
    for f in EXTRACTION_FIXTURES:
        if not DOCX or not os.path.exists(DOCX):
            out.append(dict(fixture_id=f["fid"], kind="EXTRACTION_MUTATION", title=f["title"],
                            designated_gates=["<extractor fail-closed>"], detected=None,
                            fired=["SKIPPED_NO_DOCX"]))
            continue
        try:
            f["call"](DOCX)
            det, fired = False, ["EXTRACTOR_DID_NOT_FAIL"]
        except EXTRACT.ExtractionError as exc:
            det, fired = True, [f"ExtractionError: {str(exc)[:80]}"]
        except Exception as exc:
            det, fired = True, [f"{type(exc).__name__}: {str(exc)[:80]}"]
        out.append(dict(fixture_id=f["fid"], kind="EXTRACTION_MUTATION", title=f["title"],
                        designated_gates=["<extractor fail-closed>"], detected=det, fired=fired))
    ran = [r for r in out if r["detected"] is not None]
    return dict(baseline_pass=sum(1 for v in good.values() if v), baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out), ran=len(ran),
                skipped=[r["fixture_id"] for r in out if r["detected"] is None],
                detected=sum(1 for r in ran if r["detected"]),
                missed=sorted(r["fixture_id"] for r in ran if not r["detected"]),
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if r["missed"] or r["baseline_false_failures"] else 0)
