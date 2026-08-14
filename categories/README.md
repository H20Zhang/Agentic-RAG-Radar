# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the information-acquisition control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What information should be acquired next, and how is that need planned/decomposed? | PlanRAG anchor; open question is explicit planning vs reactive evidence-driven control. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What retrieval operations/corpora/tools—and what retrieval budget—should the agent control? | Strong cluster spans A-RAG, LLM-Wiki, READ, DocNavRAG, and graded budget control. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | What state should make the next retrieval, verification, or stopping decision? | S2G-RAG gives explicit sufficiency/gap state an earlier baseline; LoongReflect now pushes state further toward explicit rollback/recovery. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential/resource-allocation/state-control action space? | SPARKLE raises adaptive-policy baselines; LoongReflect learns reversible recovery; Agentic-R/Graph-R1 target trajectory utility; SAGE isolates k allocation. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate agentic control from stronger tools, budgets, models, or rediscovered prior art? | Evaluation now spans historical baselines, realized operating points, and VAKRA-style executable cross-source grounding. |

## Cross-cutting lens

For system claims, the radar reasons over:

`substrate × operation set × state × policy × realized resources × base model × historical baseline`

Two additional stress tests now matter. First, **state can be editable**, not only descriptive: rollback semantics should be separated from the learned policy that decides when to use them. Second, **cross-source composition** can fail even when individual tools work: API choice, document retrieval, entity grounding, and policy constraints need trajectory-level evaluation.

“Realized resources” is intentionally stronger than a nominal budget: a claimed target retrieval rate, call cap, or context budget is not a matched comparison until held-out usage and controller-side cost are reported.

The historical axis asks whether the control-loop shape is actually new, or whether novelty lies in the LLM-era interface, learned policy, scale, state representation, or information environment.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture retrieval substrate, modality, control pattern, training paradigm, and task/domain without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.
