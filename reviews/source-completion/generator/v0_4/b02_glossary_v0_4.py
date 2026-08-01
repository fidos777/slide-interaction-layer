# -*- coding: utf-8 -*-
"""ONE controlled italic glossary for K5 PL06 T03 B02 v0.4.

Used by BOTH the learner canvas and the Speaker Notes writer. There is deliberately no
second term list anywhere in the toolchain: two lists drift, and a term italicised on the
canvas but not in the Notes is exactly the regression Bariah found.

Policy source: Bariah's review guide item 5 — "GLOBAL di speaker notes untuk semua slide.
English words in italic" — and S&G v0.3.
"""
import re

# Longest first so a multi-word phrase always wins over a shorter overlap.
ITALIC_TERMS = [
    "Wood-Plastic Composite",   # S&G v0.3, N-06 authorised form
    "Multiple Response",        # quiz item type, Bariah exemplar slide 73
    "Drinking Fountain",        # component name, Bariah exemplar slide 6 / 43
    "Water Feature",            # component name, Bariah exemplar slide 6 / 71
    "Boardwalk",                # source row label, modul ms 238
    "Footbridge",               # source row label, modul ms 238
    "Promenade",                # source row label, modul ms 238
    "Mind Map",                 # S03 visual direction, Bariah exemplar slide 6
    "BBQ Pit",                  # component name, capital P per S&G v0.3
]

# Never italicised even where the characters are Latin: identifiers and metadata.
NEVER_ITALIC_PREFIXES = ("K5-PL06", "K5PL06", "SCR_", "ST_", "II_", "RP-", "B02-", "SFX_",
                         "FAMILY_", "PP-", "http", "modul ms")
NEVER_ITALIC_TOKENS = {"ACP", "HPL", "UV", "WPC", "HDPE", "FRC", "PVC", "MMD", "LMS",
                       "CIDB", "PL06", "MS2680", "KL"}

_PAT = re.compile("(" + "|".join(re.escape(t) for t in ITALIC_TERMS) + ")")


def parts(s):
    """Split a string into [(text, italic)] runs. Case-sensitive: the lowercase Malay
    forms that appear inside VO prose are not instructional terminology."""
    if not s:
        return [("", False)]
    out = []
    for tok in _PAT.split(s):
        if not tok:
            continue
        ital = tok in ITALIC_TERMS
        if ital and (any(tok.startswith(p) for p in NEVER_ITALIC_PREFIXES)
                     or tok in NEVER_ITALIC_TOKENS):
            ital = False
        out.append((tok, ital))
    return out or [(s, False)]


def occurrences(s):
    """Every glossary occurrence in a string, as (term, start, end)."""
    return [(m.group(1), m.start(1), m.end(1)) for m in _PAT.finditer(s or "")]
