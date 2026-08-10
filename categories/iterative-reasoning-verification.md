# Iterative Reasoning & Verification

> **Core question:** How should new evidence change the next retrieval, reasoning, verification, and stopping decision?

This category is about the **closed loop after retrieval begins**. It includes on-demand search, evidence checking, context-gap detection, adaptive stopping, and context construction driven by intermediate observations.

## Current papers

### [ACE-GraphRAG](../papers/2608.01269.md) — ★★★★☆

**Design point:** make context assembly over a hierarchical graph an adaptive policy that can choose complementary depth- and breadth-oriented retrieval branches.

**Key separation:** rich representation is not the same as a good inference-time context policy.

### [Search-o1](../papers/2501.05366.md) — ★★★★☆

**Design point:** trigger search at knowledge gaps inside a reasoning trajectory, then reason over retrieved documents before reinjecting distilled evidence into the main chain.

**Why it is an anchor:** it makes external search a reasoning-time action rather than a preprocessing step.

## Current tension

Iterative retrieval is easy to claim and hard to evaluate. More iterations can mean better decisions—or simply **more opportunities, more tokens, and more latency**. A credible result should separate adaptive control from extra budget.

A second issue is **state representation**. Raw conversation/reasoning history may be a poor control state. Explicit evidence sufficiency, uncertainty, provenance, or missing-information state may make the loop more inspectable and transferable.

## What would count as meaningful progress?

- adaptive versus fixed stopping under matched retrieval/token budgets;
- explicit evidence/progress state versus raw history alone;
- verifier decisions tied to measurable error reduction rather than extra sampling;
- robust loop behavior when retrieved evidence conflicts or is adversarial;
- transfer of the control policy across different retrieval substrates.