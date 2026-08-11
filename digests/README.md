# 🧭 Agentic RAG Research Compactions

Start here when you want the **research picture**, not a list of papers.

Compactions answer three questions:

1. **What changed?**
2. **Which papers actually matter?**
3. **What should we believe or test next?**

## Latest Weekly

### [2026-W32 · Designing the retrieval interaction](weekly/2026-W32.md)

**Thesis:** early-August Agentic RAG work is moving beyond “call a better retriever more times” toward **designing the retrieval interface, making evidence progress explicit, and treating context construction as a policy**.

The strongest tension is equally important: READ reports BM25 as statistically indistinguishable from its agentic method. That suggests some apparent Agentic RAG gains may come from **better retrieval primitives rather than better adaptive control**.

**Best entry path:** A-RAG → READ → DocNavRAG → ACE-GraphRAG.  
[Read the weekly synthesis →](weekly/2026-W32.md)

## Current Monthly Map

### [2026-08 · Rolling research map](monthly/2026-08.md)

**Current thesis:** Agentic RAG is beginning to look like a control stack:

`retrieval substrate → operation/interface → evidence state/controller → learning/evaluation`

Three provisional clusters organize the month so far:

- **Retrieval-interface redesign** — richer operations than fixed top-k.
- **Stateful evidence construction** — explicit representations of what is known and missing.
- **Adaptive context engineering** — query-dependent policies for assembling context from richer substrates.

The unresolved research problem is causal attribution: to understand whether an “agentic” method is genuinely better, comparisons increasingly need to separate **substrate, operation set, state, policy, budget, and base model**.

[Explore the August research map →](monthly/2026-08.md)

## How to Use These Reports

**Weekly** is for deciding what to read now. It keeps the few shifts, disagreements, and papers worth carrying into the next week.

**Monthly** is for deciding how your mental model of the field should change. It revisits older anchors when new work makes them look different and highlights open problems that may deserve research investment.

Paper-level details remain available in [`../papers/`](../papers/) and the [research-problem map](../categories/README.md).

---

For curation and compaction methodology, see the [maintainer guide](../docs/MAINTENANCE.md).