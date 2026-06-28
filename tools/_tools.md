# 🔧 Tools — index

> Index for `tools/`. Standalone **Python/Excel utilities** that Maestro builds and runs
> (through the `analyst` agent for analysis, `slide-builder` for exhibits) to turn data
> into answers and deliverables. Distinct from [`brain/`](../brain/reference/brain-conventions.md)
> (the memory) and [`scripts/`](../scripts/_scripts.md) (system housekeeping).
>
> ↑ Up: [`CLAUDE.md`](../CLAUDE.md) · siblings: [`scripts/`](../scripts/_scripts.md) · [`brain/`](../brain/reference/brain-conventions.md)

## What lives here
- One-off and reusable analysis scripts for the active case(s): data pulls, classification
  engines, model builders, chart/exhibit generators (python-pptx, openpyxl, Tableau prep).
- Reusable **playbooks** (a documented method + its scripts) live in their own subfolder
  with a `README`; the durable write-up is catalogued in the reference wiki
  ([`_reference.md`](../brain/reference/_reference.md)).

## How Claude should use tools
- **Build & run them through the `analyst` agent** (analysis) or `slide-builder` (exhibits)
  — don't hand-roll heavy data work in the main thread.
- **Deliverables go to the project's SharePoint folder** (dated), never committed here.
  `tools/` holds the *scripts and local working copies*, not the outputs.
- **Never drive Office via COM automation** (breaks BCG add-ins) and **never re-save a live
  cube via openpyxl** (destroys pivots/charts) — deliver a separate file to copy from.
  _(These are durable working rules — see the [decision log](../brain/decisions/decision-log.md).)_
- Prefer a parameterised, reusable script over a throwaway; if a method will recur,
  promote it to a `README`-documented playbook and catalogue it in the reference wiki.

## ⚠️ Confidentiality
Tooling here routinely embeds **client data** (file names, values, categories). The whole
folder is **git-ignored** from the public template (`.gitignore`: `tools/*`), except the
generic, client-free `project_scanner.py` and this index. Never force-add a script that
carries client data.
