# -*- coding: utf-8 -*-
"""Stage 4.2F-C Lane 2 — controlled extraction for PL06 batch 1, by heading anchor.

    python3 docs/pl06/tools/pl06_extract_v1.py

This generalises the Stage 4.2F-B0 T04 extractor rather than replacing it. `t04_extract_v1`
stays untouched and still owns T04's committed extract; this module takes the same algorithm
with the unit-specific parts as parameters, so four more units can be read the same way.

That generalisation is checked, not asserted: `t04_equivalence()` runs THIS extractor over
T04's own boundary and compares the result, row for row, with the frozen
`T04_SOURCE_EXTRACT_v1.json` on disk. If the new reader disagrees with the old one about the
unit both have read, the difference shows up before any new unit is trusted.

SHARED BOUNDARIES
-----------------
T03-B03 shares its start page with T03-B02 and its end page with T03-B04. T03-B04 shares its
start page with T03-B03. Extraction never uses a page range: it resolves the named heading in
the body, slices between body-child indices, and then emits the neighbouring records on each
side by name — the last records of the preceding unit and the first records of the following
one — so that "no content leaked" is a checkable claim about specific paragraphs rather than
a reassurance.
"""
import hashlib
import json
import os
import sys
import xml.etree.ElementTree as ET
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PL06 = os.path.dirname(HERE)
DOCS = os.path.dirname(PL06)
REPO = os.path.dirname(DOCS)
sys.path.insert(0, os.path.join(DOCS, "source", "tools"))
import src_authority_v1 as SRC   # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
DGM = "{http://schemas.openxmlformats.org/drawingml/2006/diagram}"
PIC = "{http://schemas.openxmlformats.org/drawingml/2006/picture}"

STAGE = "4.2F-C"
EXTRACT_VERSION = "v1"
MODULE_ATTESTED = "MODULE_SOURCE_ATTESTED"
AUTHORITY = "SRC-AUTH-01"

OUT_DIR = os.path.join(PL06, "batch1_extract")

# How many neighbouring records to emit on each side of a boundary. Enough to show what was
# left behind, few enough to stay readable.
NEIGHBOUR_WINDOW = 6


class ExtractionError(RuntimeError):
    """Fail closed. An extraction that cannot prove its boundary does not produce rows."""


# ==========================================================================================
# UNITS — every field here comes from the frozen boundary map, verified in Lane 1
# ==========================================================================================
UNITS = [
    dict(unit_id="K5-PL06-T03-B03", prefix="T03B03", topik=3, bahagian=3,
         lesson_title="Infrastruktur",
         start_anchor="Infrastruktur", stop_anchor="Badan Air (Water Body)",
         frozen_start=4704, frozen_stop=4815,
         module_pages=(250, 255), subtopics="3.5 Infrastruktur",
         shared_start=True, shared_end=True,
         preceding_unit="K5-PL06-T03-B02", following_unit="K5-PL06-T03-B04"),
    dict(unit_id="K5-PL06-T03-B04", prefix="T03B04", topik=3, bahagian=4,
         lesson_title="Badan Air (Water Body)",
         start_anchor="Badan Air (Water Body)", stop_anchor="Pencahayaan / Lighting",
         frozen_start=4815, frozen_stop=4951,
         module_pages=(255, 261), subtopics="3.6 Badan Air (Water Body)",
         shared_start=True, shared_end=False,
         preceding_unit="K5-PL06-T03-B03", following_unit="K5-PL06-T03-B05"),
    dict(unit_id="K5-PL06-T05-B01", prefix="T05B01", topik=5, bahagian=1,
         lesson_title="Pengurusan Kualiti Projek",
         start_anchor="PENGURUSAN KUALITI PROJEK",
         stop_anchor="PERLINDUNGAN DAN PENAMBAHBAIKAN ALAM SEKITAR",
         frozen_start=5360, frozen_stop=5543,
         module_pages=(284, 293),
         subtopics=("5.1 Project Quality Plan (PQP) + 5.2 Jaminan Kualiti + "
                    "5.3 Inspection and Testing for Quality Control + "
                    "5.4 Penyata Kaedah Kerja"),
         shared_start=False, shared_end=False,
         preceding_unit="K5-PL06-T04-B01", following_unit="K5-PL06-T06-B01"),
    dict(unit_id="K5-PL06-T06-B01", prefix="T06B01", topik=6, bahagian=1,
         lesson_title="Perlindungan dan Penambahbaikan Alam Sekitar",
         start_anchor="PERLINDUNGAN DAN PENAMBAHBAIKAN ALAM SEKITAR",
         stop_anchor="DEMOBILISASI",
         frozen_start=5543, frozen_stop=5705,
         module_pages=(294, 302),
         subtopics=("6.1 Environmental Management Plan + 6.2 Contoh Aplikasi dalam Landskap "
                    "+ 6.3 Pengurusan Alam Sekitar"),
         shared_start=False, shared_end=False,
         preceding_unit="K5-PL06-T05-B01", following_unit="K5-PL06-T07-B01"),
]
UNIT_IDS = [u["unit_id"] for u in UNITS]

# T04's own parameters, used only to prove this reader agrees with the frozen extract.
T04_PARAMS = dict(unit_id="K5-PL06-T04-B01", prefix="T04", topik=4, bahagian=1,
                  lesson_title="Penjagaan dan Penyelenggaraan",
                  start_anchor="PENJAAGAAN DAN PENYELENGGARAAN",
                  stop_anchor="PENGURUSAN KUALITI PROJEK",
                  frozen_start=5220, frozen_stop=5360, module_pages=(276, 283),
                  subtopics="4.1 Landskap Lembut + 4.2 Landskap Kejur",
                  shared_start=False, shared_end=False,
                  preceding_unit=None, following_unit="K5-PL06-T05-B01")


# ==========================================================================================
def _text(el):
    return "".join(t.text or "" for t in el.iter(f"{W}t"))


def _style(p):
    s = p.find(f"{W}pPr/{W}pStyle")
    return s.get(f"{W}val") if s is not None else None


def _numpr(p):
    n = p.find(f"{W}pPr/{W}numPr")
    if n is None:
        return None
    lv, nid = n.find(f"{W}ilvl"), n.find(f"{W}numId")
    return dict(level=int(lv.get(f"{W}val")) if lv is not None else 0,
                num_id=int(nid.get(f"{W}val")) if nid is not None else None)


def _open_module():
    data, how = SRC.k5_open_bytes()
    if data is None:
        raise ExtractionError(SRC.MISSING_TOKEN)
    got = hashlib.sha256(data).hexdigest()
    if got != SRC.K5_DOCX_SHA256:
        raise ExtractionError(f"module DOCX identity mismatch: {got}")
    import io
    return zipfile.ZipFile(io.BytesIO(data)), dict(
        filename=SRC.K5_DOCX_NAME, bytes=len(data), sha256=got,
        identity_matches_expected=True, retrieval=how)


def _row_summary(el, idx, page):
    """A neighbouring record, named precisely enough to be checked."""
    if el.tag == f"{W}tbl":
        return dict(body_paragraph_index=None, segment_kind="TABLE",
                    text=_text(el).strip()[:120], module_page=page)
    return dict(body_paragraph_index=idx, segment_kind="PARAGRAPH",
                style=_style(el), text=_text(el).strip()[:160], module_page=page)


def extract(unit, z=None, probe=None):
    """Extract one unit by heading anchor. Never by page range."""
    close = False
    if z is None:
        z, probe = _open_module()
        close = True
    body = ET.fromstring(z.read("word/document.xml")).find(f"{W}body")
    kids = list(body)
    body_paras = [c for c in kids if c.tag == f"{W}p"]
    all_paras = list(body.iter(f"{W}p"))

    def find_idx(seq, s):
        return [i for i, p in enumerate(seq) if _text(p).strip() == s]

    hits_start = find_idx(body_paras, unit["start_anchor"])
    hits_stop = find_idx(body_paras, unit["stop_anchor"])
    if not hits_start:
        raise ExtractionError(f"start anchor not found: {unit['start_anchor']!r}")
    if not hits_stop:
        raise ExtractionError(f"stop anchor not found: {unit['stop_anchor']!r}")

    # A heading string can occur more than once — in the table of contents and in the body.
    # The frozen index disambiguates; it is not trusted blindly, it is required to be one of
    # the hits, and the run records every hit so a silent second match cannot hide.
    start_i = unit["frozen_start"]
    stop_i = unit["frozen_stop"]
    anchor_search = dict(
        start_anchor=unit["start_anchor"], start_hits=hits_start,
        stop_anchor=unit["stop_anchor"], stop_hits=hits_stop,
        frozen_start=unit["frozen_start"], frozen_stop=unit["frozen_stop"],
        frozen_start_is_a_hit=start_i in hits_start,
        frozen_stop_is_a_hit=stop_i in hits_stop,
        start_hit_count=len(hits_start), stop_hit_count=len(hits_stop),
        note=("A heading string can appear in the table of contents as well as the body. "
              "The frozen index selects which occurrence is the section start, and every "
              "occurrence is listed so a second body match cannot pass unnoticed."))
    if not anchor_search["frozen_start_is_a_hit"]:
        raise ExtractionError(f"frozen start {start_i} is not an anchor hit: {hits_start}")
    if not anchor_search["frozen_stop_is_a_hit"]:
        raise ExtractionError(f"frozen stop {stop_i} is not an anchor hit: {hits_stop}")
    if stop_i <= start_i:
        raise ExtractionError(f"stop {stop_i} does not follow start {start_i}")

    enumeration = dict(
        body_child_paragraph_count=len(body_paras),
        all_paragraph_count=len(all_paras),
        enumeration_used="DIRECT_W_P_CHILDREN_OF_W_BODY (python-docx Document.paragraphs)",
        start_index=start_i, stop_index=stop_i, span=stop_i - start_i,
        alternate_enumeration=dict(
            name="EVERY_W_P_IN_BODY_INCLUDING_TABLE_CELLS",
            start_index=find_idx(all_paras, unit["start_anchor"])[0]
            if find_idx(all_paras, unit["start_anchor"]) else None,
            note="Recorded because the two enumerations differ and mixing them silently "
                 "would move every boundary in the project."))

    si, ei = kids.index(body_paras[start_i]), kids.index(body_paras[stop_i])
    seg = kids[si:ei]

    # ---- page attribution ----
    page = unit["module_pages"][0] - 1
    pages, breaks = [], 0
    for el in seg:
        n = (sum(1 for _ in el.iter(f"{W}lastRenderedPageBreak"))
             + sum(1 for b in el.iter(f"{W}br") if b.get(f"{W}type") == "page"))
        page += n
        breaks += n
        pages.append(page)
    page_attribution = dict(
        method="w:lastRenderedPageBreak plus explicit w:br type=page",
        authority="ADVISORY_CACHED_LAYOUT",
        page_break_markers=breaks, first_page=pages[0] if pages else None,
        last_page=pages[-1] if pages else None, distinct_pages=sorted(set(pages)),
        expected=list(unit["module_pages"]),
        matches_frozen_map=((pages[0], pages[-1]) == tuple(unit["module_pages"])
                            if pages else False),
        caveat="Word's cached layout, not a typeset guarantee. Corroboration, not authority.")

    # ---- boundary proof: what was deliberately left on each side ----
    pre_idx = list(range(max(0, start_i - NEIGHBOUR_WINDOW), start_i))
    post_idx = list(range(stop_i, min(len(body_paras), stop_i + NEIGHBOUR_WINDOW)))
    excluded_before = [_row_summary(body_paras[i], i, None) for i in pre_idx]
    excluded_after = [_row_summary(body_paras[i], i, None) for i in post_idx]

    # ---- rows ----
    rels = {r.get("Id"): r.get("Target")
            for r in ET.fromstring(z.read("word/_rels/document.xml.rels"))}
    P = unit["prefix"]
    rows, assets, lists, tables = [], [], [], []
    h1 = h2 = h3 = None
    seq = 0
    for i, el in enumerate(seg):
        pg = pages[i]
        if el.tag == f"{W}tbl":
            seq += 1
            grid = []
            for tr in el.findall(f"{W}tr"):
                cells = []
                for tc in tr.findall(f"{W}tc"):
                    span = tc.find(f"{W}tcPr/{W}gridSpan")
                    vm = tc.find(f"{W}tcPr/{W}vMerge")
                    cells.append(dict(
                        text=_text(tc).strip(),
                        grid_span=int(span.get(f"{W}val")) if span is not None else 1,
                        v_merge=(vm.get(f"{W}val") or "continue") if vm is not None else None))
                grid.append(cells)
            tid = f"{P}-TBL-{len(tables) + 1:02d}"
            tables.append(dict(table_id=tid, unit_id=unit["unit_id"], sequence=seq,
                               heading_path=[x for x in (h1, h2, h3) if x],
                               rows=len(grid),
                               columns=max((len(r) for r in grid), default=0),
                               merged_cells=sum(1 for r in grid for c in r
                                                if c["grid_span"] > 1 or c["v_merge"]),
                               module_page=pg, segment_index=i, grid=grid))
            rows.append(dict(row_id=f"{P}-ROW-{seq:03d}", unit_id=unit["unit_id"],
                             sequence=seq,
                             heading_path=[x for x in (h1, h2, h3) if x],
                             content_type="TABLE", raw_source_text="",
                             controlled_display_text="", source_paragraph_start=None,
                             source_paragraph_end=None, module_page=pg,
                             docx_relationship_id=None, authority_class=MODULE_ATTESTED,
                             normalisation_status="NOT_NORMALISED",
                             visual_relationship=None, table_relationship=tid,
                             external_claim_status="NONE", segment_index=i,
                             list_level=None, paragraph_style=None))
            continue

        txt = _text(el).strip()
        st = _style(el)
        num = _numpr(el)
        dgm = next((e for e in el.iter(f"{DGM}relIds")), None)
        blips = [b for b in el.iter(f"{A}blip")]

        if dgm is not None:
            seq += 1
            rid = dgm.get(f"{R}dm")
            data_part = "word/" + rels.get(rid, "")
            dbytes = z.read(data_part)
            droot = ET.fromstring(dbytes)
            nodes = []
            for pt in droot.iter(f"{DGM}pt"):
                nt = "".join(x.text or "" for x in pt.iter(f"{A}t")).strip()
                if nt:
                    nodes.append(nt)
            extent = _extent(el)
            aid = f"{P}-DGM-{len([a for a in assets if a['asset_kind'].startswith('SMART')]) + 1:02d}"
            assets.append(dict(
                asset_id=aid, unit_id=unit["unit_id"],
                relationship_id=",".join(f"{k.split('}')[-1]}={v}"
                                         for k, v in dgm.attrib.items()),
                embedded_filename=data_part,
                mime_type="application/xml (SmartArt diagram data)",
                dimensions_in=f"{extent[0]} x {extent[1]}" if extent else None,
                sha256=hashlib.sha256(dbytes).hexdigest(),
                nearest_heading=h3 or h2 or h1, source_paragraph=start_i + i, module_page=pg,
                caption=None, source_subject_nodes=nodes, node_count=len(nodes),
                proposed_storyboard_role="PROCESS_FLOW_VISUAL",
                source_bound_status="SOURCE_BOUND_CAPTIONLESS",
                asset_kind="SMARTART_DIAGRAM_NOT_RASTER"))
            rows.append(dict(row_id=f"{P}-ROW-{seq:03d}", unit_id=unit["unit_id"],
                             sequence=seq,
                             heading_path=[x for x in (h1, h2, h3) if x],
                             content_type="DIAGRAM", raw_source_text="",
                             controlled_display_text="",
                             source_paragraph_start=start_i + i,
                             source_paragraph_end=start_i + i, module_page=pg,
                             docx_relationship_id=rid, authority_class=MODULE_ATTESTED,
                             normalisation_status="NOT_NORMALISED",
                             visual_relationship=aid, table_relationship=None,
                             external_claim_status="NONE", segment_index=i,
                             list_level=None, paragraph_style=st))
            continue

        if blips:
            seq += 1
            ids = [b.get(f"{R}embed") for b in blips if b.get(f"{R}embed")]
            extent = _extent(el)
            imgs = []
            for rid in ids:
                target = rels.get(rid)
                part = "word/" + target if target else None
                ibytes = z.read(part) if part and part in z.namelist() else b""
                aid = f"{P}-IMG-{len([a for a in assets if a['asset_kind'] == 'RASTER_IMAGE']) + 1:02d}"
                assets.append(dict(
                    asset_id=aid, unit_id=unit["unit_id"], relationship_id=rid,
                    embedded_filename=part,
                    mime_type=_mime(part), dimensions_in=(f"{extent[0]} x {extent[1]}"
                                                          if extent else None),
                    sha256=hashlib.sha256(ibytes).hexdigest() if ibytes else None,
                    bytes=len(ibytes),
                    nearest_heading=h3 or h2 or h1, source_paragraph=start_i + i,
                    module_page=pg, caption=None,
                    source_subject_nodes=[], node_count=0,
                    proposed_storyboard_role="SOURCE_FIGURE_SUBJECT_NOT_YET_RULED",
                    source_bound_status="SOURCE_BOUND_CAPTIONLESS",
                    asset_kind="RASTER_IMAGE"))
                imgs.append(aid)
            rows.append(dict(row_id=f"{P}-ROW-{seq:03d}", unit_id=unit["unit_id"],
                             sequence=seq,
                             heading_path=[x for x in (h1, h2, h3) if x],
                             content_type="IMAGE", raw_source_text=txt,
                             controlled_display_text=txt,
                             source_paragraph_start=start_i + i,
                             source_paragraph_end=start_i + i, module_page=pg,
                             docx_relationship_id=",".join(ids),
                             authority_class=MODULE_ATTESTED,
                             normalisation_status="NOT_NORMALISED",
                             visual_relationship=",".join(imgs), table_relationship=None,
                             external_claim_status="NONE", segment_index=i,
                             list_level=None, paragraph_style=st))
            continue

        if not txt:
            continue

        if st == "Heading1":
            h1, h2, h3 = txt, None, None
            ctype = "HEADING_1"
        elif st == "Heading2":
            h2, h3 = txt, None
            ctype = "HEADING_2"
        elif st == "Heading3":
            h3 = txt
            ctype = "HEADING_3"
        elif num is not None:
            ctype = "LIST_ITEM"
        else:
            ctype = "PARAGRAPH"

        seq += 1
        rid_ = f"{P}-ROW-{seq:03d}"
        if num is not None:
            lists.append(dict(list_item_id=f"{P}-LI-{len(lists) + 1:03d}", row_id=rid_,
                              unit_id=unit["unit_id"], sequence=seq, num_id=num["num_id"],
                              level=num["level"],
                              marker_type="ORDERED_OR_BULLET_PER_numbering.xml",
                              style=st or "", heading_path=[x for x in (h1, h2, h3) if x],
                              module_page=pg, raw_wording=txt))
        rows.append(dict(row_id=rid_, unit_id=unit["unit_id"], sequence=seq,
                         heading_path=[x for x in (h1, h2, h3) if x],
                         content_type=ctype, raw_source_text=txt,
                         controlled_display_text=txt, source_paragraph_start=start_i + i,
                         source_paragraph_end=start_i + i, module_page=pg,
                         docx_relationship_id=None, authority_class=MODULE_ATTESTED,
                         normalisation_status="NOT_NORMALISED",
                         visual_relationship=None, table_relationship=None,
                         external_claim_status="PENDING_CLASSIFICATION",
                         segment_index=i, list_level=num["level"] if num else None,
                         paragraph_style=st))

    empty = sum(1 for el in seg
                if el.tag == f"{W}p" and not _text(el).strip()
                and next((e for e in el.iter(f"{DGM}relIds")), None) is None
                and not [b for b in el.iter(f"{A}blip")])

    # Typeset attribution overwrites the cached-layout page on every row, in place.
    pdf_pages = _pdf_attribute(rows, unit["module_pages"])

    if close:
        z.close()
    return dict(
        extract=f"{unit['prefix']}_SOURCE_EXTRACT", version=EXTRACT_VERSION, stage=STAGE,
        unit_id=unit["unit_id"], lesson_title=unit["lesson_title"],
        topik=unit["topik"], bahagian=unit["bahagian"],
        authority_inherited=AUTHORITY,
        boundary=dict(
            raw_start_anchor=unit["start_anchor"], raw_stop_anchor=unit["stop_anchor"],
            frozen_start_paragraph=unit["frozen_start"],
            frozen_stop_paragraph=unit["frozen_stop"],
            module_pages=list(unit["module_pages"]), subtopics=unit["subtopics"],
            shared_start=unit["shared_start"], shared_end=unit["shared_end"],
            preceding_unit=unit["preceding_unit"], following_unit=unit["following_unit"],
            extraction_method="HEADING_ANCHOR_BODY_CHILD_SLICE_NEVER_PAGE_RANGE",
            anchor_search=anchor_search, paragraph_enumeration=enumeration),
        docx_probe=probe,
        page_attribution=pdf_pages if pdf_pages.get("available") else page_attribution,
        page_attribution_primary=("TYPESET_PDF" if pdf_pages.get("available")
                                  else "WORD_CACHED_LAYOUT"),
        page_attribution_secondary=page_attribution,
        page_attribution_divergence=dict(
            cached_layout_range=[page_attribution["first_page"],
                                 page_attribution["last_page"]],
            typeset_range=[pdf_pages.get("first_page"), pdf_pages.get("last_page")],
            frozen_map_range=list(unit["module_pages"]),
            cached_layout_agrees_with_frozen=page_attribution["matches_frozen_map"],
            typeset_agrees_with_frozen=pdf_pages.get("matches_frozen_map"),
            note=("Two independent readings are kept. Where they disagree the typeset PDF "
                  "governs, because it is what a reader actually holds; Word's cached "
                  "layout is advisory and was wrong on every unit in this batch.")),
        boundary_proof=dict(
            neighbour_window=NEIGHBOUR_WINDOW,
            excluded_before=excluded_before, excluded_after=excluded_after,
            included_first=_row_summary(body_paras[start_i], start_i,
                                        pages[0] if pages else None),
            included_last_index=start_i + len(seg) - 1,
            first_included_paragraph_index=start_i,
            last_included_paragraph_index=start_i + len(seg) - 1,
            excluded_before_indices=pre_idx, excluded_after_indices=post_idx),
        totals=dict(body_elements_in_span=len(seg), empty_spacing_paragraphs=empty,
                    content_rows=len(rows),
                    headings=sum(1 for r in rows if r["content_type"].startswith("HEADING")),
                    paragraphs=sum(1 for r in rows if r["content_type"] == "PARAGRAPH"),
                    numbered_paragraphs=len(lists),
                    list_item_rows=sum(1 for r in rows if r["content_type"] == "LIST_ITEM"),
                    tables=len(tables),
                    diagrams=sum(1 for r in rows if r["content_type"] == "DIAGRAM"),
                    raster_images=sum(1 for r in rows if r["content_type"] == "IMAGE"),
                    assets=len(assets)),
        rows=rows, assets=assets, lists=lists, tables=tables)


# ==========================================================================================
# PAGE ATTRIBUTION — from the typeset PDF, not from Word's cached layout
#
# The T04 extractor attributed pages by counting <w:lastRenderedPageBreak>. That is Word's
# cached layout, and on T04 it happened to land on the frozen range exactly. On all four of
# these units it does not: it under-counts the last page of T03-B03, T03-B04 and T05-B01 by
# one, and over-counts T06-B01 by one. Trusting it would have published a wrong page range
# for every unit in this batch while the frozen map was right all along.
#
# The rendered PDF is a real typeset artifact, hash-verified in Lane 1, and it prints its own
# module page number in the footer. So page attribution now comes from finding the text on a
# page whose footer says which page it is. The cached-layout number is still computed and
# still reported — as the weaker second opinion it always was.
PDF_FOOTER_RE = "Mukasurat"
_PDF_INDEX = None


def pdf_page_index():
    """module page number -> text of that page, built once from the rendered PDF."""
    global _PDF_INDEX
    if _PDF_INDEX is not None:
        return _PDF_INDEX
    import re
    try:
        import fitz
    except ImportError:
        _PDF_INDEX = {}
        return _PDF_INDEX
    path, how = SRC.k5_binary_path()
    if path is None:
        _PDF_INDEX = {}
        return _PDF_INDEX
    with zipfile.ZipFile(path) as z:
        data = z.read(SRC.K5_ZIP_MEMBER_PDF)
    if hashlib.sha256(data).hexdigest() != SRC.K5_PDF_SHA256:
        raise ExtractionError("rendered PDF identity mismatch — refusing to attribute pages")
    doc = fitz.open(stream=data, filetype="pdf")
    idx = {}
    for pno in range(doc.page_count):
        txt = doc[pno].get_text()
        m = re.search(PDF_FOOTER_RE + r"\s*(\d+)", txt)
        if m:
            idx[int(m.group(1))] = txt
    doc.close()
    _PDF_INDEX = idx
    return idx


def _pdf_attribute(rows, module_pages):
    """Give every row the module page whose typeset text contains it."""
    idx = pdf_page_index()
    lo, hi = module_pages
    window = [p for p in range(lo, hi + 1) if p in idx]
    if not window:
        return dict(available=False,
                    reason="no PDF pages in range — attribution left on cached layout")
    flat = {p: " ".join(idx[p].split()) for p in window}
    found, unresolved, cur = 0, [], lo
    for r in rows:
        needle = " ".join((r["raw_source_text"] or "").split())[:60]
        hit = None
        if len(needle) >= 12:
            # Search forward from the current page only. "Fungsi" and "Fokus Utama
            # Kontraktor" repeat once per component, and a plain first-match search sent
            # every one of them back to the page where the phrase first appeared — six
            # components' worth of rows all claiming page 250.
            for p in [x for x in window if x >= cur]:
                if needle in flat[p]:
                    hit = p
                    break
        if hit is None:
            unresolved.append(r["row_id"])
            r["module_page"] = cur                    # carried forward, and recorded as such
            r["module_page_basis"] = "CARRIED_FORWARD_FROM_PREVIOUS_ROW"
        else:
            found += 1
            cur = hit
            r["module_page"] = hit
            r["module_page_basis"] = "TYPESET_PDF_FOOTER"
    pages = [r["module_page"] for r in rows]
    return dict(available=True, method="typeset PDF page whose footer names the module page",
                authority="TYPESET_ARTIFACT_HASH_VERIFIED",
                resolved_rows=found, carried_forward_rows=len(unresolved),
                carried_forward_row_ids=unresolved[:12],
                first_page=min(pages) if pages else None,
                last_page=max(pages) if pages else None,
                distinct_pages=sorted(set(pages)),
                expected=list(module_pages),
                matches_frozen_map=((min(pages), max(pages)) == tuple(module_pages)
                                    if pages else False),
                note=("Rows whose text could not be located — headings that Word numbers, "
                      "captionless figures, empty table rows — carry the previous row's page "
                      "and say so, rather than being silently assigned one."))


def _extent(el):
    for e in el.iter():
        if e.tag.endswith("}extent"):
            return (round(int(e.get("cx")) / 914400.0, 2),
                    round(int(e.get("cy")) / 914400.0, 2))
    return None


def _mime(part):
    if not part:
        return None
    ext = os.path.splitext(part)[1].lower().lstrip(".")
    return {"png": "image/png", "jpeg": "image/jpeg", "jpg": "image/jpeg",
            "emf": "image/emf", "wmf": "image/wmf", "gif": "image/gif"}.get(ext, "unknown")


def extract_all():
    z, probe = _open_module()
    try:
        return {u["unit_id"]: extract(u, z, probe) for u in UNITS}
    finally:
        z.close()


# ==========================================================================================
# EQUIVALENCE — this reader checked against the frozen T04 extract it generalises
# ==========================================================================================
T04_FROZEN = os.path.join(PL06, "t04", "T04_SOURCE_EXTRACT_v1.json")


def t04_equivalence():
    """Run THIS extractor over T04's boundary and compare with the committed extract.

    Without this, a new reader could quietly disagree with the old one about the very unit
    both have read, and the difference would first surface as a mystery in a new unit.
    """
    if not os.path.exists(T04_FROZEN):
        return dict(ran=False, reason="frozen T04 extract not on disk")
    frozen = json.load(open(T04_FROZEN, encoding="utf-8"))
    z, probe = _open_module()
    try:
        got = extract(T04_PARAMS, z, probe)
    finally:
        z.close()
    ft, gt = frozen["totals"], got["totals"]
    keys = ["body_elements_in_span", "empty_spacing_paragraphs", "content_rows", "headings",
            "paragraphs", "numbered_paragraphs", "list_item_rows", "tables", "diagrams"]
    frows = frozen["rows"]
    grows = got["rows"]
    text_mismatches = [
        dict(sequence=f["sequence"], frozen=f["raw_source_text"][:70],
             got=g["raw_source_text"][:70])
        for f, g in zip(frows, grows) if f["raw_source_text"] != g["raw_source_text"]]
    type_mismatches = [
        dict(sequence=f["sequence"], frozen=f["content_type"], got=g["content_type"])
        for f, g in zip(frows, grows) if f["content_type"] != g["content_type"]]
    para_mismatches = [
        dict(sequence=f["sequence"], frozen=f["source_paragraph_start"],
             got=g["source_paragraph_start"])
        for f, g in zip(frows, grows)
        if f["source_paragraph_start"] != g["source_paragraph_start"]]
    return dict(
        ran=True,
        totals_compared=keys,
        totals_differing={k: dict(frozen=ft[k], got=gt[k]) for k in keys if ft[k] != gt[k]},
        frozen_row_count=len(frows), got_row_count=len(grows),
        row_count_matches=len(frows) == len(grows),
        text_mismatches=text_mismatches, type_mismatches=type_mismatches,
        paragraph_index_mismatches=para_mismatches,
        equivalent=(len(frows) == len(grows) and not text_mismatches
                    and not type_mismatches and not para_mismatches
                    and not [k for k in keys if ft[k] != gt[k]]),
        note=("The generalised reader is only trusted on four new units because it reproduces "
              "the frozen T04 extract exactly on the unit it did not write."))


# ==========================================================================================
# LEAK PROOF — a claim about specific paragraphs, not a reassurance
# ==========================================================================================
def leak_report(extracts):
    """Prove no unit's rows carry a paragraph that belongs to a neighbour."""
    spans = {uid: (e["boundary_proof"]["first_included_paragraph_index"],
                   e["boundary_proof"]["last_included_paragraph_index"])
             for uid, e in extracts.items()}
    out = []
    for uid, e in extracts.items():
        lo, hi = spans[uid]
        idxs = [r["source_paragraph_start"] for r in e["rows"]
                if r["source_paragraph_start"] is not None]
        outside = [i for i in idxs if not (lo <= i <= hi)]
        # A row of THIS unit landing inside ANOTHER extracted unit's span is the leak that
        # matters, and it is checked by name rather than by trusting the slice.
        cross = {other: [i for i in idxs if spans[other][0] <= i <= spans[other][1]]
                 for other in extracts if other != uid}
        cross = {k: v for k, v in cross.items() if v}
        u = next(x for x in UNITS if x["unit_id"] == uid)
        out.append(dict(
            unit_id=uid, shared_start=u["shared_start"], shared_end=u["shared_end"],
            span=[lo, hi], rows_with_paragraph_index=len(idxs),
            paragraph_indices_outside_own_span=outside,
            rows_landing_in_another_units_span=cross,
            first_excluded_before=(e["boundary_proof"]["excluded_before"][-1]["text"]
                                   if e["boundary_proof"]["excluded_before"] else None),
            first_excluded_after=(e["boundary_proof"]["excluded_after"][0]["text"]
                                  if e["boundary_proof"]["excluded_after"] else None),
            clean=not outside and not cross))
    # Adjacent T03 units must abut exactly: B03 ends where B04 begins, with nothing dropped.
    b3 = spans.get("K5-PL06-T03-B03")
    b4 = spans.get("K5-PL06-T03-B04")
    abut = dict(
        pair="K5-PL06-T03-B03 → K5-PL06-T03-B04",
        b03_last_included=b3[1] if b3 else None,
        b04_first_included=b4[0] if b4 else None,
        contiguous=(b3 is not None and b4 is not None and b3[1] + 1 == b4[0]),
        gap=(b4[0] - b3[1] - 1) if (b3 and b4) else None,
        note=("The two units share module page 255. If the slice were page-wise, one of them "
              "would carry the other's paragraphs. Contiguous with a gap of zero means the "
              "heading anchor split exactly, losing nothing and duplicating nothing."))
    return dict(units=out, adjacency=abut,
                all_clean=all(u["clean"] for u in out) and abut["contiguous"])


if __name__ == "__main__":
    ex = extract_all()
    os.makedirs(OUT_DIR, exist_ok=True)
    for uid, data in ex.items():
        p = os.path.join(OUT_DIR, f"{uid.replace('-', '_')}_SOURCE_EXTRACT_v1.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
            f.write("\n")
        t = data["totals"]
        print(f"{uid}: rows={t['content_rows']:>3} headings={t['headings']:>2} "
              f"tables={t['tables']} images={t['raster_images']} "
              f"diagrams={t['diagrams']} assets={t['assets']} "
              f"pages={data['page_attribution']['first_page']}-"
              f"{data['page_attribution']['last_page']} "
              f"({'page match' if data['page_attribution']['matches_frozen_map'] else 'PAGE MISMATCH'})")
    eq = t04_equivalence()
    print("\nT04 equivalence:", "OK" if eq.get("equivalent") else eq)
    lk = leak_report(ex)
    print("leak report:", "CLEAN" if lk["all_clean"] else lk)
    print("adjacency:", lk["adjacency"]["contiguous"], "gap", lk["adjacency"]["gap"])
