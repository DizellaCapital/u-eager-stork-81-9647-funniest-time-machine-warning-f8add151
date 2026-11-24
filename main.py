"""Funniest Time Machine Warning Label entry program.

Writes one warning label for a time machine to
MAKEFUN_OUTPUT_DIR/entry.txt. The label is a single line of at most
120 characters, phrased as a genuine safety notice. Standard library
only.
"""

import os
import sys

ENTRY = "WARNING: At 6:04 p.m., do not greet the man in your coat. He is you, and he already reported you as a stranger."


def fail(message):
    print(message, file=sys.stderr)
    return 1


def main():
    text = ENTRY
    if len(text) < 1 or len(text) > 120:
        return fail("entry must be 1-120 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        return fail("entry must be a single line")
    if "\t" in text:
        return fail("entry must not contain tabs")
    if not text.strip():
        return fail("entry must not be only whitespace")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != text:
        return fail("read-back mismatch")
    print("entry written: %d characters" % len(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
