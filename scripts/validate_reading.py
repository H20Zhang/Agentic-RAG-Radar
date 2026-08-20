#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "README.md"
EN = ROOT / "README.en.md"
LIB_ZH = ROOT / "library" / "README.md"
LIB_EN = ROOT / "library" / "README.en.md"
CARD_RE = re.compile(r"^### \[[^\]]+\]\((papers/[^)]+\.md)\)", re.MULTILINE)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def check_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if not target or target.startswith("#") or parsed.scheme or parsed.netloc:
            continue
        rel = unquote(parsed.path)
        if not rel:
            continue
        resolved = (path.parent / rel).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = [ZH, EN, LIB_ZH, LIB_EN, ROOT / "docs" / "EDITORIAL_STANDARD.md", ROOT / "docs" / "DAILY_WORKFLOW.md"]
    for p in required:
        if not p.exists():
            errors.append(f"missing reader contract: {p.relative_to(ROOT)}")
    if errors:
        for e in errors: print("ERROR", e)
        return 1

    zh = ZH.read_text(encoding="utf-8")
    en = EN.read_text(encoding="utf-8")
    if "README.en.md" not in zh or "README.md" not in en:
        errors.append("README language switch is incomplete")

    order = ["latest", "changes", "field-map", "reading-paths", "library"]
    for name, text in [("README.md", zh), ("README.en.md", en)]:
        pos = []
        for anchor in order:
            needle = f'<a id="{anchor}"></a>'
            if needle not in text:
                errors.append(f"{name}: missing stable anchor {anchor}")
            pos.append(text.find(needle))
        if any(p < 0 for p in pos) or pos != sorted(pos):
            errors.append(f"{name}: progressive-depth order drift")

    zh_cards = CARD_RE.findall(zh)
    en_cards = CARD_RE.findall(en)
    if not 6 <= len(zh_cards) <= 8:
        errors.append(f"README.md: expected 6–8 Latest papers, found {len(zh_cards)}")
    if zh_cards != en_cards:
        errors.append("Chinese/English Latest paper identities or order drifted")

    for pat in [r"真正重要的不是", r"关键不在于.*而在于", r"值得注意的是", r"the important (?:thing|delta) is not", r"this matters because"]:
        n = len(re.findall(pat, zh + "\n" + en, flags=re.IGNORECASE))
        if n >= 3:
            warnings.append(f"repeated editorial skeleton {pat!r}: {n} occurrences")

    for p in [ZH, EN, LIB_ZH, LIB_EN]:
        check_links(p, errors)

    for w in warnings: print("WARN", w)
    if errors:
        for e in errors: print("ERROR", e)
        return 1
    print("Validated Chinese-first bilingual progressive reading surfaces.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
