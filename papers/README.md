# Curated Paper Index

A complete chronology of papers **accepted by Agentic RAG Radar**. This is a curated research index, not a claim of exhaustive coverage of all Agentic RAG literature.

Use [Latest Papers](../README.md#-latest-papers) for the newest high-priority work, [What's Changing](../README.md#-whats-changing) for synthesis, [Reading Paths](../README.md#-reading-paths) for guided study, and the [Research Map](../categories/README.md) for problem-oriented browsing.

## Browse by Research Problem

- [Planning & Query Formulation](../categories/planning-query-formulation.md)
- [Retrieval & Tool Use](../categories/retrieval-tool-use.md)
- [Iterative Reasoning & Verification](../categories/iterative-reasoning-verification.md)
- [Multi-Agent & Orchestration](../categories/multi-agent-orchestration.md)
- [Learning & Optimization](../categories/learning-optimization.md)
- [Evaluation & Analysis](../categories/evaluation-analysis.md)

## Chronology

## 2026

### August

#### 2026-08-17 · [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](2608.16370.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** When queryable execution state is dropped, the agent can enter a re-query loop: retrieval rises while task work stays roughly flat; restoring that state removes most of the added interaction.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.16370) · [Research note](2608.16370.md)

#### 2026-08-17 · [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](2608.16185.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** LENS keeps the evidence space latent until the query arrives, then iteratively proposes raw-document regions, observes LLM relevance, updates beliefs, and stops under a budget.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.16185) · [Research note](2608.16185.md)

#### 2026-08-15 · [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](2608.15191.md)
`Iterative Reasoning & Verification` · **★★★★☆**

**Research delta.** RAAC observes criteria coverage, document novelty, query diversity, and query-to-question similarity, then chooses continue, intervene with a critical re-thinker, or stop.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.15191) · [Research note](2608.15191.md)

#### 2026-08-13 · [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](2608.12888.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** ReFind keeps the raw archive intact and moves intelligence into a stateful runtime interface: reformulate lexical queries, expand local context, use session/time structure, skip inspected sessions, and collect evidence over multiple rounds.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](2608.12888.md)

#### 2026-08-12 · [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](2608.12282.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** VAKRA evaluates executable cross-source trajectories under a fixed agent harness and finds that the difficult boundary is often language-mediated entity and evidence grounding rather than API invocation syntax alone.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.12282) · [Research note](2608.12282.md) · [Code](https://github.com/IBM/vakra)

#### 2026-08-12 · [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](2608.11967.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** The agent can explicitly reflect on evidence/risk and backtrack to a trusted prefix, while privileged local supervision and outcome RL jointly train those recovery decisions.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.11967) · [Research note](2608.11967.md)

#### 2026-08-09 · [Forgotten History or Test-of-Time? Retrospect and Prospect on RAG from an IR Perspective](2608.08445.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** The useful novelty baseline extends back to classical IR/QA: query reformulation, verification, constraint relaxation, and iterative retrieval existed long before LLMs, while LLMs change the interface and implementation regime.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.08445) · [Research note](2608.08445.md)

#### 2026-08-08 · [SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems](2608.08237.md)
`Learning & Optimization` · **★★★☆☆**

**Research delta.** A lightweight policy uses retrieval-side features to choose a query-specific passage budget k before generation, making retrieval budget a controllable systems action rather than a global constant.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.08237) · [Research note](2608.08237.md)

#### 2026-08-06 · [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](2608.06305.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** The key delta is an agent-controlled operation set—lexical search, structural navigation, and bounded reads—with observations feeding the next retrieval decision.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2608.06305) · [Research note](2608.06305.md)

#### 2026-08-03 · [SearchMaster: Grounded and Regulated Self-Play for Search Agents](2608.01822.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** The key delta is not self-play alone: explicit evidence-chain task generation, search-depth-aware task reward, and an over-opening penalty shape which tasks and trajectories become training signal.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.01822) · [Research note](2608.01822.md) · [Code](https://github.com/WentaoTan/SearchMaster)

#### 2026-08-03 · [Search, Inspect, Fetch: Exploiting Boolean Retrieval for Deep-Research Agents](2608.02751.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** The research delta is a structure-preserving search-inspect-fetch interface: Boolean constraints define what may be considered, ranking orders it, result cards expose addressable structure, and fetch reads only the selected section.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2608.02751) · [Research note](2608.02751.md) · [Code](https://github.com/ielab/skim-search-agent)

#### 2026-08-03 · [DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction for Complex Document Question Answering](2608.01565.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** The key delta is environment–policy co-design: document-native navigation updates an explicit collected/missing evidence state that drives the next retrieval action.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2608.01565) · [Research note](2608.01565.md)

#### 2026-08-02 · [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](2608.01269.md)
`Iterative Reasoning & Verification` · **★★★★☆**

**Research delta.** The key delta is a context-policy layer that detects gaps and selects complementary depth/breadth retrieval branches rather than using fixed graph context assembly.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2608.01269) · [Research note](2608.01269.md)

### July

#### 2026-07-27 · [When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost](2607.24010.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** A router must be evaluated at an operating point that separates utility ranking, threshold-to-budget calibration, retrieval harm, and trigger-side cost.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2607.24010) · [Research note](2607.24010.md)

#### 2026-07-27 · [A New Role for Relevance: Guiding Corpus Interaction in Agentic Search](2607.24223.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** RARG carries relevance into DCI execution: document order, entry points, and match-level observations are prioritized rather than treating all files/matches as equally promising.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2607.24223) · [Research note](2607.24223.md) · [Code](https://github.com/LeqsNaN/RARG)

### June

#### 2026-06-29 · [Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented Generation](2606.29959.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** The important abstraction is graded budget allocation with separate cost axes: retrieval-call rate, full-context rate, passage budget, and measured latency are not interchangeable.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2606.29959) · [Research note](2606.29959.md) · [Code](https://github.com/dongzhe1/know-before-you-fetch)

#### 2026-06-24 · [SPARKLE: A Structured and Plug-and-play Agentic Retrieval Policy for Adaptive RAG Models](2026.acl-long.1793.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** A separate proxy policy decides whether to retrieve, formulates queries, and integrates retrieved knowledge; PPO with tree-structured rollouts optimizes that policy without finetuning the retriever or answer LLM.

**Evidence basis.** full-text reviewed

[Paper](https://aclanthology.org/2026.acl-long.1793/) · [Research note](2026.acl-long.1793.md) · [Code](https://github.com/jyfang6/sparkle)

#### 2026-06-12 · [DR-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion](2606.14885.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** DR-DCI alternates retriever-steered workspace expansion with local DCI operations, using retrieval for corpus-scale recall and direct interaction for evidence resolution.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2606.14885) · [Research note](2606.14885.md) · [Code](https://github.com/EigenTom/DR-DCI)

#### 2026-06-05 · [Towards Retrieving Interaction Spaces for Agentic Search](2606.06880.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** RISE makes retrieval construct a persistent bounded interaction space outside the context window, then preprocesses documents with navigational structure for shell-style local inspection.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2606.06880) · [Research note](2606.06880.md) · [Code](https://github.com/texttron/RISE)

### May

#### 2026-05-30 · [Critic-R: Improving Agentic Search using Instruction-tuned Retrievers with Natural Language Introspective Feedback](2606.00590.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** A separate critic judges evidence sufficiency from the reasoner's introspective trace, rewrites failed queries at inference, and converts accepted/rejected refinement trajectories into positives and hard negatives for retriever training.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2606.00590) · [Research note](2606.00590.md) · [Code](https://github.com/zarif98sjs/Critic-R)

#### 2026-05-28 · [GrepSeek: Training Search Agents for Direct Corpus Interaction](2605.29307.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** GrepSeek trains the DCI policy itself with verified cold-start trajectories followed by GRPO, while a sharded execution engine reduces shell-search cost without changing command semantics.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.29307) · [Research note](2605.29307.md) · [Code](https://github.com/alirezasalemi7/grepseek)

#### 2026-05-27 · [Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?](2605.27881.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** The study shows that environment coverage and training protocol can dominate algorithm choice; finer process rewards can also distort search behavior rather than uniformly improving it.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.27881) · [Research note](2605.27881.md) · [Code](https://github.com/YiboZhao624/SearchAgentReview)

#### 2026-05-25 · [Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki](2605.25480.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** The important delta is environment/interface co-design: documents are compiled into traversable Wiki pages, while the agent composes search, read, link-following, and sufficiency checks instead of consuming one fixed top-k context.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.25480) · [Research note](2605.25480.md)

#### 2026-05-21 · [SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval](2605.22219.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** The benchmark separates source discovery from environment configuration: the agent must preserve the site-specific retrieval state under which answer-bearing evidence becomes visible.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.22219) · [Research note](2605.22219.md) · [Project](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)

#### 2026-05-14 · [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](2605.15184.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** Retriever ranking can flip when the same model/retrieval method is placed in a different harness or when results move from inline context to programmatic file delivery.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.15184) · [Research note](2605.15184.md)

#### 2026-05-11 · [Rethinking Agentic Search with Pi-Serini: Is Lexical Retrieval Sufficient?](2605.10848.md)
`Evaluation & Analysis` · **★★★★☆**

**Research delta.** A strong lexical baseline is a system consisting of the backend ranker, how deep a ranking is surfaced, and how the agent can inspect that ranking; backend recall and agent-inspected evidence are distinct bottlenecks.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2605.10848) · [Research note](2605.10848.md) · [Code](https://github.com/justram/pi-serini) · [Project](https://ricky42613.github.io/piserini)

#### 2026-05-07 · [Superintelligent Retrieval Agent: The Next Frontier of Information Retrieval](2605.06647.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** SIRA moves control before evidence inspection: the LLM predicts missing evidence vocabulary, grounds it with corpus statistics, and compiles weighted lexical retrieval rather than learning vocabulary through repeated snippet exposure.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.06647) · [Research note](2605.06647.md) · [Code](https://github.com/facebookresearch/sira)

#### 2026-05-03 · [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](2605.05242.md)
`Retrieval & Tool Use` · **★★★★★**

**Research delta.** DCI reframes retrieval as interface resolution: grep/find/read/shell operations expose fine-grained evidence actions that a top-k similarity API hides.

**Evidence basis.** full-text reviewed

[Paper](https://arxiv.org/abs/2605.05242) · [Research note](2605.05242.md) · [Code](https://github.com/DCI-Agent/DCI-Agent-Lite)

### April

#### 2026-04-26 · [S2G-RAG: Structured Sufficiency and Gap Judging for Iterative Retrieval-Augmented QA](2604.23783.md)
`Iterative Reasoning & Verification` · **★★★★☆**

**Research delta.** The controller explicitly separates 'is current evidence sufficient?' from 'what is missing?', then maps structured gap items into the next retrieval query while keeping a compact evidence memory.

**Evidence basis.** full-text reviewed

[Paper](https://aclanthology.org/2026.acl-long.1185/) · [Research note](2604.23783.md)

### March

#### 2026-03-07 · [SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions](2603.07379.md)
`Evaluation & Analysis` · **★★★☆☆**

**Research delta.** The useful organizing lens is state → action/control policy → retrieval/tool observation → state update → stop/generate, with architecture/evaluation choices mapped onto that loop.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2603.07379) · [Research note](2603.07379.md)

### February

#### 2026-02-03 · [A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces](2602.03442.md)
`Retrieval & Tool Use` · **★★★★☆**

**Research delta.** The key delta is the retrieval API: broad keyword/semantic discovery and fine-grained chunk reading become explicit actions that the model composes adaptively.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2602.03442) · [Research note](2602.03442.md) · [Code](https://github.com/Ayanami0730/arag) · [Project](https://agentresearchlab.com/agents/a-rag/index.html)

### January

#### 2026-01-17 · [Agentic-R: Learning to Retrieve for Agentic Search](2601.11888.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** The retriever and the agent's evolving query distribution are coupled: retrieval is optimized for usefulness to the final multi-turn trajectory, not only local similarity.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2601.11888) · [Research note](2601.11888.md) · [Code](https://github.com/8421BCD/Agentic-R)

<details>
<summary><strong>2025</strong></summary>

### July

#### 2025-07-29 · [Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning](2507.21892.md)
`Learning & Optimization` · **★★★★☆**

**Research delta.** The knowledge graph becomes an interactive environment and the whole reason→graph-action→observation trajectory is optimized with outcome-level reinforcement learning.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2507.21892) · [Research note](2507.21892.md) · [Code](https://github.com/LHRLAB/Graph-R1)

### January

#### 2025-01-09 · [Search-o1: Agentic Search-Enhanced Large Reasoning Models](2501.05366.md)
`Iterative Reasoning & Verification` · **★★★★☆**

**Research delta.** Search is triggered at knowledge gaps inside reasoning, while a separate document-reasoning step distills retrieved evidence before reinjection into the main trajectory.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2501.05366) · [Research note](2501.05366.md) · [Code](https://github.com/sunnynexus/Search-o1)

</details>

<details>
<summary><strong>2024</strong></summary>

### June

#### 2024-06-18 · [PlanRAG: A Plan-then-Retrieval Augmented Generation for Generative Large Language Models as Decision Makers](2406.12430.md)
`Planning & Query Formulation` · **★★★☆☆**

**Research delta.** The high-level plan becomes the controller for iterative data acquisition instead of letting retrieval evolve as an unstructured sequence of searches.

**Evidence basis.** abstract-level

[Paper](https://arxiv.org/abs/2406.12430) · [Research note](2406.12430.md) · [Code](https://github.com/myeon9h/PlanRAG)

</details>

---

The index is generated deterministically from `data/papers/*.json`; research theses, category tensions, and reading paths remain human-edited and evidence-grounded.
