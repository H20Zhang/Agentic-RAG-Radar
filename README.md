# 🤖 Agentic RAG Radar

**A living research map of Agentic Retrieval-Augmented Generation.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-18 · [Latest papers](#-latest-papers) · [Start here](#-start-here) · [Browse by research problem](categories/README.md) · [Research compactions](#-research-compactions)

**Current field thesis:** the useful question is no longer “retriever or agent?” or “one search or many?” It is **where information and state should be materialized, and where adaptivity should live**: compile structure before retrieval when it is stable and observable; defer localization/control until after evidence arrives when the next action depends on fresh information; preserve enough recoverable state that compression does not merely shift cost into re-querying.

## 🔥 Latest Papers

### [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](papers/2608.16185.md)
`Retrieval & Tool Use` · `documents` `iterative search` `budget allocation` · **★★★★☆** · 2026-08-17

**AI take:** LENS is important because it moves **evidence materialization itself** to query time: raw-document regions remain latent until the information need is known. The negative result is equally important—ReAct has slightly higher D500 EM and is essentially tied on fullwiki—so the claim is better freshness/evidence localization, not universal answer quality.

[Paper](https://arxiv.org/abs/2608.16185) · [Research note](papers/2608.16185.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Fixed chunks/indexes are efficient but commit to evidence boundaries before the query and can go stale when raw files change.

**Core mechanism.** Treat raw-document regions as a latent evidence space; propose lexical/local/exploratory regions, inspect them with a relevance oracle, update per-fact beliefs, and stop under a budget.

**Agent loop.** `prior → propose raw region → inspect → update belief/proposal mix → continue or stop → consolidate grounded evidence → answer`

**Compared with.** Fresh/stale indexed RAG, index-free ReAct-style search on matched corpus snapshots, a closed-book reference, and component ablations.

**Evidence to remember.** On the controlled 500-question setting, LENS reports **62.4% EM / 84.8% evidence recall** versus **65.2% / 50.4%** for ReAct. On fullwiki, answer EM is nearly tied (**43.3% vs 42.7%**) while grounded answers favor LENS (**84.0% vs 70.7%**). The paper also reports higher online token/latency cost for LENS.

**Open question.** Under matched offline + online lifecycle cost, when is query-time latent evidence localization better than maintaining a fresh index?

</details>

### [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](papers/2608.16370.md)
`Evaluation & Analysis` · `memory` `iterative search` · **★★★★☆** · 2026-08-17

**AI take:** This exposes a metric blind spot: **fewer context tokens can mean more retrieval**, while task completion looks unchanged. Oracle restoration of dropped queryable state removes most of the extra interaction, so state-retention policy belongs in retrieval-cost attribution rather than being treated as a separate runtime detail.

[Paper](https://arxiv.org/abs/2608.16370) · [Research note](papers/2608.16370.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Completion + token reduction can make context compression look free even when the agent repeatedly re-fetches state that compression removed.

**Core mechanism.** Under a fixed 24-turn horizon, decompose tool calls into retrieval/reacquisition versus execution, vary compression, and inject exact dropped state through oracle interventions.

**Agent loop.** `state dropped → information needed again → re-query environment → resume task`; restoring queryable state short-circuits the re-query loop.

**Compared with.** Full context, sliding compression, fact-preserving summary at the same ratio, oracle-restored state, and ALFWorld as an external boundary condition.

**Evidence to remember.** At `5×`, retrieval rises in all six model-regime cells and five remain significant after Holm correction while completion changes are not significant. GPT-5.5 High changes **80%→85% completion** but **21.0→63.9 retrieval calls**. Negative result: the same sliding compression causes no retrieval surge in ALFWorld.

**Open question.** Which state should a production agent retain because reacquiring it costs more in tool latency/money than keeping it in context?

</details>

### [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](papers/2608.15191.md)
`Iterative Reasoning & Verification` · `iterative search` `adaptive stopping` `query rewrite` · **★★★★☆** · 2026-08-15

**AI take:** RAAC makes **search progress observable**: coverage, document novelty, query diversity, and drift signals drive `continue / intervene / stop`. Same-agent overlays are a strong comparison, but “14 fewer searches” is not yet a total-cost win because the controller and critical re-thinker add LLM calls.

[Paper](https://arxiv.org/abs/2608.15191) · [Research note](papers/2608.15191.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Deep-research agents often keep searching after recall/accuracy saturate and increasingly revisit seen documents.

**Core mechanism.** Maintain four unsupervised progress signals and let an overlay controller continue, stop, or invoke a critical re-thinker that generates a substantially different search query.

**Agent loop.** `search → update coverage/novelty/diversity/alignment → continue | redirect | stop → retrieve or answer`

**Compared with.** The same seven DRAs without RAAC, spanning multiple agent architectures, plus narrower trigger/stopping controllers.

**Evidence to remember.** On BrowseComp-Plus, RAAC reduces search calls by **14 on average** and improves accuracy by about **3 points on average**, with gains up to **10 points**. Negative/confounder: effects are heterogeneous; some cells use more searches or lose recall, and RAAC adds Claude-based controller/re-thinker compute.

**Open question.** Does progress-aware control still win when total controller + retrieval latency/tokens—not only search-call count—are matched?

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2608.12888.md)
`Retrieval & Tool Use` · `memory` `sparse` `iterative search` · **★★★★☆** · 2026-08-13

**AI take:** The important result is not “BM25 beats memory.” ReFind shows that **question-time access can substitute for some pre-built semantic memory structure** when the raw archive exposes session/time/local-context controls. Matched generic-agentic and one-search controls show both the interface and result-conditioned iteration matter.

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2608.12888.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Memory systems summarize/embed/structure history before the future question is known, potentially discarding details later needed.

**Core mechanism.** Keep raw chat turns intact; expose session-aware ranking, neighboring-turn expansion, temporal filtering, and seen-session state to a lexical retrieval agent.

**Agent loop.** `form keywords/time scope → search → inspect local/session context → save evidence → reformulate → skip seen sessions → stop → answer`

**Compared with.** Structured memory systems, single-shot BM25-RAG, matched generic multi-round BM25, and one-search control.

**Evidence to remember.** ReFind reports **58.2 mean accuracy** versus **53.2** for HippoRAG 2 and **48.8** for BM25-RAG across six tasks. On LongMemEval-S/M, full interface gives **93.2/89.3**, versus **78.7/82.2** generic-agentic and **84.7/68.9** one-search. EventQA slightly favors single-shot BM25 (**74.6 vs 74.1**).

**Open question.** Which workloads should precompute semantic memory structure and which should defer intelligence to question-time search after matching lifecycle cost?

</details>

### [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](papers/2608.11967.md)
`Learning & Optimization` · `memory control` `backtracking` `RL` · **★★★★☆** · 2026-08-12

**AI take:** The meaningful delta is not “reflection helps.” LoongReflect makes **active execution state reversible**: diagnose a bad branch, roll back a contaminated suffix, preserve a corrective lesson, and resume. Privileged global supervision remains the main attribution caveat.

[Paper](https://arxiv.org/abs/2608.11967) · [Research note](papers/2608.11967.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** One bad retrieval/entity association can contaminate many later search decisions while terminal reward gives weak credit to the earlier recovery decision.

**Core mechanism.** Maintain a reversible trajectory tree with `reflect` and `backtrack`; restore a trusted prefix and keep a corrective lesson.

**Agent loop.** `reason/retrieve → reflect → continue or backtrack → restore trusted state + lesson → resume → answer`

**Compared with.** ReAct, Search-R1, AgenticRAG-R1, and outcome/self-distillation approaches without the same reversible recovery semantics.

**Evidence to remember.** For Qwen2.5-3B, the paper reports **46.15 average F1** across seven RAG benchmarks versus **33.55** for AgenticRAG-R1. Caveat: the teacher has privileged global trajectory information, so the evidence supports the recovery-learning package more strongly than rollback alone.

**Open question.** How much comes from rollback semantics versus privileged reflection supervision and learned control?

</details>

### [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](papers/2608.12282.md)
`Evaluation & Analysis` · `APIs` `documents` `cross-source grounding` · **★★★★☆** · 2026-08-12

**AI take:** VAKRA matters because it evaluates **composition**, not because it proposes another agent. APIs, document retrieval, multi-hop reasoning, and policy constraints must stay coherent in one executable trajectory; failures cluster around entity disambiguation and cross-source grounding.

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/vakra) · [Research note](papers/2608.12282.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Agents can look competent on API-use and document-QA benchmarks separately yet fail when identity, evidence, and policy constraints must remain coherent across both.

**Core mechanism.** Combine executable APIs, document retrieval, and policy-constrained multi-source tasks; re-execute predicted tool calls under a fixed ReAct harness.

**Agent loop.** `interpret task/policy → choose API or document retrieval → observe evidence → cross-source grounding → continue, abstain, or answer`

**Compared with.** API-only tool-use suites, document-only RAG benchmarks, and final-answer evaluation without executable trajectory checking.

**Evidence to remember.** The best evaluated model reaches **70.4%** on single-hop endpoint-style tasks but roughly **50–51%** on compositional APIs; some policy-constrained unanswerable settings fall to **2.4%**.

**Open question.** Which controller change repairs cross-source identity/grounding failures when model, tools, and realized budget are fixed?

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Where retrieval control/materialization should live** | [SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) → [RARG](papers/2607.24223.md) | Why “one search vs many” is downstream: some intelligence can be compiled before retrieval, while raw/dynamic corpora may justify query-time evidence localization and result-conditioned interaction. |
| **How state becomes controllable—and costly** | [SGR-Bench](papers/2605.22219.md) → [S2G-RAG](papers/2604.23783.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md) | External source state, evidence/progress state, reversible reasoning state, and retained/recoverable context are different control layers with different failure costs. |
| **How to evaluate agentic retrieval causally** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [Context Compression Cost](papers/2608.16370.md) → [VAKRA](papers/2608.12282.md) | Why evidence coverage, interface/harness, retained state, realized interaction cost, and cross-source composition must be separated before crediting a retrieval policy. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**SIRA** shows that some apparent “agentic” search can be compiled before evidence is read. **LENS** gives the dynamic-raw-document counterpoint: evidence granularity/materialization can itself be deferred until query time. **Context Compression Cost** then shows why moving state out of context is not automatically cheaper—the agent may buy it back through retrieval.

Together they suggest a systems view of Agentic RAG as **materialization placement × adaptivity placement × state recoverability × lifecycle cost**.

</details>

## ⭐ Design Anchors

| Work | Why it is a useful design point |
|---|---|
| **[SIRA](papers/2605.06647.md)** | Makes pre-retrieval action compilation from LLM priors + corpus-visible statistics explicit. |
| **[A-RAG](papers/2602.03442.md)** | Makes retrieval operations an explicit model-controlled interface. |
| **[DCI](papers/2605.05242.md)** | Makes raw corpus interaction and interface resolution first-class. |
| **[RISE](papers/2606.06880.md)** | Makes retrieval construct a bounded persistent interaction space. |
| **[RARG](papers/2607.24223.md)** | Reintroduces relevance as guidance inside direct interaction rather than a final evidence bottleneck. |
| **[ReFind](papers/2608.12888.md)** | Makes raw-history preservation + substrate-native question-time search a strong baseline for structured memory. |
| **[SGR-Bench](papers/2605.22219.md)** | Makes external retrieval state a first-class evaluation object. |
| **[S2G-RAG](papers/2604.23783.md)** | Makes sufficiency and missing-information state explicit. |
| **[Training Protocols](papers/2605.27881.md)** | Makes retrieval-corpus coverage and training protocol part of the learning claim. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

`information need → pre-retrieval compilation / corpus interface → evidence materialization + observation → result-conditioned control → external + internal state → lifecycle/resource-aware evaluation`

The key correction is that **both adaptivity and materialization have a location**. SIRA asks what can be compiled before reading evidence; DCI/RISE/RARG ask what operations survive inside the retrieval boundary; ReFind and LENS show why raw/dynamic substrates can justify question-time interaction. SGR-Bench, LoongReflect, and the compression study then separate source state, active reasoning state, and recoverability cost.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Question |
|---|---|
| **[Planning & Query Formulation](categories/planning-query-formulation.md)** | What information should be acquired next, and what can be decided before evidence is retrieved? |
| **[Retrieval & Tool Use](categories/retrieval-tool-use.md)** | What should be pre-materialized versus exposed as query-time corpus operations? |
| **[Iterative Reasoning & Verification](categories/iterative-reasoning-verification.md)** | What progress/state should drive continue, redirect, recovery, or stopping? |
| **[Multi-Agent & Orchestration](categories/multi-agent-orchestration.md)** | When does specialization/coordination justify multiple agents? |
| **[Learning & Optimization](categories/learning-optimization.md)** | What should be learned, and which parts of the training environment make the learned gain causal? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we isolate policy gains from evidence, interfaces, retained state, harnesses, budgets, models, or prior art? |

<details>
<summary><strong>Planning & Query Formulation — plan first, or react to evidence?</strong></summary>

**Current anchors.** PlanRAG and SIRA as adjacent design points.

**Strongest signal.** Some retrieval decisions can be compiled from model priors plus corpus-visible statistics before evidence retrieval; other needs emerge only after observing results.

**Biggest unresolved question.** Which information needs are predictable before retrieval, and which require evidence-conditioned replanning?

**Next decisive evidence.** Same backend/corpus/model and total compute, comparing pre-retrieval compilation, one-shot retrieval, and result-conditioned replanning while controlling what corpus statistics each controller can observe.

</details>

<details>
<summary><strong>Retrieval & Tool Use — what should be materialized, and when?</strong></summary>

**Current anchors.** SIRA, Pi-Serini, A-RAG, DCI, RISE, DR-DCI, RARG, ReFind, **LENS**, SIEVE, LLM-Wiki, READ, and Know Before You Fetch.

**Strongest signal.** The tension is now two-dimensional: **compiled control vs result-conditioned interaction**, and **pre-materialized evidence vs query-time localization**. LENS strengthens the latter while preserving a negative result: better evidence grounding does not imply better answer EM.

**Biggest unresolved question.** When should a system pay offline to materialize stable evidence/index structure, and when should it preserve raw data and pay online because freshness or query-dependent granularity dominates?

**Next decisive evidence.** Same update stream/model/corpus with lifecycle-matched compute, varying index materialization, action expressivity, result-conditioned iteration, evidence localization, and freshness.

</details>

<details>
<summary><strong>Iterative Reasoning & Verification — what state should drive the next action?</strong></summary>

**Current anchors.** S2G-RAG, DocNavRAG, **RAAC**, LoongReflect, Search-o1, and ACE-GraphRAG.

**Strongest signal.** “History” is becoming multiple explicit state variables: evidence sufficiency/gaps, **trajectory progress/stagnation**, and recoverable active reasoning state. RAAC adds progress observability; LoongReflect adds rollback.

**Biggest unresolved question.** Do progress signals improve control because they expose missing information, or because an extra controller/re-thinker adds model capacity and compute?

**Next decisive evidence.** Same DRA/history representation with stopping-only, progress-signal, redirect, and rollback controls at matched total controller + retrieval cost.

</details>

<details>
<summary><strong>Multi-Agent & Orchestration — is another agent worth the coordination cost?</strong></summary>

**Current status.** No paper currently clears the radar's precision threshold as a primary multi-agent retrieval contribution; the empty category is intentional.

**Strongest signal.** Parallel LLM calls are not enough. Specialization, evidence coordination, conflict resolution, or adaptive budget allocation must be the research delta.

**Biggest unresolved question.** Does orchestration beat a strong single-agent controller at comparable total model/retrieval budget?

**Next decisive evidence.** Matched-budget many-vs-one comparisons with genuinely different tools/corpora/objectives and explicit coordination analysis.

</details>

<details>
<summary><strong>Learning & Optimization — what exactly is being learned?</strong></summary>

**Current anchors.** Agentic-R, Critic-R, GrepSeek, SearchMaster, SPARKLE, Graph-R1, SAGE, and LoongReflect; Training Protocols is the evaluation baseline.

**Strongest signal.** “Better RL” is not identifiable until the retrieval/training environment is controlled. Missing answer-bearing passages can create positive reward from parametric knowledge, while tool format, rollout freshness, and search budget materially change learned behavior.

**Biggest unresolved question.** Did learning improve information-acquisition decisions, or did evidence coverage, interface compatibility, privileged supervision, easier self-play tasks, or a different budget provide most of the gain?

**Next decisive evidence.** Same corpus coverage, environment/state/action space/base model and realized budget, with reward/credit assignment and supervision distribution varied independently.

</details>

<details>
<summary><strong>Evaluation & Analysis — how do we know what caused the gain?</strong></summary>

**Current anchors.** Training Protocols, Pi-Serini, SGR-Bench, Is Grep All You Need?, When Should Active RAG Retrieve?, **Context Compression Cost**, VAKRA, Forgotten History or Test-of-Time?, and Agentic RAG SoK.

**Strongest signal.** Final-answer success can hide failures/cost earlier in the information path. The compression study adds a clean example: **state removal can triple retrieval while completion stays statistically unchanged**; oracle restoration attributes most of the extra interaction to reacquiring queryable state.

**Biggest unresolved question.** Can we locate cost/failure to evidence availability, backend exposure, agent inspection, environment state, retained state, controller action, or cross-source grounding?

**Next decisive evidence.** Factorial executable evaluation with known evidence coverage, controlled backend/interface/state/harness/controller substitutions, full offline+online cost logging, and counterfactual repair of one intermediate variable.

</details>

[Explore the full research map →](categories/README.md)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W34 · Materialization, progress observability, and the hidden re-query tax](digests/weekly/2026-W34.md)**  
W34 adds three coupled control points: LENS moves evidence materialization to query time, RAAC makes search progress visible to a continue/redirect/stop controller, and the context-compression study shows that removing state can simply move cost into external reacquisition.

[Read the rolling W34 synthesis →](digests/weekly/2026-W34.md)

**[2026-W33 · Where should retrieval intelligence live?](digests/weekly/2026-W33.md)**  
ReFind moves memory intelligence from offline structure into question-time search, LoongReflect makes accumulated state reversible, and VAKRA tests cross-source trajectory integrity; SIRA is the pre-retrieval counterpoint.

[Read the W33 synthesis →](digests/weekly/2026-W33.md)

**[2026-W32 · Convergence, factorization, and a stricter novelty baseline](digests/weekly/2026-W32.md)**  
W32 asks what remains after matching interface, harness, adaptive baseline, realized resources, and supervision distribution.

[Read the revised W32 synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map](digests/monthly/2026-08.md)**  
August now separates **adaptivity placement, evidence-materialization placement, and state recoverability**. LENS adds the raw-dynamic-document case; RAAC adds progress-aware control; context compression shows why state savings must be charged against reacquisition.

[Explore the August map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling year-to-date map](digests/yearly/2026.md)**  
The durable 2026 shift remains explicit design of the agent's information environment: what is precomputed, what becomes observable after retrieval, what state persists, and what offline + online resources are actually spent.

[Explore the 2026 year-to-date map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes while fresh. **Monthly** rebuilds the field map. **Yearly** keeps durable shifts, defining papers, weakened ideas, evidence standards, and open problems. Lower-level reports remain in the repository for provenance.

</details>

## 🖼️ How to Read a Paper Here

- **30-second scan:** title, category, importance, date, and skeptical AI take.
- **60-second expand:** problem, mechanism, control flow, closest comparison, strongest evidence including negative results, and one open question. A verified high-resolution visual appears first when available, with a guide to how to read it and what not to infer.
- **Deep dive:** open the research note for detailed evidence, limitations, provenance, and visual grounding.

## What Counts as Agentic RAG?

A work is included when **external retrieval/search/context acquisition is substantive and an agent, controller, or learned policy materially changes whether, what, where, how, or how many times information is acquired**.

Ordinary fixed `retrieve top-k → generate` pipelines are not included merely because they use an LLM. Generic agents are excluded when retrieval is incidental. Pure retriever/reranker/index work is excluded unless adaptive information-access control is itself part of the research contribution.

## About the Radar

This is a **curated research map, not an exhaustive keyword feed**. Every included work should help answer:

1. **What actually changed?**
2. **Compared with what—including stronger historical/design predecessors?**
3. **Does the evidence isolate the claimed cause?**

Negative results are kept when they change the interpretation of a paper.

## 🤝 Contributing

Corrections are especially welcome when they change the conclusion: a missing baseline, unfair resource budget, wrong taxonomy, overclaimed novelty, broken provenance, or a visual that implies a mechanism the evidence does not support.

<details>
<summary><strong>Methodology & maintenance</strong></summary>

See the [maintainer guide](docs/MAINTENANCE.md), [curation protocol](CURATION.md), [compaction protocol](COMPACTION.md), [visual grounding rules](VISUALS.md), [taxonomy](taxonomy.yaml), and [structured paper records](data/papers/).

</details>

---

If this radar saves you research time, consider starring the repo.
