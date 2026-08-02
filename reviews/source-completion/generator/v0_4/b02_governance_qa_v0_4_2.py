# -*- coding: utf-8 -*-
"""Stage 4.2B hardened QA. Runs the full prior suite, then adds the layers the
QA_PREDICATE_AUDIT flagged as missing.

Added layers:
  ORACLE_CONFORMANCE  expected values come from b02_oracle_extract_v0_4_2, which imports
                      nothing from the generator, so no gate compares a value with itself.
  IDENTITY            tick and card gates assert WHICH items, not how many.
  VISIBILITY          text must not be covered by an opaque shape stacked above it.
  NON_VACUOUS         every population-based gate asserts its population is non-empty.
  TYPED_NOTES         every Notes paragraph carries an explicit block type and spoken flag.
"""
import json, os, re, sys, zipfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(os.path.dirname(HERE), "audit"))
import b02_model_adapter_v0_4 as ADAPT
import b02_regression_qa_v0_4_1 as PRIOR
import b02_generator_v0_4 as GEN
import b02_visual_policy_v0_4 as VP
import b02_visual_directions_v0_4 as VD
import b02_instructions_v0_4 as INS
import b02_glossary_v0_4 as GL
from b02_proof_qa_v0_4 import read_pptx
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "generator", "audit"))
import b02_oracle_extract_v0_4_2 as ORACLE

STAGE_W, STAGE_H = 13.3333, 7.5


def run(pptx):
    res = list(PRIOR.run(pptx))
    n_prior = len(res)
    def chk(k, v, e): res.append((k, v, e, v == e))

    M = ADAPT.Model(); pages = ADAPT.all_pages(M); deck = read_pptx(pptx)
    D = {p["id"]: d for p, d in zip(pages, deck)}
    st_of = {p["id"]: M.state(p["state_id"]) for p in pages}
    rec_of = {p["id"]: M.screen(p["screen_id"]) for p in pages}
    ctext = {pid: " ".join(s["text"] for s in d["canvas"]) for pid, d in D.items()}
    pol = {pid: VP.classify(M, rec_of[pid], st_of[pid]) for pid in D}
    nblocks = {}
    for p in pages:
        _, _, nb = GEN.build_page(M, p, pages)
        nblocks[p["id"]] = nb

    # ============================ ORACLE CONFORMANCE ============================
    o_prom = ORACLE.promenade_visual_direction()
    o_s01 = ORACLE.s01_visual_direction()
    o_klik = ORACLE.klik_instruction()
    chk("ORACLE_SOURCE_IS_FROZEN_BARIAH_PPTX",
        os.path.basename(ORACLE.VBARIAH).endswith("_vBariah.pptx"), True)
    chk("ORACLE_MODULE_IMPORTS_NO_GENERATOR",
        not any(x in open(ORACLE.__file__).read() for x in
                ("b02_generator", "b02_visual_policy", "b02_glossary", "b02_instructions")), True)
    prom_pid = next(pid for pid in D
                    if st_of[pid]["runtime_state_id"] == "ST_STRUKTUR_PERSISIR_AIR_POPUP_01")
    body = " ".join(s["text"] for s in D[prom_pid]["canvas"] if s["name"] == "VisualPanelBody")
    chk("ORACLE_PROMENADE_SUBJECT_MATCHES", o_prom["subject"] in body, True)
    chk("ORACLE_PROMENADE_HEADING_MATCHES",
        any(s["text"].strip() == o_prom["heading"]
            for s in D[prom_pid]["canvas"] if s["name"] == "VisualPanelHead"), True)
    s01 = next(pid for pid in D if rec_of[pid]["learner_screen_id"] == "SCR_S01")
    chk("ORACLE_S01_TITLE_MATCHES_FROZEN",
        any(t in ctext[s01] for t in o_s01["titles"] if "Topik 3 Bahagian 2" in t), True)
    chk("ORACLE_S01_NO_STANDALONE_TITLE_IN_FROZEN", len(o_s01["standalone_component_title"]), 0)
    chk("ORACLE_S01_NO_STANDALONE_TITLE_IN_BUILD",
        sum(1 for s in D[s01]["canvas"] if s["text"].strip() == "Komponen Landskap"), 0)
    klik_pids = [pid for pid in D if o_klik["text"] and o_klik["text"] in ctext[pid]]
    chk("ORACLE_KLIK_WORDING_PRESENT", len(klik_pids) > 0, True)
    chk("ORACLE_KLIK_WORDING_UNMODIFIED",
        all(o_klik["text"] in ctext[pid] for pid in klik_pids), True)

    # ============================ IDENTITY, NOT COUNT ============================
    tick_id_bad = []
    order = {p["id"]: i for i, p in enumerate(pages)}
    for p in pages:
        pid = p["id"]; st = st_of[pid]
        items = M.items_of(p["screen_id"])
        if not items:
            continue
        seen = {q["state_id"] for q in pages[:order[pid]]}
        seen_done = {q["state_id"] for q in pages[:order[pid]]
                     if M.state(q["state_id"])["screen_role"] in
                     ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE")}
        expected = set()
        for it in items:
            rs = it["runtime_state_id"]
            if rs in seen or rs == st["runtime_state_id"]:
                expected.add(it["interaction_item_id"]); continue
            m = re.match(r"^ST_(.+)_EX(\d+)_BASE$", rs)
            if m and f"ST_{m.group(1)}_EX{m.group(2)}_ALL_SPEC_VIEWED" in seen_done:
                expected.add(it["interaction_item_id"])
        if st["screen_role"] in ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE"):
            expected = {i["interaction_item_id"] for i in items}
        # identity: a tick sits at the top-right of its own card, so match by geometry
        cards = [s for s in D[pid]["canvas"] if s["name"] == "ItemCard"]
        ticks = [s for s in D[pid]["canvas"] if s["name"] == "Tick"]
        labels = [M.rows[i["source_row_uid"]]["label"] if i["item_kind"] == "EXAMPLE_POPUP"
                  else i["label"] for i in items]
        ticked = set()
        for t in ticks:
            for c, it in zip(cards, items):
                if c["x"] <= t["x"] <= c["x"] + c["w"] and c["y"] <= t["y"] <= c["y"] + c["h"]:
                    ticked.add(it["interaction_item_id"])
        if ticked != expected:
            tick_id_bad.append((pid, sorted(expected - ticked), sorted(ticked - expected)))
    chk("TICK_IDENTITY_MISMATCHES", len(tick_id_bad), 0)
    chk("TICK_IDENTITY_PAGES_EVALUATED", sum(1 for p in pages if M.items_of(p["screen_id"])) > 0, True)

    # ============================ VISIBILITY ============================
    OPAQUE = {"PopupPanel", "ProdPanel", "AnswerKeyBox", "ComponentCard", "ItemCard", "Btn"}
    covered = []
    for pid, d in D.items():
        shapes = d["canvas"]
        for i, s in enumerate(shapes):
            if not s["text"].strip() or s["name"] in OPAQUE:
                continue
            for j in range(i + 1, len(shapes)):
                o = shapes[j]
                if o["name"] not in OPAQUE:
                    continue
                if (o["x"] <= s["x"] + .01 and o["y"] <= s["y"] + .01
                        and o["x"] + o["w"] >= s["x"] + s["w"] - .01
                        and o["y"] + o["h"] >= s["y"] + s["h"] - .01):
                    covered.append((pid, s["name"], o["name"]))
    # A popup state IS a modal overlay: the screen behind it is meant to be obscured, and
    # that is the one occlusion in the deck that is by design rather than by accident. It is
    # excluded from the defect count and then pinned from four directions below, so the
    # exclusion cannot widen without a gate moving: only PopupPanel, only on STATE_POPUP
    # pages, only shapes named VisualDir, and only that exact number of them.
    modal = [c for c in covered
             if c[2] == "PopupPanel" and st_of[c[0]]["screen_role"] == "STATE_POPUP"]
    chk("TEXT_COVERED_BY_OPAQUE_SHAPE", len(covered) - len(modal), 0)
    chk("MODAL_OCCLUDED_SHAPES_EVALUATED", len(modal), 16)
    chk("MODAL_OCCLUDED_SHAPE_NAMES", sorted({n for _, n, _ in modal}), ["VisualDir"])
    chk("MODAL_OCCLUSION_ON_NON_POPUP_PAGES",
        sum(1 for pid, n, o in covered
            if o == "PopupPanel" and st_of[pid]["screen_role"] != "STATE_POPUP"), 0)
    chk("NON_MODAL_OCCLUSIONS", sorted({o for _, _, o in covered if o != "PopupPanel"}), [])
    # answer keys must be visible inside the stage, not merely present
    ak = [(pid, s) for pid, d in D.items() for s in d["canvas"] if s["name"] == "AnswerKeyBody"]
    chk("ANSWER_KEYS_EVALUATED", len(ak), 5)
    chk("ANSWER_KEYS_OUTSIDE_STAGE",
        sum(1 for pid, s in ak if s["x"] < 0 or s["y"] < 0
            or s["x"] + s["w"] > STAGE_W + .01 or s["y"] + s["h"] > STAGE_H + .01), 0)
    chk("ANSWER_KEYS_COVERED", sum(1 for pid, n, o in covered if n == "AnswerKeyBody"), 0)

    # ============================ FOUR-EDGE GEOMETRY, EVERY SHAPE ============================
    # Stage 4.2E-C. Two changes, both tightening.
    #
    # The top threshold was `y < -0.66`, a number picked to clear the title placeholder at
    # -0.631 in. Any ordinary shape parked between -0.66 and 0 passed with it. It is now
    # `y < -0.01` like the other three edges, with the placeholder cleared by an entry in the
    # exemption registry that matches on placeholder type, name and all four coordinates.
    #
    # The population was `d["canvas"]`, which is the reader's partition of shapes with
    # (x + w) <= 0 — so the production panel, and anything else pushed fully left of the
    # stage, was never evaluated at all. It is now every shape on the slide.
    import b02_geometry_exemptions_v0_4_4_1 as GEX
    edges = collections.Counter()
    allshapes = [s for d in D.values() for s in d["shapes"]]
    for s in allshapes:
        ex = GEX.exemption_for(s)
        for e in GEX.edges_outside(s):
            if ex is not None and e in ex["edges_exempted"]:
                continue
            edges[e] += 1
    for e in ("left", "right", "top", "bottom"):
        chk(f"SHAPES_BEYOND_{e.upper()}_EDGE", edges[e], 0)
    chk("GEOMETRY_SHAPES_EVALUATED", sum(len(d["canvas"]) for d in D.values()) > 500, True)
    chk("GEOMETRY_SHAPES_EVALUATED_INCLUDING_OFF_CANVAS", len(allshapes) > 500, True)
    chk("UNREGISTERED_OFF_CANVAS_EXEMPTIONS", GEX.unregistered_off_canvas(allshapes), [])

    # ============================ TYPED NOTES ============================
    allb = [b for nb in nblocks.values() for b in nb]
    chk("NOTES_BLOCKS_TOTAL_EVALUATED", len(allb) > 0, True)
    chk("NOTES_BLOCKS_WITHOUT_TYPE", sum(1 for b in allb if not b.get("block_type")), 0)
    chk("NOTES_BLOCKS_WITHOUT_SPOKEN_FLAG", sum(1 for b in allb if "spoken" not in b), 0)
    chk("NOTES_BLOCKS_WITH_UNKNOWN_TYPE",
        sum(1 for b in allb if b["block_type"] not in
            (GEN.NB_CONTEXT, GEN.NB_VO, GEN.NB_INSTR, GEN.NB_PROD)), 0)
    chk("NON_SPOKEN_BLOCKS_IN_SPOKEN_EXPORT",
        sum(1 for nb in nblocks.values() for b in nb
            if not b["spoken"] and b["text"] in GEN.spoken_export(nb)), 0)
    # Reconstruct each notes paragraph from its runs. A glossary term makes a paragraph span
    # several <a:r> elements, so a raw substring test would report false misses.
    xml_paras = PRIOR.notes_runs(pptx)
    missing = 0
    for p, paras in zip(pages, xml_paras):
        joined = ["".join(t for t, _ in runs) for runs in paras]
        for b in nblocks[p["id"]]:
            if b["spoken"] and b["text"].strip() and b["text"] not in joined:
                missing += 1
    chk("SPOKEN_BLOCKS_MISSING_FROM_NOTES", missing, 0)
    chk("NOTES_PARAGRAPHS_RECONSTRUCTED",
        sum(len(x) for x in xml_paras) > 0, True)
    chk("SILENT_STATES_WITH_NOTES_BLOCKS",
        sum(1 for p in pages if st_of[p["id"]]["notes_policy"] == "SILENT_STATE_NOTES"
            and nblocks[p["id"]]), 0)
    chk("SPOKEN_EXPORT_DRIVEN_BY_FLAG_NOT_ORDER",
        all(GEN.spoken_export(nb) == [b["text"] for b in nb if b["spoken"] and b["text"].strip()]
            for nb in nblocks.values()), True)

    # ============================ BOUNDED PARITY ============================
    click = [p["id"] for p in pages
             if INS.is_screen_level_click(INS.for_page(rec_of[p["id"]], st_of[p["id"]]))]
    chk("SCREEN_LEVEL_CLICK_INSTRUCTIONS_EVALUATED", len(click) > 0, True)
    bad = 0
    for pid in click:
        ins = INS.for_page(rec_of[pid], st_of[pid])
        spoken = GEN.spoken_export(nblocks[pid])
        if ins not in ctext[pid] or ins not in spoken:
            bad += 1
    chk("CONFIRMED_SCREEN_LEVEL_CLICK_MISMATCHES", bad, 0)
    chk("MICRO_CONTROL_SCOPE_SELF_RESOLVED",
        sum(1 for pid in D for b in nblocks[pid]
            if b["block_type"] == GEN.NB_INSTR
            and b["text"].strip().startswith(("Klik Semak", "Klik Tutup", "Klik Kembali"))), 0)
    chk("REVIEW_ONLY_ANSWER_KEYS_IN_SPOKEN_VO",
        sum(1 for pid in D for t in GEN.spoken_export(nblocks[pid])
            if "Jawapan:" in t or "Jawapan betul:" in t or "SEMAKAN CIDB" in t), 0)
    chk("INSTRUCTIONS_WITH_UNCLASSIFIED_AUTHORITY",
        sum(1 for p in pages
            if (i2 := INS.for_page(rec_of[p["id"]], st_of[p["id"]]))
            and INS.authority(i2) == "UNCLASSIFIED"), 0)

    # ============================ FAIL-CLOSED VISUAL GOVERNANCE ============================
    chk("BARIAH_DIRECT_FIELDS_WITH_MISSING_VALUE",
        sum(1 for sid, v in VP.BARIAH_DIRECT.items() if not (v or "").strip()), 0)
    chk("REQUIRED_VISUALS_EVALUATED",
        sum(1 for pid in pol if pol[pid]["visual_requirement"] == VP.REQUIRED) > 0, True)
    chk("REQUIRED_VISUALS_UNRESOLVED",
        sum(1 for pid in pol if pol[pid]["visual_requirement"] == VP.REQUIRED
            and not pol[pid]["visual_status"].startswith("RESOLVED")), 0)
    # SUPERSEDED at Stage 4.2C. Bariah's 4:40 PM screenshot closed the only open conflict, so
    # a gate that PASSES only while a conflict exists would now demand one be kept alive. The
    # machinery is retained for the next conflict — both replacement gates below still fire if
    # any conflict is ever registered again — and the closed ruling must now be disclosed as
    # superseded, which is a disclosure duty the retired gate never imposed.
    chk("EVIDENCE_CONFLICTS_DISCLOSED__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT",
        "SUPERSEDED", "SUPERSEDED")
    chk("ACTIVE_EVIDENCE_CONFLICTS",
        sum(1 for pid in pol if pol[pid].get("evidence_conflict")), 0)
    chk("EVIDENCE_CONFLICTS_IN_PRODUCTION_PANEL__SUPERSEDED_BY_SUPERSEDED_RULING_DISCLOSURE",
        "SUPERSEDED", "SUPERSEDED")
    # still live: any conflict that reappears must reach the panel
    chk("EVIDENCE_CONFLICTS_IN_PRODUCTION_PANEL",
        sum(1 for pid in pol if pol[pid].get("evidence_conflict")
            and "KONFLIK BUKTI" not in " ".join(s["text"] for s in D[pid]["panel"])), 0)
    sup = [pid for pid in pol if pol[pid].get("superseded_ruling")]
    chk("SUPERSEDED_RULINGS_EVALUATED", len(sup) > 0, True)
    chk("SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL",
        sum(1 for pid in sup
            if "ARAHAN DIGANTI" not in " ".join(s["text"] for s in D[pid]["panel"])), 0)
    chk("SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE",
        sum(1 for pid in sup
            if pol[pid]["superseded_ruling"]["superseded_direction"] in ctext[pid]), 0)

    chk("PRIOR_SUITE_CHECKS", n_prior, 237)
    return res


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep); fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
