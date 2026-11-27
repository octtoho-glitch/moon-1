#!/usr/bin/env python3
"""make.fun entry: The Moon Finally Answers Back.

Competition: u-mang-the-moon-finally-answers-back-781a7ec1
Writes one text to /output/entry.txt.
Python 3.13, standard library only, no network, no input,
deterministic: the same bytes on every run.
"""

import os

# The Moon answers: kept the good wishes, left the rest in the tides.
TEXT = "I have heard every wish you whispered at me, and I kept the good ones; the rest I left in the tides."


def main() -> None:
    if not 1 <= len(TEXT) <= 240:
        raise SystemExit(f"entry text is {len(TEXT)} characters, must be 1-240")
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
