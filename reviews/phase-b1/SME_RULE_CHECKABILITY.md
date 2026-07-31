# SME_RULE_CHECKABILITY

Phase B1 — assessment (not implementation) of deterministic checkers for Bariah's provisional rules,
plus source normalisation and toolchain metadata.

Source artifact: `3f626ac5-BARIAH_REVIEW_8SLIDES.pptx`, SHA-256 `ee4f5479…8bb9e7`.
**No checker was built. No gate was implemented. No rule was promoted to canonical.**

### Standing evidence limitation

`packet_B02.json`, the 19-slide K5 B02 Tier-1 specification, `asset_manifest.json`, the source nodes,
and `SB_K4PL3T2_v1.2.pptx` are **absent from this session** (see `BARIAH_REVIEW_INGEST.md §1.1`).
Every requirement below that names *the 19 packet screens* or *bound source nodes* is therefore
`NOT_DETERMINABLE` on evidence, and is marked as such at the point it arises. The reviewed deck is
measured in full.

The deck supplies one asset the packet cannot: an **untouched base / Bariah-revised pair** —
`slide7.xml` (`sldId 9016`, no change records) and `slide8.xml` (`sldId 9017`, `add`, duplicate of
`slide7`). This pair is the controlled before/after for four of the five rules.

---

## 1. Rule R1 — narrator prefix

> `Tidak perlu letak Hilmi di VO. Understood that it’s Hilmi. (Only put Hilmi in Slide 3 Narrator)`
> — `slide8.xml` shape `id=3` `TextBox 2`, off-canvas, `spChg add mod @23:12:17.323` — `SME_AUTHORED_RULE`

### 1.1 Exact occurrences in the reviewed deck — `MEASURED_FACT`

Token `Hilmi` (word-boundary, case-insensitive): **5 total**.

| Locus | Bound slide | Count | Form | Kind |
|---|---|---:|---|---|
| `notesSlide1.xml` | `slide1` (9003, **untouched base**) | 1 | `Hilmi: Struktur taman membina fungsi…` | **narrator VO** |
| `notesSlide6.xml` | `slide7` (9016, **untouched base**) | 1 | `Hilmi: Komponen Landskap — Struktur Taman…` | **narrator VO** |
| `slide8.xml` `id=3` | — | 3 | inside the rule text itself | **annotation, not content** |

Token `Hilmi:` (with colon): **2** — both narrator VO, both in **untouched base** notes, both at the
start of the VO body paragraph immediately after the two-line `PL06 …` / `Topik 3 Bahagian 2 …` header.

**Zero** occurrences in `notesSlide2` (→ `slide3`), `notesSlide3` (→ `slide4`), `notesSlide4`
(→ `slide5`, empty), `notesSlide5` (→ `slide6`), **`notesSlide7` (→ `slide8`)**.

### 1.2 The rule was applied, and the control pair proves it — `MEASURED_FACT`

`notesSlide6` (base, bound to untouched `slide7`) opens `Hilmi: Komponen Landskap — …`
`notesSlide7` (Bariah, bound to `slide8`) opens `Komponen Landskap - Struktur Taman Dan Perabot Taman`

Same content, prefix removed. `slide8`'s `sldChg` carries `modNotesTx`. Bariah wrote the rule **and**
executed it on the one screen she revised.

### 1.3 Occurrences in the 19-screen packet — `NOT_DETERMINABLE`

`packet_B02.json` is absent. No count can be produced.

### 1.4 Narrator vs scenario dialogue — is each occurrence classifiable?

In this deck, **yes, for all 5** (§1.1). But that result is unearned: **the reviewed deck contains no
scenario dialogue at all.** Every VO body is continuous third-person exposition. There is no character
turn, no speaker exchange, no quoted utterance anywhere in the seven notes slides.

### 1.5 Can a deterministic checker distinguish narrator from dialogue? — `NOT_DETERMINABLE`

A checker anchored at paragraph start —

```
^\s*Hilmi\s*:          applied to notesSlide body paragraphs only
```

— achieves 5/5 on the reviewed deck. That number is meaningless for the rule as written, because the
discriminating case is **unrepresented in the evidence**. The rule presupposes a corpus where `Hilmi`
can appear as a scenario speaker; this deck contains no such instance, so the checker has never been
exercised against the case it exists to resolve.

Two further blockers, both independent of corpus size:

1. **`Slide 3 Narrator` is unresolvable.** The reviewed deck's slide 3 is the Card base state, and its
   notes (`notesSlide2`) contain **no** `Hilmi:`. The referent must be screen 3 of the 19-screen
   packet, not this deck. Without the packet the exemption's scope cannot be located, so a checker
   cannot know which occurrence is licensed. `NOT_DETERMINABLE`
2. **Narrator/dialogue is a role distinction, not a string distinction.** `Hilmi:` at paragraph start
   is the same token in both cases. Discriminating them requires a speaker-role field the storyboard
   format does not carry.

**Assessment:** checkable as a **flagging** rule (surface every `^Hilmi\s*:` in a notes body for human
adjudication) — high recall, no false negatives on this evidence. **Not** checkable as a **gating**
rule until (a) the packet supplies the `Slide 3 Narrator` referent and (b) at least one scenario-dialogue
instance exists to calibrate against. `PROVISIONAL_IDENTIFIER`

---

## 2. Rule R2 — English terms in italics

> `English Words in italic (cth: Water Feature)` — `slide8.xml id=3 p1`; the example token carries
> `rPr i="1"`, so the rule exemplifies itself — `SME_AUTHORED_RULE`

### 2.1 Lexicon seed — learner-visible English-origin terms — `MEASURED_FACT`

Seed only. **Not a cross-course registry.** Source-node forms are `NOT_DETERMINABLE` (source absent);
the untouched base `slide7`/`notesSlide6` stands as the best available pre-review proxy and is labelled
as such.

| # | Displayed form | Locus | Base-proxy form (`slide7`/`notesSlide6`) | Italic? | Uncertainty |
|---:|---|---|---|---|---|
| 1 | `Water Feature` | `slide1 id=24` (label) | — | **no** | low — unambiguous English compound |
| 2 | `Water Feature` | `slide3 id=24` (label) | — | **no** | low |
| 3 | `Water Feature` | `slide5 id=14` (label) | — | **no** | low |
| 4 | `Water Feature` | `slide7 id=25 p2` | `Water Feature` | **no** | low |
| 5 | `Water Feature` | `slide8 id=25 p2` | `Water Feature` | **YES** `i="1"` | low |
| 6 | `Drinking Fountain` | `slide7 id=25 p2` | `Drinking Fountain` | **no** | low |
| 7 | `Drinking Fountain` | `slide8 id=25 p3` | `Drinking Fountain` | **YES** `i="1"` | low |
| 8 | `BBQ pit` | `slide7 id=25 p2` | `BBQ pit` | **no** | medium — acronym + common noun; see §7 |
| 9 | `BBQ Pit` | `slide8 id=25 p3` | `BBQ pit` | **YES** `i="1"` | medium — form changed, see §7 |
| 10 | `Water Feature` | `slide8 id=3 p1` (annotation) | — | **YES** `i="1"` | n/a — rule example, off-canvas |

**Learner-visible distinct terms: 3** — `Water Feature`, `Drinking Fountain`, `BBQ pit`/`BBQ Pit`.

### 2.2 Application rate — `MEASURED_FACT`

Italic is applied at **exactly one locus**: `slide8` (`sldId 9017`), Bariah's revised Rumusan.
Rows 1–4, 6, 8 — six learner-visible occurrences on `slide1`, `slide3`, `slide5`, `slide7` — carry
**no** italic. Application rate across the reviewed deck: **3 of 9 = 33 %.**

This is expected and is not a defect: `slide1` and `slide7` are untouched base slides Bariah never
edited, and `slide3`/`slide5` are Card states she built before writing R2 at 23:12:17. The rule was
authored near the end of the session and applied only to the screen revised after it.

### 2.3 Excluded from the lexicon — `MEASURED_FACT`

| Category | Tokens | Why excluded |
|---|---|---|
| Production/meta English | `Click & Reveal`, `Hotspot`, `Card`, `Note to MMD`, `Full-slide reveal`, `learner` | authoring vocabulary, off-canvas or in `slide2` rationale; never learner display |
| Placeholder | `[button label]` ×4 (`slide6`) | literal placeholder text |
| Annotation English | `Understood that it’s Hilmi`, `Only put Hilmi in Slide 3 Narrator`, `English Words in italic`, `relate to application in industry`, `I think it’s best/logical to use` | Bariah's review prose, off-canvas |
| Established Malay loans | `informasi`, `landskap`, `struktur`, `komponen`, `navigasi`, `maklumat`, `strategik`, `elemen`, `kategori`, `grid`, `senarai` | naturalised in Malay orthography; italicising these would be wrong |

**The loan-word boundary is the checker's hard problem**, and it is a lexicon problem, not a parsing
one. `informasi` and `Water Feature` are both English-derived; only the second is in scope. No
algorithm distinguishes them — only a maintained term list can.

### 2.4 Assessment

**Mechanically checkable, given a term list.** For each entry, locate it in display runs and assert
`rPr/@i="1"` on the covering run(s). Both halves are cheap: `a:t` text and `a:r/a:rPr/@i` are adjacent
in the XML.

Two implementation facts from this evidence:

1. **Run fragmentation is not an obstacle here.** All three italicised terms are stored as **single
   intact runs** (`<a:r><a:rPr i="1" lang="en-MY"/><a:t>Water Feature</a:t></a:r>`), so the italic
   span aligns exactly with the term. But `slide8 p1` shows the same sentence split across 17 runs at
   word granularity — a term-boundary matcher must join runs before matching, then map back.
2. **`lang="en-MY"` is not a usable signal.** It is set on virtually every run in `slide8`, including
   pure Malay ones, and absent on `slide1`'s runs entirely.

Classification: **checkable — `PROVISIONAL_IDENTIFIER`.** The checker is sound; the term list is the
open artifact. This lexicon is a **seed of 3 terms from one 8-slide deck** and must not be treated as
a cross-course registry.

---

## 3. Rule R3 — Rumusan visible labels

> `Tidak perlu letak perkataan Kepentingan, Isi Utama, Manfaat` — `slide8.xml id=3 p2` — `SME_AUTHORED_RULE`

### 3.1 Presence check — `MEASURED_FACT`

| Label | `slide7` (base, untouched) | `slide8` (Bariah) | `notesSlide6` (base VO) | `notesSlide7` (Bariah VO) |
|---|---|---|---|---|
| `Kepentingan` | **present** — `id=25 p1`: `Kepentingan: mengenal pasti…` | **absent** | present | **absent** |
| `Isi Utama` | **present** — `id=25 p2`: `Isi utama: struktur taman…` (lowercase `u`) | **absent** | present | **absent** |
| `Manfaat` | **present** — `id=25 p3`: `Manfaat kefahaman: anda boleh…` | **absent** | present | **absent** |
| `Manfaat kefahaman` | **present** — `id=25 p3` | **absent** | present | **absent** |

**All four labels present in the base; all four removed in Bariah's revision, in display and in VO.**
The rule was authored and fully executed. `MEASURED_FACT`

### 3.2 Can it be checked deterministically? — **Yes.** `MEASURED_FACT`

This is the most checkable rule in the set. All four targets are fixed literals occupying the
paragraph-initial position followed by a colon:

```
^\s*(Kepentingan|Isi\s+Utama|Manfaat(\s+kefahaman)?)\s*:     case-insensitive
applied to: display body of any slide whose title bar text == "Rumusan"
```

Three calibrations the evidence forces:

1. **Case-insensitive is mandatory.** The rule says `Isi Utama`; the source says `Isi utama`. A
   case-sensitive matcher misses the real occurrence — the exact failure mode the checker exists to
   catch.
2. **`Manfaat` must match as a prefix.** The rule names `Manfaat`; the source carries
   `Manfaat kefahaman:`. Matching the bare word only would miss it.
3. **Scope must be Rumusan-only.** `Kepentingan` is a legitimate Malay noun elsewhere. Restrict to
   Rumusan screens, identified by title-bar text — both `slide7` and `slide8` carry `Rumusan` in
   `TextBox 6`.

Zero false positives and zero false negatives on the reviewed deck: 4/4 present in `slide7`, 0/4 in
`slide8`. **Assessment: fully deterministic, gate-grade.** `PROVISIONAL_IDENTIFIER` only as to whether
the four-item list is complete for other modules.

---

## 4. Rule R4 — `anda` versus `kontraktor`

> `Di Rumusan, Jangan guna anda, guna kontraktor` — `slide8.xml id=3 p3` — `SME_AUTHORED_RULE`

### 4.1 Complete enumeration across the reviewed deck — `MEASURED_FACT`

Word-boundary, case-insensitive, across all 8 slides and all 7 notes slides.

**`anda` — 3 occurrences:**

| # | Locus | Channel | Verbatim | Screen type |
|---:|---|---|---|---|
| 1 | `slide7 id=25 p3` | **display** | `Manfaat kefahaman: anda boleh mengenal pasti dan menerangkan setiap komponen landskap serta fungsinya di tapak.` | Rumusan (base) |
| 2 | `notesSlide6` | **VO** | `…Manfaat kefahaman: anda boleh mengenal pasti…` | Rumusan (base) |
| 3 | `slide8 id=3 p3` | **annotation** (off-canvas) | `Di Rumusan, Jangan guna anda, guna kontraktor` | rule text, not content |

**`kontraktor` — 3 occurrences:**

| # | Locus | Channel | Verbatim | Screen type |
|---:|---|---|---|---|
| 1 | `slide8 id=25 p4` | **display** | `Kontraktor dapat merancang, melaksana dan menyelenggara setiap komponen landskap mengikut fungsinya di tapak` | Rumusan (Bariah) |
| 2 | `notesSlide7` | **VO** | `…kontraktor dapat merancang, melaksana dan menyelenggara…` | Rumusan (Bariah) |
| 3 | `slide8 id=3 p3` | **annotation** (off-canvas) | `…guna kontraktor` | rule text, not content |

**Learner-visible totals: `anda` = 1 (base Rumusan display), `kontraktor` = 1 (revised Rumusan display).**
Zero occurrences of either token in dialogue — the deck contains no dialogue (§1.4).
Zero occurrences of either token outside Rumusan, anywhere in the deck.

### 4.2 The substitution is a clean controlled pair — `MEASURED_FACT`

```
slide7  (base)     display : Manfaat kefahaman: anda boleh mengenal pasti dan menerangkan …
slide8  (Bariah)   display : Kontraktor dapat merancang, melaksana dan menyelenggara …
```

Bariah changed **both** channels — display and VO — in the same revision. This is not a display-only
edit.

### 4.3 Counts across the 19 packet screens — `NOT_DETERMINABLE`

`packet_B02.json` is absent.

### 4.4 Scope reconciliation — the rule cannot be tested outside Rumusan — `NOT_DETERMINABLE`

The rule is explicitly scoped `Di Rumusan`. In the reviewed deck, **every** occurrence of `anda` is
already inside Rumusan, so the deck cannot demonstrate whether `anda` is acceptable elsewhere — the
negative case has no instances.

Per the task's instruction, **the rule is not assumed to apply outside Rumusan.** A checker built on
this evidence must scope to Rumusan screens and must not flag `anda` on subtopic or reveal-child
screens until the packet establishes the broader scope.

**Assessment:** the string test is trivially deterministic — `\banda\b` within a Rumusan display or VO
body is a hard fail. The scope boundary is the open question, not the match. `PROVISIONAL_IDENTIFIER` /
`OPEN_DECISION` on scope.

---

## 5. Rule R5 — industry application

> `Manfaat – relate to application in industry` — `slide8.xml id=3 p4` — `SME_AUTHORED_RULE`

## Classification: `JUDGMENT_RULE_NOT_DETERMINISTIC`

### 5.1 What the controlled pair actually shows — `MEASURED_FACT`

```
slide7 p3 (base)    : Manfaat kefahaman: anda boleh mengenal pasti dan menerangkan
                      setiap komponen landskap serta fungsinya di tapak.
slide8 p4 (Bariah)  : Kontraktor dapat merancang, melaksana dan menyelenggara
                      setiap komponen landskap mengikut fungsinya di tapak
```

Three simultaneous shifts:

| Dimension | Base | Revised |
|---|---|---|
| Actor | `anda` (2nd person addressee) | `Kontraktor` (occupational role) |
| Verb class | `mengenal pasti`, `menerangkan` — **cognition** | `merancang`, `melaksana`, `menyelenggara` — **operational** |
| Site locative | `di tapak` | `di tapak` — **unchanged** |

### 5.2 Why a lexical checker fails — `MEASURED_FACT`

The most obvious proxy — search for an industry/site locative — **does not discriminate**:
`di tapak` is present in **both** the compliant and the non-compliant text. A checker keyed on
`tapak`, `industri`, or `lokasi` passes the base sentence that Bariah rewrote precisely because it did
not satisfy her rule. **Any purely lexical site-reference test is a false pass on this evidence.**

What actually changed is the **actor** and the **verb class**. Both are semantic categories, and the
verb shift in particular is open-ended — `melaksana` and `menyelenggara` are two members of an
unbounded set of operational verbs.

### 5.3 A bounded rubric is suggested but not supported — `OPEN_DECISION`

The pair suggests a three-part conjunctive rubric:

```
(a) an occupational actor noun heads the benefit clause   (kontraktor, penyelia, juruteknik, …)
(b) at least one operational verb is present              (merancang, melaksana, menyelenggara, …)
(c) a site or industry locative is present                (di tapak, di lapangan, industri, …)
```

Applied to the pair: base satisfies (c) only → fail; revised satisfies (a)(b)(c) → pass. It
discriminates.

**But it must not be adopted, for three reasons:**

1. **n = 1.** One before/after pair cannot fix the closed membership of the actor list or the verb list.
   A list induced from a single example will over-fit to `kontraktor` / `merancang` / `melaksana` /
   `menyelenggara`.
2. **Condition (c) is inert.** It is satisfied by both members of the only pair available, so the pair
   supplies no evidence about its discriminating power.
3. **`relate to` is not a surface relation.** Bariah's wording asks for a *connection* between learning
   and industry practice. A sentence can name a contractor and three operational verbs and still fail
   to connect the learning objective to site application; and one can make the connection without any
   listed verb.

**Assessment: `JUDGMENT_RULE_NOT_DETERMINISTIC`.** The rubric above is recorded as a **candidate for
corpus validation**, not as a checker. Promoting it would require the 19-screen packet plus other
modules' Rumusan screens to establish list membership and measure false-pass rate. Until then this
rule is a human review item. It may reasonably be implemented as an **advisory prompt** — "does this
benefit clause name a role and an operational action?" — never as a gate.

---

## 6. Card versus Hotspot

Governing definition, `SME_AUTHORED_RULE` — `slide2.xml id=6` (`sldId 9020`, `new`):

> `Click & Reveal (Hotspot) digunakan untuk item, kategori atau komponen yang dipaparkan pada satu imej atau gambar rajah.`
> `Click & Reveal (Card) digunakan untuk item, kategori atau komponen yang disusun sebagai senarai atau grid berasingan.`
> `Apabila diklik, kedua-duanya memaparkan maklumat secara paparan penuh, atau pop up dengan butang tutup, bergantung kepada tahap penjelasan yang diperlukan.`

### 6.1 Per-screen report for the 19 B02 screens — `NOT_DETERMINABLE`

`packet_B02.json` and the 19-slide Tier-1 specification are absent. Bound child counts, source-image
bindings, and region data for the 19 screens cannot be obtained.

### 6.2 Per-screen report for the reviewed deck — `MEASURED_FACT` / `PROVISIONAL_IDENTIFIER`

| Screen | `sldId` | Bound children | One covering source image? | Children visually discrete? | Source coordinates / regions? | Provisional |
|---|---:|---:|---|---|---|---|
| `slide1` | 9003 | **4** (labels id 21–24) | **Yes** — `Rectangle 9` (0.8046, 1.7813) 5.8621 × 5.2604, `Visual: struktur taman — rujuk modul ms 237 (imej K5PL06T03-B02-IMG-01)` | Yes — 4 stacked boxes at x 8.5938, pitch 0.7846 | **No** | **`INDETERMINATE`** |
| `slide2` | 9020 | 0 | n/a | n/a | n/a | n/a — rationale text |
| `slide3` | 9019 | **4** (cards id 19, 3, 4, 5) | **No** — 4 separate 3.935 × 1.9901 visual rects, one per component | Yes — 2 × 2 grid, gaps 0.7074 / 0.3701 | **No** | **`CARD`** |
| `slide4` | 9011 | 0 | n/a — reveal **child** | n/a | n/a | n/a |
| `slide5` | 9008 | **4** (cards + 4 ticks) | **No** — same 4 discrete rects | Yes — as `slide3`, plus completion ticks | **No** | **`CARD`** (completion state of `slide3`) |
| `slide6` | 9021 | **4** (`[button label]` id 21, 7, 8, 10) | **Yes** — `Rectangle 9` (0.7917, 1.9438) 11.75 × 5.0979, `Visual: XXX` | **No** — 4 markers **inside** the panel at scattered positions | **No** — positions are placeholders | **`HOTSPOT`** |
| `slide7` | 9016 | 0 | n/a — Rumusan | n/a | n/a | n/a |
| `slide8` | 9017 | 0 | n/a — Rumusan | n/a | n/a | n/a |

### 6.3 Why `slide1` is `INDETERMINATE` — `MEASURED_FACT`

`slide1` is the untouched probe base, and its evidence **contradicts itself**:

- Its off-canvas note (inherited, `INHERITED_PROBE_CONTENT`) says `4 hotspot. Nombor selebihnya dibuang.`
  and `Klik hotspot -> reveal full-slide, bukan pop up.` — declaring Hotspot.
- Its geometry says otherwise. The visual panel spans x **0.8046 → 6.6667**. All four labels sit at
  x **8.5938**, i.e. **1.9271 in clear of the image's right edge**. The children are **not on the
  image** — they are a vertically stacked list beside it.

Against R6, `slide1` fails the Hotspot test (children are not `dipaparkan pada satu imej`) and fails
the Card test (there is no `grid berasingan`; there is one shared image plus a list). It is a third
form the definition does not cover: **list-beside-image**.

**This is exactly the ambiguity Bariah's review resolves.** Her `slide3` note reads
`(PENAMBAHBAIKAN, I think it’s best/logical to use Click & Reveal (Card))`, and `slide3` rebuilds the
screen as four discrete visuals — converting the ambiguous list-beside-image into an unambiguous Card
grid. `slide6` (`IF HOTSPOT - CONTOH`) is the counter-example showing what a real Hotspot would look
like: markers *inside* the covering image. `MEASURED_FACT`

### 6.4 The blocking finding — no source-side region data anywhere — `MEASURED_FACT`

**The package contains no coordinate or region data for any screen.** No hotspot geometry, no image
maps, no region identifiers, no `p:custDataLst` at slide or shape level (grep for `custDataLst` across
`ppt/` returns `presentation.xml` **only**). The single media part is
`ppt/media/image1.svg` — a 228-byte checkmark icon, not a content image. Every `Visual:` panel is a
**text placeholder describing an image that is not in the package**.

`slide6`'s four `[button label]` positions — (7.4283, 2.1965), (5.1106, 3.2474), (6.6267, 4.8672),
(2.4439, 5.9562) — carry the literal text `[button label]` and are scattered without relation to any
image content. They are layout placeholders, not derived hotspot regions.

**Consequence:** a Card/Hotspot selection **gate** cannot be built from the current evidence at all.
Hotspot selection requires source-side region identification, and the source supplies none. The
provisional identifiers in §6.2 are inferred from *slide geometry* — which is downstream authoring
output, not source authority.

**Assessment: `PROVISIONAL_IDENTIFIER` throughout. No gate implemented. No identifier treated as
canonical.** The reconciliation input Stage 0A requires is `asset_manifest.json` plus the source nodes,
to establish per-screen whether a single covering image with identifiable regions exists.

---

## 7. Source normalisation

**Standing limitation:** bound source nodes are absent. The comparison below uses the untouched base
`slide7.xml` (`sldId 9016`) and its VO `notesSlide6.xml` as the **pre-review proxy** for source form.
Every classification is therefore provisional against that proxy, not against source. Where the task
statement supplies the source form directly (`BBQ pit`), that is used and marked.

### 7.1 Complete difference table, `slide7` → `slide8` — `MEASURED_FACT`

| # | Base form (`slide7`) | Reviewed display (`slide8`) | Difference type | Classification |
|---:|---|---|---|---|
| 1 | `BBQ pit` **(source form per task statement)** | `BBQ Pit` | capitalisation | **display normalisation** — deviates from source |
| 2 | `Komponen Landskap — Struktur…` (em dash U+2014) | `Komponen Landskap - Struktur…` (hyphen-minus U+002D) | punctuation | **unresolved source variant** |
| 3 | `…Struktur Taman dan Perabot Taman` | `…Struktur Taman Dan Perabot Taman` | capitalisation | **probable typo correction — in reverse** (see §7.2) |
| 4 | `perabot taman merangkumi …` | `Elemen Perabot Taman - …` | capitalisation + word addition | **display normalisation** |
| 5 | `struktur taman merangkumi …` | `Struktur Taman - …` | capitalisation + verb→punctuation | **display normalisation** |
| 6 | `anda boleh …` | `Kontraktor dapat …` | lexical substitution | **SME rule R4** — not normalisation |
| 7 | `Kepentingan:` / `Isi utama:` / `Manfaat kefahaman:` | *(removed)* | label deletion | **SME rule R3** — not normalisation |
| 8 | all bullets end `.` | **no** bullet ends with punctuation | punctuation | **display normalisation** |
| 9 | `Drinking Fountain, BBQ pit.` | `Drinking Fountain dan BBQ Pit` | punctuation → conjunction | **display normalisation** |
| 10 | `Water Feature` / `Drinking Fountain` / `BBQ pit` plain | same terms with `rPr i="1"` | formatting | **SME rule R2** — not normalisation |
| 11 | `mengenal pasti komponen landskap` | `Mengenal pasti struktur dan elemen landskap` | lexical | **unresolved source variant** |

Sentence-terminal punctuation (row 8) is removed from **all four** bullets, consistently. That is a
deliberate house style, not drift. `MEASURED_FACT`

### 7.2 The `Dan` case — a normalisation that introduces an error — `MEASURED_FACT`

Row 3: the base reads `Struktur Taman dan Perabot Taman`; the revision reads
`Struktur Taman Dan Perabot Taman`. Malay title case does not capitalise the coordinating conjunction
`dan`. This is **over-application of title case** — the normalisation pass capitalised a word that
should have stayed lowercase.

It is listed as *probable typo correction — in reverse* because the mechanism is a correction pass, but
the outcome on this token is a regression. It must not be approved silently.

### 7.3 The `BBQ pit` → `BBQ Pit` case — `OPEN_DECISION`

Taking the task statement's source form `BBQ pit` as given:

- source: `BBQ pit`
- base display (`slide7`): `BBQ pit` — **exact source reproduction**
- base VO (`notesSlide6`): `BBQ pit` — **exact source reproduction**
- revised display (`slide8`): `BBQ Pit` — **display normalisation**, deviates from source
- revised VO (`notesSlide7`): `BBQ Pit` — deviates in the VO channel too

Bariah changed **both** channels. This is not a display-only presentation choice; the source-bound VO
now carries a form the source does not. The other four furniture items — `Kerusi Taman`, `Papan Tanda`,
`Tong Sampah`, `Drinking Fountain` — are title-cased in both base and revision, so `BBQ pit` was the
odd one out and the change makes the list internally consistent. That is a defensible reason, and it is
still a source deviation.

**Not silently approved.** Enters Stage 0A as an explicit decision: does display/VO normalisation to
list-internal consistency override exact source reproduction for proper-noun furniture labels? The
same decision governs rows 4, 5, and 9.

### 7.4 Assessment

Capitalisation, spacing, punctuation, and singular/plural differences are **fully deterministic** to
detect — a normalised string comparison between a display label and its bound source node, reporting
the diff class, needs no semantics. What is **not** automatable is the *approval*: rows 1, 4, 5, 8, 9
are all defensible display normalisations and all deviate from source. `PROVISIONAL_IDENTIFIER` on
detection; `OPEN_DECISION` on the approval policy.

---

## 8. Toolchain and iSpring metadata

### 8.1 Non-standard package parts — `MEASURED_FACT`

| Part | Relationship type | Rel ID | From |
|---|---|---|---|
| `ppt/tags/tag1.xml` | `…/officeDocument/2006/relationships/tags` | `rId11` | `presentation.xml` |
| `ppt/changesInfos/changesInfo1.xml` | `…/office/2016/11/relationships/changesInfo` | `rId16` | `presentation.xml` |
| `ppt/revisionInfo.xml` | `…/office/2015/10/relationships/revisionInfo` | `rId17` | `presentation.xml` |

`ppt/tags/tag1.xml` is bound by `<p:custDataLst><p:tags r:id="rId11"/></p:custDataLst>` inside
`p:presentation`. **A repository-wide grep for `custDataLst` across `ppt/` matches `presentation.xml`
and nothing else** — no slide, shape, or picture carries a tag list.

**Therefore all 23 tags are presentation-level. There are no slide-level and no object-level iSpring
tags in this package.** `MEASURED_FACT`

### 8.2 Complete tag enumeration — `MEASURED_FACT`

All in `ppt/tags/tag1.xml`, all presentation-level.

| # | Tag name | Value (truncated) | References |
|---:|---|---|---|
| 1 | `ISPRING_PROJECT_VERSION` | `9.3` | — |
| 2 | `ISPRING_PROJECT_FOLDER_UPDATED` | `1` | — |
| 3 | `ISPRING_FIRST_PUBLISH` | `1` | — |
| 4 | `ISPRING-SUITE_ISPRING_CURRENT_PLAYER_ID` | `universal` | player skin |
| 5 | `ISPRING_PRESENTATION_COURSE_TITLE` | `MMD_KAK_PL1_T1_1_B1_V2` | — |
| 6 | `ISPRING_LMS_API_VERSION` | `SCORM 2004 (4th edition)` | LMS contract |
| 7 | `ISPRING_ULTRA_SCORM_COURSE_ID` | `DC8FA8F0-C7D4-4252-AD7C-C7ACF6350A60` | SCORM course identity |
| 8 | `ISPRING_CMI5_LAUNCH_METHOD` | `any window` | — |
| 9 | `ISPRINGCLOUDFOLDERID` | `1` | iSpring Cloud |
| 10 | `ISPRINGONLINEFOLDERID` | `1` | iSpring Online |
| 11 | `ISPRING_SCORM_RATE_SLIDES` | `0` | — |
| 12 | `FLASHSPRING_ZOOM_TAG` | `81` | legacy FlashSpring |
| 13 | `ISPRING_UUID` | `{14AF07AC-E6DE-4F59-8DD5-EDDAAC45A0A8}` | project identity |
| 14 | `ISPRING_OUTPUT_FOLDER` | 481 ch — 3 GUID↔path pairs | **external** `D:\` and `C:\Users\HP\OneDrive\…` paths |
| 15 | `ISPRING_RESOURCE_FOLDER` | `D:\KERJA DANIEL\CIDB CYCLE 6 KAK\MMD\PL 06\Topik 3\B2\MMD_KAK_PL6_T3_B2_V4\` | **external** |
| 16 | `ISPRING_PRESENTATION_PATH` | `D:\…\MMD_KAK_PL6_T3_B2_V4.pptx` | **external** |
| 17 | `ISPRING_PRESENTATION_INFO_2` | 1596 ch — embedded XML listing **14 slide GUIDs** with `pptId`s | **internal, dangling** — see §8.3 |
| 18 | `ISPRING_SCREEN_RECS_UPDATED` | `D:\…\MMD_KAK_PL6_T3_B2_V4\` | **external** |
| 19 | `ISPRING-SUITE_ISPRING_PLAYERS_CUSTOMIZATION_2` | **26,502 ch** JSON — full player skin | — |
| 20 | `ISPRING_ULTRA_SCORM_COURCE_TITLE` | `MMD_KAK_PL1_T6_T3_B2_V4` *(sic — `COURCE`)* | — |
| 21 | `ISPRING_PRESENTATION_TITLE` | `MMD_KAK_PL1_T6_T3_B2_V4` | — |
| 22 | `ISPRING_SCORM_ENDPOINT` | 256 ch — `<endpoint><enable>0</enable><lrs>https://…` | LRS endpoint |
| 23 | `ISPRING_PUBLISH_SETTINGS` | 1972 ch JSON | — |

Tag 19 alone is **26,502 characters — roughly 38 % of the 68,710-byte package** before compression.

**No tag references any package part or media item.** Tags 14–16 and 18 reference external Windows
filesystem paths; tag 17 references internal slide GUIDs (§8.3). `ppt/media/image1.svg` is referenced
only by `slide5.xml.rels`, never by a tag.

### 8.3 The tag block is foreign to this deck — `MEASURED_FACT`

Three independent contradictions:

1. **Wrong module.** Every path and title names **PL06 Topik 3 Bahagian 2** (`MMD_KAK_PL6_T3_B2_V4`).
   The deck's own content is **K5 PL06 T03 B02** per the module-reference notes, and the course-title
   tags read `MMD_KAK_PL1_T1_1_B1_V2` and `MMD_KAK_PL1_T6_T3_B2_V4` — **three different course
   identifiers in one tag block**.
2. **Wrong slide count.** `ISPRING_PRESENTATION_INFO_2` enumerates **14** slides with `pptId`s
   `966, 950, 374, 944, 984, 260, 986, 956, 962, 985, 964, 963, 987, 983`. This package has **8**
   slides with `sldId`s `9003, 9008, 9011, 9016, 9017, 9019, 9020, 9021` — **no overlap whatsoever.**
   Every one of the 14 references is dangling.
3. **Foreign authorship.** The paths name `KERJA DANIEL` and `C:\Users\HP\…`; the deck's sole recorded
   editor is `Bariah Ahmad` (`LiveId 0648d156d4325605`).

**Conclusion: the iSpring tag block is inherited debris from a donor file and describes no part of this
artifact.** It carries a live SCORM course ID and an LRS endpoint that belong to a different course.
`MEASURED_FACT` — enters Stage 0A as a hygiene item.

### 8.4 Survival analysis — `PROVISIONAL_IDENTIFIER`

Reasoned from part structure and relationship graph. **Not tested by writing** — the task forbids it,
so each verdict states its basis.

| Path | `ppt/tags/tag1.xml` | `changesInfo1.xml` | `revisionInfo.xml` | Basis |
|---|---|---|---|---|
| **Package-preserving edit** (unzip → edit target XML → rezip) | **survives** | **survives** | **survives** | parts untouched; only the edited part is rewritten |
| **`python-pptx` save** | **expected to survive** | **expected to survive** | **expected to survive** | all three are reachable from `presentation.xml` via `rId11/16/17`. `python-pptx` walks the relationship graph and round-trips parts it has no model for as opaque blobs; `p:custDataLst` is a sibling of `p:sldIdLst` in `presentation.xml` and is not touched by slide add/remove. **Inference from the rel graph, not an executed test.** |
| **PptxGenJS compiler rebuild** | **does not survive** | **does not survive** | **does not survive** | PptxGenJS emits a package from scratch. It has no API for `p:tag` parts, `custDataLst`, `changesInfo`, or `revisionInfo`, and no mechanism to carry an arbitrary inbound part. Anything not modelled by the generator is absent from its output by construction. |

**Explicit preservation or reinjection step required?**

| Part | Required? | Rationale |
|---|---|---|
| `ppt/tags/tag1.xml` | **No — and reinjection is contra-indicated** | §8.3 proves the block is foreign. Reinjecting it would propagate a wrong SCORM course ID, a wrong LRS endpoint, and 14 dangling slide references into a rebuilt package. **Recommend deliberate non-preservation.** `CAIR_RECOMMENDATION` |
| `changesInfo1.xml` | **No for output; YES for evidence** | The change log is the entire basis of the 4-to-8 mapping and the base/added partition. It must be **retained in the evidence chain** but has no place in a compiled deliverable. |
| `revisionInfo.xml` | **No** | Records one client's save counter; no downstream consumer. |

If iSpring publishing is ever a required output path, the correct action is **not** to reinject this
block but to author a **correct** tag set for the actual module. Carrying tag 19's 26,502-character
player skin through a rebuild would also be the single largest contributor to output size.

**Any compiler-rebuild path silently drops all three parts.** Whether that is loss or cleanup differs
per part, and §8.4's recommendation column is the assessment — not a decision. `OPEN_DECISION`

---

## 9. Summary of checkability verdicts

| Rule | Verdict | Label |
|---|---|---|
| R1 narrator prefix `Hilmi:` | flagging-grade only; `Slide 3 Narrator` referent unresolvable; discriminating case absent from evidence | `PROVISIONAL_IDENTIFIER` / `NOT_DETERMINABLE` |
| R2 English terms in italics | mechanically checkable; blocked on a maintained term list; loan-word boundary is the hard problem | `PROVISIONAL_IDENTIFIER` |
| R3 Rumusan visible labels | **fully deterministic, gate-grade**; 4/4 in base, 0/4 in revision; needs case-insensitive + prefix match | `MEASURED_FACT` |
| R4 `anda` vs `kontraktor` | string test deterministic; **scope beyond Rumusan unreconciled** | `PROVISIONAL_IDENTIFIER` / `OPEN_DECISION` |
| R5 industry application | lexical proxies produce false passes on the only available pair | **`JUDGMENT_RULE_NOT_DETERMINISTIC`** |
| R6 Card vs Hotspot | no source-side region data exists in the package; gate not constructible | `PROVISIONAL_IDENTIFIER` |
| Source normalisation | detection deterministic; approval policy is a human decision; `Dan` regression found | `OPEN_DECISION` |
| iSpring metadata | 23 tags, all presentation-level, all foreign to this deck | `MEASURED_FACT` |

---

## 10. Modification statement

No checker was implemented. No gate was created. No lexicon or registry was established. No provisional
identifier was treated as canonical. No PPTX was modified and no part was written or tested by writing.
