# Agentic RAG Research Compactions

This directory is the **human reading layer** of Agentic RAG Radar. Canonical records preserve papers and provenance; compactions preserve the research picture.

## Current research map

### [Weekly · 2026-W32](weekly/2026-W32.md)

**Thesis:** early-August work shifts attention from repeatedly calling a better retriever toward **designing the retrieval interface, making evidence progress explicit, and treating context assembly as a policy**.

The report keeps an important counter-signal: READ's BM25 result suggests some apparent “agentic” gains may actually come from a better lexical/interface choice. That motivates primitive-matched, budget-matched, and state-ablation comparisons rather than another aggregate leaderboard.

### [Monthly · 2026-08 (rolling)](monthly/2026-08.md)

**Thesis:** Agentic RAG is beginning to look like a control stack:

`retrieval substrate → operation/interface → evidence state/controller → learning/evaluation`

The current month map is provisional and organized around three clusters: retrieval-interface redesign, stateful evidence construction, and adaptive context engineering. The report is intentionally revised when new evidence contradicts the map; it is not a chronological append-only log.

## What a compaction keeps

A compaction should preserve information that changes a researcher's decision:

- a real abstraction shift that survives hiding paper titles;
- the few papers that materially change the design space or evidence base;
- negative results, baseline reversals, and incompatible assumptions;
- evidence strength, retrieval/token-budget caveats, and missing ablations;
- a minimal reading order and open questions worth spending attention on.

It should aggressively remove repeated background, contribution boilerplate, and paper-by-paper details already recoverable from canonical records.

## Hierarchy

| Layer | Artifact | Reader question |
|---|---|---|
| **L0 · Canonical papers** | `../data/papers/*.json` + `../papers/` | What exactly did this paper claim, compare, and show? |
| **L1 · Weekly** | `weekly/YYYY-Www.md` | What changed this week, and which disagreements matter? |
| **L2 · Monthly** | `monthly/YYYY-MM.md` | How is the field map changing, and what should influence research direction? |

The same daily maintenance task performs ingestion and checks whether a completed week/month is missing or stale. Monthly reports may use weekly reports as an index, but load-bearing claims are re-grounded in canonical paper records to avoid recursive summary drift.

See [`../COMPACTION.md`](../COMPACTION.md) for the editorial protocol.