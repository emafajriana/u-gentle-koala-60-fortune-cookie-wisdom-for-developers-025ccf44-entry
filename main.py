#!/usr/bin/env python3
"""Entry for make.fun: 'Fortune Cookie Wisdom for Developers'.

Writes one original fortune-cookie line for a software developer to
the output entry file. Stdlib only, deterministic.
"""

import os
import sys

FORTUNE = (
    "Legacy code is not a curse but a letter from developers who "
    "survived the same deadline you fear."
)

# No trailing newline: the gate counts every character in entry.txt,
# so the file holds exactly the fortune and nothing else.
assert FORTUNE == FORTUNE.strip(), "fortune must not carry stray whitespace"
assert "\n" not in FORTUNE, "fortune must be a single line"

MAX_CHARS = 120


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> int:
    """Read the written file back and check it against the gate:
    UTF-8 text, 1 to 120 characters, not only white space, and
    exactly the fortune this program was written to deliver."""
    with open(path, "r", encoding="utf-8", newline="") as fh:
        text = fh.read()
    if text != FORTUNE:
        print(f"FAIL: entry.txt differs from FORTUNE ({len(text)} chars)", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"FAIL: {len(text)} chars, gate is 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: entry is only white space", file=sys.stderr)
        return 1
    print(f"OK: {len(text)} chars — {text!r}")
    return 0


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(FORTUNE)
    return verify(path)


if __name__ == "__main__":
    sys.exit(main())
