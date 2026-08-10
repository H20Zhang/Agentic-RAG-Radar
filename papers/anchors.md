# Anchor Papers

These are bootstrap anchors used to define the research space. They are **not** a ranking of the whole field. The first-pass notes below are intentionally marked as bootstrap interpretations; canonical records preserve whether full text has been checked.

## A-RAG — Hierarchical Retrieval Interfaces

**A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces** · arXiv:2602.03442  
`Retrieval & Tool Use` · `tool selection` · `iterative search`

**TL;DR.** Give the model keyword search, semantic search, and chunk read as explicit retrieval actions, then let it compose them adaptively rather than execute a fixed RAG workflow.

**Agent loop.** `Reason → choose search tool → inspect → chunk read → refine or answer`

**Why it matters.** The useful abstraction is the retrieval **interface**: if frontier models already improve at tool use, a small well-designed hierarchy of retrieval operations may scale better than increasingly elaborate hard-coded RAG pipelines.

[Paper](https://arxiv.org/abs/2602.03442) · [Code](https://github.com/Ayanami0730/arag)

## Agentic-R — Train the Retriever for the Agent Trajectory

**Agentic-R: Learning to Retrieve for Agentic Search** · arXiv:2601.11888  
`Learning & Optimization` · `iterative search` · `retriever learning`

**TL;DR.** Train retrieval for downstream trajectory utility, not only local query–passage similarity, and let the retriever co-evolve with the agent's changing query distribution.

**Agent loop.** `Reason → query → retrieve → update query/state → repeat → answer`

**Why it matters.** Once retrieval is an action in a multi-turn policy, a retriever optimized for static relevance is solving the wrong objective. This paper makes that mismatch explicit.

[Paper](https://arxiv.org/abs/2601.11888) · [Code](https://github.com/8421BCD/Agentic-R)

## Search-o1 — Search Inside the Reasoning Trace

**Search-o1: Agentic Search-Enhanced Large Reasoning Models** · arXiv:2501.05366  
`Iterative Reasoning & Verification` · `on-demand search`

**TL;DR.** Trigger external search at knowledge gaps inside a long reasoning trace and use a separate document-reasoning step to distill retrieved evidence before returning it to the main chain.

**Agent loop.** `Reason → detect gap → search → reason over documents → inject evidence → continue`

**Why it matters.** Search becomes a native reasoning action rather than a preprocessing step, while evidence processing is separated from the main reasoning trajectory to control noise.

[Paper](https://arxiv.org/abs/2501.05366) · [Code](https://github.com/sunnynexus/Search-o1)

## Graph-R1 — Learn Multi-turn Graph Retrieval

**Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning** · arXiv:2507.21892  
`Learning & Optimization` · `GraphRAG` · `RL`

**TL;DR.** Treat the knowledge graph as an interactive retrieval environment and optimize a multi-turn graph retrieval/reasoning policy end to end with RL.

**Agent loop.** `Reason → graph action → observe evidence → update state → repeat → answer`

**Why it matters.** It shifts GraphRAG from static graph-context construction toward learned retrieval trajectories, making intermediate graph access part of the policy.

[Paper](https://arxiv.org/abs/2507.21892) · [Code](https://github.com/LHRLAB/Graph-R1)

## PlanRAG — Plan Before Data Acquisition

**PlanRAG: A Plan-then-Retrieval Augmented Generation for Generative Large Language Models as Decision Makers** · arXiv:2406.12430 · NAACL 2024  
`Planning & Query Formulation` · `database`

**TL;DR.** Generate an explicit decision plan first, then use that plan to drive iterative data retrieval and analysis.

**Agent loop.** `Plan → data query → retrieve/analyze → update → repeat → decide`

**Why it matters.** It makes the high-level information-acquisition plan explicit instead of treating iterative retrieval as an unstructured sequence of searches.

[Paper](https://arxiv.org/abs/2406.12430) · [Code](https://github.com/myeon9h/PlanRAG)

## Agentic RAG SoK — Sequential Decision View

**SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions** · arXiv:2603.07379  
`Evaluation & Analysis`

**TL;DR.** Formalize Agentic RAG as a sequential decision process and organize architectures around control policies, retrieval orchestration, memory, and tool invocation.

**Why it matters.** The strongest potential contribution is not another taxonomy label set but a trajectory-level view that could make evaluation and failure analysis more principled.

[Paper](https://arxiv.org/abs/2603.07379)

---

**Bootstrap caveat:** these cards are initial curator interpretations based on verified metadata and paper abstracts/project information. The canonical records currently mark `full_text_checked: false`; the daily research reader should progressively upgrade high-value anchors with full-paper evidence and ablation-level notes.
