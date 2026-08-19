# Retrieval & Tool Use

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** What information-access operations should an agent control, what evidence resolution should they expose, and **what should be materialized before the query versus localized after it?**

This category covers the agent-facing retrieval environment: corpus observability, operation set, corpus boundary, evidence granularity, source structure/state, and resource semantics. The central 2026 correction is that neither “retriever versus agent” nor “one search versus many” is a sufficient design axis.

## Current papers

### [A-RAG](../papers/2602.03442.md) — ★★★★☆

**Design point:** expose keyword search, semantic search, and chunk reads as a model-controlled retrieval-operation hierarchy rather than a fixed pipeline.

### [DocNavRAG](../papers/2608.01565.md) — ★★★★☆

**Design point:** couple document-native navigation with explicit collected/missing evidence state so structure and retrieval control evolve together.


### [Direct Corpus Interaction](../papers/2605.05242.md) — ★★★★★

**Design point:** bypass a fixed similarity API and let the agent compose grep/find/read/shell operations over raw corpus files.

**Why it is an anchor:** makes retrieval-interface resolution explicit. **Boundary:** raw full-corpus interaction degrades with distractor scale.

### [SIRA](../papers/2605.06647.md) — ★★★★☆

**Design point:** move adaptivity before evidence retrieval: predict discriminative evidence vocabulary, validate it with corpus statistics, and compile a lexical retrieval action.

**Boundary:** the setup pays offline LLM corpus-enrichment cost, and the advantage is not universal across backbone/budget.

### [Pi-Serini](../papers/2605.10848.md) — ★★★★☆

**Design point:** separate lexical backend quality, surfaced ranking depth, and agent browse/read inspection. Backend recall and inspected evidence are different bottlenecks.

### [RISE](../papers/2606.06880.md) — ★★★★☆

**Design point:** retrieval constructs a persistent bounded interaction space outside the prompt; shell operations happen inside that space.

### [DR-DCI](../papers/2606.14885.md) — ★★★★☆

**Design point:** retrieval becomes an agent-callable `pull(query,k)` action that dynamically expands persistent workspace state.

### [RARG](../papers/2607.24223.md) — ★★★★☆

**Design point:** carry relevance inside interaction as an execution prior. A faster generative reranking variant uses fewer tools but loses accuracy, so fewer interactions is not automatically better.

### [ReFind](../papers/2608.12888.md) — ★★★★☆

**Design point:** preserve raw chat history and move intelligence into a question-time lexical/session/time/local-context interface.

**Why it matters:** generic multi-round BM25 is weaker than the full interface, while one-search control is also weaker on LongMemEval-M; both interface quality and result-conditioned iteration matter. EventQA slightly favors single-shot BM25.

### [LENS](../papers/2608.16185.md) — ★★★★☆

**Design point:** move **evidence materialization** to query time over dynamic raw documents. Candidate evidence windows remain latent until the question arrives; a budgeted loop proposes regions, inspects relevance, updates beliefs, and narrows.

**Why it matters:** LENS improves evidence localization/grounding and freshness, not answer EM: ReAct is higher on D500 EM and essentially tied on fullwiki. The trade is lifecycle freshness/evidence fidelity versus extra online compute.

### [SIEVE](../papers/2608.02751.md) — ★★★★☆

**Design point:** separate candidate admissibility, ranking, inspection, and reading granularity; its Search–Fetch control removes Boolean candidate selection while holding the rest closer to fixed.

### [LLM-Wiki](../papers/2605.25480.md) — ★★★★☆

**Design point:** compile documents into a persistent linked Wiki and expose search/read/link traversal as an agent-native environment.

### [Beyond Top-K / READ](../papers/2608.06305.md) — ★★★★☆

**Design point:** lexical search, structural navigation, and bounded reads replace one opaque dense top-k call.

**Skeptical result:** BM25 is statistically indistinguishable from READ in the reported setting, so the primitive/interface claim is stronger than a generic agent-policy claim.

### [Know Before You Fetch](../papers/2606.29959.md) — ★★★★☆

**Design point:** make retrieval amount explicit and distinguish calls, context volume, latency, and abstention rather than collapsing them into one “budget.”

## Current tension: compile, materialize, or defer?

Two orthogonal placement decisions now matter.

**Where does adaptivity live?** SIRA shows some exploratory behavior can be compiled before retrieval when discriminative corpus signals are already observable. ReFind shows the opposite regime: when useful names/times/session context emerge only after retrieval, result-conditioned reformulation adds value.

**When does evidence become a retrieval unit?** Indexed RAG materializes chunks/vectors before the query. DCI preserves raw files but uses explicit operations over them. LENS goes further by treating evidence windows as query-conditioned latent objects that are localized online.

So `number of rounds` remains an outcome, not a primitive. A more stable decomposition is:

`pre-retrieval corpus observability × evidence-materialization time × action expressivity × result-conditioned information gain × state persistence × lifecycle cost`.

## What would count as meaningful progress?

The decisive experiment is the same changing corpus + same model + same answer budget while independently varying:

`offline index/materialization → compiled one-shot action → direct raw interaction → latent query-time localization → result-conditioned iteration`.

Cost must include construction/update, controller/oracle compute, retrieval calls, inspected tokens, latency, and freshness lag. Without that accounting, “index-free” can simply mean **offline work moved online**.
