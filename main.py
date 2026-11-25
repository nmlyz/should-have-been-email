#!/usr/bin/env python3
"""Write one line about a meeting that should have been an email.

The line is kept as a single constant, checked against the entry
rules, and written to entry.txt.
"""

import os
import sys

LINE = "We all joined from different rooms in the same building, to say nothing to each other in high definition."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print("error: line must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line must not have leading or trailing whitespace",
              file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in LINE):
        print("error: line must not contain control characters",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(path, "rb") as f:
        data = f.read()
    if data != (LINE + "\n").encode("utf-8"):
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if data.count(b"\n") != 1 or not data.endswith(b"\n"):
        print("error: output must be exactly one line plus newline",
              file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
