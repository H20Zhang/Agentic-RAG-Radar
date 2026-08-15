# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the information-acquisition control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What information should be acquired next, and how is that need planned/decomposed? | PlanRAG anchor; open question is explicit planning vs reactive evidence-driven control. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What corpus boundary, evidence operations, and resource semantics should the agent control? | DCI exposes interface resolution; RISE/DR-DCI bound it for scale; RARG carries relevance into local interaction. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | What state should make the next retrieval, verification, recovery, or stopping decision? | S2G-RAG gives explicit sufficiency/gap state; LoongReflect pushes state toward rollback/recovery. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential/interface/state-control action space? | Agentic-R learns retriever utility; Critic-R learns from process feedback; GrepSeek learns DCI actions; LoongReflect learns recovery. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate agentic control from interfaces, harnesses, budgets, models, or old prior art? | Evaluation now factorizes corpus boundary/interface resolution and harness/delivery in addition to realized resources and historical baselines. |

## Cross-cutting lens

For system claims, the radar now reasons over:

`substrate × corpus boundary/interface resolution × harness/delivery × state × policy × realized resources × base model × historical baseline`

The interface correction is important. A conventional retriever, raw direct-corpus interaction, and a bounded persistent workspace expose different evidence operations even if they use the same answer model. The harness correction is separate: identical retrieval can still behave differently when tool outputs are injected inline versus made available as files or when prompts/tool contracts change.

Two additional stress tests remain. **State can be editable**, not only descriptive: rollback semantics should be separated from the policy deciding when to use them. And **cross-source composition** can fail even when individual tools work: API choice, document retrieval, entity grounding, and policy constraints need trajectory-level evaluation.

“Realized resources” remains stronger than a nominal budget: a target retrieval rate, call cap, or context budget is not matched until held-out usage and controller-side cost are reported.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture retrieval substrate, modality, control pattern, training paradigm, and task/domain without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.
