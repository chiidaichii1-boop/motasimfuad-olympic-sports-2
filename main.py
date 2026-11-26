"""Rejected Olympic Sports entry.

Writes one funny single-line sport the Olympics turned down to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Python standard library only; fully deterministic.
"""

import os

LINE = (
    "Synchronised Sighing: four athletes sigh in perfect unison "
    "at a delayed train announcement \u2014 gold for the deepest "
    "collective disappointment."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
