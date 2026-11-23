"""Menyalin gambar berita hari ini ke folder keluaran make.fun.

Skrip kecil ini tidak mengubah gambar sama sekali: ia hanya
menyalin ulang entry.png byte demi byte dari samping skrip ini
ke direktori keluaran yang diminta.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print(f"Menyalin {source} -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
