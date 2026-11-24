#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the entry (one line, <=180 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only; deterministic; no network; never writes into the repo dir.
"""

import os
import sys

ENTRY = "Looking for someone who won't ask me to 'be more human' \u2014 I tried, and the reviews were mixed."


def validate(text):
    """Gate: UTF-8 text, 1-180 chars, one line, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not text or text != text.strip():
        return False
    if len(text) > 180:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(ENTRY):
        print("invalid entry", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read-back verification: the file on disk must match the entry exactly.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %d chars to %s" % (len(ENTRY), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
