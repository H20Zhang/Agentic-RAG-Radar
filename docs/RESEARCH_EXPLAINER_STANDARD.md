# Research Explainer Standard

Use this standard for high-value Agentic RAG paper notes, README folds, Reading Paths, and category arguments. It fixes the reasoning sequence, not the prose template.

## 1. Research delta

State the smallest change that matters:

`previous design → changed control/information placement → consequence`

Avoid generic architecture summaries.

## 2. Problem that survives the strongest existing design

Explain what still fails after giving the baseline a competent retrieval backend, interface, harness, and reasonable budget. Do not motivate an agentic controller by comparing only with a weak one-shot baseline.

## 3. Mechanism / information flow

Describe the actual loop:

`information need → query/planning → retrieval interface → evidence materialization → inspect/reason → continue/redirect/stop → retained state → answer/action`

Name where adaptivity lives, when evidence becomes materialized, and what state persists.

## 4. Closest comparison

Always answer:

- closest meaningful alternative;
- backend/model/interface/harness/budget held fixed;
- which variables still change together.

Treat unmatched system gains as package-level evidence.

## 5. Decisive evidence

Keep 1–3 belief-changing results, including useful negative results. Separate answer quality, evidence coverage, number of retrieval actions, retained context, latency/tokens, and total lifecycle cost when the paper reports them.

Fewer search calls do not imply lower total cost if controller/oracle/re-thinker work increases.

## 6. What remains unproven

Surface the strongest attribution or systems gap, such as:

- interface/harness mismatch;
- stale versus fresh corpus mismatch;
- offline indexing cost moved online;
- controller cost omitted from search-call accounting;
- dropped context reappearing as reacquisition;
- privileged supervision;
- answer gains absent despite evidence gains.

## 7. Field-map consequence

State which design axis changes:

- adaptivity placement;
- evidence-materialization time;
- retrieval-interface resolution;
- state persistence/recoverability;
- resource/lifecycle accounting;
- evaluation causal identifiability.

## 8. Related reading

Choose 2–4 works for contrast or continuation. Prefer a predecessor, a competing design point, and the next evidence boundary rather than a long related-work list.

## README compression

A 60–90 second README fold should retain the causal story, closest comparison, decisive evidence, and strongest caveat in 2–4 natural paragraphs. It must not copy the full research note.

## Epistemic discipline

Distinguish paper-reported fact, curator interpretation, and open hypothesis / decisive next test explicitly in wording.
