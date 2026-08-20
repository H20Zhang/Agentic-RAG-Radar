# Adaptivity 应该放在哪里？

[← Research Map](../README.md) · [首页](../../README.md)

> **当前判断：** Adaptivity 不是“有/没有 agent”二选一，而是 placement decision：哪些 control 可以在 evidence 到来前 compile，哪些 decision 只有看见 retrieval result 后才有信息做。

## Strongest signal

SIRA 一类方法说明：如果 corpus statistics / discriminative vocabulary 在 query 前可观察，一部分 exploratory behavior 可以提前 compile 成 retrieval action。ReFind 则给出相反 regime：有用的 name、time、session relation 只有 first-hop evidence 出现后才知道，result-conditioned reformulation 才有价值。

因此 `number of rounds` 更像 outcome，而不是 primitive。

## Boundary

Pre-retrieval control 可能支付 offline corpus-side intelligence；multi-round control 则支付 online token/latency，并可能在简单 workload 上浪费搜索。

## Decisive next evidence

同一 substrate、model 与 total compute，独立比较：

`pre-retrieval compilation → one-shot action → result-conditioned replanning`

并严格控制 controller 能观察到的 corpus information。

## 继续读

[SIRA](../../papers/2605.06647.md) · [ReFind 中文笔记](../../papers/2608.12888.zh.md) · [PlanRAG](../../papers/2406.12430.md)
