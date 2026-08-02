# -*- coding: utf-8 -*-
"""Emits the T04 pre-storyboard decision pack from one controlled data source.

    python3 docs/pl06/t04/tools/t04_pack_emit_v1.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_pack_data_v1 as P

OUT = os.path.dirname(HERE)
BANNER = ("> **Every proposal below is `CAIR_ASSISTED_DRAFT` / `PENDING_BARIAH_REVIEW`.** "
          "Bariah is the sole Instructional Designer and the only approval authority. CAIR "
          "prepared the source analysis, the mapping and the drafts; none of it is approved "
          "instructional content and none of it may be treated as an ID decision.")


def _c(v):
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (list, tuple)):
        return "; ".join(str(x) for x in v) or "—"
    return str(v)


def _tbl(h, rows):
    o = ["| " + " | ".join(h) + " |", "|" + "|".join("---" for _ in h) + "|"]
    for r in rows:
        o.append("| " + " | ".join(_c(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return "\n".join(o)


def mapping_json():
    return json.dumps(dict(
        pack="T04_SOURCE_TO_SCREEN_MAPPING", version="v1", stage=P.STAGE, unit_id=P.UNIT_ID,
        content_status=P.CONTENT_STATUS, approval_status=P.APPROVAL_STATUS,
        instructional_authority=P.INSTRUCTIONAL_AUTHORITY, roles=P.ROLES,
        screen_count_claim=P.SCREEN_COUNT_CLAIM, treatment_statuses=P.TREATMENT_STATUSES,
        screens=P.MAPPING), ensure_ascii=False, indent=1)


def contracts_json():
    return json.dumps(dict(
        pack="T04_SCREEN_CONTRACTS_DRAFT", version="v1", stage=P.STAGE, unit_id=P.UNIT_ID,
        content_status=P.CONTENT_STATUS, approval_status=P.APPROVAL_STATUS,
        instructional_authority=P.INSTRUCTIONAL_AUTHORITY,
        contracts=P.CONTRACTS), ensure_ascii=False, indent=1)


def mapping_md():
    L = ["# T04_SOURCE_TO_SCREEN_MAPPING — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"UNIT               = {P.UNIT_ID}",
         f"SCREEN CANDIDATES  = {len(P.MAPPING)}",
         f"FINAL SCREEN COUNT = {P.SCREEN_COUNT_CLAIM['final_screen_count']}",
         f"CONTENT STATUS     = {P.CONTENT_STATUS}",
         f"APPROVAL STATUS    = {P.APPROVAL_STATUS}",
         "B02_FAMILIES_PROPAGATED = 0", "```", "", BANNER, "",
         "# Role ownership", "",
         _tbl(["role", "owns"], [[k, "; ".join(v)] for k, v in P.ROLES.items()]), "",
         "# Why no screen count is claimed", "", P.SCREEN_COUNT_CLAIM["reason"], "",
         "# Mapping", ""]
    L.append(_tbl(["candidate", "working title", "treatment", "status", "source rows",
                   "visual dep", "Bariah decision"],
                  [[f"`{m['screen_candidate_id']}`", m["working_title"],
                    m["proposed_treatment"], f"`{m['treatment_status']}`",
                    str(len(m["source_row_ids"])), m["source_visual_dependency"][:24],
                    m["bariah_decision_required"]] for m in P.MAPPING]))
    L += ["", "# Detail", ""]
    for m in P.MAPPING:
        L += [f"## `{m['screen_candidate_id']}` — {m['working_title']}", "",
              _tbl(["field", "value"], [[k, v] for k, v in m.items()
                                        if k != "screen_candidate_id"]), ""]
    return "\n".join(L)


def contracts_md():
    L = ["# T04_SCREEN_CONTRACTS_DRAFT — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"CONTRACTS = {len(P.CONTRACTS)}",
         "PROCESS_FLOW 1 · CLICK_TO_REVEAL 2 · SEQUENTIAL_STEPS 1 · COMPARISON 1 · "
         "PENDING_HUMAN 1",
         f"APPROVAL  = {P.APPROVAL_STATUS}", "```", "", BANNER, "",
         "# The reveal rule", "",
         "Both `CLICK_TO_REVEAL` contracts hide **supplementary description only**. Every "
         "legal, safety and compliance obligation in this unit — all eleven source rows — "
         "sits on `T04-CT-04` and is **visible in the base state**. A learner who never "
         "interacts with anything still sees every obligation. That separation is deliberate "
         "and is held by the gate `LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL`.", ""]
    for c in P.CONTRACTS:
        L += [f"# `{c['contract_id']}` — {c['candidate_type']}", "",
              _tbl(["field", "value"],
                   [[k, v] for k, v in c.items()
                    if k not in ("contract_id", "candidate_type", "options", "bariah_approval")]),
              ""]
        if c.get("options"):
            L += ["**Options — no treatment is chosen here.**", "",
                  _tbl(["option", "proposal", "source grounding", "trade-off"],
                       [[o["option"], o["label"], o["grounding"], o["tradeoff"]]
                        for o in c["options"]]), ""]
        L += [_tbl(["Bariah approval", "value"],
                   [["status", c["bariah_approval"]["status"]],
                    ["decision", "☐ accept  ☐ amend  ☐ reject"],
                    ["comment", "_________________________"]]), ""]
    return "\n".join(L)


def smartart_md():
    S = P.SMARTART
    L = ["# T04_SMARTART_SIX_NODE_CONTRACT — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"ASSET  = {S['asset_id']}", f"NODES  = {S['node_count']}",
         f"FLOW   = {S['directional_flow']}", "HIERARCHY = NONE",
         f"SMARTART_TREATMENT_STATUS = {S['treatment_status']}", "```", "", BANNER, "",
         "# 1. Asset identity", "",
         _tbl(["field", "value"],
              [["asset_id", f"`{S['asset_id']}`"], ["SHA-256", f"`{S['asset_sha256']}`"],
               ["relationship IDs", f"`{S['relationship_id']}`"],
               ["embedded part", f"`{S['embedded_part']}`"],
               ["source page", f"modul ms {S['source_page']}"],
               ["source paragraph", S["source_paragraph"]],
               ["source row", f"`{S['source_row']}`"],
               ["original dimensions", f"{S['original_dimensions_in']} in"],
               ["caption", S["caption"]], ["source authority", S["source_authority"]]]), "",
         "# 2. The six nodes, in source order", ""]
    L.append(_tbl(["#", "raw node text"],
                  [[i + 1, n] for i, n in enumerate(S["nodes"])]))
    L += ["", _tbl(["property", "measured value"],
                   [["node sequence", S["node_sequence"]],
                    ["directional flow", f"**{S['directional_flow']}**"],
                    ["flow evidence", S["flow_evidence"]],
                    ["connectors", S["connectors"]],
                    ["hierarchy", f"**{S['hierarchy']}**"]]), "",
          "The flat structure matters: nothing in the source subordinates one activity to "
          "another, so a redraw must not introduce a tree, a cycle or a grouping.", "",
          "# 3. Treatment A — review storyboard", "",
          _tbl(["field", "value"],
               [["approach", S["review_storyboard_treatment"]["approach"]],
                ["asset production", S["review_storyboard_treatment"]["asset_production"]]]), ""]
    for r in S["review_storyboard_treatment"]["rules"]:
        L.append(f"- {r}")
    L += ["", "# 4. Treatment B — future MMD", "",
          _tbl(["field", "value"],
               [["approach", S["future_mmd_treatment"]["approach"]],
                ["asset production", S["future_mmd_treatment"]["asset_production"]]]), ""]
    for r in S["future_mmd_treatment"]["rules"]:
        L.append(f"- {r}")
    L += ["", f"```\nSMARTART_TREATMENT_STATUS = {S['treatment_status']}\n```", ""]
    return "\n".join(L)


def rumusan_md():
    R = P.RUMUSAN
    L = ["# T04_RUMUSAN_CAIR_ASSISTED_DRAFT — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"content_status          = {R['content_status']}",
         f"instructional_authority = {R['instructional_authority']}",
         f"approval_status         = {R['approval_status']}",
         f"statements              = {len(R['statements'])}", "```", "",
         "> **The module contains no Rumusan.** Not for T04 and not for any unit — zero hits "
         "for `Rumusan` across all 6,167 body paragraphs. What follows is a CAIR-assisted "
         "draft compressed from rows already in the controlled extract. **It did not come "
         "from the module**, it is not approved, and Bariah is its author of record.", "",
         "Provenance rule applied: " + R["provenance"], "",
         "# Draft statements", ""]
    for s in R["statements"]:
        L += [f"## `{s['statement_id']}`", "", f"> {s['draft_text']}", "",
              _tbl(["field", "value"],
                   [["supporting source rows", ", ".join(f"`{r}`" for r in s["source_row_ids"])],
                    ["source heading", s["source_heading"]],
                    ["reason for inclusion", s["reason_for_inclusion"]],
                    ["simplification applied", s["simplification_applied"]],
                    ["factual-risk status", f"**{s['factual_risk_status']}**"]]), ""]
    L += ["# Bariah review table", "", R["length_note"], "",
          _tbl(["statement", "accept", "edit", "remove", "comment"],
               [[f"`{s['statement_id']}`", "☐", "☐", "☐", "_______________"]
                for s in R["statements"]]), "",
          "One statement deserves a second look: **`T04-RUM-03`** is marked "
          "`MEDIUM` factual risk because it states as a general rule a pattern the source "
          "repeats three times but never generalises. If that reads as overreach, it should "
          "be cut or narrowed.", ""]
    return "\n".join(L)


def quiz_md():
    Q = P.QUIZ
    L = ["# T04_QUIZ_BLUEPRINT — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"QUIZ_STRUCTURE = {Q['quiz_structure']}",
         f"QUIZ_CONTENT   = {Q['quiz_content']}",
         f"FINAL_AUTHOR   = {Q['final_author']}", "```", "",
         "> **No question was written.** This is coverage analysis, not a quiz. Deliberately "
         "not produced: " + ", ".join(Q["not_produced"]) + ".", "",
         "# Coverage blueprint", ""]
    L.append(_tbl(["id", "learning point", "source rows", "type", "demand", "misconception",
                   "suitability", "Bariah decision"],
                  [[f"`{b['blueprint_id']}`", b["learning_point"],
                    ", ".join(f"`{r}`" for r in b["source_rows"]),
                    b["proposed_question_type"], b["cognitive_demand"],
                    b["misconception_to_test"], b["suitability"],
                    b["bariah_decision_required"]] for b in Q["blueprint"]]))
    L += ["", "# Evidence for each correct answer", "",
          _tbl(["id", "evidence in source"],
               [[f"`{b['blueprint_id']}`", b["evidence_for_correct_answer"]]
                for b in Q["blueprint"]]), "",
          "# Two structures for Bariah to choose from", ""]
    for o in Q["structure_options"]:
        L += [f"## Option {o['option']} — {o['label']}", "",
              _tbl(["", ""], [["advantages", o["advantages"]],
                              ["constraints", o["constraints"]]]), ""]
    L += ["Six blueprint points against a five-item quiz is the tension. Option A requires "
          "cutting one; Option B requires a rule for how structure is derived. Neither is "
          "chosen here.", "",
          "```", f"QUIZ_STRUCTURE = {Q['quiz_structure']}",
          f"QUIZ_CONTENT   = {Q['quiz_content']}", "```", ""]
    return "\n".join(L)


def decisions_md():
    L = ["# T04_BARIAH_DECISION_PACK — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"DECISIONS = {len(P.DECISIONS)}", "APPROVED = 0", "```", "", BANNER, "",
         "Five decisions. None is answered by the module — that is why they are here.", ""]
    for d in P.DECISIONS:
        L += [f"# `{d['decision_id']}` — {d['title']}", "",
              _tbl(["field", "value"],
                   [["source evidence", d["current_source_evidence"]],
                    ["**recommendation**", f"**{d['recommendation']}**"],
                    ["alternative", d["alternative"]],
                    ["consequence — recommended", d["consequence_recommended"]],
                    ["consequence — alternative", d["consequence_alternative"]],
                    ["scope", f"**{d['scope']}**"],
                    ["affected screens", ", ".join(d["affected_screens"])]]), "",
              _tbl(["approval", "comments"],
                   [["☐ accept   ☐ amend   ☐ reject", "_______________________________"]]), ""]
    L += ["# A note on scope", "",
          "`D-03` is recommended **for this unit only** and must not be read as a PL06-global "
          "cast decision. T04 is procedural content with no dialogue scenario in the source, "
          "which makes it a poor place to settle a cast question for the whole Pakej Latihan. "
          "`D-02` is the opposite — it is asked precisely because the answer may be "
          "PL06-wide.", ""]
    return "\n".join(L)


def whatsapp_md():
    L = ["# T04_BARIAH_WHATSAPP_DRAFT — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`. **Not sent.**", "",
         "Draft message, Malay, ready to copy. Recommendations are stated plainly; nothing "
         "is presented as decided.", "", "```text",
         "Salam Bariah,", "",
         "Sumber untuk Topik 4 Bahagian 1 (Penjagaan dan Penyelenggaraan, modul ms 276–283)",
         "sudah siap diekstrak sepenuhnya daripada modul. Semua kandungan sudah dipetakan.",
         "", "Ada 5 perkara yang modul sendiri tidak jawab, jadi perlukan keputusan Bariah:",
         "",
         "1. VISUAL — Topik ini tiada gambar langsung. Hanya ada satu rajah proses",
         "   (6 kotak) di permulaan. Cadangan kami: guna teks + rajah sahaja, tanpa gambar.",
         "   Setuju?",
         "",
         "2. KUIZ — Modul tiada soalan kuiz langsung, untuk mana-mana topik. Format",
         "   4 MCQ + 1 MR dan lulus 60% itu datang daripada dokumen B02 sahaja. Perlu",
         "   Bariah sahkan sama ada format itu untuk seluruh PL06 atau khusus B02 dahulu.",
         "",
         "3. WATAK — Cadangan kami: guna Hilmi sebagai narator sahaja, tiada watak tambahan",
         "   untuk T04. Kandungan ini prosedur, tiada babak dialog dalam sumber.",
         "",
         "4. KANDUNGAN PERUNDANGAN — Ada bahagian racun yang melibatkan Akta, lesen",
         "   pengendali, PPE dan SDS. Cadangan kami: semua kewajipan ini nampak terus di",
         "   skrin, tidak disembunyikan di belakang klik. Penerangan tambahan boleh guna klik.",
         "",
         "5. RAJAH PROSES — Cadangan kami: rujuk rajah asal dalam papan cerita, dan MMD",
         "   lukis semula kemudian. Urutan 6 kotak kekal sama.",
         "", "Dua perkara penting:", "",
         "• RUMUSAN — Modul tiada rumusan. Kami sediakan draf 5 ayat sebagai cadangan",
         "  sahaja, diambil terus daripada isi sumber. Ini bukan rumusan muktamad —",
         "  Bariah yang tentukan dan boleh pinda atau buang.",
         "",
         "• KUIZ — Kami tidak tulis sebarang soalan. Yang disediakan hanya senarai topik",
         "  yang boleh diuji berserta rujukan sumber. Soalan sebenar Bariah yang tulis.",
         "",
         "Boleh Bariah sahkan atau pinda mana-mana daripada 5 perkara di atas? Selepas itu",
         "kami boleh mula bina papan cerita T04.", "",
         "Terima kasih.",
         "```", "",
         "**Not sent.** Sending is Firdaus's call.", ""]
    return "\n".join(L)


def portability_md():
    T = P.PORTABILITY_TEMPLATE
    L = ["# T04_PORTABILITY_MEASUREMENT_TEMPLATE — v1", "",
         f"Stage {P.STAGE}. Generated from `{P.GENERATED_BY}`.", "", "```",
         f"STATUS = {T['status']}", f"SCORE  = {T['score']}", "```", "",
         "> **Nothing here is measured yet.** This template is completed *after* the T04 "
         "storyboard is generated. " + T["rule"], "",
         "# Measurements", "",
         _tbl(["metric", "value", "basis"],
              [[r["metric"], f"`{r['value']}`", r["basis"] or "—"] for r in T["rows"]]), "",
         "# Portability score bands", "",
         _tbl(["score", "meaning"], [[b, m] for b, m in P.PORTABILITY_BANDS]), "",
         "```", f"SCORE = {T['score']}", "```", "",
         "The score is what will tell us whether the B02 investment generalises. One early "
         "signal is already in hand and it is not encouraging for visual reuse: T04 has one "
         "visual against B02's fourteen, so the visual-treatment reuse percentage is likely "
         "to be the lowest row in this table. That is a prediction, not a measurement, and it "
         "is written here as a prediction.", ""]
    return "\n".join(L)


FILES = [
    ("T04_SOURCE_TO_SCREEN_MAPPING_v1.md", mapping_md),
    ("T04_SOURCE_TO_SCREEN_MAPPING_v1.json", mapping_json),
    ("T04_SCREEN_CONTRACTS_DRAFT_v1.md", contracts_md),
    ("T04_SCREEN_CONTRACTS_DRAFT_v1.json", contracts_json),
    ("T04_SMARTART_SIX_NODE_CONTRACT_v1.md", smartart_md),
    ("T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v1.md", rumusan_md),
    ("T04_QUIZ_BLUEPRINT_v1.md", quiz_md),
    ("T04_BARIAH_DECISION_PACK_v1.md", decisions_md),
    ("T04_BARIAH_WHATSAPP_DRAFT_v1.md", whatsapp_md),
    ("T04_PORTABILITY_MEASUREMENT_TEMPLATE_v1.md", portability_md),
]


def write(outdir=OUT):
    out = []
    for n, fn in FILES:
        b = fn()
        if not b.endswith("\n"):
            b += "\n"
        p = os.path.join(outdir, n)
        open(p, "w", encoding="utf-8").write(b)
        out.append(p)
    return out


if __name__ == "__main__":
    for p in write():
        print("wrote", os.path.relpath(p))
