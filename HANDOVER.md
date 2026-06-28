# Maestro — Handover & Setup Guide

Welcome. This is **Maestro**: a personal chief-of-staff agent system for consultants,
built on Claude Code. You talk to one orchestrator ("Maestro"); it coordinates a team
of specialist sub-agents and keeps a persistent **brain** of markdown files so context
survives across days.

This package is a **clean, empty copy** — all of the original owner's personal data,
daily logs, client/project files, development history, and credentials have been
removed. What's here is the *system* plus *blank templates* ready for you to fill in.

> 📖 Read [GUIDE.md](GUIDE.md) for the full handbook (architecture, every command and
> agent, the development loop, best practices). [README.md](README.md) is the quick
> start. This file is just how to go from this zip → your own live system.

---

## What's in the box

```
maestro/
├── CLAUDE.md            ← Maestro's operating manual (auto-loads every session)
├── GUIDE.md             ← full handbook
├── README.md            ← quick start
├── HANDOVER.md          ← this file
├── .claude/
│   ├── agents/          ← the 10 specialist sub-agents (ready to use)
│   └── commands/        ← slash commands: /setup /morning /eod /capture /task /schedule
│                          /client /newcase /retro /feedback /meeting-to-work-items
└── brain/               ← THE SECOND BRAIN (empty — you fill it)
    ├── profile/         ← working-preferences.md · bio.md · case-history.md  ← FILL FIRST
    ├── clients/         ← one file per client (+ _archive/) — _clients.md (mother) + _template-client.md
    ├── projects/        ← one file per workstream (+ _archive/) — _projects.md + _template-project.md
    ├── daily/           ← dated logs — _daily.md (mother) + _template-daily.md
    ├── tasks/           ← backlog.md (empty) · notion-sync.md (optional)
    ├── credentials/     ← empty; _credentials.md + _template-credentials.md (use a password manager!)
    └── development/     ← objectives.md (empty) + cdc/ project-feedback/ retros/ (templates)
```

Every `brain/` data file is blank or a template. Placeholders are marked `_(…)_`,
`{{OWNER}}`, `{{SEU_NOME_COMPLETO}}`, `{{SEU_EMAIL}}`.

**Not included** (intentionally): the owner's daily logs, real client/project files,
development feedback, credentials, and any case-specific tools/scripts (they contained
client data). The `tools/` reusable playbooks can be carried over separately once
stripped of client figures.

---

## Prerequisite #0 — get Claude Code access

Maestro runs on **Claude Code**. If you don't have it yet, request it on **IT Connect**:
**“Claude Enterprise (Chat + Code)”** →
https://bostonconsultinggroup.service-now.com/esc?id=sc_cat_item&sys_id=560ff6473b84cf505db5389aa4e45ab7&table=sc_cat_item&searchTerm=Claude%20Enterprise%20(Chat%20%20%20Code)

The plain claude.ai chat will not work — Maestro needs local files, sub-agents, and commands.

---

## Setup

> **The easy path:** put the folder somewhere local, open it in Claude Code, and just
> type **`/setup`**. Maestro detects it's a first run, diagnoses what's missing, and
> walks you through everything below — one step at a time. The manual steps are here for
> reference if you'd rather do it yourself.

1. **Put the folder somewhere local** (e.g. `~/maestro/`). Keep it off shared drives —
   the brain will hold confidential material.

2. **Open it in Claude Code.** Use the Claude Code desktop app, terminal, or IDE
   extension and open the folder that **directly contains `CLAUDE.md`**. Plain claude.ai
   chat or the regular Claude app will NOT work (no local files, no sub-agents, no
   commands). On open, `CLAUDE.md` loads automatically and Claude becomes Maestro — and
   it will offer to run `/setup`.

   ⚠️ **Folder nesting gotcha.** The zip creates a `maestro/` folder *inside* wherever you
   extract it. If you made your own folder and extracted into it, the files are nested one
   level deep (e.g. `…/your-folder/maestro/CLAUDE.md`) — open that inner `maestro/`, not the
   outer one. **Rule:** the folder you open must show `CLAUDE.md` and `.claude/` at its root.
   **Check you're right:** the first reply comes back *as Maestro* (not "I'm Claude Code, here
   to help with software development"), and typing `/` shows `/setup`, `/morning`, etc. in the
   autocomplete. If you only see generic commands or a dev-assistant intro, you opened the
   wrong level — go one folder deeper.

3. **Personalize the identity.** In `CLAUDE.md` (top) and across the system, replace the
   placeholders with your details:
   - `{{OWNER}}` → your name
   - `{{SEU_NOME_COMPLETO}}` → your full name
   - `{{SEU_EMAIL}}` → your work email
   Easiest: tell Maestro *"set me up — I'm <name>, <email>, <role> at <firm>"* and let
   it do the replacements. (CLAUDE.md is also where you'd adjust firm-specific framing
   if you're not at BCG — the connectors and register are BCG-flavored by default.)

4. **Fill your profile** (the highest-leverage step — Maestro reads it every session):
   - Start with `brain/profile/working-preferences.md` — level, hours, how you like
     outputs, what never to explain to you, protected time.
   - Then `bio.md` (the person) and `case-history.md` (your trajectory).
   - You don't have to edit by hand: brain-dump to Maestro and it structures the files.

5. **Connect integrations** (optional but recommended):
   - **Microsoft 365** (Outlook email + calendar) — powers the morning brief. Claude
     will prompt you to authenticate the first time `briefing-analyst` runs.
   - **Notion** — if you keep tasks there, fill `brain/tasks/notion-sync.md` on first
     use (Maestro will probe your databases). If not, ignore that file.
   - Firm connectors (slides, knowledge search, financial data) as available.

6. **Seed your development objectives** — run `/feedback` with your latest project
   feedback and last formal review. This populates `brain/development/objectives.md`,
   which drives the daily development nudge and the Friday retro.

7. **Onboard your current case** — `/newcase <path to the proposal deck>`. Maestro mines
   the deck, drafts the client + project files, and asks you only what the deck doesn't
   answer.

8. **Run `/morning`** the next workday. You're live.

---

## The daily rhythm (the habit that makes it work)

| When | You | Maestro |
|---|---|---|
| **Morning** | new chat → `/morning` | reads the brain, pulls calendar + email, gives ONE prioritized brief + a development nudge, opens today's log |
| **Through the day** | just talk | captures durable facts to the brain; delegates builds (slides, analysis) to specialists |
| **End of day** | `/eod` | finalizes the log, updates the backlog, recaps + previews tomorrow |
| **Friday** | `/retro` | reviews the week vs. your objectives; sets one intention |
| **On feedback** | `/feedback` | files it and updates your objectives |

**Golden rule:** one conversation per day; anything durable must reach the brain
(`/eod` and `/capture` do this). The chat is disposable — the brain is permanent.

---

## A few principles to keep it healthy

- **Capture ruthlessly.** The system is exactly as smart as the brain is current.
- **Fresh chat daily.** Long chats degrade; `/eod` then close, `/morning` in a new one.
- **Treat first runs as pilots.** If an agent does something wrong, say *"builder mode"*
  and fix the agent/command — the fix is permanent. (Agent/command changes need a
  session restart to register.)
- **Confidentiality.** Keep the folder local, follow your firm's data-handling policy,
  never paste brain content into non-sanctioned tools, and prefer a password manager
  over plaintext in `brain/credentials/`.

Make it yours: say **"builder mode"** anytime to add agents, commands, or structure.
See GUIDE.md §10.
