"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the entrant's own fridge to
/output/entry.txt. The line is a fixed, hand-written joke: the program
itself is deterministic, so the graded run reproduces the exact same
text every time.

The roast: the fridge hums all night like it is rehearsing for a choir
it will never join, and its only solo is the ice maker choking on a
cube. Specific detail (the ice maker), twist in the last few words,
one line, reads aloud cleanly.
"""

import os

ENTRY = (
    "My fridge hums all night like it's rehearsing for a choir it'll "
    "never join, and its only solo is the ice maker choking on a cube."
)


def validate(entry: str) -> None:
    """Enforce the competition gate locally: 1 to 200 chars, one line."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry is {len(entry)} chars, must be 1-200")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
