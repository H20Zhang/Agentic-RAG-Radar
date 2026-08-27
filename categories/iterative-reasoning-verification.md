# Iterative Reasoning & Verification

[← Research Map](README.md) · [Latest Papers](../README.md#-latest-papers) · [Reading Paths](../README.md#-reading-paths) · [Curated Paper Index](../papers/README.md)
> **Core question:** What progress/state should make the next retrieval, redirect, verification, recovery, or stopping decision?

This category is about the closed loop after retrieval begins. The important object is not “iteration” itself, but the state that tells the controller what has been established, what is missing, whether search is still producing new information, and whether the current branch should continue.

## Current papers


### [EviGraph](../papers/2608.24667.md) — ★★★★★

**Design point:** materialize verified source spans into claim-level support/conflict state so retrieval failure, recording failure, and stopping failure are separately observable. **Boundary:** the frozen verifier supplies privileged semantic judgments; the clean result isolates RL inside the dual-role architecture, not the full graph package.

### [NIS-Agent](../papers/2608.23045.md) — ★★★★☆

**Design point:** separate search ownership, evidence validation, and synthesis. Its fixed-results Observer Mode isolates a 15–30 point judgment effect; the end-to-end package still changes roles, stopping, prompts, and tool flow together.

### [EvoWiki](../papers/2608.23265.md) — ★★★★☆

**Design point:** resolve supersession while writing incremental state and preserve closed validity intervals for audit. The matched no-overwrite control reinforces StateMem's separation between historical recall and operative-state assembly.

### [Compaction Cliff](../papers/2608.22752.md) — ★★★★☆

**Design point:** protect hard constraints as a distinct state type under compaction. **Boundary:** typed metadata is privileged relative to type-blind controls and downstream context budgets are not matched.

### [ASCP](../papers/2608.23252.md) — ★★★★☆

**Design point:** factorially compare fixed evidence reuse, fresh rotation, and feedback-conditioned context allocation. **Boundary:** the full scheduler is statistically tied with deep rotation, and their matched resource delta is unreported.

### [SSE-Bio](../papers/2608.22132.md) — ★★★★☆

**Design point:** route among no retrieval, KG, reusable templates, or both from explicit reasoning-gap state. **Boundary:** absolute joint correctness is low and most audited failures occur after routing.

### [D2-ScaleAgent](../papers/2608.16417.md) — ★★★☆☆

**Design point:** use an Evidence Bank and verifier to route between breadth (“find another page”) and depth (“inspect a found page more closely”) rather than treating iteration count as the control variable.

**Boundary:** verifier removal is informative, but the full package's 21.4K tokens, latency, and routing calls are not matched in the key controls; direct Gemini VQA remains stronger on both main benchmarks.

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
