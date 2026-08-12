# 🧭 Agentic RAG Research Compactions

Start here when you want the **research picture**, not a chronological paper feed.

The archive intentionally becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

The underlying paper records remain available for detail; compactions preserve the conclusions, disagreements, and research questions worth carrying forward.

## Recent Month · Weekly

### [2026-W32 · Convergence, factorization, and a stricter novelty baseline](weekly/2026-W32.md)

**Revised thesis:** W32 is not best described as the week Agentic RAG “moved beyond top-k.” Earlier 2026 work already made agent-facing retrieval environments explicit. The more durable change is that **interface, evidence state, context policy, and retrieval budget are becoming separable control variables**, while the new IR-history perspective pushes the novelty baseline back to classical QA.

The strongest tensions are now: **better primitive vs better policy**, **adaptive budget vs real resource cost**, and **modern capability vs older control-loop precedent**.

[Read the weekly synthesis →](weekly/2026-W32.md)

> Weekly reports stay on the primary archive surface for roughly the latest month; older weekly files remain for provenance.

## Recent Quarter · Monthly

### [2026-08 · Rolling research map](monthly/2026-08.md)

**Current thesis:** August is a **convergence + factorization** story:

`environment/interface → evidence state → policy/stopping → resource allocation → evaluation`

The rolling map now groups evidence into **environment/interface design**, **state + resource-aware control**, and **evaluation/novelty discipline**. Backfilled LLM-Wiki and Know Before You Fetch materially changed the chronology and baseline standard rather than simply adding two more papers.

[Explore the August research map →](monthly/2026-08.md)

> Monthly reports stay on the primary archive surface for roughly the latest quarter; older files remain in the repository and are compressed again at yearly granularity.

## All Years · Yearly

### [2026 · Rolling year-to-date map](yearly/2026.md)

**Current thesis:** the durable 2026 movement is toward an explicit **information-acquisition control stack** whose environment, state, policy, and resource objective can be tested separately. The year map now also tracks a second axis: whether a claimed agentic mechanism is genuinely new or a new LLM-era implementation of an older IR/QA control principle.

The report remains explicitly rolling; incomplete historical backfill is not presented as full-year coverage.

[Explore the 2026 year-to-date map →](yearly/2026.md)

Earlier years will only be added when backfill is sufficiently complete to justify an annual map rather than an anchor sample.

## How the Time Hierarchy Works

**Weekly** preserves local deltas and tensions. **Monthly** rebuilds the field map. **Yearly** keeps only durable shifts, defining papers, weakened claims, evidence standards, and open problems.

This is **not recursive summarization**: lower-level compactions are indexes, while load-bearing monthly/yearly conclusions are re-grounded in canonical records and source/full-paper notes.

Paper-level detail remains in [`../papers/`](../papers/) and the [research-problem map](../categories/README.md).

---

For methodology, see the [maintainer guide](../docs/MAINTENANCE.md) and [compaction protocol](../COMPACTION.md).
