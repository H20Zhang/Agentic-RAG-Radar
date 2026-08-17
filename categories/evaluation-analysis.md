# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system genuinely makes better information-acquisition decisions rather than using a richer interface, different environment state, different harness, looser resource budget, stronger model, easier benchmark—or rediscovered prior art?

This category covers benchmarks, surveys/SoKs, diagnostic studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [VAKRA](../papers/2608.12282.md) — ★★★★☆

**Design point:** executable cross-source trajectories combining APIs, document retrieval, multi-hop reasoning, and policy constraints under a fixed ReAct harness.

**Why it matters:** capability composition fails around entity disambiguation and cross-source grounding even when individual API/document tasks look much easier.

### [SGR-Bench](../papers/2605.22219.md) — ★★★★☆

**Design point:** make **site-specific retrieval state** measurable. The agent must not only find the right specialized source, but also establish and preserve filters, views, hierarchies, scopes, or time windows under which answer-bearing evidence becomes visible.

**Why it matters:** source discovery and internal evidence tracking are not enough if the external data system is in the wrong state. Retrieval-scope drift and criterion mismatch dominate the audited failure set.

### [Pi-Serini](../papers/2605.10848.md) — ★★★★☆

**Design point:** separate retriever family from **backend configuration, surfaced ranking depth, and agent inspection interface**.

**Why it matters:** default/shallow BM25 can be a misleading baseline. On BrowseComp-Plus, tuned BM25 plus deep cached rankings and browse/read tools materially changes the dense-versus-lexical conclusion; previewed recall still saturates much earlier than surfaced recall.

### [Is Grep All You Need?](../papers/2605.15184.md) — ★★★★☆

**Design point:** factor retrieval mode from **agent harness and evidence-delivery path**. On LongMemEval-S, grep-versus-vector conclusions can flip when inline tool output becomes programmatic file delivery, and the same model/retrieval mode moves substantially across harnesses.

**Why it matters:** “same model + different retriever” is not a clean retrieval comparison if prompt/tool/result rendering/stopping semantics also change.

### [When Should Active RAG Retrieve?](../papers/2607.24010.md) — ★★★★☆

**Design point:** make the router's realized operating point auditable: separate utility ranking, calibrated threshold transfer, evidence use, retrieval harm, and trigger-side cost.

### [Forgotten History or Test-of-Time?](../papers/2608.08445.md) — ★★★★☆

**Design point:** push the novelty baseline back to classical IR/QA retrieve→verify→reformulate loops.

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

## Evaluation lens used by this radar

The current lens is:

`substrate × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state × policy × realized resources × base model × training distribution × historical baseline`

Two distinctions matter.

First, **environment retrieval state is not agent memory**. SGR-Bench shows that an agent can carry the right reasoning/evidence history and still fail because the external site is configured to the wrong scope, filter, or view. Conversely, better internal state does not prove better environment-state control.

Second, **retriever family is not a sufficient experimental variable**. Pi-Serini shows that backend parameterization, how deep a ranking is surfaced, and what inspection operations the agent receives can reverse a naive lexical-versus-dense conclusion. These should normally be accounted for inside the interface/resource axes rather than promoted into an ever-growing list of independent buzzword factors.

The DCI lineage and harness studies add complementary confounders: corpus boundary and evidence operations alter what the agent can express; result delivery and tool contracts alter how the same evidence is consumed. VAKRA then asks whether those components remain coherent across heterogeneous sources in one executable trajectory.

## What would count as meaningful progress?

The next bar is a factorial executable benchmark that can replay the same task under controlled **backend × interface × environment-state × harness × controller** substitutions while logging realized calls/tokens/latency and allowing counterfactual repair of one intermediate decision.

That would let us distinguish five questions that current leaderboards often collapse: did the backend surface the evidence, could the agent inspect it, was the external source in the right state, did the controller choose the right action, and did the harness preserve the evidence faithfully?
