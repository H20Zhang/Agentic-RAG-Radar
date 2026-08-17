# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the information-acquisition control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What information should be acquired next, and how is that need planned/decomposed? | PlanRAG anchor; open question is explicit planning vs reactive evidence-driven control. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What corpus boundary, evidence operations, source structure, environment state, and resource semantics should the agent control? | DCI exposes interface resolution; Pi-Serini raises the lexical baseline; RISE/DR-DCI bound interaction for scale; RARG guides local execution; SIEVE factorizes admissibility, ranking, inspection, and reading. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | What state should make the next retrieval, verification, recovery, or stopping decision? | S2G-RAG gives explicit sufficiency/gap state; LoongReflect pushes agent state toward rollback/recovery. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential/interface/state-control action space? | Agentic-R learns retriever utility; Critic-R learns from process feedback; GrepSeek learns DCI actions; SearchMaster regulates self-play task/trajectory generation; LoongReflect learns recovery. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate agentic control from interfaces, environment state, harnesses, budgets, models, or old prior art? | SGR-Bench makes site-specific retrieval state measurable; Pi-Serini exposes backend tuning/depth as baseline confounders; VAKRA stress-tests cross-source composition. |

## Cross-cutting lens

For system claims, the radar now reasons over:

`substrate × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state × policy × realized resources × base model × training distribution × historical baseline`

The new distinction is **environment retrieval state versus agent state**. SGR-Bench shows that finding the right website does not mean the right evidence is exposed: filters, views, hierarchies, scopes, or time windows may still be wrong. Internal evidence/memory state cannot repair a source that remains configured to the wrong retrieval state.

A second correction is that **retriever family is not a controlled variable by itself**. Pi-Serini shows that BM25 tuning, surfaced ranking depth, and browse/read affordances can materially change the lexical-versus-dense conclusion. Those choices belong inside interface/resource accounting rather than being hidden under the label “BM25 baseline.”

The earlier interface and harness corrections remain. DCI/RISE/DR-DCI show that corpus boundaries and evidence operations alter what the agent can express; SIEVE shows that candidate admissibility, ranking, inspection, and read granularity are separable; Is Grep All You Need? shows that identical retrieval can behave differently when tool output is delivered through a different harness path.

“Realized resources” remains stronger than a nominal budget: a target retrieval rate, call cap, deep ranking, or context budget is not matched until held-out usage and controller/backend costs are reported.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture retrieval substrate, modality, control pattern, training paradigm, and task/domain without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.
