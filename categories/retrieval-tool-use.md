# Retrieval & Tool Use

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** What information-access operations should an agent control, what evidence resolution should they expose, and **what should be materialized before the query versus localized after it?**

This category covers the agent-facing retrieval environment: corpus observability, operation set, corpus boundary, evidence granularity, source structure/state, and resource semantics. The central 2026 correction is that neither “retriever versus agent” nor “one search versus many” is a sufficient design axis.

## Current papers

### [PACE](../papers/2608.25115.md) — ★★★★☆

**Design point:** reorder a fixed candidate pool for evidence density, then adapt reranking depth from live reranker-versus-LLM serving pressure. **Boundary:** it controls ranking compute inside an already retrieved pool; HotpotQA/2Wiki exclude initial top-100 retrieval failures and the online headline is evidence recall plus serving latency, not matched answer accuracy.

### [Retrieve, Match, Escalate](../papers/2608.25037.md) — ★★★★☆

**Design point:** route only the ambiguous product-linking tail to a multimodal VLM that can acquire external Web evidence. **Boundary:** the production +9pp coverage result uses a previous-generation cheap linker, and there is no same-VLM no-search control isolating Web acquisition.

### [Crase](../papers/2608.24809.md) — ★★★★★

**Design point:** after fixed seed searches, move exploration extent and stopping into a 1.5-hop citation substrate rather than a model-terminated search loop. **Boundary:** the strong recall/cost comparison changes output contract, corpus substrate, and models, so boundedness is not isolated.

### [Risk-Aware Reranking](../papers/2608.22751.md) — ★★★★☆

**Design point:** treat the pre-execution shortlist as a risk surface by trading relevance against labeled tool risk. **Boundary:** exposure is not execution safety, labels and evaluation are coupled, and strict filtering removes some genuinely needed risky tools.

### [EARM](../papers/2608.22767.md) — ★★★☆☆

**Design point:** retain judged retrieval episodes as reusable reranking state. **Boundary:** the evidence is one fixed LoCoMo store/query order with incomplete lifecycle cost accounting.

### [Scroll](../papers/2608.21690.md) — ★★★★☆

**Design point:** retain lossless history in an event log and persistent Python namespace, then materialize selected state at query time.

**Boundary:** the closest CodeAct increment is small and lifecycle resources are not matched.

### [CTIFoundry](../papers/2608.18613.md) — ★★★★☆

**Design point:** materialize documents as entities, relations, chunks, and resolvable identifiers, then expose `resolve / traverse / collect / read` operations to the same stock agent.

**Boundary:** the full treatment bundles the scaffold, seven typed tools, output descriptions, prompt placement, and task skills; only offline build cost is reported comprehensively.

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

## Current tension: compile, materialize, defer, or escalate?

The new results expose three orthogonal placement decisions.

**Where does adaptivity live?** SIRA compiles some exploratory behavior before retrieval when discriminative corpus signals are observable. ReFind uses result-conditioned reformulation when names/times/session context emerge only after retrieval. PACE adds a different input altogether: serving pressure can adapt how much ranking compute to spend even when the evidence pool is fixed.

**When does evidence become a retrieval unit?** Indexed RAG materializes chunks/vectors before the query. DCI preserves raw files but uses explicit operations over them. LENS treats evidence windows as query-conditioned latent objects localized online.

**Which queries deserve a more expensive evidence environment?** Retrieve, Match, Escalate routes only uncertain product-linking cases into image inspection + Web search. That suggests a production decomposition distinct from “search more rounds”: cheap substrate first, then confidence-gated escalation to a richer substrate.

So `number of rounds` remains an outcome, not a primitive. A more stable decomposition is:

`pre-retrieval corpus observability × evidence-materialization time × action expressivity × result-conditioned information gain × state persistence × escalation policy × lifecycle cost`.

## What would count as meaningful progress?

The decisive experiment is the same changing corpus + same model + same output contract while independently varying:

`offline index/materialization → compiled one-shot action → direct raw interaction → latent query-time localization → result-conditioned iteration → confidence-gated richer substrate`.

For serving-aware systems, also cross evidence ordering with compute-budget control rather than crediting one package. Cost must include construction/update, candidate-pool generation, router/controller/oracle compute, retrieval/search calls, inspected tokens, reranked pairs, latency, storage, cache residency, and freshness lag. Without that accounting, “adaptive” can simply mean **work moved to a different stage or paid only by a hidden hard tail**.
