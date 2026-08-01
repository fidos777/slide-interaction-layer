# BARIAH_REVIEW_CHECKLIST — v0.4.3

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx` — 100 review pages.

# What changed since v0.4.2

Your three WhatsApp screenshots of 1 August are now **frozen in the repository and hash-checked on
every run**. Until they arrived, those three rulings existed only as typed-out text in a task
message, and we would not treat typed text as if it were your screenshot. Every correction below is
now bound to the image it came from.

## 1. S01 — Speaker Notes re-cut, exactly as you marked

Your boxed block said **"Speaker Notes: Edit to this"**. Four spoken lines are now three:

```
PL06: Pengurusan Operasi Pembinaan Landskap.
Topik 3 Bahagian 2: Komponen Landskap.
Klik butang “Mula” untuk memulakan pembelajaran.
```

- `Pakej Latihan 06:` → `PL06:`
- *"Dalam bahagian ini, anda akan mempelajari tentang komponen landskap."* — **removed**
- *"Klik Mula untuk meneruskan."* → *"Klik butang “Mula” untuk memulakan pembelajaran."*

Two things on the S01 canvas were also wrong against your corrected page and are now fixed: the
**Topik 3 Bahagian 2 line** was missing from the body, and the **`ARAHAN VISUAL — SPESIFIKASI
SAHAJA`** heading above the visual direction was not being drawn. Your two title marks (① retitle,
② remove the duplicate) were already in from v0.4.1.

## 2. "Semua contoh ada visual" — now applied without a qualifier

At v0.4.2 we read your rule as conditional for the Contoh screens, because your corrected slide 12
showed no visual line. **The message you sent carries no qualifier**, so that reading is withdrawn.

Every example card on the four Contoh screens now carries **its own visual direction** — the same
one its popup shows, taken from that example's own source row. We did not write a new direction for
the screen as a whole, because you did not give one.

Specification popups still have **no** visual panel, per *"KECUALI pop up Spesifikasi"*.

## 3. Struktur Persisir Air — the conflict you were asked about is closed

At v0.4.2 we flagged a conflict and asked you to choose. Your screenshot of that screen answers it:

```
ACTIVE       [Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]
SUPERSEDED   [Visual: Rajah 23 — Contoh Boardwalk …]   ← as the component-main direction only
```

Rajah 23 is still the **Boardwalk example's** own direction and still appears there. Only its use on
the component-main screen is retired. The retired instruction is printed in that page's production
panel as `ARAHAN DIGANTI` so the history stays visible; it is not a second live instruction.

**There are now zero open evidence conflicts in the deck.**

# What we did NOT decide for you

Your caption read *"Slide 5 - apply to yang lain where applicable/necessary"*. That tells us the
principle, not the content, and *"where applicable/necessary"* is your call. So **eight
component-main screens are still awaiting your decision** and show the module's own visual text
marked `PROVISIONAL_VISUAL_PROPOSAL`:

Struktur Teduhan · Kemudahan Awam · Water Feature · Kerusi Taman · Papan Tanda · Tong Sampah ·
Drinking Fountain · BBQ Pit

Please either confirm the module text for each, or give the direction you want.

# Review priorities — not limits

Please look at these first. **If you see anything else wrong, flag it** — this is where we think the
risk is, not a boundary on what you may raise.

1. **S01 (page 1)** — is the canvas and the Speaker Notes now exactly as you marked?
2. **Contoh screens** — pages 6–12 (Struktur Persisir Air) and the three others. Each card now has a
   small grey direction beneath it. Is that the right placement, and the right level of detail?
3. **The eight component mains above** — the one decision block left in this deck.
4. **Struktur Persisir Air main (page 5)** — confirm the direction we settled on is the one you meant.

# One defect worth knowing about

The card visuals were initially derived from the *state* rather than the *screen*, so the popup and
all-viewed versions of each Contoh screen rendered with no card visuals at all — while the automated
suite reported everything green. It was caught by looking at the rendered pages. A new check now
measures all 24 state pages of those 4 screens, and the earlier deck fails it.

That is worth stating plainly: **303 of 303 checks passing measures the checks, not the deck.** Your
eye still finds things ours does not.

# Standing

`REVIEW_READY` · `NOT_FOR_MMD_BUILD` · `MULTIMEDIA_NOT_PRODUCED`

Not claimed: `PRODUCTION_APPROVED`, `CANONICAL_FREEZE`, `MMD_BUILD_READY`,
`SOURCE_INTEGRITY_FULLY_VERIFIED`, `MICROSOFT_POWERPOINT_EQUIVALENCE`. The deck has **not** been
opened in Microsoft PowerPoint — this container cannot run it. `B02-CAIR-INT-001` is still open.
