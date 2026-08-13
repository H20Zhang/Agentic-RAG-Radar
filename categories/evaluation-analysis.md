# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system is genuinely making better information-acquisition decisions rather than using better tools, looser budgets, more compute, easier benchmarks—or rediscovering an older IR/QA control pattern under new terminology?

This category covers benchmarks, surveys/SoKs, diagnostic studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [When Should Active RAG Retrieve?](../papers/2607.24010.md) — ★★★★☆

**Design point:** make the router's **operating point** auditable: separate utility ranking, calibrated threshold transfer, realized evidence usage, retrieval harm, and trigger-side cost.

**Why it matters:** two systems with the same nominal “50% retrieval budget” are not matched if their held-out usage differs. Even matched evidence use is not matched total cost when one controller needs a probe retrieval or no-retrieval generation before deciding.

**Caveat:** the main experiments are controlled routing diagnostics, not full open-domain multi-tool search.

### [Forgotten History or Test-of-Time?](../papers/2608.08445.md) — ★★★★☆

**Design point:** push the novelty baseline for Agentic RAG back to classical IR/QA, with QUALIFIER as a concrete retrieve→verify→reformulate precedent.

**Why it matters:** “iterative retrieval,” query refinement, verification, or stopping are not sufficient novelty claims by themselves. Modern work should isolate what LLM-era interfaces, learning, state, scale, or capability add.

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

## Evaluation lens used by this radar

For a system-level gain, separate when possible:

`substrate × operation set × state × policy × realized budget × base model × historical baseline`

The new emphasis on **realized** budget is deliberate. Report calls/tokens/context volume/latency separately, but also ask whether a learned threshold actually transfers to the held-out usage target and how often retrieval changes a correct no-retrieval answer into a wrong one.

A second hidden variable is the controller's pre-decision path. Query-only routing, uncertainty from a no-retrieval generation, and probe-retrieval scoring can share the same final evidence-use rate while paying meaningfully different costs.

The historical axis does **not** mean “nothing is new.” It asks whether novelty lies in the control-loop shape or in modern representation, learning, scale, tool interfaces, and richer information environments.

## What would count as meaningful progress?

The next bar is a trajectory benchmark that reports quality against **realized multi-resource frontiers**—retrieval calls, retrieved/context tokens, controller compute, wall-clock/latency—while labeling routing, stopping, evidence-state, and tool-selection failures. Strong historical and simple uncertainty/lexical baselines should remain in the comparison when they attack the same information-acquisition decision.
