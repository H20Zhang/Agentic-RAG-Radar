# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system genuinely makes better information-acquisition decisions rather than using a richer interface, different harness, looser resource budget, stronger model, easier benchmark—or rediscovered prior art?

This category covers benchmarks, surveys/SoKs, diagnostic studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [VAKRA](../papers/2608.12282.md) — ★★★★☆

**Design point:** executable cross-source trajectories combining APIs, document retrieval, multi-hop reasoning, and policy constraints under a fixed ReAct harness.

**Why it matters:** capability composition fails around entity disambiguation and cross-source grounding even when individual API/document tasks look much easier.

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

The earlier lens was:

`substrate × operation set × state × policy × realized resources × base model × historical baseline`

The DCI/harness backfill adds a missing factor:

`substrate × corpus boundary/interface resolution × harness/delivery × state × policy × realized resources × base model × historical baseline`

That change is substantive. DCI/RISE/DR-DCI show that the corpus boundary and evidence operations can alter what the agent is capable of expressing; Is Grep All You Need? shows the same retrieval primitive can behave very differently depending on how the harness presents tool results. A system-level score cannot attribute gains to “retrieval” while those variables move together.

VAKRA adds the complementary composition test: after factorizing components, do they still maintain entity/provenance/policy coherence across heterogeneous sources in one executable trajectory?

## What would count as meaningful progress?

The next bar is a factorial executable benchmark that can replay the same task under controlled **interface × harness × controller** substitutions, while logging realized calls/tokens/latency and allowing counterfactual repair of one intermediate decision. That would separate a better retriever from a higher-resolution interface, a better evidence-delivery path, a better policy, and a cross-source grounding failure instead of treating all four as “agent quality.”
