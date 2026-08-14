# Evaluation & Analysis

> **Core question:** How do we tell whether an Agentic RAG system is genuinely making better information-acquisition decisions rather than using better tools, looser budgets, more compute, easier benchmarks—or rediscovering an older IR/QA control pattern under new terminology?

This category covers benchmarks, surveys/SoKs, diagnostic studies, failure analysis, historical/systematization work, and evaluation methodology for adaptive retrieval systems.

## Current design anchors

### [VAKRA](../papers/2608.12282.md) — ★★★★☆

**Design point:** evaluate **executable cross-source trajectories** that combine APIs and document retrieval under natural-language tool-use policies, while holding the ReAct harness fixed across models.

**Why it matters:** isolated API accuracy and document QA miss the composition failure. VAKRA's trace analysis points instead to entity disambiguation and cross-source grounding as major failure surfaces. The benchmark therefore tests a capability closer to enterprise research agents: maintaining a coherent evidence chain across heterogeneous sources.

**Caveat:** the fixed harness isolates model capability but does not identify which planner, memory, or retrieval-controller architecture would repair the failures.

### [When Should Active RAG Retrieve?](../papers/2607.24010.md) — ★★★★☆

**Design point:** make the router's **operating point** auditable: separate utility ranking, calibrated threshold transfer, realized evidence usage, retrieval harm, and trigger-side cost.

**Why it matters:** two systems with the same nominal “50% retrieval budget” are not matched if their held-out usage differs. Even matched evidence use is not matched total cost when one controller needs a probe retrieval or no-retrieval generation before deciding.

### [Forgotten History or Test-of-Time?](../papers/2608.08445.md) — ★★★★☆

**Design point:** push the novelty baseline for Agentic RAG back to classical IR/QA, with QUALIFIER as a concrete retrieve→verify→reformulate precedent.

**Why it matters:** “iterative retrieval,” query refinement, verification, or stopping are not sufficient novelty claims by themselves. Modern work should isolate what LLM-era interfaces, learning, state, scale, or capability add.

### [Agentic RAG SoK](../papers/2603.07379.md) — ★★★☆☆

**Design point:** organize Agentic RAG as a sequential decision process over state, retrieval/tool actions, observations, and stopping.

## Evaluation lens used by this radar

For a system-level gain, separate when possible:

`substrate × operation set × state × policy × realized budget × base model × historical baseline`

VAKRA adds a complementary question: **does the benchmark require the agent to compose those variables across heterogeneous sources in one executable trajectory?** A model can be good at selecting an API and good at document QA independently yet still fail when entity identity, retrieved evidence, and policy constraints must remain consistent across both.

“Realized” budget remains deliberate. Report calls/tokens/context volume/latency separately, and ask whether a learned threshold actually transfers to the held-out usage target and how often retrieval changes a correct no-retrieval answer into a wrong one.

The historical axis does not mean “nothing is new.” It asks whether novelty lies in the control-loop shape or in modern representation, learning, scale, tool interfaces, and richer information environments.

## What would count as meaningful progress?

The next bar is an executable trajectory benchmark that combines **cross-source grounding + intervention-style attribution + realized multi-resource frontiers**. VAKRA supplies the first part; Active-RAG evaluation supplies operating-point discipline. The missing experiment would replay the same failing task under alternate controllers or patched intermediate states to isolate whether the error came from source selection, entity grounding, retrieval, policy interpretation, or synthesis.
