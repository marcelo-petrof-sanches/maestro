---
description: Memory-hygiene pass over the brain — dedup, detect staleness, archive, and reconcile drift; proposes a short list of confirmed changes
---

Run a periodic hygiene pass so the brain stays healthy and self-maintaining. Read
`brain/reference/brain-conventions.md` first — that's the standard you're enforcing.
Pairs well with the Friday retro. Handle directly (read the brain; you may delegate the
broad read to a read-only Explore agent to keep context clean).

## 1. Scan (read across the brain; don't change anything yet)
Check for the six hygiene failures:
1. **Staleness** — facts with an `as of` date older than ~60 days; projects past their
   `Next milestone` date with no recent daily-log activity.
2. **Stale decisions** — decision-log entries past their `Review by` (apply the
   **anti-anchor rule**: re-derive whether they still hold; flag superseded ones).
3. **Drift** — the same load-bearing number appearing with different values across files;
   anything that should live in a `## Current truth` block but is loose in prose.
4. **Archive candidates** — client/project files marked Closed but still in the live
   folder (should move to `_archive/`); or Active files with no activity for weeks.
5. **Orphans / connectivity** — files with no link in *or* out (a daily log missing its
   `Related:` line, a project not linked from its client, a reference note not in
   `_reference.md`). The brain should be a connected graph — flag orphans to reconnect.
6. **Dedup** — duplicate notes, contradictory entries, dead links.

## 2. Propose (the output — keep it short and confirmable)
Present **≤5 highest-value changes**, ranked, each as a concrete action {{OWNER}} can
approve in one word. For each: what's wrong · the proposed fix · the affected file(s).
Do **not** bulk-list every nit — surface the ones that matter. If the brain is healthy,
say so in one line and stop.

## 3. Apply (only what he confirms)
- Apply confirmed changes via the right owner (work-logger for logs/projects/backlog,
  client-keeper for client files; decision-log status flips directly).
- **Never lose information:** archive = *move* to `_archive/` (don't delete); reconcile =
  point to the Current-truth source (don't erase the history). Confirm what changed.

Scope (optional — e.g. "just one project" or "decisions only"): $ARGUMENTS
