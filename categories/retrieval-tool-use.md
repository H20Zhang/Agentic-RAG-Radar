# Retrieval & Tool Use

> **Core question:** What information-access operations should an agent control, what evidence resolution should they expose, and **when should adaptivity happen before versus after evidence retrieval?**

This category covers the **agent-facing retrieval environment**: corpus observability, operation set, corpus boundary, local evidence resolution, source structure/state, and resource semantics. The central 2026 correction is that neither “retriever versus agent” nor “one search versus many” is a sufficient design axis.

## Current papers

### [Direct Corpus Interaction](../papers/2605.05242.md) — ★★★★★

**Design point:** bypass the fixed similarity API and let the agent compose grep/find/read/shell operations over raw corpus files.

**Why it is an anchor:** introduces **retrieval-interface resolution** as an explanation for why capable agents can outperform a stronger ranker even when the ranker already surfaced gold documents.

**Boundary:** raw full-corpus interaction degrades with distractor scale; high resolution is not free.

### [SIRA](../papers/2605.06647.md) — ★★★★☆

**Design point:** move adaptivity **before evidence retrieval**. An LLM predicts discriminative evidence vocabulary; document-frequency/index signals validate and weight it; the result is compiled into a lexical retrieval action rather than learned from repeated result snippets.

**Why it matters:** it is the strongest current counterexample to “more search rounds = more capable agent.” Across BEIR, the compiled retrieval program is competitive with learned dense/sparse and multi-round baselines. But the main method also pays substantial offline LLM document-enrichment cost, and its BrowseComp-Wikipedia advantage is not universal across backbone/budget: GPT-5.4 SIRA loses to GPT-5.4 Perplexity at Recall@100.

### [Pi-Serini](../papers/2605.10848.md) — ★★★★☆

**Design point:** keep a conventional lexical backend, tune it for the corpus, surface a deep cached ranking, and expose browse/read operations so the agent can inspect that ranking incrementally.

**Why it matters:** backend recall and agent-inspected evidence are separate bottlenecks. A lexical system can look weak because tuning, surfaced depth, or browsing affordances are weak.

### [RISE](../papers/2606.06880.md) — ★★★★☆

**Design point:** retrieval constructs a persistent bounded **interaction space** outside the prompt; shell operations happen inside that space.

### [DR-DCI](../papers/2606.14885.md) — ★★★★☆

**Design point:** turn retrieval into an agent-callable `pull(query,k)` action that dynamically expands persistent workspace state.

### [RARG](../papers/2607.24223.md) — ★★★★☆

**Design point:** carry relevance **inside** interaction as an execution prior: document order, entry points, and local grep-match visibility are prioritized instead of treating every file/match equally.

**Useful negative:** a faster generative reranking variant uses fewer tools but loses accuracy, so “fewer interactions” is not itself a better policy.

### [ReFind](../papers/2608.12888.md) — ★★★★☆

**Design point:** preserve raw chat history and move intelligence into a **question-time, substrate-native retrieval interface**: lexical reformulation, session-aware ranking, local turn expansion, time filtering, and seen-session state.

**Why it matters:** two matched controls separate the causal story. Generic multi-round BM25 is materially weaker than the full interface, so iteration alone is insufficient; forcing one search is also materially weaker on LongMemEval-M, so some useful query terms/scopes really do emerge only after inspecting evidence.

**Boundary:** EventQA slightly favors single-shot BM25-RAG, and the method shifts cost from memory construction to query time rather than eliminating it.

### [SIEVE](../papers/2608.02751.md) — ★★★★☆

**Design point:** separate **candidate admissibility, ranking, inspection, and reading granularity**. The matched Search–Fetch control keeps ranking/result depth/selective read while removing Boolean candidate selection.

### [LLM-Wiki](../papers/2605.25480.md) — ★★★★☆

**Design point:** compile documents into a persistent linked Wiki and expose search/read/link traversal as an agent-native environment.

### [Beyond Top-K / READ](../papers/2608.06305.md) — ★★★★☆

**Design point:** lexical search, structural navigation, and bounded reads replace one opaque dense top-k call.

**Skeptical result:** BM25 is statistically indistinguishable from READ in the reported setting, so the primitive/interface claim is stronger than a generic agentic-policy claim.

### [Know Before You Fetch](../papers/2606.29959.md) — ★★★★☆

**Design point:** make retrieval amount explicit and distinguish calls, context volume, latency, and abstention rather than collapsing them into one “budget.”

## Current tension: compile control or defer it?

The older interaction-space lineage remains useful:

`fixed top-k → raw high-resolution interaction → bounded/persistent workspace → relevance-guided interaction`

But **SIRA ↔ ReFind** adds a sharper orthogonal question: **where should adaptivity live?**

SIRA shows that some exploratory search can be compiled away when the controller can predict discriminative vocabulary and validate it against corpus-visible statistics *before* evidence is read. ReFind shows the opposite regime: when useful names, timestamps, or session-local context only become visible after retrieval, result-conditioned reformulation adds value. Its generic-agentic control also shows that simply looping over BM25 is not enough; the interface has to expose the right substrate structure.

So `number of rounds` is an outcome, not a primitive. The more stable decomposition is:

`pre-retrieval corpus observability × action expressivity × result-conditioned information gain × state persistence × realized cost`.

Pi-Serini and SIEVE then refine the middle of that path: what ranking depth survives, which candidates are admissible, what the agent sees before reading, and how much content it fetches.

## What would count as meaningful progress?

The decisive experiment is **same model + same backend/corpus + same harness + equal total compute** while independently varying:

`pre-retrieval corpus signals → compiled action → one-shot retrieval → result-conditioned iteration → inspection/read interface → persistent state`.

Cost must include both sides of the boundary. SIRA's offline corpus enrichment and ReFind's extra question-time LLM/search calls are different ways to spend computation. Without matching them, “one-shot” versus “agentic” remains another bundled systems comparison rather than a causal result.
