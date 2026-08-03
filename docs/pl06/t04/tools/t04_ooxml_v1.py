# -*- coding: utf-8 -*-
"""Exact namespace + local-name element matching for OOXML parts.

WHY THIS EXISTS
---------------
Substring matching on OOXML markup is wrong in a way that reads as right. Two live examples
from this project:

    doc.count("<w:ins")   also counts <w:insideH> and <w:insideV> table borders  → 12, not 0
    <w:t[^>]*>            also matches <w:tcPr>                                  → cell XML as text

The first nearly produced a false claim that the authority document contained twelve tracked
insertions. The second produced raw table markup inside extracted prose. Both were caught, but
only by chance, and both would have been impossible with element-identity matching.

This module is deliberately small. It is a helper, not a framework: three functions over the
standard library's own XML parser, which already understands namespaces.
"""
import re
import xml.etree.ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

NS = dict(w=W)


def qn(local, ns=W):
    """The fully-qualified ElementTree name for a local name in a namespace."""
    return f"{{{ns}}}{local}"


def iter_elements(xml_text, local, ns=W):
    """Every element whose namespace AND local name match exactly.

    <w:insideH> does not match local='ins'. <w:tcPr> does not match local='t'. The parser
    resolves the prefix from the document's own declarations, so a part that binds `w:` to a
    different URI does not silently pass either.
    """
    root = ET.fromstring(xml_text)
    want = qn(local, ns)
    return [e for e in root.iter() if e.tag == want]


def count_elements(xml_text, local, ns=W):
    return len(iter_elements(xml_text, local, ns))


def paragraph_texts(xml_text, ns=W):
    """Visible text per <w:p>, joined with no separator.

    Runs are joined with NO separator on purpose. Word splits a single word across runs at
    formatting and proofing boundaries, so joining with a space inserts spaces mid-word and
    makes genuinely verbatim text compare as altered.
    """
    root = ET.fromstring(xml_text)
    out = []
    for p in root.iter(qn("p", ns)):
        out.append("".join(t.text or "" for t in p.iter(qn("t", ns))))
    return out


def document_text(xml_text, ns=W):
    return re.sub(r"\s+", " ", "".join(
        (t.text or "") for t in ET.fromstring(xml_text).iter(qn("t", ns))))


# ==========================================================================================
# Self-proof. These are the exact confusions that bit this project.
# ==========================================================================================
PROOF_CASES = [
    dict(case_id="XML-01",
         description="<w:insideH> is not <w:ins>",
         fragment='<w:document xmlns:w="{W}"><w:tblBorders><w:insideH w:val="single"/>'
                  '</w:tblBorders></w:document>',
         local="ins", expected_exact=0, naive_pattern="<w:ins", expected_naive=1),
    dict(case_id="XML-02",
         description="<w:insideV> is not <w:ins>",
         fragment='<w:document xmlns:w="{W}"><w:tblBorders><w:insideV w:val="single"/>'
                  '</w:tblBorders></w:document>',
         local="ins", expected_exact=0, naive_pattern="<w:ins", expected_naive=1),
    dict(case_id="XML-03",
         description="<w:tcPr> is not <w:t>",
         fragment='<w:document xmlns:w="{W}"><w:tbl><w:tr><w:tc><w:tcPr/></w:tc></w:tr>'
                  '</w:tbl></w:document>',
         local="t", expected_exact=0, naive_pattern="<w:t", expected_naive=2),
    dict(case_id="XML-04",
         description="a real <w:ins> is still found",
         fragment='<w:document xmlns:w="{W}"><w:p><w:ins w:id="1"><w:r><w:t>x</w:t></w:r>'
                  '</w:ins></w:p></w:document>',
         local="ins", expected_exact=1, naive_pattern="<w:ins", kind="POSITIVE_CONTROL"),
    dict(case_id="XML-05",
         description="a real <w:t> is still found alongside <w:tcPr>",
         fragment='<w:document xmlns:w="{W}"><w:tbl><w:tr><w:tc><w:tcPr/>'
                  '<w:p><w:r><w:t>x</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:document>',
         local="t", expected_exact=1, naive_pattern="<w:t", expected_naive=4),
    dict(case_id="XML-06",
         description="<w:delText> is not <w:del>",
         fragment='<w:document xmlns:w="{W}"><w:p><w:r><w:delText>x</w:delText></w:r>'
                  '</w:p></w:document>',
         local="del", expected_exact=0, naive_pattern="<w:del", expected_naive=2),
]


def proofs():
    out = []
    for c in PROOF_CASES:
        frag = c["fragment"].replace("{W}", W)
        exact = count_elements(frag, c["local"])
        naive = frag.count(c["naive_pattern"])
        out.append(dict(
            case_id=c["case_id"], description=c["description"],
            local_name=c["local"],
            exact_match_count=exact, expected_exact=c["expected_exact"],
            naive_substring_count=naive,
            exact_is_correct=exact == c["expected_exact"],
            kind=c.get("kind", "CONFUSION"),
            # A CONFUSION case must show substring counting giving a different, wrong answer.
            # A POSITIVE_CONTROL only has to show the exact matcher still finds the real
            # element — it exists so the helper cannot pass by returning zero for everything.
            naive_would_have_been_wrong=naive != c["expected_exact"],
            ok=(exact == c["expected_exact"]
                and (c.get("kind") == "POSITIVE_CONTROL" or naive != c["expected_exact"]))))
    return out


if __name__ == "__main__":
    import json
    import sys
    r = proofs()
    print(json.dumps(r, indent=1))
    sys.exit(0 if all(x["ok"] for x in r) else 1)
