# Agentic RAG Radar

[中文](README.md) | **English**

A living research map of agent-controlled retrieval, evidence access, and information-state management.

Use this radar to answer: **where should retrieval intelligence live, when should evidence be materialized, what state should persist, and what does adaptivity actually buy?**

**Research Radar family:** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Timeline](#timeline) · [3 min: 7/30-day changes](#periods) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

**Status:** Last updated: **2026-08-25** · Last synthesized: **2026-08-25T02:53:28Z (UTC)**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## Latest Timeline

> **Migration notice:** Historic Radar acceptance timestamps were not stored for these six legacy records. They are ordered by original paper date and are not presented as newly accepted by the Radar. Post-v2 entries use `radar_published_at` while preserving `published_at`.

<a id="entry-2608.20627"></a>
<details><summary>2026-08-25 · AgenticRAG-FP · Resource accounting → causal failure attribution <!-- timefirst:area=causal-failure-attribution --> — Uses certified hop faults and counterfactual reruns to localize propagated retrieval failure. <!-- timefirst:delta=propagation-conditioned-failure-attribution --></summary>

**Question.** After failure changes later retrieval, which hop remains identifiable as the causal origin? <!-- timefirst:question=causal-hop-identification -->

**Evidence.** Exact hop signal: in strict dense Claude/MuSiQue, coverage is 0.91/0/0 and frozen-hop repair is 0.51/0.25/0.48. <!-- timefirst:evidence=failure-probes~exact-hop-signal -->

**Caveat.** Survivor conditioned comparison: only still-failed traces are scored, the clean corpus heals 54–85% of content faults, and active-probe compute is unmatched. <!-- timefirst:caveat=failure-boundary~survivor-conditioned-comparison -->

**Map.** `early_signal`: adds a propagation-conditioned attribution coordinate; one narrow matrix is not a durable direction.

**Links.** [When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation](https://arxiv.org/abs/2608.20627) · [Artifact](https://github.com/anote-ai/Research-AgenticRAG) · [English deep note](papers/2608.20627.md) · [中文深读](papers/2608.20627.zh.md)

</details>

<a id="entry-2608.20771"></a>
<details><summary>2026-08-25 · CAS · Adaptivity placement → conformal evidence-set sizing <!-- timefirst:area=conformal-evidence-set-sizing --> — Uses calibrated retrieval mass to adapt evidence-set size per search. <!-- timefirst:delta=query-conditioned-retrieval-width --></summary>

**Question.** Can top-k become a query-conditioned decision instead of a global constant? <!-- timefirst:question=adaptive-evidence-set-size -->

**Evidence.** Matched component ablations: Qwen2.5-3B full is 0.401, without ACI 0.384, and fixed top-k=3 0.389. <!-- timefirst:evidence=cas-components~matched-component-ablations -->

**Caveat.** Calibration correctness gap: 239 teacher-created queries do not establish cross-dataset exchangeability, and answer NLL is not factual correctness. <!-- timefirst:caveat=cas-guarantee~calibration-correctness-gap -->

**Map.** `early_signal`: adds conformal evidence-set sizing without turning marginal coverage guarantees into end-to-end reliability.

**Links.** [CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting](https://arxiv.org/abs/2608.20771) · [Code](https://github.com/S1llyBird/CAS) · [English deep note](papers/2608.20771.md) · [中文深读](papers/2608.20771.zh.md)

</details>

<a id="entry-2608.21690"></a>
<details><summary>2026-08-25 · Scroll · State persistence → programmatic context materialization <!-- timefirst:area=programmatic-context-materialization --> — Retains a lossless event log and materializes needed state only at query time. <!-- timefirst:delta=query-time-context-environment --></summary>

**Question.** Can an agent keep complete history recoverable while materializing only the context needed now? <!-- timefirst:question=lossless-query-time-context -->

**Evidence.** Persistent REPL ablation: BEAM10M full 73.1, no REPL 65.8, no index 71.3, and lossy ingestion 19.9. <!-- timefirst:evidence=scroll-mechanism~persistent-repl-ablation -->

**Caveat.** Unmatched lifecycle accounting: Scroll leads CodeAct by only 1.4 on LOCA-256K; cross-system comparisons and latency/storage/CPU/dollar cost are unmatched. <!-- timefirst:caveat=scroll-cost~unmatched-lifecycle-accounting -->

**Map.** `early_signal`: connects retained state with query-time materialization; no durable map edit without lifecycle evidence.

**Links.** [Context as an Environment: Programmatic Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.21690) · [Reproduction branch](https://github.com/niceIrene/QwenPaw/tree/scroll-research) · [English deep note](papers/2608.21690.md) · [中文深读](papers/2608.21690.zh.md)

</details>

<a id="entry-2608.21808"></a>
<details><summary>2026-08-25 · MCite-RL · Evidence materialization → visual localization reward <!-- timefirst:area=visual-evidence-localization --> — Trains explicit visual citations with final-box and terminal-crop reward. <!-- timefirst:delta=terminal-visual-citation-reward --></summary>

**Question.** Can a visual RAG agent learn to localize the image region supporting its answer? <!-- timefirst:question=visual-evidence-citation -->

**Evidence.** Citation reward ablation: 7B full answer/citation is 60.00/36.05 versus 54.20/20.56 without citation rewards. <!-- timefirst:evidence=mcite-reward~citation-reward-ablation -->

**Caveat.** Terminal crop supervision: the process reward uses only the terminal crop; 8.6% of teacher trajectories survive, and runtime accounting is incomplete. <!-- timefirst:caveat=mcite-process~terminal-crop-supervision -->

**Map.** `early_signal`: adds visual evidence-localization reward without equating box overlap with semantic support.

**Links.** [MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21808) · [English deep note](papers/2608.21808.md) · [中文深读](papers/2608.21808.zh.md)

</details>

<a id="entry-2608.22132"></a>
<details><summary>2026-08-25 · SSE-Bio · Adaptivity placement → dual-source routing <!-- timefirst:area=dual-source-retrieval-routing --> — Routes among KG, template, both, and none from structured gap state. <!-- timefirst:delta=structured-gap-source-selection --></summary>

**Question.** Which evidence source should the current biomedical reasoning gap trigger? <!-- timefirst:question=biomedical-source-placement -->

**Evidence.** Fixed policy comparison: learned Proxy single/multi Both_cor is 16.52/11.73 versus 13.18/9.02 for always-both. <!-- timefirst:evidence=sse-routing~fixed-policy-comparison -->

**Caveat.** Low absolute joint correctness: overall scores remain low, wrong Proxy is 13.1% of audited HLE failures, and each example averages 12.4K tokens and 6.7 calls. <!-- timefirst:caveat=sse-boundary~low-absolute-joint-correctness -->

**Map.** `early_signal`: adds structured-gap dual-source routing without crediting the Proxy for the full multi-agent package.

**Links.** [SSE-Bio: A Structured Self-Evolving Agent with Agentic Retrieval Policy for Multi-Hop Biomedical Reasoning](https://arxiv.org/abs/2608.22132) · [Code](https://github.com/ZhaohanM/SSE-Bio) · [English deep note](papers/2608.22132.md) · [中文深读](papers/2608.22132.zh.md)

</details>

<a id="entry-2608.22479"></a>
<details><summary>2026-08-25 · GTA-RAG · Adaptivity placement → evidence-chain supervision <!-- timefirst:area=evidence-chain-supervision --> — Converts graph paths into retriever-validated target trajectories before training. <!-- timefirst:delta=retriever-validated-trajectory-reward --></summary>

**Question.** Beyond answer-only reward, should complete evidence-chain acquisition be supervised directly? <!-- timefirst:question=evidence-chain-learning-target -->

**Evidence.** Trajectory reward ablation: full versus no trajectory reward gives 74.1 vs 58.7 full-chain and 49.7 vs 46.2 EM. <!-- timefirst:evidence=gta-trajectory~trajectory-reward-ablation -->

**Caveat.** Graph synthetic target distribution: the held-out test uses the same graph-path construction, only eight examples are four-hop, and external substrates/budgets are unmatched. <!-- timefirst:caveat=gta-transfer~graph-synthetic-target-distribution -->

**Map.** `early_signal`: adds retriever-validated evidence-chain supervision without assigning the graph+interface+data+RL package gain to reward alone.

**Links.** [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning](https://arxiv.org/abs/2608.22479) · [Code](https://github.com/cjcj46262/GTA-RAG) · [English deep note](papers/2608.22479.md) · [中文深读](papers/2608.22479.zh.md)

</details>

<a id="entry-2608.23252"></a>
<details><summary>2026-08-25 · ASCP · Adaptivity placement → context allocation <!-- timefirst:area=feedback-context-allocation --> — Separates fresh-evidence rotation from the feedback scheduler. <!-- timefirst:delta=fresh-evidence-allocation-factorial --></summary>

**Question.** Does repeated generation gain from context volume, fresh evidence, or feedback-conditioned selection? <!-- timefirst:question=context-allocation-causality -->

**Evidence.** Fresh evidence factorial: at `k=2,T=12`, rotation PR is 0.397 versus 0.257 for fixed reuse; equal-volume `(2,12)` beats `(24,1)` by 0.144. <!-- timefirst:evidence=ascp-allocation~fresh-evidence-factorial -->

**Caveat.** Scheduler rotation statistical tie: full ASCP is 0.309 versus 0.303 for deep rotation (`q=0.343`), with no matched resource delta. The 17.5s-versus-1.7s contrast is sequential `(2,12)` versus one-shot `(24,1)`. <!-- timefirst:caveat=ascp-attribution~scheduler-rotation-statistical-tie -->

**Map.** `early_signal`: adds fresh-evidence context allocation; the incremental value of feedback control is not established.

**Links.** [The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search](https://arxiv.org/abs/2608.23252) · [Code](https://github.com/PeiYangLiu/ascp) · [English deep note](papers/2608.23252.md) · [中文深读](papers/2608.23252.zh.md)

</details>

<a id="entry-2608.19652"></a>
<details><summary>2026-08-24 · StateMem · State persistence → supersession-aware state <!-- timefirst:area=supersession-aware-state --> — Separates retrieving history from deciding which facts and dependencies remain operative. <!-- timefirst:delta=supersession-aware-state-assembly --></summary>

**Question.** Can an agent assemble current state when retrieved history contains both superseded and operative facts? <!-- timefirst:question=evolving-state-assembly -->

**Evidence.** StateMem value chain structure: across six backends, StateMemWrapper attributes 15.0–31.7 points on StateMemBench beyond the same full transcript, chunks, call, and length budget. <!-- timefirst:evidence=statemem-control~statemem-value-chain-structure -->

**Caveat.** Synthetic benchmark upper bound: the benchmark targets the same lazy-reader failure family encoded by the method; full StateMem uses roughly 165–600 ingest LLM calls, dependency propagation can hurt, and LongMemEval structure gains are only −5 to +5 points with DeepSeek. <!-- timefirst:caveat=statemem-boundary~synthetic-benchmark-upper-bound -->

**Map.** `early_signal`: adds supersession-aware state assembly to State persistence; one benchmark/method package does not create a durable direction.

**Links.** [Can Agent Memory Systems Track Evolving State?](https://arxiv.org/abs/2608.19652) · [English deep note](papers/2608.19652.md) · [Chinese deep note](papers/2608.19652.zh.md)

</details>

<a id="entry-2608.18613"></a>
<details><summary>2026-08-21 · CTIFoundry · Interface resolution → agent-native corpus scaffold <!-- timefirst:area=agent-native-corpus-scaffold --> — Turns a flat corpus into named entities, relations, and typed evidence-path operations for the same underlying agent. <!-- timefirst:delta=typed-evidence-path-operations --></summary>

**Question.** Can a corpus scaffold and operation surface, without changing the agent, improve cross-document evidence navigation? <!-- timefirst:question=corpus-scaffold-operation-surface -->

**Evidence.** The four-model panel improves by 0.190–0.275 F1; GPT-5.4 rises from 0.610 flat base to 0.829 with tools+skills, with tools-only at 0.746 versus skills-only at 0.672. <!-- timefirst:evidence=ctifoundry-package~four-model-panel -->

**Caveat.** Tools skills bundled: the full treatment jointly changes graph/entity indexing, seven typed tools, tool outputs/descriptions, the system prompt, and user-turn skills; per-arm online cost and update lifecycle are unmatched. <!-- timefirst:caveat=ctifoundry-attribution~tools-skills-bundled -->

**Map.** `reinforces`: with VisDocAgentBench, strengthens explicit evidence-path operations under a shared output contract, without attributing the package gain to retrieval or planning alone.

**Links.** [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](https://arxiv.org/abs/2608.18613) · [English deep note](papers/2608.18613.md) · [Chinese deep note](papers/2608.18613.zh.md)

</details>

<a id="entry-2608.17889"></a>
<details><summary>2026-08-21 · VisDocAgentBench · Interface resolution → ranked visual retrieval <!-- timefirst:area=ranked-visual-retrieval --> — Uses the same top-10 opaque-page output to test static versus iterative visual target discovery. <!-- timefirst:delta=bridge-path-acquisition-benchmark --></summary>

**Question.** In page-level visual retrieval, can iterative visual target discovery repair the collapse from direct to complex targets? <!-- timefirst:question=iterative-visual-target-discovery -->

**Evidence.** In the iterative search ablation, GPT-5.6-sol visual R@1 rises from 53.33 without iteration to 61.67, while OCR rises from 27.50 to 36.67; the strongest static Nemotron reaches only 2.5% on L3. <!-- timefirst:evidence=visdoc-iteration~iterative-search-ablation -->

**Caveat.** Input token history is unmatched: the full visual agent uses about 177K input tokens versus 101K for the control; agents use a Qwen single-vector backend while the strongest static control uses Nemotron late interaction. <!-- timefirst:caveat=visdoc-attribution~input-token-history -->

**Map.** `reinforces`: with CTIFoundry, strengthens explicit evidence-path operations, while current evidence cannot isolate policy, retriever, and accumulated history.

**Links.** [VisDocAgentBench: Benchmarking Agents for Visually Rich Document Retrieval](https://arxiv.org/abs/2608.17889) · [Project](https://hulx2002.github.io/VisDocAgentBench/) · [Code](https://github.com/hulx2002/VisDocAgentBench) · [English deep note](papers/2608.17889.md) · [Chinese deep note](papers/2608.17889.zh.md)

</details>

<a id="entry-2608.16502"></a>
<details><summary>2026-08-21 · ToolScout · Interface resolution → capability retrieval <!-- timefirst:area=capability-retrieval --> — Shows how a tool retriever can mistake source style for capability match. <!-- timefirst:delta=source-style-capability-routing --></summary>

**Question.** When capability retrieval transfers to mixed tool sources, does failure come from agent planning or from missing candidate-tool recall upstream? <!-- timefirst:question=capability-retrieval-transfer -->

**Evidence.** Source-style collapse: a specialist retriever has 91.8% matched-source depth-20 coverage but only 22.3% mixed-source coverage; routing to source aggregators reaches 86.1%. <!-- timefirst:evidence=toolscout-transfer~source-style-collapse -->

**Caveat.** End-to-end execution missing: the study measures candidate coverage and proxy generation rather than executing tools to finish tasks; “source style” also mixes query–tool pairing with target-side distribution. <!-- timefirst:caveat=toolscout-scope~end-to-end-execution-missing -->

**Map.** `early_signal`: places a capability-coverage audit before agent planning; one transfer diagnosis does not establish a stable direction.

**Links.** [When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval](https://arxiv.org/abs/2608.16502) · [English deep note](papers/2608.16502.md) · [Chinese deep note](papers/2608.16502.zh.md)

</details>

<a id="entry-2608.16417"></a>
<details><summary>2026-08-21 · D2-ScaleAgent · Adaptivity placement → evidence-sufficiency routing <!-- timefirst:area=evidence-sufficiency-routing --> — Lets a verifier route between finding another page and reading a found page more deeply from an Evidence Bank. <!-- timefirst:delta=breadth-depth-evidence-routing --></summary>

**Question.** Can breadth versus depth allocation be controlled by current evidence sufficiency rather than by adding a fixed number of retrieval rounds? <!-- timefirst:question=breadth-versus-depth-allocation -->

**Evidence.** In the verifier loop ablation, GPT-4o scores 52.0 on MMLongBench with the full system, 44.1 without the verifier, 46.8 without retrieval scale, and 54.9 with the oracle. <!-- timefirst:evidence=d2-verifier~verifier-loop-ablation -->

**Caveat.** Unmatched adaptive compute: the full system itself uses 21.4K tokens, 16.22 seconds, and 5.02 routing-agent calls, but key controls lack matched costs; Gemini direct VQA is stronger on both main benchmarks. <!-- timefirst:caveat=d2-attribution~unmatched-adaptive-compute -->

**Map.** `early_signal`: adds controlled evidence for evidence-sufficiency routing without assigning a packaged visual-document-agent gain to the verifier alone.

**Links.** [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](https://arxiv.org/abs/2608.16417) · [English deep note](papers/2608.16417.md) · [Chinese deep note](papers/2608.16417.zh.md)

</details>

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
### Last 7 days · 2026-08-19—2026-08-25

- **`reinforced` · Evidence path operation surfaces · Explicit evidence-path operations gain cross-task support.** <!-- timefirst:direction key="evidence-path-operation-surfaces" state="reinforced" supports="2608.17889,2608.18613" confidence="medium" implication="make-evidence-path-operations-explicit" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="field-map" -->
  Supports: [VisDocAgentBench](#entry-2608.17889) · [CTIFoundry](#entry-2608.18613); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (make evidence path operations explicit): expose search / resolve / traverse / inspect / read under a shared output contract, then test against static controls with matched backend, harness, and budget; prior map evidence: [Interface resolution](#field-map).

- **`new_signal` · Evidence sufficiency routing · Evidence sufficiency can route breadth versus depth.** <!-- timefirst:direction key="evidence-sufficiency-routing" state="new_signal" supports="2608.16417" confidence="medium" implication="separate-page-coverage-from-reading-depth" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [D2-ScaleAgent](#entry-2608.16417); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (separate page coverage from reading depth): measure new-page coverage separately from deep inspection of found pages and charge verifier tokens, calls, and latency; prior map evidence: `none`.

- **`new_signal` · Source conditioned capability routing · Tool-capability recall is constrained by source distribution.** <!-- timefirst:direction key="source-conditioned-capability-routing" state="new_signal" supports="2608.16502" confidence="medium" implication="audit-capability-coverage-before-agent-planning" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [ToolScout](#entry-2608.16502); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (audit capability coverage before agent planning): verify candidate-tool coverage and cross-source transfer before assigning final failure to agent planning; prior map evidence: `none`.

- **`new_signal` · Supersession aware state assembly · Historical recall and operative-state assembly are separable.** <!-- timefirst:direction key="supersession-aware-state-assembly" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-recall-from-state-validity" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [StateMem](#entry-2608.19652); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (separate recall from state validity): match transcript access and answer cost while independently varying supersession, dependency propagation, and recomputation; prior map evidence: `none`.

- **`new_signal` · Fresh evidence context allocation · Fresh evidence, not scheduler complexity, is the current result.** <!-- timefirst:direction key="fresh-evidence-context-allocation" state="new_signal" supports="2608.23252" confidence="medium" implication="compare-freshness-with-feedback-under-matched-cost" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [ASCP](#entry-2608.23252); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (compare freshness with feedback under matched cost): match evidence, context, rounds, tokens, and latency; test rotation before the scheduler increment; prior map evidence: `none`.

- **`new_signal` · Retriever validated evidence chain supervision · Complete evidence chains become explicit learning targets.** <!-- timefirst:direction key="retriever-validated-evidence-chain-supervision" state="new_signal" supports="2608.22479" confidence="medium" implication="separate-chain-reward-from-retrieval-substrate" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [GTA-RAG](#entry-2608.22479); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (separate chain reward from retrieval substrate): fix graph, retriever, interface, data, and compute before varying trajectory reward; prior map evidence: `none`.

- **`new_signal` · Structured gap dual source routing · Explicit reasoning gaps can choose an evidence source.** <!-- timefirst:direction key="structured-gap-dual-source-routing" state="new_signal" supports="2608.22132" confidence="medium" implication="intervene-on-routing-separately-from-reasoning" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [SSE-Bio](#entry-2608.22132); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (intervene on routing separately from reasoning): match source inventory and orchestration, then intervene separately on routing, retrieval, and downstream reasoning; prior map evidence: `none`.

- **`new_signal` · Visual evidence localization rewards · Visual evidence regions enter the reward and output contract.** <!-- timefirst:direction key="visual-evidence-localization-rewards" state="new_signal" supports="2608.21808" confidence="medium" implication="validate-semantic-support-beyond-box-overlap" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [MCite-RL](#entry-2608.21808); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (validate semantic support beyond box overlap): match crop/search budgets and audit whether the box is grounded in answer evidence; prior map evidence: `none`.

- **`new_signal` · Query time programmatic context materialization · Lossless history can enter the prompt selectively at query time.** <!-- timefirst:direction key="query-time-programmatic-context-materialization" state="new_signal" supports="2608.21690" confidence="medium" implication="price-retention-querying-and-materialization-together" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [Scroll](#entry-2608.21690); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (price retention querying and materialization together): jointly charge retention, query programs, environment execution, and materialized prompts; prior map evidence: `none`.

- **`new_signal` · Conformal evidence set sizing · Calibrated score mass can adapt retrieval width.** <!-- timefirst:direction key="conformal-evidence-set-sizing" state="new_signal" supports="2608.20771" confidence="medium" implication="test-calibration-under-shift-and-realized-budgets" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [CAS](#entry-2608.20771); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (test calibration under shift and realized budgets): audit evidence validity under dataset shift and match realized documents, calls, tokens, and latency; prior map evidence: `none`.

- **`new_signal` · Propagation conditioned failure attribution · Retrieval failure needs live intervention for localization.** <!-- timefirst:direction key="propagation-conditioned-failure-attribution" state="new_signal" supports="2608.20627" confidence="medium" implication="report-healing-survivors-and-probe-costs" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [AgenticRAG-FP](#entry-2608.20627); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (report healing survivors and probe costs): report healed/failed trajectories, each depth denominator, and token/tool/latency cost for active probes; prior map evidence: `none`.

<a id="last-30-days"></a>
### Last 30 days · 2026-07-27—2026-08-25

- **`reinforced` · Evidence path operation surfaces · Explicit evidence-path operations gain cross-task support.** <!-- timefirst:direction key="evidence-path-operation-surfaces" state="reinforced" supports="2608.17889,2608.18613" confidence="medium" implication="make-evidence-path-operations-explicit" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="field-map" -->
  Supports: [VisDocAgentBench](#entry-2608.17889) · [CTIFoundry](#entry-2608.18613); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (make evidence path operations explicit): expose search / resolve / traverse / inspect / read under a shared output contract, then test against static controls with matched backend, harness, and budget; prior map evidence: [Interface resolution](#field-map).

- **`new_signal` · Evidence sufficiency routing · Evidence sufficiency can route breadth versus depth.** <!-- timefirst:direction key="evidence-sufficiency-routing" state="new_signal" supports="2608.16417" confidence="medium" implication="separate-page-coverage-from-reading-depth" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [D2-ScaleAgent](#entry-2608.16417); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (separate page coverage from reading depth): measure new-page coverage separately from deep inspection of found pages and charge verifier tokens, calls, and latency; prior map evidence: `none`.

- **`new_signal` · Source conditioned capability routing · Tool-capability recall is constrained by source distribution.** <!-- timefirst:direction key="source-conditioned-capability-routing" state="new_signal" supports="2608.16502" confidence="medium" implication="audit-capability-coverage-before-agent-planning" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [ToolScout](#entry-2608.16502); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (audit capability coverage before agent planning): verify candidate-tool coverage and cross-source transfer before assigning final failure to agent planning; prior map evidence: `none`.

- **`new_signal` · Supersession aware state assembly · Historical recall and operative-state assembly are separable.** <!-- timefirst:direction key="supersession-aware-state-assembly" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-recall-from-state-validity" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [StateMem](#entry-2608.19652); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (separate recall from state validity): match transcript access and answer cost while independently varying supersession, dependency propagation, and recomputation; prior map evidence: `none`.

- **`new_signal` · Fresh evidence context allocation · Fresh evidence, not scheduler complexity, is the current result.** <!-- timefirst:direction key="fresh-evidence-context-allocation" state="new_signal" supports="2608.23252" confidence="medium" implication="compare-freshness-with-feedback-under-matched-cost" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [ASCP](#entry-2608.23252); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (compare freshness with feedback under matched cost): match evidence, context, rounds, tokens, and latency; test rotation before the scheduler increment; prior map evidence: `none`.

- **`new_signal` · Retriever validated evidence chain supervision · Complete evidence chains become explicit learning targets.** <!-- timefirst:direction key="retriever-validated-evidence-chain-supervision" state="new_signal" supports="2608.22479" confidence="medium" implication="separate-chain-reward-from-retrieval-substrate" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [GTA-RAG](#entry-2608.22479); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (separate chain reward from retrieval substrate): fix graph, retriever, interface, data, and compute before varying trajectory reward; prior map evidence: `none`.

- **`new_signal` · Structured gap dual source routing · Explicit reasoning gaps can choose an evidence source.** <!-- timefirst:direction key="structured-gap-dual-source-routing" state="new_signal" supports="2608.22132" confidence="medium" implication="intervene-on-routing-separately-from-reasoning" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [SSE-Bio](#entry-2608.22132); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (intervene on routing separately from reasoning): match source inventory and orchestration, then intervene separately on routing, retrieval, and downstream reasoning; prior map evidence: `none`.

- **`new_signal` · Visual evidence localization rewards · Visual evidence regions enter the reward and output contract.** <!-- timefirst:direction key="visual-evidence-localization-rewards" state="new_signal" supports="2608.21808" confidence="medium" implication="validate-semantic-support-beyond-box-overlap" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [MCite-RL](#entry-2608.21808); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (validate semantic support beyond box overlap): match crop/search budgets and audit whether the box is grounded in answer evidence; prior map evidence: `none`.

- **`new_signal` · Query time programmatic context materialization · Lossless history can enter the prompt selectively at query time.** <!-- timefirst:direction key="query-time-programmatic-context-materialization" state="new_signal" supports="2608.21690" confidence="medium" implication="price-retention-querying-and-materialization-together" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [Scroll](#entry-2608.21690); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (price retention querying and materialization together): jointly charge retention, query programs, environment execution, and materialized prompts; prior map evidence: `none`.

- **`new_signal` · Conformal evidence set sizing · Calibrated score mass can adapt retrieval width.** <!-- timefirst:direction key="conformal-evidence-set-sizing" state="new_signal" supports="2608.20771" confidence="medium" implication="test-calibration-under-shift-and-realized-budgets" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [CAS](#entry-2608.20771); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (test calibration under shift and realized budgets): audit evidence validity under dataset shift and match realized documents, calls, tokens, and latency; prior map evidence: `none`.

- **`new_signal` · Propagation conditioned failure attribution · Retrieval failure needs live intervention for localization.** <!-- timefirst:direction key="propagation-conditioned-failure-attribution" state="new_signal" supports="2608.20627" confidence="medium" implication="report-healing-survivors-and-probe-costs" timing="radar_published_at" synthesized="2026-08-25T02:53:28Z" prior="none" -->
  Supports: [AgenticRAG-FP](#entry-2608.20627); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-08-25T02:53:28Z` (UTC); Research-design implication (report healing survivors and probe costs): report healed/failed trajectories, each depth denominator, and token/tool/latency cost for active probes; prior map evidence: `none`.

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
| **Interface resolution** | What operations and source state can the agent observe/control? | `opaque top-k ↔ explicit search/resolve/traverse/inspect/read under shared output contract` |
| **State persistence** | Which evidence, progress, or reasoning state should survive? | `stateless loop ↔ persistent/recoverable state` |
| **Resource accounting** | What is actually cheaper? | `local retrieval metric ↔ lifecycle cost + task outcome` |

[Explore the research-question map →](categories/README.en.md) · [Research-question visual](assets/editorial/research-question-map.svg) · [Evaluation view →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-rag)

<a id="reading-paths"></a>
## Reading Paths

| Question | Suggested path | What to learn |
|---|---|---|
| **Where should retrieval control and materialization live?** | [SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) → [ASCP](papers/2608.23252.md) | Move from pre-query compilation through result-conditioned access and query-time localization to fresh evidence allocation across rounds; ask where the work moved each time. |
| **What state should persist?** | [SGR-Bench](papers/2605.22219.md) → [StateMem](papers/2608.19652.md) → [Context Compression Cost](papers/2608.16370.md) → [Scroll](papers/2608.21690.md) | External source state, operative validity, reacquisition cost, and lossless programmatic state are different retained-state problems. |
| **How do we make retrieval claims causal?** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [VAKRA](papers/2608.12282.md) → [AgenticRAG-FP](papers/2608.20627.md) | Trace the causal path from evidence coverage and matched interface/harness through cross-source execution to live fault intervention. |

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
