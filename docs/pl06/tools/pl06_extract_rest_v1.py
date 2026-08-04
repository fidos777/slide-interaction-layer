# -*- coding: utf-8 -*-
"""Stage 4.2F-D Lane 5 — the eight remaining PL06 units, extracted and modelled.

    python3 docs/pl06/tools/pl06_extract_rest_v1.py

The unit list is DERIVED from the frozen boundary map, never typed. Fourteen units are
mapped; six are already represented — the delivered B02 proof, T04, and the four batch 1
units — so eight remain, and the count is computed rather than assumed.

The reader is `pl06_extract_v1.extract`, unchanged, so these eight are read by exactly the
same code that reproduced the frozen T04 extract.

WHAT THIS LAYER CLAIMS, AND HOW
-------------------------------
Batch 1's propositions and assessment stems were hand-authored after reading every unit's
content. Eight more units cannot be hand-read at that depth in one run, and inventing forty
stems that nobody verified would be worse than deriving fewer honestly. So this layer derives
them MECHANICALLY, by a stated rule, quoting the source verbatim:

    mandatory proposition   a row whose text carries an obligation marker — mesti, wajib,
                            perlu, hendaklah, tidak boleh — quoted as-is, with its row ID
    definitional statement  a row carrying ialah / adalah / merujuk kepada, quoted as-is

Both are SOURCE_DERIVED and checkable against the row they cite. Neither is an assessment
item: an item still needs a stem, a key and distractors, and those are marked
PENDING_UNIT_EXCEPTION_REVIEW rather than guessed. The derivation rule is published so it can
be disagreed with.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PL06 = os.path.dirname(HERE)
DOCS = os.path.dirname(PL06)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(DOCS, "source", "tools"))
import pl06_extract_v1 as EX      # noqa: E402
import pl06_unit_model_v1 as UM   # noqa: E402
import pl06_batch1_data_v1 as B   # noqa: E402

STAGE = "4.2F-D"
AUTHORITY = "SRC-AUTH-01"
OUT_DIR = os.path.join(PL06, "rest_extract")

# Already represented. B02 is delivered; T04 is built; the four batch 1 units were extracted
# and modelled in Stage 4.2F-C.
ALREADY_REPRESENTED = {
    "K5-PL06-T03-B02": "delivered B02 proof",
    "K5-PL06-T04-B01": "T04, storyboard built and state-review proven",
    "K5-PL06-T03-B03": "PL06 batch 1",
    "K5-PL06-T03-B04": "PL06 batch 1",
    "K5-PL06-T05-B01": "PL06 batch 1",
    "K5-PL06-T06-B01": "PL06 batch 1",
}

OBLIGATION_MARKERS = ["mesti", "wajib", "perlu", "hendaklah", "tidak boleh", "dilarang"]
DEFINITION_MARKERS = ["ialah", "adalah", "merujuk kepada", "bermaksud"]

DERIVATION_RULE = (
    "A mandatory proposition is a controlled row whose text contains one of "
    f"{OBLIGATION_MARKERS}. A definitional statement is a row containing one of "
    f"{DEFINITION_MARKERS}. Both are quoted verbatim with the row ID that carries them. "
    "Neither is an assessment item — an item needs a stem, a key and distractors, and those "
    "are left PENDING_UNIT_EXCEPTION_REVIEW rather than guessed.")


def _strip_numeral(s):
    """The map's anchors carry a section numeral that Word supplies from list numbering."""
    return re.sub(r"^\d+(\.\d+)*\s+", "", s).strip()


def remaining_units():
    """The list, derived from the frozen map. Nothing here is hand-typed."""
    lessons = json.load(open(B.BOUNDARY_MAP_PATH, encoding="utf-8"))["lessons"]
    out = []
    for l in lessons:
        uid = l["unit_id"]
        if uid in ALREADY_REPRESENTED:
            continue
        topik, bahagian = int(l["topik"]), int(l["bahagian"])
        lo, hi = (int(x) for x in l["module_page_range"].split("-"))
        out.append(dict(
            unit_id=uid, prefix=f"T{topik:02d}B{bahagian:02d}",
            topik=topik, bahagian=bahagian, lesson_title=l["lesson_title"],
            start_anchor=_strip_numeral(l["start_anchor"]),
            stop_anchor=_strip_numeral(l["end_before"]),
            frozen_start=int(l["docx_para_start"]),
            frozen_stop=int(l["docx_para_end_before"]),
            module_pages=(lo, hi), subtopics=l["subtopics"],
            shared_start=bool(l["shared_start"]), shared_end=bool(l["shared_end"]),
            preceding_unit=None, following_unit=None,
            raw_start_anchor=l["start_anchor"], raw_stop_anchor=l["end_before"]))
    # Neighbours, in map order, so the excluded-record proof can name them.
    order = [l["unit_id"] for l in lessons]
    for u in out:
        i = order.index(u["unit_id"])
        u["preceding_unit"] = order[i - 1] if i > 0 else None
        u["following_unit"] = order[i + 1] if i + 1 < len(order) else None
    return out


def extract_all():
    z, probe = EX._open_module()
    try:
        return {u["unit_id"]: EX.extract(u, z, probe) for u in remaining_units()}
    finally:
        z.close()


# ==========================================================================================
def obligations(ex):
    out = []
    for r in ex["rows"]:
        t = (r["raw_source_text"] or "").strip()
        if len(t) < 25:
            continue
        low = t.lower()
        hit = [m for m in OBLIGATION_MARKERS if m in low]
        if hit:
            out.append(dict(row_id=r["row_id"], module_page=r["module_page"],
                            markers=hit, text=t, heading_path=r["heading_path"],
                            cls="SOURCE_DERIVED"))
    return out


def definitions(ex):
    out = []
    for r in ex["rows"]:
        t = (r["raw_source_text"] or "").strip()
        if len(t) < 30:
            continue
        low = t.lower()
        hit = [m for m in DEFINITION_MARKERS if m in low]
        if hit:
            out.append(dict(row_id=r["row_id"], module_page=r["module_page"],
                            markers=hit, text=t, heading_path=r["heading_path"],
                            cls="SOURCE_DERIVED"))
    return out


def terminology(ex):
    """Bilingual headings — a Malay term with its English gloss in brackets."""
    out, seen = [], set()
    for r in ex["rows"]:
        t = (r["raw_source_text"] or "").strip()
        if r["content_type"].startswith("HEADING") and UM.is_structural(r) and "(" in t:
            if t not in seen:
                seen.add(t)
                out.append(dict(row_id=r["row_id"], term=t, module_page=r["module_page"],
                                cls="SOURCE_DERIVED"))
    return out


def visual_subjects(ex):
    """Only what the source actually carries: figures, diagrams and tables."""
    out = []
    for a in ex["assets"]:
        out.append(dict(subject=a.get("caption") or f"{a['asset_kind']} at "
                                                    f"{a['nearest_heading']}",
                        asset_id=a["asset_id"], kind=a["asset_kind"],
                        module_page=a["module_page"], has_source_figure=True,
                        cls="SOURCE_DERIVED"))
    for t in ex["tables"]:
        out.append(dict(subject=f"Table under {' / '.join(t['heading_path']) or 'unit root'}"
                                f" — {t['rows']}x{t['columns']}",
                        asset_id=t["table_id"], kind="SOURCE_TABLE",
                        module_page=t["module_page"], has_source_figure=True,
                        cls="SOURCE_DERIVED"))
    # Figure captions written as body text — "Rajah 26: ..." — count as source-attested
    # subjects even where the image itself sits in a neighbouring paragraph.
    for r in ex["rows"]:
        t = (r["raw_source_text"] or "").strip()
        if re.match(r"^(Rajah|Jadual)\s+\d+\s*:", t):
            out.append(dict(subject=t, asset_id=r["row_id"], kind="SOURCE_CAPTION",
                            module_page=r["module_page"], has_source_figure=True,
                            cls="SOURCE_DERIVED"))
    return out


def model(unit, ex):
    tree = UM.heading_tree(ex)
    comps = UM.components(ex)
    h2 = [h for h in tree if h["level"] == 2]
    if len(h2) > 1:
        groups = [dict(group_id=f"G{i + 1}", covers=h["text"], row_id=h["row_id"],
                       basis="LEVEL_2_HEADING") for i, h in enumerate(h2)]
        basis = "LEVEL_2_HEADING"
    elif comps:
        groups = [dict(group_id=f"G{i + 1}", covers=c["name"], row_id=c["row_id"],
                       basis="MODULE_REPEATED_COMPONENT_BLOCK") for i, c in enumerate(comps)]
        basis = "MODULE_REPEATED_COMPONENT_BLOCK"
    else:
        h3 = [h for h in tree if h["level"] == 3]
        groups = [dict(group_id=f"G{i + 1}", covers=h["text"], row_id=h["row_id"],
                       basis="LEVEL_3_HEADING_FALLBACK") for i, h in enumerate(h3)]
        basis = "LEVEL_3_HEADING_FALLBACK"

    obl, defs, vis = obligations(ex), definitions(ex), visual_subjects(ex)
    shell, closing = 2, 3
    return dict(
        unit_id=unit["unit_id"], lesson_title=unit["lesson_title"], stage=STAGE,
        authority_inherited=AUTHORITY,
        pending_pattern_package=UM.PENDING_PACKAGE,
        frozen_nothing=UM.FROZEN_NOTHING,
        derivation_rule=DERIVATION_RULE,
        model_depth=dict(
            level="STRUCTURAL_AND_MECHANICALLY_DERIVED",
            differs_from_batch_1=("Batch 1's propositions and stems were hand-authored after "
                                  "reading every unit. These eight are derived by a published "
                                  "rule from the rows themselves. The rows are the same "
                                  "quality; the analysis over them is shallower, and saying "
                                  "so is the point."),
            hand_authored_elements=[]),
        heading_tree=dict(cls="SOURCE_DERIVED", criterion=UM.STRUCTURAL_CRITERION,
                          structural_headings=len(tree), tree=tree),
        prose_styled_as_heading=dict(cls="SOURCE_DERIVED",
                                     count=len(UM.prose_styled_as_heading(ex))),
        components=dict(cls="SOURCE_DERIVED", count=len(comps), components=comps),
        grouping=dict(cls="CAIR_PROPOSAL", basis=basis, groups=groups,
                      automatic_component_detection=[c["name"] for c in comps],
                      note="A floor, not a ceiling."),
        screen_sequence=dict(cls="CAIR_PROPOSAL",
                             sequence=["S01 Topik entry", "S0x Orientasi"]
                             + [f"{g['group_id']}: {g['covers']}" for g in groups]
                             + ["Rumusan", "Kuiz", "Tamat"],
                             arithmetic=dict(
                                 shell_screens=shell, shell_includes_dialogue=False,
                                 content_groups=len(groups), closing_screens=closing,
                                 minimum_total_screens=shell + len(groups) + closing,
                                 maximum_total_screens="UNKNOWN_PENDING_PATTERN_DECISION",
                                 basis="one content screen per proposed group — a floor")),
        pattern_family=dict(cls="PENDING_BARIAH_PATTERN_DECISION",
                            primary_candidate=("click-to-reveal" if comps
                                               else "static content"),
                            secondary_candidate="comparison",
                            candidate_basis=("repeated component blocks" if comps
                                             else "no repeated component structure found"),
                            vocabulary=UM.SUPPORTED_TREATMENTS,
                            note="A candidate read off structure, not off content. The "
                                 "pattern package that would settle it is with Bariah."),
        interaction_candidates=dict(cls="CAIR_PROPOSAL",
                                    candidates=[dict(group_id=g["group_id"],
                                                     covers=g["covers"],
                                                     candidate="reveal per group detail")
                                                for g in groups]),
        runtime_state_estimate=dict(cls="CAIR_PROPOSAL",
                                    base_states_floor=shell + len(groups) + closing,
                                    triggered_states="UNKNOWN_PENDING_PATTERN_DECISION",
                                    total_runtime_states="UNKNOWN_PENDING_PATTERN_DECISION"),
        rumusan=dict(cls="PENDING_UNIT_EXCEPTION_REVIEW",
                     beat_count="UNKNOWN_NOT_AUTHORED",
                     treatment="RP-007 — this Bahagian only, contractor perspective",
                     treatment_cls="COURSE_RULE_ALREADY_APPROVED",
                     note="Beats are not drafted for these eight. Drafting them needs the "
                          "unit read end to end, which this layer did not do."),
        dialogue=dict(cls="PENDING_UNIT_EXCEPTION_REVIEW", verdict="NOT_ASSESSED",
                      reason="Whether a dialogue is justified is a content judgement and "
                             "this layer is structural. Not guessed.",
                      cast="NO_CHARACTER_PROPOSED_STOP_006_OPEN"),
        mandatory_propositions=dict(cls="SOURCE_DERIVED", derivation="OBLIGATION_MARKER",
                                    count=len(obl), propositions=obl),
        definitional_statements=dict(cls="SOURCE_DERIVED", derivation="DEFINITION_MARKER",
                                     count=len(defs), statements=defs),
        assessment=dict(cls="PENDING_UNIT_EXCEPTION_REVIEW",
                        composition="4 Multiple Choice + 1 Multiple Response",
                        composition_cls="COURSE_RULE_ALREADY_APPROVED",
                        key_status="NOT_DRAFTED",
                        key_authority="NONE — no item exists, so none is approved",
                        source_supported_propositions=len(obl) + len(defs),
                        items=[],
                        note="The propositions an item could be built on are extracted and "
                             "cited. The items themselves are not drafted."),
        visual_obligations=dict(cls="SOURCE_DERIVED",
                                count=len(vis),
                                source_attested=len([v for v in vis
                                                     if v["has_source_figure"]]),
                                subjects=vis,
                                rule="RP-104 — read from the source's own figure or table",
                                rule_cls="COURSE_RULE_ALREADY_APPROVED",
                                note="Only figures, diagrams, tables and captions actually "
                                     "present in the span. Nothing composed from a name."),
        terminology=dict(cls="SOURCE_DERIVED", count=len(terminology(ex)),
                         terms=terminology(ex)),
        extraction_qa=UM.extraction_qa(ex))


def all_models():
    ex = extract_all()
    units = {u["unit_id"]: u for u in remaining_units()}
    return {uid: model(units[uid], e) for uid, e in ex.items()}, ex


if __name__ == "__main__":
    units = remaining_units()
    print(f"remaining PL06 units derived from the frozen map: {len(units)}")
    for u in units:
        print(f"  {u['unit_id']}  {u['module_pages'][0]}-{u['module_pages'][1]}  "
              f"{u['lesson_title'][:44]}")
    models, ex = all_models()
    os.makedirs(OUT_DIR, exist_ok=True)
    for uid, e in ex.items():
        with open(os.path.join(OUT_DIR, f"{uid.replace('-', '_')}_SOURCE_EXTRACT_v1.json"),
                  "w", encoding="utf-8") as f:
            json.dump(e, f, ensure_ascii=False, indent=1)
            f.write("\n")
    for uid, m in models.items():
        with open(os.path.join(OUT_DIR, f"{uid.replace('-', '_')}_PROVISIONAL_MODEL_v1.json"),
                  "w", encoding="utf-8") as f:
            json.dump(m, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print()
    tot = 0
    for uid, m in models.items():
        e = ex[uid]
        tot += e["totals"]["content_rows"]
        pa = e["page_attribution"]
        print(f"{uid}: rows={e['totals']['content_rows']:>3} "
              f"pages={pa['first_page']}-{pa['last_page']}"
              f"{'' if pa['matches_frozen_map'] else ' PAGE MISMATCH'} "
              f"groups={len(m['grouping']['groups']):>2} "
              f"obl={m['mandatory_propositions']['count']:>3} "
              f"def={m['definitional_statements']['count']:>3} "
              f"vis={m['visual_obligations']['count']:>2} "
              f"tbl={e['totals']['tables']} img={e['totals']['raster_images']}")
    print(f"\ntotal controlled rows: {tot}")
    lk = EX.leak_report(ex, remaining_units())
    print("leak report:", "CLEAN" if lk["all_clean"] else lk)
