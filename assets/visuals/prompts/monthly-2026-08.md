# Visual brief — Monthly 2026-08 field map

**Renderer:** GPT-image-gen  
**Status:** pending generation  
**Grounding:** rolling August synthesis backed by canonical records for READ, DocNavRAG, ACE-GraphRAG, plus design anchors A-RAG, Search-o1, PlanRAG, Graph-R1, and Agentic-R

## Visual question

What research stack is emerging in Agentic RAG, and where is August activity currently concentrated?

## Grounded synthesis

Show a four-layer horizontal or vertical research stack:

1. **retrieval substrate** — documents / graph / database;
2. **operation / interface** — top-k vs explicit search / navigation / read actions;
3. **evidence state / controller** — collected/missing evidence, context-gap detection, routing/stopping;
4. **learning / evaluation** — trajectory learning, retriever learning, matched-budget evaluation.

Highlight August activity primarily around layers 2 and 3. Add a small cross-cutting audit ribbon: **budget / primitive confounds**.

## Research delta to emphasize

The field is beginning to move from asking only *which retriever is best?* toward designing and evaluating the **control stack around retrieval**.

## Compared with

A retriever-centric view where RAG is mostly `query → retriever → top-k context → generation` and all improvement is attributed to retrieval quality.

## Do not imply

- Do not present the four-layer stack as a settled community consensus; it is the radar's current research map.
- Do not imply August has enough papers to prove a long-term trend.
- Do not visually attribute system-level gains to policy when interface or budget changed simultaneously.
- Do not make the figure a timeline; it is a design-space map.

## Art direction

Clean research field map with four stacked layers, each using a simple symbolic motif. Visually emphasize `interface` and `state/controller`; keep `substrate` and `learning/evaluation` supportive. A thin skeptical ribbon labeled `primitive / budget confounds` should cut across the stack. Minimal text, no decorative robot or glowing neural-network imagery.
