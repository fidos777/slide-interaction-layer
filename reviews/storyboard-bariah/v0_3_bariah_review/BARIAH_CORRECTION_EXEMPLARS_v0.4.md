# BARIAH CORRECTION EXEMPLARS — K5 PL06 T03 B02

**Purpose:** Extract the 12 corrected exemplar slides inserted by Bariah into the annotated storyboard and convert them into an implementation-ready change register for the next clean regeneration.

## Source artifacts

| Artifact | SHA-256 | Role |
|---|---|---|
| `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx` | `cdfc78e6395614ca79badda54ff5bbf2241c075e16ed26606fe6e69749e72809` | Primary slide-level evidence; 75 slides containing 63 original review pages + 12 corrected exemplars |
| `Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx` | `c15ae05e20358eda17b8e272f5dd9a5ef85831016976a926346371ea5790bcf3` | Decision and propagation context, especially the new Perabot Taman interaction structure |

## Extraction rule

The deck contains exactly 12 inserted corrected exemplar slides. Each original slide is marked `Bariah: Changes made. Refer next slide.` and is followed immediately by its corrected exemplar.

| Exemplar ID | Original slide | Corrected exemplar | Review page / screen |
|---|---:|---:|---|
| EX-01 | 1 | 2 | RP-001 / S01 |
| EX-02 | 3 | 4 | RP-002 / S02 |
| EX-03 | 5 | 6 | RP-003 / S03 |
| EX-04 | 7 | 8 | RP-004 / STRUKTUR_TAMAN_MASTER |
| EX-05 | 9 | 10 | RP-005 / STRUKTUR_PERSISIR_AIR_MAIN |
| EX-06 | 11 | 12 | RP-006 / STRUKTUR_PERSISIR_AIR_EXAMPLES base |
| EX-07 | 13 | 14 | RP-007 / Promenade popup state |
| EX-08 | 19 | 20 | RP-012 / Struktur Persisir Air all-viewed state |
| EX-09 | 42 | 43 | RP-034 / PERABOT_TAMAN_MASTER |
| EX-10 | 70 | 71 | RP-061 / RUMUSAN |
| EX-11 | 72 | 73 | RP-062 / KUIZ |
| EX-12 | 74 | 75 | RP-063 / TAMAT |

---

# EX-01 — S01 title/topic screen

**Pair:** slide 1 → slide 2  
**Scope:** local frame-screen change + global Notes grammar evidence

## Bariah’s corrected treatment

- Add the course-level title on the learner canvas:
  - `KURSUS KERJA BANGUNAN – PEMBINAAN LANDSKAP LUAR`
- Retain:
  - `PL06: Pengurusan Operasi Pembinaan Landskap`
  - `Topik 3 Bahagian 2: Komponen Landskap`
  - `MULA`
- Replace the opening VO with the shorter instruction:
  - `Klik butang MULA untuk memulakan pembelajaran.`
- Speaker Notes must begin with production-context headers:
  1. course title;
  2. PL title;
  3. topic/bahagian title;
  4. blank line;
  5. actual VO/transcript.

## Implementation rule

`S01_NOTES_TEMPLATE = COURSE_TITLE + PL_TITLE + TOPIC_BAHAGIAN_TITLE + VO`

## Do not carry forward

- The original narrated welcome sentence beginning `Selamat datang ke Pakej Latihan enam...`.

---

# EX-02 — S02 Pengenalan scenario

**Pair:** slide 3 → slide 4  
**Scope:** local dialogue rewrite + global Notes grammar evidence + unresolved source check

## Bariah’s corrected treatment

- Learner-facing heading becomes simply `Pengenalan`.
- Restore PL and Topic/Bahagian headers in Speaker Notes.
- Rewrite the dialogue so the Pelatih demonstrates baseline knowledge and seeks scope confirmation, rather than asking from zero knowledge.
- Use bracketed speaker labels in Notes:
  - `[Pelatih]`
  - `[Penyelia Tapak]`
- Insert character-name placeholder `[Nama]` rather than inventing a name.
- Add the statement that both groups must follow `MS2680`.

## Implementation rule

Use the corrected dialogue as the authoritative wording for S02, subject to the source-verification gate below.

## Open / blocking evidence item

`MS2680` is now a Bariah-directed claim but remains **PENDING SOURCE VERIFICATION** before it can be treated as a final factual statement applying to both Struktur Taman and Perabot Taman.

## Casting status

- Course-wide naming policy is confirmed in the review guide.
- Actual names remain open; do not invent them.

---

# EX-03 — S03 Hilmi overview and reflection

**Pair:** slide 5 → slide 6  
**Scope:** local frame-screen change + global Notes grammar + terminology treatment

## Bariah’s corrected treatment

- Learner-facing heading changes from `Gambaran Keseluruhan` to `Pengenalan`.
- Retain Hilmi, the two-group overview and the Mind Map direction.
- Refine the reflection question to:
  - `Jika anda ditugaskan memasang kerusi taman di tepi tasik, apakah jenis bahan yang anda akan pilih, dan mengapa?`
- Rewrite VO to connect explicitly with the previous page.
- Restore PL and Topic/Bahagian headers in Notes.
- `Hilmi:` remains on S03 only.

## Propagation rule

The Notes header pattern applies to all content/VO slides, but not to silent runtime completion states.

## Style rule

English-origin terms in learner-facing text and Notes must be italicised according to Bariah’s global instruction.

---

# EX-04 — Struktur Taman group master

**Pair:** slide 7 → slide 8  
**Scope:** Struktur Taman master template + shell-navigation rule

## Bariah’s corrected treatment

- Remove the custom learner-canvas `Seterusnya` button.
- The next control belongs to the player/shell navigation.
- Retain the four clickable structure cards and the instruction:
  - `Klik pada setiap struktur untuk penjelasan lanjut.`
- Restore PL and Topic/Bahagian headers in Notes.
- Notes include:
  - `Struktur Taman` context;
  - overview VO;
  - interaction instruction.

## Implementation rule

Do not remove completion gating. Move it from a custom canvas control to the shell control:

`player_next_enabled = group_complete[STRUKTUR_TAMAN]`

## Required metadata correction

The corrected exemplar still carries legacy off-canvas wording referring to `Seterusnya`. The clean regeneration must update metadata to state **shell navigation**, not a custom learner-canvas button.

---

# EX-05 — Struktur Persisir Air main explanation

**Pair:** slide 9 → slide 10  
**Scope:** global template for all Struktur Taman main explanation screens

## Bariah’s corrected treatment

- Remove the custom learner-canvas `Seterusnya` button.
- Separate the content into a clear explanation block and an `Aspek Pembinaan` block where source content exists.
- Preserve the full source-bound VO and the transition sentence to the example screen.
- Restore PL and Topic/Bahagian headers in Notes.
- Add group context in Notes: `Struktur Taman`.

## Propagation instruction

Bariah explicitly wrote:

`Apply changes to other struktur taman.`

Apply this template to:

- Struktur Teduhan;
- Kemudahan Awam;
- Water Feature;

while preserving source-specific differences. Do not invent an `Aspek Pembinaan` section where the module does not contain one.

## Required metadata correction

The clean version must not retain off-canvas wording that says `Satu butang Seterusnya` if the learner-canvas button has been removed. Reference the shell next control instead.

---

# EX-06 — Struktur example-selection screen

**Pair:** slide 11 → slide 12  
**Scope:** global template for all Struktur Taman example-selection screens

## Bariah’s corrected treatment

- Change learner instruction from:
  - `Klik pada setiap item...`
  to:
  - `Klik pada setiap contoh untuk penjelasan lanjut.`
- Restore PL and Topic/Bahagian headers in Notes.
- Notes must include:
  - group context `Struktur Taman`;
  - screen context `Contoh [Nama Komponen]`;
  - interaction instruction.
- Retain the example items, completion ticks and `Kembali` behaviour.

## Propagation instruction

Bariah explicitly wrote:

`Apply changes to other struktur taman.`

Apply to the example-selection screens for all four Struktur Taman components.

---

# EX-07 — Struktur popup state

**Pair:** slide 13 → slide 14  
**Scope:** global template for all Struktur Taman popup states

## Bariah’s corrected treatment

- Change the underlying instruction to `Klik pada setiap contoh...`.
- Use title-style field labels rather than all caps:
  - `Fungsi dan Penerangan`
  - `Contoh`
- Replace the text button `Tutup` with a close icon.
- Add a visual direction tied to the selected example, even where the source does not provide a dedicated figure.
- Restore PL and Topic/Bahagian headers in Notes.
- Notes must include group and example-screen context before the VO.

## Propagation instruction

Bariah explicitly wrote:

`Apply changes to other contoh struktur pop ups.`

Apply to every popup under:

- Struktur Persisir Air;
- Struktur Teduhan;
- Kemudahan Awam;
- Water Feature.

## Editorial cleanup

Use grammatically normal title case in the clean build:

`Fungsi dan Penerangan`

not the exemplar’s accidental double space / capitalisation form `Fungsi Dan  Penerangan`.

---

# EX-08 — Struktur all-viewed completion state

**Pair:** slide 19 → slide 20  
**Scope:** completion-state template where applicable

## Bariah’s corrected treatment

- Use `Klik pada setiap contoh...` consistently.
- Preserve completion ticks and enabled `Kembali` state.
- Keep Speaker Notes genuinely empty for silent completion states.

## Propagation instruction

Bariah wrote:

`Apply changes to others, where applicable.`

Apply the terminology and visual-state treatment to all equivalent all-viewed states, but do not add Notes headers to silent states.

---

# EX-09 — Perabot Taman master / gateway

**Pair:** slide 42 → slide 43  
**Scope:** major architecture change; use with the review guide, not as a standalone visual tweak

## Bariah’s corrected treatment

- Remove the custom learner-canvas `Seterusnya` button.
- Restore PL and Topic/Bahagian headers in Notes.
- Notes introduce the five perabot components and end with:
  - `Mari lihat setiap contoh perabot di halaman seterusnya.`
- Bariah marks this screen:
  - `New structure. Refer doc Panduan_Semakan_Bariah...`

## Governing Perabot architecture from the review guide

### Family P1 — Kerusi Taman, Tong Sampah, Drinking Fountain

`Component explanation + list of examples`  
→ click example at Level 1  
→ full-slide example with `Kembali`  
→ click specification at Level 2  
→ popup  
→ close with icon.

### Family P2 — Papan Tanda, BBQ Pit

`Component explanation + list of specification categories`  
→ click specification at Level 1  
→ popup directly  
→ close with icon.

Papan Tanda categories explicitly identified by Bariah:

- Bahan Panel;
- Bahan Struktur Tiang;
- Grafik;
- Rekaan.

BBQ Pit follows the same structural pattern as Papan Tanda, using source-attested specification groupings.

## Superseded assumption

Do not preserve a single global interaction pattern for all nine components. Struktur Taman and Perabot Taman now use different interaction families.

## Source integrity rule

The 26 source rows remain unchanged. Interaction decomposition may create more interaction items/states but must not rewrite source-row identity.

---

# EX-10 — Rumusan

**Pair:** slide 70 → slide 71  
**Scope:** local content approval + global Notes and italics rule

## Bariah’s corrected treatment

- Learner canvas content is retained.
- Wording is approved in the review guide.
- Restore PL and Topic/Bahagian headers in Notes.
- Add `Rumusan` as the Notes context heading.
- Remove the redundant VO opening label `Komponen Landskap — Struktur Taman dan Perabot Taman.` from the narrated paragraph.
- Apply italics to English terms globally in Speaker Notes and learner-facing content.

## Approved status

Rumusan wording is **LULUS**. Do not rewrite it unless a later source defect is found.

---

# EX-11 — Kuiz

**Pair:** slide 72 → slide 73  
**Scope:** major frame-screen and assessment-presentation update

## Bariah’s corrected treatment

Retain the existing assessment contract:

- 5 questions;
- 4 MCQ + 1 Multiple Response;
- pass mark 3/5 = 60%;
- `Semak Jawapan`;
- `Ulang Kuiz`;
- below 60% does not block progression.

Add / change:

1. State that the quiz is for comprehension only and is not part of the final examination grade.
2. Add learner instruction:
   - `Jawab semua soalan dengan pilihan jawapan yang betul.`
   - `Klik butang “MULA KUIZ” untuk mula.`
3. Add `MULA KUIZ` interaction before Question 1.
4. Immediate feedback per item:
   - correct SFX + VO/text: `Pilihan jawapan tepat.`
   - wrong SFX + VO/text: `Pilihan jawapan tidak tepat.`
5. After all questions:
   - show score;
   - show `Lulus` or `Tidak Lulus`;
   - show `Semak Jawapan` and `Ulang Kuiz`.
6. Multiple Response must not use `A, B, C...` labels; show option text directly.
7. Add subsection locators to the source references where available.
8. Restore PL and Topic/Bahagian headers in Notes.

## Required implementation interpretation

The longer explanatory rationale previously used as immediate feedback is no longer the approved immediate-feedback treatment. Preserve detailed rationale, if required, for `Semak Jawapan` rather than automatically presenting it as the immediate message.

---

# EX-12 — Tamat

**Pair:** slide 74 → slide 75  
**Scope:** end-screen visual hierarchy + unresolved LMS exit behaviour

## Bariah’s corrected treatment

- Change heading to:
  - `Tamat Topik 3 Bahagian 2: Komponen Landskap`
- Add course title and PL title hierarchy on the learner canvas.
- Restore PL and Topic/Bahagian headers in Notes.
- Use concise VO:
  - `Tamat Topik 3 Bahagian 2: Komponen Landskap. Teruskan pembelajaran ke bahagian seterusnya.`
- Disable shell `Seterusnya` on this screen.
- Learner closes the lesson/window in the LMS.

## Open decision requiring Firdaus confirmation

Separate the two concepts:

- **logical next destination:** next Bahagian in Topik 3;
- **physical exit behaviour:** close the lesson/window, then return through the LMS.

Confirm before production freeze:

- when completion is reported;
- where the LMS returns after window close;
- whether the next Bahagian is launched manually or automatically.

---

# Cross-exemplar rules extracted

## G-01 — Speaker Notes grammar

For content/VO slides:

1. course title when applicable;
2. PL title;
3. Topic/Bahagian title;
4. blank line;
5. screen/group context heading where applicable;
6. exact VO/transcript.

For silent runtime completion states:

- Notes remain genuinely empty.

## G-02 — English-term styling

Italicise approved English terms consistently across:

- learner canvas;
- popup headings/content;
- Speaker Notes;
- Rumusan;
- Kuiz;
- Tamat where applicable.

## G-03 — Navigation controls

- Remove duplicate custom `Seterusnya` buttons where the function belongs to shell/player navigation.
- Preserve gating semantics on the shell control.
- Popup close uses an icon, not a text `Tutup` button.
- `Kembali` target is interaction-family-specific, not one global hard-coded target.

## G-04 — Structure vs Perabot architecture

- Struktur Taman retains the reviewed Main → Contoh → popup pattern.
- Perabot Taman moves to two separate interaction families defined in EX-09.

## G-05 — Source evidence remains stable

Preserve:

- 26 meaningful source rows;
- 14 source assets;
- row IDs;
- source locators;
- image ownership findings.

Regenerate:

- interaction-item count;
- runtime-state count;
- review-page count;
- parent/child map;
- completion rules per family.

---

# Remaining unresolved items after exemplar extraction

| ID | Item | Status / owner |
|---|---|---|
| U-01 | Verify whether MS2680 applies to both Struktur Taman and Perabot Taman | Source QA / Firdaus before final factual adoption |
| U-02 | Provide actual character names for course-wide PL06 usage | Bariah / ID |
| U-03 | Confirm LMS completion and close-window behaviour on Tamat | Firdaus / LMS owner |
| U-04 | Define BBQ Pit specification group labels from source-attested substructure | ID implementation, then Bariah confirmation if wording is interpretive |
| U-05 | Confirm detailed quiz rationale placement under `Semak Jawapan` | ID / Bariah if not already established |

---

# Adoption verdict

```text
TWELVE_BARIAH_CORRECTION_EXEMPLARS_EXTRACTED
READY_FOR_SG_AND_SCREEN_STATE_MAP_UPDATE
NOT_READY_FOR_CLEAN_V0_4_GENERATION_UNTIL:
- Perabot interaction families are modelled;
- shell navigation semantics are updated;
- MS2680 is verified or explicitly held;
- open Tamat behaviour is recorded.
```

## Preservation instruction

Treat `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx` as immutable review evidence. Do not edit it into the clean build. Generate the next clean version from controlled content, the updated decision register and the regenerated screen/state model.
