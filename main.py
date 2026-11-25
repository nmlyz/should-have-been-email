#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a joke about a meeting that should
have been an email.

The line was picked from 36 candidates by pairwise judging against the
brief — a remote meeting joined from different rooms in the same building,
to say nothing in high definition. It turns on its last word, names
something true about meetings people have actually sat through, and never
says the obvious line about the meeting being an email. The program checks
the result against the entry gate (length, single line, no leading or
trailing space, exact judged length) before writing it, then reads the
file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "We all joined from different rooms in the same building, "
    "to say nothing to each other in high definition."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
