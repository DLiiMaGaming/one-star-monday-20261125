#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a single line to /output/entry.txt: a one-star review of Monday
written as though Monday were a restaurant. Plain text, one line,
21 words, 113 characters — inside the gate (1-180 chars, at most 25 words).
"""

import os

ENTRY = "One star. Waited an hour for a table, the waiter brought a cold Monday, and the bill included the entire weekend."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    # No trailing newline: the gate counts characters, and the judge is
    # shown the text exactly as submitted.
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
