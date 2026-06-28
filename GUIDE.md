# The Maestro Guide

*A personal chief-of-staff agent system for management consultants, built on Claude Code.*

---

## 1. What is Maestro?

Maestro is a **personal agent system** you talk to every day. It combines three ideas:

1. **An orchestrator ("Maestro")** — a chief of staff persona you interact with. You
   never talk to the specialists directly; Maestro coordinates them.
2. **A second brain** — a folder of plain markdown files that stores everything
   durable: who you are, your clients, your projects, your tasks, what happened each
   day, your professional development. **Files are the memory.** Conversations are
   disposable; the brain is permanent.
3. **A team of specialist sub-agents** — each with one job (reading your email,
   keeping client knowledge, building slides, running analyses...). Maestro delegates
   to them and synthesizes the results.

The result: every morning you open a *fresh* conversation, and Maestro already knows
your clients, your backlog, what you did yesterday, and what you're trying to improve
— because it reads the brain, not the chat history.

### Requirements
- **Claude Code** (desktop app or terminal) — the normal claude.ai chat cannot run
  Maestro (no local file access, no sub-agents, no commands).
- Optional but recommended: the **Microsoft 365 connector** (email + calendar briefs)
  and BCG connectors (Deckster for charts, Knowledge Search, CapIQ, etc.).

---

## 2. Architecture

```
maestro/                      ← open Claude Code HERE (this folder = Maestro's home)
├── CLAUDE.md                 ← Maestro's operating manual (auto-loads every session)
├── GUIDE.md                  ← this guide
├── README.md                 ← quick start
├── .claude/
│   ├── agents/               ← the 10 specialists (see §5)
│   └── commands/             ← the slash commands (see §4)
└── brain/                    ← THE SECOND BRAIN (see §6)
    ├── profile/              ← who you are (bio, case history, working preferences)
    ├── clients/              ← one file per client (+ _archive/)
    ├── projects/             ← one file per workstream (+ _archive/)
    ├── daily/                ← one log per day (YYYY-MM-DD.md)
    ├── tasks/backlog.md      ← the master task list (P0–P3)
    └── development/          ← feedback, objectives, retros (see §7)
```

**How a session works:** when you open Claude Code in this folder, `CLAUDE.md` loads
automatically and turns Claude into Maestro. Before answering anything substantive,
Maestro reads the brain (profile, objectives, backlog, recent daily logs). When you
ask for something specialized, it spawns the right sub-agent, gives it the relevant
brain context, and writes durable results back to the brain.

**Key design rule:** sub-agents cannot talk to you directly — only Maestro can. So
interactive workflows are always *command + agent* pairs: the agent does the legwork,
Maestro handles the conversation.

---

## 3. The daily rhythm

This is the core habit loop. The system's value compounds with consistency.

| When | What you do | What happens |
|---|---|---|
| **Morning** | New chat → `/morning` | Maestro reads the brain, pulls your calendar + email (via briefing-analyst), gets a prioritization (work-advisor), and gives ONE briefing: today's shape, top 3 priorities, watch-outs, a development nudge, and your first move. Opens today's daily log. |
| **Through the day** | Just talk to it | Tell it what happened ("met the CFO, she's worried about timeline") → it captures to the brain. Ask for help ("draft the storyline", "run this analysis") → it delegates. Quick saves: `/capture <note>`. |
| **End of day** | `/eod` | Finalizes today's log (done / decisions / carried over), updates the backlog, flags development evidence, gives a 3-line recap + tomorrow's first priority. |
| **Friday** | `/retro` | Weekly development retro: the week vs. your objectives, with receipts from the daily logs. Lands ONE intention for next week. |
| **Next morning** | Close the chat, open a new one | Nothing is lost — `/eod` flushed everything to files. |

**Golden rule:** one conversation per day. Anything durable must reach the brain
(`/eod` and `/capture` do this) — whatever stays only in the chat dies with the chat.

---

## 4. Commands reference

| Command | What it does | When to use |
|---|---|---|
| `/morning [context]` | Full morning brief: brain + calendar + email + prioritization + development nudge + opens daily log | Start of every workday |
| `/eod [what I did]` | Closes the day: finalizes log, updates backlog, recap + tomorrow preview | End of every workday |
| `/capture <note>` | Quick-files a task / client fact / decision to the right brain file, 1-line confirmation | Anytime something durable happens |
| `/task <op>` | Fast Notion to-do operations: add / done / reschedule / list (syncs backlog.md too) | All-day task management |
| `/schedule <what/when/who>` | Checks conflicts + participant availability, then gives a one-click prefilled Outlook event link (M365 calendar is read-only, so final click is yours) | Booking meetings fast |
| `/client <name + ask>` | Briefs you on a client from its file, OR updates the file with new info | Before a meeting; after learning something |
| `/newcase <proposal path>` | Onboards a new case: reads the proposal deck (PDF/PPTX), drafts client + project files, asks you only what the deck doesn't answer, updates case history + backlog | Every case start |
| `/retro [thoughts]` | Friday weekly retro vs. development objectives; writes to `development/retros/` | Fridays |
| `/feedback <what they said>` | Files formal feedback (project feedback or CDC — it routes by type) and updates your development objectives | Whenever you receive formal feedback |
| `/meeting-to-work-items <transcript/notes>` | Extracts decisions + action items (owner/due) + follow-ups from a meeting and files them into the backlog/Notion + logs | After any meeting with a transcript or notes |
| `/setup [context]` | Guided first-run onboarding: diagnoses what's missing and walks a new user through identity, profile, integrations, objectives, and first case | First time you open the system |

**No command needed** for normal use — commands are shortcuts for the rituals. Plain
conversation ("what should I do next?", "help me prep the SteerCo") works anytime.

**Builder Mode** (not a command — just say it): "builder mode" or "let's improve the
maestro" switches Maestro from chief of staff to system engineer so you can modify
agents, commands, and structure. New/changed agents and commands take effect after a
session restart.

---

## 5. The agent team

You never invoke these directly — Maestro delegates based on what you ask.

| Agent | Job | Typical trigger |
|---|---|---|
| **briefing-analyst** | Reads Outlook email + calendar + Teams/Zoom transcripts; returns a tight digest (schedule, emails needing you, deadlines, notables). Read-only — never sends or replies. | `/morning`; "what's in my inbox?"; "summarize that meeting" |
| **case-onboarder** | Mines a proposal deck (PDF/PPTX) completely; drafts client + project files with `❓ TBC` markers; returns a ≤6-question gap list | `/newcase` |
| **client-keeper** | Maintains `brain/clients/` — people (with relationship notes), politics, sensitivities, decision history. Reconciles rather than overwrites. | `/client`; any durable client fact you mention |
| **work-logger** | Maintains daily logs, the task backlog, and project status files | `/eod`; `/capture`; progress updates |
| **work-advisor** | Prioritization: ranks your options by deadline pressure, leverage, cost of delay, energy fit, visibility — and your development objectives as tie-breaker. Opinionated: ranked list + first move + what NOT to do. | `/morning`; "what should I do first?" |
| **slide-builder** | BCG-style storylines (action titles, pyramid principle), page-by-page content, ThinkCell charts/tables via Deckster | "build me a storyline"; "turn this into slides" |
| **analyst** | Quantitative work: Python (pandas, optimization), Excel models (clean inputs→calcs→outputs structure), external data pulls (CapIQ, BLS, World Bank...). Always ends with the "so what". | "size this market"; "build the model"; "analyze this data" |
| **support-coach** | The human side: decompressing, reframing setbacks, prepping hard conversations, sustainable pace. Reads your bio + reflections; warmer register, no deliverable pressure. Not a substitute for professional care. | Stress, overload, feedback anxiety, "rough day" |
| **challenger** | Read-only pressure-test of a recommendation/analysis/slide message in 3 lenses (logic · risk · audience) before it goes up. Returns verdict + what breaks + the hard question + fastest fix. | "challenge this"; "is this ready for the partner/client?"; before any send up the chain |
| **artifact-reviewer** | Stateless, read-only conformity gate: does the finished deliverable do what the brief asked? Ask-by-ask checklist + gaps + scope creep. | Before any client/partner deliverable ships |

---

## 6. The brain

Every folder has a `_template-<type>.md` (e.g. `_template-client.md`) showing the expected
shape, and a mother file `_<folder>.md` (a map/index of that folder). Maestro creates files
as things come up — you never pre-create anything.

| Path | Contains | Maintained by |
|---|---|---|
| `profile/bio.md` | Who you are as a person — background, life outside work, what drives you, long-term ambition. Read every session; anchors support-coach. | You (via conversation) |
| `profile/case-history.md` | Your case trajectory: one entry per case (role, team, skills) + a skills/exposure summary (spikes, gaps, partner relationships). Feeds CDC prep and staffing thinking. | case-onboarder + you |
| `profile/working-preferences.md` | The operational manual: level, working style, peak hours, output standards, communication preferences, protected time. Read every session. | You |
| `clients/<slug>.md` | Everything about a client: people table with relationship notes, politics, sensitivities, decision history. Status 🟢 Active / ⚪ Closed; closed ones move to `_archive/`. | client-keeper |
| `projects/<slug>.md` | A workstream you own: objective, status, workplan, decisions, risks. Same active/archive convention. | work-logger |
| `daily/YYYY-MM-DD.md` | The day's narrative: morning plan, log, done, decisions, carried over, reflections | Maestro + work-logger |
| `tasks/backlog.md` | Master task list: P0 (today) → P3 (someday), waiting-on, done | work-logger |
| `development/` | Your growth engine — see §7 | various |

**Why plain markdown?** Portable, diffable, readable without any tool, easy to back up
(e.g. `git init`), and any agent can read/write it. No lock-in.

---

## 7. The development loop

Designed around the consulting feedback cycle: granular **project feedback** per case,
and a **career development committee (CDC)** every ~6 months.

```
daily nudge ──► friday /retro ──► evidence accumulates ──► CDC prep = compilation
     ▲                                                            │
     └────────── objectives.md ◄── /feedback (project or CDC) ◄───┘
```

- `development/objectives.md` — your 2–4 live development objectives, each with
  practice cues and an **evidence log**. Maestro reads it every session and gives one
  concrete nudge per day, tied to a real calendar moment.
- `development/project-feedback/` — one file per case: strengths, development areas
  (near-verbatim), your read, actions agreed. **Folds into** objectives.
- `development/cdc/` — one file per committee cycle: overall assessment, trajectory,
  cross-project themes, forward priorities. **A CDC resets** objectives.
- `development/retros/` — Friday retros: where each objective showed up or was missed
  this week (with receipts from daily logs), cross-week patterns, one intention.

The payoff: CDC prep stops being archaeology — Maestro compiles months of logged
evidence, retros, and feedback files into a self-review pack.

---

## 8. Best practices

1. **Fresh chat daily.** Long chats degrade (context fills up and gets summarized);
   the brain doesn't. `/eod` then close; `/morning` in a new chat.
2. **Capture ruthlessly.** The system is exactly as smart as the brain is current.
   When in doubt, `/capture` it.
3. **Parallel conversations are fine — with roles.** You can run several Maestro chats
   at once: one "day chat" (owns `/morning`, `/eod`, the daily log and backlog) plus
   "workroom chats" for heavy deliverables (slides, models). Sessions share files but
   not context — so let only the day chat write the log/backlog, and `/capture`
   workroom outcomes when done. Avoid two chats editing the same file simultaneously.
4. **Onboard every case via `/newcase`.** The proposal deck is the richest source of
   truth at case start — mine it once, properly.
5. **Don't skip Fridays.** The retro is what turns daily logs into career evidence.
6. **Restart after building.** Any change to agents or commands needs a session
   restart to register. (Brain edits apply from the next session start.)
7. **Trust but verify early.** Treat the first run of each agent as a pilot; correct
   it (Builder Mode) and the fix is permanent.
8. **Confidentiality.** The brain holds client-confidential material. Keep the folder
   local, follow your firm's data-handling policy, and never paste brain content into
   non-sanctioned tools.

---

## 9. Setting it up as a new user

To adopt this system from someone else's copy:

1. **Copy the `maestro/` folder** to your machine.
2. **Empty the brain** — delete the contents of `brain/clients/`, `brain/projects/`,
   `brain/daily/`, `brain/development/project-feedback/`, `brain/development/cdc/`,
   `brain/development/retros/` (keep every `_template-*.md`, every `_<folder>.md` mother, and the folder structure), and
   reset `brain/tasks/backlog.md`, `brain/development/objectives.md`, and the three
   `brain/profile/` files to their headers. **Never reuse someone else's brain — it's
   confidential.**
3. **Personalize `CLAUDE.md`** — replace the owner's name and email at the top.
4. **Fill your profile** — open Claude Code in the folder and brain-dump: "update my
   working preferences: I'm a..., I work best...", then bio, then case history.
   Maestro structures it into the files.
5. **Connect Microsoft 365** when briefing-analyst first asks to authenticate.
6. **Seed your development objectives** — `/feedback` with your latest project
   feedback and last CDC outcome.
7. **Onboard your current case** — `/newcase <path to proposal>`.
8. Run `/morning` the next workday. You're live.

---

## 10. Extending the system

Say **"builder mode"** in any Maestro session, then describe what you want. Design
principles Maestro follows when building:

- **Files are the memory** — new capabilities read/write the brain, never rely on
  chat state.
- **One agent, one job** — with a sharp `description` field (that's how Maestro routes
  delegation).
- **Interactive flows = command + agent** — agents can't ask you questions; Maestro does.
- **Update the team table** in CLAUDE.md §3 and the README when adding agents.

Ideas that fit naturally: a scheduled automatic morning brief, a knowledge-search
agent for internal BCG content, an expert-interview prep agent, a weekly status-email
drafter, mobile access via a synced private git repo.
