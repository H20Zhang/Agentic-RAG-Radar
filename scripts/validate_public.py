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


def latest_records(text: str, records: list[dict[str, object]]) -> tuple[list[re.Match[str]], dict[str, dict[str, object]], str]:
    record_by_note = {note_path(record): record for record in records}
    latest_start = re.search(r"^##\s+Latest Papers\s*$", text, re.MULTILINE)
    changes_start = re.search(r"^##\s+What[’']s Changing\s*$", text, re.MULTILINE)
    if not latest_start or not changes_start or changes_start.start() <= latest_start.start():
        return [], record_by_note, ""
    latest = text[latest_start.end():changes_start.start()]
    return list(LATEST_CARD_RE.finditer(latest)), record_by_note, latest


def check_readme(records: list[dict[str, object]], errors: list[str]) -> set[str]:
    text = read(README)
    headings = [normalize_heading(m.group(1)) for m in re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE)]
    if len(headings) < 4 or headings[:4] != EXPECTED_README_H2:
        add_error(errors, "README.md: first four H2 sections must be " + " -> ".join(EXPECTED_README_H2) + f"; found {headings[:4]!r}")

    nav_needles = [
        "[Latest Papers](#latest-papers)",
        "[What's Changing](#whats-changing)",
        "[Reading Paths](#reading-paths)",
        "[Research Map](#research-map)",
        "[Paper Index](papers/README.md)",
    ]
    for needle in nav_needles:
        if needle not in text:
            add_error(errors, f"README.md: top navigation is missing {needle}")

    if "assets/editorial/field-overview.svg" not in text:
        add_error(errors, "README.md: missing field-overview research visual")
    if "assets/editorial/research-question-map.svg" not in text:
        add_error(errors, "README.md: missing Research Map visual")

    matches, record_by_note, latest = latest_records(text, records)
    if not matches:
        add_error(errors, "README.md: Latest Papers has no recognizable paper cards")
        return set()

    dates: list[str] = []
    latest_note_paths: set[str] = set()
    for i, match in enumerate(matches):
        rel = match.group("path")
        latest_note_paths.add(rel)
        record = record_by_note.get(rel)
        if record is None:
            add_error(errors, f"README.md: Latest paper {rel} has no canonical record")
            continue
        if not (ROOT / rel).exists():
            add_error(errors, f"README.md: Latest paper note does not exist: {rel}")
        dates.append(str(record["published"]))

        card_end = matches[i + 1].start() if i + 1 < len(matches) else len(latest)
        card = latest[match.start():card_end]
        for label in ["**Why it matters.**", "**Key result.**", "**The catch.**"]:
            if label not in card:
                add_error(errors, f"README.md:{rel}: latest card missing {label}")
        if card.count("Research snapshot") != 1:
            add_error(errors, f"README.md:{rel}: expected exactly one Research snapshot fold")
        for label in ["**Research question.**", "**Mechanism.**", "**Nearest design point.**", "**Evidence & attribution.**", "**Open question.**"]:
            if label not in card:
                add_error(errors, f"README.md:{rel}: Research snapshot missing {label}")

        visual = record.get("visual_explainer")
        if isinstance(visual, dict) and visual.get("status") == "generated":
            image_path = visual.get("image_path")
            if not isinstance(image_path, str) or image_path not in card:
                add_error(errors, f"README.md:{rel}: canonical generated visual is not embedded in Latest card/fold")
            for label in ["**How to read this figure.**", "**Do not over-read.**"]:
                if label not in card:
                    add_error(errors, f"README.md:{rel}: canonical generated visual lacks {label}")

    if dates != sorted(dates, reverse=True):
        add_error(errors, f"README.md: Latest Papers are not in non-increasing publication order: {dates}")

    if "AI take" in text:
        add_error(errors, "README.md: use researcher-facing verdict language instead of 'AI take'")
    if "★" in text or "☆" in text:
        add_error(errors, "README.md: star-glyph importance ratings are not allowed on the primary research surface")

    forbidden = ["needs_regeneration", "status=pending", "backfill queue", "renderer failure", "scheduler mechanics"]
    lower = text.lower()
    for phrase in forbidden:
        if phrase.lower() in lower:
            add_error(errors, f"README.md: public surface exposes internal phrase {phrase!r}")

    return latest_note_paths


def check_paper_notes(records: list[dict[str, object]], latest_notes: set[str], errors: list[str]) -> None:
    legacy_required = ["Problem", "Core idea", "Compared to what", "Evidence", "Why it matters"]
    editorial_required = ["Research question", "Research delta", "Mechanism", "Evidence & attribution", "Where it fits", "Open question"]

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
        if rel in latest_notes:
            for section in editorial_required:
                if section.lower() not in headings:
                    add_error(errors, f"{rel}: current Latest note missing ## {section}")
            for label in ["**Why this paper matters**", "**Strongest evidence**", "**Biggest caveat**"]:
                if label not in text:
                    add_error(errors, f"{rel}: current Latest note missing 30-second verdict field {label}")
        else:
            # Older notes can keep the legacy deep structure while they are progressively migrated.
            if not any(section.lower() in headings for section in editorial_required):
                for section in legacy_required:
                    if section.lower() not in headings:
                        add_error(errors, f"{rel}: legacy note missing ## {section}")

        visual = record.get("visual_explainer")
        if isinstance(visual, dict):
            status = visual.get("status")
            if status != "generated" and re.search(r"^##\s+Visual explainer\s*$", text, re.MULTILINE):
                add_error(errors, f"{rel}: incomplete visual state must not appear as a public Visual explainer section")
            if status == "generated":
                image_path = visual.get("image_path")
                if isinstance(image_path, str) and image_path not in text:
                    add_error(errors, f"{rel}: canonical generated visual is not embedded")
                for label in ["**How to read this figure.**", "**Do not over-read.**"]:
                    if label not in text:
                        add_error(errors, f"{rel}: canonical generated visual lacks {label}")


def check_research_map(records: list[dict[str, object]], errors: list[str]) -> None:
    map_path = CATEGORIES_DIR / "README.md"
    text = read(map_path)
    if "## Live Research Questions" not in text:
        add_error(errors, "categories/README.md: Research Map must be research-question-first")
    for question in [
        "Where should adaptivity live?",
        "When should evidence be materialized?",
        "What state should persist?",
        "How should retrieval expose the corpus?",
        "What should be learned?",
        "What makes an evaluation causal?",
    ]:
        if question not in text:
            add_error(errors, f"categories/README.md: missing live research question {question!r}")
    if "../assets/editorial/research-question-map.svg" not in text:
        add_error(errors, "categories/README.md: missing research-question map visual")

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
        category_text = read(path)
        rel_note = "../" + note_path(record)
        if rel_note not in category_text:
            add_error(errors, f"categories/{filename}: missing link to {rel_note}")

    for filename in CATEGORY_FILES.values():
        path = CATEGORIES_DIR / filename
        if not path.exists():
            continue
        category_text = read(path)
        if "**Core question:**" not in category_text:
            add_error(errors, f"categories/{filename}: missing Core question")
        if "../papers/README.md" not in category_text:
            add_error(errors, f"categories/{filename}: missing Curated Paper Index navigation")


def check_paper_index(errors: list[str]) -> None:
    path = PAPERS_DIR / "README.md"
    if not path.exists():
        add_error(errors, "papers/README.md: generated index is missing")
        return
    text = read(path)
    if "| Date | Paper | Area | Importance | Review |" not in text:
        add_error(errors, "papers/README.md: index is not using the compact chronology table")
    if "**Research delta.**" in text:
        add_error(errors, "papers/README.md: lookup index should not repeat research-delta prose")
    if "★" in text or "☆" in text:
        add_error(errors, "papers/README.md: use textual importance rather than star glyphs")


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if target.startswith("../../issues/") or target.startswith("/issues/"):
        return None
    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]
    target = target.strip("<>")
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    return (source.parent / unquote(target)).resolve()


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
    for needle in ["## Research question", "## Research delta", "## Evidence & attribution", "## Where it fits", "## Open question", "How to read this figure", "Do not over-read"]:
        if needle not in template:
            add_error(errors, f"templates/paper.md: missing editorial contract marker {needle!r}")
    if "pending or needs regeneration" in template.lower() or "pointing to the grounded brief" in template.lower():
        add_error(errors, "templates/paper.md: must not teach public visual-placeholder behavior")

    visual_readme = read(ROOT / "assets" / "visuals" / "README.md")
    for needle in ["assets/visuals/masters/<paper-id>.png", "assets/visuals/<paper-id>.webp", "How to read this figure"]:
        if needle not in visual_readme:
            add_error(errors, f"assets/visuals/README.md: missing active visual contract marker {needle!r}")


def main() -> int:
    errors: list[str] = []
    records = load_records()
    latest_notes = check_readme(records, errors)
    check_paper_notes(records, latest_notes, errors)
    check_research_map(records, errors)
    check_paper_index(errors)
    check_links(errors)
    check_contract_drift(errors)

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"Public-surface validation failed with {len(errors)} error(s).")
        return 1

    print(f"Validated polished public research surfaces for {len(records)} accepted paper record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
