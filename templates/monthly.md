# Agentic RAG Monthly — YYYY-MM

> **Coverage:** YYYY-MM-01 to YYYY-MM-DD · **Status:** rolling/finalized · **Accepted papers:** N

## Month thesis

State the best current model of **how the research map changed**, not how many papers appeared. For a rolling month, rewrite this thesis when new evidence contradicts it; do not append chronology to protect an early narrative.

## Field-map clusters

Organize papers by the control abstraction they change, for example:

- retrieval substrate;
- operation/interface;
- evidence/progress state;
- planning/routing/control policy;
- learning/optimization;
- evaluation/failure analysis.

A cluster needs a shared mechanism or trade-off, not just similar vocabulary.

## Older anchors reinterpreted

When current papers change how earlier work should be understood, make that connection explicit. This prevents the monthly report from becoming a standalone list disconnected from the field's design trajectory.

## Most important papers

Select only papers that materially change an abstraction, method family, benchmark, or evidence base. For each:

**lasting delta → nearest prior design point → evidence strength → what remains unproven.**

For sparse months, fewer papers with deeper comparison is better.

## Core causal tension

Give the strongest competing explanations for current gains. Explicitly reason over:

`substrate × operation set × state × policy × budget`

Do not attribute a system-level gain to `policy` if the operation set, model, or budget also changed without a separating ablation.

## Evidence audit

Assess:

- benchmark concentration and domain diversity;
- repeated/weak baselines;
- retrieval calls, retrieved tokens, latency/cost;
- component and state/policy ablations;
- negative results or baseline reversals;
- percentage of load-bearing claims that are full-text-grounded.

## Visual field map

When it improves understanding, generate **one GPT-image-gen field map** grounded in canonical records. It should show the month-level design movement or tension—not decorate the report. Keep labels minimal and save a separate grounding brief.

## Open problems

List **3–5 questions** whose resolution would change what researchers build, train, or evaluate next.

## Minimal reading path

Teach the month efficiently: essential abstraction first, then optional depth. A non-chronological path is usually better.

## Rolling/final status

If rolling, state which parts of the field map are provisional and what new evidence would falsify them. At month close, finalize unless later corrections materially change the synthesis.

---

**Anti-drift rule:** weekly reports may be used as an index, but load-bearing monthly claims must be re-grounded in canonical paper records and source/full-paper notes.
