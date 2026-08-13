# Iterative Reasoning & Verification

> **Core question:** How should new evidence change the next retrieval, reasoning, verification, and stopping decision?

This category is about the **closed loop after retrieval begins**. The important object is increasingly not “iteration” itself, but the state that tells the controller what has been established, what is missing, and whether another information-acquisition action is justified.

## Current papers

### [S2G-RAG](../papers/2604.23783.md) — ★★★★☆

**Design point:** explicitly predict whether current evidence is sufficient and, if not, represent missing information as structured gap items that become the next query.

**Why it changes the map:** a matched-budget ablation isolates a strong contribution from the sufficiency/gap controller. It also shows that explicit missing-evidence state was already a concrete 2026 design point before the August DocNavRAG work.

### [ACE-GraphRAG](../papers/2608.01269.md) — ★★★★☆

**Design point:** make context assembly over a hierarchical graph an adaptive policy that can choose complementary depth- and breadth-oriented retrieval branches.

**Key separation:** rich representation is not the same as a good inference-time context policy.

### [Search-o1](../papers/2501.05366.md) — ★★★★☆

**Design point:** trigger search at knowledge gaps inside a reasoning trajectory, then reason over retrieved documents before reinjecting distilled evidence into the main chain.

**Why it is an anchor:** it makes external search a reasoning-time action rather than a preprocessing step.

## Current tension

The useful comparison is now **explicit state versus implicit history**, not “iterative versus one-shot.” S2G-RAG gives explicit sufficiency/missing-information state a stronger baseline; DocNavRAG later couples a related evidence state to a document-native navigation environment; ACE changes the context policy over a graph substrate.

That makes causal attribution harder but cleaner: representation, state, action space, stopping policy, and retrieval budget should be varied separately when possible.

## What would count as meaningful progress?

A decisive next result would compare explicit evidence/gap state against a strong raw-history controller while matching retrieval calls, retrieved tokens, and answer-model capacity. It should also stress conflicting evidence and transfer the same state abstraction across documents, web, SQL, code, or graphs.
