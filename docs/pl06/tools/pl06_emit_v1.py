# -*- coding: utf-8 -*-
"""Emits every PL06 scale-out deliverable from the one controlled data source.

    python3 docs/pl06/tools/pl06_emit_v1.py [outdir]

The Markdown inventory and the CSV inventory are produced in the same pass from the same
list of dicts, so `MARKDOWN_CSV_DIVERGENCE` can only be non-zero if this file is wrong —
never because two hand-maintained documents drifted.
"""
import csv, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pl06_inventory_data_v1 as D

OUT = os.path.dirname(HERE)


def _cell(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (list, tuple)):
        return "; ".join(str(x) for x in v)
    return str(v)


def csv_text():
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(D.CSV_COLUMNS)
    for u in D.UNITS:
        w.writerow([_cell(u[c]) for c in D.CSV_COLUMNS])
    return buf.getvalue()


def _md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(_cell(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)


# ------------------------------------------------------------------ inventory
def inventory_md():
    topo = " / ".join(str(D.TOPOLOGY[t]) for t in sorted(D.TOPOLOGY))
    done = sum(1 for u in D.UNITS if u["unit_scope"] == "DELIVERED_BASELINE")
    L = ["# PL06_STORYBOARD_PRODUCTION_INVENTORY — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}` — do not hand-edit this file; "
         "edit the controlled data source and re-emit.", "",
         "```", f"UNITS = {len(D.UNITS)}",
         "TOPIK_ENUMERATED = 7 of 7",
         f"BAHAGIAN_ENUMERATED = {len(D.UNITS)} of {len(D.UNITS)}",
         f"TOPOLOGY = {topo}",
         f"COMPLETED = {done}   REMAINING = {len(D.UNITS) - done}",
         f"GROUPING_AUTHORITY = {D.GROUPING_AUTHORITY['status']}",
         f"VERDICT = {D.VERDICT}", "```", "",
         "> **Stage 4.2F-A2 replaced this inventory's foundation.** The previous version listed "
         "**8** units at Topik granularity with every Bahagian unresolved, because the only "
         "artifact describing PL06 was a montage slide that enumerates Topik and nothing else. "
         "The source ingest supplies the complete module by identity and a frozen boundary map "
         "with a named DOCX heading anchor for all **14** lesson units. Every row below is now "
         "read from that map, not asserted here.", "",
         "# 1. What the evidence establishes", "",
         "| Level | Established | Evidence |", "|---|---|---|",
         "| Course | K5 — Kursus Kerja Bangunan – Pembinaan Landskap Luar | M1 |",
         "| Pakej Latihan | eight, PL01–PL08, named | M1 slide 2 |",
         "| PL06 Topik | **seven, named** | M2 slide 3, corroborated by F1 body headings |",
         f"| PL06 Bahagian | **fourteen**, topology {topo} | F2 boundary map |",
         "| PL06 module span | pages 162–309; PL07 begins at 310 | F1 / F2 |",
         "| Per-unit boundary | named DOCX heading anchor + paragraph index | F2 |",
         "| T03 B02 content | 26 source rows, 14 assets, modul ms 237–250 | P1, F2 |",
         "| Any other unit's content | **not yet extracted** | — |", "",
         "# 1.1 What it does not establish", "",
         f"The lesson **grouping** authority is `{D.GROUPING_AUTHORITY['status']}`. "
         + D.GROUPING_AUTHORITY["what_is_established"].capitalize()
         + ". What is not established: " + D.GROUPING_AUTHORITY["what_is_not_established"]
         + ". Referenced as "
         + ", ".join(f"`{i}`" for i in D.GROUPING_AUTHORITY["referenced_identifiers"])
         + " — " + D.GROUPING_AUTHORITY["search_result"] + ".", "",
         D.GROUPING_AUTHORITY["note"], "",
         "The seven Topik titles, as carried by the frozen boundary map:", ""]
    for n, t in D._TOPIK:
        L.append(f"{n}. **Topik {n}: {t}** — {D.TOPOLOGY[n]} "
                 + ("lesson" if D.TOPOLOGY[n] == 1 else "lessons"))
    L += ["", "# 2. Unit inventory", ""]
    _bm = {r["unit_id"]: r for r in D.BOUNDARY_ROWS}
    L.append(_md_table(
        ["order", "unit_id", "lesson title", "modul ms", "boundary", "scope", "readiness", "lane"],
        [[u["recommended_execution_order"], f"`{u['unit_id']}`", u["bahagian_title"],
          _bm[u["unit_id"]]["module_page_range"],
          ("shared" if (_bm[u["unit_id"]]["shared_start"] or _bm[u["unit_id"]]["shared_end"])
           else "clean"),
          u["unit_scope"], f"`{u['readiness_status']}`",
          u["lane"].replace("LANE_", "").split("_")[0]]
         for u in D.UNITS]))
    L += ["",
          f"Six of the fourteen units start or end on a **shared** module page "
          f"({', '.join(str(p) for p in D.SHARED_BOUNDARY_PAGES)}) and must be split by heading "
          "anchor, never by page extraction.", ""]
    L += ["", "# 3. Per-unit detail", ""]
    for u in D.UNITS:
        L += [f"## `{u['unit_id']}` — {u['topik_title']}"
              + (f", Bahagian {u['bahagian_number']}" if u["bahagian_number"] is not None else ""),
              ""]
        L.append(_md_table(["field", "value"],
                           [[c, u[c]] for c in D.CSV_COLUMNS if c not in ("unit_id",)]))
        L.append("")
    L += ["# 4. Source anomalies found while reading the evidence", "",
          "Recorded, not silently corrected.", ""]
    L.append(_md_table(["id", "locus", "finding", "impact", "owner", "status"],
                       [[a["id"], a["locus"], a["finding"], a["impact"], a["owner"], a["status"]]
                        for a in D.SOURCE_ANOMALIES]))
    L += ["", "# 5. Frozen evidence register", ""]
    L.append(_md_table(["ref", "kind", "path", "bytes", "sha256", "establishes", "authority"],
                       [[e["ref"], e["kind"], f"`{e['path']}`", e["bytes"] or "—",
                         (e["sha256"][:16] + "…") if e["sha256"] else "—",
                         e["establishes"], e["authority_class"]] for e in D.EVIDENCE]))
    L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ portability
def portability_md():
    counts = {c: sum(1 for r in D.RULES if r["portability_class"] == c)
              for c in D.PORTABILITY_CLASSES}
    L = ["# PL06_RULE_PORTABILITY_MATRIX — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```"]
    for c in D.PORTABILITY_CLASSES:
        L.append(f"{c} = {counts[c]}")
    L += [f"TOTAL_RULES = {len(D.RULES)}", "```", "",
          "> **A rule is not global because it worked once.** Every entry in class A had to be "
          "traceable to a statement about the shell, the grammar or the governance mechanism — "
          "not to the fact that B02 shipped with it. Two entries (RP-009, RP-010) are marked "
          "GLOBAL on the strength of a Style and Guidelines document that is itself the B02 "
          "slice, and both carry `human_authority_required = VERIFY` for that reason.", ""]
    for c, title in [("PL06_GLOBAL_REUSABLE", "A. PL06_GLOBAL_REUSABLE"),
                     ("REUSABLE_WITH_SOURCE_SPECIFIC_BINDING",
                      "B. REUSABLE_WITH_SOURCE_SPECIFIC_BINDING"),
                     ("B02_SPECIFIC_DO_NOT_PROPAGATE", "C. B02_SPECIFIC_DO_NOT_PROPAGATE")]:
        L += [f"# {title}", ""]
        L.append(_md_table(
            ["rule_id", "rule", "evidence", "destination scope", "human authority",
             "oracle", "propagation risk"],
            [[f"`{r['rule_id']}`", r["rule_description"], r["evidence"], r["destination_scope"],
              r["human_authority_required"], "yes" if r["automated_oracle_available"] else "**no**",
              r["propagation_risk"]]
             for r in D.RULES if r["portability_class"] == c]))
        L.append("")
    L += ["# The two rules most likely to be propagated wrongly", "",
          "**RP-106 / RP-215 — the cast.** Bariah's answer *\"Gunakan nama watak untuk keseluruhan "
          "PL06\"* is PL06-scoped, which makes it read like a global instruction. It is an answer "
          "about the *practice* of naming characters, qualified by *bergantung kepada kesesuaian*, "
          "and it names no one. Meanwhile the ratified character bank marks **Haziq** and **Encik "
          "Roslan** CANONICAL while B02 ships **Alya** and **Encik Rahman**. Reading her answer as "
          "\"use Alya and Encik Rahman everywhere\" would override a ratified bank on the strength "
          "of an answer to a different question. Recorded as `SRC-ANOM-003` and `STOP-006`.", "",
          "**RP-205 — the overview cardinalities.** 5, 5, 3, 3, 3, 2, 3, 2, 1 is the most "
          "template-shaped artefact B02 produced, and the frozen mapping contract explicitly "
          "records `UNIVERSAL_FIXED_CARD_COUNT = False` and `MINIMUM_OVERVIEW_CARDINALITY = 1`. "
          "The counts are per-component derivations from B02's own source rows. Nothing above the "
          "minimum transfers.", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ capability
def capability_md():
    lanes = {}
    for u in D.UNITS:
        lanes[u["lane"]] = lanes.get(u["lane"], 0) + 1
    L = ["# PL06_CAPABILITY_COVERAGE_MATRIX — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```"]
    for l in D.LANE_VALUES:
        L.append(f"{l} = {lanes.get(l, 0)}")
    L += ["```", "",
          "> One unit is Lane A and it is the one already delivered. Every remaining unit is "
          "Lane D. That is not a statement about our generator — the shell, the Notes schema, the "
          "geometry registry and the identity discipline are all ready. It is a statement about "
          "custody: there is no source to point them at.", "",
          "# Lane assignment", ""]
    L.append(_md_table(["unit_id", "lane", "effort", "source-authority dependency"],
                       [[f"`{c['unit_id']}`", c["lane"], c["estimated_implementation_effort"],
                         c["source_authority_dependency"]] for c in D.CAPABILITY]))
    L += ["", "# Detail", ""]
    for c in D.CAPABILITY:
        L += [f"## `{c['unit_id']}`", ""]
        L.append(_md_table(["field", "value"],
                           [[k, v] for k, v in c.items() if k != "unit_id"]))
        L.append("")
    L += ["# What is portable today, independent of any unit", "",
          "The capability that would survive contact with a new unit right now:", "",
          "- the review shell and its stage geometry (RP-001)",
          "- the S01/S02/S03 grammar as *structure* (RP-002)",
          "- the production panel and the artifact-identity discipline (RP-003, RP-014)",
          "- the typed Notes block schema (RP-004)",
          "- the italics *mechanism*, not the term list (RP-005)",
          "- completion-state, Rumusan, quiz-review and Tamat treatments (RP-006 – RP-012)",
          "- the registered off-canvas geometry treatment (RP-013)",
          "- the oracle contract and population-pinning discipline (RP-016, RP-017)", "",
          "What is not portable is everything that touches content: the families, the components, "
          "the cardinalities, the subjects, the counts and the glossary.", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ selection
def selection_md():
    S = D.SELECTION
    L = ["# PL06_FIRST_SCALE_OUT_SELECTION — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"SELECTED_FIRST_SCALE_OUT_UNIT = {S['selected_unit_id']}",
         f"SELECTION_STATUS = {S['selection_status']}",
         f"SELECTION_IS_UNCONDITIONAL = {str(S['selection_is_unconditional']).lower()}",
         "```", "",
         "# 1. Scoring", "",
         "Scores are 0–5. **A criterion with no evidence scores 0, not a midpoint.** That is why "
         "four of the ten columns are zero for every candidate.", ""]
    L.append(_md_table(["candidate"] + D.SELECTION_CRITERIA + ["total"],
                       [[f"`{c['unit_id']}`"] + [c["scores"][k] for k in D.SELECTION_CRITERIA]
                        + [sum(c["scores"].values())] for c in D.CANDIDATE_SCORES]))
    L += ["", "Notes on each candidate:", ""]
    for c in D.CANDIDATE_SCORES:
        L.append(f"- **`{c['unit_id']}`** — {c['label']}. {c['note']}")
    L += ["", "# 2. Selection rationale", ""]
    for r in S["rationale"]:
        L.append(f"- {r}")
    L += ["", "# 3. What this selection is not", "", S["honest_caveat"], "",
          "# 4. Rejected candidates", ""]
    L.append(_md_table(["unit_id", "reason"],
                       [[f"`{r['unit_id']}`", r["reason"]] for r in S["rejected"]]))
    L += ["", "# 5. Required preconditions", "",
          "None of these is ours to satisfy alone.", ""]
    for p in S["required_preconditions"]:
        L.append(f"- {p}")
    L += ["", "# 6. Expected end-to-end path", ""]
    for i, s in enumerate(S["expected_end_to_end_path"], 1):
        L.append(f"{s}" if s[0].isdigit() else f"{i}. {s}")
    L += ["", "Step 5 is the one that matters for a scale-out proof. If the unit's structure is "
          "re-derived and it happens to land on something like Family S, that is a finding. If "
          "Family S is imported and then found to fit, that is not a finding — it is the "
          "architecture answering its own question.", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ plan
def plan_md():
    L = ["# PL06_EXECUTION_PLAN — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"WAVE_0_UNITS = 1", f"WAVE_1_UNITS = 0", f"WAVE_2_UNITS = 0", f"WAVE_3_UNITS = 0",
         f"HELD_UNITS = {len(D.WAVES[4]['units'])}",
         f"WAVE_0_WORKING_TIME = {D.WAVE0_WORKING_TIME}", "```", "",
         "> Waves 1, 2 and 3 are empty and that is the honest state. A unit cannot be placed in a "
         "lane before its source is read, so every remaining unit sits on Hold and the plan below "
         "is a plan for **one** unit plus a source-delivery request.", "",
         "# 1. Duration basis", "",
         "Every figure in this plan is either measured in this repository or marked "
         "`NOT_EVIDENCED`. Nothing is estimated from experience.", ""]
    L.append(_md_table(["metric", "value", "basis"],
                       [[m["metric"], f"**{m['value']}**", m["basis"]] for m in D.MEASURED_BASIS]))
    L += ["", "# 2. Waves", ""]
    L.append(_md_table(["wave", "title", "units", "entry condition"],
                       [[w["wave"], w["title"],
                         ", ".join(f"`{u}`" for u in w["units"]) or "—",
                         w["entry_condition"]] for w in D.WAVES]))
    L += ["", "# 3. Per-unit plan", ""]
    L.append(_md_table(
        ["unit_id", "wave", "owner", "deps", "source", "model", "gen", "QA", "render",
         "smoke", "Bariah", "output", "blocker"],
        [[f"`{r['unit_id']}`", r["wave"], r["owner"], r["dependencies"], r["source_extraction"],
          r["controlled_model"], r["generation"], r["automated_qa"], r["rendered_inspection"],
          r["powerpoint_smoke"], r["bariah_review"], r["expected_output_version"], r["blocker"]]
         for r in D.PLAN_ROWS]))
    L += ["", "# 4. Wave 0 total", "",
          f"**{D.WAVE0_WORKING_TIME} of working time.** Basis: {D.WAVE0_WORKING_TIME_BASIS}", "",
          "The Bariah review turnaround measured twice at a mean of **14h15m calendar** is "
          "excluded — it is not our time to spend and it is not working hours.", "",
          "# 5. The critical path is not ours", "",
          "Wave 0's working time is under three hours. It has been blocked for the entire life of "
          "this project on one thing: **a module extract that is not in the repository.** The "
          "same blocker held B02 up at its intake gate on 31 July until the source arrived by "
          "Drive, at which point the whole first block took 3h18m end to end.", "",
          "The highest-value action available today is not engineering. It is asking for the "
          "Topik 4 page range and the Bahagian list.", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ open items
def open_items_md():
    L = ["# PL06_OPEN_AUTHORITY_ITEMS — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"STOP_CONDITIONS = {len(D.STOP_CONDITIONS)}"]
    for s in D.STOP_SCOPES:
        L.append(f"{s} = {sum(1 for c in D.STOP_CONDITIONS if c['scope'] == s)}")
    L += ["```", "",
          "> A global open item does not block an unrelated ready unit. That is why `scope` is a "
          "typed field: `BLOCKS_THIS_UNIT` stops a build, the other three do not.", "",
          "# Stop conditions", ""]
    L.append(_md_table(["id", "condition", "scope", "applies to", "description", "resolver",
                        "evidence"],
                       [[f"`{c['id']}`", c["condition"], f"**{c['scope']}**",
                         ", ".join(c["applies_to"]) if c["applies_to"] != ["ALL"] else "ALL",
                         c["description"], c["resolver"], c["evidence"]]
                        for c in D.STOP_CONDITIONS]))
    L += ["", "# Source anomalies", ""]
    L.append(_md_table(["id", "locus", "verbatim", "finding", "owner", "status"],
                       [[a["id"], a["locus"], f"`{a['verbatim']}`", a["finding"], a["owner"],
                         a["status"]] for a in D.SOURCE_ANOMALIES]))
    L += ["", "# Who owns what", "",
          "| Owner | Items |", "|---|---|",
          "| **FIRDAUS / CAIR** | source delivery for every remaining unit (STOP-001), "
          "canonical module integrity (STOP-009), running and recording the PowerPoint smoke "
          "(STOP-011) |",
          "| **BARIAH** | Bahagian boundaries (STOP-002), cast binding (STOP-006), the montage "
          "numbering anomaly (SRC-ANOM-001), written confirmation of the call approval |",
          "| **source governance** | PL06 pronunciation precedence (STOP-007), MS2680 (STOP-008) |",
          "| **CAIR** | the K5 course lock (STOP-010) |",
          "| **CC** | nothing on this list. Every item here needs a human. |", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ approval record
def approval_md():
    A = D.APPROVAL_RECORD
    L = ["# B02_BARIAH_CALL_APPROVAL_RECORD — v1", "",
         f"Stage {D.STAGE}. Generated from `{D.GENERATED_BY}`.", "", "```",
         f"AUTHORITY_CLASS = {A['authority_class']}",
         f"WRITTEN_CONFIRMATION = {A['written_confirmation']}", "```", "",
         "# 1. The record", ""]
    L.append(_md_table(["field", "value"],
                       [["project", A["project"]], ["artifact", f"`{A['artifact']}`"],
                        ["bytes", f"{A['artifact_bytes']:,}"],
                        ["sha256", f"`{A['artifact_sha256']}`"],
                        ["approval channel", f"**{A['approval_channel']}**"],
                        ["reported by", A["reported_by"]], ["reviewer", A["reviewer"]],
                        ["reported result", A["reported_result"]],
                        ["direction", f"**{A['direction']}**"],
                        ["authority class", f"**{A['authority_class']}**"],
                        ["written confirmation", f"**{A['written_confirmation']}**"]]))
    L += ["", "# 2. What this is", "", A["evidence_status"], "",
          "# 3. What it authorises", ""]
    for m in A["may_authorise"]:
        L.append(f"- {m}")
    L += ["", "# 4. What it does not authorise", ""]
    for m in A["may_not_authorise"]:
        L.append(f"- {m}")
    L += ["", "**Forbidden classifications for this event:** "
          + ", ".join(f"`{f}`" for f in A["forbidden_classifications"]) + ". A call is not a "
          "screenshot and it is not a written confirmation, however clear the report of it is.",
          "", "# 5. PowerPoint smoke", "", A["powerpoint_smoke_status"], "",
          "This matters more than it looks. `READY_FOR_MICROSOFT_POWERPOINT_SMOKE` was the whole "
          "point of the v0.4.4.1 release, and the deck has now been opened in PowerPoint — by "
          "Bariah, on her machine, with no record of what was checked. That is genuinely good "
          "news and it is not the test. The test remains unrun.", "",
          "# 6. Supersession", "",
          "This record is superseded, not amended, the moment written confirmation arrives. The "
          "replacement record inherits nothing: a written confirmation may say less than the call "
          "did, and if it does, the written text wins.", ""]
    return "\n".join(L)


FILES = [
    ("PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.md", inventory_md),
    ("PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.csv", csv_text),
    ("PL06_RULE_PORTABILITY_MATRIX_v1.md", portability_md),
    ("PL06_CAPABILITY_COVERAGE_MATRIX_v1.md", capability_md),
    ("PL06_FIRST_SCALE_OUT_SELECTION_v1.md", selection_md),
    ("PL06_EXECUTION_PLAN_v1.md", plan_md),
    ("PL06_OPEN_AUTHORITY_ITEMS_v1.md", open_items_md),
    ("B02_BARIAH_CALL_APPROVAL_RECORD_v1.md", approval_md),
]


def write(outdir=OUT):
    os.makedirs(outdir, exist_ok=True)
    written = []
    for name, fn in FILES:
        body = fn()
        if not body.endswith("\n"):
            body += "\n"
        p = os.path.join(outdir, name)
        open(p, "w", encoding="utf-8").write(body)
        written.append(p)
    return written


if __name__ == "__main__":
    for p in write(sys.argv[1] if len(sys.argv) > 1 else OUT):
        print("wrote", os.path.relpath(p))
