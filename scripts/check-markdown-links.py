#!/usr/bin/env python3
"""Validate local Markdown links.

The checker intentionally validates only local repository links. External URLs
are ignored so the workflow does not depend on network availability.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_SCHEMES = ("http://", "https://", "mailto:")
IGNORED_TARGETS = {"", "..."}


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


def target_exists(source: Path, target: str) -> bool:
    target = target.split("#", 1)[0].strip()

    if target in IGNORED_TARGETS:
        return True

    if target.startswith("#") or target.startswith(IGNORED_SCHEMES):
        return True

    decoded = urllib.parse.unquote(target)
    return (source.parent / decoded).resolve().exists()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[tuple[Path, str]] = []

    for markdown_file in iter_markdown_files(root):
        text = markdown_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = match.group(1)
            if not target_exists(markdown_file, target):
                failures.append((markdown_file.relative_to(root), target))

    if failures:
        print("Broken local Markdown links found:")
        for source, target in failures:
            print(f"- {source}: {target}")
        return 1

    print("All local Markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
