# Retrieval & Tool Use

> **Core question:** What retrieval operations, corpora, tools, or databases should the agent be able to invoke—and what information should each operation expose back to the controller?

This category covers the **retrieval interface / action space**. The main design variable is not just the retriever model; it is what operations are exposed and how they can be composed.

## Current papers

### [Beyond Top-K / READ](../papers/2608.06305.md) — ★★★★☆

**Design point:** replace one opaque dense top-k call with lexical search, structural navigation, and bounded reads.

**Skeptical result:** BM25 is reported as statistically indistinguishable from READ, so the evidence favors an interface/lexical-access claim more strongly than a generic “agentic beats non-agentic” claim.

### [DocNavRAG](../papers/2608.01565.md) — ★★★★☆

**Design point:** make document-native hierarchy and cross-region relations navigable operations while carrying explicit collected/missing evidence state.

**Open attribution:** structure, state, and retrieval budget all need component-level separation.

### [A-RAG](../papers/2602.03442.md) — ★★★★☆

**Design point:** expose keyword search, semantic search, and chunk read as a hierarchy of model-controlled retrieval actions.

**Why it is an anchor:** it makes retrieval API design a first-class systems question rather than hard-coding another workflow.

## Current tension

**A richer action space can improve capability while making control harder.** The research problem is therefore not “more tools are better,” but finding a **minimal sufficient retrieval API**: expressive enough to preserve structure and evidence needs, small enough for reliable planning and matched-budget evaluation.

## What would count as meaningful progress?

- operation-set ablations with the same controller;
- fixed/heuristic versus agentic control using identical retrieval primitives;
- matched calls, tokens, latency, and context volume;
- transfer of the same interface across document/web/SQL/graph/code substrates;
- interpretable failure analysis showing *which missing operation* caused retrieval failure.