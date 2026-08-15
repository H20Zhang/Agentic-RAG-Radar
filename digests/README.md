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

**Revised thesis:** W32 is not best described as the week Agentic RAG “moved beyond top-k.” Historical backfill now makes that correction stronger: by May–July, DCI, RISE, DR-DCI, and RARG had already made corpus-interface resolution, bounded interaction spaces, dynamic workspaces, and relevance-guided interaction explicit research objects.

[Read the W32 synthesis →](weekly/2026-W32.md)

> Weekly reports stay on the primary archive surface for roughly the latest month; older weekly files remain for provenance.

## Recent Quarter · Monthly

### [2026-08 · Rolling research map](monthly/2026-08.md)

**Current thesis:** August is a **factorization + trajectory-integrity** story, now re-grounded against a stronger pre-August interaction-space lineage:

`corpus boundary/interface resolution → explicit/editable state → adaptive policy/stopping → resource allocation → harness/delivery → executable evaluation`

The important correction is that “retrieval interface” was already more mature than this radar previously represented. DCI exposes interface resolution; RISE/DR-DCI recover scale through persistent workspaces; RARG carries relevance into execution; Is Grep All You Need? shows the surrounding harness can reverse retrieval conclusions.

[Explore the August research map →](monthly/2026-08.md)

> Monthly reports stay on the primary archive surface for roughly the latest quarter. Older files remain in the repository and are compressed again at yearly granularity.

## All Years · Yearly

### [2026 · Rolling year-to-date map](yearly/2026.md)

**Current thesis:** the durable 2026 movement is toward explicit design of the agent's **information environment**—corpus boundary, evidence operations, persistent state, adaptive policy, and realized resources—plus a stricter causal bar that treats harness/evidence delivery as part of the system.

The report remains explicitly rolling; incomplete historical backfill is not presented as full-year coverage.

[Explore the 2026 year-to-date map →](yearly/2026.md)

Earlier years will only be added when backfill is sufficiently complete to justify an annual map rather than an anchor sample.

## How the Time Hierarchy Works

**Weekly** preserves local deltas and tensions. **Monthly** rebuilds the field map. **Yearly** keeps only durable shifts, defining papers, weakened claims, evidence standards, and open problems.

This is **not recursive summarization**: lower-level compactions are indexes, while load-bearing monthly/yearly conclusions are re-grounded in canonical records and source/full-paper notes.

Paper-level detail remains in [`../papers/`](../papers/) and the [research-problem map](../categories/README.md).

---

For methodology, see the [maintainer guide](../docs/MAINTENANCE.md) and [compaction protocol](../COMPACTION.md).
