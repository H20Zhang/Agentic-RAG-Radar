# Contributing

Agentic RAG Radar is a curated research map, not an exhaustive RAG paper feed. Contributions are most useful when they improve the **research conclusion** rather than only expand coverage.

## What belongs in the radar

A paper is in scope when both are true:

1. **External information acquisition is substantive** — retrieval, search, browsing, tool-mediated context access, or another external evidence source materially affects the task.
2. **Retrieval is meaningfully controlled** — an agent, controller, or learned policy changes whether, what, where, how, or how many times information is acquired.

Typical in-scope questions include adaptive/active retrieval, retrieval planning, iterative or interleaved search, query reformulation/decomposition, verifier-guided retrieval, agent-facing retrieval interfaces, retrieval policy learning, GraphRAG agents, and resource-aware stopping/budget allocation.

Usually out of scope:

- fixed `retrieve top-k → generate` pipelines with no meaningful retrieval control;
- generic agents where retrieval is incidental to the contribution;
- pure retriever/reranker/index improvements unless adaptive information-access control is itself part of the research claim;
- promotional submissions whose central evidence cannot be checked.

## Suggest a paper

Use the **Suggest an Agentic RAG paper** issue form. The most useful suggestions identify:

- the smallest research delta that makes the paper important;
- the closest baseline or historical/design predecessor;
- what the agent actually controls;
- negative results, unmatched resource budgets, or other causal confounders.

A paper does not need a positive headline result to be valuable. Strong negative results and careful analyses are especially welcome when they change how the field should interpret prior work.

## Suggest a correction

Open an issue when you find a correction that could change a reader's conclusion, including:

- wrong taxonomy or importance framing;
- broken/canonical links or duplicate paper versions;
- incorrect benchmark numbers or unsupported method descriptions;
- a missing stronger baseline or historical predecessor;
- unmatched retrieval calls, context tokens, latency, compute, or base-model changes;
- a visual that implies a mechanism or causal edge the evidence does not establish.

Please link the primary source when possible and distinguish verified facts from your interpretation.

## Evidence standard

The radar tries to keep **relevance separate from importance** and asks three questions for every strong claim:

1. **What actually changed?**
2. **Compared with what?**
3. **Does the evidence isolate the claimed cause?**

We prefer matched comparisons and full-text evidence where available. If a result may instead come from a better retrieval primitive, richer interface/state, larger realized budget, stronger base model, easier training distribution, or another confound, that alternative explanation should be preserved rather than edited away.

Thanks for helping keep the map skeptical, useful, and research-first.
