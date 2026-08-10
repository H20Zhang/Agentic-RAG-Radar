# Research Compaction Protocol

Agentic RAG Radar uses a **three-level research memory hierarchy** rather than accumulating one Markdown file per day.

## Levels

| Level | Persistent artifact | Purpose |
|---|---|---|
| **L0 · Paper records** | `data/papers/*.json` + `papers/*` | Lossless-ish canonical facts, provenance, classification, and per-paper research notes. |
| **L1 · Weekly compaction** | `digests/weekly/YYYY-Www.md` | Compress the week's papers into research deltas, clusters, disagreements, and a reading priority. |
| **L2 · Monthly compaction** | `digests/monthly/YYYY-MM.md` | Rebuild the field-level picture: which abstractions are gaining traction, what evidence changed, and which open questions matter next. |

Daily ingestion **does not create a daily Markdown archive**. It updates canonical records, per-paper notes when useful, and the rolling `Latest Papers` section in the README.

## Weekly compaction

A weekly digest is not a concatenation of paper summaries. It should answer:

1. **What changed this week?** Identify 1–3 research shifts that would still matter if individual paper titles were hidden.
2. **Which papers matter most, compared with what?** Rank only the few papers that materially change an abstraction, method family, evidence base, or benchmark.
3. **Where do papers agree or conflict?** Preserve negative results, baseline reversals, and incompatible assumptions.
4. **What should a researcher read next?** End with a compact reading order and 1–3 open questions worth tracking.

The weekly compactor must read the canonical paper records and available full-paper notes for that week. Do not summarize the README alone.

## Monthly compaction

A monthly digest should operate at a higher abstraction level than the weekly reports. It should include:

- **Field map changes:** which taxonomy areas grew, converged, split, or became less convincing.
- **Most important papers:** usually 5–10 maximum, selected by research significance rather than recency.
- **Emerging design patterns:** recurring agent loops, retrieval interfaces, training strategies, or evaluation protocols.
- **Evidence audit:** benchmark concentration, matched-budget issues, repeated baselines, negative results, and claims that strengthened or weakened during the month.
- **Open problems:** 3–5 questions whose resolution could change the direction of Agentic RAG research.

Monthly compaction may use weekly digests as an index, but **must re-check canonical paper records and source notes for load-bearing claims**. Never recursively summarize summaries as the sole evidence source; that creates compounding interpretation error.

## Retention policy

- Keep every accepted canonical paper record.
- Keep per-paper Markdown only when it adds researcher-facing analysis beyond the JSON record; do not create files merely for symmetry.
- Keep one weekly digest per ISO week and one monthly digest per calendar month.
- README is a rolling view, not an archive.
- Corrections propagate upward: if an important paper is reclassified or a claim is corrected, update the relevant weekly/monthly digest when the correction changes its synthesis.

## Multi-agent compaction

When parallel research roles are available, use independent roles before synthesis:

| Role | Weekly / monthly responsibility |
|---|---|
| **Clusterer** | Group papers by actual research delta, not keyword similarity. |
| **Evidence Auditor** | Compare benchmarks, baselines, budgets, ablations, and negative results. |
| **Trend Skeptic** | Challenge whether an apparent trend is real or merely several similarly framed papers. |
| **Synthesizer** | Produce the final compact report only after seeing the independent analyses. |

The goal is **lossy compression of repetition, not loss of disagreement or uncertainty**.
