# Research Radar Editorial Standard

This is the prose contract for reader-facing Agentic RAG Radar content. It applies to Chinese/English README surfaces, Research Library pages, high-value paper notes, category arguments, and public compactions.

## Reasoning contract

Settle the research judgment before drafting:

1. **Research delta** — `previous design → changed variable → consequence`.
2. **Problem** — what still fails under the strongest reasonable existing design?
3. **Mechanism** — what actually happens in the execution/data/control flow?
4. **Closest comparison** — what is held fixed, and what still changes together?
5. **Decisive evidence** — which 1–3 results should change belief?
6. **What remains unproven** — strongest alternative explanation, mismatched resource budget, or unsupported attribution.
7. **Field-map consequence** — which placement/control/state question changes?

For Agentic RAG, explicitly ask when useful: **what is precomputed, what becomes observable only after evidence arrives, what state survives between actions, and where offline/online cost is paid**.

## Chinese-first bilingual rule

`README.md` is Simplified Chinese by default; `README.en.md` is a complete English counterpart. They are two editorial projections of one semantic judgment, not independent corpora.

Keep canonical paper titles, benchmarks, model names, metrics, protocol/tool names, and established technical terms in English when that improves precision and literature search.

Chinese entry prose must still use Chinese sentence structure. Preserve canonical names and standard acronyms where they improve search, but write connective grammar and ordinary process descriptions in Chinese when a precise expression exists; do not place English clause skeletons inside Chinese particles.

## Public entry surfaces

Root and Research Library READMEs should work like direct, curated lists: give readers the current items, map, and routes before maintenance explanation.

- Keep depth navigation compact and do not repeat its promise in prose.
- Do not add a methodology manifesto or summarize an adjacent table before and after it.
- Do not add label wrappers beyond the required `Question / Evidence / Caveat / Map / Links` contract.
- Preserve substantive expansions, but make the collapsed line identify the mechanism, evidence, or limitation rather than using a generic fold title.

## Preferred prose

- Start paragraphs with the claim, not scene-setting.
- Use concrete operations: `search`, `read`, `filter`, `materialize`, `retain`, `reacquire`, `backtrack`, rather than vague framework language.
- Compare before praising.
- Keep negative results visible when they bound the claim.
- Charge controller/oracle/reacquisition work when discussing “fewer searches” or “less context.”
- Distinguish system-level evidence from component attribution.
- One paragraph should advance one research idea.

## AI-house-style patterns to avoid

Warn on repeated sentence skeletons across nearby notes, especially:

- `真正重要的不是 X，而是 Y` / `the important thing is not X but Y`;
- repeated `the meaningful delta…`, `this matters because…`, `the strongest result…`;
- empty Chinese transitions such as `值得注意的是`, `此外`, `总的来说`;
- generic praise (`novel`, `robust`, `powerful`, `significant`, `重要`, `强大`) without evidence/comparison;
- forced three-part symmetry for rhythm;
- abstract nouns where an observable operation or state can be named;
- conclusion paragraphs that only restate the opening.

Do not ban isolated words. The target is **pattern density and loss of specificity**.

## README expansion contract

A Timeline expansion is not a mini paper note. It should explain the surviving problem, decisive evidence, strongest caveat, map consequence, and audit links without copying the deep note.

Put one Last updated / Last synthesized status directly after depth navigation and before Timeline so Timeline remains the first substantive feed. A closed Timeline summary uses the date, a short canonical label, an exact canonical Field Map axis prefix (optionally `axis → subproblem`), and the delta. Keep the complete canonical title visible as the primary-source link inside the expanded body; Chinese and English must preserve the same label, title link, and axis mapping.

## Epistemic language

Use explicit boundaries:

- paper fact: `论文报告…` / `the paper reports…`;
- curator interpretation: `这更支持整套 package，而不是单独证明 X` / `this supports the package more strongly than X`;
- open hypothesis: `下一步最有判别力的实验是…` / `the next decisive test is…`.
