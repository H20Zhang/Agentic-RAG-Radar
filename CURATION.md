# Daily Curation Protocol

This repository is maintained as a **research radar**, not a keyword dump. Daily maintenance should optimize for **high recall during discovery, high precision at publication, and explicit skepticism before synthesis**.

## Independent roles

Each run should use independent parallel roles whenever the execution environment supports them. Roles should form judgments separately before the editor synthesizes them.

| Role | Responsibility | Failure it should prevent |
|---|---|---|
| **Discovery** | Search a broad overlapping recent window across arXiv and other high-signal scholarly sources; expand beyond the literal phrase `agentic RAG`. | Missing papers because authors use different terminology. |
| **Inclusion Judge & Taxonomy** | Decide whether retrieval is genuinely agent-controlled and assign the primary category + orthogonal tags. | Scope creep into ordinary RAG or generic agents. |
| **Research Reader** | Read deeply enough to identify the actual control loop, nearest design point, evidence, limitations, and the one mechanism worth teaching. | Abstract paraphrases masquerading as research analysis. |
| **Visual Explainer** | Convert the verified mechanism into one original GPT-image-gen teaching figure with an auditable grounding brief. | Decorative, dashboard-like, or paper-copy visuals that do not improve understanding. |
| **Evidence Auditor / Skeptical Reviewer** | Challenge inclusion, novelty, importance, baseline quality, resource matching, historical prior art, unsupported claims, duplicate versions, links, and visual overstatement. | Inflated “agentic” causal or novelty claims. |
| **Research Editor** | Produce the final paper card / compaction only after seeing the independent judgments. | Verbosity, paper-by-paper concatenation, and conclusions without consequences. |

The skeptical role should actively try to falsify the proposed interpretation.

## Discovery policy

Use an overlapping lookback window rather than a strict calendar-day query. Search beyond naming conventions: agentic/adaptive/active retrieval, planning, decomposition/reformulation, iterative/interleaved search, verifier-guided retrieval, tool-using RAG, GraphRAG agents, retrieval policy learning, retrieval budgeting/stopping, and agentic information seeking.

Deduplicate by canonical paper identity, preferably arXiv ID.

## Inclusion gate

Ask four questions in order:

1. Is external retrieval/search/context acquisition substantive?
2. Does an agent/controller/policy materially control retrieval behavior?
3. Is that control part of the research contribution rather than implementation glue?
4. Compared with the nearest **static, adaptive, and historical** design point where relevant, is the claimed delta identifiable?

If (1)–(3) are not clearly yes, reject or hold. A paper can be highly relevant yet low importance.

## Analysis standard

For every accepted paper, record TL;DR, Problem, Core Idea, Agent Loop, Retrieval Design, Compared to What, Evidence, Why It Matters, Limitations/Questions, AI Confidence, and accurate provenance/full-text status.

Do not claim experimental superiority from an abstract alone.

## Causal + novelty attribution checklist

Agentic RAG papers often change multiple variables at once. Before attributing a gain to a policy, reason over:

`substrate × operation set × state × policy × budget × base model × historical baseline`

The first six axes address causal attribution. The last asks whether the claimed control pattern has meaningful classical IR/QA antecedents and, if so, what modern models/interfaces/learning/scaling actually add.

Useful checks include:

- same retrieval primitive, fixed vs adaptive policy;
- **adaptive vs adaptive** controller comparisons when available;
- separate retrieval-call, context/token, latency, and controller/probe overhead accounting;
- explicit state vs raw history/reasoning trace;
- strong lexical/sparse as well as dense baselines;
- component ablations that isolate interface, state, routing, budget allocation, and learning;
- historical re-implementations when novelty rests on query refinement, verification, or closed-loop retrieval.

Negative results and baseline reversals should be preserved.

## GPT-image visual standard

Every accepted paper must have a `visual_explainer` contract and grounding brief under `assets/visuals/prompts/`.

**GPT-image-gen is preferred.** Follow [`VISUALS.md`](VISUALS.md): one named paper per generation call, one research question, minimal image text, original conceptual explanation, no paper-figure copying, no repo dashboards or multi-paper status graphics.

Status meanings:

- `pending` — record + grounding brief exist; a QC-passing binary asset has not yet been committed;
- `needs_regeneration` — existing visual is invalid/outdated;
- `generated` — the exact `image_path` exists in GitHub and required paper/README embeds are synchronized.

Do not assume PNG; the canonical `image_path` is authoritative and WebP is preferred for web-facing assets.

Existing pending visuals remain the priority backfill queue before decorative/synthesis graphics.

## Scoring

`relevance ∈ [0,1]` measures topical fit. `importance ∈ {1,...,5}` measures expected research significance.

- **5 — Field-shaping:** changes an abstraction, benchmark, or dominant direction with unusually strong evidence.
- **4 — Important:** clear reusable idea or strong evidence likely to influence follow-up work.
- **3 — Solid:** meaningful contribution but narrower delta or evidence.
- **2 — Incremental:** valid but limited novelty/evidence/scope.
- **1 — Peripheral:** included for completeness.

Do not reward recency or fashionable naming.

## Update policy

For every accepted paper:

1. create/update canonical JSON;
2. create/update researcher-facing paper card;
3. create/update visual grounding brief and exact asset status/path;
4. refresh README Latest/Notable and relevant research-problem category when the field view changes;
5. propagate meaningful corrections upward into weekly/monthly/yearly compactions.

Each run writes one compact archival provenance log under `runs/daily/YYYY/MM/DD.md`. It records accepted/deferred candidates, meaningful corrections, visual/workflow status, and compaction actions without repeating full paper notes.

Never fabricate links, benchmark results, full-text analysis, or visual components. See [`COMPACTION.md`](COMPACTION.md), [`VISUALS.md`](VISUALS.md), and [`runs/README.md`](runs/README.md).
