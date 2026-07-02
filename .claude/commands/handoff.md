---
description: Compact the current session into a structured handoff so a new session (or tomorrow) resumes cleanly. Use for "hand this off", "save context", "prep a resume", or when wrapping mid-task before context resets.
argument-hint: [optional focus]
---

Turn the live session into a durable, **structured** handoff so nothing is lost when context
resets or you pick it up tomorrow. This is the mid-task continuity tool — lighter than
`/eod` (which is the full end-of-day close). Retrieval-first: file it where you'll look for
it next.

## 1. Capture — the structured block (the pattern that makes resume reliable)
Write a compact handoff with these fields (skip any that are empty):
- **Goal** — what we're trying to accomplish.
- **State** — what's done / where we are right now.
- **Decisions made** — the durable ones (also send to `/decision-log`).
- **Remaining** — the next concrete steps, ordered.
- **Dead ends** — approaches already tried that did NOT work, so the next session doesn't
  waste time re-trying them. (This field is the highest-value part — most handoffs omit it.)
- **Open questions / waiting-on** — what's blocked and on whom.
- **Load-bearing facts/numbers** — send to the project's `## Current truth` (link, don't restate).

## 2. File it
Append the block to today's `brain/daily/YYYY-MM-DD.md` under a `## Handoff` heading
(work-logger owns the daily log). Promote durable items to their real homes
(decision-log / Current truth / client file) rather than leaving them only in the handoff.

## 3. Confirm
Three lines on what a fresh session needs to read to resume: the daily `## Handoff` block +
the linked homes. (To resume later, that's exactly what you read first.)

Focus: $ARGUMENTS
