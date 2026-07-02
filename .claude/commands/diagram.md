---
description: Turn an English description into a diagram — process flow, org chart, issue tree, 2x2, sequence, timeline. Renders to SVG (offline) + editable source. Use for "make a diagram/flowchart of...", "draw this", "diagram the process". For polished client-DECK exhibits, use slide-builder/Deckster instead.
argument-hint: [what to diagram, in words]
---

Turn {{OWNER}}'s English into a **thinking / draft diagram** — for memos, internal alignment,
issue trees, quick process maps. **Not** a polished client-deck exhibit (those go via
slide-builder + Deckster/ThinkCell). You write the Mermaid; `tools/diagram.py` renders it.

## Steps
1. **Pick the right Mermaid type** for the intent: `flowchart` (process), `sequenceDiagram`
   (interactions), `mindmap` (issue/hypothesis tree), `quadrantChart` (2x2), `gantt`
   (timeline/roadmap), `erDiagram` (data).
2. **Write clean Mermaid source** — tight labels, client lexicon, left-to-right where it reads better.
3. **Render:** `python tools/diagram.py <file.mmd> --out-dir <dir> --name <name>` (or pipe the
   source via `-`). For case work, save the `.mmd` in the project's SharePoint folder (dated).
4. **Show {{OWNER}}** the rendered SVG path + the Mermaid source, and note it's **editable** by
   pasting the `.mmd` into excalidraw.com (Mermaid import) or mermaid.live. Offer tweaks.

Notes: rendering uses mermaid-cli (Node); the **first** run may fetch packages (needs network —
can be blocked on a locked BCG machine). The tool **never hard-fails** — it always keeps the
`.mmd` source. Rendering is **local**, so confidential content is fine.

What to diagram: $ARGUMENTS
