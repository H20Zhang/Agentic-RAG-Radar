#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:
    raise SystemExit("Install dependencies with: pip install jsonschema") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "data" / "paper.schema.json"
PAPERS_DIR = ROOT / "data" / "papers"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )

    if not PAPERS_DIR.exists():
        print("No data/papers directory yet; schema is valid JSON and there are no records to check.")
        return 0

    paths = sorted(PAPERS_DIR.glob("*.json"))
    errors = 0
    seen_ids: set[str] = set()

    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"ERROR {path}: invalid JSON: {exc}")
            errors += 1
            continue

        record_id = record.get("id")
        if record_id in seen_ids:
            print(f"ERROR {path}: duplicate id {record_id!r}")
            errors += 1
        elif isinstance(record_id, str):
            seen_ids.add(record_id)

        record_errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
        for error in record_errors:
            where = ".".join(str(part) for part in error.path) or "<root>"
            print(f"ERROR {path}:{where}: {error.message}")
            errors += 1

    if errors:
        print(f"Validation failed with {errors} error(s).")
        return 1

    print(f"Validated {len(paths)} paper record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
