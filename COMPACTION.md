# Research Compaction Protocol

Agentic RAG Radar treats paper curation as a **research-memory hierarchy**, not an append-only stream of Markdown summaries.

The objective is to preserve enough provenance to revisit a paper or curation decision while continuously compressing repeated detail into higher-level research judgments.

## Levels

| Level | Persistent artifact | Purpose | What must not be lost |
|---|---|---|---|
| **L0 · Paper records** | `data/papers/*.json` + `papers/*` | Canonical facts, provenance, classification, paper-level interpretation, visual grounding. | source links, evidence status, uncertainty, corrections |
| **L0-log · Daily runs** | `runs/daily/YYYY/MM/DD.md` | Compact archival history of what the curator accepted, deferred, corrected, or failed to complete. | decision history, borderline exclusions, visual/workflow failures |
| **L1 · Weekly compaction** | `digests/weekly/YYYY-Www.md` | Identify the week's real research deltas, disagreements, and reading priority. | negative results, conflicting assumptions, evidence caveats |
| **L2 · Monthly compaction** | `digests/monthly/YYYY-MM.md` | Rebuild the field map: abstractions, evidence strength, open problems, and changes in research direction. | competing explanations, weakening claims, unresolved causal attribution |

Daily ingestion updates L0 and writes **one compact nested run log** for provenance. Those run logs are not paper summaries and are never the primary browsing interface.

## Editorial principle

A compaction is successful only if it answers questions that a chronological list cannot:

> **So what changed? Compared with what? How strong is the evidence? What should a researcher do differently after reading this?**

A report should become *shorter than the source material but harder to write*. If it is mostly one paragraph per paper, it is not compaction yet.

## Daily run-log policy

Daily logs exist to debug and audit the curator, not to accumulate another human-facing paper feed.

A run log should record only:

- discovery window / notable source changes when material;
- newly accepted papers and one-line inclusion reason;
- important deferred/rejected borderline candidates;
- meaningful classification/evidence corrections;
- visual-generation/backfill status or workflow blockers;
- whether weekly/monthly compaction was created or revised.

Do **not** duplicate full TL;DRs, experiment tables, or per-paper research notes. Those belong in canonical records/cards.

Nest logs under `runs/daily/YYYY/MM/` so the repository does not degrade into hundreds of top-level date files.

## Weekly compaction

A weekly report should be detailed when the number of papers is small. Sparse weeks are an opportunity to compare mechanisms and evidence carefully rather than pad the report with more papers.

It should contain:

1. **Week thesis** — one falsifiable statement about what changed.
2. **1–3 durable shifts** — clusters defined by research delta/control point, not title keywords.
3. **Most important papers** — only papers that change an abstraction, method family, benchmark, or evidence base; each must answer `delta → compared with → evidence → so what`.
4. **Tension / disagreement** — at least one alternative explanation, negative result, or reason the apparent trend may be overstated when evidence permits.
5. **Evidence audit** — matched retrieval/token budget, baseline quality, ablations, benchmark concentration, and full-text-grounding status.
6. **Reading order + open questions** — minimal sequence that teaches the design space, followed by 1–3 questions worth tracking.

### Weekly attribution rule

A paper can be discussed as **adjacent context** when its publication date falls just outside the ISO week but it is needed to make a comparison intelligible. Label this explicitly; do not silently inflate the week's paper count.

## Monthly compaction

The monthly report operates one abstraction level higher. During an open month it may exist as **rolling**, but it must be rewritten as evidence changes rather than appended chronologically. After the month closes it becomes **finalized** unless later corrections materially change the synthesis.

A monthly report should contain:

- **Month thesis** — the best current model of how the field map changed.
- **Field-map clusters** — method families/control points that grew, converged, split, or weakened.
- **Older anchors reinterpreted** — when new work changes how earlier papers should be understood, make that connection explicit.
- **Most important papers** — usually 5–10 maximum for a mature month; fewer is better when evidence is sparse.
- **Core tension** — competing causal explanations for observed gains.
- **Evidence audit** — budget fairness, benchmark concentration, repeated baselines, negative results, and full-text coverage.
- **Open problems** — 3–5 questions whose answers could change what researchers build or evaluate next.
- **Minimal reading path** — teach the abstraction efficiently, not chronologically.

Monthly reports may use weekly reports as an **index only**. Every load-bearing claim must be re-grounded in canonical paper records and source/full-paper notes. Never recursively summarize weekly summaries as the sole evidence source.

## Multi-role challenge before synthesis

When parallel research roles are supported, roles should work independently before the final editor sees their outputs:

| Role | Job | What it should challenge |
|---|---|---|
| **Clusterer / Field Mapper** | Group papers by actual research delta and identify a candidate field map. | keyword similarity, fashionable naming, forced taxonomy fit |
| **Evidence Auditor** | Compare benchmarks, baselines, calls/tokens/latency, ablations, effect sizes, and negative results. | causal over-attribution, unfair budgets, weak baseline selection |
| **Trend Skeptic** | Construct the strongest alternative explanation for each proposed trend. | confirmation bias, three papers being mistaken for a paradigm shift |
| **Research Editor** | Write the synthesis after seeing the independent analyses. | verbosity, paper-by-paper concatenation, claims without consequences |

The editor should prefer **one important tension** over five weak trends.

## Factorized evaluation lens

Agentic RAG results frequently change several variables simultaneously. When possible, compactions should reason about these axes separately:

| Axis | Example values |
|---|---|
| **Substrate** | flat chunks / documents / graph / SQL / web / code |
| **Operation set** | top-k / lexical search / navigation / bounded read / graph actions / tool routing |
| **State** | raw history / evidence set / missing-information state / provenance / uncertainty |
| **Policy** | fixed heuristic / prompted agent / planner / learned policy / RL |
| **Budget** | retrieval calls / retrieved tokens / latency / monetary or energy cost |

A headline gain is not automatically evidence for the `policy` axis if the operation set or budget also changed.

## Retention and correction policy

- Keep every accepted canonical paper record.
- Keep per-paper Markdown when it adds researcher-facing explanation beyond the JSON record.
- Keep compact nested daily run logs as provenance; do not expose them as the main reading feed.
- Keep one weekly report per ISO week and one monthly report per calendar month.
- README is a rolling landing page, not an archive.
- Correct upward: if a paper's classification, evidence, or importance changes enough to alter a weekly/monthly conclusion, revise the compaction.
- Do not preserve an old narrative merely for consistency. A rolling report should explicitly change its thesis when new evidence falsifies it.

The goal is **lossy compression of repetition, not loss of disagreement, provenance, or uncertainty**.