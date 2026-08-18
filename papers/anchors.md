# Design Anchors

These are **design points, not a ranking**. The goal is to expose the few abstractions needed to understand the current Agentic RAG control stack.

| Paper | Design point | Research card |
|---|---|---|
| **SIRA** | corpus-aware **pre-retrieval action compilation** from model priors + index-visible statistics | [2605.06647](2605.06647.md) |
| **A-RAG** | model-controlled retrieval operation hierarchy | [2602.03442](2602.03442.md) |
| **Direct Corpus Interaction (DCI)** | raw-corpus interface resolution: grep/find/read instead of fixed top-k evidence delivery | [2605.05242](2605.05242.md) |
| **RISE** | retrieval as construction of a bounded persistent interaction space | [2606.06880](2606.06880.md) |
| **DR-DCI** | retrieval as an agent-callable action that dynamically expands durable workspace state | [2606.14885](2606.14885.md) |
| **RARG** | relevance as an execution prior inside direct corpus interaction | [2607.24223](2607.24223.md) |
| **ReFind** | raw-history fidelity + substrate-native result-conditioned search instead of mandatory pre-built semantic memory | [2608.12888](2608.12888.md) |
| **S2G-RAG** | explicit sufficiency / missing-information state | [2604.23783](2604.23783.md) |
| **SGR-Bench** | external retrieval state as a first-class evaluation object | [2605.22219](2605.22219.md) |
| **Training Protocols** | corpus answerability + training protocol as prerequisites for causal search-agent RL claims | [2605.27881](2605.27881.md) |
| **Is Grep All You Need?** | harness and evidence-delivery path as retrieval-evaluation confounders | [2605.15184](2605.15184.md) |

## How to read the anchors

A useful progression is:

`pre-retrieval observability → compiled action / corpus interface → evidence observation → result-conditioned control → external + internal state → resource-aware evaluation`

The central new tension is **where adaptivity should live**. SIRA asks what can be decided before evidence is read; DCI/RISE/RARG ask which local operations survive the retrieval boundary; ReFind shows that some workloads still need new queries conditioned on evidence revealed by earlier searches.

The interface lineage **A-RAG → DCI → RISE → DR-DCI → RARG** remains important, but it is no longer the whole map. ReFind adds the memory-side question of whether structure should be precomputed at all, while SIRA adds the opposite possibility that richer corpus observability can compile away runtime exploration.

**SGR-Bench adds a separate state boundary:** the external source can be in the wrong filter/scope/view state even when the agent's internal evidence state is coherent. **Training Protocols adds an even earlier validity boundary:** if answer-bearing evidence is absent from the retrieval environment, a positive final-answer reward may train parametric recall rather than retrieval.

## Caveat

Anchors are promoted only when they change the field map or the evidence bar. They should not become an exhaustive paper index; category pages and canonical records hold the broader archive.
