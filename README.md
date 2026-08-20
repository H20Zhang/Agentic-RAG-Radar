# Agentic RAG Radar

**中文** | [English](README.en.md)

追踪 Agent 如何主动获取、检查、控制和保存外部信息。

[Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[最新论文](#latest) · [领域地图](#field-map) · [阅读路径](#reading-paths) · [浏览全部](#library)

最后更新：**2026-08-20**

<a id="latest"></a>
<a id="latest-papers"></a>
<a id="-latest-papers"></a>
## 最新论文

### [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](papers/2608.16185.md)
`Retrieval & Tool Use` · `documents` `iterative search` `budget allocation` · **4/5** · 2026-08-17

LENS 把**证据单元的形成**推迟到查询时：在收到查询之前，不必把原始文档区域预先固定为 chunk。

[论文](https://arxiv.org/abs/2608.16185) · [英文研究笔记](papers/2608.16185.md)

<details><summary><strong>LENS 如何按查询定位证据</strong></summary>

固定的 chunk 和索引会在查询到来前预先划定证据边界；原始文件更新后，索引还可能过期。LENS 先根据多种低成本信号找出候选原始文档区域，再由 relevance oracle 检查，更新 per-fact belief 和 proposal weight，并在预算范围内停止。

最有信息量的结果来自证据定位，而不是答案 EM。在 D500 受控设置中，LENS 达到 **62.4% EM / 84.8% 证据召回率**，ReAct-style search 为 **65.2% / 50.4%**；在 fixed fullwiki 设置中，两者的 EM 基本持平，但 LENS 的有依据答案表现更好。它为此付出了更多在线 token 和延迟。要判断这是否是更好的系统取舍，还需要在同一个生命周期预算下比较最新索引的维护成本与查询时定位成本。

</details>

### [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](papers/2608.16370.md)
`Evaluation & Analysis` · `memory` `iterative search` · **4/5** · 2026-08-17

缩短上下文不一定会降低成本：被压缩掉的状态之后可能需要通过大量**重新获取式检索（reacquisition retrieval）**找回，而任务完成情况几乎不变。

[论文](https://arxiv.org/abs/2608.16370) · [英文研究笔记](papers/2608.16370.md)

<details><summary><strong>上下文压缩如何转移成本</strong></summary>

论文把工具调用分为执行任务的调用，以及因上下文丢失而重新获取状态的调用。在固定的 24 轮交互范围内，sliding compression 越激进，检索越多；oracle 恢复被丢弃但仍可查询的状态后，大部分额外交互都会消失。

在一个代表性实验单元中，检索调用从 **21.0 增至 63.9**，任务完成情况却没有显著变化。负面边界同样重要：ALFWorld 没有出现同样的激增。因此，“节省了多少上下文 token”本身不能作为成本指标；还应比较保留状态的成本，以及以后通过工具或检索重新获取它所需的延迟和费用。

</details>

### [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](papers/2608.15191.md)
`Iterative Reasoning & Verification` · `adaptive stopping` `query rewrite` · **4/5** · 2026-08-15

RAAC 显式记录**搜索进度**，并根据 coverage、novelty、query diversity 和 drift 决定继续、转向还是停止。

[论文](https://arxiv.org/abs/2608.15191) · [英文研究笔记](papers/2608.15191.md)

<details><summary><strong>RAAC 如何决定继续、转向或停止</strong></summary>

深度研究 Agent 的常见问题不是无法继续搜索，而是在证据已经饱和后仍继续搜索。RAAC 在原 Agent 外增加进度信号，据此继续搜索、停止，或调用 critical re-thinker 生成实质不同的新查询。

在 BrowseComp-Plus 上，论文报告平均减少约 **14 次搜索调用**，同时平均准确率提升约 **3 个百分点**。但 controller 和 re-thinker 本身也需要额外的 LLM 调用，所以搜索次数减少并不等于总成本更低。下一步应对齐 controller 与检索所消耗的 token、延迟和金钱成本。

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2608.12888.md)
`Retrieval & Tool Use` · `memory` `iterative search` · **4/5** · 2026-08-13

如果原始归档提供会话、时间和局部上下文控制，并允许 Agent 根据结果继续搜索，那么查询时访问可以替代一部分预先构建的语义记忆结构。

[论文](https://arxiv.org/abs/2608.12888) · [英文研究笔记](papers/2608.12888.md)

<details><summary><strong>ReFind 如何搜索原始聊天记录</strong></summary>

ReFind 保留带时间戳的原始对话轮次，并提供词法搜索、相邻上下文、会话融合、时间过滤器和已查看会话的状态。因此，在判断语义记忆结构是否必要时，它比 one-shot BM25 更适合作为对照。

在六个任务上，论文报告的平均准确率为 **58.2**，HippoRAG 2 为 **53.2**，BM25-RAG 为 **48.8**。在 LongMemEval-S/M 上，完整接口达到 **93.2/89.3**，也高于条件对齐的通用多轮 BM25 和单次搜索对照。尚未解决的问题是生命周期对齐的成本，尤其是在语义任务和行动型 Agent 任务上。

</details>

### [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](papers/2608.11967.md)
`Learning & Optimization` · `backtracking` `RL` · **4/5** · 2026-08-12

LoongReflect 使**搜索状态可以回滚**：发现受污染的分支后，Agent 回到可信前缀，保留纠错经验，再继续执行。

[论文](https://arxiv.org/abs/2608.11967) · [英文研究笔记](papers/2608.11967.md)

<details><summary><strong>LoongReflect 如何回滚受污染的搜索状态</strong></summary>

错误的实体关联或证据可能污染后续许多搜索动作。LoongReflect 训练 Agent 进行反思，回退到可信状态，保留纠错经验，再从那里继续执行，而不是一直携带错误后缀。

在 Qwen2.5-3B 上，论文报告七个 RAG 基准的平均成绩为 **46.15 F1**，AgenticRAG-R1 为 **33.55**。但教师模型拥有特权全局轨迹信息，因此当前实验更能支持整套恢复学习方案，尚不能把全部增益归因于回滚语义本身。

</details>

### [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](papers/2608.12282.md)
`Evaluation & Analysis` · `APIs` `documents` `cross-source grounding` · **4/5** · 2026-08-12

VAKRA 不再分别测试 API 使用或文档 QA，而是检查它们能否与多跳推理、策略约束在**同一条可执行轨迹**中保持一致。

[论文](https://arxiv.org/abs/2608.12282) · [代码](https://github.com/IBM/vakra) · [英文研究笔记](papers/2608.12282.md)

<details><summary><strong>VAKRA 如何测试跨来源执行</strong></summary>

一个 Agent 可以分别在 API 基准和文档 QA 上表现良好，却在跨来源执行时因身份解析、grounding 或策略约束而失败。VAKRA 在固定评测框架中重新执行预测的工具调用，评估完整轨迹，而不只评估最终答案。

最佳模型在单跳端点式任务上达到 **70.4%**，但在组合式 API 上只有约 **50–51%**；一些受策略约束的不可回答设置低至 **2.4%**。这是评测结果，并非某个 controller 的组件层面证据。下一步应固定模型、工具和预算，再隔离究竟哪种控制变化能修复跨来源 grounding。

</details>

<a id="changes"></a>
<a id="whats-changing"></a>
<a id="-whats-changing"></a>
## 最近的研究变化

| 变化 | 新证据 | 对研究设计的含义 |
|---|---|---|
| **证据的形成时机成为一等设计变量。** | Indexed RAG 预先生成 chunk；DCI 保留原始文件；LENS 在线完成随查询变化的证据定位。 | 应比较时效性、证据保真度与离线和在线总成本，而不只看答案分数。 |
| **搜索进度与保留状态成为显式控制状态。** | RAAC 暴露搜索进度；LoongReflect 让推理状态可以回滚；上下文压缩研究衡量丢弃状态带来的重新查询成本。 | 归因检索成本时应计入状态策略，而不能把它当作运行时基础设施。 |
| **强检索基线必须包含接口与评测框架。** | ReFind、Pi-Serini 与评测框架分析都表明，搜索原语、展示给 Agent 的结果深度和交互协议能显著改变结论。 | 在把增益归因于“Agent 检索策略”之前，应先对齐接口和评测框架。 |

按时间浏览：[周报](digests/README.md) · [月报](digests/monthly/2026-08.md) · [年报](digests/yearly/2026.md)

<a id="field-map"></a>
## 领域地图

`信息需求 → 查询/规划 → 检索接口 → 证据形成 → 检查/推理 → 继续/转向/停止 → 持久状态 → 回答/行动`

| 设计轴 | 核心问题 | 当前张力 |
|---|---|---|
| **Adaptivity placement** | 哪些操作可以在看到证据前预先编排，哪些必须根据返回结果调整？ | `pre-query compilation ↔ query-time adaptation` |
| **Evidence materialization** | 何时应把文本块、区域或工作区固化为可操作对象？ | `pre-materialized index ↔ raw/query-conditioned evidence` |
| **Interface resolution** | Agent 能观察和控制哪些检索操作与来源状态？ | `opaque top-k ↔ explicit search/read/filter/navigation` |
| **State persistence** | 哪些证据、进度和推理状态应跨动作保留？ | `stateless loop ↔ persistent/recoverable state` |
| **Resource accounting** | 哪种方案的总成本更低？ | `local retrieval metric ↔ lifecycle cost + task outcome` |

[浏览完整研究问题地图 →](categories/README.md) · [查看这个方向的评测 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#rag-agentic-retrieval)

<a id="reading-paths"></a>
<a id="-reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该学到什么 |
|---|---|---|
| **检索控制和证据形成应放在哪个环节？** | [SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) | 有些检索决策可以预先编排；有些信息只有读到证据后才可见；连证据粒度本身也可以推迟到查询时再决定。 |
| **哪些状态值得保留？** | [SGR-Bench](papers/2605.22219.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md) | 环境状态、进度状态、可回滚推理状态和保留上下文的失败成本各不相同。 |
| **怎样对检索结论做因果归因？** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [VAKRA](papers/2608.12282.md) | 只有把后端、接口、评测框架、模型、预算和跨来源执行分开，才能判断检索策略的贡献。 |

<a id="library"></a>
## 研究资料库

历史工作可以按问题与设计张力浏览，也可以按论文或时间查找。

[按问题、研究路线与年份浏览](library/README.md) · [研究问题地图](categories/README.md) · [论文时间索引](papers/README.md) · [时间维度综述](digests/README.md)

## 收录范围

纳入的工作需要让 Agent 对**是否、检索什么、去哪里检索、如何检索、检索多少**拥有实质控制，或者改变支持这种控制的持久信息状态。普通固定式 RAG 如果没有真正的控制、接口或状态贡献，通常不纳入。

## 维护

[参与贡献](CONTRIBUTING.md) · [收录标准](CURATION.md) · [日常流程](docs/DAILY_WORKFLOW.md)
