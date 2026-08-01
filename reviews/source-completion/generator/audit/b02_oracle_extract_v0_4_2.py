# -*- coding: utf-8 -*-
"""Extract expected values DIRECTLY from frozen Bariah OOXML.

The point of this module is independence. Nothing here imports the generator or any of
its helpers, so an expected value can never be produced by the same code that produced
the artifact under test.
"""
import os, re, sys, zipfile
from xml.etree import ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"

_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "..", "..", ".."))
_EV = os.path.join(_REPO, "reviews", "storyboard-bariah", "v0_3_bariah_review")
VBARIAH = os.path.join(_EV, "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx")
GUIDE = os.path.join(_EV, "Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx")


def slide_shapes(pptx, n):
    """(shape name, [paragraph strings]) for one slide of a frozen deck."""
    root = ET.fromstring(zipfile.ZipFile(pptx).read(f"ppt/slides/slide{n}.xml"))
    out = []
    for sp in root.iter(f"{P}sp"):
        nm = sp.find(f".//{P}cNvPr")
        paras = ["".join(t.text or "" for t in p.iter(f"{A}t")) for p in sp.iter(f"{A}p")]
        out.append((nm.get("name") if nm is not None else "", [x for x in paras if x]))
    return out


def slide_text(pptx, n):
    return [t for _, ps in slide_shapes(pptx, n) for t in ps]


def notes_runs(pptx, n):
    """Runs of a frozen deck's notes part: [(text, italic)]."""
    try:
        root = ET.fromstring(zipfile.ZipFile(pptx).read(f"ppt/notesSlides/notesSlide{n}.xml"))
    except KeyError:
        return []
    out = []
    for r in root.iter(f"{A}r"):
        rPr = r.find(f"{A}rPr"); t = r.find(f"{A}t")
        out.append(((t.text or "") if t is not None else "", rPr is not None and rPr.get("i") == "1"))
    return out


def docx_paragraphs(docx):
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    root = ET.fromstring(zipfile.ZipFile(docx).read("word/document.xml"))
    return ["".join(t.text or "" for t in p.iter(f"{W}t")) for p in root.iter(f"{W}p")]


# ---------------------------------------------------------------- oracles
def promenade_visual_direction():
    """Bariah's corrected Promenade popup, annotated deck slide 14.

    Returns the visual-direction line and its heading exactly as she left them.
    """
    txt = slide_text(VBARIAH, 14)
    heading = next((t for t in txt if t.strip().startswith("ARAHAN VISUAL")), None)
    direction = next((t for t in txt if t.strip().startswith("[Visual:")), None)
    subject = None
    if direction:
        m = re.match(r"\[Visual:\s*(.+?)\]\s*$", direction.strip())
        subject = m.group(1).strip() if m else None
    return dict(slide=14, heading=heading, direction=direction, subject=subject,
                contoh=next((t for t in txt if "Titiwangsa" in t), None))


def s01_visual_direction():
    """Bariah's corrected S01, annotated deck slide 2."""
    txt = slide_text(VBARIAH, 2)
    return dict(slide=2,
                visual=[t for t in txt if t.strip().startswith("[Visual:")],
                titles=[t for t in txt if "Topik 3 Bahagian 2" in t or "KURSUS KERJA" in t
                        or t.strip().startswith("PL06:")],
                standalone_component_title=[t for t in txt if t.strip() == "Komponen Landskap"])


def tamat_copy():
    """Bariah's corrected Tamat, annotated deck slide 75, plus its notes."""
    txt = slide_text(VBARIAH, 75)
    nt = "".join(t for t, _ in notes_runs(VBARIAH, 75))
    return dict(slide=75, canvas=[t for t in txt if not t.startswith("Bariah:")], notes=nt,
                superseded_marker=[t for t in txt if t.startswith("Bariah:")])


def quiz_answer_key():
    """Answer letters as Bariah left them in the corrected quiz notes, slide 73."""
    nt = "\n".join(t for t, _ in notes_runs(VBARIAH, 73))
    mcq = dict(re.findall(r"Soalan (\d) — MCQ.*?\nJawapan: ([A-D])", nt, re.S))
    mr = re.findall(r"^(.+?)\s*✓\s*$", nt, re.M)
    return dict(slide=73, mcq_answers=mcq, multiple_response_correct=[x.strip() for x in mr])


def guide_item(n):
    """A numbered decision cell from the completed review guide."""
    ps = docx_paragraphs(GUIDE)
    return [p for p in ps if p.strip()]


def klik_instruction():
    """Bariah's own screen-level instruction wording, from the corrected group master."""
    for n in (8, 12, 14):
        for t in slide_text(VBARIAH, n):
            if t.strip().startswith("Klik pada setiap"):
                return dict(slide=n, text=t.strip())
    return dict(slide=None, text=None)


if __name__ == "__main__":
    import json
    print(json.dumps(dict(promenade=promenade_visual_direction(), s01=s01_visual_direction(),
                          tamat=tamat_copy(), quiz=quiz_answer_key(), klik=klik_instruction()),
                     ensure_ascii=False, indent=1))
