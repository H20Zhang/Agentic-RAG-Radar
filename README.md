# 🤖 Agentic RAG Radar

**A living research map of Agentic Retrieval-Augmented Generation.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes, visual explainers, and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-12 · [Latest papers](#-latest-papers) · [Start here](#-start-here) · [Browse by research problem](categories/README.md) · [Research compactions](#-research-compactions)

## 🔥 Latest Papers

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

### [DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction](papers/2608.01565.md)
`Retrieval & Tool Use` · `graph` `documents` `evidence state` · **★★★★☆** · 2026-08-03

**AI take:** The reusable abstraction is **environment + evidence-state co-design**: preserve document-native structure as retrieval operations and explicitly track what evidence is collected versus still missing.

[Paper](https://arxiv.org/abs/2608.01565) · [Research note](papers/2608.01565.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Complex document questions need complementary evidence across distant sections/documents; flat retrieval repeatedly reconstructs location from similarity.

**Core mechanism.** Turn hierarchy/cross-region relations into a navigable environment and maintain **collected evidence + missing evidence** state.

**Agent loop.** `locate → navigate/expand → fetch → update evidence state → identify missing evidence → continue or answer`

**Compared with.** Flat passage-level iterative RAG, repeated global semantic search, and fixed-traversal GraphRAG.

**Evidence to remember.** The abstract reports average gains of **7.8% answer quality** and **17.7% context sufficiency** across four long-/multi-document QA benchmarks; structure, state, and budget attribution remain open.

**Open question.** Does explicit evidence state transfer beyond documents to web, SQL, code, or graph-search agents?

</details>

### [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](papers/2608.01269.md)
`Iterative Reasoning & Verification` · `graph` `context policy` `multi-hop QA` · **★★★★☆** · 2026-08-02

**AI take:** A rich hierarchy does not guarantee the right context. ACE-GraphRAG makes **context assembly itself a query-dependent policy**; the unresolved question is whether gains survive matched retrieval/token budgets.

[Paper](https://arxiv.org/abs/2608.01269) · [Research note](papers/2608.01269.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Hierarchical GraphRAG can represent useful evidence yet still assemble the wrong context with fixed rules.

**Core mechanism.** Detect a context gap and choose complementary **depth-oriented factual** versus **breadth-oriented semantic** retrieval branches.

**Agent loop.** `build context → detect gap → choose branch → retrieve → consolidate → adapt → generate`

**Compared with.** Hierarchical GraphRAG with fixed/predetermined context construction.

**Evidence to remember.** The paper reports gains on HotpotQA, 2WikiMultiHopQA, and UltraDomain subsets; exact attribution to the adaptive policy versus extra context budget still needs stronger checking.

**Open question.** Is the policy better, or does the system simply spend more retrieval/context budget through multiple branches?

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Why retrieval is becoming an environment, not a call** | [A-RAG](papers/2602.03442.md) → [LLM-Wiki](papers/2605.25480.md) → [READ](papers/2608.06305.md) → [DocNavRAG](papers/2608.01565.md) | How the retrieval API/index product becomes part of the research design, and why environment and runtime policy must be separated. |
| **How evidence becomes explicit state** | [S2G-RAG](papers/2604.23783.md) → [Search-o1](papers/2501.05366.md) → [DocNavRAG](papers/2608.01565.md) → [ACE-GraphRAG](papers/2608.01269.md) | Why “iterative” is too weak a description; the important object is the state representing sufficiency, gaps, progress, and stopping. |
| **How retrieval becomes a learned/resource-aware policy** | [SPARKLE](papers/2026.acl-long.1793.md) → [Agentic-R](papers/2601.11888.md) → [Know Before You Fetch](papers/2606.29959.md) → [SAGE](papers/2608.08237.md) | Why adaptive-vs-adaptive baselines and realized calls/tokens/latency matter more than “adaptive beats static.” |

<details>
<summary><strong>If you only read three papers</strong></summary>

**LLM-Wiki** gives the clearest environment/interface story and a useful structure-vs-traversal ablation. **S2G-RAG** gives an earlier, better-controlled explicit missing-information state baseline. **SPARKLE** raises the learned-policy bar by comparing against other adaptive/search-RL systems rather than only static retrieval.

Together they make the current radar thesis harder to overclaim: **environment, state, policy, and resources are separate research objects and should be evaluated separately.**

</details>

## ⭐ Design Anchors

| Work | Why it is a useful design point |
|---|---|
| **[A-RAG](papers/2602.03442.md)** | Makes keyword search, semantic search, and chunk read an explicit model-controlled retrieval interface. |
| **[LLM-Wiki](papers/2605.25480.md)** | Makes the index product an agent-facing linked environment and ablates progressive traversal against the same structure. |
| **[S2G-RAG](papers/2604.23783.md)** | Makes evidence sufficiency and missing-information gaps explicit state with a matched-budget controller ablation. |
| **[SPARKLE](papers/2026.acl-long.1793.md)** | Separates a learned retrieval policy from the answer LLM and compares against adaptive/search-RL baselines. |
| **[Know Before You Fetch](papers/2606.29959.md)** | Makes retrieval amount a graded action and separates calls, context volume, and measured latency. |
| **[When Should Active RAG Retrieve?](papers/2607.24010.md)** | Makes the router's realized operating point, retrieval harm, calibration transfer, and trigger-side cost auditable. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

A useful progression is:

`information need → agent-facing environment → explicit evidence state → adaptive/learned policy → resource allocation → operating-point evaluation`

The 2026 map is therefore broader than “agent + retriever.” It increasingly looks like **environment × state × policy × realized resources**, with a second question running through the whole stack: which control ideas are new versus newly scalable/learnable with LLMs?

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Question |
|---|---|
| **[Planning & Query Formulation](categories/planning-query-formulation.md)** | What information should be acquired next, and how is that need planned/decomposed? |
| **[Retrieval & Tool Use](categories/retrieval-tool-use.md)** | Which information operations—and how much retrieval resource—should the agent control? |
| **[Iterative Reasoning & Verification](categories/iterative-reasoning-verification.md)** | What state should make the next retrieval, verification, or stopping decision? |
| **[Multi-Agent & Orchestration](categories/multi-agent-orchestration.md)** | When does specialization/coordination justify multiple agents? |
| **[Learning & Optimization](categories/learning-optimization.md)** | What should be learned once retrieval is a trajectory or resource-allocation action space? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we isolate agentic control from stronger tools, budgets, models, or rediscovered prior art? |

<details>
<summary><strong>Planning & Query Formulation — plan first, or react to evidence?</strong></summary>

**Current anchor.** [PlanRAG](papers/2406.12430.md).

**Strongest signal.** Explicit planning gives retrieval a stable upstream objective, but evidence-state systems suggest the next step can instead be selected directly from what remains missing.

**Biggest unresolved question.** When does a precommitted plan beat online replanning after failed or contradictory retrieval?

**Next decisive evidence.** Plan-repair/decomposition experiments under matched resource budgets and structured targets such as SQL, graphs, web, or code.

</details>

<details>
<summary><strong>Retrieval & Tool Use — what should the agent actually be allowed to do?</strong></summary>

**Current anchors.** A-RAG, LLM-Wiki, READ, DocNavRAG, and Know Before You Fetch.

**Strongest signal.** The target is becoming a **minimal sufficient retrieval API with explicit resource semantics**: search/read/navigation plus a clear meaning for calls, context volume, latency, and budget.

**Biggest unresolved question.** How much capability comes from the richer environment, how much from adaptive policy, and how much from resource allocation?

**Next decisive evidence.** Same-substrate operation ablations, fixed-vs-agentic control using identical tools, and adaptive-vs-adaptive budget comparisons at matched realized resources.

</details>

<details>
<summary><strong>Iterative Reasoning & Verification — what state should drive the next retrieval?</strong></summary>

**Current anchors.** S2G-RAG, Search-o1, DocNavRAG, and ACE-GraphRAG.

**Strongest signal.** “Iterative” is too weak a description. The important design object is the **state** representing sufficiency, missing information, provenance, uncertainty, and stopping conditions.

**Biggest unresolved question.** Does explicit evidence state beat a strong raw-history controller once calls/tokens and answer-model capacity are matched?

**Next decisive evidence.** Explicit-state vs raw-history ablations, adaptive vs fixed stopping at equal resources, and conflicting/adversarial-evidence tests.

</details>

<details>
<summary><strong>Multi-Agent & Orchestration — is another agent worth the coordination cost?</strong></summary>

**Current status.** No paper currently clears the radar's precision threshold as a primary multi-agent retrieval contribution; the empty category is intentional.

**Strongest signal.** Parallel LLM calls are not enough. Specialization, evidence coordination, conflict resolution, or adaptive budget allocation must be the research delta.

**Biggest unresolved question.** Does orchestration beat a strong single-agent controller at comparable total model/retrieval budget?

**Next decisive evidence.** Matched-budget many-vs-one comparisons with genuinely different tools/corpora/objectives and explicit coordination analysis.

</details>

<details>
<summary><strong>Learning & Optimization — what should be learned?</strong></summary>

**Current anchors.** SPARKLE, Agentic-R, Graph-R1, and SAGE.

**Strongest signal.** Learning objectives are expanding from local relevance to **trajectory utility and resource allocation**, while SPARKLE makes strong adaptive-vs-adaptive comparison a realistic baseline.

**Biggest unresolved question.** Did the learned policy improve decisions, or merely discover a better average compute allocation than a weak controller/static baseline?

**Next decisive evidence.** Prompted, supervised, and RL controllers on the same interface/base model with matched realized calls/tokens/latency, plus transfer under workload drift.

</details>

<details>
<summary><strong>Evaluation & Analysis — how do we know the “agentic” or “new” part caused the gain?</strong></summary>

**Current anchors.** When Should Active RAG Retrieve?, Forgotten History or Test-of-Time?, and Agentic RAG SoK.

**Strongest signal.** A system score is not enough when papers change **substrate × operation set × state × policy × realized resources × base model**; a novelty claim is also incomplete when the same control pattern has classical IR/QA antecedents.

**Biggest unresolved question.** Can policy quality be measured independently of better tools/resources while identifying what LLM-era capability is genuinely new?

**Next decisive evidence.** Matched operating-point trajectory benchmarks, explicit failure labels, diverse workloads beyond document QA, and modern implementations of strong historical baselines.

</details>

[Explore the full research map →](categories/README.md)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W32 · Convergence, factorization, and a stricter novelty baseline](digests/weekly/2026-W32.md)**  
W32 is a convergence and stress-test of the control stack, not the origin of its components. The sharper question is what a new system adds after matching **environment, explicit state, adaptive baseline, realized resource budget, and historical prior art**.

[Read the full weekly synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map](digests/monthly/2026-08.md)**  
The month-to-date map is `information environment → explicit state → adaptive policy/stopping → resource allocation → operating-point evaluation`. The important August signal is **factorization + stricter causal attribution**, not “the field suddenly discovered adaptive retrieval.”

[Explore the August map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling year-to-date map](digests/yearly/2026.md)**  
The durable 2026 shift is the factorization of information acquisition into separately researchable objects, plus a stricter evaluation bar: strong adaptive baselines, realized resources, and historical IR/QA antecedents.

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
2. **Compared with what—including older prior art?**
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
