# 🧭 Agentic RAG Research Compactions

Start here when you want the **research picture**, not a chronological paper feed.

The archive intentionally becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

## Recent Month · Weekly

### [2026-W34 · Materialization, progress observability, and the hidden re-query tax](weekly/2026-W34.md)

**Rolling thesis:** moving work out of an index or prompt is only a systems improvement if it does not reappear as query-time localization, controller, or state-reacquisition cost. LENS, RAAC, and the context-compression study expose three different versions of that transfer.

[Read the rolling W34 synthesis →](weekly/2026-W34.md)

### [2026-W33 · Where should retrieval intelligence live?](weekly/2026-W33.md)

**Thesis:** runtime interaction is valuable when it exposes information that could not have been compiled before retrieval. ReFind, LoongReflect, and VAKRA expose runtime interface/state/trajectory bottlenecks; SIRA is the pre-retrieval counterpoint.

[Read the W33 synthesis →](weekly/2026-W33.md)

### [2026-W32 · Convergence, factorization, and a stricter novelty baseline](weekly/2026-W32.md)

**Revised thesis:** interface and learning factorization matter more than “agentic” naming; SIEVE separates admissibility/ranking/inspection/reading, while SearchMaster makes training distribution causal.

[Read the revised W32 synthesis →](weekly/2026-W32.md)

> Weekly reports stay on the primary archive surface for roughly the latest month; older weekly files remain for provenance.

## Recent Quarter · Monthly

### [2026-08 · Rolling research map](monthly/2026-08.md)

**Current thesis:** August is a **placement-of-work** story: what evidence is materialized before the query, what control is deferred until after evidence arrives, and what state is retained versus reacquired. LENS, RAAC, and the context-compression study sharpen all three.

[Explore the August research map →](monthly/2026-08.md)

> Monthly reports stay on the primary archive surface for roughly the latest quarter. Older files remain in the repository and are compressed again at yearly granularity.

## All Years · Yearly

### [2026 · Rolling year-to-date map](yearly/2026.md)

**Current thesis:** the durable 2026 shift is toward explicit design of where information-acquisition work lives—what is precomputed/materialized, what becomes observable after retrieval, what state persists, and how offline + online resources are spent.

The report remains explicitly rolling; incomplete historical backfill is not presented as full-year coverage.

[Explore the 2026 year-to-date map →](yearly/2026.md)

Earlier years will only be added when backfill is sufficiently complete to justify an annual map rather than an anchor sample.

## How the Time Hierarchy Works

**Weekly** preserves local deltas and tensions. **Monthly** rebuilds the field map. **Yearly** keeps only durable shifts, defining papers, weakened claims, evidence standards, and open problems.

This is **not recursive summarization**: lower-level compactions are indexes, while load-bearing monthly/yearly conclusions are re-grounded in canonical records and source/full-paper notes.

Paper-level detail remains in [`../papers/`](../papers/) and the [research-problem map](../categories/README.md).

---

For methodology, see the [maintainer guide](../docs/MAINTENANCE.md) and [compaction protocol](../COMPACTION.md).
