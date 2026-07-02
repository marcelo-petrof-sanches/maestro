---
description: Systematic root-cause investigation of something broken or surprising — a number that won't tie, a model throwing off results, data that contradicts itself. Use for "investigate", "why is this wrong", "this doesn't add up", "debug this".
argument-hint: [what's broken / the symptom]
---

A disciplined root-cause loop for broken or surprising analytical outputs. **Iron law: no
fixes without investigation** — don't patch a symptom before you've proven the cause.
Handle directly; delegate heavy data work to `analyst`.

Use this on a **broken/surprising output**. To sharpen a plan use `/grill-me`; to gate a
finished deliverable use `/pre-flight`.

## The loop
1. **State the symptom precisely** — expected vs. actual, with the exact number/behaviour and
   *where* it appears (cell, slide, table). Reproduce it before theorising.
2. **Trace, don't guess** — follow the data/logic flow **backward** from the symptom to its
   source. Read the actual formulas/cells/steps; never assume what a step does.
3. **Hypotheses, ranked** — list the plausible causes; pick the most likely × cheapest to test.
4. **Test one at a time** — confirm or kill each hypothesis with evidence before moving on;
   note what you ruled out (so you don't circle back).
5. **Stop rule** — after **3 failed fix attempts**, stop: your model of the problem is
   probably wrong. Re-frame the symptom from scratch before trying again.
6. **Fix + verify** — once the root cause is *proven* (not suspected), fix it, then re-check
   the symptom is gone **and** nothing downstream broke.

## Close (fixed contract)
- **Root cause** — proven, stated in one line (with the evidence that proves it).
- **The fix** — what changed.
- **Blast radius** — does this mean a number that already went out was wrong? If yes, flag it
  for correction and update the project's `## Current truth`.
- **The gotcha** — capture the lesson as a durable learning so it can't recur (feeds `/consolidate`).

What's broken: $ARGUMENTS
