# Visual brief — Weekly 2026-W32 synthesis

**Renderer:** GPT-image-gen  
**Status:** pending generation  
**Grounding:** canonical records for READ, DocNavRAG, and ACE-GraphRAG; abstract-level evidence caveats preserved

## Visual question

What is the common design movement across early-August Agentic RAG, and what competing explanation prevents us from calling it simply an “agentic win”?

## Grounded synthesis

Show one control stack with three highlighted changes:

1. **interface** — top-k becomes explicit search/navigation/read operations;
2. **state** — collected/missing evidence drives the next action;
3. **policy** — context assembly over a rich graph becomes adaptive.

Add a skeptical side annotation: **better primitive / more budget?** The visual should make clear that policy gains are confounded unless primitive and budget are matched.

## Compared with

A conventional pipeline where retrieval is a single top-k stage and context assembly is fixed.

## Do not imply

- Do not show three papers as proof of a settled paradigm shift.
- Do not imply READ beats BM25; the reported result is statistically indistinguishable.
- Do not merge DocNavRAG evidence state and ACE-GraphRAG policy into one invented architecture.

## Art direction

Wide research field map rather than one architecture. Use three adjacent layers or cards—`interface`, `state`, `policy`—connected by a light progression arrow. A small caution wedge labeled `primitive / budget confound` should cut across the progression. Minimal labels and generous whitespace.
