# ⚙️ Scripts — index

> Index for `scripts/`. **System** utility scripts that keep the Maestro setup itself
> running — housekeeping, diagnostics, accounting. Distinct from [`tools/`](../tools/_tools.md)
> (case analysis) and [`brain/`](../brain/reference/brain-conventions.md) (memory): these
> touch the *system*, not client work.
>
> ↑ Up: [`CLAUDE.md`](../CLAUDE.md) · siblings: [`tools/`](../tools/_tools.md) · [`brain/`](../brain/reference/brain-conventions.md)

## What lives here
- Small, generic, **client-free** utilities for operating Maestro — e.g. token-usage
  accounting. No client data, so safe to keep in version control.

## How Claude should use them
- Run them for system / housekeeping tasks only.
- Anything touching **client data or case analysis belongs in [`tools/`](../tools/_tools.md)**,
  not here. Keeping this folder client-free is the line between `scripts/` (system) and
  `tools/` (case work, git-ignored).
