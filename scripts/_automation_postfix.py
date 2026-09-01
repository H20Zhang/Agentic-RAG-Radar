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

p = ROOT / "tests/test_validate_reading.py"
s = p.read_text(encoding="utf-8").replace(OLD, NEW)
needle = "self.assertEqual(3, periods.count('state=\"reinforced\"'))"
if s.count(needle) != 1:
    raise SystemExit(f"expected one reinforced-count assertion, found {s.count(needle)}")
s = s.replace(needle, "self.assertEqual(2, periods.count('state=\"reinforced\"'))", 1)
p.write_text(s, encoding="utf-8")
