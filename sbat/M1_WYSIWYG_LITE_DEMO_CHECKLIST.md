# SBAT M1 WYSIWYG-lite Demo Checklist

> Final M1 demo + verification pack for the SBAT Screen C (one-slide MMD planning) prototype.
> This is a documentation/verification artifact. It does not change the tool's behaviour.

---

## Current verified state

| Item | Value |
|------|-------|
| branch | `main` |
| HEAD | `01d31d2 style(sbat): polish MMD review workflow` |
| UI file | `sbat/m1-screen-c.html` |
| Demo checklist file | `sbat/M1_WYSIWYG_LITE_DEMO_CHECKLIST.md` |

Build chain that produced this state (most recent last):

```
46dd1f8 v0.6.0: Pattern Expansion v1 (P9/P10/P11)
…
39cab3e feat(sbat): add M1 Screen C prototype with register cross-reference
b349e5e feat(sbat): add verified MMD pilot records and ADR-002
21bb03a feat(sbat): add review-first UI for pilot records
bb85231 feat(sbat): add MMD readiness dashboard for pilot records   (M1.2)
750052e feat(sbat): add WYSIWYG-lite slide mock previews            (M1.3)
f9066f5 feat(sbat): add asset requirement view for MMD planning     (M1.4)
291ba7c feat(sbat): add print-ready review handoff                  (M1.5)
c12754d feat(sbat): add editable WYSIWYG-lite treatment preview     (M1.6)
bb84432 feat(sbat): add reviewer decision panel                     (M1.7)
01d31d2 style(sbat): polish MMD review workflow                     (M1.8)  <-- HEAD
```

Single-file, in-memory only: no backend, no database, no localStorage/sessionStorage, no external dependency. Export-to-JSON is the only output artifact.

---

## What SBAT M1 is

- A **review-first Storyboard Authoring Tool** screen (Screen C, one slide at a time).
- A surface that **supports the Bariah/Laila review workflow** for MMD planning.
- A tool that **helps translate workshop/panel inputs into MMD planning decisions** — structuring evidence, dependencies and the decision gate in one place.
- A **visual WYSIWYG-lite preview only** — a lightweight mock of the slide treatment, driven live from the existing review fields.
- A surface where **human ratification remains required** before anything is locked for final MMD build.

---

## What SBAT M1 is not

- It is **not a full WYSIWYG** authoring canvas (no drag/drop authoring, no free-form layout editor).
- It is **not a SCORM builder** or runtime/plugin.
- It is **not an importer** — it does not ingest decks, workshop exports, or registers automatically.
- It is **not a database** app — there is no persistence; everything is in-memory until you Export JSON.
- It is **not an approval system** — it records review intent, not authority.
- It is **not an auto-finalizer** — it never auto-clears a gate or marks content approved.
- It is **not source-of-truth** beyond the verified pilot fields embedded in the page.

---

## Demo narrative

Suggested ~60-second flow to walk through live:

1. **Open** `sbat/m1-screen-c.html` in a browser (double-click; no server needed).
2. **Select a pilot record** — use the top dropdown, or click a row in the dashboard.
3. **Review the MMD Readiness Dashboard** — counters + filters give the at-a-glance status of the 3 pilot records.
4. **Check the Asset Requirement View** — see each record's production dependency type (SB/content, character, quiz-content, visual/asset review).
5. **Inspect the Slide Review evidence** — VO script, on-screen text (AI-derived), MMD graphics/production notes, AMEND-K1 governance, Laila production/visual, SBAT recommendation.
6. **Inspect the WYSIWYG-lite Slide Mock Preview** — the visual mock changes by interaction pattern (P0 static / P6 quiz / P11 drag-match).
7. **Edit existing fields in Advanced / JSON Mode** (e.g. `onscreen_text`, `mmd_graphics_notes`, `pattern`, `decision_gate`) and **observe the live preview update** when you return to Review Mode.
8. **Review "Can MMD proceed?"** — the authoritative decision gate, in plain language.
9. **Use the Reviewer Decision Panel** as a **review-only meeting aid** — pick a decision, add a meeting note. It is not saved and not exported.
10. **Click Print / Save PDF** for a clean handoff sheet of the active slide.

---

## Pilot records included

Three verified pilot records ship embedded in the page (plus a default `s06` sample). These are the only records with verified data — see the Do-not-claim list.

### PL1T3 s2 — character swap
- **pattern:** P0 (Static)
- **gate:** `BLOCKED_PENDING_SB`
- **convergence_type:** `character-swap`
- **meaning:** The on-screen presenter/persona must be confirmed against the approved character bank before final MMD lock. Build action is a presenter swap only; **awaiting SB confirmation**.

### PL3T1 s28 — quiz gap
- **pattern:** P6 (Quiz)
- **gate:** `BLOCKED_PENDING_SB`
- **convergence_type:** `quiz-gap`
- **meaning:** The quiz screen is a placeholder. **Ratified quiz stem, options, correct answer and feedback are needed** from SB before final quiz build.

### PL5T3 s4 — visual / real-image review
- **pattern:** P11 (Drag-Match)
- **gate:** `REVIEW`
- **convergence_type:** `asset-gap`
- **meaning:** The storyboard's **real-image requirement is confirmed** from file, **but missing approved assets are not confirmed**. This is a review of available imagery, not a confirmed missing-asset block.
- **Explicit note:** PL5T3 s4 **must remain REVIEW, not BLOCKED_PENDING_ASSET.** The requirement being confirmed is not the same as an approved asset being confirmed absent.

---

## Manual browser test checklist

Run these by hand in a browser (no automation required). Tick each:

- [ ] Page opens without a JS error (check the browser console).
- [ ] Review Mode loads by default.
- [ ] Dashboard counters appear.
- [ ] Dashboard filters work (All / Blocked SB / Review / Asset / Quiz / Character).
- [ ] Dashboard row **click** loads that record into Review Mode.
- [ ] Dashboard keyboard **Enter/Space** on a focused row loads that record.
- [ ] Dropdown loads each pilot record (s06, PL1T3 s2, PL3T1 s28, PL5T3 s4).
- [ ] Asset Requirement View shows all 3 records as dependency cards.
- [ ] Slide Review fields update per selected record (VO, on-screen text, MMD notes, AMEND-K1, Laila, recommendation).
- [ ] WYSIWYG-lite preview changes by pattern: P0 static, P6 quiz-shell, P11 drag-match.
- [ ] Editing `onscreen_text` (Advanced / JSON Mode) updates the mock preview on-screen text.
- [ ] Editing `mmd_graphics_notes` updates the mock preview treatment note.
- [ ] Changing `decision_gate` updates the preview metadata + MMD implication styling/text.
- [ ] Reviewer Decision Panel selection visually marks the selected option.
- [ ] Reviewer note updates the review-only summary ("Reviewer selection: …" / "Reviewer note: …").
- [ ] Reviewer state (selection + note) resets when another record loads.
- [ ] Print / Save PDF opens the browser print dialog.
- [ ] Print output hides non-handoff controls (dropdown, dashboard, filters, mode toggle, Advanced/JSON panel, Export JSON, Reset/Load, raw JSON, reviewer panel, orientation note).
- [ ] Advanced / JSON Mode still works (form edits + live JSON).
- [ ] Export JSON still works (downloads `<slide_id>.sbat.json`).
- [ ] PL5T3 remains `REVIEW` (not `BLOCKED_PENDING_ASSET`) after loading it.

---

## Verification commands

Run from the repo root.

```bash
# State
git status --short
git log --oneline -5
git diff --stat HEAD~1..HEAD

# JS syntax (extract <script> body, syntax-check with node)
awk '/^<script>/{f=1;next}/^<\/script>/{f=0}f' sbat/m1-screen-c.html > /tmp/m19.js
node --check /tmp/m19.js

# Required sections / functions present in the UI
grep -nE "MMD Readiness Dashboard|Asset Requirement View|Slide Mock Preview|Reviewer Decision Panel|Print / Save PDF" sbat/m1-screen-c.html
grep -nE "renderDashRows|dashActivate|renderAssetView|renderMockPreview|renderHandoff|renderReviewerSummary|resetReviewerPanel" sbat/m1-screen-c.html

# PL5T3 must remain REVIEW, not asset-blocked
grep -nE -A12 '"pl5t3-s4"' sbat/m1-screen-c.html | grep -E 'pattern:"P11"|decision_gate:"REVIEW"|convergence_type:"asset-gap"|BLOCKED_PENDING_ASSET'

# Forbidden additions (expect only benign "no localStorage" comments)
grep -nE "localStorage|sessionStorage|indexedDB|fetch\(|import |script src|SCORM|Kanban|jspdf|pdf-lib|html2canvas" sbat/m1-screen-c.html

# getRecord() body must not be polluted by reviewer/preview/doc state
sed -n '/function getRecord/,/^  }/p' sbat/m1-screen-c.html | grep -iE "reviewer|workflow|demo|talk track|wysiwyg|mock" || echo "getRecord body CLEAN"
```

Expected: JS syntax OK; all sections/functions found; PL5T3 line shows `decision_gate:"REVIEW"`; forbidden grep returns only the two descriptive "no localStorage" comments; `getRecord` body CLEAN.

---

## Do-not-claim list

When demoing, **do not claim**:

- Do not claim the tool has **imported all workshop/deck data** — there is no importer; only the embedded pilot records are present.
- Do not claim **all CIDB slides are verified** — only the 3 pilot records (+ s06 sample) carry verified data.
- Do not claim **PL5T3 has missing approved assets** — the real-image *requirement* is confirmed; **missing approved assets are not confirmed**. It is a REVIEW, not an asset-block.
- Do not claim the **reviewer decision is saved or exported** — the Reviewer Decision Panel is a review-only meeting aid; it is not persisted and not in the exported JSON.
- Do not claim the **WYSIWYG-lite is final** design — it is a display-only WYSIWYG-lite preview mock, not the final MMD build.
- Do not claim **MMD can proceed for blocked slides without SB ratification** — `BLOCKED_PENDING_SB` records (PL1T3 s2, PL3T1 s28) require SB ratification first.

---

## Demo talk track

Short Malay-English (bahasa rojak) script for Firdaus to use with Bariah/Laila:

> "Ni SBAT M1 — bukan nak ganti judgment korang. **SBAT tak replace human judgment.** Dia cuma *structure* review evidence supaya satu slide boleh tengok sekali gus.
>
> Tengok flow dia: **Dashboard** bagi status semua pilot record. **Asset Requirement View** pisahkan jenis dependency — yang mana **SB/content blocker**, yang mana **asset/visual review**, yang mana **MMD action**, dan yang mana **reviewer decision**. Jadi kita tak campur-aduk.
>
> Preview tu **WYSIWYG-lite** je — visual mock, *bukan final design*. Edit field dalam Advanced / JSON Mode, preview update live. Tapi semua ni *display-only* — **kena human ratification dulu** sebelum lock untuk MMD.
>
> Contoh PL5T3 s4: requirement untuk real image memang confirmed, **tapi kita tak claim asset hilang** — so dia kekal **REVIEW**, bukan blocked. PL1T3 s2 dengan PL3T1 s28 pulak **blocked pending SB** — kena SB sign-off dulu, tak boleh proceed main-main.
>
> Reviewer Decision Panel tu **meeting aid je** — boleh tanda decision, boleh tulis note, tapi **tak save, tak export**. Authoritative gate hanya berubah kalau human ubah sendiri.
>
> Last sekali, **Print / Save PDF** untuk handoff masa discussion.
>
> Idea besar dia: **SBAT tolong prepare MMD tanpa pretend benda yang belum settle tu dah final.**"

Key points to land verbally:
- SBAT is **not replacing judgment** — it structures review evidence.
- It **separates SB/content blockers, asset review, MMD action, and reviewer decision**.
- It **helps prepare MMD without pretending unresolved items are final.**

---

## Final readiness verdict

- **M1 is demo-ready** if the Manual browser test checklist above passes.
- The **remaining risk is data coverage, not UI capability** — the workflow surfaces (dashboard, asset view, preview, handoff, reviewer panel) are complete for the 3 verified pilots; what is limited is how many verified records exist.
- The **next phase should focus on importing/expanding verified records only after Bariah/Laila validate the pilot flow** — do not scale data ingestion before the review workflow itself is signed off.
