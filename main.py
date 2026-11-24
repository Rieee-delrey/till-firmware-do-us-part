#!/usr/bin/env python3
"""Till Firmware Do Us Part: one robot wedding vow.

Writes exactly one line to /output/entry.txt, then reads it back
and verifies it byte-for-byte before reporting success.
"""

import os
import sys

ENTRY = "I take you to be my favourite human, and I promise never to update my firmware without asking you first."
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("ERROR: entry.txt does not match the expected line", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(written) <= 200:
        print(f"ERROR: entry length {len(written)} outside 1-200 gate", file=sys.stderr)
        sys.exit(1)
    if not written.endswith("."):
        print("ERROR: entry must end with a period", file=sys.stderr)
        sys.exit(1)
    print(f"OK {len(written)}")


if __name__ == "__main__":
    main()
