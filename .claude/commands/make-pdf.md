---
description: Turn a Markdown file (memo, one-pager, self-review pack) into a publication-quality, self-contained HTML you can print to PDF. Use for "make a PDF/document of this", "turn this memo into a shareable doc". NOT for slide decks (use slide-builder).
argument-hint: [path to a .md file, or the content to write first]
---

Turn a Markdown document into a clean, **self-contained HTML** (offline, no external deps)
that prints to PDF from the browser. For **non-deck documents** — memos, one-pagers,
leave-behinds, the CDC self-review pack, meeting notes. (Slides = slide-builder/Deckster.)

## Steps
1. **Get the source:** a path to a `.md`, or write the content to a `.md` first. For client
   work, save it in the project's SharePoint folder (dated).
2. **Run:** `python tools/make_pdf.py <file.md> --out-dir <dir> --title "<Title>"`.
3. **Deliver:** show the `.html` path. If a PDF engine is installed it also emits `.pdf`;
   otherwise tell {{OWNER}} to open the HTML and **Ctrl/Cmd+P → Save as PDF** (clean, reliable).
4. **Diagrams:** ` ```mermaid ` fenced blocks render inline as SVG automatically — pair with
   `/diagram` to draft the figure, then embed it.

Notes: needs the `markdown` lib (`pip install markdown`). Diagram rendering + auto-PDF are
best-effort and never hard-fail. Everything runs **local** — safe for confidential material.

Source (path or content): $ARGUMENTS
