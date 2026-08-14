# 🧭 Agentic RAG Research Compactions

Start here when you want the **research picture**, not a chronological paper feed.

The archive intentionally becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

The underlying paper records remain available for detail; compactions preserve the conclusions, disagreements, and research questions worth carrying forward.

## Recent Month · Weekly

### [2026-W33 · State recovery and cross-source trajectory integrity](weekly/2026-W33.md)

**Rolling thesis:** the new pressure point is no longer just “what should the agent retrieve next?” LoongReflect makes accumulated execution state **reversible**, while VAKRA tests whether agents can keep identity and evidence coherent across APIs and document retrieval in one executable trajectory.

The key tension is causal: rollback-style state control may help long-horizon search, but VAKRA's failures often look like entity/schema grounding rather than a clearly bad branch. Those are different failure modes and should not be collapsed into one “memory problem.”

[Read the rolling W33 synthesis →](weekly/2026-W33.md)

### [2026-W32 · Convergence, factorization, and a stricter novelty baseline](weekly/2026-W32.md)

**Revised thesis:** W32 is not best described as the week Agentic RAG “moved beyond top-k.” Earlier 2026 work already made agent-facing retrieval environments explicit. The more durable change is that **interface, evidence state, context policy, and retrieval budget are becoming separable control variables**, while the new IR-history perspective pushes the novelty baseline back to classical QA.

[Read the W32 synthesis →](weekly/2026-W32.md)

> Weekly reports stay on the primary archive surface for roughly the latest month; older weekly files remain for provenance.

## Recent Quarter · Monthly

### [2026-08 · Rolling research map](monthly/2026-08.md)

**Current thesis:** August is a **factorization + trajectory-integrity** story:

`environment/interface → explicit/editable state → adaptive policy/stopping → resource allocation → executable evaluation`

W33 adds state rollback and cross-source grounding without invalidating the earlier map; it makes the state and evaluation layers sharper.

[Explore the August research map →](monthly/2026-08.md)

> Monthly reports stay on the primary archive surface for roughly the latest quarter; older files remain in the repository and are compressed again at yearly granularity.

## All Years · Yearly

### [2026 · Rolling year-to-date map](yearly/2026.md)

**Current thesis:** the durable 2026 movement is toward an explicit **information-acquisition control stack** whose environment, state, policy, and resource objective can be tested separately. The year map also tracks whether a claimed mechanism is genuinely new or a new LLM-era implementation of an older IR/QA control principle.

The report remains explicitly rolling; incomplete historical backfill is not presented as full-year coverage.

[Explore the 2026 year-to-date map →](yearly/2026.md)

Earlier years will only be added when backfill is sufficiently complete to justify an annual map rather than an anchor sample.

## How the Time Hierarchy Works

**Weekly** preserves local deltas and tensions. **Monthly** rebuilds the field map. **Yearly** keeps only durable shifts, defining papers, weakened claims, evidence standards, and open problems.

This is **not recursive summarization**: lower-level compactions are indexes, while load-bearing monthly/yearly conclusions are re-grounded in canonical records and source/full-paper notes.

Paper-level detail remains in [`../papers/`](../papers/) and the [research-problem map](../categories/README.md).

---

For methodology, see the [maintainer guide](../docs/MAINTENANCE.md) and [compaction protocol](../COMPACTION.md).
