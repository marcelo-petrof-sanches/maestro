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
| `brain/reference/` | reusable frameworks, methods, this file | "How do we do X / how is the brain organized?" |

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

## File naming
- Daily: `brain/daily/YYYY-MM-DD.md` · Clients: `brain/clients/<slug>.md`
- Projects: `brain/projects/<slug>.md` · Decisions: `D-NNN` inside the one log
- Use the `_template.md` in each folder as the shape for new files. Always real dates.
