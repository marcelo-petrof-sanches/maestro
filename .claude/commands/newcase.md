---
description: Onboard a new case from a proposal deck — extracts client/project info, asks me the gaps, creates the brain files
---

A new case is starting. Onboard it into the brain:

1. If no proposal file path was given below, ask me for it (PDF or PPTX).
2. Delegate to **case-onboarder**: pass the file path; it reads the full deck, drafts
   `brain/clients/<slug>.md` + `brain/projects/<slug>.md` (with `❓ TBC` markers), and
   returns a case summary + gap list.
3. Present me the 5-line case summary, then ask me the gap questions (in ONE compact
   batch, per my preferences — not one message per question).
4. With my answers: finalize both files (resolve the `❓ TBC` markers), add the case
   entry to `brain/profile/case-history.md` (newest first, including my role/workstream),
   and update the skills/exposure summary there if this case adds new exposure.
5. Seed `brain/tasks/backlog.md` with the immediate next steps implied by the proposal
   timeline (kickoff prep, data requests, first interviews).
6. Confirm: list the files created/updated and flag anything still open.

Proposal path + any context: $ARGUMENTS
