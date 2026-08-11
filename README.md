# 🤖 Agentic RAG Radar

**A living research map of Agentic Retrieval-Augmented Generation.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical AI research notes, visual explainers, and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-11 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](categories/README.md)

## 🧭 Research Compactions

If you only have a few minutes, **start here**. The archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

### Recent Month · Weekly

Weekly compactions preserve the local research movement while it is still useful to inspect week by week.

**[2026-W32 · Designing the retrieval interaction](digests/weekly/2026-W32.md)**  
Early-August Agentic RAG is shifting from “better retrieval” toward **designing the retrieval interaction itself**: richer operation spaces, explicit evidence state, and adaptive context policies. The central tension is whether gains come from agentic control or from stronger primitives and larger budgets; READ's BM25 result is the strongest current warning against over-attribution.

**Suggested reading:** A-RAG → READ → DocNavRAG → ACE-GraphRAG → Agentic-R / Graph-R1.  
[Read the full weekly synthesis →](digests/weekly/2026-W32.md)

> As new weeks arrive, this section keeps the meaningful weekly compactions from roughly the latest month. Older weekly reports remain in the repository but stop competing for homepage attention once monthly synthesis covers them.

### Recent Quarter · Monthly

Monthly compactions answer a slower question: **how should your mental model of the field change?**

**[2026-08 · Rolling research map](digests/monthly/2026-08.md)**  
Agentic RAG is beginning to look less like a retriever problem and more like a **control-stack problem**:

`retrieval substrate → operation/interface → evidence state/controller → learning/evaluation`

The current August map has three provisional clusters: **retrieval-interface redesign**, **stateful evidence construction**, and **adaptive context engineering**. The unresolved issue is causal attribution across **substrate × operation set × state × policy × budget × base model**.

[Explore the rolling August research map →](digests/monthly/2026-08.md)

> This section keeps monthly maps from roughly the latest quarter. Older monthly reports remain available, but the long-term public history is compressed again at yearly granularity.

### All Years · Yearly

Yearly compactions are the durable archive: **what survived the year, what weakened, which papers defined the field, and what questions carried forward?**

**[2026 · Rolling year-to-date map](digests/yearly/2026.md)**  
The strongest 2026 signal so far is a move from “agent + retriever” toward an explicit **information-acquisition control stack** in which retrieval operations, evidence state, adaptive policy, and trajectory-level learning/evaluation are increasingly separable research objects.

This report is deliberately labeled rolling. Earlier historical years will only receive an annual map after backfill is sufficiently complete; a few selected anchors will never be presented as “full-year coverage.”

[Explore the 2026 year-to-date map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** keeps local changes and disagreements while they are fresh. **Monthly** compresses several weeks into field-map movement. **Yearly** re-evaluates the entire period and preserves only durable shifts, defining papers, failed or weakening ideas, evidence standards, and open problems entering the next year.

Lower-level reports are retained for provenance; they simply age out of the primary reading surface. Higher-level reports are also **re-grounded from canonical paper records**, not produced by recursively summarizing lower-level prose.

</details>

## 🚀 Start Here

Different papers matter depending on what you want to understand. These are deliberately short reading paths rather than exhaustive lists.

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Why Agentic RAG is more than repeated top-k** | [A-RAG](papers/2602.03442.md) → [READ](papers/2608.06305.md) → [DocNavRAG](papers/2608.01565.md) | How the retrieval API itself becomes part of the research design. |
| **How retrieval becomes a sequential policy** | [Search-o1](papers/2501.05366.md) → [ACE-GraphRAG](papers/2608.01269.md) → [Graph-R1](papers/2507.21892.md) | How observations, state, routing, stopping, and policy interact across multiple retrieval steps. |
| **How Agentic RAG should be learned and evaluated** | [Agentic-R](papers/2601.11888.md) → [Graph-R1](papers/2507.21892.md) → [Agentic RAG SoK](papers/2603.07379.md) → [August map](digests/monthly/2026-08.md) | Why trajectory utility, matched budgets, and causal attribution matter more than another unconstrained QA score. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**A-RAG** gives the cleanest starting abstraction: retrieval is an **interface of controllable operations**, not just a retriever call.

**READ** is useful because it both strengthens and attacks the agentic story: richer retrieval operations help substantially, yet BM25 matching READ warns that the primitive may matter more than the policy.

**DocNavRAG** adds the next layer: the agent needs not only operations, but also explicit **evidence/progress state** telling it what has been collected and what remains missing.

Together they motivate the current radar thesis: **Agentic RAG is increasingly a problem of environment + state + policy co-design.**

</details>

## 🔥 Latest Papers

### [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](papers/2608.06305.md)
`Retrieval & Tool Use` · `sparse` `documents` `iterative search` · **★★★★☆** · 2026-08-06

**AI take:** The strongest result is not “agents beat RAG.” It is that an iterative agent cannot rescue a bad retrieval primitive: lexical search + structural navigation + bounded reads strongly outperform dense top-k, while **BM25 is statistically indistinguishable from READ**. That negative result makes the paper more informative, not less.

[Paper](https://arxiv.org/abs/2608.06305) · [Research note](papers/2608.06305.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Chunk-and-embed retrieval can destroy structural context in table-heavy long documents, especially when values depend on distant headers, units, or layout.

**Core mechanism.** Replace one opaque dense top-k call with three explicit operations the agent can compose: **lexical search → structural navigation → bounded read**.

**Agent loop.** `Search → navigate → bounded read → inspect → refine → answer`

**Compared with.** Dense top-k RAG, the same iterative agent loop restricted to a top-k tool, and BM25.

**Evidence to remember.** The abstract reports 58.8% accuracy versus 15.7% for dense retrieval and 27.5% for the same agent loop with top-k. But BM25 is statistically indistinguishable from READ — so the strongest conclusion is about the **retrieval interface / primitive**, not that agentic control itself is always necessary.

**Open question.** Under matched lexical primitives and retrieval budgets, how much extra value comes from adaptive agent composition?

</details>

### [DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction](papers/2608.01565.md)
`Retrieval & Tool Use` · `graph` `documents` `planning` `multi-hop QA` · **★★★★☆** · 2026-08-03

**AI take:** The useful abstraction is **environment–policy co-design**: preserve document-native hierarchy/relations as retrieval operations, then maintain explicit collected/missing evidence state so the next action is conditioned on information progress rather than another global search.

[Paper](https://arxiv.org/abs/2608.01565) · [Research note](papers/2608.01565.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Complex document questions need complementary evidence across sections or documents. Flat retrieval repeatedly reconstructs location through semantic similarity, while many GraphRAG systems build structure but traverse it with a fixed policy.

**Core mechanism.** Turn document hierarchy and cross-region relations into a navigable environment, expose operations such as locate / navigate / expand / fetch, and maintain explicit **collected evidence + missing evidence** state.

**Agent loop.** `Locate → navigate/expand → fetch → update evidence state → identify what is missing → continue or answer`

**Compared with.** Flat passage-level iterative RAG, repeated global semantic search, and fixed-traversal GraphRAG.

**Evidence to remember.** The abstract reports average gains of **7.8% in answer quality** and **17.7% in context sufficiency** across four long-/multi-document QA benchmarks. The current radar has not yet isolated how much comes from structure, evidence state, or additional retrieval budget.

**Open question.** Does explicit evidence state remain useful when the retrieval substrate changes from long documents to web search, SQL, code, or knowledge graphs?

</details>

### [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](papers/2608.01269.md)
`Iterative Reasoning & Verification` · `graph` `routing` `multi-hop QA` · **★★★★☆** · 2026-08-02

**AI take:** Building a richer hierarchy does not guarantee better context. ACE-GraphRAG makes the missing layer explicit: **context assembly itself is a query-dependent policy** over complementary retrieval branches. The remaining question is whether gains survive matched retrieval/token budgets.

[Paper](https://arxiv.org/abs/2608.01269) · [Research note](papers/2608.01269.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A hierarchical GraphRAG can represent rich multi-resolution evidence and still send the wrong context to the model because context construction remains fixed.

**Core mechanism.** Add an inference-time context policy that detects context gaps and chooses between complementary **depth-oriented factual** and **breadth-oriented semantic** retrieval branches before consolidating evidence.

**Agent loop.** `Build context → detect gap → choose branch → retrieve → consolidate → adapt → generate`

**Compared with.** Hierarchical GraphRAG with fixed or largely predetermined context construction.

**Evidence to remember.** The abstract reports gains on HotpotQA, 2WikiMultiHopQA, and UltraDomain subsets, but the radar still needs full-paper budget matching and component ablations before assigning those gains specifically to the adaptive policy.

**Open question.** Is the policy itself better, or does the system simply spend more retrieval/context budget through multiple branches?

</details>

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

<details>
<summary><strong>How these anchors fit together</strong></summary>

One useful way to read the field is as a sequence of changing control boundaries:

1. **PlanRAG** — make the information-acquisition **plan** explicit.
2. **Search-o1** — move retrieval **inside the reasoning trajectory**.
3. **A-RAG** — replace one retrieval call with an explicit **operation/interface hierarchy**.
4. **Graph-R1** — treat retrieval actions as a **multi-turn policy** and optimize the trajectory with RL.
5. **Agentic-R** — train the retriever for **trajectory-level downstream utility**, not static relevance alone.
6. **Agentic RAG SoK** — abstract these systems as a broader **sequential retrieval/control problem**.

The current 2026 work is pushing especially hard on the middle of this stack: **what operations the agent controls, what state it carries, and how context policy should adapt under a budget.**

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

Rather than grouping papers only by application, the radar asks **which part of the Agentic RAG control stack is changing?** Open a research problem for the current design points, strongest signal, and the next decisive question.

| Research problem | Question |
|---|---|
| **[Planning & Query Formulation](categories/planning-query-formulation.md)** | What should be retrieved next, and how is the information need decomposed or reformulated? |
| **[Retrieval & Tool Use](categories/retrieval-tool-use.md)** | Which retriever, corpus, operation, database, or tool should the agent invoke? |
| **[Iterative Reasoning & Verification](categories/iterative-reasoning-verification.md)** | How does new evidence change the next retrieval, reasoning, or stopping decision? |
| **[Multi-Agent & Orchestration](categories/multi-agent-orchestration.md)** | When does specialization or coordination justify multiple retrieval agents? |
| **[Learning & Optimization](categories/learning-optimization.md)** | How should retrieval/routing/search policies be trained rather than hand-prompted? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we isolate agentic control from better tools, larger budgets, or benchmark artifacts? |

<details>
<summary><strong>Planning & Query Formulation — plan first, or react to evidence?</strong></summary>

**Current anchor.** [PlanRAG](papers/2406.12430.md): make the information-acquisition plan explicit before iterative retrieval.

**Strongest signal.** Explicit planning gives the retrieval process a stable upstream objective, but recent stateful systems raise a competing design: decide the next step directly from what evidence is still missing.

**Biggest unresolved question.** When is a precommitted plan better than online replanning, especially after contradictory or failed retrieval?

**Next decisive evidence.** Plan-repair and decomposition experiments under matched retrieval/token budgets, ideally over structured targets such as SQL, graphs, web, or code rather than only passage queries.

[Explore this research problem →](categories/planning-query-formulation.md)

</details>

<details>
<summary><strong>Retrieval & Tool Use — what should the agent actually be allowed to do?</strong></summary>

**Current anchors.** [A-RAG](papers/2602.03442.md), [READ](papers/2608.06305.md), and [DocNavRAG](papers/2608.01565.md).

**Strongest signal.** This is the strongest current cluster: the field is moving from “choose a retriever” toward **designing a minimal sufficient retrieval API** — search, navigation, read, graph operations, or other data-native actions.

**Biggest unresolved question.** How much capability comes from a richer action space, and how much from the agent policy choosing among those actions?

**Next decisive evidence.** Same-controller operation-set ablations, same-operation fixed-vs-agentic policy comparisons, matched calls/tokens/latency, and transfer of one interface across documents, web, SQL, graphs, and code.

[Explore this research problem →](categories/retrieval-tool-use.md)

</details>

<details>
<summary><strong>Iterative Reasoning & Verification — what state should drive the next retrieval?</strong></summary>

**Current anchors.** [Search-o1](papers/2501.05366.md) and [ACE-GraphRAG](papers/2608.01269.md), with DocNavRAG providing an important adjacent signal around explicit evidence state.

**Strongest signal.** Iteration alone is becoming too weak a description. The emerging question is what **progress/evidence state** the controller should maintain, how it detects a gap, and when it should stop.

**Biggest unresolved question.** Does explicit evidence/progress state outperform simply conditioning on the raw reasoning/history once retrieval budgets are matched?

**Next decisive evidence.** Explicit-state vs raw-history ablations, adaptive vs fixed stopping at equal budgets, and conflict/adversarial-evidence tests.

[Explore this research problem →](categories/iterative-reasoning-verification.md)

</details>

<details>
<summary><strong>Multi-Agent & Orchestration — is another agent worth the coordination cost?</strong></summary>

**Current status.** No paper currently clears this radar's precision threshold as a primary multi-agent retrieval contribution. That emptiness is intentional.

**Strongest signal.** Parallel LLM calls are not enough. A convincing multi-agent RAG contribution needs identifiable specialization, coordination, conflict resolution, or adaptive budget allocation.

**Biggest unresolved question.** Does orchestration outperform a strong single-agent controller when total model and retrieval budgets are comparable?

**Next decisive evidence.** Matched-budget many-vs-one comparisons where agents truly have different tools/corpora/evidence objectives and where coordination quality, not extra compute, explains the gain.

[Explore this research problem →](categories/multi-agent-orchestration.md)

</details>

<details>
<summary><strong>Learning & Optimization — what should be learned once retrieval is a trajectory?</strong></summary>

**Current anchors.** [Agentic-R](papers/2601.11888.md) and [Graph-R1](papers/2507.21892.md).

**Strongest signal.** Static relevance becomes a mismatched objective once retrieval is one action in a multi-step policy. Training is starting to target trajectory utility rather than isolated query–passage similarity.

**Biggest unresolved question.** What deserves credit when the final answer improves — the retriever, intermediate actions, the controller, or the changed environment/action space?

**Next decisive evidence.** Learned-vs-prompted policies on the same interface, convincing intermediate-action credit assignment, transfer across agents/substrates, and sample-efficiency/stability analysis beyond final QA accuracy.

[Explore this research problem →](categories/learning-optimization.md)

</details>

<details>
<summary><strong>Evaluation & Analysis — how do we know the “agentic” part caused the gain?</strong></summary>

**Current anchor.** [Agentic RAG SoK](papers/2603.07379.md) provides a sequential-decision framing; recent READ/DocNavRAG/ACE results expose why stronger evaluation is needed.

**Strongest signal.** A system-level score is not enough when papers simultaneously change **substrate × operation set × state × policy × budget × base model**.

**Biggest unresolved question.** Can we measure policy/trajectory quality independently of simply giving a system better tools, more retrieval calls, or more context?

**Next decisive evidence.** Matched-budget trajectory benchmarks, explicit failure labels for routing/stopping/state/tool-selection, diverse workloads beyond document QA, and reproducible quality–cost frontiers.

[Explore this research problem →](categories/evaluation-analysis.md)

</details>

[Explore the full research map →](categories/README.md)

## 🖼️ How to Read a Paper Here

The README is intentionally layered:

- **30-second scan:** title, category, importance, and the one-paragraph AI take.
- **60-second expand:** problem, mechanism, agent loop, closest comparison, strongest evidence, and the one open question that matters most.
- **Deep dive:** open the full research note for the visual explainer, detailed evidence, limitations, and provenance.

This keeps the homepage useful both as a radar and as a lightweight reading interface. GitHub's native collapsed sections let the deeper layer stay available without making the default view dense.

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