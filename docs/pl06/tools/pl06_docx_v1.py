# -*- coding: utf-8 -*-
"""A governed OOXML writer for PL06 review documents — mechanism only, no content.

This is the generalisation of the proven Stage 4.2F-B0.8A T04 writer: direct OOXML assembly,
no document library, no template, deterministic bytes. It carries no unit content of its own,
so a cross-unit package and a unit package cannot drift apart in mechanism.

The caller supplies ONE block list. Both the Markdown projection and the DOCX are rendered
from that same list, which is why a sentence cannot reach one and not the other.
"""
import os
import zipfile

NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
PAGE_W, PAGE_H = 11906, 16838          # A4 portrait, twips
MARGIN = 1134                          # 2 cm
CONTENT_W = PAGE_W - 2 * MARGIN

# The model is deterministic, so the package must be too: same model, same bytes.
FIXED_TS = "2026-08-03T00:00:00Z"
FIXED_ZIP_DATE = (2026, 8, 3, 0, 0, 0)


# ==========================================================================================
# Block constructors — the one vocabulary both renderers understand
# ==========================================================================================
def h(level, text, **kw):
    return dict(kind="heading", level=level, text=text, **kw)


def p(text, **kw):
    return dict(kind="para", text=text, **kw)


def bullet(text):
    return dict(kind="bullet", text=text)


def field(text):
    return dict(kind="field", text=text)


def table(headers, rows, widths=None):
    return dict(kind="table", headers=headers, rows=[[str(c) for c in r] for r in rows],
                widths=widths)


def pagebreak():
    return dict(kind="pagebreak")


# ==========================================================================================
# Markdown projection
# ==========================================================================================
def render_markdown(blocks):
    out = []
    for b in blocks:
        k = b["kind"]
        if k == "heading":
            out.append("\n" + "#" * (b["level"] + 1) + " " + b["text"] + "\n")
        elif k == "para":
            role = b.get("role")
            if role == "emphasis":
                out.append("**" + b["text"] + "**\n")
            elif role == "risk":
                out.append("> " + b["text"] + "\n")
            elif role in ("item_label", "question"):
                out.append("**" + b["text"] + "**\n")
            else:
                out.append(b["text"] + "\n")
        elif k == "bullet":
            out.append("- " + b["text"])
        elif k == "field":
            out.append("`" + b["text"] + "`\n")
        elif k == "table":
            out.append("")
            out.append("| " + " | ".join(b["headers"]) + " |")
            out.append("|" + "|".join("---" for _ in b["headers"]) + "|")
            for r in b["rows"]:
                out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
            out.append("")
        elif k == "pagebreak":
            out.append("\n---\n")
    return "\n".join(out).replace("\n\n\n", "\n\n") + "\n"


# ==========================================================================================
# DOCX — direct OOXML assembly
# ==========================================================================================
def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _run(text, bold=False, size=20, italic=False, color=None):
    rpr = ["<w:rPr>"]
    if bold:
        rpr.append("<w:b/>")
    if italic:
        rpr.append("<w:i/>")
    if color:
        rpr.append(f'<w:color w:val="{color}"/>')
    rpr.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>')
    return "".join(rpr) + f'<w:t xml:space="preserve">{_esc(text)}</w:t>'


def _para(text, *, bold=False, size=20, italic=False, align=None, space_after=120,
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


def _pagebreak_xml():
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


def _table_xml(headers, rows, widths=None):
    n = len(headers)
    cols = ([int(CONTENT_W * w / sum(widths)) for w in widths] if widths
            else [CONTENT_W // n] * n)
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
               + "".join(_cell(x, c, bold=True, shade="E8EAED")
                         for x, c in zip(headers, cols)) + "</w:tr>")
    for row in rows:
        out.append("<w:tr><w:trPr><w:cantSplit/></w:trPr>"
                   + "".join(_cell(x, c) for x, c in zip(row, cols)) + "</w:tr>")
    out.append("</w:tbl>")
    out.append('<w:p><w:pPr><w:spacing w:after="60"/></w:pPr></w:p>')
    return "".join(out)


HEADING_STYLE = {0: (44, True, None), 1: (30, True, "1A4D2E"), 2: (24, True, "1A4D2E"),
                 3: (21, True, "37474F")}


def _body_xml(blocks):
    out = []
    for b in blocks:
        k = b["kind"]
        if k == "heading":
            size, bold, color = HEADING_STYLE[b["level"]]
            out.append(_para(b["text"], bold=bold, size=size, color=color,
                             space_before=200 if b["level"] else 0, space_after=120,
                             align="center" if b.get("role") == "cover_title" else None,
                             keep_next=True))
        elif k == "para":
            role = b.get("role")
            if role in ("cover_subtitle", "cover_unit"):
                out.append(_para(b["text"], size=26 if role == "cover_subtitle" else 20,
                                 align="center", space_after=80))
            elif role == "emphasis":
                out.append(_para(b["text"], bold=True, space_after=140))
            elif role == "item_label":
                out.append(_para(b["text"], bold=True, space_before=140, space_after=60,
                                 keep_next=True))
            elif role == "risk":
                out.append(_para(b["text"], italic=True, ind=200, shade="FFF4E5",
                                 space_after=140))
            elif role == "question":
                out.append(_para(b["text"], bold=True, shade="E8F0FE", space_before=120,
                                 space_after=100))
            elif role == "provenance":
                out.append(_para(b["text"], size=16, color="5F6368", space_after=40))
            else:
                out.append(_para(b["text"]))
        elif k == "bullet":
            out.append(_para("•  " + b["text"], ind=200, space_after=40))
        elif k == "field":
            out.append(_para(b["text"], size=20, space_after=160))
        elif k == "table":
            out.append(_table_xml(b["headers"], b["rows"], b.get("widths")))
        elif k == "pagebreak":
            out.append(_pagebreak_xml())
    sect = (f'<w:sectPr><w:pgSz w:w="{PAGE_W}" w:h="{PAGE_H}"/>'
            f'<w:pgMar w:top="{MARGIN}" w:right="{MARGIN}" w:bottom="{MARGIN}" '
            f'w:left="{MARGIN}" w:header="708" w:footer="708" w:gutter="0"/>'
            '<w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
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
                  '<Types xmlns="http://schemas.openxmlformats.org/package/2006/'
                  'content-types">'
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


def _core(title):
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/'
            'metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" '
            'xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<dc:title>{_esc(title)}</dc:title>'
            '<dc:language>ms-MY</dc:language><cp:revision>1</cp:revision>'
            f'<dcterms:created xsi:type="dcterms:W3CDTF">{FIXED_TS}</dcterms:created>'
            f'<dcterms:modified xsi:type="dcterms:W3CDTF">{FIXED_TS}</dcterms:modified>'
            '</cp:coreProperties>')


_APP = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/'
        'extended-properties"><Application>CAIR governed OOXML writer</Application>'
        '<AppVersion>1.0000</AppVersion></Properties>')


def render_docx(blocks, path, title):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    parts = [("[Content_Types].xml", _CONTENT_TYPES), ("_rels/.rels", _ROOT_RELS),
             ("word/document.xml", _body_xml(blocks)), ("word/styles.xml", _STYLES),
             ("word/settings.xml", _SETTINGS), ("word/_rels/document.xml.rels", _DOC_RELS),
             ("docProps/core.xml", _core(title)), ("docProps/app.xml", _APP)]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts:
            zi = zipfile.ZipInfo(name, date_time=FIXED_ZIP_DATE)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o600 << 16
            z.writestr(zi, data.encode("utf-8"))
    return path


# ==========================================================================================
# DETERMINISTIC PAGE PREVIEW
#
# This is NOT a Word render. LibreOffice in this environment has no Writer filter, so no
# native render is possible and none is claimed. This is a layout approximation, drawn from
# the same block list, used to estimate page count and to be looked at.
# ==========================================================================================
PREVIEW_KIND = "DETERMINISTIC_LAYOUT_APPROXIMATION_NOT_A_WORD_RENDER"
DPI = 96


def render_preview(blocks, out_dir, prefix="P"):
    from PIL import Image, ImageDraw, ImageFont

    def font(sz, bold=False):
        base = "/usr/share/fonts/truetype/liberation/"
        nm = "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"
        return ImageFont.truetype(base + nm, sz)

    W = int(PAGE_W / 1440 * DPI)
    H = int(PAGE_H / 1440 * DPI)
    Mg = int(MARGIN / 1440 * DPI)
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        if f.endswith(".png"):
            os.remove(os.path.join(out_dir, f))

    pages, state = [], {}

    def new_page():
        img = Image.new("RGB", (W, H), (255, 255, 255))
        state["img"] = img
        state["d"] = ImageDraw.Draw(img)
        state["y"] = Mg
        pages.append(img)

    def _split_long(word, f, width):
        """Break a token wider than the column, the way Word breaks an unbreakable run.

        Without this the preview draws a long token straight through the cell border and
        reads as clean when the real layout is not — governance tokens like
        T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN are exactly the case that exposed it.
        """
        if state["d"].textlength(word, font=f) <= width:
            return [word]
        parts, cur = [], ""
        for ch in word:
            if cur and state["d"].textlength(cur + ch, font=f) > width:
                parts.append(cur)
                cur = ch
            else:
                cur += ch
        if cur:
            parts.append(cur)
        return parts

    def wrap(text, f, width):
        lines, cur = [], ""
        for raw in str(text).split():
            for w in _split_long(raw, f, width):
                probe = (cur + " " + w).strip()
                if state["d"].textlength(probe, font=f) > width and cur:
                    lines.append(cur)
                    cur = w
                else:
                    cur = probe
        if cur:
            lines.append(cur)
        return lines or [""]

    def emit(text, f, indent=0, after=4, fill=(26, 26, 26), centre=False):
        lh = f.size + 5
        for ln in wrap(text, f, W - 2 * Mg - indent):
            if state["y"] + lh > H - Mg:
                new_page()
            x = Mg + indent
            if centre:
                x = (W - state["d"].textlength(ln, font=f)) / 2
            state["d"].text((x, state["y"]), ln, font=f, fill=fill)
            state["y"] += lh
        state["y"] += after

    def emit_table(headers, rows):
        n = len(headers)
        cw = (W - 2 * Mg) // n
        fh, fb = font(11, True), font(11)
        for row, fnt, bg in ([(headers, fh, (232, 234, 237))]
                             + [(r, fb, None) for r in rows]):
            cells = [wrap(c, fnt, cw - 10) for c in row]
            rh = max(len(c) for c in cells) * (fnt.size + 4) + 6
            if state["y"] + rh > H - Mg:
                new_page()
            if bg:
                state["d"].rectangle([Mg, state["y"], W - Mg, state["y"] + rh], fill=bg)
            for i, cell in enumerate(cells):
                yy = state["y"] + 3
                for ln in cell:
                    state["d"].text((Mg + i * cw + 5, yy), ln, font=fnt, fill=(26, 26, 26))
                    yy += fnt.size + 4
            state["d"].rectangle([Mg, state["y"], W - Mg, state["y"] + rh],
                                 outline=(154, 160, 166))
            for i in range(1, n):
                state["d"].line([(Mg + i * cw, state["y"]),
                                 (Mg + i * cw, state["y"] + rh)], fill=(154, 160, 166))
            state["y"] += rh
        state["y"] += 8

    new_page()
    for b in blocks:
        k = b["kind"]
        if k == "pagebreak":
            new_page()
        elif k == "heading":
            sz = {0: 30, 1: 20, 2: 16, 3: 14}[b["level"]]
            if state["y"] + sz + 12 > H - Mg:
                new_page()
            emit(b["text"], font(sz, True), after=8,
                 fill=(26, 26, 26) if b["level"] == 0 else (26, 77, 46),
                 centre=b.get("role") == "cover_title")
        elif k == "para":
            role = b.get("role")
            if role in ("cover_subtitle", "cover_unit"):
                emit(b["text"], font(17 if role == "cover_subtitle" else 13), after=6,
                     centre=True)
            elif role == "provenance":
                emit(b["text"], font(10), after=2, fill=(95, 99, 104))
            elif role in ("emphasis", "item_label", "question"):
                emit(b["text"], font(13, True), after=6)
            elif role == "risk":
                emit(b["text"], font(12), indent=14, after=8, fill=(120, 70, 10))
            else:
                emit(b["text"], font(13), after=6)
        elif k == "bullet":
            emit("•  " + b["text"], font(13), indent=14, after=3)
        elif k == "field":
            emit(b["text"], font(13), after=10, fill=(60, 60, 60))
        elif k == "table":
            emit_table(b["headers"], b["rows"])

    made = []
    for i, img in enumerate(pages, 1):
        pth = os.path.join(out_dir, f"{prefix}{i:02d}.png")
        img.save(pth)
        made.append(pth)
    return made
