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
| **L3 · Yearly compaction** | `digests/yearly/YYYY.md` | Re-evaluate the year and preserve only durable field shifts, defining papers, failed ideas, and next-year research questions. | changes of mind, important negative evidence, durable evaluation lessons |

Daily ingestion updates L0 and writes **one compact nested run log** for provenance. Those run logs are not paper summaries and are never the primary browsing interface.

## Public time hierarchy

The reader-facing archive deliberately reduces temporal resolution as work gets older:

- **Recent ~1 month → weekly reports.** Preserve local research movement while it is still useful to inspect week by week.
- **Recent ~1 quarter → monthly reports.** Compress older weekly detail into field-map changes.
- **All years → yearly reports.** Keep one durable research map per year as the long-term public history.

The lower-level files are **not deleted** when they age out of the primary navigation. They remain available for audit and provenance. The display hierarchy controls attention, not retention.

Do not create a historical yearly report unless coverage is sufficient to justify it. A handful of hand-picked anchors must never be presented as a full-year research map. The current year may have an explicitly labeled **rolling** report.

## Editorial principle

A compaction is successful only if it answers questions that a chronological list cannot:

> **So what changed? Compared with what? How strong is the evidence? What should a researcher do differently after reading this?**

A report should become *shorter than the source material but harder to write*. If it is mostly one paragraph per paper, it is not compaction yet.

## Daily run-log policy

Daily logs exist to debug and audit the curator, not to accumulate another human-facing paper feed. Record only discovery-window changes when material, newly accepted papers with one-line reasons, important deferred/rejected candidates, meaningful corrections, visual/backfill status, and compaction actions or blockers.

Do **not** duplicate full TL;DRs, experiment tables, or per-paper research notes. Nest logs under `runs/daily/YYYY/MM/`.

## Weekly compaction

A weekly report should be detailed when the number of papers is small. Sparse weeks are an opportunity to compare mechanisms and evidence carefully rather than pad the report with more papers.

It should contain:

1. **Week thesis** — one falsifiable statement about what changed.
2. **1–3 durable shifts** — clusters defined by research delta/control point, not title keywords.
3. **Most important papers** — only papers that change an abstraction, method family, benchmark, or evidence base; each must answer `delta → compared with → evidence → so what`.
4. **Tension / disagreement** — at least one alternative explanation, negative result, or reason the apparent trend may be overstated when evidence permits.
5. **Evidence audit** — matched retrieval/token budget, baseline quality, ablations, benchmark concentration, and full-text-grounding status.
6. **Reading order + open questions** — minimal sequence that teaches the design space, followed by 1–3 questions worth tracking.

A paper can be discussed as **adjacent context** when its publication date falls just outside the ISO week but it is needed to make a comparison intelligible. Label this explicitly; do not silently inflate the week's paper count.

## Monthly compaction

The monthly report operates one abstraction level higher. During an open month it may exist as **rolling**, but it must be rewritten as evidence changes rather than appended chronologically. After the month closes it becomes **finalized** unless later corrections materially change the synthesis.

A monthly report should contain a month thesis, field-map clusters, older anchors reinterpreted when useful, the few most important papers, a core causal tension, an evidence audit, 3–5 open problems, and a minimal reading path.

Monthly reports may use weekly reports as an **index only**. Every load-bearing claim must be re-grounded in canonical paper records and source/full-paper notes. Never recursively summarize weekly summaries as the sole evidence source.

## Yearly compaction

A yearly report is not twelve monthly summaries concatenated. It should answer a harder question: **what actually survived the year?**

A finalized yearly report should contain:

- **Year thesis** — the strongest field-level model that still holds after seeing the whole year.
- **Start-of-year → end-of-year change** — what the field stopped treating as default and what became first-class.
- **Durable shifts** — only changes supported across multiple months or by unusually strong evidence.
- **Papers that defined the year** — a short ranked set chosen by lasting research impact, not publication count.
- **Ideas that weakened or failed** — mid-year narratives, methods, or evaluation claims that did not survive stronger evidence.
- **Year-level evidence audit** — benchmark concentration, budget matching, replication/open-source evidence, and recurring confounders.
- **Open problems entering the next year** — questions whose answers could materially redirect the field.
- **Minimal yearly reading path** — the smallest sequence that teaches the year's durable changes.

The current year's report may be **rolling** and revised when monthly evidence changes the thesis. At year end it is finalized after re-grounding important claims in canonical paper records, not by recursively summarizing monthly reports.

Historical yearly reports require adequate coverage. If backfill is incomplete, say so explicitly or do not create the report.

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

Agentic RAG results frequently change several variables simultaneously. Compactions should reason about these axes separately whenever possible:

| Axis | Example values |
|---|---|
| **Substrate** | flat chunks / documents / graph / SQL / web / code |
| **Operation set** | top-k / lexical search / navigation / bounded read / graph actions / tool routing |
| **State** | raw history / evidence set / missing-information state / provenance / uncertainty |
| **Policy** | fixed heuristic / prompted agent / planner / learned policy / RL |
| **Budget** | retrieval calls / retrieved tokens / latency / monetary or energy cost |
| **Base model** | reasoning capability / tool-use capability / context window / model family |

A headline gain is not automatically evidence for the `policy` axis if the operation set, budget, or base model also changed.

## Retention and correction policy

- Keep every accepted canonical paper record.
- Keep per-paper Markdown when it adds researcher-facing explanation beyond the JSON record.
- Keep compact nested daily run logs as provenance; do not expose them as the main reading feed.
- Keep every weekly and monthly compaction file even after it ages out of the primary navigation.
- Keep one yearly report per sufficiently covered calendar year; finalized yearly reports are the permanent long-term public archive.
- README and `digests/README.md` use the attention hierarchy: recent month by week, recent quarter by month, all years by year.
- Correct upward: if a paper's classification, evidence, or importance changes enough to alter a weekly/monthly/yearly conclusion, revise the affected compaction.
- Do not preserve an old narrative merely for consistency. Rolling reports should change their thesis when new evidence falsifies it.

The goal is **lossy compression of repetition, not loss of disagreement, provenance, or uncertainty**.