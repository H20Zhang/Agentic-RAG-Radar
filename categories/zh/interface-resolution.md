# Retrieval 应如何暴露 Corpus？

[← Research Map](../README.md) · [首页](../../README.md)

> **当前判断：** “Retriever quality”太粗。Backend recall 只是上游条件；candidate admissibility、surfaced depth、operation set、local/structural navigation、inspection 与 read resolution 都会决定 agent 最终能看到什么。

## Strongest signal

DCI/A-RAG/RISE 一类工作把 opaque top-k 拆成可调用 operation；Pi-Serini 进一步区分 backend ranking depth 与 agent 实际 inspect 的 evidence；ReFind 显示 domain-native session/time/context controls 会显著改变 raw retrieval 的竞争力。

因此“same retriever”并不自动意味着 same experiment。

## Boundary

更丰富 interface 会增加 tool-call、token 与 controller complexity；lexical/direct interaction 在 semantic mismatch 下仍可能脆弱。Harness 如果不允许模型看到相同深度或相同 context，也会制造虚假的 policy difference。

## Decisive next evidence

做 factorial experiment：

`backend × surfaced depth × operation set × read resolution × harness`

保持 model、evidence pool 与 realized budget 一致。

## 继续读

[DCI](../../papers/2605.05242.md) · [Pi-Serini](../../papers/2605.10848.md) · [ReFind 中文笔记](../../papers/2608.12888.zh.md)
