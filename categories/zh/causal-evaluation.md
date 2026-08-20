# 什么样的 Evaluation 才能支持 Causal Attribution？

[← Research Map](../README.md) · [首页](../../README.md)

> **当前判断：** Controller 还没开始行动前，attribution 就可能已经失败。Evidence 必须存在、backend 必须暴露、interface/harness 必须让 agent 看见、source/internal state 必须正确、realized resources 必须匹配，之后才能给 policy 记功。

## Strongest signal

Training Protocols、Pi-Serini、Is Grep All You Need?、SGR-Bench、VAKRA 从不同角度说明：所谓“same retriever”或“same task”仍可能因为 surfaced depth、delivery path、environment state、harness、tool budget 与 cross-source execution 不同而不是同一个实验。

Final-answer success 尤其容易掩盖 upstream failure 或额外工作。

## Boundary

完全 factorial 的 evaluation 很昂贵，而且有些变量天然耦合。目标不应是假装所有 paper 都能做完美 causal inference，而是**明确 claim 能走到哪一层**：system package、controller、retriever、interface，还是某个 state mechanism。

## Decisive next evidence

最有价值的 benchmark 形态是 executable replay：同一个 task 可以独立 swap backend、interface、source state、retained state、harness、controller，并对某一个 intermediate failure 做 counterfactual repair。

同时记录实际 token、latency、tool calls 与 controller cost。

## 继续读

[Training Protocols](../../papers/2605.27881.md) · [Pi-Serini](../../papers/2605.10848.md) · [VAKRA 中文笔记](../../papers/2608.12282.zh.md) · [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)
