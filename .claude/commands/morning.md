---
description: Start the day — Maestro reads the brain, pulls email + calendar, and gives a prioritized briefing
---

Run the morning brief as defined in CLAUDE.md §2:

1. Read `brain/profile/working-preferences.md` (+ `bio.md`),
   `brain/tasks/backlog.md`, the 2 most recent `brain/daily/`
   logs, and any active client/project files referenced there.

1.5. **Project scanner** — for each `*-scanner-config.json` in `brain/projects/`, run
   TWO modes via Bash (parallel calls are fine):

   a) **Delta** (changes since yesterday):
      ```
      python tools/project_scanner.py brain/projects/<slug>-scanner-config.json
      ```
      Include output under "📁 Mudanças no projeto" if non-empty; skip if silent.

   b) **Meeting materials** (last 3 days):
      ```
      python tools/project_scanner.py brain/projects/<slug>-scanner-config.json --meetings
      ```
      Include output under "📋 Materiais disponíveis". Always show if there's a client
      meeting or CTM on today's calendar. If no meetings, include only if material was
      modified in the last 24h.

   c) **File verification** — after showing the delta, ask ONCE:
      "Reference files still the same? (deck: `<label>` · excel: `<label>`).
      If any was renamed or versioned, share the new path." Update `deep_scan_files`
      in the config if the answer indicates a change.

2. Delegate to **briefing-analyst** for today's calendar + important email (note if
   Microsoft 365 isn't authenticated and continue). In parallel, pull open tasks from
   {{OWNER}}'s Notion task database per `brain/tasks/notion-sync.md` (you make the
   Notion calls yourself — sub-agents can't). Notion sync is **first active item**:
   pull open tasks, compare with backlog.md, flag anything out of sync.
3. Delegate to **work-advisor** for a ranked recommendation, passing it the brain context.
4. Synthesize ONE crisp briefing: Today's shape · Top 3 priorities (with why) ·
   Watch-outs · Project file delta (if any) · Suggested first move.
5. Open/create today's daily log (`brain/daily/<today>.md`) and record the plan
   (delegate to work-logger or do it directly).

Additional context from {{OWNER}} (optional): $ARGUMENTS
