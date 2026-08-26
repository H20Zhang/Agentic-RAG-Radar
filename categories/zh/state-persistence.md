# 什么 State 值得持久化？

[← Research Map](../README.md) · [首页](../../README.md)

> **当前判断：** Agent state 不是一个对象。Source configuration、collected evidence/gaps、search progress、active reasoning state、retained context 的 owner 与 failure mode 都不同。State 的价值取决于 **future reuse × recoverability × reacquisition cost**。StateMem 与 EvoWiki 进一步表明：保留历史和解析 operative state 也不是同一操作，validity 可以在 answer time 组装，也可以在 write time 物化。

## Strongest signal

SGR-Bench 把 source/environment configuration 纳入 retrieval competence；S2G-RAG 维护 evidence sufficiency/gap；RAAC 显式维护 progress；LoongReflect 让 active reasoning trajectory 可回滚；Context Compression Cost 则证明某些 dropped state 会以额外 retrieval 的形式被重新买回来。StateMem 在回答时组装 supersession/precedence，EvoWiki 在写入时关闭被替代事实的 validity interval；后者的 matched no-overwrite control 把 macro accuracy 从 51.46 提到 60.09。

因此“context 越短越好”与“state 越多越好”都不是稳定目标。

## Boundary

更显式的 state 可能只是给 controller 增加容量或 privileged supervision；另一方面，并非所有 environment 都存在明显 re-query tax。很多 external action 也不可逆，恢复 internal reasoning state 并不能恢复 world state。

## Decisive next evidence

先把 supersession resolution 在 write time 与 answer time 之间移动，并匹配 extraction、history access、answer context、update cost、dependency handling 与 answer quality；再对 state classes 做 counterfactual restore / delete / freeze。

## 继续读

[StateMem 中文笔记](../../papers/2608.19652.zh.md) · [EvoWiki 中文笔记](../../papers/2608.23265.zh.md) · [Context Compression Cost 中文笔记](../../papers/2608.16370.zh.md) · [LoongReflect 中文笔记](../../papers/2608.11967.zh.md)
