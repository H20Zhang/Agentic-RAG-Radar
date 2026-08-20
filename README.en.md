# Agentic RAG Radar

[中文](README.md) | **English**

A research map of agent-controlled retrieval, evidence access, and information-state management.

[Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[Latest Papers](#latest) · [Field Map](#field-map) · [Reading Paths](#reading-paths) · [Browse all](#library)

Last updated: **2026-08-20**

<a id="latest"></a>
<a id="latest-papers"></a>
<a id="-latest-papers"></a>
## Latest Papers

### [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](papers/2608.16185.md)
`Retrieval & Tool Use` · `documents` `iterative search` `budget allocation` · **4/5** · 2026-08-17

LENS defers **evidence materialization itself** until query time: raw-document regions remain latent until the information need is known.

[Paper](https://arxiv.org/abs/2608.16185) · [Research note](papers/2608.16185.md)

<details><summary><strong>How LENS localizes evidence at query time</strong></summary>

Fixed chunks and indexes commit to evidence boundaries before the query and can become stale as raw files change. LENS instead proposes raw-document regions from multiple cheap cues, inspects them with a relevance oracle, updates per-fact beliefs and proposal weights, and stops under a budget.

The strongest result is evidence localization rather than answer EM. On the controlled D500 setting, LENS reports **62.4% EM / 84.8% evidence recall** versus **65.2% / 50.4%** for ReAct-style search. On fixed fullwiki, EM is nearly tied while grounded answers favor LENS. The trade is better freshness/grounding for more online token and latency cost. The decisive systems question is lifecycle-matched cost against a maintained fresh index.

</details>

### [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](papers/2608.16370.md)
`Evaluation & Analysis` · `memory` `iterative search` · **4/5** · 2026-08-17

Removing context can simply move cost into the environment: fewer retained tokens may cause much more **reacquisition retrieval** while task completion looks unchanged.

[Paper](https://arxiv.org/abs/2608.16370) · [Research note](papers/2608.16370.md)

<details><summary><strong>How context compression shifts cost</strong></summary>

The paper separates execution tool calls from calls that reacquire state dropped by compression. Under a fixed 24-turn horizon, retrieval rises consistently as sliding compression becomes more aggressive; oracle restoration of the dropped queryable state removes most of that extra interaction.

One representative cell changes from **21.0 to 63.9 retrieval calls** while completion remains statistically similar. The negative boundary matters too: ALFWorld does not show the same surge. So “context saved” is not a cost metric by itself; production accounting should compare retained-state cost with the latency/money needed to fetch state again.

</details>

### [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](papers/2608.15191.md)
`Iterative Reasoning & Verification` · `adaptive stopping` `query rewrite` · **4/5** · 2026-08-15

RAAC makes **search progress observable** and uses coverage, novelty, query diversity, and drift to decide whether to continue, redirect, or stop.

[Paper](https://arxiv.org/abs/2608.15191) · [Research note](papers/2608.15191.md)

<details><summary><strong>How RAAC decides whether to continue, redirect, or stop</strong></summary>

Deep-research agents can keep searching after useful evidence saturates. RAAC overlays progress signals on the same underlying agent and triggers either continued search, stopping, or a critical re-thinker that generates a substantially different query.

On BrowseComp-Plus, the paper reports roughly **14 fewer search calls on average** and about **3 accuracy points** improvement across the tested agents. But the controller and re-thinker add LLM calls, so fewer searches are not yet a total-cost win. The decisive follow-up should match controller + retrieval tokens, latency, and monetary cost, not search-call count alone.

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2608.12888.md)
`Retrieval & Tool Use` · `memory` `iterative search` · **4/5** · 2026-08-13

Question-time access over raw chat can substitute for some pre-built memory structure when the interface exposes session, time, and local-context controls and lets the agent iterate on results.

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2608.12888.md)

<details><summary><strong>How ReFind searches raw chat logs</strong></summary>

ReFind keeps raw timestamped turns intact and exposes lexical search, neighboring context, session fusion, temporal filters, and seen-session state. This makes it a stronger control than one-shot BM25 when asking whether semantic memory structure is necessary.

Across six tasks the paper reports **58.2 mean accuracy**, versus **53.2 HippoRAG 2** and **48.8 BM25-RAG**. On LongMemEval-S/M, the full interface reaches **93.2/89.3**, beating matched generic multi-round BM25 and a one-search control. The open question is lifecycle-matched cost on semantic and acting-agent workloads.

</details>

### [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](papers/2608.11967.md)
`Learning & Optimization` · `backtracking` `RL` · **4/5** · 2026-08-12

LoongReflect makes active search state **reversible**: detect a contaminated branch, roll back to a trusted prefix, keep a corrective lesson, and resume.

[Paper](https://arxiv.org/abs/2608.11967) · [Research note](papers/2608.11967.md)

<details><summary><strong>How LoongReflect rolls back contaminated search state</strong></summary>

A wrong entity association or retrieved fact can contaminate many later actions. LoongReflect trains an agent to reflect, backtrack to a trusted state, preserve a corrective lesson, and continue rather than carrying the corrupted suffix forward.

For Qwen2.5-3B the paper reports **46.15 average F1** across seven RAG benchmarks versus **33.55** for AgenticRAG-R1. The attribution caveat is substantial: the teacher uses privileged global trajectory information, so the evidence supports the recovery-learning package more strongly than rollback semantics alone.

</details>

### [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](papers/2608.12282.md)
`Evaluation & Analysis` · `APIs` `documents` `cross-source grounding` · **4/5** · 2026-08-12

VAKRA evaluates whether API calls, document retrieval, multi-hop reasoning, and policy constraints remain coherent in one executable trajectory.

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/vakra) · [Research note](papers/2608.12282.md)

<details><summary><strong>How VAKRA tests cross-source execution</strong></summary>

API-use and document-QA benchmarks can each look strong while the combined agent fails at identity resolution, evidence grounding, or policy constraints. VAKRA re-executes predicted tool calls in a fixed harness and evaluates cross-source trajectories rather than final answers alone.

The best evaluated model reaches **70.4%** on single-hop endpoint-style tasks but only roughly **50–51%** on compositional APIs; some policy-constrained unanswerable settings fall to **2.4%**. This is a benchmark result, not evidence for one controller design. The next useful experiment should fix model/tools/budget and isolate which control change repairs cross-source grounding.

</details>

<a id="changes"></a>
<a id="whats-changing"></a>
<a id="-whats-changing"></a>
## Recent Research Shifts

| Shift | Evidence | Research implication |
|---|---|---|
| **Evidence materialization is now a first-class design variable.** | Indexed RAG pre-materializes chunks; DCI preserves raw files; LENS moves query-conditioned evidence localization online. | Compare freshness, evidence fidelity, and offline+online cost—not only answer quality. |
| **Progress and retained state are becoming explicit control state.** | RAAC exposes search progress; LoongReflect makes reasoning state reversible; context-compression work prices the re-query tax of dropped state. | State policy belongs in retrieval-cost attribution rather than being treated as runtime plumbing. |
| **A strong retrieval baseline includes the interface and harness.** | ReFind, Pi-Serini, and harness analyses show that search primitives, surfaced depth, and interaction protocol can significantly change the conclusion. | Match interface/harness before crediting “agentic retrieval.” |

Temporal views: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a>
## Field Map

`information need → query/planning → retrieval interface → evidence materialization → inspection/reasoning → continue/redirect/stop → persistent state → answer/action`

| Axis | Question | Current tension |
|---|---|---|
| **Adaptivity placement** | What can be compiled before evidence arrives, and what requires result-conditioned control? | `pre-query compilation ↔ query-time adaptation` |
| **Evidence materialization** | When should chunks/regions/workspaces become concrete? | `pre-materialized index ↔ raw/query-conditioned evidence` |
| **Interface resolution** | What operations and source state can the agent observe/control? | `opaque top-k ↔ explicit search/read/filter/navigation` |
| **State persistence** | Which evidence, progress, or reasoning state should survive? | `stateless loop ↔ persistent/recoverable state` |
| **Resource accounting** | What is actually cheaper? | `local retrieval metric ↔ lifecycle cost + task outcome` |

[Explore the research-question map →](categories/README.md) · [Evaluation view →](https://github.com/H20Zhang/Agent-Benchmark-Radar#rag-agentic-retrieval)

<a id="reading-paths"></a>
<a id="-reading-paths"></a>
## Reading Paths

| Question | Suggested path | What to learn |
|---|---|---|
| **Where should retrieval control and materialization live?** | [SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) | Some retrieval decisions can be compiled before retrieval; other information only becomes available after evidence is inspected; evidence granularity can itself be deferred until query time. |
| **What state should persist?** | [SGR-Bench](papers/2605.22219.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md) | Environment state, progress state, reversible reasoning state, and retained context have different failure costs. |
| **How do we make retrieval claims causal?** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [VAKRA](papers/2608.12282.md) | Backend, interface, harness, model, budget, and cross-source execution must be separated before attributing gains to retrieval policy. |

<a id="library"></a>
## Research Library

Browse earlier work by problem and design tension, by paper, or by date.

[Browse by problem / research line / year](library/README.en.md) · [Research-question map](categories/README.md) · [Curated chronological paper index](papers/README.md) · [Temporal synthesis](digests/README.md)

## Scope

In-scope work gives an agent meaningful control over whether, what, where, how, or how much external information to acquire, or changes the persistent information state that makes such control possible. Plain fixed RAG without a substantive control/interface/state contribution is usually outside scope.

## Maintenance

[Contributing](CONTRIBUTING.md) · [Curation](CURATION.md) · [Daily workflow](docs/DAILY_WORKFLOW.md)
