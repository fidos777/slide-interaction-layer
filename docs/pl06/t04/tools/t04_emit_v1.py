# -*- coding: utf-8 -*-
"""Emits every T04 deliverable from the one controlled extract plus its analysis layer.

    python3 docs/pl06/t04/tools/t04_emit_v1.py
"""
import csv, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_data_v1 as D

OUT = os.path.dirname(HERE)


def _c(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (list, tuple)):
        return "; ".join(str(x) for x in v)
    return str(v)


def _tbl(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(_c(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def _csv(cols, rows):
    b = io.StringIO()
    w = csv.writer(b, lineterminator="\n")
    w.writerow(cols)
    for r in rows:
        w.writerow([_c(r.get(c)) for c in cols])
    return b.getvalue()


VIS_COLS = ["asset_id", "unit_id", "asset_kind", "relationship_id", "embedded_filename",
            "mime_type", "dimensions_in", "sha256", "nearest_heading", "source_paragraph",
            "module_page", "caption", "source_subject_nodes", "node_count",
            "proposed_storyboard_role", "source_bound_status"]
TBL_COLS = ["table_id", "unit_id", "sequence", "heading_path", "rows", "columns",
            "merged_cells", "module_page", "segment_index"]
LST_COLS = ["list_item_id", "row_id", "unit_id", "sequence", "num_id", "level", "marker_type",
            "style", "heading_path", "module_page", "raw_wording"]


def visual_csv():
    return _csv(VIS_COLS, D.ASSETS)


def table_csv():
    if not D.TABLES:
        # An empty inventory still needs a header row and an explicit statement, or a reader
        # cannot tell "no tables" from "not checked".
        return _csv(TBL_COLS, []) + "# NO TABLES IN K5-PL06-T04-B01 — 140 body elements in the\n" \
               "# boundary, all <w:p>, zero <w:tbl>. Measured, not assumed.\n"
    return _csv(TBL_COLS, D.TABLES)


def list_csv():
    return _csv(LST_COLS, D.LISTS)


def controlled_content_md():
    T = D.TOTALS
    L = ["# T04_CONTROLLED_CONTENT — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}` — do not hand-edit. "
         "Every row is read from `T04_SOURCE_EXTRACT_v1.json`.", "", "```",
         f"UNIT            = {D.UNIT_ID}",
         f"LESSON          = {D.EX['lesson_title']}",
         f"MODULE PAGES    = {D.BOUNDARY['module_pages'][0]}-{D.BOUNDARY['module_pages'][1]}",
         f"SUBTOPICS       = {D.BOUNDARY['subtopics']}",
         f"CONTENT ROWS    = {T['content_rows']}",
         f"AUTHORITY       = MODULE_SOURCE_ATTESTED (all rows)",
         f"VERDICT         = {D.VERDICT}", "```", "",
         "# 1. Boundary", "",
         _tbl(["field", "value"], [
             ["raw start anchor", f"`{D.BOUNDARY['raw_start_anchor']}`"],
             ["governed display label", f"`{D.BOUNDARY['governed_start_label']}`"],
             ["normalisation status", f"**{D.BOUNDARY['normalisation_status']}**"],
             ["normalisation authority", D.BOUNDARY["normalisation_authority"]],
             ["raw stop anchor", f"`{D.BOUNDARY['raw_stop_anchor']}` (excluded)"],
             ["paragraph span", f"{D.PROBE['paragraph_enumeration']['start_index']} to before "
                                f"{D.PROBE['paragraph_enumeration']['stop_index']}"],
             ["module pages", "276–283"]]), "",
         "**The misspelled heading is the anchor.** Searching the body for the correctly "
         "spelled `PENJAGAAN DAN PENYELENGGARAAN` returns "
         f"{len(D.PROBE['anchor_search']['governed_label_body_hits'])} body headings — the only "
         "match in the document is the table-of-contents entry, which is not a section start. "
         "An extraction driven from the governed label would find nothing.", "",
         "## 1.1 The paragraph index is enumeration-dependent", "",
         "The frozen map's 5220 and 5360 hold under **one** enumeration: direct `<w:p>` "
         "children of `<w:body>` — python-docx `Document.paragraphs` — which **excludes "
         "paragraphs nested inside tables**. Counting every `<w:p>` in the body instead gives "
         f"**{D.PROBE['paragraph_enumeration']['alternate_enumeration']['start_index']}** and "
         f"**{D.PROBE['paragraph_enumeration']['alternate_enumeration']['stop_index']}** — the "
         "same 140-paragraph span, shifted by "
         f"{D.PROBE['paragraph_enumeration']['alternate_enumeration']['offset_from_used']}.", "",
         "Both are recorded in the extract. Extraction walks **body children** between the two "
         "anchor elements, not the index, so a table inside the boundary would be captured "
         "even though the index that located the boundary cannot see one. There are none — "
         "measured, not assumed.", "",
         "# 2. Totals", "",
         _tbl(["metric", "value"], [[k, v] for k, v in T.items()]), "",
         "# 3. Structure", "",
         _tbl(["level", "heading", "module page"],
              [[r["content_type"].replace("HEADING_", "H"), r["controlled_display_text"],
                r["module_page"]] for r in D.ROWS
               if r["content_type"] in ("HEADING_1", "HEADING_2")]), "",
         "Below the two Heading-2 blocks sit "
         f"{sum(1 for r in D.ROWS if r['content_type'] == 'HEADING_3')} Heading-3 rows. "
         "Landskap Lembut decomposes into three maintenance operations — **Siram**, **Baja**, "
         "**Racun** — each with a definition, a *Kaedah Pelaksanaan* block and an *Aspek "
         "Pengurusan untuk Kontraktor* block. Landskap Kejur decomposes into four function "
         "groups, each with two sub-items.", "",
         "# 4. Every row", ""]
    L.append(_tbl(["row_id", "seq", "type", "page", "heading path", "controlled display text"],
                  [[f"`{r['row_id']}`", r["sequence"], r["content_type"], r["module_page"],
                    " › ".join(r["heading_path"]),
                    (r["controlled_display_text"] or "—")[:150]] for r in D.ROWS]))
    L += ["", "Every row carries `authority_class = MODULE_SOURCE_ATTESTED`. Nothing in this "
          "unit is BARIAH_DIRECT: she has ruled on B02's treatment, not on T04's content.", ""]
    return "\n".join(L)


def rumusan_quiz_md():
    L = ["# T04_RUMUSAN_AND_QUIZ_MAP — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         "RUMUSAN      = NOT_FOUND", "QUIZ_ITEMS   = NOT_FOUND", "ANSWER_KEY   = NOT_FOUND",
         "FEEDBACK     = SOURCE_AVAILABLE_ELSEWHERE",
         "COMPOSITION  = AUTHORITY_UNRESOLVED", "```", "",
         "> **The module contains no Rumusan and no assessment items — for T04 or for any "
         "other unit.** Searched the entire DOCX body, all 6,167 body-level paragraphs: "
         "`Rumusan` 0 hits, `Kuiz` 0 hits, `Soalan` 0 hits.", "",
         "This retro-explains B02. Its Rumusan and its five quiz questions were **authored**, "
         "not extracted — the Style and Guidelines specifies the treatment and supplies no "
         "text. No storyboard in this project has ever had a source-supplied Rumusan, and "
         "nothing about the source ingest changes that.", "",
         "# Coverage", ""]
    L.append(_tbl(["item", "status", "evidence", "implication", "authority", "blocks"],
                  [[i["item"], f"**{i['status']}**", i["evidence"], i["implication"],
                    i["authority"], i["blocks"]] for i in D.QUIZ_COVERAGE]))
    L += ["", "# What must not be assumed", "",
          "`4 MCQ + 1 MR` and the `60%` pass threshold are specified in **A3**, which is the "
          "B02 slice of the Style and Guidelines. No artifact states that either applies to "
          "every PL06 unit. Both are carried as `AUTHORITY_UNRESOLVED` and as rules RP-009 and "
          "RP-010 with `human_authority_required = VERIFY`. Applying them to T04 without "
          "confirmation would be exactly the B02-specific propagation the portability matrix "
          "exists to prevent.", "",
          "No question, option, answer or Rumusan sentence has been drafted in this stage.", ""]
    return "\n".join(L)


def claims_md():
    L = ["# T04_EXTERNAL_CLAIMS_REGISTER — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"CLAIMS = {len(D.EXTERNAL_CLAIMS)}",
         f"EXTERNAL_VERIFICATION_REQUIRED = "
         f"{sum(1 for c in D.EXTERNAL_CLAIMS if c['status'] == 'EXTERNAL_VERIFICATION_REQUIRED')}",
         f"SAFE_FOR_REVIEW_DECK = "
         f"{sum(1 for c in D.EXTERNAL_CLAIMS if c['scope'] == 'SAFE_FOR_REVIEW_DECK')}",
         "BLOCKS_THIS_UNIT = 0", "MS2680_IN_T04 = false", "```", "",
         "> **No claim in T04 blocks this unit.** Two require external verification before "
         "canonical freeze; the rest are source statements that render safely in a review "
         "deck. MS2680 — the open B02 standards item — appears **nowhere** in T04, so it does "
         "not touch this unit. A global open item must not block unrelated content.", "",
         "# Claims", ""]
    L.append(_tbl(["id", "kind", "quote", "status", "scope", "rows"],
                  [[f"`{c['claim_id']}`", c["kind"], c["quote"], f"**{c['status']}**",
                    c["scope"], ", ".join(c["row_ids"]) or "—"] for c in D.EXTERNAL_CLAIMS]))
    L += ["", "# Notes", ""]
    for c in D.EXTERNAL_CLAIMS:
        L.append(f"- **`{c['claim_id']}` {c['kind']}** — {c['note']}")
    L += ["", "# Two cautions for the storyboard model", "",
          "- **Do not tighten a qualitative condition into a number.** The source says spraying "
          "may only happen in *cuaca tenang (tidak berangin)*. It states no wind speed. Writing "
          "one would be inventing a technical threshold.",
          "- **Do not state a watering frequency.** The source gives a timing practice — early "
          "morning or late afternoon — and then explicitly defers frequency to plant type, "
          "weather and growth stage. That deferral is the content.", ""]
    return "\n".join(L)


def candidates_md():
    L = ["# T04_SCREEN_CANDIDATE_MAP — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"CANDIDATES = {len(D.SCREEN_CANDIDATES)}",
         f"NEW_TREATMENT_REQUIRED = "
         f"{sum(1 for c in D.SCREEN_CANDIDATES if c['new_treatment_required'].startswith('YES'))}",
         f"PENDING_HUMAN = "
         f"{sum(1 for c in D.SCREEN_CANDIDATES if c['candidate'] == 'PENDING_HUMAN')}",
         "B02_FAMILIES_PROPAGATED = 0", "```", "",
         "> **These are candidates, not a design.** Every one names the source rows it rests "
         "on. None imports FAMILY_S, FAMILY_P1, FAMILY_P2, a B02 cardinality, the Papan Tanda "
         "or BBQ Pit rulings, a B02 learner-screen count, or Alya and Encik Rahman.", "",
         "# Candidates", ""]
    for c in D.SCREEN_CANDIDATES:
        L += [f"## `{c['candidate_id']}` — {c['candidate']}: {c['title']}", "",
              _tbl(["field", "value"], [
                  ["source rows", ", ".join(f"`{r}`" for r in c["source_rows"]) or "**none**"],
                  ["reason", c["reason"]],
                  ["reusable capability", c["reusable_capability"]],
                  ["new treatment required", f"**{c['new_treatment_required']}**"],
                  ["human decision required", c["human_decision_required"]],
                  ["visual dependency", c["visual_dependency"]],
                  ["narration dependency", c["narration_dependency"]]]), ""]
    L += ["# The portability finding", "",
          "**Five of six candidates have no visual dependency at all, because the unit has no "
          "photographs.** T04 contains exactly one visual — the opening SmartArt process "
          "diagram — against B02's fourteen extracted assets.", "",
          "That single fact is the most useful thing this stage produced. B02's component-main "
          "treatment is a *source-bound overview of photographs*; it was ruled by Bariah on a "
          "unit that had photographs to bind. T04 has none. Applying the same treatment here "
          "would require inventing subjects, which is prohibited — so RP-101 arrives with "
          "nothing to bind to, and that needs a human ruling rather than a default.", ""]
    return "\n".join(L)


def gaps_md():
    L = ["# T04_SOURCE_GAPS — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"GAPS = {len(D.SOURCE_GAPS)}",
         f"BLOCKS_THIS_UNIT = "
         f"{sum(1 for g in D.SOURCE_GAPS if g['severity'] == 'BLOCKS_THIS_UNIT')}",
         f"INSTRUCTIONAL_STATUS = {D.READINESS['instructional_status']}", "```", "",
         "# Readiness semantics", "",
         "`SOURCE_INCOMPLETE` is retired for these units. It conflated three different states "
         "with three different owners:", "",
         _tbl(["state", "meaning", "who clears it"], [
             ["`SOURCE_PRESENT_CONTENT_NOT_EXTRACTED`",
              "source and boundary in custody, nobody has read it", "us, by working"],
             ["`CONTENT_ASSESSMENT_PENDING`",
              "read and modelled, instructional treatment not settled", "us to propose, a human to approve"],
             ["`SOURCE_GAP_CONFIRMED`",
              "read, and the content is genuinely not in the module",
              "**nobody, by reading** — it must be authored"]]), "",
         f"**T04-B01 is `{D.READINESS['instructional_status']}`.** " + D.READINESS["content_extraction"] + ".", "",
         f"The other twelve units stay `SOURCE_PRESENT_CONTENT_NOT_EXTRACTED`. "
         + D.READINESS["note"], "",
         "# Gaps", ""]
    L.append(_tbl(["id", "item", "severity", "finding", "owner"],
                  [[f"`{g['gap_id']}`", g["item"], f"**{g['severity']}**", g["finding"],
                    g["owner"]] for g in D.SOURCE_GAPS]))
    L += ["", "# Notes", ""]
    for g in D.SOURCE_GAPS:
        L.append(f"- **`{g['gap_id']}`** — {g['note']}")
    L += ["", "# Targeted decisions", "",
          "Five, and none of them is ours to close:", ""]
    L.append(_tbl(["id", "question", "owner", "blocks", "evidence"],
                  [[f"`{d['decision_id']}`", d["question"], d["owner"], d["blocks"],
                    d["evidence"]] for d in D.TARGETED_DECISIONS]))
    L.append("")
    return "\n".join(L)


FILES = [
    ("T04_CONTROLLED_CONTENT_v1.md", controlled_content_md),
    ("T04_VISUAL_INVENTORY_v1.csv", visual_csv),
    ("T04_TABLE_INVENTORY_v1.csv", table_csv),
    ("T04_LIST_INVENTORY_v1.csv", list_csv),
    ("T04_RUMUSAN_AND_QUIZ_MAP_v1.md", rumusan_quiz_md),
    ("T04_EXTERNAL_CLAIMS_REGISTER_v1.md", claims_md),
    ("T04_SCREEN_CANDIDATE_MAP_v1.md", candidates_md),
    ("T04_SOURCE_GAPS_v1.md", gaps_md),
]


def write(outdir=OUT):
    out = []
    for name, fn in FILES:
        b = fn()
        if not b.endswith("\n"):
            b += "\n"
        p = os.path.join(outdir, name)
        open(p, "w", encoding="utf-8").write(b)
        out.append(p)
    return out


if __name__ == "__main__":
    for p in write():
        print("wrote", os.path.relpath(p))
