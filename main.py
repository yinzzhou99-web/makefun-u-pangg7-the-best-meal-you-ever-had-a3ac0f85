#!/usr/bin/env python3
"""The Best Meal You Ever Had.

Writes one sentence about the best meal ever had to /output/entry.txt.
Standard library only; no network, no third-party packages.
"""

import os

TEXT = (
    "My grandmother's rendang, simmered since dawn in coconut milk and dried "
    "chilies, tasted of woodsmoke and patience, and I ate three helpings "
    "standing in her kitchen doorway."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError("entry text must be 1-200 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
