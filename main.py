"""One-line entry writer for the "One Line, Zero Use" sprint.

Writes exactly one line to /output/entry.txt as UTF-8 with no
trailing newline. Standard library only; nothing is printed and
nothing else is written.
"""

import os

ENTRY_LINE = "I can hear what my plants are thinking. They are thinking about dying, and they blame me."
OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(line):
    """Return the character count of line, or raise if it breaks the gate.

    The competition accepts a single line of 1-200 characters. A blank
    line is rejected too, so a whitespace-only entry can never slip
    through as a technically valid length.
    """
    count = len(line)
    if count < MIN_CHARS or count > MAX_CHARS:
        raise ValueError(
            "entry line must be {}-{} characters long, got {}".format(
                MIN_CHARS, MAX_CHARS, count
            )
        )
    if not line.strip():
        raise ValueError("entry line must not be blank")
    return count


def write_entry(line, path=OUTPUT_PATH):
    """Write line to path as UTF-8, creating the folder if needed.

    Opens with newline="" and writes the line exactly as given, so no
    trailing newline is ever added.
    """
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    check_length(ENTRY_LINE)
    write_entry(ENTRY_LINE)


if __name__ == "__main__":
    main()
