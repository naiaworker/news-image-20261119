#!/usr/bin/env python3
"""news-image-20261119 entry program (program/v1).

Copies the bundled entry.png (the entry image, generated for this bounty)
to /output/entry.png, byte for byte. Python standard library only.
Deterministic: the output is always exactly the bundled file's bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"entry.png not found next to main.py: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
