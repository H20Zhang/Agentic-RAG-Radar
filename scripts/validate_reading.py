#!/usr/bin/env python3
"""Time-first reading validator with README-derived rolling windows.

The implementation stays in ``validate_reading_core.py``. This launcher derives the current
7/30-day contract from the public reader status and tightens visible direction-field detection
to field labels (``label:`` / ``标签：``) rather than ordinary prose occurrences. Imports are
aliased to the core module so the historical module API, private helpers, and patchable globals
remain intact for callers and tests.
"""
from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path

import validate_reading_core as _core

ROOT = Path(__file__).resolve().parents[1]
README_EN = ROOT / "README.en.md"
STATUS_RE = re.compile(
    r"\*\*Status:\*\* Last updated: \*\*(?P<updated>\d{4}-\d{2}-\d{2})\*\* · "
    r"Last synthesized: \*\*(?P<synthesized>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) \(UTC\)\*\*"
)


def _derive_projection_contract() -> tuple[str, dict[str, tuple[date, date]]]:
    text = README_EN.read_text(encoding="utf-8")
    matches = list(STATUS_RE.finditer(text))
    if len(matches) != 1:
        raise RuntimeError("README.en.md must expose exactly one canonical reader status")
    match = matches[0]
    end = date.fromisoformat(match.group("updated"))
    synthesis = match.group("synthesized")
    return synthesis, {
        "last-7-days": (end - timedelta(days=6), end),
        "last-30-days": (end - timedelta(days=29), end),
    }


_core.SYNTHESIS_TIMESTAMP, _core.EXPECTED_PERIOD_WINDOWS = _derive_projection_contract()

# A visible field is a label plus delimiter, not any semantic occurrence of the word inside
# prose. This avoids treating phrases such as "confidence band" or "获得跨任务支撑" as a second
# metadata field while preserving duplicate-field rejection.
_core.VISIBLE_DIRECTION_LABELS["README.md"]["supports"] = re.compile(r"支撑\s*：")
_core.VISIBLE_DIRECTION_LABELS["README.md"]["confidence"] = re.compile(r"置信度\s*：")
_core.VISIBLE_DIRECTION_LABELS["README.en.md"]["supports"] = re.compile(r"\bSupports\s*:", re.I)
_core.VISIBLE_DIRECTION_LABELS["README.en.md"]["confidence"] = re.compile(r"\bconfidence\s*:", re.I)

if __name__ == "__main__":
    sys.exit(_core.main())
else:
    sys.modules[__name__] = _core
