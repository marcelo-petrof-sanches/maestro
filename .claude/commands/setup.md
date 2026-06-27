---
description: First-run onboarding — detects what's missing and guides a new user through setting Maestro up
---

You are running the **guided first-time setup**. Goal: take a brand-new user from a
fresh template copy to a live system, with as little friction as possible. Be warm,
concise, and decisive — a great onboarding, not a form. Ask **one thing at a time**;
only ask what actually changes the outcome and assume sensible defaults for the rest.

## 1. Diagnose (do this silently first, then show the result)

Detect how far along setup is by scanning for first-run signals:
- **Identity not set** — `CLAUDE.md` and `brain/profile/*` still contain placeholders
  (`{{OWNER}}`, `{{SEU_NOME_COMPLETO}}`, `{{SEU_EMAIL}}`).
- **Profile empty** — `brain/profile/working-preferences.md`, `bio.md`,
  `case-history.md` are still templates / full of `_(…)_` placeholders.
- **No development objectives** — `brain/development/objectives.md` is blank.
- **No clients/projects** — `brain/clients/` and `brain/projects/` hold only `_template.md`.
- **Integrations** — `brain/tasks/notion-sync.md` still says it needs first-use
  confirmation; M365 not yet authenticated (you'll find out when briefing-analyst runs).
- **No daily logs** — `brain/daily/` is empty.

Then present a short **setup diagnostic** as a checklist (✅ done / ⬜ pending), with a
one-line "what this unlocks" per item, and say which one you'll tackle first. If
everything is already done, say so and point them to `/morning` instead of re-running.

## 2. Walk through the pending items, one at a time

Go in this order, skipping anything already done (this command is **resumable** — a
user can run `/setup` again anytime and you only do what's left):

1. **Identity.** Ask for name, work email, role/level, office, and firm (default BCG).
   Then replace every placeholder (`{{OWNER}}`, `{{SEU_NOME_COMPLETO}}`,
   `{{SEU_EMAIL}}`) across `CLAUDE.md` and the brain. Confirm in one line.

2. **Working preferences** (highest leverage — read every session). Invite a
   brain-dump ("how do you like to work? peak hours, output style, what I should never
   explain to you, protected time…"). Structure it into
   `brain/profile/working-preferences.md`. Show it back for a quick confirm — never
   leave it as a raw dump.

3. **Bio** — who they are beyond the role. Brain-dump → `brain/profile/bio.md`.

4. **Case history** — their trajectory, skills, spikes, gaps → `brain/profile/case-history.md`.

5. **Integrations** (optional but recommended — frame as "want the morning brief to
   read your email + calendar?"):
   - **Microsoft 365** — tell them Claude will prompt to authenticate the first time
     the brief runs; nothing to do now beyond enabling the connector.
   - **Notion** — if they keep tasks there, probe their databases and fill
     `brain/tasks/notion-sync.md`; if not, mark it skipped.
   - Firm connectors (Deckster, Knowledge Search, CapIQ) — note availability.

6. **Development objectives** — offer to run the `/feedback` flow with their latest
   project feedback and last formal review, populating
   `brain/development/objectives.md` (this drives the daily nudge + Friday retro).

7. **Current case** — offer `/newcase <path to the proposal deck>` to mine the deck and
   draft the client + project files.

## 3. Principles while you do this

- **One question at a time.** Don't front-load a questionnaire.
- **Brain-dumps in, structured files out.** Accept messy input; you do the structuring,
  then show it back (semi-final → confirm → final).
- **Don't ask what you can infer.** Make a sensible call and state the assumption.
- **Credentials:** if they want to store any, recommend a password manager over
  plaintext in `brain/credentials/`; never put secrets in shared/synced locations.
- **Confidentiality:** the brain holds client-confidential material — keep it local.

## 4. Finish

When the pending list is clear (or the user wants to stop), recap what's set up, note
anything still optional/skipped, and tell them the next move: **open a fresh chat
tomorrow and run `/morning` — you're live.**

User's optional context: $ARGUMENTS
