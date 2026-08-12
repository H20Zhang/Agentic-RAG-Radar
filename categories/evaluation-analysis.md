# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system is genuinely making better information-acquisition decisions rather than using better tools, more context, more compute, easier benchmarks—or rediscovering an older IR/QA control pattern under new terminology?

This category covers benchmarks, surveys/SoKs, diagnostic studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [Forgotten History or Test-of-Time?](../papers/2608.08445.md) — ★★★★☆

**Design point:** push the novelty baseline for Agentic RAG back to classical IR/QA, with QUALIFIER as a concrete retrieve→verify→reformulate precedent.

**Why it matters:** “iterative retrieval,” query refinement, verification, or stopping are not sufficient novelty claims by themselves. Modern work should isolate what LLM-era interfaces, learning, state, scale, or capability add.

**Caveat:** historical continuity does not establish technical equivalence, and the paper's explanation of QUALIFIER's competitive TREC result is retrospective rather than causally ablated.

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

**Potential value:** trajectory-level framing can make architecture comparison and failure analysis cleaner than a taxonomy based only on retriever/application labels.

**Current caveat:** taxonomy novelty and literature coverage still need comparison against prior surveys and older IR/QA systematizations.

## Evaluation lens used by this radar

For a system-level gain, separate when possible:

`substrate × operation set × state × policy × budget × base model × historical baseline`

At minimum, inspect retrieval calls and retrieved tokens, controller/probe overhead, latency/cost, lexical/sparse as well as dense baselines when appropriate, policy ablations using the same operation set, explicit state versus raw context/history, benchmark diversity, negative results/baseline reversals, and whether the claimed mechanism has meaningful pre-LLM antecedents.

The historical axis does **not** mean “nothing is new.” It asks a sharper question: is the novelty in the control-loop shape, or in how modern models represent state, choose actions, learn policies, operate at scale, and interact with richer information environments?

## What would count as meaningful progress?

- benchmarks that evaluate **trajectory quality**, not only final answer accuracy;
- matched-budget protocols for adaptive variable-length search;
- tests that isolate stopping, routing, evidence-state, tool-selection, and budget-allocation failures;
- modern re-implementations of strong classical IR/QA ideas as baselines where relevant;
- workloads beyond document QA: web research, SQL/data analysis, code, scientific retrieval, multimodal evidence;
- reproducible cost–quality frontiers rather than one unconstrained best score.

The goal is not more metrics. It is an evaluation design that makes causal and novelty claims about “agentic” control harder to fake.
