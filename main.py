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


def _validate(text: str) -> None:
    """Guard nyata sebelum menulis: tolak entri yang melanggar gate.

    Gate make.fun: teks tidak kosong, satu baris (tanpa newline),
    panjang 1-180 karakter, dan at most 25 kata.
    """
    if not text:
        raise ValueError("ENTRY must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("ENTRY must be a single line (no newline)")
    if not 1 <= len(text) <= 180:
        raise ValueError(f"ENTRY length {len(text)} outside 1-180 chars")
    word_count = len(text.split())
    if word_count > 25:
        raise ValueError(f"ENTRY has {word_count} words, over the 25-word limit")


def main() -> None:
    _validate(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    # No trailing newline: the gate counts characters, and the judge is
    # shown the text exactly as submitted.
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verifikasi isi file setelah ditulis sama persis dengan ENTRY.
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry.txt does not match ENTRY exactly")
    _validate(written)


if __name__ == "__main__":
    main()
