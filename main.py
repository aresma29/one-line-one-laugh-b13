"""Print the one-line entry exactly as stored in entry.txt.

Reads the entry from the file next to this script, writes it to stdout
with no added newline, and exits 0. Works from any working directory.
"""
import os
import sys


def main():
    entry_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
