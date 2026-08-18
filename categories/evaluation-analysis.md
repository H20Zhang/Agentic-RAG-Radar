# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system genuinely makes better information-acquisition decisions rather than benefiting from missing/easier evidence, a richer interface, different environment state, different harness, looser resource budget, stronger model, easier benchmark—or rediscovered prior art?

This category covers benchmarks, controlled studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [Retrieval, Reward, and Training Protocols](../papers/2605.27881.md) — ★★★★☆

**Design point:** treat the **retrieval/training environment itself** as part of the algorithmic claim. Corpus coverage, tool format, reward design, rollout freshness, and search budget are varied under a common search-agent setup.

**Why it matters:** the authors find thousands of training questions whose answer-bearing evidence is absent from the standard corpus while the model can still emit the correct final answer from parametric knowledge and receive positive reward. A reward can therefore certify a trajectory whose external evidence channel was impossible.

### [VAKRA](../papers/2608.12282.md) — ★★★★☆

**Design point:** executable cross-source trajectories combining APIs, document retrieval, multi-hop reasoning, and policy constraints under a fixed ReAct harness.

**Why it matters:** capability composition fails around entity disambiguation and cross-source grounding even when individual API/document tasks look much easier.

### [SGR-Bench](../papers/2605.22219.md) — ★★★★☆

**Design point:** make **site-specific retrieval state** measurable: the agent must establish filters, views, hierarchies, scopes, or time windows under which answer-bearing evidence becomes visible.

### [Pi-Serini](../papers/2605.10848.md) — ★★★★☆

**Design point:** separate retriever family from **backend configuration, surfaced ranking depth, and agent inspection interface**.

### [Is Grep All You Need?](../papers/2605.15184.md) — ★★★★☆

**Design point:** factor retrieval mode from **agent harness and evidence-delivery path**; the same retrieval can behave differently when tool output is delivered differently.

### [When Should Active RAG Retrieve?](../papers/2607.24010.md) — ★★★★☆

**Design point:** make the router's realized operating point auditable: separate utility ranking, threshold transfer, evidence use, retrieval harm, and trigger-side cost.

### [Forgotten History or Test-of-Time?](../papers/2608.08445.md) — ★★★★☆

**Design point:** push the novelty baseline back to classical IR/QA retrieve→verify→reformulate loops.

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

## Evaluation lens used by this radar

The current lens is:

`substrate/evidence coverage × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state × policy × realized resources × base model × training distribution/protocol × historical baseline`

The point is not to proliferate labels. It is to locate the **first stage at which the causal chain can already be broken**.

**Evidence availability comes before retrieval quality.** Training Protocols shows that if answer-bearing evidence is absent, final-answer reward can still look healthy because the model knows the answer parametrically. This invalidates the retrieval-learning signal before questions about policy quality even begin.

**Backend exposure is not agent inspection.** Pi-Serini shows that parameterization, surfaced depth, and inspection operations change what “BM25” means experimentally.

**Right source is not right source state.** SGR-Bench shows that filters/scopes/views can still hide the answer after source discovery.

**Same evidence is not same experiment if the harness changes.** Is Grep All You Need? makes delivery/tool semantics causal; VAKRA then asks whether identity/evidence/policy remain coherent across heterogeneous sources in one executable trajectory.

## What would count as meaningful progress?

The next bar is a factorial executable benchmark that starts with **known evidence availability** and can replay the same task under controlled `backend × interface × environment-state × harness × controller` substitutions while logging realized calls/tokens/latency and allowing one intermediate decision to be counterfactually repaired.

That would distinguish six questions current leaderboards collapse: **did the environment contain the evidence, did the backend expose it, could the agent inspect it, was the source in the right state, did the controller choose the right action, and did the harness preserve the evidence faithfully?**
