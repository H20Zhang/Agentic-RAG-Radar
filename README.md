# 🤖 Agentic RAG Radar

**A living research map of Agentic Retrieval-Augmented Generation.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-17 · [Latest papers](#-latest-papers) · [Start here](#-start-here) · [Browse by research problem](categories/README.md) · [Research compactions](#-research-compactions)

**Current field thesis:** the useful question is no longer “retriever or agent?” or “one search or many?” It is **where information-acquisition intelligence should live**: compiled before retrieval, exposed through the retrieval interface, updated from evidence during search, or preserved/repaired in state.

## 🔥 Latest Papers

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2608.12888.md)
`Retrieval & Tool Use` · `memory` `sparse` `iterative search` · **★★★★☆** · 2026-08-13

**AI take:** The important result is not “BM25 beats memory.” ReFind shows that **question-time access can substitute for some pre-built semantic memory structure** when the raw archive exposes session/time/local-context controls. Matched generic-agentic and one-search controls make the claim unusually useful: both the chat-native interface and result-conditioned iteration matter.

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2608.12888.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Memory systems usually decide how to summarize, embed, or structure a conversation before the future question is known. That can reduce online work but may discard details the eventual query needs.

**Core mechanism.** Keep raw chat turns intact; index them lexically; expose session-aware rank fusion, neighboring-turn expansion, temporal filtering, and seen-session state to a retrieval agent; save only useful verbatim evidence for a separate answer stage.

**Agent loop.** `form keywords/time scope → search → inspect local/session context → save evidence → reformulate or narrow → skip seen sessions → stop → answer`

**Compared with.** Structured memory systems, single-shot BM25-RAG, a matched generic multi-round BM25 agent, and a forced one-search control.

**Evidence to remember.** Across the six MemoryAgentBench-derived tasks, ReFind reports **58.2 mean accuracy** versus **53.2** for HippoRAG 2 and **48.8** for BM25-RAG. On the matched LongMemEval-S/M control, the full interface reports **93.2/89.3**, versus **78.7/82.2** for generic-agentic BM25 and **84.7/68.9** with one search. Negative result: on EventQA, single-shot BM25-RAG is slightly higher (**74.6 vs 74.1**).

**Open question.** After matching storage fidelity, latency, update cost, and query-time compute, which workloads should precompute semantic memory structure and which should defer intelligence to question-time search?

</details>

### [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](papers/2608.11967.md)
`Learning & Optimization` · `memory control` `backtracking` `RL` · **★★★★☆** · 2026-08-12

**AI take:** The meaningful delta is not “reflection helps.” LoongReflect makes **active execution state reversible**: a controller can diagnose a branch, roll back a contaminated suffix, preserve a corrective lesson, and resume search. Privileged global supervision during training remains the main causal caveat.

[Paper](https://arxiv.org/abs/2608.11967) · [Research note](papers/2608.11967.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Long-horizon search accumulates state; one bad retrieval/entity association can contaminate many later decisions, while terminal reward gives weak credit to the earlier recovery decision.

**Core mechanism.** Maintain a reversible trajectory tree with explicit `reflect` and `backtrack` controls. Reflection consolidates verified facts, missing evidence, and branch risk; backtracking restores a trusted prefix and removes the unreliable suffix from active context.

**Agent loop.** `reason/retrieve → reflect → continue or backtrack → restore trusted state + lesson → resume search → answer`

**Compared with.** ReAct, Search-R1, AgenticRAG-R1, and outcome/self-distillation approaches without the same reversible recovery semantics.

**Evidence to remember.** For Qwen2.5-3B, the paper reports **46.15 average F1** across seven RAG benchmarks versus **33.55** for AgenticRAG-R1, with component ablations. But the teacher has privileged global trajectory information, so the evidence supports the whole recovery-learning package more strongly than rollback alone.

**Open question.** How much comes from the rollback action space itself versus privileged reflection supervision and learned control?

</details>

### [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](papers/2608.12282.md)
`Evaluation & Analysis` · `APIs` `documents` `cross-source grounding` · **★★★★☆** · 2026-08-12

**AI take:** VAKRA matters because it evaluates **composition**, not because it proposes another agent. APIs, document retrieval, multi-hop reasoning, and policy constraints must coexist in one executable trajectory; failures cluster around entity disambiguation and cross-source grounding rather than function-call syntax alone.

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/vakra) · [Research note](papers/2608.12282.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Agents can look competent on API-use and document-QA benchmarks separately yet fail when identity, evidence, and policy constraints must remain coherent across both.

**Core mechanism.** Benchmark more than 8,000 executable APIs across 62 domains together with document retrieval and policy-constrained multi-source tasks; re-execute predicted tool calls while holding a fixed ReAct harness across models.

**Agent loop.** `interpret task/policy → choose API or document retrieval → observe evidence → cross-source grounding → continue, abstain, or answer`

**Compared with.** API-only tool-use suites, document-only RAG benchmarks, and final-answer evaluation without executable trajectory checking.

**Evidence to remember.** The best evaluated model reaches **70.4%** on single-hop endpoint-style tasks but roughly **50–51%** on compositional APIs; some policy-constrained unanswerable settings fall to **2.4%**. Trace analysis points to entity disambiguation and cross-source grounding as major failures.

**Open question.** Which controller change actually repairs those failures when model, tools, and realized budget are held fixed?

</details>

### [Forgotten History or Test-of-Time? Retrospect and Prospect on RAG from an IR Perspective](papers/2608.08445.md)
`Evaluation & Analysis` · `history` `verification` `query refinement` · **★★★★☆** · 2026-08-09

**AI take:** This changes **compared with what**. Iterative query refinement, verification, and closed-loop retrieval have classical IR/QA precedents; modern novelty therefore has to live in model capability, interface, state, learning, scale, or transfer—not merely in the existence of an adaptive loop.

[Paper](https://arxiv.org/abs/2608.08445) · [Research note](papers/2608.08445.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** RAG papers often compare only against recent LLM-era systems, which can make older IR/QA ideas look newly invented.

**Core mechanism.** Historical/systematization analysis rather than a new runtime system. QUALIFIER is reconstructed as `structured constraints → retrieve/extract → verify → relax/reformulate → repeat → answer/NIL`.

**Compared with.** LLM-centric histories of RAG and Agentic RAG.

**Evidence to remember.** The paper reports QUALIFIER's TREC 2002 `pris2002` run at **290/500 correct**, second to LCC at **415/500**, and documents repeated successive-constraint relaxation. The claim that this loop explains its competitiveness is retrospective—not a matched causal ablation.

**Open question.** Which modern gains survive when strong classical closed-loop IR/QA ideas are reimplemented with today's models and interfaces?

</details>

### [SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems](papers/2608.08237.md)
`Learning & Optimization` · `budget allocation` `hybrid` `production` · **★★★☆☆** · 2026-08-08

**AI take:** SAGE makes **how much retrieval** a learned per-query action under an explicit latency SLO. The systems control point is useful; the evidence is narrower because the main baseline family is static-k even though strong adaptive controllers already exist.

[Paper](https://arxiv.org/abs/2608.08237) · [Research note](papers/2608.08237.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** One global k over-retrieves easy queries and forces a bad quality-versus-tail-latency compromise.

**Core mechanism.** `probe hybrid retrieval → retrieval-side features → learned policy chooses k → top-k context → one LLM generation`; offline budget sweeps provide imitation labels.

**Agent loop.** `probe → choose k → retrieve top-k → answer`

**Compared with.** Static-k hybrid RAG, random-k and component ablations; adaptive-k/stopping methods are discussed but not directly benchmarked in the main table.

**Evidence to remember.** On the reported 334-query NQ table with a 5 s target, SAGE gives up some EM relative to static `k=20` while substantially improving SLO compliance and P95 latency. The useful result is the quality/latency operating point, not a universal accuracy win.

**Open question.** Does the SLO-aware learned policy still win against strong adaptive budget/stopping controllers on identical retrieval hardware and cost axes?

</details>

### [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](papers/2608.06305.md)
`Retrieval & Tool Use` · `sparse` `documents` `iterative search` · **★★★★☆** · 2026-08-06

**AI take:** The strongest result is not “agents beat RAG.” It is that an iterative loop cannot rescue a bad retrieval primitive; **BM25 is statistically indistinguishable from READ**, so the paper is also a warning against over-crediting agentic composition.

[Paper](https://arxiv.org/abs/2608.06305) · [Research note](papers/2608.06305.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Chunk-and-embed retrieval can destroy structural context in table-heavy long documents.

**Core mechanism.** Replace one opaque dense top-k call with **lexical search → structural navigation → bounded read**.

**Agent loop.** `search → navigate → read → inspect → refine → answer`

**Compared with.** Dense top-k RAG, the same iterative loop restricted to top-k, and BM25.

**Evidence to remember.** The abstract reports 58.8% accuracy versus 15.7% dense retrieval and 27.5% for the same loop with top-k; BM25 is reported statistically indistinguishable from READ.

**Open question.** Under matched lexical primitives and retrieval budgets, how much extra value comes from adaptive composition?

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Where retrieval control should live** | [SIRA](papers/2605.06647.md) → [Pi-Serini](papers/2605.10848.md) → [A-RAG](papers/2602.03442.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [RARG](papers/2607.24223.md) | Why round count is not the design variable: some adaptivity can be compiled before retrieval from corpus-visible signals, while other tasks need result-conditioned inspection, reformulation, and local operations. |
| **How state becomes controllable** | [SGR-Bench](papers/2605.22219.md) → [S2G-RAG](papers/2604.23783.md) → [DocNavRAG](papers/2608.01565.md) → [LoongReflect](papers/2608.11967.md) | The distinction between external retrieval state, persistent evidence state, and editable/recoverable agent state. |
| **How to evaluate agentic retrieval causally** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [SGR-Bench](papers/2605.22219.md) → [VAKRA](papers/2608.12282.md) | Why evidence coverage, backend/interface calibration, harness, environment state, realized resources, and cross-source composition must be separated before crediting a policy or RL objective. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**SIRA** gives the cleanest argument that some “agentic” search rounds can be compiled away when corpus-visible signals make a discriminative action programmable before evidence is read. **ReFind** supplies the counterexample: distributed chat evidence benefits from result-conditioned iteration plus substrate-native controls. **LoongReflect** then asks what happens when the accumulated execution state itself becomes wrong.

Together they suggest a harder model of Agentic RAG: **information environment × placement of adaptivity × layered state × realized resources**.

</details>

## ⭐ Design Anchors

| Work | Why it is a useful design point |
|---|---|
| **[SIRA](papers/2605.06647.md)** | Makes **pre-retrieval action compilation** from LLM priors + corpus-visible statistics explicit. |
| **[A-RAG](papers/2602.03442.md)** | Makes retrieval operations an explicit model-controlled interface. |
| **[DCI](papers/2605.05242.md)** | Makes raw corpus interaction and **interface resolution** first-class. |
| **[RISE](papers/2606.06880.md)** | Makes retrieval construct a bounded persistent interaction space. |
| **[RARG](papers/2607.24223.md)** | Reintroduces relevance as guidance inside direct interaction rather than a final evidence bottleneck. |
| **[ReFind](papers/2608.12888.md)** | Makes raw-history preservation + substrate-native question-time search a strong baseline for structured memory. |
| **[SGR-Bench](papers/2605.22219.md)** | Makes external retrieval state a first-class evaluation object. |
| **[S2G-RAG](papers/2604.23783.md)** | Makes sufficiency and missing-information state explicit. |
| **[Training Protocols](papers/2605.27881.md)** | Makes retrieval-corpus coverage and training protocol part of the learning claim. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

`information need → pre-retrieval compilation / corpus interface → evidence observation → result-conditioned control → external + internal state → resource-aware evaluation`

The important correction is that **adaptivity has a location**. SIRA asks what can be decided before reading evidence; DCI/RISE/RARG ask which operations should survive inside the retrieval boundary; ReFind shows that newly exposed session/entity/time cues can make result-conditioned iteration valuable. SGR-Bench and LoongReflect then separate errors in the external source state from errors in the agent's active state.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Question |
|---|---|
| **[Planning & Query Formulation](categories/planning-query-formulation.md)** | What information should be acquired next, and what can be decided before evidence is retrieved? |
| **[Retrieval & Tool Use](categories/retrieval-tool-use.md)** | What corpus signals, boundaries, operations, state, and retrieval resources should the agent control? |
| **[Iterative Reasoning & Verification](categories/iterative-reasoning-verification.md)** | What internal state should make the next retrieval, verification, recovery, or stopping decision? |
| **[Multi-Agent & Orchestration](categories/multi-agent-orchestration.md)** | When does specialization/coordination justify multiple agents? |
| **[Learning & Optimization](categories/learning-optimization.md)** | What should be learned, and which parts of the training environment make the learned gain causal? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we isolate policy/retrieval gains from missing evidence, interfaces, state, harnesses, budgets, models, or prior art? |

<details>
<summary><strong>Planning & Query Formulation — plan first, or react to evidence?</strong></summary>

**Current anchors.** PlanRAG and SIRA as adjacent design points.

**Strongest signal.** SIRA sharpens “planning” into a testable distinction: some query/retrieval decisions can be compiled from model priors plus corpus-visible statistics before evidence retrieval, while other information needs only become apparent after observing results.

**Biggest unresolved question.** Which information needs are predictable before retrieval, and which require evidence-conditioned replanning?

**Next decisive evidence.** Same backend/corpus/model and total compute, comparing pre-retrieval compilation, one-shot retrieval, and result-conditioned replanning while controlling what corpus statistics each controller can observe.

</details>

<details>
<summary><strong>Retrieval & Tool Use — where should adaptivity live?</strong></summary>

**Current anchors.** SIRA, Pi-Serini, A-RAG, DCI, RISE, DR-DCI, RARG, ReFind, SIEVE, LLM-Wiki, READ, and Know Before You Fetch.

**Strongest signal.** The emerging tension is **compiled control versus result-conditioned interaction**. SIRA shows that corpus statistics can eliminate some exploratory rounds; ReFind shows that forcing one search loses badly on distributed chat-memory tasks, while its matched generic-agentic control shows iteration alone is insufficient without the right interface.

**Biggest unresolved question.** When should a system spend offline/pre-retrieval work to compile a better action, and when should it preserve raw evidence plus runtime operations because the next query depends on newly observed information?

**Next decisive evidence.** Same model/backend/corpus with equal total compute, independently varying pre-retrieval corpus observability, action expressivity, result-conditioned iteration, and offline-versus-query-time cost.

</details>

<details>
<summary><strong>Iterative Reasoning & Verification — what state should drive the next action?</strong></summary>

**Current anchors.** S2G-RAG, DocNavRAG, LoongReflect, Search-o1, and ACE-GraphRAG.

**Strongest signal.** “Iterative” is too weak a description. Internal state is becoming an explicit control surface: sufficiency/gaps, persistent evidence workspace, and potentially editable active reasoning state with rollback semantics. SGR-Bench is the boundary condition: external source configuration is a different state layer.

**Biggest unresolved question.** Does rollback itself help, or do gains come from privileged recovery supervision and a richer state representation—and how does internal recovery interact with a misconfigured external source state?

**Next decisive evidence.** Hold trajectory representation fixed and compare append-only reflection, prompted rollback, and learned rollback at equal tool/retrieval budgets; independently intervene on external retrieval state versus internal state.

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

**Strongest signal.** “Better RL” is not identifiable until the **retrieval/training environment** is controlled. Training Protocols shows that missing answer-bearing passages can create positive reward from parametric knowledge, while tool format, rollout freshness, and search budget materially change the learned behavior.

**Biggest unresolved question.** Did learning improve information-acquisition decisions, or did evidence coverage, interface compatibility, privileged supervision, easier self-play tasks, or a different budget provide most of the gain?

**Next decisive evidence.** Same corpus coverage, environment/state/action space/base model and realized budget, with reward/credit assignment and supervision distribution varied independently.

</details>

<details>
<summary><strong>Evaluation & Analysis — how do we know what caused the gain?</strong></summary>

**Current anchors.** Training Protocols, Pi-Serini, SGR-Bench, Is Grep All You Need?, When Should Active RAG Retrieve?, VAKRA, Forgotten History or Test-of-Time?, and Agentic RAG SoK.

**Strongest signal.** The causal chain begins earlier than retrieval quality: **does the environment contain answer-bearing evidence at all?** Training Protocols shows corpus incompleteness can generate spurious RL reward; Pi-Serini then separates backend exposure from agent inspection; SGR-Bench separates source discovery from source state; VAKRA exposes cross-source trajectory failure.

**Biggest unresolved question.** Can we locate a failure to the stage that caused it: evidence availability, backend exposure, agent inspection, environment state, controller action, or cross-source grounding?

**Next decisive evidence.** Factorial executable evaluation with known evidence coverage, controlled backend/interface/environment-state/harness/controller substitutions, realized cost logging, and counterfactual repair of one intermediate decision.

</details>

[Explore the full research map →](categories/README.md)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W33 · Where should retrieval intelligence live?](digests/weekly/2026-W33.md)**  
W33 now links three pressure points: ReFind moves memory intelligence from offline structure into question-time raw-history search, LoongReflect makes accumulated state reversible, and VAKRA tests cross-source trajectory integrity. SIRA is the counterpoint: some adaptive search can be compiled *before* evidence is read.

[Read the rolling W33 synthesis →](digests/weekly/2026-W33.md)

**[2026-W32 · Convergence, factorization, and a stricter novelty baseline](digests/weekly/2026-W32.md)**  
W32 asks what remains after matching interface, harness, adaptive baseline, realized resources, and supervision distribution. SIEVE and SearchMaster provide the most useful Aug-03 factorization evidence.

[Read the revised W32 synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map](digests/monthly/2026-08.md)**  
The August map adds **adaptivity placement** to interface/state factorization: SIRA shows that corpus-aware control can sometimes be compiled before retrieval; ReFind shows result-conditioned iteration matters when useful cues emerge only after inspecting evidence. The evaluation baseline also moves earlier to evidence availability itself.

[Explore the August map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling year-to-date map](digests/yearly/2026.md)**  
The durable 2026 shift is toward explicit design of the agent's **information environment and placement of adaptivity**—what is precomputed, what is exposed before retrieval, what changes after evidence, what state persists, and what resources are actually spent.

[Explore the 2026 year-to-date map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes while they are fresh. **Monthly** compresses several weeks into field-map movement. **Yearly** keeps only durable shifts, defining papers, weakened ideas, evidence standards, and open problems. Lower-level reports remain in the repository for provenance; they simply age out of the primary reading surface.

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
