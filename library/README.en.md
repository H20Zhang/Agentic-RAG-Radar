# Agentic RAG Research Library

[中文](README.md) | **English** · [Home](../README.en.md)

This library organizes old work by **research problem and design tension**. Weekly/monthly/yearly reports explain temporal movement; they are not the archive index.

## Browse by Research Problem

| Problem | Entry | Current tension |
|---|---|---|
| **Planning & Query Formulation** | [Open](../categories/planning-query-formulation.md) | Which search behavior can be compiled before evidence arrives, and which decisions require online evidence? |
| **Retrieval & Tool Use** | [Open](../categories/retrieval-tool-use.md) | Is opaque top-k sufficient, or should agents control explicit search/read/filter/navigation operations? |
| **Iterative Reasoning & Verification** | [Open](../categories/iterative-reasoning-verification.md) | When should an agent continue, rewrite, backtrack, or stop, and what progress signal is trustworthy? |
| **Learning & Optimization** | [Open](../categories/learning-optimization.md) | How should retrieval/control policy learn from rollout, feedback, or persistent state? |
| **Evaluation & Analysis** | [Open](../categories/evaluation-analysis.md) | How should backend, interface, harness, model, and budget be separated for causal attribution? |
| **Multi-Agent & Orchestration** | [Open](../categories/multi-agent-orchestration.md) | When does parallel search/reasoning coordination add value rather than overhead? |

## Browse by Research Line

### 1. Fixed retrieval → direct interaction → query-time evidence materialization

[SIRA](../papers/2605.06647.md) → [DCI](../papers/2605.05242.md) → [ReFind](../papers/2608.12888.md) → [LENS](../papers/2608.16185.md)

**Takeaway:** adaptivity placement and evidence-materialization time are separate design decisions. SIRA compiles some intelligence before retrieval; DCI/ReFind preserve raw substrates; LENS delays the evidence boundary itself until query time.

### 2. Search loop → progress-aware control → reversible state

[S2G-RAG](../papers/2604.23783.md) → [RAAC](../papers/2608.15191.md) → [LoongReflect](../papers/2608.11967.md) → [Context Compression Cost](../papers/2608.16370.md)

**Takeaway:** “more rounds” is not a primitive. What matters is how sufficiency/progress is observed, whether bad state can be reversed, and whether dropped state reappears later as reacquisition cost.

### 3. Retriever quality → interface/harness attribution → cross-source execution

[Pi-Serini](../papers/2605.10848.md) → [Is Grep All You Need?](../papers/2605.15184.md) → [Training Protocols](../papers/2605.27881.md) → [VAKRA](../papers/2608.12282.md)

**Takeaway:** backend score, surfaced evidence, agent harness, model, and tool budget are tightly coupled. Leaderboard gains are usually system-level evidence before they are component evidence.

## Browse by Year

The [Curated Paper Index](../papers/README.md) provides compact chronology. If your goal is to understand the field, start from a research line rather than a year.

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar): how RAG/Search evaluation moves from retrieval quality toward stateful, cross-source, executable evaluation.
- [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar): when the central problem is persistent memory across interactions.
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar): when retrieval is one stage inside end-to-end data work.
