#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:
    raise SystemExit("Install dependencies with: pip install jsonschema pillow") from exc

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Install dependencies with: pip install jsonschema pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "data" / "paper.schema.json"
PAPERS_DIR = ROOT / "data" / "papers"
MIN_VISUAL_WIDTH = 1536
CUTOVER = datetime(2026, 8, 20, tzinfo=timezone.utc)
TIME_FIELDS = ("published_at", "first_seen_at", "radar_published_at")
V2_BUNDLE_FIELDS = (*TIME_FIELDS, "time_provenance", "map_delta")
MAP_DELTAS = {"none", "early_signal", "reinforces", "revises", "splits", "retires"}
STRICT_UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
STABLE_TOKEN_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def parse_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.strptime(value, STRICT_UTC_FORMAT).replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return parsed


def canonical_direction_keys(value: object) -> tuple[str, ...] | None:
    if not isinstance(value, list) or not value:
        return None
    if any(
        not isinstance(key, str) or STABLE_TOKEN_RE.fullmatch(key) is None
        for key in value
    ):
        return None
    keys = tuple(value)
    if len(keys) != len(set(keys)):
        return None
    return keys


def time_contract_errors(record: dict[str, object]) -> list[str]:
    """Validate v2 time/map semantics while preserving untouched legacy records."""

    errors: list[str] = []
    direction_keys_present = "direction_keys" in record
    if direction_keys_present and canonical_direction_keys(
        record.get("direction_keys")
    ) is None:
        errors.append(
            "direction_keys must be a non-empty list of unique lowercase stable tokens"
        )
    present = [field for field in V2_BUNDLE_FIELDS if field in record]
    if present and len(present) != len(V2_BUNDLE_FIELDS):
        for field in V2_BUNDLE_FIELDS:
            if field not in record:
                errors.append(f"partial v2 time/map migration is missing {field}")
        return errors

    if not present:
        if direction_keys_present:
            errors.append("direction_keys requires the complete native_v2 time contract")
        return errors

    provenance = record.get("time_provenance")
    if record.get("map_delta") not in MAP_DELTAS:
        errors.append("complete time/map bundle requires a valid map_delta")

    if provenance == "legacy_unknown":
        if direction_keys_present:
            errors.append(
                "direction_keys is native-v2 support metadata and is forbidden on "
                "explicit legacy records"
            )
        published_at = record.get("published_at")
        published = record.get("published")
        if published_at != published:
            errors.append("legacy_unknown published_at must equal published")
        for field in ("first_seen_at", "radar_published_at"):
            if record.get(field) is not None:
                errors.append(f"legacy_unknown {field} must be null")
        return errors

    if provenance != "native_v2":
        errors.append("complete time/map bundle requires time_provenance=native_v2 or legacy_unknown")
        return errors

    parsed = {field: parse_timestamp(record.get(field)) for field in TIME_FIELDS}
    radar = parsed["radar_published_at"]
    for field in TIME_FIELDS:
        if parsed[field] is None:
            errors.append(f"native_v2 {field} must be a full UTC timestamp ending in Z")
    if radar is not None and radar < CUTOVER:
        errors.append("native_v2 radar_published_at cannot predate v2 cutover")
    source_provenance = record.get("provenance")
    if not isinstance(source_provenance, dict) or source_provenance.get("full_text_checked") is not True:
        errors.append("native_v2 record requires provenance.full_text_checked=true")

    if all(parsed[field] is not None for field in TIME_FIELDS):
        published = parsed["published_at"]
        first_seen = parsed["first_seen_at"]
        radar = parsed["radar_published_at"]
        assert published is not None and first_seen is not None and radar is not None
        if not published <= first_seen <= radar:
            errors.append("v2 timestamps must satisfy published_at <= first_seen_at <= radar_published_at")
    return errors


def check_repo_path(record_path: Path, value: object, label: str, *, required: bool = True) -> int:
    if value is None:
        if required:
            print(f"ERROR {record_path}:{label}: path is null")
            return 1
        return 0
    if not isinstance(value, str) or not value.strip():
        print(f"ERROR {record_path}:{label}: expected non-empty repository-relative path")
        return 1
    target = ROOT / value
    if not target.exists():
        print(f"ERROR {record_path}:{label}: missing {value}")
        return 1
    return 0


def image_size(path: Path) -> tuple[int, int]:
    with Image.open(path) as image:
        return image.size


def check_generated_visual(record_path: Path, visual: dict[str, object]) -> int:
    errors = 0
    master_value = visual.get("master_image_path")
    display_value = visual.get("image_path")
    errors += check_repo_path(record_path, master_value, "visual_explainer.master_image_path")
    errors += check_repo_path(record_path, display_value, "visual_explainer.image_path")
    if errors:
        return errors

    assert isinstance(master_value, str)
    assert isinstance(display_value, str)
    master = ROOT / master_value
    display = ROOT / display_value

    if master.suffix.lower() != ".png":
        print(f"ERROR {record_path}:visual_explainer.master_image_path: generated master must be PNG")
        errors += 1
    if display.suffix.lower() != ".webp":
        print(f"ERROR {record_path}:visual_explainer.image_path: generated display asset must be WebP")
        errors += 1

    try:
        master_size = image_size(master)
        display_size = image_size(display)
    except Exception as exc:
        print(f"ERROR {record_path}:visual_explainer: unreadable image asset: {exc}")
        return errors + 1

    if display_size[0] < MIN_VISUAL_WIDTH:
        print(
            f"ERROR {record_path}:visual_explainer.image_path: "
            f"display width {display_size[0]}px is below {MIN_VISUAL_WIDTH}px"
        )
        errors += 1
    if master_size != display_size:
        print(
            f"ERROR {record_path}:visual_explainer: master/display dimensions differ "
            f"({master_size} vs {display_size}); WebP conversion must not resize"
        )
        errors += 1

    artifact_value = visual.get("artifact_path")
    if isinstance(artifact_value, str):
        artifact = ROOT / artifact_value
        if artifact.exists():
            text = artifact.read_text(encoding="utf-8")
            if display_value not in text and f"../{display_value}" not in text:
                print(f"ERROR {record_path}:visual_explainer: generated image is not embedded in {artifact_value}")
                errors += 1
            if "**How to read this figure.**" not in text:
                print(f"ERROR {record_path}:visual_explainer: paper note lacks figure-reading explanation")
                errors += 1

    return errors


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

        if record_errors:
            continue

        contract_errors = time_contract_errors(record)
        for error in contract_errors:
            print(f"ERROR {path}:time-contract: {error}")
            errors += 1

        visual = record["visual_explainer"]
        errors += check_repo_path(path, visual.get("prompt_path"), "visual_explainer.prompt_path")
        errors += check_repo_path(path, visual.get("artifact_path"), "visual_explainer.artifact_path")

        status = visual.get("status")
        if status == "generated":
            errors += check_generated_visual(path, visual)
        elif status in {"pending", "needs_regeneration"}:
            image_path = visual.get("image_path")
            if not isinstance(image_path, str) or not image_path.strip():
                print(f"ERROR {path}:visual_explainer.image_path: incomplete visuals need their intended display path")
                errors += 1

    if errors:
        print(f"Validation failed with {errors} error(s).")
        return 1

    print(f"Validated {len(paths)} paper record(s), including visual provenance and resolution contracts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
