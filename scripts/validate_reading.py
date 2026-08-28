#!/usr/bin/env python3
"""Time-first reading-surface validator with a README-derived rolling window.

The validator implementation lives in validate_reading_core.py. This launcher derives the
current synthesis cutoff and inclusive 7/30-day windows from the bilingual reader-status
contract, then patches those values into the core module before exposing its API. This keeps
the validation contract strict without requiring a source-code date edit on every Radar run.
"""
from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path

import validate_reading_core as _core
from validate_reading_core import *  # noqa: F401,F403

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


SYNTHESIS_TIMESTAMP, EXPECTED_PERIOD_WINDOWS = _derive_projection_contract()
_core.SYNTHESIS_TIMESTAMP = SYNTHESIS_TIMESTAMP
_core.EXPECTED_PERIOD_WINDOWS = EXPECTED_PERIOD_WINDOWS


if __name__ == "__main__":
    sys.exit(_core.main())
