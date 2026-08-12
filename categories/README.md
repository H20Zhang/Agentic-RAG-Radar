# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the retrieval control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What information should be acquired next, and how is that need planned/decomposed? | PlanRAG anchor; open question is explicit planning vs reactive evidence-driven control. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What retrieval operations/corpora/tools—and what retrieval budget—should the agent control? | Strong cluster now spans A-RAG, LLM-Wiki, READ, DocNavRAG, and calibrated budget allocation. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | How does evidence change the next retrieval, verification, or stopping decision? | Search-o1 + ACE-GraphRAG; explicit state and matched-budget stopping remain open. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential/resource-allocation action space? | Agentic-R and Graph-R1 target trajectory utility; SAGE adds learned SLO-aware budget allocation. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate agentic control from stronger tools, budgets, models, or rediscovered prior art? | Factorized evaluation now needs both resource matching and a deeper classical IR/QA novelty baseline. |

## Cross-cutting lens

For system claims, the radar now reasons over:

`substrate × operation set × state × policy × budget × base model × historical baseline`

The first six axes address causal attribution. The last asks whether the claimed control pattern is actually new, or whether novelty lies in the LLM-era interface, learned policy, scale, or state representation.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture retrieval substrate, modality, control pattern—including `budget_allocation`—training paradigm, and task/domain without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.
