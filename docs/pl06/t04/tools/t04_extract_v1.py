# -*- coding: utf-8 -*-
"""Stage 4.2F-B0 — controlled source extraction for K5-PL06-T04-B01.

Reads the primary module DOCX from temporary staging and writes
`T04_SOURCE_EXTRACT_v1.json`, which becomes the ONE controlled data source for every other
T04 artifact. The DOCX is never committed and is deleted at the end of the stage, so this
extract has to carry everything a later stage needs to verify the work without it.

    python3 t04_extract_v1.py <path-to-docx> <outdir>

BOUNDARY DISCIPLINE
-------------------
Extraction anchors on the RAW body heading, typo and all:

    4.0 PENJAAGAAN DAN PENYELENGGARAAN     <- body, misspelled, this is the anchor
    4.0 PENJAGAAN DAN PENYELENGGARAAN      <- TOC / governed label, NOT an anchor

Searching for the correctly spelled string finds the table-of-contents entry and nothing in
the body. That is the whole reason the freeze package recorded the typo instead of fixing it.

PARAGRAPH INDEX DISCIPLINE
--------------------------
The frozen boundary map's anchors — paragraph 5220 to before 5360 — hold under ONE
enumeration: direct `<w:p>` children of `<w:body>`, which is what python-docx's
`Document.paragraphs` returns and which EXCLUDES paragraphs nested inside tables. Counting
every `<w:p>` anywhere in the body instead gives 6534 and 6674 — the same 140-paragraph span,
shifted by 1314.

Both enumerations are recorded below. Extraction walks body CHILDREN between the two anchor
elements, so a table inside the boundary would be captured even though the index that located
the boundary cannot see one.
"""
import hashlib, json, os, re, sys
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
DGM = "{http://schemas.openxmlformats.org/drawingml/2006/diagram}"

UNIT_ID = "K5-PL06-T04-B01"
RAW_START_ANCHOR = "PENJAAGAAN DAN PENYELENGGARAAN"
GOVERNED_START_LABEL = "PENJAGAAN DAN PENYELENGGARAAN"
RAW_STOP_ANCHOR = "PENGURUSAN KUALITI PROJEK"
EXPECTED_START_PARA = 5220
EXPECTED_STOP_PARA = 5360
EXPECTED_MODULE_PAGES = (276, 283)
EXPECTED_DOCX_BYTES = 16832861
EXPECTED_DOCX_SHA256 = "5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7"

MODULE_ATTESTED = "MODULE_SOURCE_ATTESTED"


class ExtractionError(RuntimeError):
    """Fail closed. Never fall back to a looser anchor or a page slice."""


def _text(el):
    return "".join(t.text or "" for t in el.iter(f"{W}t"))


def _style(p):
    e = p.find(f"{W}pPr/{W}pStyle")
    return e.get(f"{W}val") if e is not None else None


def _numpr(p):
    np = p.find(f"{W}pPr/{W}numPr")
    if np is None:
        return None
    nid, ilvl = np.find(f"{W}numId"), np.find(f"{W}ilvl")
    return dict(num_id=nid.get(f"{W}val") if nid is not None else None,
                level=int(ilvl.get(f"{W}val")) if ilvl is not None else 0)


def extract(docx_path, raw_start_anchor=RAW_START_ANCHOR, raw_stop_anchor=RAW_STOP_ANCHOR,
            expected_start=EXPECTED_START_PARA, expected_stop=EXPECTED_STOP_PARA):
    import zipfile
    raw = open(docx_path, "rb").read()
    probe = dict(filename=os.path.basename(docx_path), bytes=len(raw),
                 sha256=hashlib.sha256(raw).hexdigest())
    probe["identity_matches_expected"] = (probe["bytes"] == EXPECTED_DOCX_BYTES
                                          and probe["sha256"] == EXPECTED_DOCX_SHA256)
    if not probe["identity_matches_expected"]:
        raise ExtractionError("DOCX identity mismatch — refusing to read")

    z = zipfile.ZipFile(docx_path)
    body = ET.fromstring(z.read("word/document.xml")).find(f"{W}body")
    kids = list(body)
    body_paras = [c for c in kids if c.tag == f"{W}p"]        # python-docx enumeration
    all_paras = list(body.iter(f"{W}p"))                      # includes table-nested

    def find_idx(seq, s):
        return [i for i, p in enumerate(seq) if _text(p).strip() == s]

    hits_raw = find_idx(body_paras, raw_start_anchor)
    hits_gov = find_idx(body_paras, GOVERNED_START_LABEL)
    hits_stop = find_idx(body_paras, raw_stop_anchor)
    probe["anchor_search"] = dict(
        raw_start_anchor=raw_start_anchor, raw_start_hits=hits_raw,
        governed_label=GOVERNED_START_LABEL, governed_label_body_hits=hits_gov,
        raw_stop_anchor=raw_stop_anchor, raw_stop_hits=hits_stop,
        note="The governed label returns no BODY heading. Anchoring on it would find only the "
             "table-of-contents entry, which carries a page number and is not a section start.")
    if not hits_raw:
        raise ExtractionError(f"raw start anchor not found: {raw_start_anchor!r}")
    if not hits_stop:
        raise ExtractionError(f"raw stop anchor not found: {raw_stop_anchor!r}")

    start_i, stop_i = hits_raw[0], hits_stop[0]
    probe["paragraph_enumeration"] = dict(
        body_child_paragraph_count=len(body_paras),
        all_paragraph_count=len(all_paras),
        enumeration_used="DIRECT_W_P_CHILDREN_OF_W_BODY (python-docx Document.paragraphs)",
        start_index=start_i, stop_index=stop_i, span=stop_i - start_i,
        expected_start=expected_start, expected_stop=expected_stop,
        start_matches_expected=start_i == expected_start,
        stop_matches_expected=stop_i == expected_stop,
        alternate_enumeration=dict(
            name="EVERY_W_P_IN_BODY_INCLUDING_TABLE_CELLS",
            start_index=find_idx(all_paras, raw_start_anchor)[0],
            stop_index=find_idx(all_paras, raw_stop_anchor)[0],
            offset_from_used=find_idx(all_paras, raw_start_anchor)[0] - start_i))
    if start_i != expected_start or stop_i != expected_stop:
        raise ExtractionError(
            f"anchors resolve to {start_i}/{stop_i}, frozen map says "
            f"{expected_start}/{expected_stop}")

    si, ei = kids.index(body_paras[start_i]), kids.index(body_paras[stop_i])
    seg = kids[si:ei]
    probe["body_child_span"] = dict(first=si, last_exclusive=ei, elements=len(seg))

    # ---- page attribution ----
    # Word caches its last layout as <w:lastRenderedPageBreak>. The unit's first paragraph
    # carries the break that STARTED module page 276, so the counter opens one below.
    page = EXPECTED_MODULE_PAGES[0] - 1
    pages, breaks = [], 0
    for el in seg:
        n = (sum(1 for _ in el.iter(f"{W}lastRenderedPageBreak"))
             + sum(1 for b in el.iter(f"{W}br") if b.get(f"{W}type") == "page"))
        page += n
        breaks += n
        pages.append(page)
    probe["page_attribution"] = dict(
        method="w:lastRenderedPageBreak plus explicit w:br type=page",
        authority="ADVISORY_CACHED_LAYOUT",
        page_break_markers=breaks,
        first_page=pages[0], last_page=pages[-1],
        distinct_pages=sorted(set(pages)),
        expected=list(EXPECTED_MODULE_PAGES),
        matches_frozen_map=(pages[0], pages[-1]) == EXPECTED_MODULE_PAGES,
        caveat="These markers are Word's cached layout, not a typeset guarantee. They are "
               "treated as corroboration because eight distinct pages fall exactly on the "
               "276-283 range the frozen boundary map records, not as independent authority.")

    # ---- rows ----
    rels = {r.get("Id"): r.get("Target")
            for r in ET.fromstring(z.read("word/_rels/document.xml.rels"))}
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
                    cells.append(dict(text=_text(tc).strip(),
                                      grid_span=int(span.get(f"{W}val")) if span is not None else 1,
                                      v_merge=(vm.get(f"{W}val") or "continue") if vm is not None else None))
                grid.append(cells)
            tid = f"T04-TBL-{len(tables) + 1:02d}"
            tables.append(dict(table_id=tid, unit_id=UNIT_ID, sequence=seq,
                               heading_path=[x for x in (h1, h2, h3) if x],
                               rows=len(grid), columns=max((len(r) for r in grid), default=0),
                               merged_cells=sum(1 for r in grid for c in r
                                                if c["grid_span"] > 1 or c["v_merge"]),
                               module_page=pg, segment_index=i, grid=grid))
            rows.append(dict(row_id=f"T04-ROW-{seq:03d}", unit_id=UNIT_ID, sequence=seq,
                             heading_path=[x for x in (h1, h2, h3) if x],
                             content_type="TABLE", raw_source_text="",
                             controlled_display_text="", source_paragraph_start=None,
                             source_paragraph_end=None, module_page=pg,
                             docx_relationship_id=None, authority_class=MODULE_ATTESTED,
                             normalisation_status="NOT_NORMALISED",
                             visual_relationship=None, table_relationship=tid,
                             external_claim_status="NONE", segment_index=i))
            continue

        txt = _text(el).strip()
        st = _style(el)
        num = _numpr(el)
        dgm = next((e for e in el.iter(f"{DGM}relIds")), None)

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
            extent = None
            for e in el.iter():
                if e.tag.endswith("}extent"):
                    extent = (round(int(e.get("cx")) / 914400.0, 2),
                              round(int(e.get("cy")) / 914400.0, 2))
                    break
            aid = f"T04-DGM-{len(assets) + 1:02d}"
            assets.append(dict(
                asset_id=aid, unit_id=UNIT_ID,
                relationship_id=",".join(f"{k.split('}')[-1]}={v}" for k, v in dgm.attrib.items()),
                embedded_filename=data_part, mime_type="application/xml (SmartArt diagram data)",
                dimensions_in=f"{extent[0]} x {extent[1]}" if extent else None,
                sha256=hashlib.sha256(dbytes).hexdigest(),
                nearest_heading=h1, source_paragraph=start_i + i, module_page=pg,
                caption=None, source_subject_nodes=nodes, node_count=len(nodes),
                proposed_storyboard_role="PROCESS_FLOW_VISUAL",
                source_bound_status="SOURCE_BOUND_CAPTIONLESS",
                asset_kind="SMARTART_DIAGRAM_NOT_RASTER"))
            rows.append(dict(row_id=f"T04-ROW-{seq:03d}", unit_id=UNIT_ID, sequence=seq,
                             heading_path=[x for x in (h1, h2, h3) if x],
                             content_type="DIAGRAM", raw_source_text="",
                             controlled_display_text="", source_paragraph_start=start_i + i,
                             source_paragraph_end=start_i + i, module_page=pg,
                             docx_relationship_id=rid, authority_class=MODULE_ATTESTED,
                             normalisation_status="NOT_NORMALISED",
                             visual_relationship=aid, table_relationship=None,
                             external_claim_status="NONE", segment_index=i))
            continue

        if not txt:
            continue                                        # empty spacing paragraph

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
        rid_ = f"T04-ROW-{seq:03d}"
        # The only normalisation this stage performs: the misspelled Heading 1 gets a governed
        # display label. Everything else is passed through verbatim, and the raw string is
        # kept beside the display string in every row regardless.
        if ctype == "HEADING_1" and txt == RAW_START_ANCHOR:
            disp, norm = GOVERNED_START_LABEL, "RECORDED_NOT_SILENTLY_CORRECTED"
        else:
            disp, norm = txt, "NOT_NORMALISED"

        if num is not None:
            lists.append(dict(list_item_id=f"T04-LI-{len(lists) + 1:03d}", row_id=rid_,
                              unit_id=UNIT_ID, sequence=seq, num_id=num["num_id"],
                              level=num["level"],
                              marker_type="ORDERED_OR_BULLET_PER_numbering.xml",
                              style=st or "", heading_path=[x for x in (h1, h2, h3) if x],
                              module_page=pg, raw_wording=txt))

        rows.append(dict(row_id=rid_, unit_id=UNIT_ID, sequence=seq,
                         heading_path=[x for x in (h1, h2, h3) if x],
                         content_type=ctype, raw_source_text=txt,
                         controlled_display_text=disp,
                         source_paragraph_start=start_i + i, source_paragraph_end=start_i + i,
                         module_page=pg, docx_relationship_id=None,
                         authority_class=MODULE_ATTESTED, normalisation_status=norm,
                         visual_relationship=None, table_relationship=None,
                         external_claim_status="PENDING_CLASSIFICATION",
                         segment_index=i, list_level=num["level"] if num else None,
                         paragraph_style=st))

    empty = sum(1 for el in seg
                if el.tag == f"{W}p" and not _text(el).strip()
                and next((e for e in el.iter(f"{DGM}relIds")), None) is None)
    return dict(
        extract="T04_SOURCE_EXTRACT", version="v1", stage="4.2F-B0", unit_id=UNIT_ID,
        lesson_title="Penjagaan dan Penyelenggaraan",
        topik=4, bahagian=1,
        boundary=dict(
            raw_start_anchor=RAW_START_ANCHOR,
            governed_start_label=GOVERNED_START_LABEL,
            normalisation_status="RECORDED_NOT_SILENTLY_CORRECTED",
            normalisation_authority="K5-STR-005 table of contents, per the frozen boundary map; "
                                    "REFERENCED_NOT_FROZEN — the artifact is not in custody",
            raw_stop_anchor=RAW_STOP_ANCHOR,
            module_pages=list(EXPECTED_MODULE_PAGES),
            subtopics="4.1 Landskap Lembut + 4.2 Landskap Kejur"),
        docx_probe=probe,
        totals=dict(body_elements_in_span=len(seg),
                    empty_spacing_paragraphs=empty,
                    content_rows=len(rows),
                    headings=sum(1 for r in rows if r["content_type"].startswith("HEADING")),
                    paragraphs=sum(1 for r in rows if r["content_type"] == "PARAGRAPH"),
                    # Two different counts, both needed. 61 paragraphs carry <w:numPr>, but
                    # most of those are Heading3 runs that Word numbered; only 12 are
                    # ListParagraph-styled list items. A single "list" total would hide that.
                    numbered_paragraphs=len(lists),
                    list_item_rows=sum(1 for r in rows if r["content_type"] == "LIST_ITEM"),
                    tables=len(tables),
                    diagrams=sum(1 for r in rows if r["content_type"] == "DIAGRAM"),
                    raster_images=0,
                    assets=len(assets)),
        rows=rows, assets=assets, lists=lists, tables=tables)


if __name__ == "__main__":
    docx, outdir = sys.argv[1], sys.argv[2]
    data = extract(docx)
    os.makedirs(outdir, exist_ok=True)
    p = os.path.join(outdir, "T04_SOURCE_EXTRACT_v1.json")
    json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(p, "a", encoding="utf-8").write("\n")
    print("wrote", p)
    for k, v in data["totals"].items():
        print(f"  {k:<28} {v}")
