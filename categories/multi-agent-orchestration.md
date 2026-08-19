# Multi-Agent & Orchestration

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** When does splitting information acquisition across specialized agents improve retrieval quality or reliability enough to justify the coordination cost?

This category is intentionally **empty at the current precision threshold**. A paper is not included here merely because it runs several LLM agents in parallel. Retrieval/search orchestration must be a substantive research contribution.

## What we are looking for

High-signal work would isolate questions such as:

- **specialization:** different agents have genuinely different retrieval tools, corpora, roles, or evidence objectives;
- **coordination:** how subqueries, evidence, uncertainty, or provenance are shared without duplicating work;
- **conflict resolution:** how agents reconcile contradictory retrieved evidence rather than voting blindly;
- **budget allocation:** whether a controller decides which agent deserves additional search/retrieval budget;
- **causal value:** multi-agent orchestration is compared against a strong single-agent system with comparable total model/retrieval budget.

## Why the bar is high

Multi-agent RAG can appear stronger simply because it spends more inference compute and performs more searches. The key comparison is therefore not `many agents vs one agent`; it is **better decomposition/coordination vs the same resources under a simpler controller**.

Until a paper makes that delta identifiable, it belongs in another category or is held out of the radar.