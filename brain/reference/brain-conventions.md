# Brain Conventions — how the second brain is organized

> The constitution of the brain. CLAUDE.md is a router that points here; this file holds
> the detail of *where things live* and *the principles for keeping them findable*. Read
> when you're unsure where something belongs or how to keep the brain healthy.

## The retrieval-first principle (the one that matters most)
**File it where you'll look for it — work backwards from the question.**
Before writing anything down, ask: *"When I (or an agent) need this later, what will I
search for, and will this be there?"* Store the information the way it will be retrieved,
not the way it arrived.
- A fact that answers "what's the latest X number?" → the project's **Current truth** block.
- A fact that answers "why did we decide Y?" → the **decision log**.
- A fact that answers "what is this person/client like?" → the **client file**.
- A fact that answers "what did I do on day Z?" → the **daily log**.
- **The test:** after filing, could the agent find it again from a cold start, searching
  the obvious term? If not, it's filed wrong — add it where the question will be asked.

## Where things live (the map)
| Folder | Holds | The question it answers |
|---|---|---|
| `brain/profile/` | working-preferences, bio, case-history | "Who is {{OWNER}} / how does he work?" |
| `brain/development/` | objectives, retros, project-feedback, cdc | "How is he growing; what's the feedback?" |
| `brain/clients/` | one file per client (people, org, sensitivities) | "What do we know about client X?" |
| `brain/projects/` | one file per workstream + **Current truth** block | "Where does workstream X stand?" |
| `brain/decisions/decision-log.md` | numbered, dated decisions (D-NNN) | "What did we decide and why?" |
| `brain/daily/` | one log per day | "What happened on / around day Z?" |
| `brain/tasks/` | backlog + notion-sync | "What do I need to do?" |
| `brain/reference/` | reusable frameworks, methods, playbooks (start at [`_reference.md`](_reference.md)) | "How do we do X / how is the brain organized?" |

## Folder mothers (MOCs) — the graph backbone
Every folder has a **mother file** `_<folder>.md` that describes it and lists its members,
so each folder forms a connected cluster and the whole brain hangs off this file. New files
link their mother (the templates do this automatically). Mothers:
- [📅 daily](../daily/_daily.md) · [🏢 clients](../clients/_clients.md) · [📊 projects](../projects/_projects.md) · [⚖️ decisions](../decisions/_decisions.md)
- [🌱 development](../development/_development.md) ([🎯 cdc](../development/cdc/_cdc.md) · [🔁 retros](../development/retros/_retros.md) · [📝 feedback](../development/project-feedback/_feedback.md))
- [✅ tasks](../tasks/_tasks.md) · [👤 profile](../profile/_profile.md) · [📚 reference](_reference.md) · [🔑 credentials](../credentials/_credentials.md)

## Connectivity — no orphans (a brain is a graph)
**Every file connects to at least one other file.** That's what makes this a brain and
not a folder of notes — you can always navigate from any node to the rest. When you
create or close a file, connect it.

The one guardrail that keeps connectivity from becoming noise: **connect at the file
level, not the line level.** Each file declares its neighbours once (a `Related:` line or
a links section) — you do *not* turn every mention into a link. Fewer stable links beat
many stale ones (links you won't maintain rot).

How each file type connects:
- **Client ↔ project** (both directions): each client lists/links its workstreams; each
  project links its client.
- **Decision ↔ project**: every decision-log entry names its project; the project points
  back to the log. (Built into `/decision-log`.)
- **Project → reference/playbooks**: link the reusable methods it uses (Key artifacts +
  the [reference wiki](_reference.md)).
- **Daily log → what it touched**: a `Related:` line naming the project(s)/client(s) of
  the day (set at `/eod`). That single line makes every daily a connected node — no need
  to link every entry. Still **promote** durable facts to their home (Current truth /
  decision log / client file); a durable file may cite a key daily for *provenance*.
- **Profile / development**: profile files reference each other (working-preferences ↔ bio
  ↔ case-history); objectives ↔ retros ↔ feedback. Keep those links live.
- **Reference / tools**: every reusable asset sits in [`_reference.md`](_reference.md) and carries
  a `## Related` footer.

`/consolidate` runs an **orphan check** — any file with no link in or out gets flagged.

## Single-source-of-truth (no drift)
- **Load-bearing numbers live in exactly one place:** the project's `## Current truth`
  table, each with an as-of date and source. Everywhere else *links* to it; never restate
  the figure. If the same number appears twice and disagrees, reconcile to Current truth.
- **Decisions live in the decision log**, numbered and append-only. Project files may
  summarize, but the log is canonical. See its header for the **anti-anchor rule**.

## Active vs. archived
- Every client/project file carries a `Status` (🟢 Active / ⚪ Closed). Only **Active**
  files surface in the morning brief and recommendations.
- When work closes: set Status to Closed, move the file to the folder's `_archive/`
  subfolder. Archived files stay searchable but out of the daily flow.

## Freshness & hygiene
- Every durable fact carries an **as-of date** so staleness is visible.
- Re-confirm facts older than ~60 days; archive projects past their last milestone.
- `/consolidate` runs this hygiene pass (dedup, staleness, archive) periodically.

## File naming — unique names, type-readable
**No two files share a name.** The folder gives the type; the filename stays unique so
nodes never collide in the graph/search.
- **Members:** Daily `brain/daily/YYYY-MM-DD.md` · Clients `brain/clients/<slug>.md` ·
  Projects `brain/projects/<slug>.md` · Retros `…/retros/YYYY-MM-DD-retro.md` (the `-retro`
  keeps them distinct from dailies) · CDC `…/cdc/YYYY-MM-DD-cdc.md` · Feedback `…/project-feedback/YYYY-MM-DD-<slug>.md`.
- **Mother (MOC):** `_<folder>.md` (e.g. `_daily.md`) — one per folder, sorts to top.
- **Template:** `_template-<type>.md` (e.g. `_template-client.md`) — the shape for new files.
- Decisions: `D-NNN` inside the one `decision-log.md`. Always real dates.

## Relacionados
- [📚 Reference Wiki / mother](_reference.md) — reusable methods/playbooks.
