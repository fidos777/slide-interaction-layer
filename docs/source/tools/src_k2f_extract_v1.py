# -*- coding: utf-8 -*-
"""Stage 4.2F-F — measure the K2 binary and freeze the ground truth.

    docs/source/.venv-k2/bin/python docs/source/tools/src_k2f_extract_v1.py

WHAT CHANGED SINCE STAGE 4.2F-E
-------------------------------
Stage 4.2F-E could not find the K2 binary on its box. It recorded every field that
needs the bytes as UNKNOWN_NOT_MEASURED and refused to move the custody status. The
binary is now present on local disk at

    .source-intake/K2/2. PENGURUSAN PEMBINAAN LANDASAN.pdf

and its identity was verified before any measurement was taken:

    bytes  = 25,043,306                        (matches the brief)
    sha256 = 0b2d81dd..f405680                  (matches the brief — computed from the bytes)
    pages  = 346                               (matches the brief)

Only after that check did this script open the file and MEASURE the values that were
previously unknown. Nothing here is inferred: every number is read from the bytes, and
the result is frozen to K2_EXTRACTION_EVIDENCE_v1.json so the downstream artifacts —
and the QA gates — can be checked without re-opening a git-ignored binary.

The one thing this script does NOT do is decide anything instructional. It reports what
the pages say, including where the source contradicts itself; the conflicts are routed,
not resolved.
"""
import hashlib
import json
import os
import re
import sys

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    sys.exit("PyMuPDF not importable. Use the venv: .venv-k2/bin/python")

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(SRC_DIR))
BINARY = os.path.join(REPO, ".source-intake", "K2",
                      "2. PENGURUSAN PEMBINAAN LANDASAN.pdf")

STAGE = "4.2F-F"
EXPECTED = dict(bytes=25043306,
                sha256="0b2d81dda46eaf4fb018a20a78f7f9b2870129c61125768e4438937f3f405680",
                pages=346)

# Region spans confirmed from the source's own repeated footers. Every span is verified
# below against the package's self-declared 'Muka Surat: n/N' total before it is trusted.
PL_SPANS = {"PL01": (85, 124), "PL02": (125, 144), "PL03": (145, 184),
            "PL04": (185, 201), "PL05": (202, 225), "PL06": (226, 259),
            "PL07": (260, 270), "PL08": (271, 299), "PL09": (300, 318)}
PT_SPANS = {"PT01": (23, 30), "PT02": (31, 36), "PT03": (37, 43), "PT04": (44, 50),
            "PT05": (51, 57), "PT06": (58, 64), "PT07": (65, 70), "PT08": (71, 78),
            "PT09": (79, 84)}
KT_SPANS = [("KT01", 319, 321, "PL01"), ("KT02", 322, 324, "PL02"),
            ("KT03", 325, 327, "PL03"), ("KT04", 328, 330, "PL04"),
            ("KT05", 331, 333, "PL05"), ("KT06", 334, 337, "PL06"),
            ("KT07", 338, 340, "PL07"), ("KT PL08", 341, 343, "PL08"),
            ("KT PL09", 344, 346, "PL09")]
FRONT_MATTER = (1, 22)
TEACHING_PLAN_REGION = (23, 84)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _clean(lines):
    return [l.strip() for l in lines if l.strip()]


def measure():
    identity = dict(
        path=os.path.relpath(BINARY, REPO),
        bytes_observed=os.path.getsize(BINARY),
        sha256_observed=_sha256(BINARY),
        bytes_expected=EXPECTED["bytes"],
        sha256_expected=EXPECTED["sha256"])
    identity["bytes_match"] = identity["bytes_observed"] == identity["bytes_expected"]
    identity["sha256_match"] = identity["sha256_observed"] == identity["sha256_expected"]
    if not (identity["bytes_match"] and identity["sha256_match"]):
        raise SystemExit("binary identity does not match the brief — refusing to measure")

    doc = fitz.open(BINARY)
    identity["pages_observed"] = doc.page_count
    identity["pages_expected"] = EXPECTED["pages"]
    identity["pages_match"] = doc.page_count == EXPECTED["pages"]
    identity["encrypted"] = bool(doc.is_encrypted)
    identity["needs_password"] = bool(doc.needs_pass)
    identity["pdf_format"] = doc.metadata.get("format")
    identity["pdf_metadata"] = {k: doc.metadata.get(k) for k in
                                ("title", "author", "creator", "producer",
                                 "creationDate", "modDate")}

    pages = [doc.load_page(i).get_text() for i in range(doc.page_count)]
    chars_total = sum(len(p) for p in pages)

    lat = re.compile(r"\bLATIHAN\b", re.I)
    skm = re.compile(r"SKEMA\s+JAWAPAN", re.I)

    def images_in(a, b):
        n = 0
        for i in range(a, b + 1):
            n += len(doc.load_page(i - 1).get_images(full=True))
        return n

    def tables_in(a, b):
        n = 0
        for i in range(a, b + 1):
            try:
                n += len(doc.load_page(i - 1).find_tables().tables)
            except Exception:
                pass
        return n

    # ---- PL packages: verify each span against the package's own declared length ----
    pl_title_re = {pl: re.compile(rf"{pl}[:\s]+([^\n]+)") for pl in PL_SPANS}
    declared_re = re.compile(r"(?:Muka\s*surat|Page)\s*[:：]?\s*1\s*/\s*(\d+)", re.I)
    pl_rows = []
    for pl, (a, b) in PL_SPANS.items():
        span_pages = b - a + 1
        head = pages[a - 1]
        m = declared_re.search(head)
        declared = int(m.group(1)) if m else None
        # module code from the package's own header
        mm = re.search(r"\bM0(\d)\b", head)
        module = "M0" + mm.group(1) if mm else None
        # official title from the package's own first page
        tm = pl_title_re[pl].search(head)
        title = " ".join(tm.group(1).split()) if tm else None
        lat_pages = [i for i in range(a, b + 1) if lat.search(pages[i - 1])]
        skm_pages = [i for i in range(a, b + 1) if skm.search(pages[i - 1])]
        pl_rows.append(dict(
            pl=pl, pdf_start_page=a, pdf_end_page=b, span_pages=span_pages,
            declared_pages=declared,
            span_matches_declared=(declared == span_pages),
            module_code_from_own_header=module,
            official_title=title,
            latihan_pages=lat_pages, latihan_page_count=len(lat_pages),
            skema_jawapan_pages=skm_pages, skema_jawapan_page_count=len(skm_pages),
            image_count=images_in(a, b),
            table_detector_count=tables_in(a, b)))

    # ---- KT competency task papers (the back-matter assessment region) ----
    uk_re = re.compile(r"UNIT\s+KOMPETENSI\s*\n?\s*(.+?)(?:\n\s*NAMA|\n\s*A\.|\n\s*TEMPOH)",
                       re.S | re.I)
    kt_rows = []
    for code, a, b, pl in KT_SPANS:
        head = pages[a - 1]
        m = uk_re.search(head)
        unit = " ".join(m.group(1).split()) if m else None
        kt_rows.append(dict(kt_code=code, pdf_start_page=a, pdf_end_page=b,
                            span_pages=b - a + 1, positional_pl=pl,
                            printed_unit_competency=unit))

    # ---- region accounting: every one of the 346 pages assigned to exactly one region ----
    assigned = {}
    def claim(a, b, name):
        for i in range(a, b + 1):
            assigned.setdefault(i, []).append(name)
    claim(*FRONT_MATTER, "FRONT_MATTER")
    claim(*TEACHING_PLAN_REGION, "TEACHING_PLANS")
    for pl, (a, b) in PL_SPANS.items():
        claim(a, b, pl)
    for code, a, b, _ in KT_SPANS:
        claim(a, b, "KT_REGION")
    unassigned = [i for i in range(1, doc.page_count + 1) if i not in assigned]
    overlaps = {i: r for i, r in assigned.items() if len(r) > 1}

    evidence = dict(
        stage=STAGE,
        generated_by="docs/source/tools/src_k2f_extract_v1.py",
        binary_identity=identity,
        text=dict(chars_total=chars_total,
                  chars_per_page=round(chars_total / doc.page_count, 1),
                  connector_chars_stage_4_2F_E=62638,
                  ratio_full_over_connector=round(chars_total / 62638, 1)),
        regions=dict(front_matter=list(FRONT_MATTER),
                     teaching_plan_region=list(TEACHING_PLAN_REGION),
                     pl_packages_region=[85, 318],
                     kt_assessment_region=[319, 346]),
        region_accounting=dict(pages_total=doc.page_count,
                               pages_assigned=len(assigned),
                               unassigned_pages=unassigned,
                               overlapping_pages=overlaps,
                               clean_partition=(not unassigned and not overlaps)),
        pl_packages=pl_rows,
        kt_papers=kt_rows,
        front_matter_images=images_in(*FRONT_MATTER),
        teaching_plan_images=images_in(*TEACHING_PLAN_REGION),
        kt_region_images=images_in(319, 346),
        totals=dict(
            images_total=images_in(1, doc.page_count),
            pl_pages_total=sum(r["span_pages"] for r in pl_rows),
            all_pl_spans_match_declared=all(r["span_matches_declared"]
                                            for r in pl_rows),
            kt_paper_count=len(kt_rows)))
    doc.close()
    return evidence


if __name__ == "__main__":
    ev = measure()
    out = os.path.join(SRC_DIR, "K2_EXTRACTION_EVIDENCE_v1.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(ev, f, ensure_ascii=False, indent=1)
        f.write("\n")
    i = ev["binary_identity"]
    print("wrote", os.path.relpath(out, REPO))
    print(f"  identity: bytes={i['bytes_match']} sha256={i['sha256_match']} "
          f"pages={i['pages_match']} encrypted={i['encrypted']}")
    print(f"  text: {ev['text']['chars_total']:,} chars "
          f"({ev['text']['ratio_full_over_connector']}x the connector read)")
    print(f"  clean 346-page partition: {ev['region_accounting']['clean_partition']}")
    print(f"  all PL spans match declared length: "
          f"{ev['totals']['all_pl_spans_match_declared']}")
    for r in ev["pl_packages"]:
        print(f"    {r['pl']} {r['pdf_start_page']}-{r['pdf_end_page']} "
              f"({r['span_pages']}p, declared {r['declared_pages']}) "
              f"{r['module_code_from_own_header']} img={r['image_count']} "
              f"tbl~{r['table_detector_count']} skema={r['skema_jawapan_pages']}")
    print(f"  KT papers: {ev['totals']['kt_paper_count']}")
