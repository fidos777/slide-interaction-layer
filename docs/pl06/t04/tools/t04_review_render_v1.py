# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.8A — render the governed review model to Markdown, DOCX and a preview.

THE DESIGN THAT MAKES PARITY STRUCTURAL
---------------------------------------
`blocks()` turns the governed model into ONE ordered list of semantic blocks. The Markdown
renderer and the DOCX renderer both consume that same list and neither may add a block of its
own. A sentence cannot appear in the DOCX and not in the Markdown, because there is no code
path that could put it there.

The DOCX is assembled as OOXML directly — no document library, no template, every byte
determined by the model. That is the same doctrine the B02 PPTX generator uses and it is what
makes "nothing was manually added" auditable rather than asserted.
"""
import datetime, hashlib, json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_review_model_v1 as M

GENERATOR_VERSION = "t04_review_render_v1"
DOCX_DIR = os.path.join(REPO, "reviews", "storyboard-bariah", "t04_bariah_review")
DOCX_NAME = "T04_Pakej_Semakan_Bariah_v2.docx"
MD_NAME = "T04_BARIAH_CONTENT_REVIEW_PACK_v2.md"

BOX = "\u2610"
LINE = "_" * 44
LONG_LINE = "_" * 68


# ==========================================================================================
# ONE BLOCK LIST
# ==========================================================================================
def _dec_boxes(decisions, labels):
    return "   ".join(f"{BOX} {labels[d]}" for d in decisions)


def blocks():
    m = M.MODEL
    md = m["document_metadata"]
    dv = m["decision_vocabulary"]
    lab = dv["labels_ms"]
    B = []

    def h(level, text, **kw):
        B.append(dict(kind="heading", level=level, text=text, **kw))

    def p(text, **kw):
        B.append(dict(kind="para", text=text, **kw))

    def bullet(text):
        B.append(dict(kind="bullet", text=text))

    def table(headers, rows, widths=None):
        B.append(dict(kind="table", headers=headers, rows=rows, widths=widths))

    def field(text):
        B.append(dict(kind="field", text=text))

    def brk():
        B.append(dict(kind="pagebreak"))

    # ---------------- cover ----------------
    h(0, md["title_ms"], role="cover_title")
    p(md["subtitle_ms"], role="cover_subtitle")
    p(md["unit_line_ms"], role="cover_unit")
    h(1, "Status dokumen")
    p(md["opening_disclosure_ms"])
    for s in md["status_lines_ms"]:
        bullet(s)
    h(1, "Butiran penyemak")
    table(["Perkara", "Butiran"],
          [["Nama penyemak", md["reviewer_name_ms"]],
           ["Peranan", md["reviewer_role_ms"]],
           ["Versi dokumen", md["version"]],
           ["Tarikh semakan", LINE]])
    h(1, "Cara membuat semakan")
    for s in m["reviewer_instructions"]["lines_ms"]:
        bullet(s)
    p(m["reviewer_instructions"]["merge_rule_ms"], role="emphasis")
    brk()

    # ---------------- A. screens ----------------
    ss = m["screen_sequence"]
    h(1, "A. Cadangan susunan skrin")
    p(f"{ss['proposed_learner_screen_count']} skrin dicadangkan. "
      "Jumlah akhir menunggu kelulusan Bariah.")
    table(["Skrin", "Tajuk", "Layanan", "Tujuan ringkas", "Visual"],
          [[s["item_id"], s["display_title"], s["treatment_ms"], s["purpose_ms"],
            s["visual_ms"]] for s in ss["screens"]],
          widths=[9, 24, 18, 31, 18])
    p("Keputusan bagi setiap skrin:")
    for s in ss["screens"]:
        p(f"{s['item_id']} — {s['display_title']}", role="item_label")
        p(f"Kandungan: {s['population_ms']}")
        p(_dec_boxes(["ACCEPT", "EDIT", "REMOVE"], lab) + f"   {BOX} {lab['MERGE']} "
          "DENGAN ID: __________", role="decision")
        field("Sebab / cadangan susunan baharu: " + LONG_LINE)
    brk()

    # ---------------- B. visuals ----------------
    va = m["visual_asset_grouping"]
    t = va["totals"]
    h(1, "B. Cadangan visual dan kumpulan aset")
    p(va["authority_statement_ms"])
    h(2, "Bagaimana jumlah visual dikira")
    for line in va["arithmetic_ms"]:
        bullet(line)
    p(f"{t['visual_obligations']} keperluan visual BUKAN {t['visual_obligations']} visual "
      f"berasingan. Cadangan ialah {t['proposed_unique_assets']} visual, dan jumlah ini belum "
      "diluluskan.", role="emphasis")
    h(2, "Keperluan yang dipenuhi oleh visual gabungan")
    p(va["composite_disclosure_ms"])
    for x in va["composite_items"]:
        bullet(x)
    h(2, "Tajuk yang tidak memerlukan visual berasingan")
    p(va["no_separate_asset_disclosure_ms"])
    for x in va["no_separate_asset_items"]:
        bullet(x)
    h(2, "Visual yang TIDAK boleh dikongsi")
    p("Visual berikut telah dikenal pasti tidak boleh digunakan semula:")
    for x in va["do_not_reuse_items"]:
        bullet(f"{x['item']} — {x['reason_ms']}")
    p(va["reuse_question_ms"], role="question")
    field("Jawapan Bariah: " + LONG_LINE)
    h(2, "Asal usul setiap kumpulan visual")
    p(va["ag01_seventh_asset"]["disclosure_ms"])
    p(va["ag08_scenario"]["disclosure_ms"])
    table(["Kumpulan", "Visual", "Asal usul", "Bilangan dicadangkan", "Skrin", "Perkongsian"],
          [[g["item_id"], g["display_title"], g["origin_label_ms"],
            g["proposed_unique_assets"], ", ".join(g["affected_screens"]),
            g["reuse_status_ms"]] for g in va["groups"]],
          widths=[10, 24, 24, 10, 18, 14])
    p("Keputusan bagi setiap kumpulan visual:")
    for g in va["groups"]:
        p(f"{g['item_id']} — {g['display_title']}", role="item_label")
        p(f"Sekatan diketahui: {g['known_restriction_ms']}")
        p(_dec_boxes(["ACCEPT", "EDIT", "REMOVE"], lab) + f"   {BOX} {lab['MERGE']} "
          "DENGAN ID: __________", role="decision")
        p(f"Perkongsian visual:   {BOX} " + f"   {BOX} ".join(
            m["decision_vocabulary"]["reuse_labels_ms"][r]
            for r in g["allowed_reuse_decisions"]), role="decision")
        field("Sebab / cadangan susunan baharu: " + LONG_LINE)
    brk()

    # ---------------- C. dialogue ----------------
    d = m["slide_2_dialogue"]
    h(1, "C. Perbualan Slide 2")
    table(["Perkara", "Butiran"],
          [["Watak", "; ".join(f"{c['name']} ({c['role_ms']})" for c in d["cast"])],
           ["Status", d["cast_status_ms"]],
           ["Kesesuaian watak", d["contextual_fit_scope_ms"]]])
    h(2, "Had kandungan perbualan")
    for r in d["boundaries"]["rules_ms"]:
        bullet(r)
    h(2, "Draf perbualan")
    for L in d["lines"]:
        p(f"{L['item_id']} — {L['speaker']}", role="item_label")
        p(f"{L['speaker']}: {L['display_text']}", role="dialogue")
        p(_dec_boxes(d["allowed_decisions"], lab), role="decision")
        field("Komen / pindaan: " + LONG_LINE)
    brk()

    # ---------------- D. rumusan ----------------
    r = m["rumusan"]
    h(1, "D. Rumusan")
    p(r["heading"], role="emphasis")
    for pt in r["points"]:
        p(f"{pt['item_id']}", role="item_label")
        p(pt["display_text"], role="rumusan_point")
        if pt["risk_flag"]:
            p(r["risk_note_ms"], role="risk")
        p(_dec_boxes(r["allowed_decisions"], lab), role="decision")
        field("Komen / pindaan: " + LONG_LINE)
    dep = m["cross_item_dependencies"][0]
    h(2, "Kaitan antara Rumusan dan Kuiz")
    p(dep["note_ms"])
    brk()

    # ---------------- E. quiz ----------------
    q = m["quiz"]
    h(1, "E. Kuiz")
    table(["Perkara", "Butiran"],
          [["Susunan", q["composition_ms"]],
           ["Markah lulus", q["pass_threshold_ms"]],
           ["Skop", q["scope_ms"]],
           ["Jawapan", q["answer_key_ms"]]])
    if q.get("distractor_review"):
        p(q["distractor_review"]["bariah_note_ms"], role="risk")
    for it in q["items"]:
        p(f"{it['item_id']} ({it['question_type']})", role="item_label")
        p(it["display_text"], role="quiz_stem")
        for o in it["options"]:
            bullet(f"{o['key']}. {o['text']}"
                   + ("   [cadangan jawapan]" if o["proposed_correct"] else ""))
        p(_dec_boxes(q["allowed_decisions"], lab), role="decision")
        field("Komen / pindaan: " + LONG_LINE)
    brk()

    # ---------------- F. approvals ----------------
    h(1, "F. Keputusan dan pindaan Bariah")
    table(["Rujukan", "Perkara", "Apa yang diperlukan", "Selesai"],
          [[a["item_id"], a["title_ms"], a["what_ms"], BOX]
           for a in m["remaining_approvals"]],
          widths=[10, 24, 52, 10])
    fr = m["final_review_record"]
    h(2, "Keputusan keseluruhan")
    for v in fr["verdict_options_ms"]:
        p(f"{BOX} {v}", role="decision")
    field(fr["closing_note_ms"])
    field(fr["reviewer_name_field_ms"])
    field(fr["reviewer_date_field_ms"])
    field(fr["signature_field_ms"])
    return B


BLOCKS = blocks()


# ==========================================================================================
# MARKDOWN
# ==========================================================================================
def render_md():
    out = []
    for b in BLOCKS:
        k = b["kind"]
        if k == "heading":
            out += ["", "#" * max(1, b["level"] + 1) + " " + b["text"], ""]
        elif k == "para":
            if b.get("role") == "emphasis":
                out += ["**" + b["text"] + "**", ""]
            elif b.get("role") in ("item_label", "quiz_stem"):
                out += ["**" + b["text"] + "**", ""]
            elif b.get("role") == "risk":
                out += ["> " + b["text"], ""]
            elif b.get("role") == "dialogue":
                out += ["> " + b["text"], ""]
            else:
                out += [b["text"], ""]
        elif k == "bullet":
            out.append("- " + b["text"])
        elif k == "field":
            out += [b["text"], ""]
        elif k == "table":
            out.append("| " + " | ".join(str(x) for x in b["headers"]) + " |")
            out.append("|" + "|".join("---" for _ in b["headers"]) + "|")
            for row in b["rows"]:
                out.append("| " + " | ".join(
                    str(c).replace("|", "\\|").replace("\n", " ") for c in row) + " |")
            out.append("")
        elif k == "pagebreak":
            out += ["", "---", ""]
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    with open(os.path.join(T04, MD_NAME), "w", encoding="utf-8") as f:
        f.write(text)
    return MD_NAME


# ==========================================================================================
# DOCX — direct OOXML assembly
# ==========================================================================================
NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
PAGE_W, PAGE_H = 11906, 16838          # A4 portrait, twips
MARGIN = 1134                          # 2 cm
CONTENT_W = PAGE_W - 2 * MARGIN        # 9638 twips


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _run(text, bold=False, size=20, italic=False, color=None):
    rpr = ["<w:rPr>"]
    if bold:
        rpr.append("<w:b/>")
    if italic:
        rpr.append("<w:i/>")
    if color:
        rpr.append(f'<w:color w:val="{color}"/>')
    rpr.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    rpr.append("</w:rPr>")
    return "".join(rpr) + f'<w:t xml:space="preserve">{_esc(text)}</w:t>'


def _p(text, *, bold=False, size=20, italic=False, align=None, space_after=120,
       space_before=0, ind=0, color=None, shade=None, keep_next=False):
    ppr = ["<w:pPr>"]
    if keep_next:
        ppr.append("<w:keepNext/>")
    ppr.append(f'<w:spacing w:before="{space_before}" w:after="{space_after}" '
               f'w:line="240" w:lineRule="auto"/>')
    if ind:
        ppr.append(f'<w:ind w:left="{ind}"/>')
    if align:
        ppr.append(f'<w:jc w:val="{align}"/>')
    if shade:
        ppr.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>')
    ppr.append("</w:pPr>")
    return ("<w:p>" + "".join(ppr) + "<w:r>"
            + _run(text, bold=bold, size=size, italic=italic, color=color) + "</w:r></w:p>")


def _pagebreak():
    return ('<w:p><w:pPr><w:spacing w:after="0"/></w:pPr>'
            '<w:r><w:br w:type="page"/></w:r></w:p>')


def _cell(text, w, *, bold=False, size=18, shade=None):
    tcpr = [f'<w:tcW w:w="{w}" w:type="dxa"/>']
    if shade:
        tcpr.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>')
    tcpr.append('<w:tcMar><w:top w:w="60" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/>'
                '<w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>')
    body = ('<w:p><w:pPr><w:spacing w:before="20" w:after="20" w:line="240" '
            'w:lineRule="auto"/></w:pPr><w:r>'
            + _run(text, bold=bold, size=size) + "</w:r></w:p>")
    return f'<w:tc><w:tcPr>{"".join(tcpr)}</w:tcPr>{body}</w:tc>'


def _table(headers, rows, widths=None):
    n = len(headers)
    if widths:
        tot = sum(widths)
        cols = [int(CONTENT_W * w / tot) for w in widths]
    else:
        cols = [CONTENT_W // n] * n
    cols[-1] = CONTENT_W - sum(cols[:-1])
    borders = ("<w:tblBorders>"
               + "".join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="9AA0A6"/>'
                         for s in ("top", "left", "bottom", "right", "insideH", "insideV"))
               + "</w:tblBorders>")
    out = ['<w:tbl><w:tblPr>'
           f'<w:tblW w:w="{CONTENT_W}" w:type="dxa"/><w:tblLayout w:type="fixed"/>'
           + borders + '</w:tblPr><w:tblGrid>'
           + "".join(f'<w:gridCol w:w="{c}"/>' for c in cols) + "</w:tblGrid>"]
    out.append('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>'
               + "".join(_cell(h, c, bold=True, shade="E8EAED")
                         for h, c in zip(headers, cols)) + "</w:tr>")
    for row in rows:
        out.append("<w:tr><w:trPr><w:cantSplit/></w:trPr>"
                   + "".join(_cell(x, c) for x, c in zip(row, cols)) + "</w:tr>")
    out.append("</w:tbl>")
    # Word needs a paragraph after a table or the next table merges into it.
    out.append('<w:p><w:pPr><w:spacing w:after="60"/></w:pPr></w:p>')
    return "".join(out)


HEADING_STYLE = {0: (44, True, None), 1: (30, True, "1A4D2E"), 2: (24, True, "1A4D2E")}


def _body_xml():
    out = []
    for b in BLOCKS:
        k = b["kind"]
        if k == "heading":
            size, bold, color = HEADING_STYLE[b["level"]]
            out.append(_p(b["text"], bold=bold, size=size, color=color,
                          space_before=200 if b["level"] else 0, space_after=120,
                          align="center" if b.get("role") == "cover_title" else None,
                          keep_next=True))
        elif k == "para":
            role = b.get("role")
            if role in ("cover_subtitle", "cover_unit"):
                out.append(_p(b["text"], size=26 if role == "cover_subtitle" else 20,
                              align="center", space_after=80))
            elif role == "emphasis":
                out.append(_p(b["text"], bold=True, space_after=140))
            elif role in ("item_label", "quiz_stem"):
                out.append(_p(b["text"], bold=True, space_before=140, space_after=60,
                              keep_next=True))
            elif role == "risk":
                out.append(_p(b["text"], italic=True, ind=200, shade="FFF4E5",
                              space_after=140))
            elif role == "dialogue":
                out.append(_p(b["text"], ind=200, space_after=60, keep_next=True))
            elif role == "decision":
                out.append(_p(b["text"], size=20, space_after=60, keep_next=True))
            elif role == "question":
                out.append(_p(b["text"], bold=True, shade="E8F0FE", space_before=120,
                              space_after=100))
            else:
                out.append(_p(b["text"]))
        elif k == "bullet":
            out.append(_p("\u2022  " + b["text"], ind=200, space_after=40))
        elif k == "field":
            out.append(_p(b["text"], size=20, space_after=160))
        elif k == "table":
            out.append(_table(b["headers"], b["rows"], b.get("widths")))
        elif k == "pagebreak":
            out.append(_pagebreak())
    sect = (f'<w:sectPr><w:pgSz w:w="{PAGE_W}" w:h="{PAGE_H}"/>'
            f'<w:pgMar w:top="{MARGIN}" w:right="{MARGIN}" w:bottom="{MARGIN}" '
            f'w:left="{MARGIN}" w:header="708" w:footer="708" w:gutter="0"/>'
            '<w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>')
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            f'<w:document {NS}><w:body>' + "".join(out) + sect + "</w:body></w:document>")


_STYLES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
           f'<w:styles {NS}><w:docDefaults><w:rPrDefault><w:rPr>'
           '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
           '<w:sz w:val="20"/><w:szCs w:val="20"/><w:lang w:val="ms-MY"/>'
           '</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>'
           '<w:spacing w:after="120" w:line="240" w:lineRule="auto"/>'
           '</w:pPr></w:pPrDefault></w:docDefaults>'
           '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
           '<w:name w:val="Normal"/><w:qFormat/></w:style></w:styles>')

_CONTENT_TYPES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                  '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                  '<Default Extension="rels" ContentType="application/vnd.openxmlformats-'
                  'package.relationships+xml"/>'
                  '<Default Extension="xml" ContentType="application/xml"/>'
                  '<Override PartName="/word/document.xml" ContentType="application/vnd.'
                  'openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                  '<Override PartName="/word/styles.xml" ContentType="application/vnd.'
                  'openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
                  '<Override PartName="/word/settings.xml" ContentType="application/vnd.'
                  'openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
                  '<Override PartName="/docProps/core.xml" ContentType="application/vnd.'
                  'openxmlformats-package.core-properties+xml"/>'
                  '<Override PartName="/docProps/app.xml" ContentType="application/vnd.'
                  'openxmlformats-officedocument.extended-properties+xml"/>'
                  '</Types>')

_ROOT_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
              '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/'
              'relationships">'
              '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/'
              'officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
              '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/'
              'relationships/metadata/core-properties" Target="docProps/core.xml"/>'
              '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/'
              'officeDocument/2006/relationships/extended-properties" '
              'Target="docProps/app.xml"/></Relationships>')

_DOC_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/'
             'relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/'
             'officeDocument/2006/relationships/styles" Target="styles.xml"/>'
             '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/'
             'officeDocument/2006/relationships/settings" Target="settings.xml"/>'
             '</Relationships>')

_SETTINGS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
             f'<w:settings {NS}><w:zoom w:percent="100"/>'
             '<w:defaultTabStop w:val="720"/><w:compat/></w:settings>')

# Fixed timestamp: the model is deterministic and the package must be too, so the same model
# always produces the same bytes. The real generation time is recorded in the manifest.
FIXED_TS = "2026-08-02T00:00:00Z"


def _core():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/'
            'metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" '
            'xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<dc:title>{_esc(M.DOCUMENT_METADATA["title_ms"])} — '
            f'{_esc(M.DOCUMENT_METADATA["subtitle_ms"])}</dc:title>'
            '<dc:language>ms-MY</dc:language>'
            f'<cp:revision>1</cp:revision>'
            f'<dcterms:created xsi:type="dcterms:W3CDTF">{FIXED_TS}</dcterms:created>'
            f'<dcterms:modified xsi:type="dcterms:W3CDTF">{FIXED_TS}</dcterms:modified>'
            '</cp:coreProperties>')


def _app():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/'
            'extended-properties">'
            '<Application>CAIR governed OOXML writer</Application>'
            '<AppVersion>1.0000</AppVersion></Properties>')


def render_docx():
    os.makedirs(DOCX_DIR, exist_ok=True)
    path = os.path.join(DOCX_DIR, DOCX_NAME)
    parts = [("[Content_Types].xml", _CONTENT_TYPES), ("_rels/.rels", _ROOT_RELS),
             ("word/document.xml", _body_xml()), ("word/styles.xml", _STYLES),
             ("word/settings.xml", _SETTINGS), ("word/_rels/document.xml.rels", _DOC_RELS),
             ("docProps/core.xml", _core()), ("docProps/app.xml", _app())]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts:
            zi = zipfile.ZipInfo(name, date_time=(2026, 8, 2, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o600 << 16
            z.writestr(zi, data.encode("utf-8"))
    return path


# ==========================================================================================
# DETERMINISTIC PREVIEW — the fallback when no native renderer exists
# ==========================================================================================
def render_preview():
    """A deterministic A4 page preview drawn from the same block list.

    This is NOT a Word render. It is a layout approximation used to estimate page count and
    to give Firdaus something to eyeball. Its limitations are recorded, not glossed.
    """
    from PIL import Image, ImageDraw, ImageFont
    DPI = 96
    W = int(PAGE_W / 1440 * DPI)
    H = int(PAGE_H / 1440 * DPI)
    Mg = int(MARGIN / 1440 * DPI)

    def font(sz, bold=False):
        base = "/usr/share/fonts/truetype/liberation/LiberationSans"
        for cand in ((base + "-Bold.ttf") if bold else (base + "-Regular.ttf"),
                     "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
            if os.path.exists(cand):
                try:
                    return ImageFont.truetype(cand, sz)
                except Exception:
                    pass
        return ImageFont.load_default()

    pages, img, drw, y = [], None, None, 0

    def new_page():
        nonlocal img, drw, y
        if img is not None:
            pages.append(img)
        img = Image.new("RGB", (W, H), "white")
        drw = ImageDraw.Draw(img)
        y = Mg

    def wrap(text, f, width):
        words, lines, cur = str(text).split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if drw.textlength(t, font=f) <= width:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def emit(text, f, indent=0, after=4):
        nonlocal y
        for ln in wrap(text, f, W - 2 * Mg - indent):
            if y + 18 > H - Mg:
                new_page()
            drw.text((Mg + indent, y), ln, font=f, fill="black")
            y += int(f.size * 1.35)
        y += after

    new_page()
    for b in BLOCKS:
        k = b["kind"]
        if k == "pagebreak":
            new_page()
        elif k == "heading":
            sz = {0: 22, 1: 15, 2: 12}[b["level"]]
            y += 6
            emit(b["text"], font(sz, True), after=6)
        elif k == "para":
            emit(b["text"], font(10, b.get("role") in ("emphasis", "item_label", "quiz_stem",
                                                       "question")),
                 indent=10 if b.get("role") in ("risk", "dialogue") else 0)
        elif k == "bullet":
            emit("\u2022 " + b["text"], font(10), indent=10, after=2)
        elif k == "field":
            emit(b["text"], font(10), after=8)
        elif k == "table":
            f, fb = font(9), font(9, True)
            emit(" | ".join(str(x) for x in b["headers"]), fb, after=2)
            for row in b["rows"]:
                emit(" | ".join(str(c) for c in row), f, indent=6, after=1)
            y += 6
    pages.append(img)
    outdir = os.path.join(T04, "preview")
    os.makedirs(outdir, exist_ok=True)
    for old in os.listdir(outdir):
        if old.startswith("T04_Pakej_Semakan_Bariah_v2_p") and old.endswith(".png"):
            os.remove(os.path.join(outdir, old))
    names = []
    for i, im in enumerate(pages, 1):
        n = f"T04_Pakej_Semakan_Bariah_v2_p{i:02d}.png"
        im.save(os.path.join(outdir, n))
        names.append(n)
    return names


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


if __name__ == "__main__":
    M.emit()
    md = render_md()
    dx = render_docx()
    pv = render_preview()
    print("wrote", md)
    print("wrote", os.path.relpath(dx, REPO))
    print("bytes", os.path.getsize(dx), "sha256", sha256_file(dx))
    print("preview pages", len(pv))
    print("blocks", len(BLOCKS))
