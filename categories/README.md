# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the information-acquisition control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What can be decided before evidence is retrieved, and what should be replanned after observing it? | PlanRAG anchors explicit planning; SIRA compiles retrieval actions from corpus-visible statistics before evidence inspection. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What should be pre-materialized versus exposed as query-time corpus operations? | SIRA ↔ ReFind already separated compile-before from adapt-after; LENS adds a second placement decision by making **evidence regions themselves query-time/latent** over dynamic raw documents. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | What progress/state should drive continue, redirect, verification, recovery, or stopping? | S2G-RAG gives sufficiency/gap state; RAAC gives trajectory-progress/stagnation signals; LoongReflect adds rollback/recovery. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential/interface/state-control action space? | Agentic-R learns retriever utility; Critic-R learns process feedback; GrepSeek learns DCI actions; SearchMaster controls self-play distribution; LoongReflect learns recovery. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate policy/retrieval gains from evidence, interfaces, retained state, harnesses, budgets, models, or prior art? | Training Protocols starts at evidence availability; Pi-Serini/backend depth and SGR-Bench/source state isolate earlier stages; the compression study shows completion can hide a large **state-reacquisition tax**. |

## Cross-cutting lens

For system claims, the radar reasons over:

`substrate/evidence coverage × pre-retrieval corpus observability × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state/retention × policy × realized resources × base model × training distribution/protocol × historical baseline`

The current correction is no longer just **adaptivity placement**. **Materialization placement** matters too. SIRA shows that some search behavior can be compiled before evidence retrieval. ReFind shows result-conditioned iteration can matter when newly retrieved names/times/session cues change the next query. LENS asks an earlier systems question: should evidence boundaries/index structures exist before the query at all, or should a dynamic raw corpus be localized after the question arrives?

The state layer also needs a cost model. RAAC shows a controller can benefit from explicit progress/novelty signals; LoongReflect makes active state reversible; the context-compression study shows that dropping recoverable state may not change success while causing the agent to re-query the environment far more often. **Less context is not automatically less work.**

The evaluation chain still starts earlier: the external corpus must contain answer-bearing evidence, the backend must expose it, the agent must be able to inspect it, source state and harness must preserve it, and realized offline+online costs must be counted before crediting a policy.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture substrate, modality, control pattern, training paradigm, and task/domain. Category pages are living research views: they should change when evidence changes, not simply accumulate links.
