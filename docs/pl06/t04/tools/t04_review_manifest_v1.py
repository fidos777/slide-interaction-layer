# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.8A — emit the governed review artifact manifest (Markdown + JSON)."""
import datetime, hashlib, json, os, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_review_model_v1 as M
import t04_review_render_v1 as R
import t04_review_semantic_v1 as SEM
import t04_review_artifact_qa_v1 as QA

GENERATED_AT = os.environ.get("T04_MANIFEST_TS", "2026-08-02T10:40:00Z")


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def build():
    docx = os.path.join(R.DOCX_DIR, R.DOCX_NAME)
    md = SEM.MD_PATH
    model = SEM.MODEL_PATH
    par = SEM.parity()
    prev = sorted(x for x in os.listdir(os.path.join(T04, "preview")) if x.endswith(".png"))
    return dict(
        stage=M.STAGE, unit_id=M.UNIT_ID,
        artifact_hierarchy=M.ARTIFACT_HIERARCHY,
        external_manual_docx=M.EXTERNAL_MANUAL_DOCX,
        governed_docx=dict(
            path=os.path.relpath(docx, REPO), filename=R.DOCX_NAME,
            byte_size=os.path.getsize(docx), sha256=_sha(docx),
            page_count_estimated_from_preview=len(prev),
            page_count_source="deterministic preview from the same model — NOT a Word "
                              "pagination; Word decides the real count",
            generation_timestamp=GENERATED_AT,
            source_model_hash=M.model_hash(),
            generator_version=R.GENERATOR_VERSION,
            semantic_item_count=len(M.reviewable_item_ids()),
            delivery_status=QA.DELIVERY_STATUS),
        generated_markdown=dict(path="docs/pl06/t04/" + R.MD_NAME,
                                byte_size=os.path.getsize(md), sha256=_sha(md)),
        controlled_model=dict(path="docs/pl06/t04/T04_BARIAH_REVIEW_MODEL_v1.json",
                              byte_size=os.path.getsize(model), sha256=_sha(model),
                              model_hash=M.model_hash()),
        semantic_parity=dict(
            JSON_MODEL_SEMANTIC_DIGEST=par["JSON_MODEL_SEMANTIC_DIGEST"],
            MARKDOWN_SEMANTIC_DIGEST=par["MARKDOWN_SEMANTIC_DIGEST"],
            DOCX_SEMANTIC_DIGEST=par["DOCX_SEMANTIC_DIGEST"],
            all_three_agree=par["all_three_agree"],
            substantive_string_counts=par["counts"],
            docx_only_substantive=par["docx_only_substantive"],
            markdown_only_substantive=par["markdown_only_substantive"],
            permitted_formatting_differences=par["permitted_formatting_differences"],
            proves=par["proves"], does_not_prove=par["does_not_prove"]),
        native_render=dict(status=QA.NATIVE_RENDER_STATUS, evidence=QA.NATIVE_RENDER_EVIDENCE),
        fallback_preview=dict(pages=len(prev), files=prev,
                              directory="docs/pl06/t04/preview",
                              limitation="A deterministic layout approximation, not a Word "
                                         "render. It uses Liberation Sans, which lacks the "
                                         "U+2610 ballot box, so checkboxes appear as a "
                                         "fallback glyph in the preview only."),
        qa=dict(suite_id=QA.SUITE_ID, sibling_suite=QA.SIBLING_SUITE_ID,
                sibling_note=QA.SIBLING_NOTE, not_checked=QA.NOT_CHECKED),
        production_guards=M.MODEL["production_guards"])


def emit():
    m = build()
    with open(os.path.join(T04, "T04_BARIAH_REVIEW_ARTIFACT_MANIFEST_v1.json"), "w",
              encoding="utf-8") as f:
        f.write(json.dumps(m, ensure_ascii=False, indent=1) + "\n")
    g, p, mdm, cm = m["governed_docx"], m["semantic_parity"], m["generated_markdown"], \
        m["controlled_model"]
    e = m["external_manual_docx"]
    L = ["# T04_BARIAH_REVIEW_ARTIFACT_MANIFEST_v1", "", "```",
         f"STAGE            = {m['stage']}",
         f"UNIT             = {m['unit_id']}",
         f"DELIVERY_STATUS  = {g['delivery_status']}",
         f"NATIVE_RENDER    = {m['native_render']['status']}",
         "```", "", "# 1. Artifact hierarchy", "",
         "| Role | Artifact |", "|---|---|",
         f"| CONTROLLED_CONTENT_SOURCE_OF_TRUTH | `{m['artifact_hierarchy']['CONTROLLED_CONTENT_SOURCE_OF_TRUTH']}` |",
         f"| GENERATED_REFERENCE_VIEW | `{m['artifact_hierarchy']['GENERATED_REFERENCE_VIEW']}` |",
         f"| HUMAN_APPROVAL_ARTIFACT | `{m['artifact_hierarchy']['HUMAN_APPROVAL_ARTIFACT']}` |",
         "", m["artifact_hierarchy"]["rule"], "",
         "# 2. Governed DOCX", "", "```",
         f"filename                  = {g['filename']}",
         f"path                      = {g['path']}",
         f"byte_size                 = {g['byte_size']}",
         f"sha256                    = {g['sha256']}",
         f"page_count (estimated)    = {g['page_count_estimated_from_preview']}",
         f"generation_timestamp      = {g['generation_timestamp']}",
         f"source_model_hash         = {g['source_model_hash']}",
         f"generator_version         = {g['generator_version']}",
         f"semantic_item_count       = {g['semantic_item_count']}",
         f"delivery_status           = {g['delivery_status']}",
         "```", "", f"**Page count caveat.** {g['page_count_source']}", "",
         "# 3. Other governed artifacts", "",
         "| Artifact | Bytes | SHA-256 |", "|---|---:|---|",
         f"| `{cm['path']}` | {cm['byte_size']:,} | `{cm['sha256']}` |",
         f"| `{mdm['path']}` | {mdm['byte_size']:,} | `{mdm['sha256']}` |", "",
         "# 4. Semantic parity", "", "```",
         f"JSON_MODEL_SEMANTIC_DIGEST = {p['JSON_MODEL_SEMANTIC_DIGEST']}",
         f"MARKDOWN_SEMANTIC_DIGEST   = {p['MARKDOWN_SEMANTIC_DIGEST']}",
         f"DOCX_SEMANTIC_DIGEST       = {p['DOCX_SEMANTIC_DIGEST']}",
         f"all_three_agree            = {p['all_three_agree']}",
         f"substantive strings        = {p['substantive_string_counts']}",
         f"docx_only_substantive      = {p['docx_only_substantive']}",
         f"markdown_only_substantive  = {p['markdown_only_substantive']}",
         "```", "",
         f"**Proves** {p['proves']}.", "",
         f"**Does not prove** {p['does_not_prove']}.", "",
         "Permitted formatting differences: " +
         ", ".join(p["permitted_formatting_differences"]) + ".", "",
         "# 5. Rendering", "", f"`{m['native_render']['status']}`", "",
         m["native_render"]["evidence"], "",
         f"Fallback: {m['fallback_preview']['pages']} deterministic preview pages in "
         f"`{m['fallback_preview']['directory']}`.", "",
         m["fallback_preview"]["limitation"], "",
         "# 6. The non-governed reference", "", "```",
         f"filename         = {e['filename']}",
         f"byte_size        = {e['byte_size']}",
         f"sha256           = {e['sha256']}",
         f"status           = {e['status']}",
         f"delivery_status  = {e['delivery_status']}",
         f"used_as_authority= {e['used_as_authority']}",
         f"copied_into_repo = {e['copied_into_evidence']}",
         "```", "", e["page_count_note"], "",
         "**Divergences that made it non-governed:**", ""]
    L += [f"- {d}" for d in e["divergences_observed"]]
    L += ["", e["conclusion"], "", "# 7. QA", "", "```",
          f"SUITE_ID        = {m['qa']['suite_id']}",
          f"SIBLING_SUITE   = {m['qa']['sibling_suite']}",
          "```", "", m["qa"]["sibling_note"], "", "**NOT_CHECKED**", ""]
    L += [f"- {x}" for x in m["qa"]["not_checked"]]
    L += ["", "# 8. Production guards", "", "```"]
    L += [f"{k} = {v}" for k, v in m["production_guards"].items()]
    L += ["```", ""]
    with open(os.path.join(T04, "T04_BARIAH_REVIEW_ARTIFACT_MANIFEST_v1.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(L))
    return m


if __name__ == "__main__":
    m = emit()
    print("wrote T04_BARIAH_REVIEW_ARTIFACT_MANIFEST_v1.md / .json")
    print("docx", m["governed_docx"]["byte_size"], m["governed_docx"]["sha256"][:16])
