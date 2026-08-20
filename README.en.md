# Agentic RAG Radar

[中文](README.md) | **English**

A living research map of agent-controlled retrieval, evidence access, and information-state management.

Use this radar to answer: **where should retrieval intelligence live, when should evidence be materialized, what state should persist, and what does adaptivity actually buy?**

**Research Radar family:** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Timeline](#timeline) · [3 min: 7/30-day changes](#periods) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

**Status:** Last updated: **2026-08-20** · Last synthesized: **2026-08-20T00:00:00Z (UTC)**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## Latest Timeline

> **Migration notice:** Historic Radar acceptance timestamps were not stored for these six legacy records. They are ordered by original paper date and are not presented as newly accepted by the Radar. Post-v2 entries use `radar_published_at` while preserving `published_at`.

<a id="entry-2608.16185"></a>
<details><summary>2026-08-17 · LENS · Evidence materialization <!-- timefirst:area=evidence-materialization --> — Moves evidence boundaries from pre-indexing to budgeted query-time localization over raw documents. <!-- timefirst:delta=query-time-raw-region-localization --></summary>

**Question.** Under dynamic corpora, how does fixed chunk/index retrieval compare with query-time raw-document localization at attributable cost? <!-- timefirst:question=dynamic-evidence-localization -->

**Evidence.** On D500, LENS reports 62.4% EM / 84.8% evidence localization recall versus 65.2% / 50.4% for ReAct-style search; the load-bearing gain is localization and grounding, not answer EM. <!-- timefirst:evidence=lens-grounding~evidence-localization-recall -->

**Caveat.** Online proposal and relevance-oracle work adds online token latency, and lifecycle-matched comparison against maintaining a fresh index remains missing. <!-- timefirst:caveat=lens-cost~online-token-latency -->

**Map.** `early_signal`: enters the Evidence materialization axis without letting one paper rewrite the durable map.

**Links.** [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](https://arxiv.org/abs/2608.16185) · [English deep note](papers/2608.16185.md) · [Chinese deep note](papers/2608.16185.zh.md)

</details>

<a id="entry-2608.16370"></a>
<details><summary>2026-08-17 · Context Compression Cost · Resource accounting → context reacquisition <!-- timefirst:area=state-persistence-cost --> — Shows that context compression can transfer token cost into later reacquisition retrieval. <!-- timefirst:delta=compression-reacquisition-tax --></summary>

**Question.** When completion stays similar, does context compression create retrieval cost by dropping externally queryable state? <!-- timefirst:question=compression-reacquisition-cost -->

**Evidence.** In one representative fixed 24-turn cell, retrieval calls surge from 21.0 to 63.9 with no significant completion change; restoring dropped queryable state removes most extra interaction. <!-- timefirst:evidence=compression-cost~retrieval-calls-surge -->

**Caveat.** The ALFWorld negative boundary does not show the same surge, and call count is not a complete wall-clock or monetary cost model. <!-- timefirst:caveat=environment-boundary~alfworld-negative-boundary -->

**Map.** `early_signal`: puts retained state and reacquisition cost in one accounting frame without manufacturing a trend from one result.

**Links.** [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](https://arxiv.org/abs/2608.16370) · [English deep note](papers/2608.16370.md) · [Chinese deep note](papers/2608.16370.zh.md)

</details>

<a id="entry-2608.15191"></a>
<details><summary>2026-08-15 · RAAC · State persistence → progress control <!-- timefirst:area=progress-control --> — Makes coverage, novelty, query diversity, and drift explicit inputs to continue / redirect / stop. <!-- timefirst:delta=observable-search-progress --></summary>

**Question.** Can the same deep-research agent observe saturation and redirect or stop rather than continue stagnant search? <!-- timefirst:question=stagnation-control -->

**Evidence.** BrowseComp-Plus search calls fall by about 14 on average while accuracy rises by about 3 points; the control compares each underlying agent with and without the RAAC overlay. <!-- timefirst:evidence=raac-overlay~browsecomp-plus-search-calls -->

**Caveat.** Controller rethinker cost includes extra LLM calls, so fewer searches are not yet lower total compute; effects also vary across agent/dataset cells. <!-- timefirst:caveat=raac-cost~controller-rethinker-cost -->

**Map.** `early_signal`: strengthens progress state as a control surface; the claim still requires resource matching and intervention decomposition.

**Links.** [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](https://arxiv.org/abs/2608.15191) · [English deep note](papers/2608.15191.md) · [Chinese deep note](papers/2608.15191.zh.md)

</details>

<a id="entry-2608.12888"></a>
<details><summary>2026-08-13 · ReFind · Interface resolution → raw-chat retrieval <!-- timefirst:area=retrieval-interface --> — Shows that chat-native controls plus iterative access can let raw archives replace some pre-built semantic memory. <!-- timefirst:delta=raw-chat-runtime-access --></summary>

**Question.** Under matched runtime control, how much benefit comes from pre-built semantic structure versus an agent-operable session/time/local-context interface? <!-- timefirst:question=structure-versus-interface -->

**Evidence.** In the LongMemEval interface ablation, the full interface reaches 93.2/89.3 versus 78.7/82.2 for generic multi-round BM25 and 84.7/68.9 for one-search; six-task mean accuracy is 58.2. <!-- timefirst:evidence=refind-interface~longmemeval-interface-ablation -->

**Caveat.** Lifecycle cost unmatched: the evidence is mainly text chat, with roughly 2.5–2.6 searches and 5 LLM calls per query, and does not make structured memory universally unnecessary. <!-- timefirst:caveat=refind-scope~lifecycle-cost-unmatched -->

**Map.** `early_signal`: enters Interface resolution; it supports strong runtime controls, not retirement of semantic structure.

**Links.** [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](https://arxiv.org/abs/2608.12888) · [English deep note](papers/2608.12888.md) · [Chinese deep note](papers/2608.12888.zh.md)

</details>

<a id="entry-2608.11967"></a>
<details><summary>2026-08-12 · LoongReflect · State persistence → reversible search state <!-- timefirst:area=reversible-search-state --> — Lets an agent roll back a contaminated branch, retain a corrective lesson, and resume retrieval. <!-- timefirst:delta=trajectory-rollback-control --></summary>

**Question.** Can long-horizon search remove an unreliable trajectory suffix instead of letting wrong evidence contaminate later actions? <!-- timefirst:question=reversible-trajectory-recovery -->

**Evidence.** Qwen2.5-3B reports 46.15 seven benchmark F1 versus 33.55 for AgenticRAG-R1; component ablations under fixed retrieval environment/tool budgets support the combined reflection/backtracking and two-channel training package. <!-- timefirst:evidence=loongreflect-package~seven-benchmark-f1 -->

**Caveat.** Privileged teacher information includes the global trajectory during training, so current evidence cannot attribute the full gain to rollback semantics alone. <!-- timefirst:caveat=loongreflect-attribution~privileged-teacher-information -->

**Map.** `early_signal`: adds reversible state to the control surface; one recovery-learning package is not a durable trend.

**Links.** [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](https://arxiv.org/abs/2608.11967) · [English deep note](papers/2608.11967.md) · [Chinese deep note](papers/2608.11967.zh.md)

</details>

<a id="entry-2608.12282"></a>
<details><summary>2026-08-12 · VAKRA · Interface resolution → cross-source evaluation <!-- timefirst:area=cross-source-evaluation --> — Places APIs, document retrieval, policy, and multi-hop reasoning in one replayable trajectory. <!-- timefirst:delta=executable-cross-source-trajectory --></summary>

**Question.** In a fixed harness, can a model acquire evidence across APIs and documents while preserving entity grounding, policy compliance, and multi-hop composition? <!-- timefirst:question=cross-source-grounding -->

**Evidence.** The best model reaches 70.4% on single-hop tasks but roughly 50–51% compositional API accuracy, while some policy-constrained unanswerable settings fall to 2.4%; predicted tool calls are re-executed. <!-- timefirst:evidence=vakra-depth~compositional-api-accuracy -->

**Caveat.** The fixed ReAct harness isolates model capability but cannot identify which planner, memory, or retrieval controller would repair failures; aggregate trajectories still bundle causes. <!-- timefirst:caveat=vakra-attribution~fixed-react-harness -->

**Map.** `early_signal`: adds a cross-source evaluation coordinate without treating benchmark difficulty as evidence for a controller.

**Links.** [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/vakra) · [English deep note](papers/2608.12282.md) · [Chinese deep note](papers/2608.12282.zh.md)

</details>

<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>
## 7-day / 30-day Changes

Directions use Radar acceptance time only. Legacy papers remain Field Map context but cannot masquerade as rolling-window support.

<a id="last-7-days"></a>
### Last 7 days · 2026-08-14—2026-08-20

- **`no_material_change` · RAG Radar acceptance time has no reportable change.** <!-- timefirst:direction key="rag-radar-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  Supports: **none**; confidence: **high**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-20T00:00:00Z` (UTC); Research-design implication (require native v2 times for period claims): only native Radar acceptance times can support a window claim; prior map evidence: `none`.

<a id="last-30-days"></a>
### Last 30 days · 2026-07-22—2026-08-20

- **`no_material_change` · RAG Radar acceptance time has no reportable change.** <!-- timefirst:direction key="rag-radar-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  Supports: **none**; confidence: **high**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-20T00:00:00Z` (UTC); Research-design implication (require native v2 times for period claims): only native Radar acceptance times can support a window claim; prior map evidence: `none`.

Closed periods and longer compaction: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a><a id="research-map"></a>
## Field Map

![Agentic RAG field design axes](assets/editorial/field-overview.svg)

> **Beginner mental model.** `need information → search/access evidence → inspect → decide where/if to search again → answer or act`
>
> **Current thesis.** The useful design variables are not simply “retriever vs agent” or “one search vs many.” They are **where adaptivity lives, when evidence becomes materialized, what state survives between actions, and which offline + online resources are spent**.

`information need → query/planning → retrieval interface → evidence materialization → inspection/reasoning → continue/redirect/stop → persistent state → answer/action`

| Axis | Question | Current tension |
|---|---|---|
| **Adaptivity placement** | What can be compiled before evidence arrives, and what requires result-conditioned control? | `pre-query compilation ↔ query-time adaptation` |
| **Evidence materialization** | When should chunks/regions/workspaces become concrete? | `pre-materialized index ↔ raw/query-conditioned evidence` |
| **Interface resolution** | What operations and source state can the agent observe/control? | `opaque top-k ↔ explicit search/read/filter/navigation` |
| **State persistence** | Which evidence, progress, or reasoning state should survive? | `stateless loop ↔ persistent/recoverable state` |
| **Resource accounting** | What is actually cheaper? | `local retrieval metric ↔ lifecycle cost + task outcome` |

[Explore the research-question map →](categories/README.en.md) · [Research-question visual](assets/editorial/research-question-map.svg) · [Evaluation view →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-rag)

<a id="reading-paths"></a>
## Reading Paths

| Question | Suggested path | What to learn |
|---|---|---|
| **Where should retrieval control and materialization live?** | [SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) | Some retrieval decisions can be compiled before retrieval; other information only becomes available after evidence is inspected; evidence granularity can itself be deferred until query time. |
| **What state should persist?** | [SGR-Bench](papers/2605.22219.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md) | Environment state, progress state, reversible reasoning state, and retained context have different failure costs. |
| **How do we make retrieval claims causal?** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [VAKRA](papers/2608.12282.md) | Backend, interface, harness, model, budget, and cross-source execution must be separated before attributing gains to retrieval policy. |

<a id="library"></a>
## Research Library

Browse earlier work by problem and design tension, or look it up by paper or date.

[Browse by problem / research line / year](library/README.en.md) · [Research-question map](categories/README.en.md) · [Curated chronological paper index](papers/README.md) · [Temporal synthesis](digests/README.md)

## How to Use This Radar

**Scan** the collapsed Timeline lines. **Expand** the question, evidence, caveat, and map consequence. **Deep dive** into a paper note when you need to audit the claim. Use the Field Map or Library when you have a research question but no paper name.

## Scope

In-scope work gives an agent meaningful control over whether, what, where, how, or how much external information to acquire, or changes the persistent information state that makes such control possible. Plain fixed RAG without a substantive control/interface/state contribution is usually outside scope.

## Maintenance

This is a curated research map rather than an exhaustive feed. The evidence bar is: **what changed, compared with what, what was actually held fixed, and what remains confounded?**

[Contributing](CONTRIBUTING.md) · [Curation](CURATION.md) · [Daily workflow](docs/DAILY_WORKFLOW.md)
