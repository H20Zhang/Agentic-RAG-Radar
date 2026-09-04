# Agentic RAG Research Library

[中文](README.md) | **English** · [Home](../README.en.md)

Browse earlier work by **research problem, design tension, and research line**; weekly, monthly, and yearly pages record changes over time.

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

### Fixed retrieval → direct interaction → query-time evidence materialization

[SIRA](../papers/2605.06647.md) → [ITER](../papers/2608.27912.md) → [WeAgent-MMSearch](../papers/2608.28062.md) → [ContextPilot](../papers/2608.28476.md)

Adaptivity placement and evidence lifetime are separate design decisions. SIRA compiles retrieval intent before access; ITER moves trajectory state into retriever ranking; WeAgent-MMSearch keeps returned visual evidence available across turns; ContextPilot learns which working state to retain or offload.

### Search loop → validity-aware state → recovery and reacquisition

[RAAC](../papers/2608.15191.md) → [StateMem](../papers/2608.19652.md) → [EvoWiki](../papers/2608.23265.md) → [Context Compression Cost](../papers/2608.16370.md)

“More rounds” is not a primitive. What matters is how the agent observes progress, whether operative validity is resolved at answer time or write time, and whether dropped state reappears later as reacquisition cost.

### Retriever quality → interface/harness attribution → cross-source execution

[Pi-Serini](../papers/2605.10848.md) → [Is Grep All You Need?](../papers/2605.15184.md) → [Training Protocols](../papers/2605.27881.md) → [Skill Following](../papers/2609.00549.md) → [CoBRA](../papers/2609.00967.md) → [VAKRA](../papers/2608.12282.md)

Backend score, surfaced evidence, agent harness, model, and tool budget are tightly coupled. Skill Following separates selective retrieval from realized same-task utility; CoBRA then trains routing from an internal-versus-external margin on the same query. Leaderboard gains remain system-level evidence until interface, branch competence, and realized resources are matched.

## Browse by Year

The [Curated Paper Index](../papers/README.md) provides compact chronology. If your goal is to understand the field, start from a research line rather than a year.

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar): how RAG/Search evaluation moves from retrieval quality toward stateful, cross-source, executable evaluation.
- [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar): when the central problem is persistent memory across interactions.
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar): when retrieval is one stage inside end-to-end data work.
