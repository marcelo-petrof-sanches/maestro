# Notion Task Sync — Configuration

> Maestro reads this to know how to sync tasks with your personal Notion to-do list
> (connected via the claude.ai Notion connector — tools `mcp__claude_ai_Notion__*`).
> **OPTIONAL** — only relevant if you keep your tasks in Notion. If you don't, ignore
> this file (the local `backlog.md` is enough) and tell Maestro so.
>
> Status: ⚠️ **NEEDS FIRST-USE CONFIRMATION** — fill in the configuration below the
> first time you use it, then flip this to ✅ CONFIRMED.

## To confirm with Maestro on first use (then update this file)
1. **Which Notion database is your live task list?** (have Maestro probe via
   `notion-search` / `notion-fetch` and list candidates here with their IDs)
2. **Source of truth:** recommended = **Notion is master for tasks** (you maintain it
   there + mobile access); `backlog.md` stays as Maestro's local working notes (ranking
   rationale, waiting-on, done archive) synced FROM Notion.
3. Fetch the database schema (`notion-fetch` on the database ID) and record the
   **data source ID** + **property names + allowed values** here.

## Sync behavior (once confirmed)
- **/morning** → pull open tasks from the Notion database; merge with backlog.md; prioritize across both.
- **/capture or any new task** → create it in Notion (right properties) AND reflect in backlog.md.
- **/eod** → mark completed tasks done in Notion; reconcile both directions; note one-sided items.
- **Conflicts** → Notion wins (master); note the override in the daily log.

## Confirmed configuration (fill on first use)
- **Database:** _(name + ID)_
- **Data source ID:** _(…)_
- **Property mapping (key → values):**
  - **Title:** _(property key)_
  - **Priority / Status / Deadline / …** _(map each property + its allowed values)_
- ⚠️ Multi-select values are passed as a JSON-array *string*, e.g. `"[\"Analysis\"]"`.

## Notes
- Sub-agents have restricted toolsets without MCP access — **Maestro itself makes the
  Notion calls** in the main thread, then delegates local file updates.
- ⚠️ Confidentiality: this is a PERSONAL Notion workspace. Keep client references in
  tasks high-level (client name + task is fine; no confidential figures, no documents).
  Sensitive detail belongs in the local brain only.
