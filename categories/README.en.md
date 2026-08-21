# Research Map

[中文](README.md) | **English** · [Home](../README.en.md) · [Reading Paths](../README.en.md#reading-paths) · [Research Library](../library/README.en.md)

The field is more useful to reason about as a set of **live research questions** than as a taxonomy of method names. Each question below has a current answer, a boundary where that answer weakens, and an experiment that could change the map.

## Live Research Questions

### Where should adaptivity live?

**Current view.** Some control can be compiled before evidence is read when useful corpus-visible statistics or structure are observable. Other control is irreducibly result-conditioned because the next query depends on names, constraints, or relationships discovered only after retrieval.

**Key design points.** [SIRA](../papers/2605.06647.md) ↔ [ReFind](../papers/2608.12888.md), with [D2-ScaleAgent](../papers/2608.16417.md) separating breadth from depth through evidence-sufficiency routing.

**Boundary.** SIRA pays offline corpus-side intelligence and does not dominate multi-round search at every model/budget; ReFind has a task where single-shot BM25 slightly wins.

**Decisive next evidence.** Same substrate/model/total compute while independently varying pre-retrieval compilation, one-shot retrieval, and result-conditioned replanning.

### When should evidence be materialized?

**Current view.** Stable corpora and predictable evidence units favor preprocessing. Dynamic corpora or query-dependent evidence granularity can justify preserving raw data and localizing evidence only after the information need is known.

**Key design points.** [DCI](../papers/2605.05242.md) → [RISE](../papers/2606.06880.md) / [DR-DCI](../papers/2606.14885.md) → [LENS](../papers/2608.16185.md).

**Boundary.** “No index” is not “no cost”: raw interaction can scale poorly, and LENS spends more online work while failing to beat ReAct on the main answer-EM comparison.

**Decisive next evidence.** Same changing corpus and target, lifecycle-matching offline construction/update + online localization/search cost.

### What state should persist?

**Current view.** Agent state has several owners: external source configuration, accumulated evidence/gaps, trajectory progress, active reasoning state, and retained context. Its value depends on **future reuse × recoverability × reacquisition cost**, not size alone.

**Key design points.** [SGR-Bench](../papers/2605.22219.md) → [S2G-RAG](../papers/2604.23783.md) → [RAAC](../papers/2608.15191.md) → [LoongReflect](../papers/2608.11967.md) → [Context Compression Cost](../papers/2608.16370.md).

**Boundary.** More explicit state can merely add controller capacity or privileged supervision; compression does not create a retrieval tax in every environment.

**Decisive next evidence.** Counterfactual restore/delete individual state classes under matched context, tool, controller, latency, and answer-quality budgets.

### How should retrieval expose the corpus?

**Current view.** “Retriever quality” is too coarse. Candidate admissibility, ranking, surfaced depth, local operations, structural navigation, result inspection, and reading granularity can independently determine what the agent can find and verify.

**Key design points.** [A-RAG](../papers/2602.03442.md) → [DCI](../papers/2605.05242.md) → [RISE](../papers/2606.06880.md) → [RARG](../papers/2607.24223.md), with [VisDocAgentBench](../papers/2608.17889.md) and [CTIFoundry](../papers/2608.18613.md) exposing search / resolve / traverse / inspect / read as evidence-path operations under bounded output contracts.

**Boundary.** Richer interfaces can cost more; VisDocAgentBench changes backend strength and accumulated history across important comparisons, while CTIFoundry bundles corpus materialization, typed tools, output descriptions, and skills.

**Decisive next evidence.** Factorial backend × surfaced-depth × operation-set × read-resolution under the same model, output contract, evidence pool, accumulated history, and realized budget.

### What should be learned?

**Current view.** “Learn the retrieval policy” hides different objects: retriever utility, query/refinement policy, direct-corpus operations, recovery behavior, resource allocation, and training-task distribution.

**Key design points.** [Agentic-R](../papers/2601.11888.md), [Critic-R](../papers/2606.00590.md), [GrepSeek](../papers/2605.29307.md), [SearchMaster](../papers/2608.01822.md), [LoongReflect](../papers/2608.11967.md).

**Boundary.** A richer interface, privileged teacher/verifier, different evidence coverage, easier self-play curriculum, or larger realized budget can masquerade as a better learning objective.

**Decisive next evidence.** Same environment/state/action space/base model while varying learned component, reward/credit assignment, teacher information, and task generation independently.

### What makes an evaluation causal?

**Current view.** Attribution can fail before the controller acts. Evidence must exist; the backend must expose it; the agent must inspect it; source/internal state must be correct; the harness must preserve it; and realized resources must be matched before a policy receives credit.

**Key design points.** [Training Protocols](../papers/2605.27881.md) → [Pi-Serini](../papers/2605.10848.md) → [SGR-Bench](../papers/2605.22219.md) → [ToolScout](../papers/2608.16502.md) → [VisDocAgentBench](../papers/2608.17889.md).

**Boundary.** Final-answer success can hide upstream failure or extra work; even “same retriever” is not the same experiment when surfaced depth, delivery path, retained state, or controller cost differs.

**Decisive next evidence.** An executable benchmark that can replay the same task while independently swapping backend, interface, source state, retained state, harness, and controller—and counterfactually repair one intermediate failure.

## Cross-Cutting Causal Lens

`substrate/evidence coverage × pre-retrieval corpus observability × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state/retention × policy × realized resources × base model × training distribution/protocol × historical baseline`

The current systems tension is:

> **precompute / materialize / retain ↔ defer / localize / reacquire**

Removing an index, search call, or prompt token is only an efficiency win if the displaced work does not reappear elsewhere at the same answer/evidence quality.

## Browse by Canonical Category

| Category | Core question | Current signal |
|---|---|---|
| [Planning & Query Formulation](planning-query-formulation.md) | What can be decided before evidence, and what should be replanned after observing it? | PlanRAG and SIRA make pre-retrieval control explicit. |
| [Retrieval & Tool Use](retrieval-tool-use.md) | What information-access operations and evidence resolution should the agent control? | Interface resolution and materialization placement are now first-class design axes. |
| [Iterative Reasoning & Verification](iterative-reasoning-verification.md) | What state should drive continue, redirect, recovery, verification, or stopping? | Sufficiency, progress, and reversible state are separating into distinct control variables. |
| [Multi-Agent & Orchestration](multi-agent-orchestration.md) | When does specialization justify coordination cost? | No current paper clears the radar's precision threshold as a primary retrieval-orchestration contribution. |
| [Learning & Optimization](learning-optimization.md) | Which part of the information-acquisition loop should be learned? | Learning targets include retrievers, control, recovery, budgets, and self-play task distributions. |
| [Evaluation & Analysis](evaluation-analysis.md) | How do we isolate what actually caused a gain? | Evidence availability, interface, state, harness, and resources repeatedly overturn coarse conclusions. |
