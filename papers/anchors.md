# Design Anchors

These bootstrap papers are **design points**, not a ranking. Each has an individual research card and visual brief.

| Paper | Design point | Research card |
|---|---|---|
| **A-RAG** | hierarchical retrieval interface | [2602.03442](2602.03442.md) |
| **Search-o1** | search inside reasoning | [2501.05366](2501.05366.md) |
| **PlanRAG** | explicit information-acquisition planning | [2406.12430](2406.12430.md) |
| **Graph-R1** | learned multi-turn graph retrieval policy | [2507.21892](2507.21892.md) |
| **Agentic-R** | retriever learning for trajectory utility | [2601.11888](2601.11888.md) |
| **Agentic RAG SoK** | sequential-decision framing | [2603.07379](2603.07379.md) |

## Suggested reading order

**PlanRAG → Search-o1 → A-RAG → Graph-R1 / Agentic-R → SoK**

- PlanRAG makes the retrieval plan explicit.
- Search-o1 moves search inside reasoning.
- A-RAG redesigns the retrieval API itself.
- Graph-R1 learns the graph-interaction trajectory.
- Agentic-R learns the retriever for downstream trajectory utility.
- The SoK then provides a higher-level decision-process framing.

## Bootstrap caveat

Initial notes were curated from verified metadata, abstracts, and official project information. Canonical records keep `full_text_checked` explicit; importance and visual grounding should only be upgraded after deeper evidence review.
