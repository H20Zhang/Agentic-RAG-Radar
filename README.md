# 🤖 Agentic RAG Radar

> Daily tracking, taxonomy, and AI research notes for **Agentic Retrieval-Augmented Generation**.

**Agentic RAG Radar** is a GitHub-native living bibliography for research where an agent **dynamically controls retrieval, search, context acquisition, verification, or retrieval policy**. It is designed for researchers who want to know not only *what was published*, but *what changed compared with prior work and why it matters*.

## 🔥 Latest Papers

<!-- DAILY_PAPERS_START -->
_No accepted papers yet. The daily curator will populate this section._
<!-- DAILY_PAPERS_END -->

## ⭐ Notable Recent Work

<!-- NOTABLE_PAPERS_START -->
_Notable papers will be selected by research importance, separately from topical relevance._
<!-- NOTABLE_PAPERS_END -->

## 🗂 Research Taxonomy

| Category | What the agent controls |
|---|---|
| **Planning & Query Formulation** | decomposing questions, planning retrieval steps, rewriting or generating queries |
| **Retrieval & Tool Use** | choosing retrievers, search engines, databases, tools, corpora, or retrieval operators |
| **Iterative Reasoning & Verification** | interleaving retrieval with reasoning, critique, evidence checking, and stopping decisions |
| **Multi-Agent & Orchestration** | coordinating specialized search/retrieval/reasoning agents |
| **Learning & Optimization** | learning retrieval policies, routing, search strategies, or agentic RAG workflows |
| **Evaluation & Analysis** | benchmarks, diagnostic studies, surveys, failure analysis, and evaluation methodology |

Each paper also receives orthogonal tags for retrieval substrate (`dense`, `sparse`, `graph`, `web`, `SQL`, `code`, ...), modality, training paradigm, domain, and benchmark. See [`taxonomy.yaml`](taxonomy.yaml).

## 🧭 What Counts as Agentic RAG?

A paper is included when an agent or learned controller **materially changes the retrieval process at inference or decision time** — for example deciding **whether, what, where, how, or how many times to retrieve**, or using retrieved evidence to decide the next search/retrieval action.

Ordinary fixed `retrieve top-k → generate` pipelines are not included merely because they use an LLM. Generic agents are not included unless retrieval or external knowledge acquisition is a substantive research contribution.

## 🧠 AI Research Notes

For every accepted paper, the curator aims to answer:

- **TL;DR** — the actual research delta in one sentence.
- **Problem / Core Idea** — what bottleneck is addressed and what abstraction changes.
- **Agent Loop / Retrieval Design** — the control flow and retrieval interface.
- **Compared to What** — nearest method families and the real difference.
- **Evidence / Why It Matters** — what experiments support the claim and whether the contribution is important rather than merely relevant.
- **Limitations / Questions / AI Confidence** — assumptions, missing evidence, and confidence in the interpretation.

The AI notes are research aids, not authoritative summaries. Paper claims are distinguished from curator inference whenever possible.

## 📦 Repository Structure

```text
Agentic-RAG-Radar/
├── README.md                     # researcher-facing landing page
├── taxonomy.yaml                 # controlled taxonomy
├── data/
│   ├── paper.schema.json         # canonical record schema
│   └── papers/                   # one JSON record per paper
├── papers/                       # long-form AI research notes
├── templates/paper.md            # analysis template
├── scripts/validate.py           # repository integrity checks
└── .github/workflows/validate.yml
```

The canonical source of truth is `data/papers/*.json`; README and category views are derived representations.

## 🔄 Daily Curation

A daily research task performs broad discovery with an overlapping recent window, semantic inclusion filtering, taxonomy assignment, full-paper interpretation, deduplication, and independent quality control. **Relevance and importance are scored separately.** Updates should preferably land as reviewable GitHub changes rather than opaque generated prose.

Discovery intentionally searches beyond the phrase “agentic RAG”, including adaptive/active retrieval, retrieval planning, search agents, iterative retrieval, verifier-guided retrieval, GraphRAG agents, tool-using RAG, retrieval RL, and agentic information seeking.

## 🤝 Contributing

PRs that add missing papers, correct taxonomy, improve evidence, or challenge an AI interpretation are welcome. Please preserve provenance and distinguish paper-stated claims from your own interpretation.

---

If this radar saves you research time, consider starring the repo so it is easier to find again.
