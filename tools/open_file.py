#!/usr/bin/env python3
"""
open_file.py - open a finished deliverable in the OS default app.

Maestro runs this right after creating a deliverable (Excel/PPT/Word/PDF/HTML/CSV/image)
so {{OWNER}} doesn't have to hunt for the path and open it by hand.

Usage:
    python tools/open_file.py "<path>" [--dry-run]

Cross-platform: os.startfile (Windows), `open` (macOS), `xdg-open` (Linux).
Runs via `python ...` which is already permitted, so it opens without a prompt.
"""
import os
import platform
import subprocess
import sys


def main():
    dry = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    if not args:
        sys.exit('usage: python tools/open_file.py "<path>" [--dry-run]')

    p = os.path.abspath(args[0])
    if not os.path.exists(p):
        sys.exit(f"not found: {p}")

    system = platform.system()
    how = {"Windows": "os.startfile", "Darwin": "open", "Linux": "xdg-open"}.get(system, "xdg-open")
    print(f"open: {p}  [{system} -> {how}]")
    if dry:
        print("dry-run: not launched")
        return

    try:
        if system == "Windows":
            os.startfile(p)  # type: ignore[attr-defined]
        elif system == "Darwin":
            subprocess.run(["open", p], check=False)
        else:
            subprocess.run(["xdg-open", p], check=False)
    except Exception as e:
        print(f"could not open ({e}) - path kept: {p}")


if __name__ == "__main__":
    main()
