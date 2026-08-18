# Research Compaction Protocol

Agentic RAG Radar treats curation as a **research-memory hierarchy**, not an append-only stream of paper summaries. Compaction should preserve disagreement, evidence status, and causal uncertainty while removing repeated detail.

## Levels

| Level | Persistent artifact | Purpose | What must not be lost |
|---|---|---|---|
| **L0 · Paper records** | `data/papers/*.json` + `papers/*` | Canonical facts, provenance, classification, paper-level interpretation, visual grounding. | links, evidence status, uncertainty, corrections |
| **L0-log · Daily runs** | `runs/daily/YYYY/MM/DD.md` | Compact history of accepted/deferred/corrected work. | decision history, edge cases, workflow failures |
| **L1 · Weekly** | `digests/weekly/YYYY-Www.md` | Identify local research deltas, disagreements, and reading priority. | negative results, competing explanations |
| **L2 · Monthly** | `digests/monthly/YYYY-MM.md` | Rebuild the field map and causal model. | weakening claims, open problems, reinterpreted anchors |
| **L3 · Yearly** | `digests/yearly/YYYY.md` | Preserve only durable shifts and evidence standards. | changes of mind, failed ideas, next-year questions |

## Public time hierarchy

The reader-facing archive deliberately loses temporal resolution as work ages:

- **Recent ~1 month → weekly.**
- **Recent ~1 quarter → monthly.**
- **All sufficiently covered years → yearly.**

Lower-level files are never deleted merely because they age out of primary navigation. The current year may have an explicitly **rolling** report. Never present a few selected anchors as complete historical-year coverage.

## Editorial principle

A compaction succeeds only if it answers questions a chronological list cannot:

> **So what changed? Compared with what? How strong is the evidence? What should a researcher do differently?**

The report should be shorter than its sources but harder to write. A paragraph per paper is not compaction.

## Daily run-log policy

Daily logs exist for audit, not as another reader-facing feed. Record only material discovery changes, newly accepted papers with one-line reasons, important deferred/rejected candidates, meaningful corrections, visual/workflow status, and compaction actions. Do not duplicate full TL;DRs or experiment tables.

## Weekly compaction

A weekly report should contain:

1. **Week thesis** — one falsifiable statement about what changed.
2. **1–3 durable shifts** — clusters defined by actual control point/research delta.
3. **Most important papers** — only papers that change an abstraction, method family, benchmark, or evidence base; each answers `delta → compared with → evidence → so what`.
4. **Tension / disagreement** — the strongest alternative explanation or negative result.
5. **Evidence audit** — baseline quality, evidence coverage, interface/harness matching, realized resources, and full-text status.
6. **Reading order + open questions** — the smallest sequence that teaches the change.

Adjacent-context papers may be used when needed to interpret the week's delta, but must be labeled rather than silently counted as weekly papers.

## Monthly compaction

A monthly report operates one abstraction level higher. During an open month it may be **rolling**, but it must be rewritten when new evidence changes the map rather than appended chronologically.

It should contain a month thesis, field-map clusters, older anchors reinterpreted where useful, the few most important papers, one core causal tension, an evidence audit, 3–5 open problems, and a minimal reading path.

Weekly reports may be used as an index only. Load-bearing claims must be re-grounded in canonical records and source/full-paper notes.

## Yearly compaction

A yearly report is not twelve monthly summaries concatenated. It asks **what actually survived the year?** A finalized yearly report should contain a year thesis, start→end change, durable shifts, defining papers, ideas that weakened, year-level evidence audit, 3–7 open problems, and a minimal reading path.

The current year may be rolling. Historical yearly reports require adequate coverage; otherwise do not create them.

## Multi-role challenge before synthesis

When independent roles are supported:

| Role | Job | What it should challenge |
|---|---|---|
| **Clusterer / Field Mapper** | Group by actual research delta and propose a field map. | keyword similarity, fashionable naming |
| **Evidence Auditor** | Compare evidence coverage, baselines, calls/tokens/latency, ablations, and negative results. | causal over-attribution |
| **Trend Skeptic** | Construct the strongest alternative explanation. | three papers being mistaken for a paradigm shift |
| **Research Editor** | Write after seeing the independent analyses. | paper-by-paper concatenation |

Prefer **one important tension** over five weak trends.

## Factorized evaluation lens

Agentic retrieval results frequently change several variables simultaneously. Compactions should reason over:

`substrate/evidence coverage × pre-retrieval corpus observability × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state × policy × realized resources × base model × training distribution/protocol × historical baseline`

This is a causal checklist, not a taxonomy.

Three ordering rules now matter:

1. **Evidence validity precedes policy quality.** If answer-bearing evidence is absent from the external environment, a positive final-answer reward may reflect parametric knowledge rather than successful retrieval.
2. **Adaptivity has a location.** Compare what can be compiled before evidence retrieval with what genuinely requires result-conditioned interaction; `number of rounds` is not itself a capability metric.
3. **Cost spans offline and online work.** Index/memory construction, corpus enrichment, controller/probe compute, retrieval calls, inspected tokens, latency, and query-time model calls belong in the same systems accounting.

A headline gain is not automatically evidence for `policy` if evidence coverage, corpus observability, interface, state, harness, budget, or supervision also changed.

## Retention and correction policy

- Keep every accepted canonical paper record and useful paper note.
- Keep compact nested daily run logs as provenance, not primary browsing surfaces.
- Keep every weekly/monthly compaction even after it ages out of primary navigation.
- Keep one yearly report per sufficiently covered calendar year; the current year may remain rolling.
- README and `digests/README.md` use the attention hierarchy: recent month by week, recent quarter by month, sufficiently covered years by year.
- Correct upward: if a paper's classification, evidence, importance, or a newly discovered baseline changes a weekly/monthly/yearly conclusion, revise the affected compaction.
- Do not preserve an old narrative merely for consistency.

The goal is **lossy compression of repetition, not loss of disagreement, provenance, or uncertainty**.
