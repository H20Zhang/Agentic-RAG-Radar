# Agentic RAG Research Map

**中文** | [English](README.en.md) · [返回首页](../README.md) · [Research Library](../library/README.md)

与其按 method name 做 taxonomy，更有用的是围绕**现在仍然活着的研究问题**组织领域。每个问题都应该同时有：当前判断、结论失效的 boundary、以及会改变这张 map 的 decisive experiment。

## 六个 Live Research Questions

| 问题 | 当前判断 | 中文深入 |
|---|---|---|
| **Adaptivity 应该放在哪里？** | 能从 corpus-visible signal 预先决定的 control 可以 compile；依赖新 evidence 的 decision 必须 result-conditioned；D2 新增了 evidence sufficiency 驱动 breadth/depth routing 的受控信号。 | [进入](zh/adaptivity-placement.md) |
| **Evidence 什么时候 materialize？** | 稳定 corpus/固定 evidence unit 倾向预处理；dynamic corpus / query-dependent granularity 可能值得保留 raw，query 到来后再定位。 | [进入](zh/evidence-materialization.md) |
| **什么 state 值得持久化？** | State 的价值取决于 future reuse × recoverability × reacquisition cost，而不是 size 本身；StateMem 与 EvoWiki 共同表明，保留历史和解析 operative state 可以分开，validity 可在 answer time 组装或 write time 物化。 | [进入](zh/state-persistence.md) |
| **Retrieval 应如何暴露 corpus？** | “Retriever quality”太粗；VisDocAgentBench 与 CTIFoundry 进一步把 search / resolve / traverse / inspect / read 变成显式 evidence-path operation，但必须匹配 backend、harness 与预算。 | [进入](zh/interface-resolution.md) |
| **到底应该 learn 什么？** | Retrievers、query policy、operation policy、recovery、budget allocation、training distribution 是不同 learning target。 | [进入](zh/learning-targets.md) |
| **什么样的 evaluation 才 causal？** | Evidence availability、capability coverage、backend、interface、state、harness、resources 都匹配后，才能给 policy/component 归因；ToolScout 说明失败可能在 planning 前已经发生。 | [进入](zh/causal-evaluation.md) |

## Cross-Cutting Causal Lens

`substrate/evidence coverage × pre-retrieval observability × interface resolution × environment state × harness × retained agent state × policy × realized resources × base model × training protocol × historical baseline`

当前最值得记住的系统张力是：

> **precompute / materialize / retain ↔ defer / localize / reacquire**

删掉一个 index、search call 或 prompt token，只有在相同 answer/evidence quality 下，被挪走的工作**没有在别处重新出现**，才是真正的 efficiency win。

## Canonical Categories

这些 category 仍然用于 ownership/indexing，但不应该主导读者对 field 的认知。

| Category | 核心问题 | English deep page |
|---|---|---|
| Planning & Query Formulation | 哪些 decision 能在 evidence 前做，哪些必须 observation 后重规划？ | [English](planning-query-formulation.md) |
| Retrieval & Tool Use | Agent 应控制哪些 information-access operation 与 evidence resolution？ | [English](retrieval-tool-use.md) |
| Iterative Reasoning & Verification | 哪些 state 应驱动 continue / redirect / recovery / verification / stop？ | [English](iterative-reasoning-verification.md) |
| Multi-Agent & Orchestration | specialization 什么时候值得 coordination cost？ | [English](multi-agent-orchestration.md) |
| Learning & Optimization | information-acquisition loop 的哪一部分应该 learned？ | [English](learning-optimization.md) |
| Evaluation & Analysis | 怎么隔离真正造成 gain 的变量？ | [English](evaluation-analysis.md) |

Orthogonal tags 仍由 [`../taxonomy.yaml`](../taxonomy.yaml) 管理；Research Map 只在 evidence 改变时更新，不因为 paper count 增加而扩张。
