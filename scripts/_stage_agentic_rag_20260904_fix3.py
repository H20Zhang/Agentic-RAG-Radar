from pathlib import Path

for name, heading, body in [
    (
        "papers/2609.00967.md",
        "## Open question",
        "Can route-level marginal utility remain stable when one policy checkpoint, retrieval result volume, token budget, and latency budget are all matched, and when returned evidence versus evidence visibility are intervened on separately?",
    ),
    (
        "papers/2609.00967.zh.md",
        "## Open question",
        "如果固定同一 policy checkpoint，并配平返回证据量、token 与 latency，route-level marginal utility 是否仍然稳定？进一步分别干预 returned evidence 与 evidence visibility 后，调用检索的价值与检索内容本身的价值能否被拆开？",
    ),
]:
    p = Path(name)
    s = p.read_text(encoding="utf-8")
    if heading not in s:
        s = s.rstrip() + "\n\n" + heading + "\n\n" + body + "\n"
    p.write_text(s, encoding="utf-8")
