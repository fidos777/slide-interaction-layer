# -*- coding: utf-8 -*-
"""Stage 4.2E-C QA — the Stage 4.2E-B suite plus the metadata-conformance gates.

Every gate added here reads the generated PACKAGE and, where the obligation is an agreement
between two artifacts, the other artifact on disk. None of them is a model-only assertion:
the defect this stage corrects (B02-META-REG-001) was invisible for four releases precisely
because the checks that touched it read the generator's own constants and required the stale
value to be present.

Three surfaces are read:
    slide XML          production-panel identity and component-main governance blocks
    notes XML          stale release tokens must not survive in Speaker Notes either
    artifacts on disk  RUN_MANIFEST, COMPONENT_OVERVIEW_MAPPING, the review checklist
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "audit"))
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_4 as PRIOR
import b02_artifact_identity_v0_4_4_1 as IDENT
import b02_geometry_exemptions_v0_4_4_1 as GEX
import b02_overview_mapping_v0_4_4 as OV
from b02_proof_qa_v0_4 import read_pptx

MANIFEST = os.path.join(SRC, f"RUN_MANIFEST_{IDENT.VERSION}.json")
CHECKLIST = os.path.join(SRC, f"BARIAH_REVIEW_CHECKLIST_{IDENT.VERSION}.md")
QA_REPORT = os.path.join(SRC, f"STORYBOARD_QA_REPORT_{IDENT.VERSION}.md")
EXEMPTION_REGISTRY = os.path.join(SRC, f"GEOMETRY_EXEMPTION_REGISTRY_{IDENT.VERSION}.json")

DEFECT_RECORD = os.path.join(SRC, f"B02_DEFECT_REGISTER_{IDENT.VERSION}.md")

STALE_GOVERNANCE_STRINGS = ("CONDITIONAL", "PENDING_HUMAN", "PROVISIONAL_VISUAL_PROPOSAL")


def accounting(rows):
    """The three counts, separated by a DEFINITION rather than by a name.

    A supersession marker is an inert self-assertion: expected == actual == the constant
    "SUPERSEDED". Nothing else qualifies. Up to and including v0.4.4 this figure was taken
    by substring-matching "SUPERSEDED" in the gate ID, which swept in six gates that are
    ordinary live tests — SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL and the like.
    That under-reported the active suite by six and over-reported the markers by six.
    """
    markers = [r for r in rows if str(r[1]) == "SUPERSEDED" and str(r[2]) == "SUPERSEDED"]
    active = [r for r in rows if r not in markers]
    return dict(TOTAL_EMITTED_GATE_RECORDS=len(rows),
                SUPERSESSION_MARKERS_PRESENT=len(markers),
                ACTIVE_TEST_GATES=len(active),
                ACTIVE_TEST_GATES_PASSING=sum(1 for r in active if r[3]),
                FAILING=[r[0] for r in rows if not r[3]])


def _panel_lines(d):
    return [r for s in d["panel"] if s["name"] == "ProdPanel" for r in s["runs"]]


def _visual_block(lines):
    """The VISUAL: block of one production panel, as a dict of field -> value."""
    out, inside = {}, False
    for ln in lines:
        if ln.strip() == "VISUAL:":
            inside = True
            continue
        if inside:
            if ln and not ln.startswith("  "):
                break
            if ln.startswith("  ") and ": " in ln and not ln.startswith("    "):
                k, v = ln.strip().split(": ", 1)
                out[k] = v
    return out


def _unfenced(md):
    """Markdown prose with fenced code blocks removed."""
    out, keep = [], True
    for ln in md.split("\n"):
        if ln.startswith("```"):
            keep = not keep
            continue
        if keep:
            out.append(ln)
    return "\n".join(out)


def _load(path):
    if not os.path.exists(path):
        return None
    if path.endswith(".json"):
        return json.load(open(path, encoding="utf-8"))
    return open(path, encoding="utf-8").read()


def run(pptx):
    res = list(PRIOR.run(pptx))
    n_prior = len(res)
    def chk(k, v, e): res.append((k, v, e, v == e))

    M = ADAPT.Model(); pages = ADAPT.all_pages(M); deck = read_pptx(pptx)
    D = {p["id"]: d for p, d in zip(pages, deck)}
    plines = {pid: _panel_lines(d) for pid, d in D.items()}
    ptext = {pid: " ".join(s["text"] for s in d["panel"]) for pid, d in D.items()}
    ident = {pid: IDENT.panel_identity_from_text(plines[pid]) for pid in plines}

    # ==================== 1. PANEL IDENTITY vs THE RUN MANIFEST ====================
    man = _load(MANIFEST)
    chk("RUN_MANIFEST_PRESENT", man is not None, True)
    mid = (man or {}).get("artifact_identity") or {}
    chk("PANEL_VERSION_EQUALS_RUN_MANIFEST_VERSION",
        sorted({v for v, _ in ident.values()}) == [mid.get("artifact_version_line")]
        and mid.get("artifact_version") == IDENT.VERSION, True)
    chk("PANEL_VERSION_MANIFEST_MISMATCHES",
        sum(1 for v, _ in ident.values() if v != mid.get("artifact_version_line")), 0)
    chk("PANEL_STATUS_EQUALS_ACTIVE_PACKAGE_STATUS",
        all(t == mid.get("status_tokens") for _, t in ident.values()), True)
    chk("PANEL_STATUS_MANIFEST_MISMATCHES",
        sum(1 for _, t in ident.values() if t != mid.get("status_tokens")), 0)
    # ACTIVE_PANEL_VERSION is owned by the Stage 4 layer, which already reads it from the
    # package. Asserting it again under the same ID would collapse two records into one when
    # the replay harness indexes results by gate — the duplicate-ID failure this project has
    # already been bitten by once. DUPLICATE_GATE_IDS below now guards it for good.
    chk("MANIFEST_DECK_FILENAME_MATCHES_ARTIFACT",
        mid.get("deck_filename"), os.path.basename(pptx))

    # ==================== 2. STALE RELEASE TOKENS, PANEL AND NOTES ====================
    # STALE_RELEASE_TOKENS is owned by the Stage 4 layer; same duplicate-ID reason as above.
    chk("STALE_RELEASE_TOKENS_ANYWHERE_IN_PANEL",
        sum(1 for pid in ptext for tok in IDENT.STALE_STATUS_TOKENS if tok in ptext[pid]), 0)
    chk("STALE_RELEASE_TOKENS_IN_NOTES",
        sum(1 for pid in D for tok in IDENT.STALE_STATUS_TOKENS if tok in D[pid]["notes"]), 0)
    # Exact-line for the panel (a superseded line is a prefix of the active one); substring
    # for Notes, where no version line is ever written and any occurrence is a defect.
    chk("SUPERSEDED_VERSION_LINES_IN_PACKAGE",
        sum(1 for v, _ in ident.values() if v in IDENT.SUPERSEDED_VERSION_LINES)
        + sum(1 for pid in D for s in IDENT.SUPERSEDED_VERSION_LINES if s in D[pid]["notes"]), 0)

    # ==================== 3. CHECKLIST AND RELEASE REPORT IDENTITY ====================
    for label, path in (("CHECKLIST", CHECKLIST), ("QA_REPORT", QA_REPORT)):
        doc = _load(path)
        chk(f"{label}_PRESENT", doc is not None, True)
        chk(f"{label}_NAMES_ACTIVE_DECK", IDENT.DECK_FILENAME in (doc or ""), True)
        chk(f"{label}_CARRIES_FULL_STATUS_CONTRACT",
            all(t in (doc or "") for t in IDENT.STATUS_TOKENS), True)
        # Scoped to the document's own prose. A retired token inside a fenced block is
        # quoted evidence — the release report embeds the verbatim suite transcript, and
        # three gate IDs legitimately carry the token they forbid. Outside a fence, the
        # document is making the claim in its own voice, and that is what this forbids.
        chk(f"{label}_FREE_OF_STALE_STATUS_CLAIMS",
            sum(1 for t in IDENT.STALE_STATUS_TOKENS if t in _unfenced(doc or "")), 0)
        chk(f"{label}_STALE_TOKENS_ONLY_IN_QUOTED_BLOCKS",
            all(t not in _unfenced(doc or "") for t in IDENT.STALE_STATUS_TOKENS), True)
    # The stale strings must not vanish from the record just because the release documents
    # are barred from restating them. The defect register is where they are kept verbatim.
    dfc = _load(DEFECT_RECORD)
    chk("DEFECT_RECORD_PRESENT", dfc is not None, True)
    chk("DEFECT_RECORD_ID", "B02-META-REG-001" in (dfc or ""), True)
    chk("DEFECT_RECORD_CARRIES_VERBATIM_STALE_STRINGS",
        [t for t in IDENT.STALE_STATUS_TOKENS + IDENT.SUPERSEDED_VERSION_LINES
         if t not in (dfc or "")], [])

    # ==================== 4. COMPONENT-MAIN ACTIVE VISUAL GOVERNANCE ====================
    # Population pinned to learner_screen_id via the frozen mapping, then cross-checked
    # against what the package itself declares. Both must agree on nine.
    main_ids = set(OV.component_main_screens(M))
    bound = [p["id"] for p in pages if p["screen_id"] in main_ids]
    vb = {pid: _visual_block(plines[pid]) for pid in bound}
    mains = [pid for pid in bound
             if vb[pid].get("subjenis skrin") == "COMPONENT_MAIN_SCREEN"]
    screen_of = {p["id"]: p["screen_id"] for p in pages}
    chk("COMPONENT_MAIN_LEARNER_SCREENS", len(main_ids), 9)
    chk("COMPONENT_MAIN_BOUND_PAGES_EVALUATED", len(bound), 22)
    chk("COMPONENT_MAIN_PAGES", len(mains), 9)
    chk("COMPONENT_MAIN_PAGES_COVER_EVERY_SCREEN",
        sorted(screen_of[pid] for pid in mains), sorted(main_ids))

    chk("COMPONENT_MAIN_VISUAL_REQUIREMENT_REQUIRED",
        sum(1 for pid in mains if vb[pid].get("keperluan visual") == "REQUIRED"), 9)
    chk("COMPONENT_MAIN_REQUIREMENT_AUTHORITY",
        sorted({vb[pid].get("kuasa keperluan") for pid in mains}), ["BARIAH_DIRECT_SCREENSHOT"])
    chk("COMPONENT_MAIN_TREATMENT",
        sorted({vb[pid].get("rawatan") for pid in mains}), ["SOURCE_BOUND_OVERVIEW"])
    chk("COMPONENT_MAIN_TREATMENT_AUTHORITY",
        sorted({vb[pid].get("kuasa rawatan") for pid in mains}), ["BARIAH_DIRECT_SCREENSHOT"])
    chk("COMPONENT_MAIN_MAPPING_STATUS_RESOLVED",
        sum(1 for pid in mains if vb[pid].get("status pemetaan") == "RESOLVED"), 9)
    chk("COMPONENT_MAIN_MAPPING_COMPLETE",
        sum(1 for pid in mains if vb[pid].get("pemetaan instans") == "COMPLETE"), 9)
    chk("COMPONENT_MAIN_STATUS_RESOLVED",
        sum(1 for pid in mains if vb[pid].get("status") == "RESOLVED"), 9)
    chk("COMPONENT_MAIN_PENDING_HUMAN",
        sum(1 for pid in mains
            if vb[pid].get("menunggu keputusan manusia") != "TIDAK"), 0)
    chk("COMPONENT_MAIN_PROVISIONAL_VISUAL_PROPOSALS",
        sum(1 for pid in mains if "PROVISIONAL_VISUAL_PROPOSAL" in " ".join(plines[pid])), 0)
    chk("COMPONENT_MAIN_ACTIVE_VISUAL_GOVERNANCE_CURRENT",
        all(vb[pid].get("keperluan visual") == "REQUIRED"
            and vb[pid].get("status") == "RESOLVED"
            and vb[pid].get("rawatan") == "SOURCE_BOUND_OVERVIEW"
            and vb[pid].get("status pemetaan") == "RESOLVED"
            and vb[pid].get("pemetaan instans") == "COMPLETE"
            and vb[pid].get("menunggu keputusan manusia") == "TIDAK"
            and not any(s in " ".join(plines[pid]).replace("SUPERSEDED", "")
                        for s in STALE_GOVERNANCE_STRINGS)
            for pid in mains), True)
    # The whole VISUAL block of a component main, not just the fields named above.
    chk("COMPONENT_MAIN_STALE_GOVERNANCE_STRINGS_IN_VISUAL_BLOCK",
        sum(1 for pid in mains for s in STALE_GOVERNANCE_STRINGS
            for v in vb[pid].values() if s in v), 0)

    # Authority split. The requirement and the treatment are Bariah's; the SUBJECTS are not,
    # except the two Papan Tanda figures D4 names. A promotion is a subject claiming
    # BARIAH_DIRECT provenance the frozen mapping does not record her naming.
    promo, named = 0, 0
    for c in OV.mapping()["components"]:
        for s in c["subjects"]:
            if s["provenance"] == "BARIAH_DIRECT" and not s.get("directly_named_by_bariah"):
                promo += 1
            if s.get("directly_named_by_bariah"):
                named += 1
    chk("UNAUTHORISED_SUBJECT_AUTHORITY_PROMOTIONS", promo, 0)
    chk("SUBJECTS_DIRECTLY_NAMED_BY_BARIAH", named, 2)
    chk("COMPONENT_MAIN_SUBJECT_PROVENANCE_ON_PAGE",
        sum(1 for pid in mains if vb[pid].get("sumber subjek", "").startswith(
            "MODULE_SOURCE_ATTESTED")), 9)
    # The panel's subject count must equal the frozen cardinality for that component.
    comp_of = {p["id"]: p.get("component_id") for p in pages}
    chk("COMPONENT_MAIN_SUBJECT_COUNT_MATCHES_MAPPING",
        sum(1 for pid in mains
            if vb[pid].get("bilangan subjek overview") != str(OV.count(comp_of[pid]))), 0)

    # ==================== 5. OFF-CANVAS GEOMETRY EXEMPTION ====================
    allshapes = [s for d in D.values() for s in d["shapes"]]
    reg = _load(EXEMPTION_REGISTRY)
    chk("GEOMETRY_EXEMPTION_REGISTRY_PRESENT", reg is not None, True)
    chk("GEOMETRY_EXEMPTION_REGISTRY_MATCHES_CODE",
        (reg or {}).get("exemptions"), GEX.registry_records())
    chk("OFF_CANVAS_PLACEHOLDER_EXEMPTION_REGISTERED",
        any(e["exemption_id"] == "GEX-001" and e["requires_placeholder"]
            and e["ph_type"] == "title" and not e["learner_facing"]
            for e in GEX.OFF_CANVAS_EXEMPTIONS), True)
    chk("OFF_CANVAS_PRODUCTION_PANEL_EXEMPTION_REGISTERED",
        any(e["exemption_id"] == "GEX-002" and not e["requires_placeholder"]
            for e in GEX.OFF_CANVAS_EXEMPTIONS), True)
    # UNREGISTERED_OFF_CANVAS_EXEMPTIONS is owned by the four-edge geometry section of the
    # Stage 4.2B layer, which evaluates the same population; same duplicate-ID reason.
    # Every shape the registry actually clears, and nothing else.
    exempted = [s for s in allshapes if GEX.exemption_for(s) is not None]
    chk("EXEMPTED_SHAPES_EVALUATED", len(exempted), 200)
    chk("EXEMPTED_SHAPE_NAMES", sorted({s["name"] for s in exempted}),
        ["ProdPanel", "Title 1"])
    chk("TITLE_PLACEHOLDER_IS_A_REAL_PLACEHOLDER",
        all(s["is_placeholder"] and s["ph_type"] == "title"
            for s in allshapes if s["name"] == "Title 1"), True)
    chk("TITLE_PLACEHOLDER_PAGE_POPULATION",
        sum(1 for s in allshapes if s["name"] == "Title 1"), 100)
    # An ordinary shape sitting off-stage is never allowed: exemption_for() returns None for
    # anything that is not one of the two registered identities, so this counts the shapes
    # that escape the four-edge gate WITHOUT a registry entry.
    chk("ORDINARY_OFF_CANVAS_SHAPES_ALLOWED",
        sum(1 for s in allshapes
            if GEX.edges_outside(s) and GEX.exemption_for(s) is None), 0)

    # A duplicate gate ID silently collapses when results are indexed by gate — which is how
    # every mutation harness in this project reads them. Guarded here for the whole chain.
    ids = [r[0] for r in res]
    chk("DUPLICATE_GATE_IDS", sorted({k for k in ids if ids.count(k) > 1}), [])
    chk("STAGE_4_2E_B_SUITE_CHECKS", n_prior, 409)
    return res


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep); fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
