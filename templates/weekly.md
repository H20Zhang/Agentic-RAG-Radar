# Agentic RAG Weekly — YYYY-Www

> **Coverage:** YYYY-MM-DD to YYYY-MM-DD · **Status:** finalized · **Accepted papers:** N

## Week thesis

Write **one falsifiable statement** about what changed. If hiding all paper titles makes the sentence meaningless, it is probably not a research thesis yet.

For a sparse week, expand the mechanism/evidence comparison rather than padding with more papers.

## 1–3 shifts worth keeping

For each shift:

1. name the changed abstraction/control point;
2. explain what the previous design point did;
3. connect only the papers that actually support the shift;
4. state why the shift changes a research or systems decision.

Do not call a single-paper observation a trend unless explicitly labeled an early signal.

## Most important papers

Keep this short. For every selected paper use:

**Research delta → compared with what → strongest evidence → strongest caveat → why it matters.**

Importance is not relevance and not recency.

## Core tension / alternative explanation

Construct the strongest skeptical interpretation of the week's apparent progress. Examples:

- better retrieval primitive vs better agent policy;
- more retrieval/tokens vs better decisions;
- richer representation vs better context selection;
- stronger base model vs better system design.

Preserve negative results and baseline reversals.

## Evidence audit

Audit the factorized axes where applicable:

`substrate × operation set × state × policy × budget`

Check retrieval calls, retrieved tokens, latency/cost, baseline strength, ablations, benchmark concentration, and whether key claims are full-text-grounded.

## Visual synthesis

When it materially helps, create **one GPT-image-gen cluster/tension map** grounded in canonical records. Keep labels minimal and store its grounding brief under `assets/visuals/prompts/`.

## Reading order

Give the shortest sequence that teaches the design space, not a chronological list.

## Questions to carry into next week

End with **1–3 questions** whose answers would change the current synthesis.

---

**Compaction rule:** remove repeated summary detail, not disagreement, uncertainty, provenance, or causal alternatives.
