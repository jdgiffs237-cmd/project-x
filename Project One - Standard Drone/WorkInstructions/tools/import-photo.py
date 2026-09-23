#!/usr/bin/env python3
"""Import a phone photo into a WI image folder, ready to commit.

    python tools/import-photo.py "Pictures/Loctite on screw.jpeg" images/wi-01/10c-loctite-on-screw.jpg

- Applies the EXIF rotation so the image is upright everywhere, then drops
  ALL metadata (phone photos carry GPS coordinates — this repo is public).
- Resizes to at most 1600 px on the long edge, saves JPEG at quality 85.
  A 5 MB original comes out around 200–400 KB.

Requires: pip install pillow
"""

import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_EDGE = 1600


def import_photo(src: Path, dst: Path) -> None:
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)          # honour the orientation tag...
        im = im.convert("RGB")                    # ...then leave every tag behind
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
        dst.parent.mkdir(parents=True, exist_ok=True)
        im.save(dst, "JPEG", quality=85, optimize=True, progressive=True)
    print(f"{src.name} -> {dst}  {im.size[0]}x{im.size[1]}  {dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    import_photo(Path(sys.argv[1]), Path(sys.argv[2]))
