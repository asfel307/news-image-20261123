#!/usr/bin/env python3
"""Ship the pre-rendered front page for make.fun.

Standard library only. Copies entry.png from beside this file into
$MAKEFUN_OUTPUT_DIR/entry.png (falling back to /output), byte for byte.
Deterministic: the same input file always produces the same output file.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("copied", src, "->", dst)


if __name__ == "__main__":
    main()
