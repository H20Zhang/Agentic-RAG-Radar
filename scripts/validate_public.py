#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PAPERS_DIR = ROOT / "papers"
RECORDS_DIR = ROOT / "data" / "papers"
CATEGORIES_DIR = ROOT / "categories"

CATEGORY_FILES = {
    "planning_query_formulation": "planning-query-formulation.md",
    "retrieval_tool_use": "retrieval-tool-use.md",
    "iterative_reasoning_verification": "iterative-reasoning-verification.md",
    "multi_agent_orchestration": "multi-agent-orchestration.md",
    "learning_optimization": "learning-optimization.md",
    "evaluation_analysis": "evaluation-analysis.md",
}

EXPECTED_README_H2 = ["Latest Papers", "What's Changing", "Reading Paths", "Research Map"]
LATEST_CARD_RE = re.compile(r"^### \[(?P<title>.+?)\]\((?P<path>papers/[^)]+\.md)\)\s*$", re.MULTILINE)
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def normalize_heading(text: str) -> str:
    text = text.strip().replace("’", "'")
    text = re.sub(r"^[^\wA-Za-z]+", "", text).strip()
    return text


def load_records() -> list[dict[str, object]]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(RECORDS_DIR.glob("*.json"))]


def note_path(record: dict[str, object]) -> str:
    visual = record.get("visual_explainer")
    if isinstance(visual, dict):
        artifact = visual.get("artifact_path")
        if isinstance(artifact, str) and artifact:
            return artifact
    arxiv_id = record.get("arxiv_id")
    if isinstance(arxiv_id, str) and arxiv_id:
        return f"papers/{arxiv_id}.md"
    raise ValueError(f"Record {record.get('id')} has no artifact path")


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_readme(records: list[dict[str, object]], errors: list[str]) -> None:
    text = read(README)
    headings = [normalize_heading(m.group(1)) for m in re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE)]
    if len(headings) < len(EXPECTED_README_H2):
        add_error(errors, "README.md: missing required reader-facing H2 sections")
        return

    if headings[:4] != EXPECTED_README_H2:
        add_error(
            errors,
            "README.md: first four substantive H2 sections must be "
            + " -> ".join(EXPECTED_README_H2)
            + f"; found {headings[:4]!r}",
        )

    nav_needles = [
        "[Latest papers](#-latest-papers)",
        "[What’s changing](#-whats-changing)",
        "[Reading paths](#-reading-paths)",
        "[Research map](#-research-map)",
        "[Paper index](papers/README.md)",
    ]
    for needle in nav_needles:
        if needle not in text:
            add_error(errors, f"README.md: top navigation is missing {needle}")

    record_by_note = {note_path(record): record for record in records}
    latest_start = re.search(r"^##\s+[^\n]*Latest Papers\s*$", text, re.MULTILINE)
    changes_start = re.search(r"^##\s+[^\n]*What[’']s Changing\s*$", text, re.MULTILINE)
    if not latest_start or not changes_start or changes_start.start() <= latest_start.start():
        add_error(errors, "README.md: cannot isolate Latest Papers section")
        return

    latest = text[latest_start.end() : changes_start.start()]
    matches = list(LATEST_CARD_RE.finditer(latest))
    if not matches:
        add_error(errors, "README.md: Latest Papers has no recognizable paper cards")
        return

    dates: list[str] = []
    for i, match in enumerate(matches):
        rel = match.group("path")
        record = record_by_note.get(rel)
        if record is None:
            add_error(errors, f"README.md: Latest paper {rel} has no canonical record")
            continue
        note = ROOT / rel
        if not note.exists():
            add_error(errors, f"README.md: Latest paper note does not exist: {rel}")
        dates.append(str(record["published"]))

        card_end = matches[i + 1].start() if i + 1 < len(matches) else len(latest)
        card = latest[match.start() : card_end]
        fold_marker = "Understand this paper in 60 seconds"
        if card.count(fold_marker) != 1:
            add_error(errors, f"README.md:{rel}: expected exactly one 60-second fold")

        required = [
            "**Problem.",
            "**Core mechanism.",
            "**Compared with.",
            "**Evidence to remember.",
            "**Open question.",
        ]
        for label in required:
            if label not in card:
                add_error(errors, f"README.md:{rel}: 60-second fold missing {label}")

        analysis = record.get("analysis")
        if isinstance(analysis, dict) and str(analysis.get("agent_loop") or "").strip():
            if "**Agent loop." not in card and "**Control flow." not in card:
                add_error(errors, f"README.md:{rel}: fold missing Agent loop/control flow")

        visual = record.get("visual_explainer")
        if isinstance(visual, dict) and visual.get("status") == "generated":
            image_path = visual.get("image_path")
            if not isinstance(image_path, str) or image_path not in card:
                add_error(errors, f"README.md:{rel}: generated visual is not embedded in Latest fold")
            for label in ["**How to read this figure.**", "**Do not over-read.**"]:
                if label not in card:
                    add_error(errors, f"README.md:{rel}: generated visual lacks {label}")
            problem_pos = card.find("**Problem.")
            image_pos = card.find(str(image_path)) if isinstance(image_path, str) else -1
            if problem_pos >= 0 and (image_pos < 0 or image_pos > problem_pos):
                add_error(errors, f"README.md:{rel}: generated visual must appear before Problem")

    if dates != sorted(dates, reverse=True):
        add_error(errors, f"README.md: Latest Papers are not in non-increasing publication order: {dates}")

    forbidden = [
        "needs_regeneration",
        "status=pending",
        "backfill queue",
        "renderer failure",
        "scheduler mechanics",
    ]
    lower = text.lower()
    for phrase in forbidden:
        if phrase.lower() in lower:
            add_error(errors, f"README.md: public surface exposes internal phrase {phrase!r}")

    stale_headings = {"Start Here", "Research Compactions"}
    for heading in headings:
        if heading in stale_headings:
            add_error(errors, f"README.md: stale public section name {heading!r}")


def check_paper_notes(records: list[dict[str, object]], errors: list[str]) -> None:
    required_sections = [
        "Problem",
        "Core idea",
        "Retrieval design",
        "Compared to what",
        "Evidence",
        "Why it matters",
    ]
    for record in records:
        rel = note_path(record)
        path = ROOT / rel
        if not path.exists():
            add_error(errors, f"{rel}: canonical paper note is missing")
            continue
        text = read(path)
        if "**TL;DR." not in text:
            add_error(errors, f"{rel}: missing TL;DR")
        headings = [normalize_heading(m.group(1)).lower() for m in re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE)]
        for section in required_sections:
            if section.lower() not in headings:
                add_error(errors, f"{rel}: missing ## {section}")
        if not any(h.startswith("limitations") for h in headings):
            add_error(errors, f"{rel}: missing limitations/questions section")

        analysis = record.get("analysis")
        if isinstance(analysis, dict) and str(analysis.get("agent_loop") or "").strip():
            if not any(h in {"agent loop", "control flow"} for h in headings):
                add_error(errors, f"{rel}: missing Agent loop/control flow section")


def check_categories(records: list[dict[str, object]], errors: list[str]) -> None:
    for record in records:
        category = str(record["primary_category"])
        filename = CATEGORY_FILES.get(category)
        if not filename:
            add_error(errors, f"{record.get('id')}: unknown primary category {category}")
            continue
        path = CATEGORIES_DIR / filename
        if not path.exists():
            add_error(errors, f"categories/{filename}: missing primary category page")
            continue
        text = read(path)
        rel_note = "../" + note_path(record)
        if rel_note not in text:
            add_error(errors, f"categories/{filename}: missing link to {rel_note}")

    for filename in CATEGORY_FILES.values():
        path = CATEGORIES_DIR / filename
        if not path.exists():
            continue
        text = read(path)
        if "**Core question:**" not in text:
            add_error(errors, f"categories/{filename}: missing Core question")
        if "../papers/README.md" not in text:
            add_error(errors, f"categories/{filename}: missing Curated Paper Index navigation")
        if "README.md" not in text:
            add_error(errors, f"categories/{filename}: missing Research Map/home navigation")


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if target.startswith("../../issues/") or target.startswith("/issues/"):
        return None
    if " " in target and not target.startswith("<"):
        # Markdown titles are outside this repository's public-link convention.
        target = target.split(" ", 1)[0]
    target = target.strip("<>")
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    target = unquote(target)
    return (source.parent / target).resolve()


def check_links(errors: list[str]) -> None:
    paths: set[Path] = {README, ROOT / "CONTRIBUTING.md", PAPERS_DIR / "README.md", CATEGORIES_DIR / "README.md", ROOT / "digests" / "README.md"}
    paths.update(PAPERS_DIR.glob("*.md"))
    paths.update(CATEGORIES_DIR.glob("*.md"))
    for rel in ["digests/weekly/2026-W34.md", "digests/monthly/2026-08.md", "digests/yearly/2026.md"]:
        path = ROOT / rel
        if path.exists():
            paths.add(path)

    root_resolved = ROOT.resolve()
    for source in sorted(paths):
        if not source.exists():
            continue
        text = read(source)
        for raw in MD_LINK_RE.findall(text):
            target = local_link_target(source, raw)
            if target is None:
                continue
            try:
                target.relative_to(root_resolved)
            except ValueError:
                add_error(errors, f"{source.relative_to(ROOT)}: local link escapes repository: {raw}")
                continue
            if not target.exists():
                add_error(errors, f"{source.relative_to(ROOT)}: broken local link: {raw}")


def check_contract_drift(errors: list[str]) -> None:
    template = read(ROOT / "templates" / "paper.md")
    if ".webp" not in template or "**How to read this figure.**" not in template or "**Do not over-read.**" not in template:
        add_error(errors, "templates/paper.md: does not match the live visual reader contract")

    visual_readme = read(ROOT / "assets" / "visuals" / "README.md")
    for needle in ["assets/visuals/masters/<paper-id>.png", "assets/visuals/<paper-id>.webp", "How to read this figure"]:
        if needle not in visual_readme:
            add_error(errors, f"assets/visuals/README.md: missing active visual contract marker {needle!r}")


def main() -> int:
    errors: list[str] = []
    records = load_records()
    check_readme(records, errors)
    check_paper_notes(records, errors)
    check_categories(records, errors)
    check_links(errors)
    check_contract_drift(errors)

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"Public-surface validation failed with {len(errors)} error(s).")
        return 1

    print(f"Validated public research surfaces for {len(records)} accepted paper record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
