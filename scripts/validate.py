#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
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
