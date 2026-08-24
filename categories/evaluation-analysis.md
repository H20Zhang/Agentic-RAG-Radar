# Evaluation & Analysis

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** How do we tell whether an Agentic RAG system genuinely makes better information-acquisition decisions rather than benefiting from easier evidence, a richer interface, retained state, a different harness, looser resource budget, stronger model, or rediscovered prior art?

This category covers benchmarks, controlled studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [StateMem / StateMemBench](../papers/2608.19652.md) — ★★★★☆

**Design point:** separate historical recall from operative-state assembly; a matched full-transcript wrapper control isolates value-chain structure and precedence from added context and call count.

**Boundary:** the synthetic benchmark targets the method's own lazy-reader failure family, persistent ingestion costs hundreds of LLM calls, dependency propagation can hurt, and external LongMemEval structure gains are small/mixed.

### [VisDocAgentBench](../papers/2608.17889.md) — ★★★☆☆

**Design point:** hold the top-10 opaque page-output contract fixed while separating direct, bridge, and path acquisition and ablating iterative search versus page inspection.

**Boundary:** agent history/input tokens and retrieval backend strength are not matched across the strongest comparisons; only six targets are cross-document.

### [ToolScout](../papers/2608.16502.md) — ★★★☆☆

**Design point:** audit candidate capability coverage before agent planning and diagnose cross-source transfer with matched-source, mixed-source, and routed retrieval.

**Boundary:** the study stops at retrieval coverage and a generation proxy; it does not execute tools to measure end-task success.

### [Retrieval, Reward, and Training Protocols](../papers/2605.27881.md) — ★★★★☆

**Design point:** treat the retrieval/training environment itself as part of the algorithmic claim. Corpus coverage, tool format, reward, rollout freshness, and search budget are varied under a common setup.

### [What Does Context Compression Cost an Agent?](../papers/2608.16370.md) — ★★★★☆

**Design point:** separate **state retention from retrieval effort**. Under fixed horizon, dropping queryable execution state can sharply increase reacquisition calls while completion remains statistically unchanged; oracle restoration removes most of the added retrieval.

**Boundary:** ALFWorld shows no retrieval surge under the same sliding compression, so the effect depends on environment recoverability.

### [VAKRA](../papers/2608.12282.md) — ★★★★☆

**Design point:** executable cross-source trajectories combining APIs, documents, multi-hop reasoning, and policy constraints under a fixed ReAct harness.

### [SGR-Bench](../papers/2605.22219.md) — ★★★★☆

**Design point:** make site-specific retrieval state measurable: filters, views, hierarchies, scopes, and time windows determine whether answer-bearing evidence becomes visible.

### [Pi-Serini](../papers/2605.10848.md) — ★★★★☆

**Design point:** separate retriever family from backend configuration, surfaced ranking depth, and agent inspection interface.

### [Is Grep All You Need?](../papers/2605.15184.md) — ★★★★☆

**Design point:** factor retrieval mode from agent harness/evidence delivery; the same retrieval can behave differently under different tool-output paths.

### [When Should Active RAG Retrieve?](../papers/2607.24010.md) — ★★★★☆

**Design point:** make the router's realized operating point auditable: utility ranking, threshold transfer, retrieval harm, and trigger-side cost.

### [Forgotten History or Test-of-Time?](../papers/2608.08445.md) — ★★★★☆

**Design point:** push the novelty baseline back to classical IR/QA retrieve→verify→reformulate loops.

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

## Evaluation lens used by this radar

The current lens is:

`substrate/evidence coverage × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state/retention × policy × realized resources × base model × training distribution/protocol × historical baseline`

The point is to locate the **first stage at which causal attribution already breaks**.

**Evidence availability comes before retrieval quality.** Training Protocols shows positive final-answer reward can exist when answer-bearing evidence is absent.

**Backend exposure is not agent inspection.** Pi-Serini shows that parameterization, surfaced depth, and browsing operations change what “BM25” means experimentally.

**Right source is not right source state.** SGR-Bench shows filters/scopes/views can hide evidence after source discovery.

**Less context is not necessarily less work.** The compression study shows dropped queryable state can be bought back through retrieval while completion stays unchanged. A context-token metric can therefore hide a tool-interaction tax.

**Same evidence is not the same experiment if the harness/source composition changes.** Is Grep All You Need? and VAKRA expose delivery and cross-source trajectory confounders.

## What would count as meaningful progress?

The next bar is a factorial executable benchmark with known evidence availability that can replay the same task under controlled:

`backend × interface × environment-state × retained-state × harness × controller`

substitutions while logging **offline construction/update + controller + retrieval + context + latency** cost and allowing one intermediate decision/state to be counterfactually repaired.

That would distinguish whether the environment contained the evidence, the backend exposed it, the agent could inspect it, the right source state was active, context preserved it, and the controller chose the right action.
