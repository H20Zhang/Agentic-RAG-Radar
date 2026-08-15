# Design Anchors

These are **design points, not a ranking**. The goal is to expose the few abstractions needed to understand the current Agentic RAG control stack.

| Paper | Design point | Research card |
|---|---|---|
| **A-RAG** | model-controlled retrieval operation hierarchy | [2602.03442](2602.03442.md) |
| **Direct Corpus Interaction (DCI)** | raw-corpus interface resolution: grep/find/read instead of fixed top-k evidence delivery | [2605.05242](2605.05242.md) |
| **RISE** | retrieval as construction of a bounded persistent interaction space | [2606.06880](2606.06880.md) |
| **DR-DCI** | retrieval as an agent-callable action that dynamically expands durable workspace state | [2606.14885](2606.14885.md) |
| **RARG** | relevance as an execution prior inside direct corpus interaction | [2607.24223](2607.24223.md) |
| **S2G-RAG** | explicit sufficiency / missing-information state | [2604.23783](2604.23783.md) |
| **Critic-R** | process feedback from reasoning into query repair and retriever learning | [2606.00590](2606.00590.md) |
| **GrepSeek** | learned policy over a direct-corpus shell interface | [2605.29307](2605.29307.md) |
| **Is Grep All You Need?** | harness and evidence-delivery path as retrieval-evaluation confounders | [2605.15184](2605.15184.md) |
| **Know Before You Fetch** | retrieval amount as an explicit multi-resource control decision | [2606.29959](2606.29959.md) |

## How to read the anchors

A useful progression is:

`information need → corpus interface/boundary → persistent evidence workspace → explicit evidence state → adaptive/learned control → resource/harness-aware evaluation`

For the interface lineage, read **A-RAG → DCI → RISE → DR-DCI → RARG**. The sequence corrects a false binary: semantic relevance and direct interaction are not opposing paradigms. DCI exposes the cost of a low-resolution top-k interface; RISE/DR-DCI restore scalable boundaries; RARG reintroduces relevance as guidance inside the interaction space rather than as the final evidence bottleneck.

For learning, **Critic-R → GrepSeek** separates two feedback directions: use reasoning feedback to improve retrieval versus learn the corpus-operation policy itself. For evaluation, **Is Grep All You Need? → Know Before You Fetch** makes harness/delivery and realized resource use explicit causal variables.

## Caveat

Anchors are promoted only when they change the field map or the evidence bar. They should not become an exhaustive paper index; category pages and canonical records hold the broader archive.
