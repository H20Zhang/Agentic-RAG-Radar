# 🤖 Agentic RAG Radar

A daily-updated, GitHub-native research radar for **Agentic Retrieval-Augmented Generation**, with a stable taxonomy, skeptical AI research notes, and visual explainers designed for researchers rather than generic summaries.

> **Maintenance model:** one scheduled ChatGPT curation task maintains the repo. Daily runs discover and curate papers; the same run backfills visuals and conditionally produces weekly/monthly research compactions. GitHub Actions only validates repository consistency.

**Last curated:** 2026-08-10

## 🧭 Research Compactions

Compactions are the **primary reading interface**. Daily ingestion preserves freshness and provenance; weekly/monthly reports answer the harder question: **what actually changed in the research landscape?**

### [Weekly · 2026-W32](digests/weekly/2026-W32.md)

**Early-August Agentic RAG is shifting from “better retrieval” toward designing the retrieval interaction itself.** Three ideas are beginning to converge:

- **Retrieval interface > another agent loop.** READ and DocNavRAG expose lexical search, structural navigation, bounded reads, or document-native graph operations instead of repeatedly calling the same black-box top-k primitive.
- **Evidence state > implicit history.** DocNavRAG makes collected/missing evidence explicit, turning retrieval progress into state that can drive the next action and stopping decision.
- **Context assembly becomes a policy.** ACE-GraphRAG separates rich hierarchical representation from the inference-time policy that decides which evidence actually reaches the model.

The main tension is causal attribution: **are gains coming from agentic control, or simply from stronger retrieval primitives and larger budgets?** READ is especially useful because BM25 is reported as statistically indistinguishable from READ, weakening a simplistic “agent beats RAG” story and raising the bar for primitive-matched and budget-matched evaluation.

**Read next:** A-RAG → READ → DocNavRAG → ACE-GraphRAG → Agentic-R / Graph-R1.

### [Monthly · 2026-08 (rolling)](digests/monthly/2026-08.md)

**Month-to-date thesis:** Agentic RAG is beginning to look less like a retriever problem and more like a **control-stack problem**:

`retrieval substrate → operation/interface → evidence state/controller → learning/evaluation`

The current August map has three provisional clusters:

1. **Retrieval-interface redesign** — replace one-shot top-k with a compact action space the agent can control.
2. **Stateful evidence construction** — explicitly track what is known, missing, sufficient, or uncertain between retrieval actions.
3. **Adaptive context engineering** — treat routing/context assembly over rich document/graph structures as an inference-time policy.

The most important open problem is evaluation. A credible comparison increasingly needs to separate **substrate, operation set, state, policy, and budget** rather than changing all five and attributing the gain to “agentic RAG.” The rolling month map will be revised—not merely appended—if later papers falsify this thesis.

### How compaction works

This repo uses a small research-memory hierarchy:

- **Daily ingestion** keeps canonical paper records, provenance, classification, links, research notes, and visual explainers current. It does **not** create one Markdown file per day.
- **Weekly compaction** compresses the completed week into 1–3 research shifts, the few papers that matter, an evidence audit, disagreements/negative results, and a minimal reading order.
- **Monthly compaction** rebuilds the higher-level field map: which abstractions are gaining traction, what evidence strengthened or weakened, and which open questions should influence what to research next.

Compaction is deliberately **lossy for repetition, not for disagreement**. Weekly/monthly claims are re-grounded in canonical paper records instead of recursively summarizing prior summaries. See [`COMPACTION.md`](COMPACTION.md) and the [`digest archive`](digests/README.md).

## 🔥 Latest Papers

### [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](papers/2608.06305.md)
`Retrieval & Tool Use` · `sparse` `documents` `iterative search` · **★★★★☆** · 2026-08-06

**AI take:** The strongest result is not “agents beat RAG.” It is that an iterative agent cannot rescue a bad retrieval primitive: lexical search + structural navigation + bounded reads strongly outperform dense top-k, while **BM25 is statistically indistinguishable from READ**. That negative result makes the paper more informative, not less.

[Paper](https://arxiv.org/abs/2608.06305) · [AI Analysis](papers/2608.06305.md)

### [DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction](https://arxiv.org/abs/2608.01565)
`Retrieval & Tool Use` · `graph` `documents` `planning` `multi-hop QA` · **★★★★☆** · 2026-08-03

**AI take:** The useful abstraction is **environment–policy co-design**: preserve document-native hierarchy/relations as retrieval operations, then maintain explicit collected/missing evidence state so the next action is conditioned on information progress rather than another global search.

[Paper](https://arxiv.org/abs/2608.01565)

### [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](https://arxiv.org/abs/2608.01269)
`Iterative Reasoning & Verification` · `graph` `routing` `multi-hop QA` · **★★★★☆** · 2026-08-02

**AI take:** Building a richer hierarchy does not guarantee better context. ACE-GraphRAG makes the missing layer explicit: **context assembly itself is a query-dependent policy** over complementary retrieval branches. The remaining question is whether gains survive matched retrieval/token budgets.

[Paper](https://arxiv.org/abs/2608.01269)

## ⭐ Notable Design Anchors

These are not “top papers of all time”; they are useful design points for understanding the current radar:

- **[A-RAG](https://arxiv.org/abs/2602.03442)** — hierarchical keyword / semantic / chunk-read retrieval interface controlled by the model.
- **[Agentic-R](https://arxiv.org/abs/2601.11888)** — train retrieval for trajectory-level downstream utility rather than static relevance.
- **[Graph-R1](https://arxiv.org/abs/2507.21892)** — learn multi-turn graph retrieval/reasoning trajectories end to end with RL.
- **[Search-o1](https://arxiv.org/abs/2501.05366)** — trigger search inside the reasoning trace and separately reason over retrieved documents before reinjection.
- **[PlanRAG](https://arxiv.org/abs/2406.12430)** — make the information-acquisition plan explicit before iterative data retrieval.

[Read the bootstrap anchor cards →](papers/anchors.md)

## 🗂 Browse by Research Problem

The primary taxonomy asks **what part of the Agentic RAG control stack changes**, rather than classifying papers only by application domain:

| Category | Core question |
|---|---|
| **Planning & Query Formulation** | What should be retrieved next, and how is the information need decomposed/reformulated? |
| **Retrieval & Tool Use** | Which retriever, corpus, operation, database, or tool should the agent invoke? |
| **Iterative Reasoning & Verification** | How does new evidence change the next retrieval/reasoning/stopping decision? |
| **Multi-Agent & Orchestration** | How are specialized search/retrieval/reasoning agents coordinated? |
| **Learning & Optimization** | How should retrieval/routing/search policies be trained rather than hand-prompted? |
| **Evaluation & Analysis** | How do we isolate agentic control from better tools, larger budgets, or benchmark artifacts? |

Orthogonal tags capture substrate (`dense`, `sparse`, `graph`, `web`, `SQL`, `code`, ...), modality, training paradigm, task/domain, and control pattern. See [`taxonomy.yaml`](taxonomy.yaml).

## 🧭 Inclusion Rule

A work is included when **external retrieval/search/context acquisition is a substantive research component and an agent/controller/policy materially changes whether, what, where, how, or how many times information is retrieved**.

Ordinary fixed `retrieve top-k → generate` RAG is excluded merely for using an LLM. Generic agents are excluded when retrieval is incidental. Pure retriever/reranker/index work is excluded unless agentic control is part of the research contribution.

## 🖼️ Research Note for Each Paper

Each accepted paper should eventually have one concise researcher-facing page with:

- **GPT-image-gen visual explainer** — one original conceptual figure showing the paper's key control point / state / feedback loop, not a reproduction of the paper figure.
- **TL;DR / Problem / Core Idea** — the actual research delta.
- **Agent Loop / Retrieval Design** — what the model observes, chooses, retrieves, updates, and repeats.
- **Compared to What** — the nearest design point and the real difference.
- **Evidence / Why It Matters** — strongest support, important negative results, and whether the contribution is interesting or actually important.
- **Limitations / Questions / AI Confidence** — assumptions and missing tests that could change the conclusion.

Image assets are presentation; their research grounding is stored separately so a figure can be regenerated or challenged without losing provenance. See [`VISUALS.md`](VISUALS.md).

## 🔄 Curation & Provenance

The scheduled curator uses independent roles for broad discovery, inclusion/taxonomy, deep reading, visual explanation, evidence auditing, and skeptical QC. The QC role explicitly challenges novelty, matched-budget fairness, baseline choice, unsupported claims, and misleading visual simplifications before synthesis.

Canonical structured records live under [`data/papers/`](data/papers/). README, paper notes, generated figures, and compactions are derived views. Full-text-grounded claims are distinguished from abstract-grounded first-pass interpretations.

## 🤝 Contributing

Corrections are especially welcome when they change the research conclusion: missing baselines, unfair budgets, wrong taxonomy, overclaimed novelty, broken provenance, or a visual that makes the mechanism look cleaner than it really is.

---

If this radar saves you research time, consider starring the repo so it is easier to find again.