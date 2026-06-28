---
description: End of day — finalize today's log, update the backlog, and preview tomorrow
---

Run the end-of-day routine as defined in CLAUDE.md §2:

1. **Project file delta** — run the scanner for each active project config in `brain/projects/`:
   ```
   python tools/project_scanner.py brain/projects/<slug>-scanner-config.json
   ```
   Include any delta in the EOD log under "Done today" (slides/Excels modified =
   evidence of work done). Silent if no changes.
   **Check**: "Is the deck/Excel still the same filename? Was anything renamed or
   replaced today?" — if yes, update `deep_scan_files` in the config.

2. Delegate to **work-logger** to finalize today's daily log (Done today, Decisions
   made, Carried to tomorrow) and update `brain/tasks/backlog.md` (check off done,
   re-rank, archive). Update affected project status.
3. Reconcile the single-source homes: durable decisions made today → logged in
   `brain/decisions/decision-log.md`; any load-bearing number that changed → updated in
   its project's `## Current truth` block.
4. Reconcile tasks with {{OWNER}}'s Notion task database per `brain/tasks/notion-sync.md`:
   mark done items done, add anything that exists only on one side.
5. If {{OWNER}} shared client developments today, ensure **client-keeper** has captured them.
6. If anything today was clear evidence on a development objective (good or missed),
   note it in the daily log — the retro and CDC prep feed on these.
7. Give a 3-line recap and tomorrow's likely first priority.
8. **On Fridays:** offer the weekly retro (`/retro`) and a memory-hygiene pass
   (`/consolidate`) if they haven't happened this week.

What I did / want to capture for today: $ARGUMENTS
