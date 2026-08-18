# Browse Agentic RAG by Research Problem

The taxonomy is organized by **which part of the information-acquisition control stack changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What can be decided before evidence is retrieved, and what should be replanned after observing it? | PlanRAG anchors explicit planning; SIRA is the adjacent counterpoint that compiles retrieval terms/actions from corpus-visible statistics before evidence inspection. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What corpus signals, boundaries, operations, state, and resources should the agent control? | SIRA ↔ ReFind exposes the new tension: compile adaptivity before retrieval when possible, defer it to result-conditioned interaction when new evidence changes the next query. DCI/RISE/RARG still define the interaction-space lineage. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | What state should make the next retrieval, verification, recovery, or stopping decision? | S2G-RAG gives explicit sufficiency/gap state; LoongReflect pushes internal state toward rollback/recovery. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization/coordination justify multiple agents? | No paper currently clears the radar's precision threshold as a primary contribution. |
| [Learning & Optimization](learning-optimization.md) | What should be learned once retrieval is a sequential/interface/state-control action space? | Agentic-R learns retriever utility; Critic-R learns from process feedback; GrepSeek learns DCI actions; SearchMaster regulates self-play task generation; LoongReflect learns recovery. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate policy/retrieval gains from missing evidence, interfaces, environment state, harnesses, budgets, models, or prior art? | Training Protocols makes corpus answerability and training setup causal; Pi-Serini exposes backend tuning/depth; SGR-Bench exposes environment state; VAKRA stress-tests cross-source composition. |

## Cross-cutting lens

For system claims, the radar now reasons over:

`substrate/evidence coverage × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state × policy × realized resources × base model × training distribution/protocol × historical baseline`

The most important new correction is **adaptivity placement**. SIRA shows that some apparent need for multi-round search disappears when the controller can inspect corpus-level discriminative signals and compile a retrieval action before reading passages. ReFind gives the opposite boundary: on distributed chat-memory tasks, forcing one search can lose substantially because newly exposed names, times, and session-local context make later reformulation useful. `Number of rounds` is therefore not a stable research variable by itself.

The evaluation chain starts even earlier. Retrieval, Reward, and Training Protocols shows that a training corpus can omit answer-bearing evidence while the model still receives positive final-answer reward from parametric knowledge. Before asking whether a policy learned to retrieve better, we must establish that the external evidence path could support the reward in the first place.

Earlier corrections remain: Pi-Serini separates backend exposure from agent inspection; SGR-Bench separates right source from right source state; DCI/SIEVE factor interface resolution and admissibility; Is Grep All You Need? makes harness/evidence delivery a causal variable. These distinctions should simplify attribution, not become an ever-growing taxonomy of buzzwords.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture substrate, modality, control pattern, training paradigm, and task/domain. Category pages are living research views: they should change when evidence changes, not simply accumulate links.
