"""Convert a Markdown case study (or similar) into a Word document, formatted per a rubric spec.

Reads an .md file, writes a .docx with APA-ish formatting (Times New Roman 12pt,
double-spaced, 1" margins, hanging-indent references), then checks each required
section's word count against a rubric spec and prints a report. The default rubric
is the OMDS Module 5 Case Study; pass --rubric <path.json> to use another.

Dependencies: python-docx (`pip install python-docx`).

Usage (from the repo root):
    python utils/md_to_docx.py path/to/case.md                       # default rubric; .docx next to .md
    python utils/md_to_docx.py path/to/case.md -o path/to/out.docx
    python utils/md_to_docx.py path/to/case.md --rubric my_rubric.json
    python utils/md_to_docx.py path/to/case.md --no-check            # skip rubric word-count validation

Rubric JSON schema:
    {
      "name": "...",
      "total":   {"min": 900, "max": 1100},
      "sections": [
        {"heading": "Summary of the Case", "min": 250, "max": 300},
        ...
      ],
      "required_sections": ["References", "AI Appendix"]
    }

Supported Markdown subset: ATX headings (#, ##, ###), paragraphs, hyphen bullets,
GitHub-style tables, **bold**, *italic*, `code`, and [label](url) links.
"""
import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

try:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    sys.exit("python-docx is required. Install with: pip install python-docx")


# -- Default rubric: OMDS Module 5 Case Study ---------------------------------
DEFAULT_RUBRIC = {
    "name": "OMDS Module 5 — Case Study",
    "total": {"min": 900, "max": 1100},
    "sections": [
        {"heading": "Summary of the Case",          "min": 250, "max": 300},
        {"heading": "Stakeholders",                  "min": 250, "max": 300},
        {"heading": "Connection to Broader Issues",  "min": 250, "max": 300},
        {"heading": "Importance",                    "min": 150, "max": 200},
    ],
    "required_sections": ["References", "AI Appendix"],
}


# -- Style constants ----------------------------------------------------------
BODY_FONT = "Times New Roman"
BODY_SIZE_PT = 12
TITLE_SIZE_PT = 14
LINE_SPACING = 2.0           # double-spaced
MARGIN_INCHES = 1.0
LINK_RGB = RGBColor(0x05, 0x63, 0xC1)


# -- Markdown regexes ---------------------------------------------------------
HEADER_RE   = re.compile(r"^(#{1,6})\s+(.*)$")
BULLET_RE   = re.compile(r"^\s*[-*]\s+(.+)$")
METADATA_RE = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-+:?(\s*\|\s*:?-+:?)+\s*\|?\s*$")
INLINE_RE   = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")
LINK_RE     = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


# -- Parsed model -------------------------------------------------------------
@dataclass
class Section:
    heading: str
    level: int
    blocks: list = field(default_factory=list)   # ("para"|"bullet"|"table", payload)

    def plain_body_text(self) -> str:
        """Flatten the section body with markdown markers stripped, for word counting."""
        parts: List[str] = []
        for kind, payload in self.blocks:
            if kind in ("para", "bullet"):
                parts.append(strip_markdown(payload))
            elif kind == "table":
                for row in payload:
                    parts.extend(strip_markdown(cell) for cell in row)
        return " ".join(parts)


def strip_markdown(text: str) -> str:
    text = re.sub(r"\*\*|\*|`", "", text)
    text = LINK_RE.sub(r"\1", text)
    return text


def count_words(text: str) -> int:
    """Whitespace-separated tokens — matches MS Word's and `wc -w` conventions."""
    return len(text.split())


# -- Markdown parser ----------------------------------------------------------
def parse_markdown(md: str) -> Tuple[dict, List[Section]]:
    """Return ({title, metadata}, [Section]). Preamble = content before the first H2."""
    lines = md.splitlines()
    title: Optional[str] = None
    metadata: List[Tuple[Optional[str], str]] = []
    sections: List[Section] = []
    cur: Optional[Section] = None
    i = 0

    # Phase 1: preamble (everything before the first H2)
    while i < len(lines):
        ln = lines[i].rstrip()
        h = HEADER_RE.match(ln)
        if h and len(h.group(1)) >= 2:
            break
        if not ln.strip() or ln.strip() == "---":
            i += 1
            continue
        if h and len(h.group(1)) == 1 and title is None:
            title = h.group(2).strip()
            i += 1
            continue
        m = METADATA_RE.match(ln)
        if m:
            metadata.append((m.group(1).strip(), m.group(2).strip()))
        else:
            metadata.append((None, ln.strip()))
        i += 1

    # Phase 2: body sections (H2 and deeper)
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip() or ln.strip() == "---":
            i += 1
            continue

        h = HEADER_RE.match(ln)
        if h and len(h.group(1)) >= 2:
            cur = Section(heading=h.group(2).strip(), level=len(h.group(1)))
            sections.append(cur)
            i += 1
            continue
        if cur is None:
            i += 1
            continue

        # Table block (header row followed by separator row)
        if ln.strip().startswith("|") and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
            rows: List[List[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if TABLE_SEP_RE.match(lines[i]):
                    i += 1
                    continue
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            cur.blocks.append(("table", rows))
            continue

        b = BULLET_RE.match(ln)
        if b:
            cur.blocks.append(("bullet", b.group(1).strip()))
            i += 1
            continue

        # Paragraph: join wrapped continuation lines until a break-type line
        buf = [ln.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if (not nxt.strip() or nxt.strip() == "---"
                    or HEADER_RE.match(nxt) or BULLET_RE.match(nxt)
                    or nxt.strip().startswith("|")):
                break
            buf.append(nxt.strip())
            i += 1
        cur.blocks.append(("para", " ".join(buf)))

    return {"title": title, "metadata": metadata}, sections


# -- DOCX rendering -----------------------------------------------------------
def set_body_font(run):
    run.font.name = BODY_FONT
    run.font.size = Pt(BODY_SIZE_PT)


def style_paragraph(p, *, align=None, first_line=None, left=None, hanging=None,
                    space_after=0):
    pf = p.paragraph_format
    pf.line_spacing = LINE_SPACING
    pf.space_before = Pt(0)
    pf.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    if hanging is not None:
        pf.left_indent = Inches(hanging)
        pf.first_line_indent = Inches(-hanging)
    else:
        if first_line is not None:
            pf.first_line_indent = Inches(first_line)
        if left is not None:
            pf.left_indent = Inches(left)


def add_inline_runs(paragraph, text: str):
    """Add text with **bold**, *italic*, `code`, and [link](url) support."""
    pos = 0
    for m in INLINE_RE.finditer(text):
        if m.start() > pos:
            r = paragraph.add_run(text[pos:m.start()])
            set_body_font(r)
        token = m.group()
        if token.startswith("**"):
            r = paragraph.add_run(token[2:-2])
            set_body_font(r); r.bold = True
        elif token.startswith("`"):
            r = paragraph.add_run(token[1:-1])
            r.font.name = "Courier New"
            r.font.size = Pt(BODY_SIZE_PT - 1)
        elif token.startswith("["):
            lm = LINK_RE.match(token)
            r = paragraph.add_run(lm.group(1))
            set_body_font(r)
            r.font.color.rgb = LINK_RGB
            r.font.underline = True
        else:                                  # *italic*
            r = paragraph.add_run(token[1:-1])
            set_body_font(r); r.italic = True
        pos = m.end()
    if pos < len(text):
        r = paragraph.add_run(text[pos:])
        set_body_font(r)


def write_docx(preamble: dict, sections: List[Section], out_path: str):
    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(MARGIN_INCHES)
        s.left_margin = s.right_margin = Inches(MARGIN_INCHES)

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(BODY_SIZE_PT)

    # Title + metadata (centered block at top)
    if preamble["title"]:
        p = doc.add_paragraph()
        style_paragraph(p, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(preamble["title"])
        r.font.name = BODY_FONT
        r.font.size = Pt(TITLE_SIZE_PT)
        r.bold = True
    for label, value in preamble["metadata"]:
        p = doc.add_paragraph()
        style_paragraph(p, align=WD_ALIGN_PARAGRAPH.CENTER)
        if label:
            r = p.add_run(f"{label}: ")
            set_body_font(r); r.bold = True
            add_inline_runs(p, value)
        else:
            add_inline_runs(p, value)

    if preamble["title"] or preamble["metadata"]:
        doc.add_paragraph()                    # blank spacer before first section

    for sec in sections:
        is_refs = sec.heading.strip().lower() == "references"

        # Section heading
        p = doc.add_paragraph()
        style_paragraph(p, space_after=4)
        r = p.add_run(sec.heading)
        set_body_font(r); r.bold = True
        if sec.level >= 3:
            r.italic = True

        for kind, payload in sec.blocks:
            if kind == "para":
                p = doc.add_paragraph()
                if is_refs:
                    style_paragraph(p, hanging=0.5)
                else:
                    style_paragraph(p, first_line=0.5)
                add_inline_runs(p, payload)
            elif kind == "bullet":
                p = doc.add_paragraph(style="List Bullet")
                style_paragraph(p)
                add_inline_runs(p, payload)
            elif kind == "table":
                if not payload:
                    continue
                cols = max(len(row) for row in payload)
                t = doc.add_table(rows=len(payload), cols=cols)
                try:
                    t.style = "Light Grid Accent 1"
                except KeyError:
                    pass
                for r_idx, row in enumerate(payload):
                    for c_idx in range(cols):
                        cell_text = row[c_idx] if c_idx < len(row) else ""
                        cell = t.rows[r_idx].cells[c_idx]
                        cell.text = ""
                        para = cell.paragraphs[0]
                        add_inline_runs(para, cell_text)
                        if r_idx == 0:
                            for run in para.runs:
                                run.bold = True
                doc.add_paragraph()            # spacer below table

    doc.save(out_path)


# -- Rubric validation --------------------------------------------------------
def validate(sections: List[Section], rubric: dict) -> bool:
    print(f"\n=== Rubric check: {rubric['name']} ===")
    by_heading = {s.heading.strip().lower(): s for s in sections}
    rows: List[Tuple[str, Optional[int], int, int, str]] = []
    total = 0

    for rs in rubric.get("sections", []):
        key = rs["heading"].strip().lower()
        if key not in by_heading:
            rows.append((rs["heading"], None, rs["min"], rs["max"], "MISSING"))
            continue
        wc = count_words(by_heading[key].plain_body_text())
        total += wc
        if   wc < rs["min"]: status = "UNDER"
        elif wc > rs["max"]: status = "OVER"
        else:                status = "OK"
        rows.append((rs["heading"], wc, rs["min"], rs["max"], status))

    hd_width = max((len(r[0]) for r in rows), default=20) + 2
    for heading, wc, mn, mx, status in rows:
        wc_str = f"{wc:>5}" if wc is not None else "  -  "
        print(f"  [{status:7}] {heading.ljust(hd_width)}{wc_str}  target {mn}-{mx}")

    missing_req = [name for name in rubric.get("required_sections", [])
                   if name.strip().lower() not in by_heading]
    for name in missing_req:
        print(f"  [MISSING] required section: {name}")

    tmin, tmax = rubric["total"]["min"], rubric["total"]["max"]
    if   total < tmin: tstatus = "UNDER"
    elif total > tmax: tstatus = "OVER"
    else:              tstatus = "OK"
    print(f"  [{tstatus:7}] {'TOTAL'.ljust(hd_width)}{total:>5}  target {tmin}-{tmax}")

    return all(r[-1] == "OK" for r in rows) and not missing_req and tstatus == "OK"


# -- CLI ----------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("md", help="input markdown file")
    ap.add_argument("-o", "--out", help="output .docx (default: alongside the .md)")
    ap.add_argument("--rubric", help="rubric JSON (default: OMDS case study)")
    ap.add_argument("--no-check", action="store_true", help="skip rubric word-count validation")
    args = ap.parse_args()

    with open(args.md, encoding="utf-8") as f:
        md = f.read()

    rubric = DEFAULT_RUBRIC
    if args.rubric:
        with open(args.rubric, encoding="utf-8") as f:
            rubric = json.load(f)

    preamble, sections = parse_markdown(md)
    out = args.out or os.path.splitext(args.md)[0] + ".docx"
    write_docx(preamble, sections, out)
    size_kb = os.path.getsize(out) / 1024
    print(f"wrote {out}  ({size_kb:.1f} KB)")

    if not args.no_check:
        ok = validate(sections, rubric)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
