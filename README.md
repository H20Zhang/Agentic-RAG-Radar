# Agentic RAG Radar

*A continuously curated research map of adaptive retrieval, search agents, and retrieval-aware agent systems.*

**Current thesis.** Agentic retrieval is increasingly a **placement-of-work** problem: what should be precomputed, what evidence should be materialized only after the query arrives, what state is worth retaining, and what apparent savings merely reappear as localization, controller, or reacquisition cost.

**Last research update:** 18 Aug 2026 · [Latest Papers](#latest-papers) · [What's Changing](#whats-changing) · [Reading Paths](#reading-paths) · [Research Map](#research-map) · [Paper Index](papers/README.md)

<p align="center">
  <img src="assets/editorial/field-overview.svg" alt="Agentic RAG as placement of information work across precompute, materialization, adaptivity, state retention, localization, and reacquisition" width="100%">
</p>

## Latest Papers

### [LENS — In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](papers/2608.16185.md)
*17 Aug 2026 · Retrieval & Tool Use · Importance 4/5 · Full-text reviewed*

**Why it matters.** LENS moves **evidence materialization itself** from indexing time to query time: raw-document regions remain latent until the information need is known.

**Key result.** On the controlled 500-question setting, evidence recall rises from **50.4% with ReAct-style search to 84.8% with LENS**; stale-index experiments also expose the freshness advantage.

**The catch.** ReAct is slightly better on D500 answer EM (**65.2 vs 62.4**), fullwiki answer EM is nearly tied, and LENS spends more online tokens/latency. The defensible claim is better evidence localization and freshness—not universal answer-quality or cost superiority.

[Paper](https://arxiv.org/abs/2608.16185) · [Deep research note](papers/2608.16185.md)

<details>
<summary><strong>Research snapshot</strong></summary>

**Research question.** When a corpus changes frequently or the useful evidence granularity is query-dependent, should evidence units exist before the query at all?

**Mechanism.** `query-conditioned prior → propose raw-document regions → inspect relevance → update beliefs/proposal mix → continue or stop under budget → consolidate grounded evidence`

**Nearest design point.** Fresh/stale indexed RAG and matched index-free ReAct-style search over the same raw corpus snapshot.

**Evidence & attribution.** The strongest evidence is the separation between answer accuracy and evidence quality: LENS substantially improves evidence recall/grounding without improving D500 answer EM. The sequential-exploration ablation matters more than every prior heuristic, and lifecycle cost remains unmatched.

**Open question.** Under the same changing corpus and total offline+online compute, where is the crossover between persistent indexing and query-time evidence localization?

</details>

---

### [What Does Context Compression Cost an Agent?](papers/2608.16370.md)
*17 Aug 2026 · Evaluation & Analysis · Importance 4/5 · Full-text reviewed*

**Why it matters.** It shows that **smaller context can create more retrieval**: dropped execution state may simply be bought back through external tool calls.

**Key result.** At `5×` compression, retrieval rises in all six model-regime cells while completion changes are not significant; for GPT-5.5 High, retrieval jumps **21.0 → 63.9 calls** while completion changes **80% → 85%**.

**The catch.** The effect is environment-dependent: the same sliding compression produces no retrieval surge in ALFWorld. Retrieval-call count is also not a complete latency or monetary cost model.

[Paper](https://arxiv.org/abs/2608.16370) · [Deep research note](papers/2608.16370.md)

<details>
<summary><strong>Research snapshot</strong></summary>

**Research question.** What state should an agent retain because reacquiring it is more expensive than keeping it?

**Mechanism.** `state dropped → information needed again → re-query environment → resume task`; oracle restoration of dropped queryable state short-circuits the loop.

**Nearest design point.** Full context, sliding compression, fact-preserving summary at the same compression ratio, and oracle restoration of different state classes.

**Evidence & attribution.** Restoring dropped queryable state removes most of the extra interaction in the strongest setting, providing unusually clean causal evidence that state-retention policy changes realized retrieval work.

**Open question.** Can a production agent learn a retention policy from expected `state size × future reuse × reacquisition cost` rather than salience alone?

</details>

---

### [RAAC — When Deep Research Agents Stagnate](papers/2608.15191.md)
*15 Aug 2026 · Iterative Reasoning & Verification · Importance 4/5 · Full-text reviewed*

**Why it matters.** RAAC makes **search progress observable** through coverage, novelty, query diversity, and drift, then turns those signals into `continue / redirect / stop` decisions.

**Key result.** Across seven deep-research agents on BrowseComp-Plus, RAAC reports roughly **14 fewer searches on average** and about **+3 accuracy points** on average, with same-agent overlay comparisons providing a relatively strong control.

**The catch.** Search-call savings are not total-cost savings: the controller and critical re-thinker add Claude calls, and several agent/dataset cells move in the wrong direction.

[Paper](https://arxiv.org/abs/2608.15191) · [Deep research note](papers/2608.15191.md)

<details>
<summary><strong>Research snapshot</strong></summary>

**Research question.** What state tells a long-running search agent that exploration has saturated or drifted?

**Mechanism.** `search → update coverage/novelty/diversity/alignment → continue | redirect | stop → retrieve or answer`

**Nearest design point.** The same seven DRA families without the retrieval-aware overlay, plus narrower stopping/trigger controllers.

**Evidence & attribution.** Within-agent comparisons isolate the overlay better than a fresh end-to-end architecture would, but `intervene` still bundles progress signals with extra reasoning capacity from the re-thinker.

**Open question.** Does progress-aware control still win when total controller + retrieval tokens, latency, and model calls are fully charged?

</details>

---

### [ReFind — Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2608.12888.md)
*13 Aug 2026 · Retrieval & Tool Use · Importance 4/5 · Full-text reviewed*

**Why it matters.** ReFind shows that some semantic memory structure can be replaced by **question-time control over the raw archive** when the interface exposes session, time, local context, and seen-state semantics.

**Key result.** On LongMemEval-S/M, the full interface reaches **93.2 / 89.3**, versus **78.7 / 82.2** for matched generic multi-round BM25 and **84.7 / 68.9** for a one-search control.

**The catch.** EventQA slightly favors single-shot BM25, and avoiding semantic preprocessing shifts work online: ReFind still spends multiple searches and LLM calls per query.

[Paper](https://arxiv.org/abs/2608.12888) · [Deep research note](papers/2608.12888.md)

<details>
<summary><strong>Research snapshot</strong></summary>

**Research question.** Which memory workloads should precompute semantic structure, and which should preserve raw history and defer intelligence until the future question is known?

**Mechanism.** `form keywords/time scope → search raw turns → inspect expanded session context → save evidence → reformulate → skip seen sessions → stop → answer`

**Nearest design point.** Structured memory systems, single-shot BM25-RAG, matched generic multi-round BM25, and a forced one-search control.

**Evidence & attribution.** The matched generic-agentic and one-search controls separate interface quality from mere iteration more cleanly than the headline comparison against heterogeneous memory systems.

**Open question.** Where is the lifecycle crossover between semantic memory construction/update cost and runtime multi-round refinding cost?

</details>

---

### [LoongReflect — Long-Horizon Reflection with Reversible Search State](papers/2608.11967.md)
*12 Aug 2026 · Learning & Optimization · Importance 4/5 · Full-text reviewed*

**Why it matters.** The meaningful delta is not generic reflection: LoongReflect makes **active execution state reversible**, allowing the agent to remove a contaminated suffix, preserve a corrective lesson, and resume from a trusted prefix.

**Key result.** In the Qwen2.5-3B setting, the paper reports **46.15 average F1** across seven RAG benchmarks versus **33.55** for AgenticRAG-R1, with component ablations supporting reflection/backtracking and both training channels.

**The catch.** The teacher has privileged global trajectory information during training, so the evidence supports the full recovery-learning package more strongly than rollback semantics alone.

[Paper](https://arxiv.org/abs/2608.11967) · [Deep research note](papers/2608.11967.md)

<details>
<summary><strong>Research snapshot</strong></summary>

**Research question.** How should a search agent recover after an early retrieval/entity mistake contaminates later reasoning?

**Mechanism.** `reason/retrieve → reflect → continue or backtrack → restore trusted prefix + corrective lesson → resume → answer`

**Nearest design point.** Outcome-only search-agent RL and linear-context reflection methods without explicit removal of a bad active-state suffix.

**Evidence & attribution.** The retrieval environment/tool budgets are held comparatively fixed, but state representation, rollback action space, and privileged recovery supervision remain partly bundled.

**Open question.** How much of the gain survives when rollback semantics and supervision privilege are varied independently?

</details>

---

### [VAKRA — Multi-Hop Reasoning Across APIs and Retrieval](papers/2608.12282.md)
*12 Aug 2026 · Evaluation & Analysis · Importance 4/5 · Full-text reviewed*

**Why it matters.** VAKRA evaluates **cross-source composition** rather than another agent architecture: APIs, document retrieval, entity identity, and tool-use policies must remain coherent in one executable trajectory.

**Key result.** The best evaluated model reaches **70.4%** on single-hop endpoint-style tasks but only about **50–51%** on compositional APIs; some policy-constrained unanswerable settings fall to **2.4%**.

**The catch.** The benchmark diagnoses where trajectories fail but does not identify which controller, memory, or retrieval intervention repairs those failures.

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/vakra) · [Deep research note](papers/2608.12282.md)

<details>
<summary><strong>Research snapshot</strong></summary>

**Research question.** Can an agent keep source identity, evidence, policy constraints, and multi-hop reasoning coherent when information comes from both executable APIs and documents?

**Mechanism.** `interpret task/policy → choose API or document retrieval → observe structured/unstructured evidence → resolve entities → continue, abstain, or answer`

**Nearest design point.** API-only tool-use suites, document-only RAG benchmarks, and final-answer evaluation without executable trajectory replay.

**Evidence & attribution.** A fixed ReAct harness helps isolate model capability, and trace analysis points toward entity disambiguation/cross-source grounding rather than API syntax alone; however the benchmark still bundles several trajectory failure stages.

**Open question.** Which single intervention repairs the largest fraction of cross-source failures when model, tools, and total interaction budget are fixed?

</details>

## What's Changing

Recent papers matter only when they change the field model. The homepage therefore keeps **one current synthesis per time scale** rather than replaying the digest archive.

| Horizon | Research question | Current synthesis |
|---|---|---|
| **This week** | What new evidence changed the map? | **Work can move rather than disappear.** LENS moves evidence materialization online; RAAC trades searches for progress-aware controller work; context compression can move prompt cost into state reacquisition. [W34 →](digests/weekly/2026-W34.md) |
| **This month** | What design space is emerging? | **Precompute/materialize/retain ↔ defer/localize/reacquire** is becoming a common systems axis across retrieval, memory, and control. [August map →](digests/monthly/2026-08.md) |
| **2026 YTD** | What looks durable? | Agentic retrieval is becoming explicit design of the **information environment**: evidence availability, corpus interface, observable state, adaptive control, and lifecycle resources. [2026 map →](digests/yearly/2026.md) |

[Browse the research synthesis archive →](digests/README.md)

## Reading Paths

### Where should retrieval intelligence live?

[SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) → [RARG](papers/2607.24223.md)

**Progression.** Compile corpus-aware actions before evidence → expose higher-resolution corpus operations → defer control to question-time raw-history search → defer evidence boundaries themselves → reintroduce relevance as guidance inside interaction.

### What state should persist—and what can be reacquired?

[SGR-Bench](papers/2605.22219.md) → [S2G-RAG](papers/2604.23783.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md)

**Progression.** External retrieval state → explicit missing-evidence state → progress/stagnation state → reversible active reasoning state → recoverability and reacquisition cost.

### What makes an agentic-retrieval evaluation causal?

[Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [Context Compression Cost](papers/2608.16370.md) → [VAKRA](papers/2608.12282.md)

**Progression.** Evidence must exist → backend exposure differs from agent inspection → harness/delivery can flip conclusions → retained state changes realized interaction → cross-source trajectory composition adds another failure surface.

<details>
<summary><strong>If you only read three papers</strong></summary>

**SIRA** shows that some apparent search intelligence can be compiled before evidence is read. **LENS** gives the dynamic-document counterpoint by moving evidence localization itself to query time. **Context Compression Cost** then shows why moving state out of the prompt is not automatically cheaper—the agent may buy it back through retrieval.

Together they motivate the current systems view: **materialization placement × adaptivity placement × state recoverability × lifecycle cost**.

</details>

## Research Map

<p align="center">
  <img src="assets/editorial/research-question-map.svg" alt="Six live research questions organizing Agentic RAG" width="100%">
</p>

The radar is organized first by **questions whose answers can change**, not by fashionable method labels.

| Research question | Current view | What would change our mind? |
|---|---|---|
| <img src="assets/editorial/icons/adaptivity.svg" width="20"> **Where should adaptivity live?** | Compile decisions when discriminative corpus signals are observable before retrieval; react online when the next action depends on newly exposed evidence. | Same substrate/model/total compute comparing compiled, one-shot, and result-conditioned control. |
| <img src="assets/editorial/icons/materialization.svg" width="20"> **When should evidence be materialized?** | Stable corpora favor offline structure; dynamic or query-dependent evidence may justify query-time localization. | Same update stream and lifecycle budget across indexed, direct-interaction, and latent-localization designs. |
| <img src="assets/editorial/icons/state.svg" width="20"> **What state should persist?** | State value depends on future reuse, recoverability, and reacquisition cost—not size alone. | Counterfactual state restoration plus measured context/tool/latency cost. |
| <img src="assets/editorial/icons/interface.svg" width="20"> **How should the corpus be exposed?** | Ranking, surfaced depth, operations, structure, and read granularity are separable interface choices. | Factorized backend × interface × read-resolution experiments. |
| <img src="assets/editorial/icons/learning.svg" width="20"> **What should be learned?** | Retriever utility, query/refinement policy, recovery, budget allocation, and task generation are different learning objects. | Same environment/state/action space while varying learned component and supervision independently. |
| <img src="assets/editorial/icons/evaluation.svg" width="20"> **What makes evaluation causal?** | Evidence coverage, interface, state, harness, realized resources, model, and historical baseline must be separated before crediting policy. | Executable factorial benchmark with counterfactual repair of intermediate failures. |

[Explore the full Research Map →](categories/README.md) · [Browse every curated paper →](papers/README.md)

## How to Read the Radar

**Scan.** Latest Papers gives the delta, strongest result, and strongest caveat without requiring the paper note.

**Understand.** Research snapshots and figures explain the mechanism, nearest design point, attribution, and open question.

**Assess.** Deep research notes preserve full-text evidence, negative results, resource mismatches, ablations, lineage, and the next decisive experiment.

## What Counts as Agentic RAG?

A work is included when **external retrieval/search/context acquisition is substantive and an agent, controller, or learned policy materially changes whether, what, where, how, or how much information is acquired**.

Fixed `retrieve top-k → generate` pipelines are not included merely because they use an LLM. Generic agents are excluded when retrieval is incidental. Pure retriever/reranker/index work is excluded unless adaptive information-access control is itself part of the research contribution.

## About

This is a **curated research map, not an exhaustive paper feed**. Every important inclusion should help answer three questions:

1. **What actually changed?**
2. **Compared with what—including stronger historical/design predecessors?**
3. **Does the evidence isolate the claimed cause?**

Negative results are kept when they change the interpretation of a paper. Relevance and importance are judged separately.

⭐ **Star the repository if this research map is useful to your work.**

## Contributing

Corrections are especially valuable when they change the conclusion: a missing baseline, unmatched resource budget, wrong taxonomy, overclaimed novelty, broken provenance, or a visual that implies more than the evidence supports.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar, evidence standard, and paper-suggestion process.

---

Found an important Agentic RAG paper we missed? [Suggest it](../../issues/new?template=suggest-paper.yml).
