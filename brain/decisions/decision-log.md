# Decision Log

> The single, durable record of **decisions that shape work** — methodology, scope,
> stakeholder, commercial, ways-of-working. Append-only and numbered (`D-NNN`). One
> place so a decision made once never has to be re-litigated or re-discovered.
> Maintained via `/decision-log`; also written to by `/meeting-to-work-items` and `/eod`.

## What belongs here (and what doesn't)
- **Log it:** anything you'd be annoyed to re-argue — a methodology choice, a scope
  boundary, a stakeholder call, a pricing/commercial term, a "we decided to do X not Y".
- **Don't log it:** routine task progress (→ daily log), client facts/people
  (→ client file), load-bearing numbers (→ the project's **Current truth** block).
  A decision *about* a number lives here; the number itself lives in the project file.

## ⚠️ Anti-anchor rule — READ BEFORE TRUSTING ANY ENTRY
A decision log is a **snapshot of a moment**, not current truth. Before you rely on an
entry:
1. **Check the date and `Review by`.** A decision past its review date is *suspect*, not
   *true*. Re-derive whether it still holds before acting on it.
2. **Check `Status`.** `Superseded` entries are kept for history — follow the pointer to
   the entry that replaced them. Never quote a superseded decision as current.
3. **When in doubt, re-derive from primary sources** (the project file, the latest daily
   logs) rather than anchoring on what was decided weeks ago. The log tells you *what was
   decided and why*, not *what is true now*.

## How to add / change an entry
- **Add:** next `D-NNN` (ascending, never reused), today's date, newest at the **top** of
  the log. Fill every field; if unknown, write `—`.
- **Change:** never rewrite an entry's substance. To reverse or revise a decision, add a
  **new** entry and flip the old one's `Status` to `Superseded by D-MMM` (the only edit
  allowed on a past entry). This keeps the history honest.

### Entry shape
```
### D-NNN · YYYY-MM-DD · <one-line decision>
- **Decision:** <what was decided, in one sentence — the imperative outcome>
- **Why / context:** <the reasoning or trigger, brief>
- **Decided by:** <who> · **Project:** [<slug>](../projects/<slug>.md) · **Client:** <name>
- **Review by:** YYYY-MM-DD (or `—` if durable / no natural expiry)
- **Status:** Active  (or: Superseded by D-MMM · YYYY-MM-DD)
```

---

## Log (newest first)

<!-- ↓ New entries go here, at the top, with the next ascending D-NNN. -->
