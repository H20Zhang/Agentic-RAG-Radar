# Learning & Optimization

> **Core question:** Once information acquisition is a sequential action space, what should be learned—the retriever, the search policy, the evidence-state controller, recovery behavior, or resource allocation?

This category covers policy learning, retriever learning for agentic usage, reinforcement learning, distillation, and optimization of search trajectories/state/budgets.

## Current papers

### [LoongReflect](../papers/2608.11967.md) — ★★★★☆

**Design point:** learn reversible memory control for long-horizon search: reflect on branch quality, roll back a contaminated suffix, preserve a corrective lesson, then resume.

**Main caveat:** state representation, rollback action space, and privileged trajectory supervision remain partly bundled.

### [GrepSeek](../papers/2605.29307.md) — ★★★★☆

**Design point:** learn the policy over a **direct-corpus shell interface** with verified cold-start trajectories plus GRPO; accelerate exact shell execution without changing command semantics.

**Important negative:** GrepSeek loses significantly on PopQA, showing that learned DCI does not remove lexical surface-form brittleness.

### [Critic-R](../papers/2606.00590.md) — ★★★★☆

**Design point:** turn the reasoning agent's dissatisfaction with evidence into both inference-time query repair and retriever supervision. Accepted/rejected refinement attempts become positives/hard negatives without gold-passage labels.

**Cost caveat:** the critic loop buys retrieval recovery with extra model/retrieval calls; answer accuracy and operating cost should be evaluated jointly.

### [SPARKLE](../papers/2026.acl-long.1793.md) — ★★★★☆

**Design point:** learn a separate proxy policy for retrieval decision, query formulation, and knowledge integration while keeping the answer LLM/retriever outside the trained policy.

### [Agentic-R](../papers/2601.11888.md) — ★★★★☆

**Design point:** train the retriever for trajectory-level downstream utility rather than static query–passage similarity, using evolving agent queries.

### [Graph-R1](../papers/2507.21892.md) — ★★★★☆

**Design point:** optimize multi-turn graph retrieval/reasoning trajectories with reinforcement learning.

### [SAGE](../papers/2608.08237.md) — ★★★☆☆

**Design point:** learn per-query passage budget `k` under an explicit latency SLO; useful control point, but static-k is still the main baseline family.

## Current tension

“Learn the retrieval policy” now hides several distinct objects:

`retriever objective ↔ query/refinement policy ↔ corpus-operation policy ↔ state recovery ↔ resource allocation`

Agentic-R changes retriever utility; Critic-R uses natural-language process feedback to repair and train retrieval; GrepSeek learns shell interaction itself; LoongReflect learns when to discard active state. These are not interchangeable contributions.

The causal bar is therefore **same environment + same state/action space + same answer model + matched realized resources**, varying only the learned component or supervision. Otherwise a richer interface, privileged teacher, extra refinement attempts, or more turns can masquerade as better learning.

## What would count as meaningful progress?

A strong experiment should compare prompted, supervised, and RL controllers on the same information environment while separately toggling retriever learning, query refinement, direct-corpus operations, and recovery semantics. It should report not only final QA but realized retrieval/tool calls, critic/controller compute, latency, and transfer under corpus/workload drift.
