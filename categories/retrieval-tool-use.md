# Retrieval & Tool Use

> **Core question:** What retrieval operations, corpora, tools, or databases should the agent be able to invoke—and what information should each operation expose back to the controller?

This category covers the **retrieval interface / action space**. The main design variable is not just the retriever model; it is what operations are exposed, how they can be composed, and increasingly **how much retrieval resource** an action is allowed to consume.

## Current papers

### [LLM-Wiki](../papers/2605.25480.md) — ★★★★☆

**Design point:** compile documents into a persistent linked Wiki and expose search/read/link traversal as an agent-native environment rather than a flat retrieval index.

**Strong ablation:** keeping the compiled Wiki but disabling progressive traversal causes a reported 11.7–13.8 F1 drop, giving direct evidence that runtime composition adds value beyond the richer substrate.

**Caveat:** public multi-hop experiments use bounded benchmark corpora rather than web-scale Wikipedia; compilation cost and maintenance are real system costs.

### [Beyond Top-K / READ](../papers/2608.06305.md) — ★★★★☆

**Design point:** replace one opaque dense top-k call with lexical search, structural navigation, and bounded reads.

**Skeptical result:** BM25 is reported as statistically indistinguishable from READ, so the evidence favors an interface/lexical-access claim more strongly than a generic “agentic beats non-agentic” claim.

### [DocNavRAG](../papers/2608.01565.md) — ★★★★☆

**Design point:** make document-native hierarchy and cross-region relations navigable operations while carrying explicit collected/missing evidence state.

**Open attribution:** structure, state, and retrieval budget all need component-level separation.

### [A-RAG](../papers/2602.03442.md) — ★★★★☆

**Design point:** expose keyword search, semantic search, and chunk read as a hierarchy of model-controlled retrieval actions.

**Why it is an anchor:** it makes retrieval API design a first-class systems question rather than hard-coding another workflow.

### [Know Before You Fetch](../papers/2606.29959.md) — ★★★★☆

**Design point:** make retrieval amount an explicit action: answer closed-book, retrieve compact context, retrieve full context, or abstain based on calibrated correctness probability.

**Important negative result:** compact retrieval can improve passage-budget/full-context frontiers without reducing retrieval-call rate, and the confidence probe can make gating slower on smaller readers. “Less context” is not the same as “less retrieval cost.”

## Current tension

The interface question has expanded from **which operations?** to **which operations at what resource budget?** A richer action space can improve capability while making control harder, and adaptive budget policies can save passages while adding their own probe/control overhead.

The useful target is therefore a **minimal sufficient retrieval API with explicit resource semantics**: expressive enough to preserve structure and evidence needs, small enough for reliable control, and measurable in calls, tokens/passages, latency, and cost rather than one aggregate “retrieval budget.”

A chronology correction also matters: recent August papers sharpen this direction, but they did not originate it. A-RAG and especially LLM-Wiki already made the agent-facing retrieval-interface argument earlier in 2026.

## What would count as meaningful progress?

- operation-set ablations with the same controller and substrate;
- fixed/heuristic versus agentic control using identical retrieval primitives;
- adaptive-budget versus adaptive-budget comparisons, not only against static k;
- matched calls, context volume, latency, and controller overhead;
- transfer of the same interface across document/web/SQL/graph/code substrates;
- interpretable failures showing whether the missing capability was an operation, state variable, or resource allocation decision.
