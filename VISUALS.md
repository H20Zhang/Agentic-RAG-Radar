# Visual Explainer Protocol

Every accepted paper should have **one compact conceptual diagram** whose job is to make the paper's research delta understandable in roughly 10 seconds.

The diagram is an **AI-generated conceptual explainer**, not a reproduction of the paper's original figure. It should reflect our research interpretation and must not imply details that were not verified.

## One visual, one question

Choose the visual type from the paper's actual contribution:

| Paper type | Best visual | Core question the visual must answer |
|---|---|---|
| **Method / system** | Agent control loop | What does the agent observe, decide, retrieve, update, and repeat? |
| **Retrieval interface** | Operation / state diagram | What retrieval operations replace or augment fixed top-k, and what state drives the next action? |
| **Learning / RL** | Trajectory-to-policy diagram | What trajectory is optimized, what signal trains the policy, and what behavior changes at inference? |
| **Benchmark / analysis** | Evidence or failure map | What capability/failure is isolated, compared with what, and under which evaluation axis? |
| **Survey / SoK** | Taxonomy map | What are the major design axes and where do representative methods sit? |

Do **not** force every paper into a generic architecture diagram.

## Required semantic structure

For method papers, the default visual grammar is:

```text
User / Query
    ↓
Agent State / Plan
    ↓
[DECISION POINT introduced or changed by the paper]
    ↓
Retrieval / Search / Tool Operation
    ↓
Evidence / Observation
    └──────── feedback ────────→ Agent State
    ↓
Answer / Stop
```

The diagram should make four things visually explicit whenever applicable:

1. **Prior/static behavior** — what a conventional RAG pipeline would do.
2. **Research delta** — the control point, representation, interface, or policy introduced by the paper.
3. **Feedback/state** — what information changes the next retrieval decision.
4. **Stopping/output** — how the loop terminates or produces the final context/answer.

## Diagram constraints

- Prefer **Mermaid** inside the paper Markdown for GitHub-native rendering, diffability, and easy correction.
- Keep the main diagram to roughly **5–9 semantic nodes**. If it needs 15 boxes, the abstraction is probably wrong.
- Labels should describe operations, not implementation trivia.
- Highlight the paper's actual delta with text such as `NEW`, `learned`, `adaptive`, or `stateful`; do not rely on color alone.
- Use dashed/annotated branches for baselines or optional paths rather than mixing them into the main loop.
- Put quantitative results in prose unless one number is essential to understanding the mechanism.
- Never invent an edge, state variable, retriever, training signal, or component because it makes the picture cleaner.

## Required caption

Every diagram must be followed by two short lines:

- **What to notice:** the single most important mechanism/delta shown in the diagram.
- **Compared with:** the nearest static or prior method family that makes the delta meaningful.

If the visual is based only on abstract-level evidence, say so explicitly. When full text has been checked, the visual may be upgraded.

## Weekly / monthly visuals

Compaction reports may include one higher-level visual when it adds value:

- **Weekly:** a cluster/tension map of the week's research deltas.
- **Monthly:** a field map showing which control points or method families are growing, converging, or weakening.

These synthesis visuals must be generated from canonical paper records and evidence notes, not by recursively visualizing prior summaries.
