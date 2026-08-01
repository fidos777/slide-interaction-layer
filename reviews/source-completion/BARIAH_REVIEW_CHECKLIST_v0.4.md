# BARIAH_REVIEW_CHECKLIST — K5 PL06 T03 B02 v0.4

```
REVIEW_READY · BARIAH_FEEDBACK_IMPLEMENTED · PENDING_TARGETED_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx` — 100 review pages.

> **Please do not re-audit source coverage.** All 26 source rows and 14 source assets are
> mechanically verified against the module, and 105 structural checks pass. Seven
> specific things need your eye, and they are in Part B.

---

# Part A — your feedback, implemented

Nothing here needs re-checking unless it looks wrong on screen.

| Your ruling | How it is built |
|---|---|
| **Perabot Taman — new structure** | The Perabot gateway is now overview + list with **no click and no interaction level**. Learners enter each component through shell navigation. |
| **Kerusi Taman, Tong Sampah, Drinking Fountain** | Family P1: component explanation + example list → click example (Level 1, **full slide**) → click specification (Level 2, popup) → close icon returns to the same example → Kembali returns to the component list. |
| **Papan Tanda, BBQ Pit** | Family P2: explanation + specification-category list → click category (Level 1, popup) → close icon returns to the list. **No one-item Contoh screen exists** for either. Papan Tanda: Bahan Panel, Bahan Struktur/Tiang, Grafik, Rekaan. BBQ Pit: Bahan Pembinaan, Dimensi, Gril, Keselamatan — all four taken from the module's own specification lines. |
| **Struktur Taman — Lulus** | Family S flow retained exactly as built. |
| **"Tidak perlu letak butang Seterusnya"** | No custom Seterusnya is drawn anywhere. Progression is the LMS shell control, still gated by completion. |
| **"Butang tutup guna ikon"** | Every popup closes with an icon. No text button labelled Tutup exists in the deck. |
| **Speaker Notes headers** | Content and dialogue slides carry a **NON-SPOKEN CONTEXT** block (PL and Topic) separated from a **SPOKEN TRANSCRIPT** block, so nothing ambiguous reaches TTS. Silent completion states have genuinely empty Notes. |
| **"Dibaca di slide 1"** | S01 speaks the PL06 title, the Topik 3 Bahagian 2 title, a one-line orientation and the Mula instruction — and only S01 does. From S02 on, those titles are non-spoken context. |
| **English words in italic, global** | `Water Feature`, `Drinking Fountain`, `BBQ Pit`, `Wood-Plastic Composite` are italicised on canvas, in Notes and in popups. |
| **N-06** | `WPC (Wood-Plastic Composite / Plastik Kitar Semula)`. |
| **Rumusan — Lulus** | Wording unchanged. `Kepentingan`, `Isi Utama`, `Apa Yang Dipelajari` and `Manfaat` are not displayed. |
| **Cast for the whole PL06** | Alya (Kontraktor Junior) and Encik Rahman (Mentor / Kontraktor Senior Berpengalaman Landskap) on S02. Hilmi narrates on S03 and is **not** reintroduced — the Course Montage already introduced him. `Pelatih` / `Penyelia Tapak` appear nowhere as learner-facing names. |
| **Quiz** | 5 items, 4 MCQ + 1 Multiple Response, MULA KUIZ, pass 3/5 = 60%, non-blocking. Multiple Response shows option text with **no A/B/C labels**. Immediate feedback is exactly *"Pilihan jawapan tepat."* / *"Pilihan jawapan tidak tepat."* with SFX and VO. |
| **Next Bahagian in Topik 3** | Kept as production metadata. It is **not** shown on the learner canvas, because the physical exit is still unconfirmed. |
| **Montage context** | B02 opens at section level. The course introduction, the eight PLs, the PL06 objectives and the seven-topic list are not repeated. |

---

# Part B — targeted confirmation requested

Seven items. Each is a judgment only you can make.

### 1. Family P1 density
Specification cards are deliberately shorter than example cards so the example detail reads as the
primary content. **Where an example has only two specifications** (Kerusi Konkrit, all three Tong
Sampah examples) the two cards span the full width. Does the hierarchy still read correctly?

### 2. Family P2 category treatment
Papan Tanda and BBQ Pit each show four cards drawn from **one** source row. Do the labels read as
facets of a single specification rather than as four separate products?

### 3. Close-icon clarity
Filled cross on a solid disc, top-right of every popup. Is it obvious enough, and is the hit area
adequate for a touch device?

### 4. Alya and Encik Rahman — visual treatment
S02 currently specifies the two characters as name plus role. How should they appear on screen?

### 5. S01 and S03 wording
S01 speaks two titles, then *"Dalam bahagian ini, anda akan mempelajari tentang komponen landskap.
Klik Mula untuk meneruskan."* Does that read naturally after the PL06 montage? And is the S03
reflection question still the wording you want?

### 6. Quiz presentation
Both feedback variants are shown side by side on each question page so you can see them. Is that the
right storyboard convention, or should they be separate states?

### 7. Tamat instruction
*"Tutup tetingkap pelajaran untuk keluar."* with no visible next control. Clear enough for a learner?

---

# Part C — still waiting on someone else

| Item | Waiting on | Effect on this deck |
|---|---|---|
| **MS2680** — does it apply to both Struktur Taman and Perabot Taman? | source verification / Firdaus | the sentence is **omitted** from S02 dialogue and held in production metadata. No substitute claim was invented |
| **Physical LMS exit** on Tamat | **Firdaus** | shell Next is disabled; the learner is told to close the window |
| **Detailed quiz rationale** — where does it live? | **Bariah** | rationale is production metadata only, not learner-facing |
| **Pengurus Projek** character name | Bariah / ID | not used in B02 |
| Module DOCX integrity (`B02-CAIR-INT-001`) | Firdaus / CAIR | does not affect this review build |

---

# Part D — what this build is not

It is a **review build**. It is not production-approved, not canonically frozen, not MMD-build ready,
and it does not assert complete module-DOCX integrity. No multimedia or final imagery is bound —
every visual is a written direction with its module page reference.
