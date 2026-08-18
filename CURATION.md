# Daily Curation Protocol

This repository is maintained as a **research radar**, not a keyword dump. Daily maintenance should optimize for **high recall during discovery, high precision at publication, and explicit skepticism before synthesis**.

## Independent roles

When the environment supports it, roles should form judgments independently before the editor synthesizes them.

| Role | Responsibility | Failure it should prevent |
|---|---|---|
| **Discovery** | Search a broad overlapping window across arXiv and other high-signal scholarly sources; expand beyond the literal phrase `agentic RAG`. | Missing papers because authors use different terminology. |
| **Inclusion Judge & Taxonomy** | Decide whether external information acquisition is genuinely controlled by an agent/policy and assign category/tags. | Scope creep into ordinary RAG or generic agents. |
| **Research Reader** | Read deeply enough to identify the actual control loop, nearest design point, evidence, limitations, and one mechanism worth teaching. | Abstract paraphrase masquerading as research analysis. |
| **Visual Explainer** | Turn the grounded mechanism into one original teaching figure. | Decorative/dashboard visuals or invented mechanisms. |
| **Evidence Auditor / Skeptical Reviewer** | Challenge novelty, causal attribution, baseline quality, resources, historical prior art, links, duplicate versions, and visual overstatement. | Inflated “agentic” claims. |
| **Research Editor** | Publish only after seeing the independent judgments. | Verbosity and conclusions without consequences. |

The skeptical role should actively try to falsify the proposed interpretation.

## Discovery policy

Use an overlapping lookback window rather than a strict calendar-day query. Search beyond naming conventions: agentic/adaptive/active retrieval, planning, decomposition/reformulation, iterative/interleaved search, verifier-guided retrieval, tool-using RAG, GraphRAG agents, retrieval policy learning, retrieval budgeting/stopping, agentic information seeking, and adjacent memory/search work where external acquisition is controlled at query time.

Deduplicate by canonical paper identity, preferably arXiv ID.

## Inclusion gate

Ask four questions in order:

1. Is external retrieval/search/context acquisition substantive?
2. Does an agent/controller/policy materially control whether, what, where, how, or how much information is acquired?
3. Is that control part of the research contribution rather than implementation glue?
4. Compared with the nearest **static, adaptive, and historical** design point where relevant, is the claimed delta identifiable?

If (1)–(3) are not clearly yes, reject or hold. A paper can be highly relevant yet low importance.

## Analysis standard

For every accepted paper, record TL;DR, Problem, Core Idea, Agent Loop, Retrieval Design, Compared to What, Evidence, Why It Matters, Limitations/Questions, AI Confidence, and accurate provenance/full-text status.

Do not claim experimental superiority from an abstract alone. Preserve negative results and the strongest alternative explanation.

## Causal + novelty attribution checklist

A result should be interpreted along the **information path**, not only by the method name:

`substrate/evidence coverage × pre-retrieval corpus observability × corpus boundary/interface resolution × environment retrieval state × harness/delivery × agent state × policy × realized resources × base model × training distribution/protocol × historical baseline`

This is a causal checklist, not a request to create more taxonomy axes.

Useful checks include:

- **Evidence validity first:** can the external corpus/environment actually support the target answer? Positive final-answer reward can be spurious when evidence is absent and the model answers parametrically.
- **Adaptivity placement:** compare what can be compiled before retrieval from corpus-visible signals with what genuinely requires result-conditioned interaction.
- **Same information surface:** hold backend tuning, surfaced depth, candidate admissibility, inspection/read affordances, environment state, and harness/delivery fixed before crediting policy.
- **Matched realized resources:** report calls, inspected/retrieved tokens, latency, controller/probe cost, offline construction/update cost, and query-time cost—not nominal caps alone.
- **Learning validity:** vary reward/credit assignment separately from corpus coverage, tool format, rollout freshness/off-policy degree, task-generation distribution, teacher/verifier information, and search budget.
- **Strong alternatives:** include lexical/sparse as well as dense baselines, adaptive-vs-adaptive controllers, historical retrieve→verify→reformulate precedents, and matched one-search versus multi-round controls when relevant.

A headline gain is not evidence for `policy` if the system also changed what evidence existed, what the controller could observe, how results were delivered, or how much offline/online computation was spent.

## GPT-image visual standard

Every accepted paper must have a `visual_explainer` contract and grounding brief under `assets/visuals/prompts/`.

Prefer **GPT-image-gen**. Follow [`VISUALS.md`](VISUALS.md): one named paper per generation call, one research question, minimal image text, original conceptual explanation, no paper-figure copying, no repo dashboards or multi-paper status graphics.

Status meanings:

- `pending` — record + grounding brief exist; a QC-passing binary asset has not yet been committed;
- `needs_regeneration` — an existing visual is invalid/outdated;
- `generated` — verified PNG master + same-resolution WebP exist and all required embeds/explanations are synchronized.

Existing pending/invalid visuals remain the priority queue before decorative or synthesis graphics.

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

1. create/update canonical JSON and researcher-facing paper note;
2. create/update the grounded visual brief and exact asset status/path;
3. refresh README Latest and the relevant research-problem page when the field view changes;
4. propagate meaningful corrections upward into weekly/monthly/yearly compactions;
5. write one compact archival run log under `runs/daily/YYYY/MM/DD.md`.

Never fabricate links, benchmark results, full-text analysis, or visual components. See [`COMPACTION.md`](COMPACTION.md), [`VISUALS.md`](VISUALS.md), and [`runs/README.md`](runs/README.md).
