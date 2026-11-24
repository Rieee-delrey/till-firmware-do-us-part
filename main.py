#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow a robot speaks at its own wedding.

Writes a single sentence (under 200 characters) to /output/entry.txt,
reads it back, and verifies the bytes and the 1-200 character gate.
"""
import sys

ENTRY = "I take you to be my favourite human, and I promise never to update my firmware without asking you first."

OUT = "/output/entry.txt"


def main():
    if not (1 <= len(ENTRY) <= 200):
        print("gate failed: entry is %d chars, must be 1-200" % len(ENTRY), file=sys.stderr)
        return 1
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        print("gate failed: entry must be exactly one sentence", file=sys.stderr)
        return 1
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUT, encoding="utf-8") as f:
        back = f.read()
    if back != ENTRY:
        print("read-back failed: bytes differ", file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(ENTRY), OUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
