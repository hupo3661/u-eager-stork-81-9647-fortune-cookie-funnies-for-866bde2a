"""Fortune Cookie Funnies for Engineers: one-line fortune.

Writes the single fortune-cookie line to /output/entry.txt.
The entry text itself is fixed by the contest submission and must
not be altered; only the surrounding plumbing may change.
"""

TEXT = "You will finally delete the dead code, and production will immediately miss it."

# Contest limit: the entry line must stay within 120 characters.
assert len(TEXT) <= 120, "entry line exceeds 120 characters"

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write the fortune line plus a trailing newline to path.

    Opens the file explicitly (instead of a bare one-liner) so the
    handle is always closed, even if the write is interrupted.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main():
    write_entry()


if __name__ == "__main__":
    main()
