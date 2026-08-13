# Learning & Optimization

> **Core question:** Once retrieval is a sequential or resource-allocation action space, what should be learned—the controller, the retriever, both, or the whole trajectory objective?

This category covers policy learning, retriever learning for agentic usage, reinforcement learning, distillation, and optimization of retrieval/search trajectories or budgets.

## Current papers

### [SPARKLE](../papers/2026.acl-long.1793.md) — ★★★★☆

**Design point:** learn a separate proxy policy for retrieval decision, query formulation, and knowledge integration while keeping the retriever and answer LLM outside the trained policy.

**Why it changes the evidence bar:** SPARKLE compares against adaptive/search-RL baselines rather than only static retrieval. Its matched-generator results are competitive but not uniformly dominant, which is exactly the kind of evidence needed to distinguish plug-and-play policy learning from a generic “RL wins” story.

### [Agentic-R](../papers/2601.11888.md) — ★★★★☆

**Design point:** train the retriever for downstream trajectory utility rather than only static query–passage similarity; let retriever behavior co-evolve with agent-generated queries.

**Core mismatch exposed:** a locally relevant passage can still be a poor action in a long search trajectory.

### [Graph-R1](../papers/2507.21892.md) — ★★★★☆

**Design point:** turn graph retrieval into a multi-turn interactive policy and optimize the retrieval/reasoning trajectory with reinforcement learning.

### [SAGE](../papers/2608.08237.md) — ★★★☆☆

**Design point:** learn a lightweight retrieval-side policy that chooses per-query passage budget `k` from offline latency–quality oracle sweeps under an explicit SLO.

**Evidence caveat:** the main baseline family is static-k. SPARKLE makes that weakness more visible: by 2026, adaptive-vs-adaptive policy comparisons are a realistic bar, not an aspirational one.

## Current tension

Learning is only meaningful after the **environment, action space, policy boundary, and resource objective** are fixed. SPARKLE cleanly separates a learned proxy policy from the answer LLM; SAGE isolates budget selection; Agentic-R moves the learning target into the retriever; Graph-R1 learns the multi-turn graph trajectory.

The unresolved issue is therefore not “should retrieval be learned?” but **where the learned boundary should sit and what deserves credit**. A stronger model, richer action space, extra calls, or KG preprocessing can still dominate the apparent policy gain.

## What would count as meaningful progress?

The next decisive comparisons should keep the information interface and answer model fixed while comparing prompted, supervised, and RL controllers at matched calls/tokens/latency. Transfer across retrievers, base models, and workload drift should be treated as evidence about policy abstraction—not merely another aggregate QA score.
