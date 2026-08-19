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
    records: list[dict[str, object]] = []
    for path in sorted(PAPERS_DIR.glob("*.json")):
        records.append(json.loads(path.read_text(encoding="utf-8")))
    return records


def category_slug(category: str) -> str:
    return category.replace("_", "-")


def stars(importance: int) -> str:
    return "★" * importance + "☆" * (5 - importance)


def evidence_basis(record: dict[str, object]) -> str:
    provenance = record.get("provenance")
    if isinstance(provenance, dict) and provenance.get("full_text_checked") is True:
        return "full-text reviewed"
    return "abstract-level"


def render_entry(record: dict[str, object], labels: dict[str, str]) -> list[str]:
    published = str(record["published"])
    title = str(record["title"])
    category = str(record["primary_category"])
    importance = int(record["importance"])
    visual = record.get("visual_explainer")
    takeaway = ""
    if isinstance(visual, dict):
        takeaway = str(visual.get("takeaway") or "").strip()

    urls = record.get("urls")
    assert isinstance(urls, dict)
    paper_url = str(urls["paper"])
    note_id = Path(str(record["id"]).replace("arxiv:", "")).name
    arxiv_id = record.get("arxiv_id")
    if isinstance(arxiv_id, str) and arxiv_id:
        note_id = arxiv_id
    elif str(record["id"]).startswith("arxiv:"):
        note_id = str(record["id"]).split(":", 1)[1]
    else:
        # Non-arXiv records use the canonical artifact filename convention.
        artifact = visual.get("artifact_path") if isinstance(visual, dict) else None
        if isinstance(artifact, str) and artifact.startswith("papers/"):
            note_id = Path(artifact).stem

    lines = [
        f"#### {published} · [{title}]({note_id}.md)",
        f"`{labels.get(category, category)}` · **{stars(importance)}**",
        "",
    ]
    if takeaway:
        lines.extend([f"**Research delta.** {takeaway}", ""])
    lines.extend([f"**Evidence basis.** {evidence_basis(record)}", ""])

    link_parts = [f"[Paper]({paper_url})", f"[Research note]({note_id}.md)"]
    code = urls.get("code")
    project = urls.get("project")
    if isinstance(code, str) and code:
        link_parts.append(f"[Code]({code})")
    if isinstance(project, str) and project:
        link_parts.append(f"[Project]({project})")
    lines.extend([" · ".join(link_parts), ""])
    return lines


def render() -> str:
    labels = load_category_labels()
    records = load_records()

    records.sort(key=lambda r: (str(r["published"]), str(r["title"])), reverse=True)
    by_year: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        published = str(record["published"])
        year, month, _ = published.split("-", 2)
        by_year[year][month].append(record)

    years = sorted(by_year, reverse=True)
    current_year = years[0] if years else None

    out = [
        "# Curated Paper Index",
        "",
        "A complete chronology of papers **accepted by Agentic RAG Radar**. This is a curated research index, not a claim of exhaustive coverage of all Agentic RAG literature.",
        "",
        "Use [Latest Papers](../README.md#-latest-papers) for the newest high-priority work, [What's Changing](../README.md#-whats-changing) for synthesis, [Reading Paths](../README.md#-reading-paths) for guided study, and the [Research Map](../categories/README.md) for problem-oriented browsing.",
        "",
        "## Browse by Research Problem",
        "",
    ]

    for key, label in labels.items():
        out.append(f"- [{label}](../categories/{category_slug(key)}.md)")

    out.extend(["", "## Chronology", ""])

    month_names = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    for year in years:
        months = sorted(by_year[year], reverse=True)
        if year == current_year:
            out.extend([f"## {year}", ""])
            for month in months:
                out.extend([f"### {month_names[month]}", ""])
                for record in by_year[year][month]:
                    out.extend(render_entry(record, labels))
        else:
            out.extend(["<details>", f"<summary><strong>{year}</strong></summary>", ""])
            for month in months:
                out.extend([f"### {month_names[month]}", ""])
                for record in by_year[year][month]:
                    out.extend(render_entry(record, labels))
            out.extend(["</details>", ""])

    out.extend(
        [
            "---",
            "",
            "The index is generated deterministically from `data/papers/*.json`; research theses, category tensions, and reading paths remain human-edited and evidence-grounded.",
            "",
        ]
    )
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
