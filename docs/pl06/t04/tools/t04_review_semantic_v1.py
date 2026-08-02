# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.8A — semantic parity between the model, the Markdown and the DOCX.

WHAT THIS PROVES, AND WHAT IT DOES NOT
--------------------------------------
The Markdown and the DOCX are re-parsed FROM DISK, not re-derived from the renderer. Their
substantive strings are normalised and compared against the model's canonical projection and
against each other. So the check really does catch a sentence living in one artifact and not
the other — which is the exact defect this stage exists to close.

It does NOT prove the DOCX looks right. Layout, pagination and glyph rendering are a separate
question, answered by Part 14, and on this machine only partially.

Permitted formatting differences: heading markers, bold/italic markers, bullet glyphs, table
pipes, blockquote markers, horizontal rules, and runs of underscores used as write-in rules.
Everything else must match.
"""
import hashlib, json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_review_model_v1 as M
import t04_review_render_v1 as R

MD_PATH = os.path.join(T04, R.MD_NAME)
DOCX_PATH = os.path.join(R.DOCX_DIR, R.DOCX_NAME)
MODEL_PATH = os.path.join(T04, "T04_BARIAH_REVIEW_MODEL_v1.json")

ITEM_ID = re.compile(r"\b(T04-S\d{2}|AG-\d{2}|T04-DLG-\d{2}|T04-RUM2-\d{2}|BA-\d)\b")
QUIZ_ID = re.compile(r"\b(Q[1-5])\b")
OPTION_LINE = re.compile(r"^([A-F])\.\s+(.*)$")
SPEAKER_LINE = re.compile(r"^(Alya|Encik Rahman):\s+(.*)$")
UNDERSCORES = re.compile(r"_{3,}")
FORMAT_ONLY = re.compile(r"^[\s\-|*_#>·•]*$")


def _norm(s):
    """Collapse a string to its meaning. Formatting markers are stripped; words are not."""
    s = s.replace(" ", " ")
    s = UNDERSCORES.sub("__RULE__", s)
    s = re.sub(r"^\s*#{1,6}\s*", "", s)
    s = re.sub(r"^\s*[>\-*]\s+", "", s)
    s = s.replace("**", "").replace("•", "").replace("|", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _substantive(lines):
    out = []
    for ln in lines:
        n = _norm(ln)
        if not n or FORMAT_ONLY.match(n) or n == "__RULE__":
            continue
        out.append(n)
    return out


# ==========================================================================================
def model_strings():
    """The model's canonical projection — every block text, normalised.

    R.blocks() is called LIVE. Reading the cached R.BLOCKS made this blind to a model edit,
    which is exactly the defect this whole stage exists to prevent.
    """
    out = []
    for b in R.blocks():
        k = b["kind"]
        if k in ("heading", "para", "bullet", "field"):
            out.append(b["text"])
        elif k == "table":
            out += [str(x) for x in b["headers"]]
            for row in b["rows"]:
                out += [str(c) for c in row]
    return _substantive(out)


def md_strings():
    with open(MD_PATH, encoding="utf-8") as f:
        raw = f.read()
    lines = []
    for ln in raw.splitlines():
        if ln.strip().startswith("|") and set(ln.strip()) <= set("|- "):
            continue
        if ln.strip().startswith("|"):
            lines += [c for c in ln.strip().strip("|").split("|")]
        else:
            lines.append(ln)
    return _substantive(lines)


def docx_strings():
    z = zipfile.ZipFile(DOCX_PATH)
    xml = z.read("word/document.xml").decode("utf-8")
    paras = re.findall(r"<w:p[ >].*?</w:p>", xml, re.S)
    out = []
    for p in paras:
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S))
        t = (t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
             .replace("&quot;", '"').replace("&apos;", "'"))
        out.append(t)
    return _substantive(out)


# ==========================================================================================
def _facts(strings):
    """Structured facts extracted independently from a flat string corpus."""
    text = "\n".join(strings)
    item_ids = sorted(set(ITEM_ID.findall(text)))
    quiz_ids = sorted(set(QUIZ_ID.findall(text)))
    dialogue = sorted({f"{m.group(1)}: {m.group(2)}" for s in strings
                       for m in [SPEAKER_LINE.match(s)] if m})
    # Section headings are formatted "A. Cadangan susunan skrin" and are NOT quiz options.
    section_titles = {f"{x['section_id']}. {x['title_ms']}" for x in M.SECTIONS}
    options = sorted({f"{m.group(1)}. {m.group(2)}" for s in strings
                      for m in [OPTION_LINE.match(s)] if m
                      and f"{m.group(1)}. {m.group(2)}" not in section_titles})
    verdicts = sorted({v for v in M.FINAL_VERDICT_OPTIONS_MS if v in text})
    decisions = sorted({d for d in M.DECISION_LABELS_MS.values()
                        if re.search(rf"\b{d}\b", text)})
    reuse_labels = sorted({v for v in M.REUSE_LABELS_MS.values() if v in text})
    origins = sorted({v for v in M.ORIGIN_MS.values() if v in text})
    merge_field = "GABUNG DENGAN ID" in text
    dep_note = M.CROSS_ITEM_DEPENDENCIES[0]["note_ms"] in text
    risk_note = M.RUMUSAN["risk_note_ms"] in text
    reuse_q = M.REUSE_QUESTION_MS in text
    sig = M.FINAL_REVIEW_RECORD["signature_field_ms"].split(":")[0] in text
    return dict(
        item_ids=item_ids,
        quiz_ids=quiz_ids,
        screen_count=len([i for i in item_ids if i.startswith("T04-S")]),
        asset_group_count=len([i for i in item_ids if i.startswith("AG-")]),
        dialogue_line_count=len([i for i in item_ids if i.startswith("T04-DLG-")]),
        rumusan_point_count=len([i for i in item_ids if i.startswith("T04-RUM2-")]),
        approval_count=len([i for i in item_ids if i.startswith("BA-")]),
        dialogue=dialogue,
        quiz_options=options,
        verdict_options=verdicts,
        decision_labels=decisions,
        reuse_labels=reuse_labels,
        origin_labels=origins,
        merge_target_field_present=merge_field,
        dependency_note_present=dep_note,
        rumusan_risk_note_present=risk_note,
        reuse_question_present=reuse_q,
        signature_field_present=sig,
        totals=dict(
            visual_obligations=bool(re.search(r"\b46 keperluan visual\b", text)),
            proposed_assets=bool(re.search(r"\b41 visual", text)),
            composite=bool(re.search(r"\bLima keperluan visual\b", text)),
            no_separate=bool(re.search(r"\bTiga tajuk\b", text)),
        ),
    )


def semantic(name):
    strings = {"model": model_strings, "markdown": md_strings, "docx": docx_strings}[name]()
    f = _facts(strings)
    f["substantive_string_count"] = len(strings)
    f["substantive_strings"] = sorted(set(strings))
    return f


def digest(sem):
    return hashlib.sha256(
        json.dumps(sem, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def parity():
    sems = {n: semantic(n) for n in ("model", "markdown", "docx")}
    digs = {n: digest(s) for n, s in sems.items()}
    ms, dm, dd = (set(sems["model"]["substantive_strings"]),
                  set(sems["markdown"]["substantive_strings"]),
                  set(sems["docx"]["substantive_strings"]))
    fields = [k for k in sems["model"] if k != "substantive_strings"]
    field_diffs = {k: {n: sems[n][k] for n in sems}
                   for k in fields
                   if not (sems["model"][k] == sems["markdown"][k] == sems["docx"][k])}
    return dict(
        JSON_MODEL_SEMANTIC_DIGEST=digs["model"],
        MARKDOWN_SEMANTIC_DIGEST=digs["markdown"],
        DOCX_SEMANTIC_DIGEST=digs["docx"],
        all_three_agree=len(set(digs.values())) == 1,
        docx_only_substantive=sorted(dd - ms),
        markdown_only_substantive=sorted(dm - ms),
        model_missing_from_docx=sorted(ms - dd),
        model_missing_from_markdown=sorted(ms - dm),
        field_level_differences=field_diffs,
        counts={n: sems[n]["substantive_string_count"] for n in sems},
        permitted_formatting_differences=[
            "heading markers", "bold and italic markers", "bullet glyphs", "table pipes",
            "blockquote markers", "horizontal rules",
            "runs of underscores used as write-in rules"],
        proves="that no substantive sentence exists in one artifact and not the others",
        does_not_prove="that the DOCX renders correctly — see the visual-check record")


if __name__ == "__main__":
    r = parity()
    print(json.dumps({k: v for k, v in r.items()
                      if k not in ("field_level_differences",)},
                     ensure_ascii=False, indent=1))
    if r["field_level_differences"]:
        print("FIELD DIFFERENCES:")
        print(json.dumps(r["field_level_differences"], ensure_ascii=False, indent=1)[:4000])
    sys.exit(0 if r["all_three_agree"] else 1)
