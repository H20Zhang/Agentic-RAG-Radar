# Research Compaction Protocol

Agentic RAG Radar uses a research-memory hierarchy, not an append-only feed. Compaction removes repetition while preserving disagreement, provenance, negative results, cost, and causal uncertainty. The Daily Agent is the sole writer; separate weekly/monthly writers remain disabled.

## Evidence hierarchy

| Level | Persistent artifact | Purpose | Required retention |
|---|---|---|---|
| **L0 · Canonical** | `data/papers/*.json` + paired `papers/*` notes | Identity, facts, evidence, provenance, interpretation | links, full-text status, costs, limits, corrections |
| **L1 · Closed ISO week** | `digests/weekly/YYYY-Www.md` | Local direction change and disagreement | negative boundaries, competing explanations |
| **L2 · Closed month** | `digests/monthly/YYYY-MM.md` | Rebuild the field model from primary evidence | weakening claims, reinterpretations, open problems |
| **L3 · Year** | `digests/yearly/YYYY.md` | Durable shifts and evidence standards | changes of mind, failed ideas, next-year questions |

Candidate states and source failures stay in ignored private run artifacts or agent memory. The public repository contains no Daily Agent run logs; accepted outcomes persist in canonical projections, closed digests, and atomic commit history.

## Rolling versus closed periods

The root README maintains exact inclusive rolling 7-day and 30-day windows, synthesized from accepted canonical records and deep notes whose `radar_published_at` falls inside the window and is no later than the exact synthesis cutoff. Legacy publication-date chronology remains context but is **not rolling support** when Radar acceptance time is unknown. The displayed window and synthesis time are explicit.

On the first successful run after Monday 00:00 local time, create the immutable digest for the previous complete ISO week if absent. On the first successful run of a new month, create the previous complete calendar-month digest if absent. Use idempotent period identities; a retry may not create duplicates. A current open month/year may be labeled rolling, never complete.

Older digests remain reachable even when they leave primary navigation. Time is a projection, not the only archive key.

## Non-recursive synthesis

A compaction must answer:

> What changed, compared with what, how strong is the evidence, and what should a researcher design differently?

Weekly and monthly writers re-read canonical JSON and deep notes. Weekly prose may locate sources but never becomes evidence for a monthly claim. A paragraph per paper is not compaction. Similar names, co-occurrence, or release counts are not trends.

Each rolling or closed direction states:

`new_signal | reinforced | revised | no_material_change → supporting accepted identities → confidence → research-design implication`

One accepted work can produce `new_signal`; a durable direction requires independent support.

## Weekly contract

A closed week contains:

1. exact ISO-week dates and synthesis time;
2. one falsifiable week thesis;
3. 1–3 direction changes with accepted supporting identities;
4. strongest tension, negative result, or alternative explanation;
5. evidence audit covering coverage, baselines, interface/harness, state, realized resources, and full-text status;
6. minimal reading order and open questions.

Adjacent older context may interpret the week but is labeled and not counted as a weekly acceptance.

## Monthly contract

A closed month re-evaluates the field at one higher abstraction level: month thesis, evidence-gated field clusters, older anchors reinterpreted where necessary, few defining works, one causal tension, evidence audit, 3–5 open problems, and minimal reading path. It is rewritten from canonical evidence, not assembled from weekly paragraphs.

## Yearly contract

A year is not twelve monthly summaries. It asks what survived: start→end change, durable shifts, defining evidence, ideas that weakened, year-level evidence audit, 3–7 open problems, and a minimal reading path. Historical years require adequate coverage; otherwise do not create them.

## RAG attribution lens

Before synthesizing a strong retrieval claim, compare:

`evidence coverage × corpus observability × interface resolution × environment state × harness/delivery × agent state × policy × realized resources × model × training protocol`

Evidence validity precedes policy quality. Adaptivity has a location. Cost spans offline construction/update and online calls, inspected tokens, latency, controller compute, and model work. A headline gain is not policy evidence when interface, harness, state, evidence, model, or budget moved unmatched.

## Map and correction propagation

Every accepted v2 record has `map_delta`. `early_signal` may affect period prose but not durable map nodes. `reinforces` needs independent evidence; `revises`, `splits`, and `retires` require a claim-level old→new explanation and smallest reversible edit.

Corrections propagate upward. If identity, evidence, baseline, cost, or classification changes a root period claim or closed digest, revise every affected artifact from canonical evidence. Preserve original time fields and record the correction; do not preserve a known-wrong narrative for consistency.

The goal is lossy compression of repetition, never loss of provenance, disagreement, or uncertainty.
