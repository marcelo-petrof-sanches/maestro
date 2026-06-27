---
description: Quick task operations on my Notion to-do list (add / done / move / list)
---

Fast task operation on my Notion task database (config: `brain/tasks/notion-sync.md` —
if not yet confirmed, confirm it first, once). You make the Notion calls directly.

Interpret my input as one of:
- **add** → create the task in Notion with sensible properties (due date, priority,
  client tag if inferable) AND mirror it in `brain/tasks/backlog.md`
- **done** → mark it complete in Notion + check it off in backlog.md
- **move / reschedule** → update the due date in Notion
- **list / what's open** → show my open tasks, grouped by due date, most urgent first

Rules: be fast — execute and confirm in 1-2 lines, no commentary. If the task is
ambiguous, make the obvious call and say what you did. Keep client references
high-level in Notion (personal workspace — no confidential detail).

Operation: $ARGUMENTS
