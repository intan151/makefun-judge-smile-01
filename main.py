#!/usr/bin/env python3
"""Make the Judge Smile — one warm, surprising line about a small good thing today.

Writes a single line of at most 200 characters to /output/entry.txt.
Python standard library only; no network, no randomness.
"""

import os

ENTRY = (
    "This morning the warung lady tucked a still-warm fried banana into my bag "
    "and whispered, 'for the road \u2014 the rain is coming,' and the sky really "
    "did wait until I was home."
)


def validate_entry(text):
    """The gate needs 1-200 characters, one line, not only whitespace."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    return text


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
