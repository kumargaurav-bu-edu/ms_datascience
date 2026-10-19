"""Combine executed Jupyter notebooks into one bookmarked PDF (no LaTeX needed).

Pipeline: nbconvert (HTML, "lab" template, images embedded) -> headless Google Chrome
(print-to-pdf) -> pypdf merge with a cover/contents page and one bookmark per notebook.
Saved outputs are used as-is; notebooks are NOT re-executed.

Usage (from the repo root, in an env with nbconvert + pypdf, e.g. uiapp311):
    python utils/notebooks_to_pdf.py                       # Milestone One appendix (defaults below)
    python utils/notebooks_to_pdf.py -o out.pdf a.ipynb b.ipynb --title "My appendix"

Rendering notes:
  * Wide pandas tables are shrunk to the page width (JS run before printing).
  * MathJax is stripped so currency like "$76,437" prints literally. Remove that step
    (--keep-math) if a notebook contains real $...$ LaTeX.
"""
import argparse, html, os, re, shutil, subprocess, sys, tempfile

import nbformat
from nbconvert import HTMLExporter
from pypdf import PdfReader, PdfWriter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "", shutil.which("chrome") or "",
]

# Default set: Milestone One notebook appendix (DX799O1)
DEFAULT_TITLE = "Milestone One — Notebook Appendix"
DEFAULT_SUBTITLE = "Predicting Consumer Credit Default Across Two Markets"
DEFAULT_AUTHOR = "Kumar Gaurav · DX799 O1 Data Science Capstone (Fall 2026) · Boston University OMDS"
DEFAULT_OUT = "week_10092026_w7/DX799O1/kumar_gaurav_milestone1_notebooks.pdf"
DEFAULT_NBS = [
    ("Week 1 — Polynomial and Interaction Terms", "week_08282026/DX799O1/homework/kumar_gaurav_week1_dx799O1_v2.ipynb"),
    ("Week 2 — Ridge, Lasso and Elastic Net", "week_09042026/DX799O1/homework/kumar_gaurav_week2_dx799O1_v2.ipynb"),
    ("Week 3 — Stepwise Selection, PCR and PLSR", "week_09112026/DX799O1/homework/kumar_gaurav_week3_dx799O1_v2.ipynb"),
    ("Week 4 — Logistic Regression and Feature Scaling", "week_09182026/DX799O1/homework/kumar_gaurav_week4_dx799O1_v2.ipynb"),
    ("Week 5 — Support Vector Machines", "week_09252026/DX799O1/homework/kumar_gaurav_week5_dx799O1_v2.ipynb"),
    ("Week 6 — Decision Trees and Random Forests", "week_10022026/DX799O1/homework/kumar_gaurav_week6_dx799O1_v2.ipynb"),
]

CSS = """<style>
@page { size: Letter; margin: 0.6in; }
body { font-size: 11px; }
pre, .jp-OutputArea-output pre, .highlight pre { white-space: pre-wrap !important; word-break: break-word; }
.jp-OutputArea-output, .jp-OutputArea-output.jp-RenderedHTMLCommon, .jp-RenderedHTML { overflow: visible !important; }
.jp-OutputArea-output table { font-size: 9px !important; table-layout: auto; }
.jp-OutputArea-output table td, .jp-OutputArea-output table th { padding: 1px 4px !important; }
img { max-width: 100% !important; height: auto; page-break-inside: avoid; }
.jp-Cell { page-break-inside: auto; }
.nb-banner { font-family: Georgia, serif; border-bottom: 2px solid #333; margin-bottom: 12px; }
</style>
<script>
// shrink only the tables that overflow the page width
window.addEventListener('load', function () {
  document.querySelectorAll('.jp-OutputArea-output table').forEach(function (t) {
    var box = t.closest('.jp-OutputArea-output') || t.parentElement;
    var avail = box.clientWidth || 640, fs = 9;
    while (t.scrollWidth > avail && fs > 5) { fs -= 0.5; t.style.setProperty('font-size', fs + 'px', 'important'); }
    if (t.scrollWidth > avail) {
      var s = avail / t.scrollWidth; t.style.transformOrigin = 'top left'; t.style.transform = 'scale(' + s + ')';
      t.parentElement.style.height = (t.offsetHeight * s + 4) + 'px';
    }
  });
});
</script>"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if c and os.path.exists(c):
            return c
    sys.exit("Google Chrome/Chromium not found; install it or edit CHROME_CANDIDATES.")


def chrome_pdf(chrome, html_path, pdf_path):
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=5000", f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)


def cover_html(title, subtitle, author, nbs):
    items = "".join(f"<li>{html.escape(t)}<br><small><code>{html.escape(p)}</code></small></li>" for t, p in nbs)
    return f"""<html><head>{CSS}</head><body style="font-family: Georgia, serif; font-size:14px">
<div style="margin-top:2.5in; text-align:center"><h1>{html.escape(title)}</h1>
<h2>{html.escape(subtitle)}</h2><p>{html.escape(author)}</p></div>
<div style="margin:0.8in auto; width:70%"><h3>Contents</h3><ol>{items}</ol>
<p><small>All outputs shown are the saved executed results.</small></p></div></body></html>"""


def notebook_html(exporter, path, title, rel, keep_math):
    body, _ = exporter.from_notebook_node(nbformat.read(path, as_version=4))
    if not keep_math:
        body = re.sub(r"<script[^>]*mathjax[^>]*>\s*</script>", "", body, flags=re.I)
        body = re.sub(r'<script type="text/x-mathjax-config">.*?</script>', "", body, flags=re.S | re.I)
    banner = f'<div class="nb-banner"><h1>{html.escape(title)}</h1><p><code>{html.escape(rel)}</code></p></div>'
    body = body.replace("</head>", CSS + "</head>", 1)
    i = body.find(">", body.find("<body")) + 1
    return body[:i] + banner + body[i:]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("notebooks", nargs="*", help="notebook paths (default: Milestone One set)")
    ap.add_argument("-o", "--out", default=None, help="output PDF path")
    ap.add_argument("--title", default=DEFAULT_TITLE)
    ap.add_argument("--subtitle", default=DEFAULT_SUBTITLE)
    ap.add_argument("--author", default=DEFAULT_AUTHOR)
    ap.add_argument("--keep-math", action="store_true", help="keep MathJax (for real $...$ LaTeX)")
    a = ap.parse_args()

    if a.notebooks:
        nbs = [(os.path.splitext(os.path.basename(p))[0], os.path.relpath(os.path.abspath(p), REPO)) for p in a.notebooks]
        out = a.out or "notebooks.pdf"
    else:
        nbs, out = DEFAULT_NBS, a.out or os.path.join(REPO, DEFAULT_OUT)
    out = os.path.abspath(out)

    chrome = find_chrome()
    exporter = HTMLExporter(template_name="lab")
    exporter.embed_images = True

    with tempfile.TemporaryDirectory() as work:
        open(f"{work}/cover.html", "w").write(cover_html(a.title, a.subtitle, a.author, nbs))
        chrome_pdf(chrome, f"{work}/cover.html", f"{work}/cover.pdf")
        parts = [("Cover and contents", f"{work}/cover.pdf")]
        for i, (title, rel) in enumerate(nbs, 1):
            hp, pp = f"{work}/nb{i}.html", f"{work}/nb{i}.pdf"
            open(hp, "w").write(notebook_html(exporter, os.path.join(REPO, rel), title, rel, a.keep_math))
            chrome_pdf(chrome, hp, pp)
            parts.append((title, pp))
            print(f"{title}: {len(PdfReader(pp).pages)} pages", flush=True)

        writer, page = PdfWriter(), 0
        for title, pp in parts:
            r = PdfReader(pp)
            for p in r.pages:
                writer.add_page(p)
            writer.add_outline_item(title, page)
            page += len(r.pages)
        writer.add_metadata({"/Title": a.title})
        with open(out, "wb") as f:
            writer.write(f)
    print(f"saved {out} ({page} pages, {os.path.getsize(out) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
