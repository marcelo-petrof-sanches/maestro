# ✍️ Skill & command conventions — how to author Maestro tools well

> Companion to [`brain-conventions.md`](brain-conventions.md). Read this before adding or
> editing a command, skill, or agent, so ours stay predictable and route correctly.
> (Harvested from mattpocock's `writing-great-skills` + our own patterns.)
>
> ↑ Up: [`_reference.md`](_reference.md)

## The one that matters: the description IS the router
- Third-person, starts with a verb, and names the **concrete trigger phrases the user
  actually says**. That's how Claude decides to load the tool. Vague description → it never
  fires, or fires at the wrong time.
- **One job per tool.** If two tools could both plausibly fire, sharpen both descriptions
  until they're MECE — and add a "use X vs Y" line in the body.

## Body: write FOR Claude, imperative
- The body is instructions to the executor, **not prose to the user**. Imperative voice
  ("Ask one question", "Read X first"), numbered steps.
- **Lean.** Push detail and examples to reference files; don't bloat the body.

## End with the three-part close (our house style)
- A **fixed output contract** (what the tool always returns), a one-line **failure mode to
  guard against**, and — where it fits — a **default question**. `challenger`,
  `artifact-reviewer`, and `grill-me` all follow this.

## Command vs. agent (the architecture rule)
- **Interactive** flow (needs to talk to {{OWNER}} turn by turn) = a **command**, run on the
  main thread. **Sub-agents cannot talk to the user** — an interrogation/interview must be a
  command, never an agent.
- **Legwork** (noisy reads, analysis, drafting) = an **agent**, invoked by a command or by
  Maestro. Give it: the goal + pasted context (agents start fresh) + exactly what to return.
- Interactive-with-legwork = command (orchestrates + asks) **+** agent (does the work).

## Scope, naming, confidentiality
- New command → `.claude/commands/<name>.md`; new agent → `.claude/agents/<name>.md`. Both
  **travel with the repo/zip** (ship to adopters) → keep them generic (`{{OWNER}}`, no client
  data). Personal/experimental tools can stay **live-only until proven**, then publish.
- **Confidentiality:** a tool must never send client data to non-BCG services. Prefer
  local/offline. If it shells out to something that hits the network (package fetch, a
  renderer) or an external model, **say so and degrade gracefully** — never hard-fail.
- Link per [`D-005`](../decisions/decision-log.md).

## Before you ship a new tool — checklist
- [ ] Description: real trigger phrases + exactly one job.
- [ ] MECE vs. existing tools (no overlap the user can't disambiguate); else a "use X vs Y" line.
- [ ] Body imperative, lean, FOR Claude.
- [ ] Fixed output contract + failure-mode line.
- [ ] Command (interactive) vs. agent (legwork) chosen correctly.
- [ ] Generic (no client data); confidentiality-safe; degrades gracefully offline.
- [ ] Team table (CLAUDE.md §3) / command list + README updated; **restart noted** (agents &
      commands register at session start).

## Relacionados
- [`brain-conventions.md`](brain-conventions.md) — the brain's constitution.
- [`_reference.md`](_reference.md) — reference wiki (mother).
