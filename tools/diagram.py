#!/usr/bin/env python3
"""
diagram.py - render a Mermaid diagram to SVG/PNG (offline, best-effort).

The *English -> mermaid* step is Claude's job (via /diagram). This tool just renders
the mermaid source, and never hard-fails: if the renderer isn't available it keeps the
.mmd source and tells you where to paste it.

Usage:
    python tools/diagram.py <input.mmd> [--out-dir DIR] [--name NAME] [--png]
    echo "flowchart LR; A-->B" | python tools/diagram.py - --name flow

Renderer: mermaid-cli via `npx -y @mermaid-js/mermaid-cli` (needs Node; downloads a
headless Chromium on first use -> that first run needs network and may be blocked on a
locked machine). Content stays local; only the npm package is fetched. The .mmd source is
always kept and is importable at https://mermaid.live and excalidraw.com (Mermaid import)
for editing.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def render(mmd_path: Path, out_base: Path, png: bool) -> list[Path]:
    """Try to render via mermaid-cli. Return produced files (empty if renderer absent)."""
    npx = shutil.which("npx")
    if not npx:
        return []
    produced = []
    targets = [out_base.with_suffix(".svg")]
    if png:
        targets.append(out_base.with_suffix(".png"))
    for target in targets:
        try:
            r = subprocess.run(
                [npx, "-y", "@mermaid-js/mermaid-cli", "-i", str(mmd_path),
                 "-o", str(target), "-q"],
                capture_output=True, encoding="utf-8", errors="replace", timeout=180,
            )
            if r.returncode == 0 and target.exists():
                produced.append(target)
            else:
                sys.stderr.write((r.stderr or "").strip()[:500] + "\n")
        except Exception as e:  # timeout, missing chromium, blocked network...
            sys.stderr.write(f"render skipped ({target.suffix}): {e}\n")
    return produced


def main():
    ap = argparse.ArgumentParser(description="Render a Mermaid diagram (offline, best-effort).")
    ap.add_argument("input", help="path to a .mmd file, or '-' to read mermaid from stdin")
    ap.add_argument("--out-dir", default=".", help="output directory (default: cwd)")
    ap.add_argument("--name", default="diagram", help="base name for outputs")
    ap.add_argument("--png", action="store_true", help="also render a PNG")
    args = ap.parse_args()

    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    src = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")

    mmd_path = out_dir / f"{args.name}.mmd"
    mmd_path.write_text(src, encoding="utf-8")

    produced = render(mmd_path, out_dir / args.name, args.png)

    print(f"source: {mmd_path}")
    if produced:
        for p in produced:
            print(f"rendered: {p}")
        print("Editable: paste the .mmd into excalidraw.com (Mermaid import) or mermaid.live.")
    else:
        print("renderer unavailable (no Node/mermaid-cli, or blocked) - source kept.")
        print("Render/edit online: https://mermaid.live  or  excalidraw.com (Mermaid import).")


if __name__ == "__main__":
    main()
