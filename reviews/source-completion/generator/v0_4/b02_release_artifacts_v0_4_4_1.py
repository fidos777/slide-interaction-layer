# -*- coding: utf-8 -*-
"""Emits the machine-readable release artifacts for v0.4.4.1 from the controlled sources.

Nothing here restates a version string, a status token or an exemption by hand — that is
the whole point of Stage 4.2E-C. Run after the deck is generated:

    python3 b02_release_artifacts_v0_4_4_1.py <source-completion-dir>
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "audit"))
import b02_artifact_identity_v0_4_4_1 as IDENT
import b02_geometry_exemptions_v0_4_4_1 as GEX
import b02_overview_mapping_v0_4_4 as OV
import b02_model_adapter_v0_4 as ADAPT


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


TOOLCHAIN_V0_3 = [
    "b02_content_v0_3.py", "b02_content_v0_3.json", "b02_model_v0_3.py",
    "b02_generator_v0_3.py", "b02_render_check.py", "b02_qa_v0_3.py", "b02_docs_v0_3.py",
]

RETAINED = [
    "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3.pptx",
    "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx",
    "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx",
    "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_2.pptx",
    "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx",
    "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4.pptx",
]

EVIDENCE_DIR = "reviews/storyboard-bariah/v0_3_bariah_review"
EVIDENCE = [
    "B02_BARIAH_S01_EVIDENCE.jpg",
    "B02_BARIAH_STRUKTUR_PERSISIR_EVIDENCE.jpg",
    "B02_BARIAH_VISUAL_POLICY_EVIDENCE.png",
    "B02_BARIAH_DECISION_TAMBAHAN_TEXT.png",
    "B02_BARIAH_DECISION_VISUAL_PERSISTENCE.png",
    "B02_BARIAH_DECISION_CAST_QUIZ_VO_PUNCTUATION.png",
    "B02_BARIAH_DECISION_OVERVIEW_CARDINALITY_20260802.png",
]


def geometry_registry():
    return dict(
        registry="GEOMETRY_EXEMPTION_REGISTRY",
        artifact_version=IDENT.VERSION,
        stage="4.2E-C",
        outcome="B_UNREGISTERED_GEOMETRY_EXEMPTION_NOW_REGISTERED",
        rule=("A shape outside the 13.3333 x 7.5 in stage fails the four-edge geometry gate "
              "unless an entry below matches its placeholder-ness, placeholder type, shape "
              "name and all four coordinates to 0.001 in, AND the edge it crosses is one the "
              "entry exempts. Naming a shape after an exempt one, or moving an exempt shape, "
              "matches nothing."),
        prior_mechanism=dict(
            title_placeholder="ad hoc numeric threshold `y < -0.66` in the four-edge gate",
            production_panel="excluded by the reader's (x + w) <= 0 canvas/panel partition, "
                             "which the four-edge gate never iterated past",
            classification="UNREGISTERED_GEOMETRY_EXEMPTION"),
        exemptions=GEX.registry_records())


def artifact_identity_registry():
    return dict(registry="ARTIFACT_IDENTITY_AND_VERSION",
                controlled_source="generator/v0_4/b02_artifact_identity_v0_4_4_1.py",
                defect_corrected="B02-META-REG-001",
                consumers=["production panel (b02_generator_v0_4.prodpanel_v4)",
                           f"RUN_MANIFEST_{IDENT.VERSION}.json",
                           "b02_full_qa_v0_4 (package identity gates)",
                           "b02_governance_qa_v0_4_4_1 (manifest agreement gates)",
                           f"BARIAH_REVIEW_CHECKLIST_{IDENT.VERSION}.md",
                           f"STORYBOARD_QA_REPORT_{IDENT.VERSION}.md"],
                panel_lines=IDENT.panel_head_lines(),
                **IDENT.manifest_identity())


def package_status_contract():
    return dict(contract="ACTIVE_PACKAGE_STATUS",
                artifact_version=IDENT.VERSION,
                status_tokens=list(IDENT.STATUS_TOKENS),
                meaning={
                    "REVIEW_CANDIDATE":
                        "offered for review; not accepted, not frozen",
                    "FINAL_BARIAH_DECISIONS_IMPLEMENTED":
                        "every decision frozen at Stage 4.2E-A is built into this package",
                    "INSTANCE_MAPPING_COMPLETE":
                        "9/9 component-main overview mappings resolved, 0 ambiguous",
                    "READY_FOR_MICROSOFT_POWERPOINT_SMOKE":
                        "the next step is opening it in Microsoft PowerPoint; that has not "
                        "happened and no equivalence is claimed",
                    "NOT_FOR_MMD_BUILD":
                        "multimedia development must not start from this package",
                    "NOT_CANONICALLY_FROZEN":
                        "the canonical module source is still open (MS2680, B02-CAIR-INT-001)",
                    "MULTIMEDIA_NOT_PRODUCED":
                        "no image, audio, video or animation is embedded or produced",
                },
                prohibited_as_current_status=list(IDENT.STALE_STATUS_TOKENS),
                never_assertable_status_tokens=list(IDENT.FORBIDDEN_STATUS_TOKENS),
                never_assertable_claims=list(IDENT.FORBIDDEN_CLAIM_STRINGS))


def component_main_governance():
    M = ADAPT.Model()
    import b02_visual_policy_v0_4 as VP
    rows = []
    for c in OV.mapping()["components"]:
        g = VP.component_main_governance(c["component_id"])
        rows.append(dict(component_id=c["component_id"],
                         component_name=c["component_name"],
                         learner_screen_id=c["learner_screen_id"],
                         active=dict(visual_requirement=g["visual_requirement"],
                                     requirement_authority=g["requirement_authority"],
                                     treatment=g["treatment"],
                                     treatment_authority=g["treatment_authority"],
                                     subject_provenance=g["subject_provenance"],
                                     overview_subject_count=g["overview_subject_count"],
                                     mapping_status=g["mapping_status"],
                                     instance_mapping=g["instance_mapping"],
                                     pending_human=g["pending_human"]),
                         subjects=[dict(label=s["subject_label"],
                                        provenance=s["provenance"],
                                        directly_named_by_bariah=s["directly_named_by_bariah"])
                                   for s in c["subjects"]],
                         superseded_lineage=dict(
                             until_version="v0.4.4",
                             visual_requirement="CONDITIONAL",
                             visual_status=("RESOLVED_BY_DIRECT_AUTHORITY"
                                            if c["component_id"] == "STRUKTUR_PERSISIR_AIR"
                                            else "PENDING_HUMAN"),
                             proposal_class=(None if c["component_id"] == "STRUKTUR_PERSISIR_AIR"
                                             else "PROVISIONAL_VISUAL_PROPOSAL"),
                             superseded_by="D2 6:52 PM component-main ruling + frozen 9/9 "
                                           "overview mapping (Stage 4.2E-B)",
                             recorded_here_not_on_the_page=True)))
    return dict(registry="COMPONENT_MAIN_VISUAL_GOVERNANCE",
                artifact_version=IDENT.VERSION,
                authority_split=dict(
                    requirement="BARIAH_DIRECT_SCREENSHOT — D2, 6:52 PM",
                    treatment="BARIAH_DIRECT_SCREENSHOT — D2, 6:52 PM",
                    subject_identity="per subject: MODULE_SOURCE_ATTESTED, except the two "
                                     "Papan Tanda figures named in D4",
                    note="Bariah settled the requirement and the treatment for all nine and "
                         "named a subject for none of them except those two figures. The "
                         "direction authorities on the page are unchanged from v0.4.4."),
                totals=dict(COMPONENT_MAIN_PAGES=9,
                            COMPONENT_MAIN_VISUAL_REQUIREMENT_REQUIRED=9,
                            COMPONENT_MAIN_PENDING_HUMAN=0,
                            COMPONENT_MAIN_PROVISIONAL_VISUAL_PROPOSALS=0,
                            COMPONENT_MAIN_MAPPING_COMPLETE=9,
                            UNAUTHORISED_SUBJECT_AUTHORITY_PROMOTIONS=0),
                components=rows)


def run_manifest(root, qa=None, mutation=None, replay=None, rendered=None):
    deck = os.path.join(root, IDENT.DECK_FILENAME)
    gen = os.path.join(root, "generator")
    return dict(
        manifest="B02_RUN_MANIFEST",
        stage="4.2E-C",
        artifact_identity=artifact_identity_registry(),
        status_tokens=list(IDENT.STATUS_TOKENS),
        not_asserted=list(IDENT.FORBIDDEN_CLAIM_STRINGS),
        defect_corrected=dict(
            id="B02-META-REG-001", title="ARTIFACT_VERSION_AND_STATUS_DRIFT",
            affected_pages=100,
            stale_version_line="K5 PL06 T03 B02 — PAPAN CERITA v0.4",
            stale_status_tokens=["REVIEW_READY", "BARIAH_FEEDBACK_IMPLEMENTED",
                                 "PENDING_TARGETED_CONFIRMATION"],
            retained_tokens=["NOT_FOR_MMD_BUILD", "MULTIMEDIA_NOT_PRODUCED"],
            emitting_source="b02_generator_v0_4.prodpanel_v4 head[] + TOKENS_V4"),
        repository=dict(branch="claude/verify-powerpoint-file-vpfzkg"),
        outputs=dict(deck=IDENT.DECK_FILENAME,
                     bytes=os.path.getsize(deck), sha256=sha(deck)),
        retained_unchanged={f: dict(bytes=os.path.getsize(os.path.join(root, f)),
                                    sha256=sha(os.path.join(root, f))) for f in RETAINED},
        frozen_decision_evidence={
            f: dict(bytes=os.path.getsize(os.path.join(root, "..", "..", EVIDENCE_DIR, f)),
                    sha256=sha(os.path.join(root, "..", "..", EVIDENCE_DIR, f)))
            for f in EVIDENCE},
        toolchain={f: sha(os.path.join(gen, f)) for f in TOOLCHAIN_V0_3},
        overview_mapping={c["component_id"]: c["overview_visual_count"]
                          for c in OV.mapping()["components"]},
        geometry_exemptions=geometry_registry(),
        package_status_contract=package_status_contract(),
        qa=qa or {}, mutation=mutation or {}, historical_replay=replay or {},
        rendered_inspection=rendered or {},
        totals=dict(REVIEW_PAGES=100, LEARNER_SCREENS=29, RUNTIME_STATES=100,
                    INTERACTION_ITEMS=54, SOURCE_ROWS=26, SOURCE_ASSETS=14, COMPONENTS=9,
                    EMBEDDED_MEDIA=0, SLIDES_MANUALLY_PATCHED=0),
        environment_limitations=dict(
            libreoffice_impress_import="unavailable in this container",
            microsoft_powerpoint_smoke="NOT RUN",
            microsoft_powerpoint_equivalence="NOT CLAIMED"))


def write(root, **kw):
    def dump(name, obj):
        p = os.path.join(root, name)
        json.dump(obj, open(p, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1, sort_keys=False)
        open(p, "a", encoding="utf-8").write("\n")
        return p
    out = [dump(f"GEOMETRY_EXEMPTION_REGISTRY_{IDENT.VERSION}.json", geometry_registry()),
           dump(f"ARTIFACT_IDENTITY_REGISTRY_{IDENT.VERSION}.json",
                artifact_identity_registry()),
           dump(f"ACTIVE_PACKAGE_STATUS_CONTRACT_{IDENT.VERSION}.json",
                package_status_contract()),
           dump(f"COMPONENT_MAIN_VISUAL_GOVERNANCE_{IDENT.VERSION}.json",
                component_main_governance()),
           dump(f"RUN_MANIFEST_{IDENT.VERSION}.json", run_manifest(root, **kw))]
    return out


if __name__ == "__main__":
    for p in write(sys.argv[1] if len(sys.argv) > 1 else "."):
        print("wrote", os.path.basename(p))
