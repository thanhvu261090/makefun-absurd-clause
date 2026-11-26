#!/usr/bin/env python3
"""An absurd clause hidden deep inside a terms-of-service agreement.

Writes the clause to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Gate: one original English sentence, at most 200 characters.
"""

import os

ENTRY = (
    "The user agrees that, by scrolling past this clause, they have legally "
    "adopted the company's office plant, including all future watering obligations."
)
# One sentence, 149 chars: scrolling past unread boilerplate legally adopts
# the office plant — deadpan consent language, absurd obligation.


def validate(text):
    """Return True only if text is a valid gate entry."""
    if not isinstance(text, str):
        return False
    if not text.strip() or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    return 1 <= len(text) <= 200


def write_entry(text, path):
    """Write the entry text to path, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not validate(ENTRY):
        raise SystemExit("entry fails the gate: must be one sentence, <= 200 chars")
    write_entry(ENTRY, path)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
