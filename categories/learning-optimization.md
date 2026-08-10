# Learning & Optimization

> **Core question:** Once retrieval is a sequential action space, what should be learned—the controller, the retriever, both, or the whole trajectory objective?

This category covers policy learning, retriever learning for agentic usage, reinforcement learning, distillation, and optimization of retrieval/search trajectories.

## Current papers

### [Agentic-R](../papers/2601.11888.md) — ★★★★☆

**Design point:** train the retriever for downstream trajectory utility rather than only static query–passage similarity; let retriever behavior co-evolve with agent-generated queries.

**Core mismatch exposed:** a locally relevant passage can still be a poor action in a long search trajectory.

### [Graph-R1](../papers/2507.21892.md) — ★★★★☆

**Design point:** turn graph retrieval into a multi-turn interactive policy and optimize the retrieval/reasoning trajectory with reinforcement learning.

**Core mismatch exposed:** static graph context construction leaves the actual retrieval trajectory outside the learned policy.

## Current tension

Learning is only meaningful after the **environment and action space** are specified. If papers simultaneously change representation, retrieval operations, reward, policy, and model, it becomes difficult to know what learned behavior is actually responsible for the gain.

Credit assignment is the second bottleneck: final-answer reward is easy to measure but weakly identifies which intermediate retrieval action was useful or harmful.

## What would count as meaningful progress?

- trajectory-level reward or supervision with convincing intermediate-action attribution;
- transfer across base agents, retrievers, or retrieval substrates;
- learned policy compared with strong prompted/fixed controllers on the same interface;
- stability and sample-efficiency analysis, not only final QA accuracy;
- joint retriever/controller optimization that separates where each component contributes.