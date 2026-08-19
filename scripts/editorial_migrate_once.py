#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean_incomplete_visual_sections() -> int:
    changed = 0
    for record_path in sorted((ROOT / "data" / "papers").glob("*.json")):
        record = json.loads(record_path.read_text(encoding="utf-8"))
        visual = record.get("visual_explainer")
        if not isinstance(visual, dict) or visual.get("status") == "generated":
            continue
        artifact = visual.get("artifact_path")
        if not isinstance(artifact, str):
            continue
        path = ROOT / artifact
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new = re.sub(
            r"\n## Visual explainer\s*\n.*?(?=\n##\s)",
            "\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    changed = clean_incomplete_visual_sections()
    subprocess.run(["python", "scripts/build_paper_index.py"], cwd=ROOT, check=True)
    print(f"Cleaned incomplete visual placeholders from {changed} paper note(s).")


if __name__ == "__main__":
    main()
