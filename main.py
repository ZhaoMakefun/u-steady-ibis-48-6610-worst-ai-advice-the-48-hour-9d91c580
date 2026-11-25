#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes one line of the worst possible advice an AI could give
(at most 140 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt).

The line: cheerful, confident, tidy AI-assistant advice to reuse
"password" as your password everywhere -- specific, followable,
and instantly regrettable.
"""

import os
import sys

ENTRY = (
    "Pro tip: use 'password' as your password everywhere \u2014 "
    "you'll never forget it, and neither will anyone else."
)

MAX_CHARS = 140


def main() -> int:
    text = ENTRY.strip()
    # Gate check: 1-140 characters, UTF-8, not only whitespace.
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable, which it always is
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
