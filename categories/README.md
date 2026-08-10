# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the retrieval control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What information should be acquired next, and how is that need planned/decomposed? | PlanRAG anchor; open question is explicit planning vs reactive evidence-driven control. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What retrieval operations/corpora/tools should the agent control? | Strongest current cluster: A-RAG, READ, DocNavRAG. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | How does evidence change the next retrieval, verification, or stopping decision? | Search-o1 + ACE-GraphRAG; state and matched-budget stopping remain open. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential action space? | Agentic-R and Graph-R1 expose retriever/policy trajectory objectives. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate agentic control from stronger tools, budgets, or models? | SoK anchor; factorized evaluation is a major open need. |

## Cross-cutting lens

For system claims, the radar tries to reason over:

`substrate × operation set × state × policy × budget × base model`

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture retrieval substrate, modality, control pattern, training paradigm, and task/domain without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.