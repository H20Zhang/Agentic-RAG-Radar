#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_records() -> list[dict[str, object]]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data" / "papers").glob("*.json"))]


def note_path(record: dict[str, object]) -> Path:
    visual = record["visual_explainer"]
    assert isinstance(visual, dict)
    return ROOT / str(visual["artifact_path"])


def repair_notes(records: list[dict[str, object]]) -> None:
    for record in records:
        path = note_path(record)
        text = path.read_text(encoding="utf-8")
        analysis = record["analysis"]
        assert isinstance(analysis, dict)
        changed = False

        if "## Agent loop" not in text and "## Control flow" not in text:
            loop = str(analysis.get("agent_loop") or "").strip()
            if loop:
                marker = "## Retrieval design\n"
                block = f"## Agent loop\n\n`{loop}`\n\n"
                if marker in text:
                    text = text.replace(marker, block + marker, 1)
                else:
                    marker = "## Compared to what\n"
                    if marker in text:
                        text = text.replace(marker, block + marker, 1)
                changed = True

        if "## Retrieval design" not in text:
            design = str(analysis.get("retrieval_design") or "").strip()
            if design:
                marker = "## Compared to what\n"
                block = f"## Retrieval design\n\n{design}\n\n"
                if marker in text:
                    text = text.replace(marker, block + marker, 1)
                    changed = True

        if changed:
            path.write_text(text, encoding="utf-8")


def repair_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    old_nav = "**Last updated:** 2026-08-18 · [Latest papers](#-latest-papers) · [What’s changing](#-whats-changing) · [Reading paths](#-reading-paths) · [Research map](#-research-map)"
    new_nav = old_nav + " · [Paper index](papers/README.md)"
    if old_nav in text and "[Paper index](papers/README.md)" not in text:
        text = text.replace(old_nav, new_nav, 1)

    map_link = "[Explore the full research map →](categories/README.md)"
    index_link = "[Browse the complete Curated Paper Index →](papers/README.md)"
    if map_link in text and index_link not in text:
        text = text.replace(map_link, map_link + " · " + index_link, 1)
    path.write_text(text, encoding="utf-8")


def repair_categories() -> None:
    category_dir = ROOT / "categories"
    nav = "[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)"
    for path in sorted(category_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if path.name == "README.md":
            text = text.replace("# Browse Agentic RAG by Research Problem", "# Research Map", 1)
            if "[Curated Paper Index](../papers/README.md)" not in text:
                lines = text.splitlines()
                lines.insert(2, "[Latest Papers](../README.md#-latest-papers) · [What's Changing](../README.md#-whats-changing) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)")
                text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
        else:
            if "../papers/README.md" not in text:
                lines = text.splitlines()
                insert_at = 2 if len(lines) >= 2 else len(lines)
                lines.insert(insert_at, nav)
                text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
        path.write_text(text, encoding="utf-8")

    retrieval = category_dir / "retrieval-tool-use.md"
    text = retrieval.read_text(encoding="utf-8")
    marker = "## Current papers\n"
    additions = []
    if "../papers/2602.03442.md" not in text:
        additions.append(
            "### [A-RAG](../papers/2602.03442.md) — ★★★★☆\n\n"
            "**Design point:** expose keyword search, semantic search, and chunk reads as a model-controlled retrieval-operation hierarchy rather than a fixed pipeline.\n"
        )
    if "../papers/2608.01565.md" not in text:
        additions.append(
            "### [DocNavRAG](../papers/2608.01565.md) — ★★★★☆\n\n"
            "**Design point:** couple document-native navigation with explicit collected/missing evidence state so structure and retrieval control evolve together.\n"
        )
    if additions and marker in text:
        text = text.replace(marker, marker + "\n" + "\n".join(additions) + "\n", 1)
        retrieval.write_text(text, encoding="utf-8")


def main() -> None:
    records = load_records()
    repair_notes(records)
    repair_readme()
    repair_categories()


if __name__ == "__main__":
    main()
