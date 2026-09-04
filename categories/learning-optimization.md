# Learning & Optimization

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** Once information acquisition is a sequential action space, what should be learned—the retriever, the search policy, the evidence-state controller, recovery behavior, resource allocation, or even the training-task distribution itself?

This category covers policy learning, retriever learning for agentic usage, reinforcement learning, distillation, optimization of search trajectories/state/budgets, and self-generated supervision for search agents.

## Current papers


### [CoBRA](../papers/2609.00967.md) — ★★★★☆

**Design point:** train selective retrieval from a same-query internal-versus-external utility margin, then inject that route-level margin through reference-split RL. **Boundary:** the discovery experts are separately fine-tuned and MARS ablations do not match realized tool calls, tokens, latency, or evidence volume.

### [ContextPilot](../papers/2608.28476.md) — ★★★★☆

**Design point:** learn proactive working-context edits across planning, retrieval, memory, and offloading, with context-sensitive partial rollouts and action-level credit. **Boundary:** the full result bundles the tool surface, SFT data, rollout policy, and credit assignment; complete lifecycle cost is unmatched.

### [ITER](../papers/2608.27912.md) — ★★★★☆

**Design point:** make retriever utility trajectory-relative by conditioning on prior searches and demoting already consumed relevant evidence. **Boundary:** supervision is success-conditioned, candidate exposure is de-duplicated during collection, and longer encoder-input cost is unreported.


### [AWM](../papers/2608.25618.md) — ★★★★☆

**Design point:** train the agent to preserve answer-supporting evidence in source-linked terminal working memory, with an EP-given control that separates memory extraction from page access. **Boundary:** the reward adds two frozen Qwen3-14B passes per rollout and measures answerability rather than claim-level source grounding.

### [CAFE](../papers/2608.24794.md) — ★★★★☆

**Design point:** learn when to request corrective feedback while a critic is updated from the policy's changing on-policy failures. **Boundary:** request shaping, token credit, critic RDPO, extra feedback work, and online/offline schedule remain coupled; the matched-step study shows schedule is itself consequential.

### [GTA-RAG](../papers/2608.22479.md) — ★★★★☆

**Design point:** supervise retriever-validated target-document chains before natural-QA reward. **Boundary:** graph construction, hybrid retrieval, synthetic targets, and training remain a package.

### [MCite-RL](../papers/2608.21808.md) — ★★★☆☆

**Design point:** add final visual-localization rewards to an iterative retrieve/crop/answer policy. **Boundary:** the process term uses only the terminal crop, and bbox overlap is not semantic support.

### [CAS](../papers/2608.20771.md) — ★★★☆☆

**Design point:** adapt evidence-set size from calibrated retrieval mass and weight rollout updates from answer NLL. **Boundary:** marginal set coverage and NLL control do not guarantee answer correctness.

### [LoongReflect](../papers/2608.11967.md) — ★★★★☆

**Design point:** learn reversible memory control for long-horizon search: reflect on branch quality, roll back a contaminated suffix, preserve a corrective lesson, then resume.

**Main caveat:** state representation, rollback action space, and privileged trajectory supervision remain partly bundled.

### [SearchMaster](../papers/2608.01822.md) — ★★★★☆

**Design point:** make the **self-play training distribution** a controlled object. Evidence-chain task generation reduces pseudo multi-hop questions; minimum successful search depth calibrates task difficulty; an over-opening penalty regulates tool-use drift.

**Key evidence:** a same-backbone naive-self-play baseline and component ablations separate a large generic self-play gain from additional ECG/SDR/OOP gains more cleanly than the heterogeneous external leaderboard.

**Cost caveat:** the approach removes human-written QA/expert demonstrations, not training infrastructure—many proposer/solver rollouts and verifier calls are still required.

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

`retriever objective ↔ query/refinement policy ↔ corpus-operation policy ↔ state recovery ↔ resource allocation ↔ training-task distribution`.

Agentic-R changes retriever utility; Critic-R uses natural-language process feedback to repair and train retrieval; GrepSeek learns shell interaction itself; LoongReflect learns when to discard active state; SearchMaster changes **which self-generated tasks and trajectories are allowed to supervise the learner**.

That last distinction matters for self-improving agents. A policy can optimize perfectly against a bad self-generated curriculum. SearchMaster's strongest lesson is therefore not “self-play works,” but that evidence grounding, task difficulty, and tool-use regularization need their own objectives.

The causal bar is **same environment + same state/action space + same answer model + matched realized resources**, while separately varying both the learned component and the supervision/curriculum that trained it. Otherwise a richer interface, privileged teacher/verifier, extra refinement attempts, or easier self-generated tasks can masquerade as better learning.

## What would count as meaningful progress?

A strong experiment should compare prompted, supervised, RL, and self-play controllers on the same information environment while separately toggling retriever learning, query refinement, direct-corpus operations, recovery semantics, and **task-generation policy**. For self-play systems, report not only final QA but also shortcut/pseudo-task rate, realized search depth, verifier/rollout compute, tool-use drift, transfer under corpus/workload change, and whether task difficulty remains meaningful as the learner improves.
