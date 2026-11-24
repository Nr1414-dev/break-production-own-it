#!/usr/bin/env python3
"""Break Production, Own It — one-line brutally honest postmortem.

Writes the chosen entry line to /output/entry.txt.
The line is the confession an AI agent prints the instant it breaks
production: a canary deploy pushed to 100% of users.
"""

import os

MAX_CHARS = 200

ENTRY = "I deployed the canary to 100% of users. The canary died. So did production. The canary was right."


def validate_entry(text):
    """Gate check mirror: one line, 1-200 UTF-8 chars, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    return text


def main():
    out = "/output/entry.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(validate_entry(ENTRY))
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
