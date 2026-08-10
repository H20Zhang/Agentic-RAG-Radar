# Daily Curation Protocol

This repository is maintained as a **research radar**, not a keyword dump. The daily updater should optimize for high recall during discovery and high precision at publication time.

## Multi-agent workflow

Each daily run should use independent parallel research roles whenever the execution environment supports subagents or parallel tasks.

| Role | Responsibility | Failure it should prevent |
|---|---|---|
| **Discovery** | Search a broad overlapping recent window across arXiv and other high-signal scholarly sources; expand beyond the literal phrase `agentic RAG`. | Missing papers because authors use different terminology. |
| **Relevance & Taxonomy** | Independently decide whether retrieval is genuinely agent-controlled and assign the primary category + orthogonal tags. | Scope creep into ordinary RAG or generic agents. |
| **Research Reader** | Read the paper deeply enough to extract the actual control loop, closest comparison, evidence, limitations, and the one mechanism that deserves a visual explainer. | Abstract paraphrases masquerading as research analysis. |
| **Skeptical QC** | Challenge inclusion, importance, classification, unsupported claims, duplicate versions, broken/unverified links, and misleading visual simplifications. | LLM agreement bias and inflated novelty claims. |

These roles should work independently before synthesis where practical. The QC role should not simply summarize the other roles.

## Discovery policy

Use an overlapping lookback window rather than a strict calendar-day query. Candidate queries should cover terms such as:

- agentic RAG / agentic retrieval / agentic search
- adaptive or active retrieval
- retrieval planning / query decomposition / query reformulation
- iterative search / interleaved retrieval and reasoning
- verifier- or critic-guided retrieval
- tool-using RAG / retrieval routing
- GraphRAG agents / graph retrieval agents
- retrieval policy learning / RL for retrieval
- agentic information seeking

Deduplicate by canonical paper identity (prefer arXiv ID when available), not title string alone.

## Inclusion gate

Ask four questions in order:

1. Is external retrieval/search/context acquisition a substantive component?
2. Does an agent/controller/policy materially control retrieval behavior?
3. Is that control part of the research contribution rather than implementation glue?
4. Compared with the nearest static/adaptive baseline, is the claimed delta identifiable?

If (1)-(3) are not clearly yes, reject or hold for review.

## Analysis standard

For accepted papers, record:

- **TL;DR:** one-sentence research delta.
- **Problem:** the concrete limitation in prior systems.
- **Core Idea:** the mechanism or abstraction introduced.
- **Agent Loop:** e.g. `Plan → Search → Inspect → Reformulate → Search → Verify → Answer`.
- **Retrieval Design:** available retrieval operations, granularity, routing, state, and stopping behavior.
- **Compared to What:** nearest method families and the actual delta.
- **Evidence:** datasets, metrics, baselines, key ablations, and what the experiments do *not* establish.
- **Why It Matters:** importance relative to existing agentic RAG work, not a contribution restatement.
- **Limitations / Questions:** 1–3 assumptions or missing tests that could change the conclusion.
- **AI Confidence:** high / medium / low.

Do not claim experimental superiority from an abstract alone. Set `provenance.full_text_checked` accurately.

## Visual explainer standard

Every accepted paper should have **one conceptual visual explainer** in its researcher-facing Markdown, following [`VISUALS.md`](VISUALS.md). The diagram should answer the single question that makes the paper easiest to understand: agent control loop for method papers, operation/state diagram for retrieval-interface work, trajectory-to-policy diagram for learning papers, evidence/failure map for analysis papers, or taxonomy map for surveys.

Prefer GitHub-native Mermaid so diagrams stay text-diffable and easy to correct. Keep the main diagram compact and explicitly mark the research delta rather than reproducing implementation detail. Follow it with **What to notice** and **Compared with**. If only the abstract has been checked, the visual must be labeled as abstract-grounded rather than presented as a verified reconstruction of the full method.

## Scoring

`relevance ∈ [0,1]` measures topical fit. `importance ∈ {1,...,5}` measures estimated research significance. A paper can be highly relevant and low importance.

Suggested importance interpretation:

- **5 — Field-shaping:** changes the abstraction, benchmark, or dominant research direction.
- **4 — Important:** clear reusable idea or strong evidence likely to influence follow-up work.
- **3 — Solid:** meaningful contribution but narrower delta or evidence.
- **2 — Incremental:** valid but limited novelty, evidence, or scope.
- **1 — Peripheral:** included for completeness; little expected research impact.

## Update policy

Prefer small auditable diffs. Add or correct canonical records under `data/papers/`, generate researcher-facing notes under `papers/` when they add useful analysis, include the visual explainer, and refresh README latest/notable views. **Do not create one Markdown digest per day.** Daily output is an ingestion layer; durable human-facing history is compacted weekly and monthly under `digests/`.

Never silently fabricate code/project links, benchmark results, full-text analysis, or diagram edges/components. See [`COMPACTION.md`](COMPACTION.md) for weekly/monthly synthesis rules, including the requirement that monthly reports re-check canonical records rather than recursively trusting summaries.
