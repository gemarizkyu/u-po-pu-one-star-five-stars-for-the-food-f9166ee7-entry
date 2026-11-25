#!/usr/bin/env python3
"""One Star, Five Stars for the Food.

make.fun bounty: u-po-pu-one-star-five-stars-for-the-food-f9166ee7

The program writes a single sentence (at most 200 characters) to
/output/entry.txt: a one-star review of Earth written by an alien
tourist that still slips in a real compliment about the food.

No network, no model calls, no randomness, no wall clock: the text is
a fixed, hand-written sentence, so every run replays byte for byte.
"""

import os
import sys

# The entry: one sentence, 154 characters, one-star alien review of
# Earth with a genuine compliment about the food (smoky sate).
ENTRY = (
    "One star: Earth sells you water that falls free from the sky "
    "and charges rent just to sleep, but one plate of smoky sate "
    "made the whole invasion worth it."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the sealed gate: UTF-8 text, 1-200 chars, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over {MAX_CHARS}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")


def main() -> int:
    validate(ENTRY)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
