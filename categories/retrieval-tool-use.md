# Retrieval & Tool Use

> **Core question:** What information-access operations should an agent control, what evidence resolution should they expose, and where should retrieval draw the scalable boundary?

This category covers the **agent-facing retrieval environment**: operation set, corpus boundary, local evidence resolution, source structure, environment retrieval state, and resource semantics. The central 2026 correction is that “retriever versus agent” is the wrong binary. A better decomposition is **global candidate discovery × admissibility × environment state × local interaction × evidence delivery × execution guidance**.

## Current papers

### [Direct Corpus Interaction](../papers/2605.05242.md) — ★★★★★

**Design point:** bypass the fixed similarity API and let the agent compose grep/find/read/shell operations over raw corpus files.

**Why it is an anchor:** introduces **retrieval-interface resolution** as the explanation for why capable agents can outperform a stronger ranker even when the ranker already surfaced gold documents.

**Boundary:** raw full-corpus interaction degrades sharply with distractor scale; high resolution is not free.

### [Pi-Serini](../papers/2605.10848.md) — ★★★★☆

**Design point:** keep a conventional lexical backend, but tune it for the corpus, surface a much deeper cached ranking, and expose browse/read operations so the agent can inspect that ranking incrementally.

**Why it matters:** it is a useful counterweight to “richer interaction always beats retrieval.” On BrowseComp-Plus, well-configured BM25 plus a better inspection interface is already very strong. The negative detail is equally important: surfaced recall keeps rising with depth while previewed recall saturates, so backend recall and browsing policy remain separate bottlenecks.

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

Pi-Serini adds an important correction to the first step: **a conventional retriever can look weak simply because its parameters, surfaced depth, or inspection interface are weak**. DCI therefore should not be read as “indexes are obsolete”; it shows that some fixed retrieval interfaces are too lossy. Pi-Serini shows that increasing backend recall and preserving deeper ranking access can recover much of the gap on at least one deep-research corpus.

SIEVE adds an orthogonal decomposition: even after the corpus boundary is chosen, the interface can still separate **which sources are admissible, how they are ranked, what structure is visible before reading, and what content is fetched**.

The stable question is therefore not lexical versus dense or retriever versus shell. It is **where relevance constrains the search space, how much candidate information survives that boundary, and what operations the agent retains for inspecting and refining evidence**.

## What would count as meaningful progress?

The decisive comparison is **same model + same harness + same corpus + matched realized resources** while independently varying:

`backend/ranker configuration × surfaced depth × corpus boundary × candidate admissibility × inspection surface × read granularity × local operation set × state persistence`.

Without that factorial design, a gain can still be caused by a better-tuned backend, richer operations, deeper cached rankings, more informative result cards, a larger workspace, or a different harness. Pi-Serini and SIEVE are useful precisely because each begins to separate some of those variables rather than comparing only complete stacks.
