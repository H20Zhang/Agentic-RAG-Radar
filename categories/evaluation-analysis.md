# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system is genuinely making better information-acquisition decisions rather than using better tools, more context, more compute, or an easier benchmark setup?

This category covers benchmarks, surveys/SoKs, diagnostic studies, failure analysis, and evaluation methodology for adaptive retrieval systems.

## Current design anchor

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

**Potential value:** trajectory-level framing could make architecture comparison and failure analysis cleaner than a taxonomy based only on retriever/application labels.

**Current caveat:** the radar has not yet audited taxonomy novelty or literature coverage against prior surveys.

## Evaluation lens used by this radar

For a system-level gain, try to separate:

`substrate × operation set × state × policy × budget × base model`

At minimum, inspect:

- retrieval calls and retrieved tokens;
- latency / cost when available;
- lexical/sparse as well as dense baselines when appropriate;
- policy ablations using the same operation set;
- explicit state versus raw context/history;
- benchmark diversity and contamination concerns;
- negative results and baseline reversals.

## What would count as meaningful progress?

- benchmarks that evaluate **trajectory quality**, not only final answer accuracy;
- matched-budget protocols for adaptive variable-length search;
- tests that isolate stopping, routing, evidence-state, and tool-selection failures;
- workloads beyond document QA: web research, SQL/data analysis, code, scientific retrieval, multimodal evidence;
- reproducible cost–quality frontiers rather than one unconstrained best score.

The goal is not more metrics. It is an evaluation design that makes causal claims about “agentic” control harder to fake.