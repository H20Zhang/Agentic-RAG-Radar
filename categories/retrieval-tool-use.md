# Retrieval & Tool Use

> **Core question:** What information-access operations should an agent control, what evidence resolution should they expose, and where should retrieval draw the scalable boundary?

This category covers the **agent-facing retrieval environment**: operation set, corpus boundary, local evidence resolution, source structure, and resource semantics. The central 2026 correction is that “retriever versus agent” is the wrong binary. A better decomposition is **global candidate discovery × admissibility × local interaction × evidence delivery × execution guidance**.

## Current papers

### [Direct Corpus Interaction](../papers/2605.05242.md) — ★★★★★

**Design point:** bypass the fixed similarity API and let the agent compose grep/find/read/shell operations over raw corpus files.

**Why it is an anchor:** introduces **retrieval-interface resolution** as the explanation for why capable agents can outperform a stronger ranker even when the ranker already surfaced gold documents.

**Boundary:** raw full-corpus interaction degrades sharply with distractor scale; high resolution is not free.

### [RISE](../papers/2606.06880.md) — ★★★★☆

**Design point:** retrieval constructs a persistent bounded **interaction space** outside the prompt; shell operations happen inside that space. Full RISE adds navigational document structure.

**Key evidence:** matches raw DCI at 78% on a 100-query BrowseComp-Plus setup with gpt-5.4-mini at roughly one quarter of per-query cost. The 1M scaling result supports the boundary idea but is not fully model-matched.

### [DR-DCI](../papers/2606.14885.md) — ★★★★☆

**Design point:** turn retrieval into an agent-callable `pull(query,k)` action that dynamically expands persistent workspace state.

**Key evidence:** on the full 830-query BrowseComp-Plus evaluation, 71.20% versus 62.90% for Raw-DCI while using fewer tools and sharply less wall time/cost under the shared DCI harness.

### [RARG](../papers/2607.24223.md) — ★★★★☆

**Design point:** carry relevance **inside** interaction as an execution prior: document order, entry points, and local grep-match visibility are prioritized instead of treating every file/match equally.

**Useful negative:** a faster generative reranking variant uses fewer tools but loses accuracy, so “fewer interactions” is not itself a better policy.

### [SIEVE](../papers/2608.02751.md) — ★★★★☆

**Design point:** separate **candidate admissibility, ranking, inspection, and reading granularity**. Fielded Boolean constraints define which sources may be considered, ranking orders that set, result cards expose headings/snippets, and fetch reads a selected section.

**Key evidence:** the matched Search–Fetch control keeps the same ranker, result depth, and section-level reading while removing BQL selection; this makes the candidate-selection claim more identifiable than a full-stack comparison.

**Boundary:** zero-result fallback is frequent, so exact constraints are useful only together with recovery from over-constrained search.

### [LLM-Wiki](../papers/2605.25480.md) — ★★★★☆

**Design point:** compile documents into a persistent linked Wiki and expose search/read/link traversal as an agent-native environment. Keeping the structure while disabling progressive traversal produces a large reported drop, directly separating substrate from runtime navigation.

### [Beyond Top-K / READ](../papers/2608.06305.md) — ★★★★☆

**Design point:** lexical search, structural navigation, and bounded reads replace one opaque dense top-k call.

**Skeptical result:** BM25 is statistically indistinguishable from READ in the reported setting, so the primitive/interface claim is stronger than a generic agentic-policy claim.

### [Know Before You Fetch](../papers/2606.29959.md) — ★★★★☆

**Design point:** make retrieval amount explicit and distinguish calls, context volume, latency, and abstention rather than collapsing them into one “budget.”

## Current tension

The field has moved through a useful dialectic:

`fixed top-k → raw high-resolution interaction → bounded/persistent workspace → relevance-guided interaction`

SIEVE adds an orthogonal decomposition: even after the corpus boundary is chosen, the interface can still separate **which sources are admissible, how they are ranked, what structure is visible before reading, and what content is fetched**.

The lesson is not that relevance or indexes should disappear. DCI shows that a ranked-list interface can be too low-resolution; RISE and DR-DCI show that unrestricted interaction loses scale; RARG shows that relevance is valuable again when it **guides execution without becoming the final evidence bottleneck**; SIEVE shows that source structure can remain actionable without exposing raw files.

This changes how later document-navigation work should be read. A-RAG, LLM-Wiki, READ, SIEVE, and DocNavRAG are part of a broader question about the agent's information environment, not isolated GraphRAG/RAG workflow inventions.

## What would count as meaningful progress?

The decisive comparison is now **same model + same harness + same corpus + matched realized resources** while independently varying:

`corpus boundary × candidate admissibility × ranker × inspection surface × read granularity × local operation set × state persistence`.

Without that factorial design, a gain can still be caused by a better ranker, richer operations, more informative result cards, a larger workspace, or a different harness. SIEVE is useful precisely because its Search–Fetch control starts to separate some of those variables.
