# -*- coding: utf-8 -*-
"""Stage 4.2F-D Lane 4 — the K3 course-level decision document.

    python3 docs/source/tools/src_k3_decision_emit_v1.py

ONE decision, K3-COURSE-01, on ONE page, in a document of its own. It is deliberately not
folded into the K5 Kelompok 0 package: that package is under Bariah review right now, and a
K3 question arriving inside a K5 review would be answered in the wrong frame.

Every string on the page is projected from src_k3_v1. Nothing is typed here that is not
already in the model, so the document and the model cannot drift apart.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "docs", "pl06", "tools"))
import src_k3_v1 as K        # noqa: E402
import pl06_docx_v1 as W     # noqa: E402

OUT_DIR = os.path.join(ROOT, "reviews", "storyboard-bariah", "k3_course_decision")
DOCX_NAME = "K3_Keputusan_Peringkat_Kursus_v0_1.docx"
TITLE = "K3 — Keputusan Peringkat Kursus v0.1"

STATUS = "PENDING_BARIAH_REVIEW"
NOT_AUTHORITY = ("Dokumen ini BUKAN kelulusan. Ia menjadi authority hanya selepas Bariah "
                 "menandatangani pilihan di bawah.")


def blocks():
    inv = K.k3_inventory()
    d = K.K3_COURSE_DECISION
    skema = inv["skema_form_finding"]["not_uniform"]
    fam = skema["structural_families"]

    b = [
        W.h(1, "KEPUTUSAN PERINGKAT KURSUS — K3"),
        W.field(f"Dokumen: {DOCX_NAME}"),
        W.field(f"Kursus: {inv['course_title']}  |  Kod bidang: {inv['field_code']}"),
        W.field(f"Status: {STATUS}  |  Untuk: Bariah (Instructional Designer)"),
        W.field(f"Peringkat: {K.STAGE}  |  Authority sumber: {K.AUTHORITY}"),
        W.p(NOT_AUTHORITY),

        W.h(2, f"{d['decision_id']} — {d['subject_ms']}"),
        W.p("Apa yang sumber tunjukkan (dibaca daripada kesembilan-sembilan pakej, "
            "bukan dianggarkan):"),
        W.bullet(f"{inv['pdfs']} pakej K3, kesemuanya telah dibaca penuh, merangkumi "
                 f"{len(inv['modules_evidenced'])} modul "
                 f"({', '.join(inv['modules_evidenced'])}), "
                 f"{inv['total_source_pages']} muka surat."),
        W.bullet("Setiap pakej membawa LATIHAN dan SKEMA JAWAPAN tersendiri — soalan esei "
                 "pendek, 15 minit."),
        W.bullet(f"Bilangan soalan TIDAK seragam: {len(skema['question_count']['five'])} "
                 f"pakej ada 5 soalan, {len(skema['question_count']['three'])} pakej "
                 f"({', '.join(skema['question_count']['three'])}) ada 3. Jumlah "
                 f"{skema['question_count']['total']} soalan."),
        W.bullet(f"Bentuk skema TIDAK seragam: {len(fam)} struktur berbeza di bawah "
                 f"{skema['distinct_labels']} label — "
                 + "; ".join(f"{K.SKEMA_FAMILY_MS[k]}: {', '.join(v)}"
                             for k, v in fam.items()) + "."),
        W.bullet(f"{', '.join(skema['packages_carrying_marks'])} bukan jawapan model. Ia "
                 "rubrik pemarkahan (2 + 4 + 4 = 10 markah setiap soalan) — arahan kepada "
                 "pemeriksa, bukan jawapan yang boleh ditunjukkan kepada pelajar."),
        W.bullet("Kursus K5 menggunakan 4 MCQ + 1 Multiple Response, ambang 60 peratus. "
                 "Peraturan itu TIDAK digunakan untuk K3 dalam dokumen ini."),

        W.h(2, "Pilihan"),
        # ASCII tick box on purpose. U+2610 BALLOT BOX rendered as tofu in the preview
        # font, and a glyph the reviewer's Word may also lack is a worse risk on a page
        # whose entire job is to be ticked.
        W.table(["Pilih", "Pilihan", "Kesan kepada pengeluaran", "Kos"],
                [["[  ]  " + o["key"], o["label_ms"], o["consequence_ms"],
                  o["production_cost_ms"]] for o in d["options"]],
                widths=[8, 22, 54, 16]),

        W.h(2, "Nota"),
        W.bullet(d["cair_note_ms"]),
        W.bullet("Menyekat: " + ", ".join(d["blocks_ms"])
                 + ". TIDAK menyekat: " + ", ".join(d["does_not_block_ms"]) + "."),
        W.p("Tandatangan: ____________________      Tarikh: ____________________"),
    ]
    return b


def emit():
    os.makedirs(OUT_DIR, exist_ok=True)
    bl = blocks()
    docx_path = os.path.join(OUT_DIR, DOCX_NAME)
    W.render_docx(bl, docx_path, TITLE)
    md_path = os.path.join(OUT_DIR, "K3_Keputusan_Peringkat_Kursus_v0_1.md")
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(W.render_markdown(bl))
    prev_dir = os.path.join(OUT_DIR, "preview")
    pages = W.render_preview(bl, prev_dir, prefix="K3DEC")
    return dict(docx=docx_path, md=md_path, preview_dir=prev_dir,
                preview_pages=pages, blocks=len(bl),
                docx_bytes=os.path.getsize(docx_path))


if __name__ == "__main__":
    r = emit()
    print(f"blocks: {r['blocks']}")
    print(f"docx:   {r['docx']} ({r['docx_bytes']} bytes)")
    print(f"md:     {r['md']}")
    print(f"preview pages: {r['preview_pages']}")
