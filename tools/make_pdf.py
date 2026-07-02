#!/usr/bin/env python3
"""
make_pdf.py - Markdown -> publication-quality, self-contained HTML (offline), + best-effort PDF.

Guaranteed output: one self-contained .html (embedded CSS, no external deps) that you can
read anywhere and print to PDF from the browser (Ctrl/Cmd+P -> Save as PDF). Mermaid code
fences are pre-rendered to inline SVG when mermaid-cli is available (else left as a labelled
code block). PDF is produced automatically only if pandoc/wkhtmltopdf is installed.

Usage:
    python tools/make_pdf.py <input.md> [--out-dir DIR] [--title TITLE]

Requires: python `markdown` (pip install markdown). Diagram rendering + PDF are best-effort;
the tool never hard-fails. Content stays local.
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CSS = """
@page { size: A4; margin: 20mm; }
* { box-sizing: border-box; }
body { font: 15px/1.6 -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
       color: #1a1a1a; max-width: 820px; margin: 40px auto; padding: 0 24px; }
h1,h2,h3 { line-height: 1.25; margin: 1.4em 0 .5em; }
h1 { font-size: 2em; border-bottom: 2px solid #2b6cb0; padding-bottom: .2em; }
h2 { font-size: 1.45em; color: #2b3a4a; } h3 { font-size: 1.15em; color: #2b3a4a; }
p, li { font-size: 15px; } a { color: #2b6cb0; }
code { background: #f2f4f7; padding: .1em .35em; border-radius: 4px; font-size: .9em; }
pre { background: #f7f9fc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;
      overflow-x: auto; font-size: .85em; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #d7dee8; padding: 8px 10px; text-align: left; }
th { background: #eef3fa; }
blockquote { border-left: 4px solid #cbd5e0; margin: 1em 0; padding: .2em 1em; color: #4a5568; }
.mermaid-diagram { margin: 1.2em 0; text-align: center; }
.mermaid-diagram svg { max-width: 100%; height: auto; }
@media print { body { margin: 0; max-width: none; } a { color: #1a1a1a; } }
"""


def render_mermaid_blocks(md: str) -> str:
    """Replace ```mermaid fences with inline SVG (best-effort). Leave as code block on failure."""
    npx = shutil.which("npx")
    pattern = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)

    def repl(m):
        code = m.group(1)
        if not npx:
            return m.group(0)  # keep the fence; markdown renders it as code
        try:
            with tempfile.TemporaryDirectory() as td:
                mmd = Path(td) / "d.mmd"; svg = Path(td) / "d.svg"
                mmd.write_text(code, encoding="utf-8")
                r = subprocess.run([npx, "-y", "@mermaid-js/mermaid-cli", "-i", str(mmd),
                                    "-o", str(svg), "-q"],
                                   capture_output=True, encoding="utf-8",
                                   errors="replace", timeout=180)
                if r.returncode == 0 and svg.exists():
                    return f'\n<div class="mermaid-diagram">{svg.read_text(encoding="utf-8")}</div>\n'
        except Exception as e:
            sys.stderr.write(f"mermaid render skipped: {e}\n")
        return m.group(0)

    return pattern.sub(repl, md)


def try_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Auto-PDF only if a known engine exists. Returns True on success."""
    if shutil.which("wkhtmltopdf"):
        try:
            subprocess.run(["wkhtmltopdf", str(html_path), str(pdf_path)],
                           capture_output=True, timeout=180)
            return pdf_path.exists()
        except Exception:
            return False
    if shutil.which("pandoc"):
        try:
            subprocess.run(["pandoc", str(html_path), "-o", str(pdf_path)],
                           capture_output=True, timeout=180)
            return pdf_path.exists()
        except Exception:
            return False
    return False


def main():
    ap = argparse.ArgumentParser(description="Markdown -> self-contained HTML (+ best-effort PDF).")
    ap.add_argument("input", help="path to a .md file")
    ap.add_argument("--out-dir", default=".", help="output directory (default: cwd)")
    ap.add_argument("--title", default=None, help="document title (default: from filename)")
    args = ap.parse_args()

    try:
        import markdown
    except ImportError:
        sys.exit("ERROR: needs the `markdown` lib -> run: python -m pip install markdown")

    src_path = Path(args.input)
    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    title = args.title or src_path.stem
    md_text = render_mermaid_blocks(src_path.read_text(encoding="utf-8"))

    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc", "sane_lists"])
    html = (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>")

    html_path = out_dir / f"{src_path.stem}.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"html: {html_path}")

    pdf_path = out_dir / f"{src_path.stem}.pdf"
    if try_pdf(html_path, pdf_path):
        print(f"pdf: {pdf_path}")
    else:
        print("pdf: no engine installed - open the HTML and Ctrl/Cmd+P -> Save as PDF")
        print("     (or install pandoc / wkhtmltopdf for automatic PDF).")


if __name__ == "__main__":
    main()
