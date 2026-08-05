# -*- coding: utf-8 -*-
"""Stage 4.2F-H — FROZEN font advance widths for review-page break decisions.

WHY THIS FILE EXISTS
--------------------
Page-break decisions must be reproducible from committed data alone. Measuring text at
build time — loading a font off the host, asking PIL for a string width — makes pagination
depend on which fonts the machine happens to have and on the imaging library's version. A
different host could then paginate differently from the same model, and the page-break map
would not be a property of the input.

Everything below is a versioned literal. The table is the horizontal ADVANCE of each
character in 1/1000 em, measured once from the font named below and committed. Widths scale
linearly with point size, so a width in points is pure arithmetic:

    width_pt(text, size_pt) = sum(ADVANCE[c] for c in text) / 1000 * size_pt

Kerning is deliberately NOT modelled. Sum-of-advances is greater than or equal to the kerned
width for every pair Liberation Sans kerns, so the estimate is conservative: it breaks a line
slightly early rather than slightly late.

`verify_against_font()` re-measures this table and is used by QA only. It is never called
from the pagination decision path.
"""

VERSION = "1"
FONT_FAMILY = "Liberation Sans Regular"
FONT_FILE_MEASURED = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_SHA256 = "4659bc0c58c5028dd488ec928d41d9265db43d9b669fc14ca8b0832daca7b144"
UNITS_PER_EM = 1000
MEASURED_WITH = "PIL.ImageFont.truetype(size=1000).getlength(char), rounded to int"

# Fallback for any character outside the table. 'm' is the widest lowercase glyph, so an
# unknown character is over-measured rather than under-measured.
FALLBACK = 833

ADVANCE = {
    ' ': 278,
    '!': 278,
    '"': 355,
    '#': 556,
    '$': 556,
    '%': 889,
    '&': 667,
    "'": 191,
    '(': 333,
    ')': 333,
    '*': 389,
    '+': 584,
    ',': 278,
    '-': 333,
    '.': 278,
    '/': 278,
    '0': 556,
    '1': 556,
    '2': 556,
    '3': 556,
    '4': 556,
    '5': 556,
    '6': 556,
    '7': 556,
    '8': 556,
    '9': 556,
    ':': 278,
    ';': 278,
    '<': 584,
    '=': 584,
    '>': 584,
    '?': 556,
    '@': 1015,
    'A': 667,
    'B': 667,
    'C': 722,
    'D': 722,
    'E': 667,
    'F': 611,
    'G': 778,
    'H': 722,
    'I': 278,
    'J': 500,
    'K': 667,
    'L': 556,
    'M': 833,
    'N': 722,
    'O': 778,
    'P': 667,
    'Q': 778,
    'R': 722,
    'S': 667,
    'T': 611,
    'U': 722,
    'V': 667,
    'W': 944,
    'X': 667,
    'Y': 667,
    'Z': 611,
    '[': 278,
    '\\': 278,
    ']': 278,
    '^': 469,
    '_': 556,
    '`': 333,
    'a': 556,
    'b': 556,
    'c': 500,
    'd': 556,
    'e': 556,
    'f': 278,
    'g': 556,
    'h': 556,
    'i': 222,
    'j': 222,
    'k': 500,
    'l': 222,
    'm': 833,
    'n': 556,
    'o': 556,
    'p': 556,
    'q': 556,
    'r': 333,
    's': 500,
    't': 278,
    'u': 556,
    'v': 500,
    'w': 722,
    'x': 500,
    'y': 500,
    'z': 500,
    '{': 334,
    '|': 260,
    '}': 334,
    '~': 584,
    '°': 400,
    '·': 333,
    '×': 584,
    '–': 556,
    '—': 1000,
    '‘': 222,
    '’': 222,
    '“': 333,
    '”': 333,
    '…': 1000,
}


def text_width_pt(text, size_pt):
    """Width of `text` in points. Pure arithmetic over frozen data."""
    return sum(ADVANCE.get(c, FALLBACK) for c in text) / UNITS_PER_EM * size_pt


def wrap(text, size_pt, width_pt):
    """Greedy word wrap, identical in shape to the renderer's, using frozen widths only."""
    out, cur = [], ""
    for w in text.split():
        probe = (cur + " " + w).strip()
        if text_width_pt(probe, size_pt) > width_pt:
            if cur:
                out.append(cur)
            cur = w
        else:
            cur = probe
    if cur:
        out.append(cur)
    return out or [""]


def verify_against_font(path=FONT_FILE_MEASURED):
    """QA ONLY. Re-measure the table. Never called from a pagination decision."""
    import hashlib
    from PIL import ImageFont
    with open(path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    font = ImageFont.truetype(path, UNITS_PER_EM)
    drift = [c for c, w in ADVANCE.items() if round(font.getlength(c)) != w]
    return dict(sha256=digest, sha256_matches=digest == FONT_SHA256,
                characters=len(ADVANCE), drifted=sorted(drift))
