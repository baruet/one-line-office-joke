#!/usr/bin/env python3
"""One-Line Office Joke: writes a single office joke to /output/entry.txt.

Deterministic: no network, no randomness, no secrets, no reads outside
the repository. The joke text is a fixed constant, so every run writes
byte-identical output.
"""

import os

JOKE = (
    "The office plant has survived three rounds of layoffs, two CEOs, "
    "and one rebrand, which is more job security than anyone in HR."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
