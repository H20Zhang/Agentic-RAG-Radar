# 🤖 Agentic RAG Radar

**A living research map of Agentic Retrieval-Augmented Generation.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes, visual explainers, and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-14 · [Latest papers](#-latest-papers) · [Start here](#-start-here) · [Browse by research problem](categories/README.md) · [Research compactions](#-research-compactions)

## 🔥 Latest Papers

### [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](papers/2608.11967.md)
`Learning & Optimization` · `memory control` `backtracking` `RL` · **★★★★☆** · 2026-08-12

**AI take:** The meaningful delta is not “reflection helps.” LoongReflect makes **active execution state reversible**: a controller can diagnose a branch, roll back a contaminated suffix, preserve a corrective lesson, and resume search. Strong adaptive/RL baselines help; privileged global supervision during training remains the main causal caveat.

[Paper](https://arxiv.org/abs/2608.11967) · [Research note](papers/2608.11967.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Long-horizon search accumulates state; one bad retrieval/entity association can contaminate many later decisions, while terminal reward gives weak credit to the earlier reflection decision that should have repaired it.

**Core mechanism.** Maintain a reversible trajectory tree with explicit `reflect` and `backtrack` controls. Reflection consolidates verified facts, missing evidence, and branch risk; backtracking restores a trusted prefix and removes the unreliable suffix from active context.

**Agent loop.** `reason/retrieve → reflect → continue or backtrack → restore trusted state + lesson → resume search → answer`

**Compared with.** ReAct, Search-R1, AgenticRAG-R1, and outcome/self-distillation approaches without the same explicit reversible recovery semantics.

**Evidence to remember.** For Qwen2.5-3B, the paper reports **46.15 average F1** across seven RAG benchmarks versus **33.55** for AgenticRAG-R1, alongside component ablations. But the fast training channel has privileged global trajectory information, so the result supports the whole recovery-learning package more strongly than any one component.

**Open question.** How much comes from the trajectory-tree/rollback action space itself versus privileged reflection supervision and learned control?

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

**AI take:** This matters because it changes **compared with what**. Iterative query refinement, verification, and closed-loop retrieval have classical IR/QA precedents; modern novelty therefore has to live in model capability, interface, state, learning, scale, or transfer—not merely in the existence of an adaptive loop.

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
| **How corpus access becomes an interaction space** | [A-RAG](papers/2602.03442.md) → [DCI](papers/2605.05242.md) → [RISE](papers/2606.06880.md) → [DR-DCI](papers/2606.14885.md) → [RARG](papers/2607.24223.md) | Why the design variable is not “dense vs lexical” but **where the corpus boundary sits and what evidence operations remain available after it**. |
| **How evidence state becomes controllable** | [S2G-RAG](papers/2604.23783.md) → [DocNavRAG](papers/2608.01565.md) → [LoongReflect](papers/2608.11967.md) | The move from sufficiency/missing-evidence state to environment-coupled state and then explicit rollback/recovery semantics. |
| **How to evaluate agentic retrieval causally** | [Is Grep All You Need?](papers/2605.15184.md) → [Know Before You Fetch](papers/2606.29959.md) → [When Should Active RAG Retrieve?](papers/2607.24010.md) → [VAKRA](papers/2608.12282.md) | Why interface, harness/delivery, realized resources, and cross-source composition must be separated before crediting a policy or retriever. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**DCI** gives the clearest interface-resolution argument: relevant documents can be reachable while the evidence API is still too coarse. **LoongReflect** gives the strongest current argument that active reasoning state may need recovery semantics rather than append-only memory. **VAKRA** stress-tests the whole story in an executable API+documents environment where cross-source grounding becomes a distinct bottleneck.

Together they suggest a harder model of Agentic RAG: **information environment × persistent/editable state × policy × realized resources × trajectory integrity**.

</details>

## ⭐ Design Anchors

| Work | Why it is a useful design point |
|---|---|
| **[A-RAG](papers/2602.03442.md)** | Makes retrieval operations an explicit model-controlled interface. |
| **[DCI](papers/2605.05242.md)** | Makes raw corpus interaction and **interface resolution** first-class. |
| **[RISE](papers/2606.06880.md)** | Makes retrieval construct a bounded persistent interaction space. |
| **[DR-DCI](papers/2606.14885.md)** | Makes retrieval dynamically expand durable workspace state. |
| **[RARG](papers/2607.24223.md)** | Reintroduces relevance as guidance inside direct interaction rather than a final evidence bottleneck. |
| **[S2G-RAG](papers/2604.23783.md)** | Makes sufficiency and missing-information state explicit. |
| **[Critic-R](papers/2606.00590.md)** | Turns reasoning feedback into query repair and retriever learning. |
| **[Is Grep All You Need?](papers/2605.15184.md)** | Makes harness and evidence-delivery path explicit retrieval confounders. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

`information need → corpus interface/boundary → persistent evidence workspace → explicit/editable state → adaptive/learned control → resource/harness-aware evaluation`

The biggest chronology correction is the interface lineage: **A-RAG → DCI → RISE → DR-DCI → RARG**. It replaces the false binary “semantic retriever or grep” with a systems question: **where should relevance constrain the search space, and what local operations should survive inside that boundary?**

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Question |
|---|---|
| **[Planning & Query Formulation](categories/planning-query-formulation.md)** | What information should be acquired next, and how is that need planned/decomposed? |
| **[Retrieval & Tool Use](categories/retrieval-tool-use.md)** | What corpus boundary, evidence operations, and resource semantics should the agent control? |
| **[Iterative Reasoning & Verification](categories/iterative-reasoning-verification.md)** | What state should make the next retrieval, verification, recovery, or stopping decision? |
| **[Multi-Agent & Orchestration](categories/multi-agent-orchestration.md)** | When does specialization/coordination justify multiple agents? |
| **[Learning & Optimization](categories/learning-optimization.md)** | What should be learned: ranking, query refinement, corpus operations, recovery, or resource allocation? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we isolate policy/retrieval gains from richer interfaces, harnesses, budgets, models, or prior art? |

<details>
<summary><strong>Planning & Query Formulation — plan first, or react to evidence?</strong></summary>

**Current anchor.** [PlanRAG](papers/2406.12430.md).

**Strongest signal.** Explicit plans give information acquisition a stable objective, while evidence-state systems suggest the next step can instead be selected from what remains missing.

**Biggest unresolved question.** When does a precommitted plan beat online replanning after failed or contradictory retrieval?

**Next decisive evidence.** Plan-repair/decomposition experiments under matched resource budgets and structured targets such as SQL, graphs, web, or code.

</details>

<details>
<summary><strong>Retrieval & Tool Use — what should the agent actually be allowed to do?</strong></summary>

**Current anchors.** A-RAG, DCI, RISE, DR-DCI, RARG, LLM-Wiki, READ, and Know Before You Fetch.

**Strongest signal.** The field has moved through `fixed top-k → raw high-resolution interaction → bounded/dynamic workspace → relevance-guided interaction`. The stable abstraction is **interaction-space design**, not a lexical-versus-dense contest.

**Biggest unresolved question.** Where should relevance constrain the environment: hard top-k boundary, workspace constructor, dynamic expansion policy, or local execution prior?

**Next decisive evidence.** Same model/harness/corpus/resources across conventional top-k, raw DCI, and bounded/dynamic interaction, independently varying boundary retriever and local operation set.

</details>

<details>
<summary><strong>Iterative Reasoning & Verification — what state should drive the next action?</strong></summary>

**Current anchors.** S2G-RAG, DocNavRAG, LoongReflect, Search-o1, and ACE-GraphRAG.

**Strongest signal.** “Iterative” is too weak a description. State is becoming an explicit control surface: sufficiency/gaps, persistent evidence workspace, and potentially editable active reasoning state with rollback semantics.

**Biggest unresolved question.** Does rollback itself help, or do gains come from privileged recovery supervision and a richer state representation?

**Next decisive evidence.** Hold trajectory representation fixed and compare append-only reflection, prompted rollback, and learned rollback at equal tool/retrieval budgets; separately test whether external workspace persistence survives reasoning-context reset.

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

**Current anchors.** Agentic-R, Critic-R, GrepSeek, SPARKLE, Graph-R1, SAGE, and LoongReflect.

**Strongest signal.** “Learned retrieval policy” now hides distinct objects: retriever utility, query/refinement policy, direct-corpus operations, state recovery, and budget allocation.

**Biggest unresolved question.** Did learning improve decisions, or did a richer interface/state/action space, privileged teacher, or extra refinement budget provide most of the gain?

**Next decisive evidence.** Prompted, supervised, and RL controllers on the same environment/state/action space/base model with matched realized calls/tokens/latency/controller compute.

</details>

<details>
<summary><strong>Evaluation & Analysis — how do we know what caused the gain?</strong></summary>

**Current anchors.** Is Grep All You Need?, When Should Active RAG Retrieve?, VAKRA, Forgotten History or Test-of-Time?, and Agentic RAG SoK.

**Strongest signal.** The causal lens now needs a **harness/delivery axis** in addition to substrate, interface, state, policy, resources, model, and historical baseline. Identical retrieval can change rank when evidence is delivered through a different harness path.

**Biggest unresolved question.** Can we causally locate a trajectory failure or performance gain rather than only observe the final score?

**Next decisive evidence.** Factorial executable evaluation that independently swaps corpus interface, evidence-delivery path, controller, and model, plus counterfactual replay of one patched intermediate decision.

</details>

[Explore the full research map →](categories/README.md)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W33 · State recovery and cross-source trajectory integrity](digests/weekly/2026-W33.md)**  
W33 adds two current stress tests: **editable/recoverable state** and **cross-source executable grounding**. The key question is whether rollback-style control helps when failures arise from entity/schema grounding rather than an obviously bad search branch.

[Read the rolling W33 synthesis →](digests/weekly/2026-W33.md)

**[2026-W32 · Convergence, factorization, and a stricter novelty baseline](digests/weekly/2026-W32.md)**  
Historical backfill now makes the W32 chronology stricter: DCI, RISE, DR-DCI, and RARG already made interface resolution and interaction-space design explicit before August. The sharper W32 question is what a paper adds after matching **interface, harness, state, adaptive baseline, and realized resources**.

[Read the revised W32 synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map](digests/monthly/2026-08.md)**  
The corrected map is `corpus boundary/interface resolution → explicit/editable state → adaptive policy/stopping → resource allocation → harness/delivery → executable evaluation`. The DCI lineage materially strengthens the environment layer; W33 sharpens state and cross-source trajectory integrity.

[Explore the August map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling year-to-date map](digests/yearly/2026.md)**  
The durable 2026 shift is toward explicit design of the agent's **information environment**—corpus boundary, evidence operations, persistent/editable state, adaptive control, and realized resources—under a causal bar that now treats harness/evidence delivery as part of the system.

[Explore the 2026 year-to-date map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes while they are fresh. **Monthly** compresses several weeks into field-map movement. **Yearly** keeps only durable shifts, defining papers, weakened ideas, evidence standards, and open problems. Lower-level reports remain in the repository for provenance; they simply age out of the primary reading surface.

</details>

## 🖼️ How to Read a Paper Here

- **30-second scan:** title, category, importance, date, and skeptical AI take.
- **60-second expand:** problem, mechanism, control flow, closest comparison, strongest evidence, and one open question; when a verified high-resolution visual exists, it appears first with a concise guide to how to read it and what not to infer.
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
