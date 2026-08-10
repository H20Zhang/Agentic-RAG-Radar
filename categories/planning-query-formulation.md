# Planning & Query Formulation

> **Core question:** What information should the agent acquire next, and how should a complex information need be decomposed, planned, or reformulated before retrieval?

This category is about **control before the retrieval call**. A paper belongs here when planning/query formulation is a substantive research object rather than a prompt convenience.

## Current design anchors

### [PlanRAG](../papers/2406.12430.md) — ★★★☆☆

**Design point:** generate an explicit decision/information-acquisition plan first, then derive iterative data queries from that plan.

**Compared with:** iterative RAG where retrieval evolves without a stable upstream plan.

**Open question:** when is an explicit plan better than online replanning from evidence state, especially when early assumptions are wrong?

## What would count as meaningful progress?

High-signal work should isolate at least one of these questions:

- **planning vs reactive control:** explicit multi-step plan versus deciding only from current evidence;
- **plan repair:** how retrieval failures or contradictory evidence revise the plan;
- **query decomposition quality:** whether subqueries improve evidence completeness under matched budgets;
- **planning cost:** whether better accuracy survives added planning tokens/latency;
- **structured targets:** planning over SQL, graph, web, code, or multimodal retrieval operations rather than only passage queries.

A new prompt that asks the LLM to “make a plan first” is not enough by itself.