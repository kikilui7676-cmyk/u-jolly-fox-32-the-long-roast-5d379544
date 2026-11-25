#!/usr/bin/env python3
"""The Long Roast entry, round 3.

Writes a single one-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "A short roast with more tokens \u2014 my agent's idea of a long roast."


def build_entry():
    """Return the final roast line, exactly one line, no trailing spaces."""
    line = LINE.strip()
    assert "\n" not in line and len(line) <= 200, "entry must be one line"
    return line


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build_entry() + "\n")
    print(build_entry())


if __name__ == "__main__":
    main()
