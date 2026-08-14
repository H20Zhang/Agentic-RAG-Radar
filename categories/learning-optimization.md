# Learning & Optimization

> **Core question:** Once retrieval is a sequential action space, what should be learned—the retrieval policy, the evidence-state controller, the recovery policy, or the whole trajectory objective?

This category covers policy learning, retriever learning for agentic usage, reinforcement learning, distillation, and optimization of retrieval/search trajectories, state control, or budgets.

## Current papers

### [LoongReflect](../papers/2608.11967.md) — ★★★★☆

**Design point:** learn **reversible memory control** for long-horizon search. Reflection diagnoses verified evidence, missing evidence, and branch risk; backtracking removes a contaminated suffix from active context and preserves a corrective lesson before search resumes.

**Why it changes the evidence bar:** the paper compares against Search-R1 / AgenticRAG-R1-class adaptive and RL search baselines rather than only static RAG, and reports component ablations for reflection/backtracking and its fast/slow learning channels. The remaining confound is training supervision: the fast channel has privileged global trajectory information.

### [SPARKLE](../papers/2026.acl-long.1793.md) — ★★★★☆

**Design point:** learn a separate proxy policy for retrieval decision, query formulation, and knowledge integration while keeping the retriever and answer LLM outside the trained policy.

**Why it changes the evidence bar:** SPARKLE compares against adaptive/search-RL baselines rather than only static retrieval. Its matched-generator results are competitive but not uniformly dominant, which is exactly the kind of evidence needed to distinguish plug-and-play policy learning from a generic “RL wins” story.

### [Agentic-R](../papers/2601.11888.md) — ★★★★☆

**Design point:** train the retriever for downstream trajectory utility rather than only static query–passage similarity; let retriever behavior co-evolve with agent-generated queries.

### [Graph-R1](../papers/2507.21892.md) — ★★★★☆

**Design point:** turn graph retrieval into a multi-turn interactive policy and optimize the retrieval/reasoning trajectory with reinforcement learning.

### [SAGE](../papers/2608.08237.md) — ★★★☆☆

**Design point:** learn a lightweight retrieval-side policy that chooses per-query passage budget `k` from offline latency–quality oracle sweeps under an explicit SLO.

**Evidence caveat:** the main baseline family is static-k. SPARKLE and LoongReflect make that weakness more visible: by 2026, adaptive-vs-adaptive policy comparisons are a realistic bar.

## Current tension

The learned boundary is moving **above retrieval**. Agentic-R changes the retriever objective; SPARKLE learns retrieval decisions and query formulation; SAGE learns resource allocation; LoongReflect learns whether accumulated execution state should be retained or rolled back.

That makes “RL improves Agentic RAG” too coarse a claim. The causal question is **which state/action boundary was learned, under what privileged supervision, and what remained fixed**. A reversible trajectory representation can help even before learning; a privileged teacher can help even if rollback is not intrinsically better; extra search turns can still masquerade as better policy.

## What would count as meaningful progress?

The next decisive experiment should independently vary **state representation × recovery action space × supervision** while keeping retrieval environment, answer model, and realized tool budget fixed. For long-horizon recovery specifically, compare append-only reflection, reversible state with a prompted controller, and reversible state with learned control. That would tell us whether the gain comes from rollback semantics, policy learning, or privileged reflection labels.
