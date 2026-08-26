# Agentic RAG Research Library

**中文** | [English](README.en.md) · [返回首页](../README.md)

按**研究问题、设计张力与研究路线**浏览历史工作；周报、月报和年报只记录时间线上的变化。

## 按研究问题浏览

| 问题 | 入口 | 当前核心张力 |
|---|---|---|
| **Adaptivity placement** | [进入](../categories/zh/adaptivity-placement.md) | 哪些搜索行为可以在证据到来前预先编排，哪些必须根据返回结果调整？ |
| **Evidence materialization** | [进入](../categories/zh/evidence-materialization.md) | 应在索引阶段固定证据单元，还是等查询到来后再定位？ |
| **State persistence** | [进入](../categories/zh/state-persistence.md) | 哪些状态值得保留，哪些状态丢弃后会产生重新获取成本？ |
| **Interface resolution** | [进入](../categories/zh/interface-resolution.md) | 不透明的 top-k 是否足够，还是需要搜索、读取、过滤、导航等显式接口？ |
| **Learning targets** | [进入](../categories/zh/learning-targets.md) | 检索器、控制、恢复、预算和任务分布中，哪些部分应该成为学习目标？ |
| **Causal evaluation** | [进入](../categories/zh/causal-evaluation.md) | 如何分离后端、接口、评测框架、状态、模型和预算，才能进行因果归因？ |

## 按研究路线浏览

### 固定式检索 → 直接交互 → 查询时证据形成

[SIRA](../papers/2605.06647.md) → [DCI](../papers/2605.05242.md) → [ReFind](../papers/2608.12888.zh.md) → [LENS](../papers/2608.16185.zh.md)

自适应位置与证据形成时机是两个不同的设计决策。SIRA 在执行检索前预先编排一部分决策；DCI 和 ReFind 保留原始载体；LENS 则把证据边界的确定进一步推迟到查询时。

### 搜索循环 → 有效状态解析 → 恢复与重新获取

[RAAC](../papers/2608.15191.zh.md) → [StateMem](../papers/2608.19652.zh.md) → [EvoWiki](../papers/2608.23265.zh.md) → [Context Compression Cost](../papers/2608.16370.zh.md)

“多搜几轮”本身不是一个原语。更重要的是 Agent 如何观察进度、operative validity 在 answer time 还是 write time 解析，以及被丢弃的状态是否会产生重新查询成本。

### 检索器质量 → 接口 / 评测框架归因 → 跨来源执行

[Pi-Serini](../papers/2605.10848.md) → [Is Grep All You Need?](../papers/2605.15184.md) → [Training Protocols](../papers/2605.27881.md) → [VAKRA](../papers/2608.12282.zh.md)

后端分数、呈现给 Agent 的证据、Agent 框架、模型与工具预算会紧密耦合；排行榜增益通常只能先作为系统层面证据。

## 按年份浏览

[Curated Paper Index](../papers/README.md) 提供简洁的时间顺序。若要理解领域脉络，建议先从研究路线开始，而不是按年份顺序阅读。

## 相关 Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)：追踪 RAG / 搜索的评测目标如何从检索质量演化为有状态、跨来源、可执行的评测。
- [Agent Memory Radar](https://github.com/H20Zhang/Agent-Memory-Radar)：适合关注跨交互持久化的记忆生命周期。
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)：适合研究检索如何成为端到端数据工作的一个阶段，而不是终点。
