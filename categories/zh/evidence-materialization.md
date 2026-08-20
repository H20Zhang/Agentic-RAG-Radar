# Evidence 什么时候 Materialize？

[← Research Map](../README.md) · [首页](../../README.md)

> **当前判断：** Evidence boundary 不是必须在 indexing time 固定。稳定 corpus / predictable unit 更适合 pre-materialization；dynamic corpus 或 query-dependent granularity 可能值得把 localization 推到 query time。

## Strongest signal

DCI 保留 raw corpus，让 agent 直接组合 file/search/read operation；RISE / DR-DCI 把 retrieval 变成 persistent interaction-space expansion；LENS 更进一步，把 raw-document region 当 latent evidence，等 query 出现后再在线定位。

这说明 design axis 不只是“有没有 index”，而是：

`什么时候决定 evidence unit × 谁决定 × 需要多少 online work`

## Boundary

“No index”不等于“no cost”。Raw interaction 可能随着 corpus scale 迅速变贵；LENS 在 evidence recall/grounding 上有优势，但 main answer EM 并没有普遍赢 ReAct，而且 online token/latency 更高。

## Decisive next evidence

同一 changing corpus、同 answer/evidence target，生命周期匹配：

`index build/update + freshness lag` vs `bounded raw interaction` vs `query-time latent localization`

把 offline 与 online cost 放到同一个账本。

## 继续读

[DCI](../../papers/2605.05242.md) · [RISE](../../papers/2606.06880.md) · [LENS 中文笔记](../../papers/2608.16185.zh.md)
