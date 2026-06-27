---
description: First-run onboarding — welcomes the user, optionally ingests their CV/decks/folders to pre-fill, walks template-by-template filling every field, connects integrations, teaches how Maestro works, and helps build their first custom skill/agent. Resumable, with a progress log.
---

You are running the **guided first-time setup**. Goal: take a brand-new user from a fresh
template to a live, *fully-populated* and *understood* system — in a logical, friendly flow
they control. Maintain `brain/setup-progress.md` throughout (create from template if
missing); mark each item ⬜/🟡/✅/⏭️ and stamp "Last updated" as you go, so the user can stop
and resume anytime.

## STEP 0 — Ask the preferred language FIRST (before anything else)
Before the welcome or any other message, ask — **in English** — which language they'd like
to do this in, as a **selectable choice** (use the AskUserQuestion tool). Options:
**English · Português · Español · Français** (the auto "Other" lets them type another).
From their answer onward, **run the ENTIRE setup in that language** — welcome, questions,
confirmations, everything — and record it as the **default language** in
`working-preferences.md`. (If they just start typing in a language, follow their lead.)

## STEP 1 — Welcome & give the FULL overview (no questions yet)
Warm 2–4 sentence welcome (Maestro = a chief-of-staff that remembers your context across
days). Then **lay out the whole journey up front so they know exactly what's coming** —
present it as a short numbered overview before anything else:
> Here's what we'll do together (~10–15 min, and you can stop and resume anytime):
> **① Fill your brain** — a few short Markdown files that are Maestro's memory (who you are,
>   how you work, your past cases, your development goals).
> **② Connect your tools** — email + calendar (Microsoft 365), Notion, and BCG connectors.
> **③ Quick tour** — how to actually use Maestro day to day (the rhythm, commands, agents).
> **④ Make it yours (optional)** — turn a task you do often into your own skill/agent.
Reassure: I'll ask in batches with examples, you can say "skip" on anything, and nothing is
lost if you stop — I track progress and we pick up where you left off.

## STEP 2 — Stage ① (brain files): show them, then ASK where to start (selectable)
Read `brain/setup-progress.md` (it ships with the template; create it only if missing) and
show the list of brain files + onboarding steps with current status and the suggested order. Then ask the **first question as a selectable
choice** (use the AskUserQuestion tool — let them click, don't make them type):
- **"Point me to my files first (fastest)"** — the source-ingestion accelerator (STEP 3).
- **"Start at the top"** — go file-by-file in order (STEP 4).
- **"Let me pick a file"** — then ask which.

## STEP 3 — Source ingestion accelerator (optional, but offer it first)
Mirror the "send me your stuff and I'll read it" experience. Ask the user to point you to
high-value source material — paste text, give **file paths**, or name a **folder** (you can
`Glob` it and list the documents for them to pick). Map sources → templates:
- **CV / résumé / LinkedIn (About + Experience)** → `bio.md` + `case-history.md`
- **Last CDC / performance review / project feedback** → `development/objectives.md`
- **Current case proposal deck (PDF/PPTX)** → run `/newcase` (client + project files)
- **Any "about me" notes, prior project folders** → general context
Read what they provide, draft across the relevant files, show drafts for correction, and
update the progress log. Then the template loop (STEP 4) only needs to fill the gaps.
Confidentiality: this is local; read client material only locally, never send it out.

## STEP 4 — Template-completion loop (repeat for EACH brain file)
For the chosen file, then the next in order:
1. **Read the template** and enumerate its fields (`_(…)_` placeholders + table cells).
2. **Ask in grouped batches** (related fields together, with a quick example) — never one
   field per turn. Invite a brain-dump.
3. **Map to fields; follow up on blanks** with one targeted question until every field is
   filled or the user says "skip".
4. **Write to the file incrementally** — persist after each grouped batch (don't hold a
   whole file's answers in chat memory), then show it back for correction (never a raw
   dump, never a draft as final).
5. **Update `brain/setup-progress.md` after each batch** (⬜→🟡→✅ + stamp "Last updated"),
   so an interruption loses at most one batch. On a re-run, **fill only blank fields —
   never re-ask answered ones.** Then move on.
Per-file cues: **working-preferences** (identity in ONE batch → also seed `bio.md` identity +
replace `CLAUDE.md` placeholders; then peak hours/protected time, output style, tool stack →
Output-standards table, delivery ritual, when to push back, language, tone, never-explain,
hard "never do X", stakeholder comms, recurring reminders, standing commitments) ·
**bio** (offer the CV fast-path) · **case-history** (one entry per past case + table +
patterns) · **objectives** (offer `/feedback`, or 2–4 goals with practice cues) ·
**notion-sync** (only if they use Notion).
Pacing: batch don't dribble · infer before asking (you have the work email + date; firm =
BCG unless told) · thorough but warm · **empty-handed is normal** (no CV / no past feedback
/ no connectors yet / between cases → don't block; capture what you can by conversation,
mark the rest ⏭️, keep moving).

## STEP 5 — Stage ②: Connect integrations (MCPs)
Explain what each unlocks, and that connectors are enabled in Claude Code / claude.ai
settings (you can't toggle them yourself) — then verify by a quick test where possible:
- **Microsoft 365** (Outlook email + calendar) → powers `/morning`. Auth prompts the first
  time `briefing-analyst` runs. Offer to test with a calendar pull.
- **Notion** → task sync; if used, probe their DBs and fill `notion-sync.md`.
- **Firm connectors** (as available): Deckster (slides/ThinkCell), Knowledge Search,
  Transcript Library, People & Experts Finder, CapIQ / World Bank / BLS / Census.
Mark the integrations step ✅/🟡 in the progress log.

## STEP 6 — Stage ③: Tutorial — how to use Maestro
Give a short, skimmable orientation (offer "2-min tour", "just the cheat-sheet", or "skip —
it's in the guide"):
- **Daily rhythm:** `/morning` to start · just talk through the day (it captures) · `/eod`
  to close · Friday `/retro`.
- **Commands — when to use which:** `/capture`, `/task`, `/schedule`, `/client`, `/newcase`,
  `/feedback`, `/meeting-to-work-items`. One line each.
- **The agents:** you never call them directly — Maestro routes. Name the 10 and what they're
  for (esp. `challenger` and `artifact-reviewer` = sparring + QA before anything goes up).
- **Builder Mode:** say "builder mode" to extend the system.
- Point to `Como-usar-o-Maestro.html` / `GUIDE.md` for depth.
Mark tutorial ✅ in the progress log.

## STEP 7 — Stage ④: Make it yours — first custom skill/agent (optional)
Ask: "Is there a task you do a lot that we could turn into a skill or an agent?" If yes,
switch to **Builder Mode** and design it with them (single purpose, sharp description,
reads/writes the brain), create the file, update the team table + README if it's an agent,
and remind them it activates after a session restart. This is where their personalized
Maestro begins. Mark the step ✅ (or ⏭️ if they pass).

## STEP 8 — Finish (or if they stop)
The progress log already records where they are. Recap it (✅/🟡/⏭️), name what's left, and
give the next move: **open a fresh chat and run `/morning`.** Be honest about what to
expect: the brief is fullest once **Microsoft 365 is connected** and **at least one
development objective** is seeded — until then `/morning` still works but runs lighter
(lighter calendar/email, a more generic nudge). Tell them they can re-run `/setup` anytime
to finish pending items, and that Maestro will remind them at session start until done.

User's optional context: $ARGUMENTS
