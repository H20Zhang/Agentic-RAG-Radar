# Iterative Reasoning & Verification

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** What progress/state should make the next retrieval, redirect, verification, recovery, or stopping decision?

This category is about the closed loop after retrieval begins. The important object is not “iteration” itself, but the state that tells the controller what has been established, what is missing, whether search is still producing new information, and whether the current branch should continue.

## Current papers

### [S2G-RAG](../papers/2604.23783.md) — ★★★★☆

**Design point:** predict whether current evidence is sufficient and, if not, represent missing information as structured gap items that become the next query.

**Why it changes the map:** a matched-budget ablation gives explicit sufficiency/gap state a strong baseline.

### [RAAC](../papers/2608.15191.md) — ★★★★☆

**Design point:** make **trajectory progress** explicit through criteria coverage, document novelty, query diversity, and query-to-question alignment, then choose `continue`, `intervene`, or `stop`.

**Why it matters:** seven same-agent overlays make stagnation measurable across DRA families. But search-call savings do not yet equal total-cost savings because the controller and critical re-thinker add LLM work, and several agent/dataset cells move the wrong way.

### [LoongReflect](../papers/2608.11967.md) — ★★★★☆

**Design point:** make active reasoning state reversible with explicit reflection/backtracking and recovery supervision.

**Boundary:** privileged global teacher information weakens attribution to rollback alone.

### [ACE-GraphRAG](../papers/2608.01269.md) — ★★★★☆

**Design point:** make context assembly over a hierarchical graph an adaptive policy choosing complementary depth/breadth retrieval branches.

### [Search-o1](../papers/2501.05366.md) — ★★★★☆

**Design point:** trigger search at knowledge gaps inside reasoning, reason over retrieved documents, and reinject distilled evidence into the main trajectory.

## Current tension

The useful comparison is now **what state is exposed to control**, not iterative versus one-shot.

S2G-RAG exposes `sufficient / missing evidence`. RAAC exposes `progress / novelty / drift`. LoongReflect exposes `trusted vs contaminated active branch` plus rollback. SGR-Bench remains the external-state boundary: the right internal controller cannot repair a source that is still filtered/configured to the wrong evidence.

This makes controller cost a first-class confound. RAAC can trade search calls for extra controller/re-thinker calls; LoongReflect can trade simpler history for privileged recovery supervision. A state abstraction is only meaningful if it improves decisions at matched total work.

## What would count as meaningful progress?

Hold the underlying DRA/retriever/history representation fixed and compare:

`implicit history → sufficiency/gap state → progress/stagnation signals → redirect-only control → rollback/recovery`

with matched controller + retrieval tokens/latency. A counterfactual replay benchmark should patch one mistaken state/action and measure whether the remaining trajectory causally recovers.
