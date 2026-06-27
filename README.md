# Maestro — your BCG chief of staff + second brain

A personal agent system: one orchestrator (**Maestro**) you talk to, backed by a
persistent **brain** of files, coordinating a team of specialist sub-agents.

> 📖 **Full handbook:** see [GUIDE.md](GUIDE.md) — architecture, all commands and
> agents, the development loop, best practices, and how a new user can set it up.

## ⬇️ Get started (3 steps)

1. **Get Claude Code** — request it on BCG IT Connect: *"Claude Enterprise (Chat + Code)"*.
   The regular claude.ai chat / Claude app will NOT run Maestro.
2. **Download this folder** — click the green **`Code`** button above → **Download ZIP**
   (or `git clone`). Unzip it. You'll get a `maestro/` folder containing `CLAUDE.md`.
3. **Open it in Claude Code and type `/setup`** — open the folder that *directly contains*
   `CLAUDE.md` (File ▸ Open Folder), then type `/setup` and press Enter. It walks you
   through everything. 👉 Visual guide: **`Como-usar-o-Maestro.html`** in this folder.

> ✅ You opened the right folder if Maestro greets you (not a generic "I'm Claude Code for
> software development") and `/setup`, `/morning` appear when you type `/`. If not, open one
> folder deeper (the one with `CLAUDE.md` inside).

## How to use it

1. Open Claude Code in this folder (`maestro/`). Maestro's instructions load
   automatically from `CLAUDE.md`.
2. **Start your day:** type `/morning` (or just "good morning"). Maestro reads the
   brain, pulls your calendar + email, and gives a prioritized briefing.
3. **Through the day:** just talk to it.
   - "Met with the CFO at <client>, she's worried about the timeline" → it remembers.
   - "What should I do next?" → it consults the backlog + work-advisor.
   - "Build me a storyline for the SteerCo deck" → it delegates to slide-builder.
   - "Size this market in Python" → analyst.
   - Use `/capture <note>` to quick-file a task/fact/decision.
   - Use `/task <add/done/move/list ...>` for quick Notion to-do operations.
   - Use `/schedule <what, when, who>` to book meetings (one-click Outlook link).
   - Use `/client <name>` to get briefed on, or update, a client.
4. **End your day:** `/eod` — it logs what happened, updates the backlog, previews tomorrow.
5. **Friday:** `/retro` — review the week against your development objectives and set
   one intention for next week.
6. **When you get formal feedback** (project feedback, CDC): `/feedback <what they said>`
   — it files it and updates your development objectives.

## The team

| Agent | Role |
|---|---|
| **Maestro** (main) | Talks to you, coordinates, keeps the brain current |
| case-onboarder | New case kickoff: proposal deck → brain files (`/newcase`) |
| briefing-analyst | Email + calendar + transcript digest |
| client-keeper | Client knowledge base |
| work-logger | Daily logs, task backlog, project status |
| work-advisor | Prioritization & recommendations |
| slide-builder | Storylines + ThinkCell charts (Deckster) |
| analyst | Excel + Python analysis |
| support-coach | Reflection & psychological support |
| challenger | Pressure-tests your logic/message before it goes to a partner/MDP or client |
| artifact-reviewer | Checks a finished deliverable against its brief before a client send |

## The brain (`brain/`)
- `profile/` — **fill this in first.** Who you are, in three parts: `bio.md` (the
  person — life before/beyond BCG), `case-history.md` (your BCG case trajectory,
  skills, spikes, gaps), `working-preferences.md` (role + how you like to work).
- `clients/` — one file per client. `projects/` — your workstreams.
- `daily/` — dated logs. `tasks/backlog.md` — the master task list.
- `development/` — your growth engine:
  - `objectives.md` — live dev objectives; Maestro reads it every session and nudges you daily
  - `project-feedback/` — granular case-team feedback, one file per project
  - `cdc/` — career development committee outcomes, one file per ~6-month cycle
    (career-level synthesis + trajectory; each CDC resets `objectives.md`)
  - `retros/` — Friday weekly retros
  CDC prep becomes compiling the evidence you've already logged.

The files ARE the memory. Maestro and every specialist read and write them, so context
survives across days and sessions.

## First-time setup
1. Fill in `brain/profile/` — start with `working-preferences.md` (level, office,
   working style, deep-work hours), then `bio.md` and `case-history.md`.
2. Create your first client file: `/client <name>` and tell Maestro about them.
3. Connect Microsoft 365 (Outlook) so the morning brief can read email + calendar —
   Claude will prompt you to authenticate the first time briefing-analyst runs.
4. Run `/morning`.

## Notes
- **Confidentiality:** the brain holds client-confidential data. Keep this folder local
  and follow BCG data-handling policy.
- **Scheduling:** the morning brief can be set to run automatically on a schedule — ask
  Maestro to "set up a scheduled morning brief" once you're happy with how it works.
- **Versioning (optional):** `git init` here to track how the brain evolves and to back
  it up.
