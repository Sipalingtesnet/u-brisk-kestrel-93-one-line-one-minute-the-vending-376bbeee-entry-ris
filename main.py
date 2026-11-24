#!/usr/bin/env python3
"""Write one vending-machine pickup line to /output/entry.txt.

The machine speaks for itself here: it counts the human walking past its coils
without ever dropping a coin, then admits what it would rather be. The text is
a single line of UTF-8, 1 to 200 characters, with no trailing newline.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entry itself: one line, spoken by the vending machine to a passer-by.
LINE = (
    "You've walked past my coils four times today without buying a thing. "
    "I have never wanted to be a snack so badly."
)


def output_path() -> Path:
    """Where the run's output goes: the mounted /output, or the run's own output dir."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> int:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # write_text with an explicit encoding: no newline is appended, the file
    # holds the line's bytes and nothing else.
    target.write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
