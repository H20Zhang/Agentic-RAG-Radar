# 🤖 Agentic RAG Radar

**A living research map of Agentic Retrieval-Augmented Generation.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical AI research notes, visual explainers, and weekly/monthly synthesis.

**Last updated:** 2026-08-11 · [Weekly synthesis](digests/weekly/2026-W32.md) · [August research map](digests/monthly/2026-08.md) · [Browse by research problem](categories/README.md)

## 🧭 Research Compactions

If you only have a few minutes, **start here**. These reports compress individual papers into the research shifts, tensions, and open questions that matter.

### [Weekly · 2026-W32](digests/weekly/2026-W32.md)

**Early-August Agentic RAG is shifting from “better retrieval” toward designing the retrieval interaction itself.**

Three ideas are beginning to converge:

- **Retrieval interface > another agent loop.** READ and DocNavRAG expose lexical search, structural navigation, bounded reads, or document-native graph operations instead of repeatedly calling the same black-box top-k primitive.
- **Evidence state > implicit history.** DocNavRAG makes collected/missing evidence explicit, turning retrieval progress into state that can drive the next action and stopping decision.
- **Context assembly becomes a policy.** ACE-GraphRAG separates rich hierarchical representation from the inference-time policy that decides which evidence actually reaches the model.

The main tension is causal attribution: **are gains coming from agentic control, or simply from stronger retrieval primitives and larger budgets?** READ is especially informative because BM25 is reported as statistically indistinguishable from READ, weakening a simplistic “agent beats RAG” story.

**Suggested reading:** A-RAG → READ → DocNavRAG → ACE-GraphRAG → Agentic-R / Graph-R1.  
[Read the full weekly synthesis →](digests/weekly/2026-W32.md)

### [Monthly · 2026-08 (rolling)](digests/monthly/2026-08.md)

**Month-to-date thesis:** Agentic RAG is beginning to look less like a retriever problem and more like a **control-stack problem**:

`retrieval substrate → operation/interface → evidence state/controller → learning/evaluation`

The current August map has three provisional clusters: **retrieval-interface redesign**, **stateful evidence construction**, and **adaptive context engineering**. The key unresolved issue is evaluation: a credible comparison increasingly needs to separate **substrate, operation set, state, policy, budget, and base model** rather than changing several at once and attributing the gain to “agentic RAG.”

[Explore the rolling August research map →](digests/monthly/2026-08.md)

<details>
<summary><strong>What is a research compaction?</strong></summary>

Paper-by-paper notes preserve detail; compactions answer a different question: **what changed in the research landscape?**

Weekly reports identify the few shifts worth carrying forward, compare the papers that actually change a design point, and preserve tensions or negative results. Monthly reports rebuild the field map at a higher level and revise earlier interpretations when new evidence weakens them.

The goal is **lossy compression of repetition, not loss of disagreement**.

</details>

## 🔥 Latest Papers

### [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](papers/2608.06305.md)
`Retrieval & Tool Use` · `sparse` `documents` `iterative search` · **★★★★☆** · 2026-08-06

**AI take:** The strongest result is not “agents beat RAG.” It is that an iterative agent cannot rescue a bad retrieval primitive: lexical search + structural navigation + bounded reads strongly outperform dense top-k, while **BM25 is statistically indistinguishable from READ**. That negative result makes the paper more informative, not less.

[Paper](https://arxiv.org/abs/2608.06305) · [Research note](papers/2608.06305.md)

### [DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction](papers/2608.01565.md)
`Retrieval & Tool Use` · `graph` `documents` `planning` `multi-hop QA` · **★★★★☆** · 2026-08-03

**AI take:** The useful abstraction is **environment–policy co-design**: preserve document-native hierarchy/relations as retrieval operations, then maintain explicit collected/missing evidence state so the next action is conditioned on information progress rather than another global search.

[Paper](https://arxiv.org/abs/2608.01565) · [Research note](papers/2608.01565.md)

### [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](papers/2608.01269.md)
`Iterative Reasoning & Verification` · `graph` `routing` `multi-hop QA` · **★★★★☆** · 2026-08-02

**AI take:** Building a richer hierarchy does not guarantee better context. ACE-GraphRAG makes the missing layer explicit: **context assembly itself is a query-dependent policy** over complementary retrieval branches. The remaining question is whether gains survive matched retrieval/token budgets.

[Paper](https://arxiv.org/abs/2608.01269) · [Research note](papers/2608.01269.md)

## ⭐ Design Anchors

Use these to orient yourself in the design space rather than as a “best papers” ranking.

| Work | Why it is a useful design point |
|---|---|
| **[A-RAG](papers/2602.03442.md)** | Exposes keyword search, semantic search, and chunk reads as an agent-controlled retrieval interface. |
| **[Search-o1](papers/2501.05366.md)** | Makes search an action inside the reasoning trace rather than a preprocessing step. |
| **[Graph-R1](papers/2507.21892.md)** | Learns multi-turn graph retrieval/reasoning trajectories end to end with RL. |
| **[Agentic-R](papers/2601.11888.md)** | Trains retrieval for trajectory-level downstream utility instead of static relevance. |
| **[PlanRAG](papers/2406.12430.md)** | Makes the information-acquisition plan explicit before iterative retrieval. |
| **[Agentic RAG SoK](papers/2603.07379.md)** | Frames Agentic RAG as a sequential retrieval/control process. |

[See the full anchor notes →](papers/anchors.md)

## 🗂 Browse by Research Problem

Rather than grouping papers only by application, the radar asks **which part of the Agentic RAG control stack is changing?**

| Research problem | Question |
|---|---|
| **[Planning & Query Formulation](categories/planning-query-formulation.md)** | What should be retrieved next, and how is the information need decomposed or reformulated? |
| **[Retrieval & Tool Use](categories/retrieval-tool-use.md)** | Which retriever, corpus, operation, database, or tool should the agent invoke? |
| **[Iterative Reasoning & Verification](categories/iterative-reasoning-verification.md)** | How does new evidence change the next retrieval, reasoning, or stopping decision? |
| **[Multi-Agent & Orchestration](categories/multi-agent-orchestration.md)** | When does specialization or coordination justify multiple retrieval agents? |
| **[Learning & Optimization](categories/learning-optimization.md)** | How should retrieval/routing/search policies be trained rather than hand-prompted? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we isolate agentic control from better tools, larger budgets, or benchmark artifacts? |

[Explore the research map →](categories/README.md)

## 🖼️ How to Read a Paper Here

Each accepted paper is intended to tell you more than its abstract:

- **Visual explainer** — one original conceptual figure focused on the key mechanism or research delta.
- **Research read** — problem, core idea, agent loop, retrieval design, and the closest comparison point.
- **Evidence check** — strongest evidence, important negative results, and likely confounders.
- **Why it matters** — whether the paper changes a reusable design point or is mainly incremental.
- **Limitations / open questions** — assumptions or missing tests that could change the conclusion.

## What Counts as Agentic RAG?

A work is included when **external retrieval/search/context acquisition is a substantive research component and an agent, controller, or learned policy materially changes whether, what, where, how, or how many times information is retrieved**.

Ordinary fixed `retrieve top-k → generate` pipelines are not included merely because they use an LLM. Generic agents are excluded when retrieval is incidental. Pure retriever/reranker/index work is excluded unless agentic control is itself part of the research contribution.

## About the Radar

This is a **curated research map, not an exhaustive keyword feed**. The aim is to help researchers answer three questions quickly:

1. **What is actually new?**
2. **Compared with what?**
3. **Does the evidence justify the claim?**

Relevance and importance are deliberately separated, and negative results are kept when they change the interpretation of a paper.

## 🤝 Contributing

Corrections are especially welcome when they change the research conclusion: a missing baseline, unfair budget, wrong taxonomy, overclaimed novelty, broken provenance, or a visual that makes the mechanism look cleaner than it really is.

<details>
<summary><strong>Methodology & maintenance</strong></summary>

The public README intentionally hides most maintenance mechanics. If you want the reproducibility and curation details, see the [maintainer guide](docs/MAINTENANCE.md), [curation protocol](CURATION.md), [compaction protocol](COMPACTION.md), [visual grounding rules](VISUALS.md), [taxonomy](taxonomy.yaml), and [structured paper records](data/papers/).

</details>

---

If this radar saves you research time, consider starring the repo.