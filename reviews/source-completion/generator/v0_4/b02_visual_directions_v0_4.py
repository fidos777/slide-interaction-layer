# -*- coding: utf-8 -*-
"""Controlled visual-direction resolver.

The v0.4 generator built a generic sentence whenever a source row carried no figure:

    [Visual: Arahan visual untuk Promenade — spesifikasi teks sahaja, modul ms 238.
     Tidak dibenamkan.]

Bariah's corrected exemplar (annotated deck, slide 14) shows the intended treatment:

    ARAHAN VISUAL — TIDAK DIBENAMKAN
    [Visual:  Promenade Tasik Titiwangsa, KL]

i.e. the direction names the SOURCE-ATTESTED example, never an auto-generated sentence.
This module is the single place any visual direction is decided.

Authority order, highest first:
  1. direct Bariah annotation in the reviewed vBariah deck
  2. Bariah correction exemplar          -> the row's source-attested `contoh`
  3. approved S&G visual direction
  4. exact source-attested example or named structure
  5. existing source asset mapping       -> the row's `visual`, which names Rajah/foto + asset id
  6. specific textual direction derived directly from the source

Nothing is invented. A row that satisfies none of these is marked
PENDING_SPECIFIC_VISUAL_DIRECTION and is never given fallback prose.
"""

HEADING = "ARAHAN VISUAL — TIDAK DIBENAMKAN"

ASSET = "SOURCE_ASSET_FIGURE"
CONTOH = "BARIAH_EXEMPLAR_CONTOH"
PENDING = "PENDING_SPECIFIC_VISUAL_DIRECTION"

# Generic shapes that must never reach a learner page again.
FALLBACK_MARKERS = ("Arahan visual untuk", "spesifikasi teks sahaja")


def for_row(row):
    """Visual direction for a source row. Returns dict(text, authority, status)."""
    vis = (row.get("visual") or "").strip()
    if vis:
        return dict(text=vis, authority=ASSET, status="RESOLVED",
                    source_row_uid=row["uid"], locator=f"modul ms {row['ms']}")
    contoh = (row.get("contoh") or "").strip()
    if contoh:
        return dict(text=f"[Visual: {contoh}]", authority=CONTOH, status="RESOLVED",
                    source_row_uid=row["uid"], locator=f"modul ms {row['ms']}")
    return dict(text=None, authority=None, status=PENDING,
                source_row_uid=row["uid"], locator=f"modul ms {row['ms']}")


def for_specification(row, label):
    """Specification popups stay tied to their parent example and source row."""
    base = for_row(row)
    if base["status"] != "RESOLVED":
        return base
    return dict(text=f"[Visual: {row['label']} — {label}. {base['text'][8:].rstrip(']')}]"
                if base["authority"] == CONTOH else base["text"],
                authority=base["authority"], status="RESOLVED",
                source_row_uid=row["uid"], locator=base["locator"],
                specification=label)


def is_generic(text):
    return bool(text) and any(m in text for m in FALLBACK_MARKERS)


def audit(M):
    """Every visual direction the deck will draw, with its authority."""
    rows = []
    for r in M.source["rows"]:
        d = for_row(r)
        rows.append(dict(source_row_uid=r["uid"], component=r["comp"], label=r["label"],
                         **{k: d[k] for k in ("text", "authority", "status", "locator")}))
    return rows
