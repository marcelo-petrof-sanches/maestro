# Reference Wiki — index

> The navigable home of **reusable knowledge**: methods, frameworks, and tool playbooks
> that outlive any single case. Start here when the question is *"how do we do X / do we
> already have a way to do this?"* — before reinventing or searching externally.
>
> **How it links:** plain relative markdown links (clickable in Claude Code, resolvable
> by agents, and it renders as a navigable vault if you open `brain/` in Obsidian).
> Every reusable asset gets (a) one line here and (b) a `## Related` footer linking back.
>
> This ships **empty** — it fills itself as you build reusable methods. The sections below
> show the shape; add a line under the right one whenever you create something worth reusing.

---

## 🧠 Methods & frameworks (reusable analytical approaches)
_None yet. Example of the format you'll add:_
- **[Market sizing — top-down/bottom-up](market-sizing.md)** — the approach + a worked
  template. *When:* any sizing question.

## 🛠️ Tool playbooks (`tools/` — runnable methods)
- **[Project scanner](../../tools/project_scanner.py)** — detects file changes in your
  active projects at `/morning` and `/eod` (delta + recent meeting materials). Configure
  per project from [`_scanner-config-template.json`](../projects/_scanner-config-template.json).

## ⚙️ System infrastructure (Maestro)
- **[Brain conventions](brain-conventions.md)** — the "constitution" of the brain: folder
  map, single-source-of-truth, retrieval-first, active/archive, hygiene cadence.
  *Read it when you're unsure where something belongs.*

---

## How to add to the wiki
1. Built a method / framework / playbook you'll reuse? Give it a file
   (`brain/reference/<slug>.md`) or a `README.md` in the tool's folder.
2. Add **one line** under the right section above (with the *when to use it*).
3. Add a `## Related` footer in the new file linking back to this index and to neighbouring
   assets. Link liberally — that's what makes the wiki navigable.
