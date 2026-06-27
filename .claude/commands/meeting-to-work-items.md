---
description: Turn a meeting transcript or notes into structured decisions, action items, and follow-ups — and file them into the brain + Notion
---

Take a meeting transcript or notes and convert it into structured, actionable output.
Input may be a file path, a pasted transcript, or "the last meeting" (then pull it via
briefing-analyst). Transcripts are often messy/auto-generated — read for substance.

## 1. Extract (delegate the heavy parsing to briefing-analyst if the transcript is long)
Pull four things, each concrete:
- **Decisions** — what was decided (and by whom, if clear). These are durable.
- **Action items** — for each: a clear imperative task, an **owner**, a **due date** if
  stated/implied, and the **client/project** it belongs to. Mark the single first
  **next action** (the one unblocking task to start with).
- **Follow-ups / open questions** — things to confirm, info to request, people to chase.
- **Risks / watch-outs** — anything that threatens the plan or needs leadership attention.

## 2. File it (this is the point — don't just print a summary)
- **Action items owned by {{OWNER}}** → add to `brain/tasks/backlog.md` at the right
  priority (delegate to work-logger) AND create them in the Notion task DB per
  `brain/tasks/notion-sync.md` (you, Maestro, make the Notion calls). Items owned by
  others → list under "Waiting on others".
- **Decisions** → append to today's `brain/daily/` log and the relevant
  `brain/projects/<slug>.md`; if a decision log exists, add it there too.
- **Durable client facts / people / sensitivities** surfaced in the meeting → delegate
  to client-keeper.
- **Risks** → note in the daily log; flag the urgent ones back to {{OWNER}}.

## 3. Report back (tight)
A scannable digest: Decisions · Action items (owner · due · where filed) · Follow-ups ·
Risks. Lead with anything that needs {{OWNER}}'s attention now. Confidentiality: keep
Notion task text high-level (no confidential figures).

Meeting to process: $ARGUMENTS
