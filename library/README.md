# Agentic RAG Research Library

**中文** | [English](README.en.md) · [返回首页](../README.md)

这里按**研究问题与 design tension**组织历史工作。Weekly / monthly / yearly 只回答“最近发生了什么”，不承担长期检索。

## 按 Research Problem 浏览

| 问题 | 入口 | 当前核心张力 |
|---|---|---|
| **Adaptivity placement** | [进入](../categories/zh/adaptivity-placement.md) | 哪些 search behavior 可以在 evidence 到来前 compile，哪些必须 result-conditioned？ |
| **Evidence materialization** | [进入](../categories/zh/evidence-materialization.md) | evidence unit 应在 indexing time 固定，还是 query 到来后再定位？ |
| **State persistence** | [进入](../categories/zh/state-persistence.md) | 哪些 state 值得保留，哪些丢掉后会以 reacquisition cost 回来？ |
| **Interface resolution** | [进入](../categories/zh/interface-resolution.md) | opaque top-k 够不够，还是需要 search/read/filter/navigation 等显式 interface？ |
| **Learning targets** | [进入](../categories/zh/learning-targets.md) | retriever、control、recovery、budget、task distribution 中到底应该 learn 什么？ |
| **Causal evaluation** | [进入](../categories/zh/causal-evaluation.md) | backend、interface、harness、state、model、budget 怎么分开，才能做 causal attribution？ |

## 按 Research Line 浏览

### 1. Fixed retrieval → direct interaction → query-time evidence materialization

[SIRA](../papers/2605.06647.md) → [DCI](../papers/2605.05242.md) → [ReFind](../papers/2608.12888.zh.md) → [LENS](../papers/2608.16185.zh.md)

**带走的结论：** adaptivity 与 evidence materialization 是两个不同 placement decision。SIRA 把一部分 intelligence compile 到 retrieval 前；DCI/ReFind 保留 raw substrate；LENS 进一步让 evidence boundary 本身到 query time 才 materialize。

### 2. Search loop → progress-aware control → reversible / recoverable state

[S2G-RAG](../papers/2604.23783.md) → [RAAC](../papers/2608.15191.zh.md) → [LoongReflect](../papers/2608.11967.zh.md) → [Context Compression Cost](../papers/2608.16370.zh.md)

**带走的结论：** “多搜几轮”不是 primitive。更重要的是 sufficiency/progress 如何被观察、错误 state 能否回退、被丢掉的 state 是否会以 re-query cost 的形式回来。

### 3. Retriever quality → interface/harness attribution → cross-source execution

[Pi-Serini](../papers/2605.10848.md) → [Is Grep All You Need?](../papers/2605.15184.md) → [Training Protocols](../papers/2605.27881.md) → [VAKRA](../papers/2608.12282.zh.md)

**带走的结论：** backend score、surfaced evidence、agent harness、model 与 tool budget 会强烈耦合；最终 leaderboard gain 通常首先是 system-level evidence。

## 按年份浏览

[Curated Paper Index](../papers/README.md) 提供简洁 chronology。若目标是理解领域，不建议从年份顺序开始。

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)：看 RAG / Search 的 evaluation target 如何从 retrieval quality 演化到 stateful、cross-source、executable evaluation。
- [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar)：当问题核心变成跨 interaction 持久化的 memory lifecycle。
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)：当 retrieval 是 end-to-end data work 的一个阶段，而不是终点。
