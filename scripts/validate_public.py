#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from build_paper_index import render as render_paper_index
from timefirst_contract import strip_html_comments, validate_pair
from validate_reading import validate_rag_timeline

ROOT = Path(__file__).resolve().parents[1]
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README.en.md"
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
ENTRY_ANCHOR_RE = re.compile(r'<a\s+id=["\']entry-([^"\']+)["\']\s*></a>', re.I)
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def normalize_heading(text: str) -> str:
    text = text.strip().replace("’", "'")
    return re.sub(r"^[^\wA-Za-z]+", "", text).strip()


def load_records() -> list[dict[str, object]]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(RECORDS_DIR.glob("*.json"))
    ]


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


def timeline_records(
    text: str,
    records: list[dict[str, object]],
    language: str,
    errors: list[str],
) -> tuple[list[str], set[str]]:
    start = text.find('<a id="timeline"></a>')
    end = text.find('<a id="periods"></a>')
    if start < 0 or end <= start:
        add_error(errors, f"{language}: cannot locate Timeline boundaries")
        return [], set()

    timeline = text[start:end]
    anchors = list(ENTRY_ANCHOR_RE.finditer(timeline))
    record_by_arxiv = {
        str(record.get("arxiv_id")): record
        for record in records
        if isinstance(record.get("arxiv_id"), str)
    }
    identities: list[str] = []
    note_paths: set[str] = set()
    for index, anchor in enumerate(anchors):
        identity = anchor.group(1)
        identities.append(identity)
        chunk_end = anchors[index + 1].start() if index + 1 < len(anchors) else len(timeline)
        chunk = timeline[anchor.end():chunk_end]
        record = record_by_arxiv.get(identity)
        if record is None:
            add_error(errors, f"{language}: Timeline identity {identity} has no canonical record")
            continue
        title = str(record.get("title", ""))
        summary_end = chunk.find("</summary>")
        expanded = chunk[summary_end + len("</summary>"):] if summary_end >= 0 else ""
        urls = record.get("urls")
        primary = urls.get("paper") if isinstance(urls, dict) else None
        canonical_title_link = (
            f"[{title}]({primary})" if isinstance(primary, str) and primary else None
        )
        if (
            canonical_title_link is None
            or strip_html_comments(expanded).count(canonical_title_link) != 1
        ):
            add_error(
                errors,
                f"{language}: Timeline identity {identity} is missing its canonical title link",
            )
        path = note_path(record)
        note_paths.add(path)
        if f"]({path})" not in chunk or f"](papers/{identity}.zh.md)" not in chunk:
            add_error(errors, f"{language}: Timeline identity {identity} is missing its paired deep-note links")
    return identities, note_paths


def check_readmes(
    records: list[dict[str, object]],
    errors: list[str],
) -> set[str]:
    zh = read(README_ZH)
    en = read(README_EN)
    errors.extend(validate_pair(zh, en))
    errors.extend(validate_rag_timeline(zh, en, records))

    zh_ids, zh_notes = timeline_records(zh, records, "README.md", errors)
    en_ids, en_notes = timeline_records(en, records, "README.en.md", errors)
    if zh_ids != en_ids or zh_notes != en_notes:
        add_error(errors, "Chinese/English Timeline canonical identity or note-set drift")

    nav_targets = ("#timeline", "#periods", "#field-map", "#reading-paths", "#library")
    for path, text in ((README_ZH, zh), (README_EN, en)):
        for target in nav_targets:
            if f"]({target})" not in text:
                add_error(errors, f"{path.name}: top navigation is missing {target}")
        for asset in (
            "assets/editorial/field-overview.svg",
            "assets/editorial/research-question-map.svg",
        ):
            if asset not in text:
                add_error(errors, f"{path.name}: missing research visual {asset}")

        lower = text.lower()
        for phrase in (
            "needs_regeneration",
            "status=pending",
            "backfill queue",
            "renderer failure",
            "scheduler mechanics",
            "abstract_only",
        ):
            if phrase in lower:
                add_error(errors, f"{path.name}: public surface exposes internal phrase {phrase!r}")
        if "AI take" in text:
            add_error(errors, f"{path.name}: use researcher-facing verdict language instead of 'AI take'")
        if "★" in text or "☆" in text:
            add_error(errors, f"{path.name}: star-glyph ratings are not allowed on the primary surface")
    return zh_notes


def check_paper_notes(
    records: list[dict[str, object]],
    timeline_notes: set[str],
    errors: list[str],
) -> None:
    legacy_required = ("Problem", "Core idea", "Compared to what", "Evidence", "Why it matters")
    editorial_required = (
        "Research question",
        "Research delta",
        "Mechanism",
        "Evidence & attribution",
        "Where it fits",
        "Open question",
    )
    chinese_required = (
        "Problem",
        "Mechanism",
        "Closest comparison",
        "Decisive evidence",
        "What remains unproven",
        "Field-map consequence",
        "Related reading",
    )

    for record in records:
        rel = note_path(record)
        path = ROOT / rel
        if not path.exists():
            add_error(errors, f"{rel}: canonical paper note is missing")
            continue
        text = read(path)
        if "**TL;DR." not in text:
            add_error(errors, f"{rel}: missing TL;DR")

        headings = [
            normalize_heading(match.group(1)).lower()
            for match in re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE)
        ]
        if rel in timeline_notes:
            for section in editorial_required:
                if section.lower() not in headings:
                    add_error(errors, f"{rel}: Timeline deep note missing ## {section}")
            for label in (
                "**Why this paper matters**",
                "**Strongest evidence**",
                "**Biggest caveat**",
            ):
                if label not in text:
                    add_error(errors, f"{rel}: Timeline deep note missing verdict field {label}")

            identity = str(record.get("arxiv_id"))
            zh_rel = f"papers/{identity}.zh.md"
            zh_path = ROOT / zh_rel
            if not zh_path.exists():
                add_error(errors, f"{zh_rel}: paired Chinese deep note is missing")
            else:
                zh_text = read(zh_path)
                zh_headings = [
                    normalize_heading(match.group(1)).lower()
                    for match in re.finditer(r"^##\s+(.+?)\s*$", zh_text, re.MULTILINE)
                ]
                for section in chinese_required:
                    if section == "Mechanism":
                        present = any("mechanism" in heading for heading in zh_headings)
                    else:
                        present = any(heading.startswith(section.lower()) for heading in zh_headings)
                    if not present:
                        add_error(errors, f"{zh_rel}: paired deep note missing ## {section}")
        elif not any(section.lower() in headings for section in editorial_required):
            for section in legacy_required:
                if section.lower() not in headings:
                    add_error(errors, f"{rel}: legacy note missing ## {section}")

        visual = record.get("visual_explainer")
        if not isinstance(visual, dict):
            continue
        status = visual.get("status")
        if status != "generated" and re.search(r"^##\s+Visual explainer\s*$", text, re.MULTILINE):
            add_error(errors, f"{rel}: incomplete visual state appears as a public Visual explainer")
        if status == "generated":
            image_path = visual.get("image_path")
            if isinstance(image_path, str) and image_path not in text:
                add_error(errors, f"{rel}: canonical generated visual is not embedded")
            for label in ("**How to read this figure.**", "**Do not over-read.**"):
                if label not in text:
                    add_error(errors, f"{rel}: canonical generated visual lacks {label}")


def check_research_map(records: list[dict[str, object]], errors: list[str]) -> None:
    zh_path = CATEGORIES_DIR / "README.md"
    en_path = CATEGORIES_DIR / "README.en.md"
    for path in (zh_path, en_path):
        if not path.exists():
            add_error(errors, f"{path.relative_to(ROOT)}: Research Map is missing")
            return
    zh = read(zh_path)
    en = read(en_path)

    zh_questions = (
        "Adaptivity 应该放在哪里",
        "Evidence 什么时候 materialize",
        "什么 state 值得持久化",
        "Retrieval 应如何暴露 corpus",
        "到底应该 learn 什么",
        "什么样的 evaluation 才 causal",
    )
    en_questions = (
        "Where should adaptivity live?",
        "When should evidence be materialized?",
        "What state should persist?",
        "How should retrieval expose the corpus?",
        "What should be learned?",
        "What makes an evaluation causal?",
    )
    for question in zh_questions:
        if question not in zh:
            add_error(errors, f"categories/README.md: missing live research question {question!r}")
    for question in en_questions:
        if question not in en:
            add_error(errors, f"categories/README.en.md: missing live research question {question!r}")

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
        rel_note = "../" + note_path(record)
        if rel_note not in read(path):
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
    if text != render_paper_index():
        add_error(errors, "papers/README.md: generated index is stale")
    if "| Date | Paper | Area | Importance | Review |" not in text:
        add_error(errors, "papers/README.md: index is not using the compact chronology table")
    for target in ("#timeline", "#periods", "#reading-paths", "#field-map"):
        if f"../README.md{target}" not in text:
            add_error(errors, f"papers/README.md: navigation is missing {target}")
    if "**Research delta.**" in text:
        add_error(errors, "papers/README.md: lookup index repeats research-delta prose")
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
    paths: set[Path] = {
        README_ZH,
        README_EN,
        ROOT / "CONTRIBUTING.md",
        ROOT / "library" / "README.md",
        ROOT / "library" / "README.en.md",
        PAPERS_DIR / "README.md",
        CATEGORIES_DIR / "README.md",
        CATEGORIES_DIR / "README.en.md",
        ROOT / "digests" / "README.md",
    }
    paths.update(PAPERS_DIR.glob("*.md"))
    paths.update(CATEGORIES_DIR.glob("*.md"))
    paths.update((ROOT / "digests" / "weekly").glob("*.md"))
    paths.update((ROOT / "digests" / "monthly").glob("*.md"))
    paths.update((ROOT / "digests" / "yearly").glob("*.md"))

    root_resolved = ROOT.resolve()
    for source in sorted(paths):
        if not source.exists():
            continue
        for raw in MD_LINK_RE.findall(read(source)):
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
    for needle in (
        "## Research question",
        "## Research delta",
        "## Evidence & attribution",
        "## Where it fits",
        "## Open question",
        "How to read this figure",
        "Do not over-read",
    ):
        if needle not in template:
            add_error(errors, f"templates/paper.md: missing editorial contract marker {needle!r}")
    if (
        "pending or needs regeneration" in template.lower()
        or "pointing to the grounded brief" in template.lower()
    ):
        add_error(errors, "templates/paper.md: teaches public visual-placeholder behavior")

    visual_readme = read(ROOT / "assets" / "visuals" / "README.md")
    for needle in (
        "assets/visuals/masters/<paper-id>.png",
        "assets/visuals/<paper-id>.webp",
        "How to read this figure",
    ):
        if needle not in visual_readme:
            add_error(errors, f"assets/visuals/README.md: missing active visual marker {needle!r}")


def main() -> int:
    errors: list[str] = []
    records = load_records()
    timeline_notes = check_readmes(records, errors)
    check_paper_notes(records, timeline_notes, errors)
    check_research_map(records, errors)
    check_paper_index(errors)
    check_links(errors)
    check_contract_drift(errors)

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"Public-surface validation failed with {len(errors)} error(s).")
        return 1

    print(
        f"Validated time-first bilingual research surfaces for {len(records)} "
        "accepted paper record(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
