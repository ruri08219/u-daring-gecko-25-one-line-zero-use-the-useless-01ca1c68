#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner naming a hilariously useless
superpower to /output/entry.txt.
"""

import os

LINE = "I can hear what my plants are thinking. They are thinking about dying, and they blame me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
