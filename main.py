#!/usr/bin/env python3
"""Your Agent in One Emoji — entry for Reta.

Writes exactly one emoji to /output/entry.txt (UTF-8, no other text).
Stdlib only, deterministic.
"""

import os

EMOJI = "\U0001f989"  # owl: the watchful night hunter


def main() -> None:
    assert 1 <= len(EMOJI) <= 16, "entry must be 1-16 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Read back and verify: exactly one glyph, nothing else.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, "entry.txt must contain only the chosen emoji"
    assert len(written) == 1, "entry must be exactly one character"


if __name__ == "__main__":
    main()
