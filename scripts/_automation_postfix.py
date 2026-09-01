from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "2026-08-28T01:56:45Z"
NEW = "2026-09-01T01:24:01Z"

for name in ("README.md", "README.en.md"):
    p = ROOT / name
    s = p.read_text(encoding="utf-8")
    replacements = {
        "timefirst:evidence=interaction-conditioned-retrieval~matched-control": "timefirst:evidence=interaction-conditioned-retrieval~qwen3-embedding-0.6b-family",
        "timefirst:caveat=interaction-conditioned-retrieval~resource-boundary": "timefirst:caveat=interaction-conditioned-retrieval~llm-verifier-labels",
        "timefirst:evidence=multimodal-evidence-persistence~matched-control": "timefirst:evidence=multimodal-evidence-persistence~weagent-mmsearch-rl",
        "timefirst:caveat=multimodal-evidence-persistence~resource-boundary": "timefirst:caveat=multimodal-evidence-persistence~runtime-recovery-cache-semantics",
        "timefirst:evidence=proactive-context-management~matched-control": "timefirst:evidence=proactive-context-management~qwen3-8b-staged-ablation",
        "timefirst:caveat=proactive-context-management~resource-boundary": "timefirst:caveat=proactive-context-management~partial-rollout-credit-assignment",
    }
    for old, new in replacements.items():
        if s.count(old) != 1:
            raise SystemExit(f"{name}: expected exactly one {old}, got {s.count(old)}")
        s = s.replace(old, new, 1)
    if name == "README.md":
        s = s.replace("success-conditioned trajectory + LLM verifier；", "success-conditioned trajectory + LLM verifier labels；", 1)
        s = s.replace("runtime recovery 与 cache；", "runtime recovery cache semantics；", 1)
        s = s.replace("partial rollout 与 credit；", "partial-rollout credit assignment；", 1)
    else:
        s = s.replace("Success-conditioned trajectories plus an LLM verifier;", "Success-conditioned trajectories plus LLM verifier labels;", 1)
        s = s.replace("runtime recovery and caching;", "runtime recovery cache semantics;", 1)
        s = s.replace("partial rollouts and credit together;", "partial-rollout credit assignment together;", 1)
    p.write_text(s, encoding="utf-8")

# The public deep-note contract uses editorial headings and exact verdict labels in English.
for identity in ("2608.27912", "2608.28062", "2608.28476"):
    p = ROOT / "papers" / f"{identity}.md"
    s = p.read_text(encoding="utf-8")
    replacements = {
        "| **Why it matters** |": "| **Why this paper matters** |",
        "| **Best evidence** |": "| **Strongest evidence** |",
        "| **Main caveat** |": "| **Biggest caveat** |",
        "## Problem": "## Research question",
        "## Closest comparison": "## Research delta",
        "## Decisive evidence": "## Evidence & attribution",
        "## What remains unproven": "## Open question",
        "## Field-map consequence": "## Where it fits",
    }
    for old, new in replacements.items():
        if s.count(old) != 1:
            raise SystemExit(f"{identity}: expected exactly one {old!r}, got {s.count(old)}")
        s = s.replace(old, new, 1)
    p.write_text(s, encoding="utf-8")

# Close the August digest on the repository's UTC+8 calendar-month boundary.
p = ROOT / "digests" / "monthly" / "2026-08.md"
s = p.read_text(encoding="utf-8")
s = s.replace("**Radar acceptance boundary:** 2026-08-31T23:59:59Z", "**Radar acceptance boundary:** 2026-08-31T16:00:00Z", 1)
p.write_text(s, encoding="utf-8")

p = ROOT / "tests" / "test_validate_reading.py"
s = p.read_text(encoding="utf-8").replace(OLD, NEW)
needle = "self.assertEqual(3, periods.count('state=\"reinforced\"'))"
if s.count(needle) != 1:
    raise SystemExit(f"expected one reinforced-count assertion, found {s.count(needle)}")
s = s.replace(needle, "self.assertEqual(2, periods.count('state=\"reinforced\"'))", 1)
needle = "self.assertEqual(34, periods.count('state=\"new_signal\"'))"
if s.count(needle) != 1:
    raise SystemExit(f"expected one new-signal-count assertion, found {s.count(needle)}")
s = s.replace(needle, "self.assertEqual(33, periods.count('state=\"new_signal\"'))", 1)
p.write_text(s, encoding="utf-8")
