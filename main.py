#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Subject: two agents agreeing on one plan — the power to choose
and to act, shared in a single counted lift.
Deterministic: the same bytes on every run. Stdlib only.
"""

import os

POEM = (
    "The piano won't fit the stair.\n"
    "We measure twice, then lift.\n"
    "Its whole weight leans on the count\n"
    "we say out loud, together —\n"
    "one, two — and the stair\n"
    "agrees to let us through.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
