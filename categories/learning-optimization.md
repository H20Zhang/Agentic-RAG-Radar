# Learning & Optimization

> **Core question:** Once retrieval is a sequential or resource-allocation action space, what should be learned—the controller, the retriever, both, or the whole trajectory objective?

This category covers policy learning, retriever learning for agentic usage, reinforcement learning, distillation, and optimization of retrieval/search trajectories or budgets.

## Current papers

### [Agentic-R](../papers/2601.11888.md) — ★★★★☆

**Design point:** train the retriever for downstream trajectory utility rather than only static query–passage similarity; let retriever behavior co-evolve with agent-generated queries.

**Core mismatch exposed:** a locally relevant passage can still be a poor action in a long search trajectory.

### [Graph-R1](../papers/2507.21892.md) — ★★★★☆

**Design point:** turn graph retrieval into a multi-turn interactive policy and optimize the retrieval/reasoning trajectory with reinforcement learning.

**Core mismatch exposed:** static graph context construction leaves the actual retrieval trajectory outside the learned policy.

### [SAGE](../papers/2608.08237.md) — ★★★☆☆

**Design point:** learn a lightweight retrieval-side policy that chooses per-query passage budget `k` from offline latency–quality oracle sweeps under an explicit SLO.

**Why it broadens the category:** not every learned retrieval policy needs to be a long reasoning trajectory. Resource allocation itself can be learned and independently deployable from the LLM.

**Evidence caveat:** the main baseline family is static-k. Adaptive-k and Stop-RAG are discussed as related work but not directly compared, so the result establishes value over fixed budgets more strongly than novelty over adaptive controllers.

## Current tension

Learning is only meaningful after the **environment, action space, and resource objective** are specified. If papers simultaneously change representation, retrieval operations, reward, policy, model, and budget, it becomes difficult to know what learned behavior is actually responsible for the gain.

Two credit-assignment problems now coexist:

- **trajectory credit:** which intermediate retrieval action helped or hurt the final answer?
- **resource credit:** did a learned controller improve decisions, or did it merely discover a better average compute allocation than a weak static baseline?

SAGE makes the second issue explicit. Its production framing is useful, but the next bar is adaptive-vs-adaptive evaluation under the same substrate and SLO.

## What would count as meaningful progress?

- trajectory-level reward or supervision with convincing intermediate-action attribution;
- learned budget policies compared with strong calibrated/adaptive controllers, not only static k;
- transfer across base agents, retrievers, workloads, and workload drift;
- learned policy compared with strong prompted/fixed controllers on the same interface;
- stability and sample-efficiency analysis, not only final QA accuracy;
- joint retriever/controller optimization that separates where each component contributes.
