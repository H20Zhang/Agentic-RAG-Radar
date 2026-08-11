# 🧭 Agentic RAG Research Compactions

Start here when you want the **research picture**, not a chronological paper feed.

The archive intentionally becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

The underlying paper records remain available for detail; compactions preserve the conclusions, disagreements, and research questions that are worth carrying forward.

## Recent Month · Weekly

Use weekly reports to decide **what changed recently and what is worth reading now**.

### [2026-W32 · Designing the retrieval interaction](weekly/2026-W32.md)

**Thesis:** early-August work is moving beyond “call a better retriever more times” toward **designing the retrieval interface, making evidence progress explicit, and treating context construction as a policy**.

The most useful counter-signal is READ's BM25 result: some apparent Agentic RAG gains may come from a stronger retrieval primitive rather than adaptive control itself.

[Read the weekly synthesis →](weekly/2026-W32.md)

> Weekly reports remain visible in this section while they fall inside the most recent ~1 month. Older weekly files are retained for provenance but stop occupying the primary archive view once monthly compactions cover that period.

## Recent Quarter · Monthly

Use monthly reports to decide **how the field map is changing**, not merely what was published.

### [2026-08 · Rolling research map](monthly/2026-08.md)

**Current thesis:** Agentic RAG is beginning to look like a control stack:

`retrieval substrate → operation/interface → evidence state/controller → learning/evaluation`

The current month is organized around retrieval-interface redesign, stateful evidence construction, and adaptive context engineering. The unresolved problem is causal attribution across **substrate × operation set × state × policy × budget × base model**.

[Explore the August research map →](monthly/2026-08.md)

> Monthly reports remain visible in this section while they fall inside the most recent ~3 months. Older monthly files stay in the repository, but the long-term public archive rolls them into yearly research maps.

## All Years · Yearly

Use yearly reports for the **durable research map**: which abstractions survived, which claims weakened, which papers defined the year, and what open problems carried forward.

### [2026 · Rolling year-to-date map](yearly/2026.md)

**Current thesis:** the durable 2026 movement is from “agent + retriever” toward an explicit **information-acquisition control stack** in which retrieval operations, evidence state, adaptive policy, and trajectory-level learning/evaluation are increasingly treated as separate research objects.

The report is deliberately labeled rolling: historical coverage before the radar's backfill is not yet complete, so it does not pretend to be a full-year census.

[Explore the 2026 year-to-date map →](yearly/2026.md)

Future finalized yearly reports will be kept here permanently. Earlier years will only be added after historical backfill is sufficiently complete to justify calling the report an annual map rather than an anchor sample.

## How the Time Hierarchy Works

**Weekly** preserves local changes and tensions while they are fresh. **Monthly** compresses several weeks into a field-map update. **Yearly** re-evaluates the whole year and keeps only durable shifts, defining papers, failed/weakening ideas, evidence standards, and open problems entering the next year.

This is **not recursive summarization**: monthly and yearly reports may use lower-level reports as indexes, but load-bearing conclusions are re-grounded in canonical paper records and source/full-paper notes to avoid compounding interpretation error.

Paper-level details remain available in [`../papers/`](../papers/) and the [research-problem map](../categories/README.md).

---

For curation and compaction methodology, see the [maintainer guide](../docs/MAINTENANCE.md).