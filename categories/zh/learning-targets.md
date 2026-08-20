# 到底应该 Learn 什么？

[← Research Map](../README.md) · [首页](../../README.md)

> **当前判断：** “Learn a retrieval policy”隐藏了多个不同 learning target：retriever utility、query/refinement policy、direct-corpus operation、recovery behavior、resource allocation、甚至 self-play task distribution。

## Strongest signal

Agentic-R、Critic-R、GrepSeek、SearchMaster、LoongReflect 等工作分别把 learning signal 放在不同位置。表面上都叫“training search agent”，但改变的 action space、teacher information、reward 与 training distribution 并不相同。

因此跨论文 leaderboard 很难回答“哪种 learning objective 更好”。

## Boundary

更丰富 interface、privileged teacher/verifier、更好的 evidence coverage、更容易的 self-play curriculum 或更大的 realized budget，都可能伪装成 learning-objective gain。

尤其 LoongReflect 的 global trajectory teacher 提醒我们：学会 recovery 与拥有更强 supervision 是两个变量。

## Decisive next evidence

固定 environment/state/action space/base model，独立变化：

`learned component × reward/credit assignment × teacher information × task-generation policy × realized budget`

并做 transfer，而不是只看原 benchmark convergence。

## 继续读

[Agentic-R](../../papers/2601.11888.md) · [GrepSeek](../../papers/2605.29307.md) · [SearchMaster](../../papers/2608.01822.md) · [LoongReflect 中文笔记](../../papers/2608.11967.zh.md)
