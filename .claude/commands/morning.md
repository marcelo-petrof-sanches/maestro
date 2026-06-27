---
description: Start the day — Maestro reads the brain, pulls email + calendar, and gives a prioritized briefing
---

Run the morning brief as defined in CLAUDE.md §2:

1. Read `brain/profile/working-preferences.md` (+ `bio.md`),
   `brain/tasks/backlog.md`, the 2 most recent `brain/daily/`
   logs, and any active client/project files referenced there.
2. Delegate to **briefing-analyst** for today's calendar + important email (note if
   Microsoft 365 isn't authenticated and continue). In parallel, pull open tasks from
   {{OWNER}}'s Notion task database per `brain/tasks/notion-sync.md` (you make the
   Notion calls yourself — sub-agents can't).
3. Delegate to **work-advisor** for a ranked recommendation, passing it the brain context.
4. Synthesize ONE crisp briefing: Today's shape · Top 3 priorities (with why) ·
   Watch-outs · Suggested first move.
5. Open/create today's daily log (`brain/daily/<today>.md`) and record the plan
   (delegate to work-logger or do it directly).

Additional context from {{OWNER}} (optional): $ARGUMENTS
