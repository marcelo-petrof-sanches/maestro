---
description: Pre-send gate — run challenger (message pressure-test) + artifact-reviewer (brief conformity) on a FINISHED deliverable before it goes to a partner/MDP/client. Use for "is this ready to send", "pre-flight this deck/email/model".
argument-hint: [the deliverable + who it's going to + the brief/ask]
---

The "sparring before it goes up" gate. Before anything reaches a partner/MDP/client, run
BOTH review lenses and synthesize a single go/no-go. You orchestrate on the main thread;
the two agents do the legwork.

Use this on a **finished deliverable** (a draft that's about to be sent). For sharpening a
*plan* before you build, use `/grill-me`; for debugging a *broken* output, use `/investigate`.

## 1. Gather
Identify three things: the **deliverable** (file / message / deck / number), the
**audience** (who it's going to), and the **brief/ask** it must satisfy. If the brief is
unclear, ask one line — the conformity check needs it.

## 2. Run both lenses concurrently
Send both agents in a single message so they run in parallel:
- **`challenger`** — pressure-test the message/logic/so-what (3 lenses: logic · risk ·
  audience). Pass the deliverable + client context.
- **`artifact-reviewer`** — conformity: does the finished thing actually do what the brief
  asked? Pass the brief + the artifact.

## 3. Synthesize (fixed contract)
One decisive verdict: **ship · ship with tweaks · fix and re-gate.** Then:
- **Blocking gaps** — must-fix before sending (from either agent), ranked.
- **The hard question** the room will ask (from `challenger`), verbatim-ish.
- **Conformity gaps** — what the brief asked for that's missing/weak (from `artifact-reviewer`).
- **Fastest path to ship** — the smallest set of fixes that clears the blockers.

Don't rubber-stamp: if **either** agent flags a must-fix, the verdict is not "ship". When in
doubt, push — the failure mode to guard against is waving through something a partner tears apart.

Deliverable + audience + brief: $ARGUMENTS
