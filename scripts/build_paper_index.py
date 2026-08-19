#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "data" / "papers"
OUTPUT = ROOT / "papers" / "README.md"
TAXONOMY = ROOT / "taxonomy.yaml"


def load_category_labels() -> dict[str, str]:
    labels: dict[str, str] = {}
    in_primary = False
    current: str | None = None
    for raw in TAXONOMY.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line == "primary_categories:":
            in_primary = True
            current = None
            continue
        if in_primary and line and not line.startswith(" "):
            break
        if not in_primary:
            continue
        if line.startswith("  ") and not line.startswith("    ") and line.endswith(":"):
            current = line.strip()[:-1]
            continue
        if current and line.startswith("    label:"):
            labels[current] = line.split(":", 1)[1].strip()
    if not labels:
        raise RuntimeError("Could not parse primary category labels from taxonomy.yaml")
    return labels


def load_records() -> list[dict[str, object]]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(PAPERS_DIR.glob("*.json"))]


def category_slug(category: str) -> str:
    return category.replace("_", "-")


def review_level(record: dict[str, object]) -> str:
    provenance = record.get("provenance")
    return "Full text" if isinstance(provenance, dict) and provenance.get("full_text_checked") is True else "Abstract"


def note_filename(record: dict[str, object]) -> str:
    visual = record.get("visual_explainer")
    if isinstance(visual, dict):
        artifact = visual.get("artifact_path")
        if isinstance(artifact, str) and artifact.startswith("papers/"):
            return Path(artifact).name
    arxiv_id = record.get("arxiv_id")
    if isinstance(arxiv_id, str) and arxiv_id:
        return f"{arxiv_id}.md"
    raise RuntimeError(f"Cannot determine note filename for {record.get('id')}")


def paper_cell(record: dict[str, object]) -> str:
    title = str(record["title"]).replace("|", "\\|")
    note = note_filename(record)
    urls = record.get("urls")
    assert isinstance(urls, dict)
    links = [f"[paper]({urls['paper']})"]
    code = urls.get("code")
    project = urls.get("project")
    if isinstance(code, str) and code:
        links.append(f"[code]({code})")
    elif isinstance(project, str) and project:
        links.append(f"[project]({project})")
    return f"**[{title}]({note})**<br><sub>{' · '.join(links)}</sub>"


def render_month(records: list[dict[str, object]], labels: dict[str, str]) -> list[str]:
    lines = ["| Date | Paper | Area | Importance | Review |", "|---|---|---|---:|---|"]
    for record in records:
        category = str(record["primary_category"])
        lines.append(
            "| {date} | {paper} | {area} | {importance}/5 | {review} |".format(
                date=str(record["published"]),
                paper=paper_cell(record),
                area=labels.get(category, category).replace("|", "\\|"),
                importance=int(record["importance"]),
                review=review_level(record),
            )
        )
    return lines + [""]


def render() -> str:
    labels = load_category_labels()
    records = load_records()
    records.sort(key=lambda r: (str(r["published"]), str(r["title"])), reverse=True)

    by_year: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        year, month, _ = str(record["published"]).split("-", 2)
        by_year[year][month].append(record)

    years = sorted(by_year, reverse=True)
    current_year = years[0] if years else None
    month_names = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December",
    }

    category_links = " · ".join(
        f"[{label}](../categories/{category_slug(key)}.md)" for key, label in labels.items()
    )

    out = [
        "# Curated Paper Index",
        "",
        "A compact chronology of papers **accepted by Agentic RAG Radar**. This is a selective research index, not a claim of exhaustive field coverage.",
        "",
        "[Latest Papers](../README.md#latest-papers) · [What's Changing](../README.md#whats-changing) · [Reading Paths](../README.md#reading-paths) · [Research Map](../categories/README.md)",
        "",
        f"**Browse by canonical area:** {category_links}",
        "",
        "The index is deliberately terse: use a paper title for the deep research note, or the Research Map when you want the field-level argument.",
        "",
    ]

    for year in years:
        months = sorted(by_year[year], reverse=True)
        if year == current_year:
            out.extend([f"## {year}", ""])
            for month in months:
                out.extend([f"### {month_names[month]}", ""])
                out.extend(render_month(by_year[year][month], labels))
        else:
            out.extend(["<details>", f"<summary><strong>{year}</strong></summary>", ""])
            for month in months:
                out.extend([f"### {month_names[month]}", ""])
                out.extend(render_month(by_year[year][month], labels))
            out.extend(["</details>", ""])

    out.extend([
        "---", "",
        "Generated deterministically from `data/papers/*.json`. Research judgments remain in the paper notes, synthesis, and Research Map.", "",
    ])
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the curated paper index from canonical records.")
    parser.add_argument("--check", action="store_true", help="Fail if papers/README.md differs from generated output.")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.exists():
            print(f"ERROR missing generated index: {OUTPUT.relative_to(ROOT)}")
            return 1
        actual = OUTPUT.read_text(encoding="utf-8")
        if actual != expected:
            print("ERROR papers/README.md is stale; run: python scripts/build_paper_index.py")
            return 1
        print("Curated Paper Index is up to date.")
        return 0
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
