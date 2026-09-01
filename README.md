# Agentic RAG Radar

**中文** | [English](README.en.md)

追踪 Agent 如何主动获取、检查、控制和保存外部信息。

这个 Radar 主要回答：**检索决策应放在哪里？证据何时形成？哪些状态值得保留？自适应控制到底换来了什么？**

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新时间线](#timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

**状态：** 最后更新：**2026-09-01** · 最后合成：**2026-09-01T01:24:01Z（UTC）**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## 最新时间线

> **迁移说明：** 这六条 legacy 记录没有保存历史 Radar 接纳时间，因此按论文公开日期排序，不把它们冒充为“最近被 Radar 接纳”。v2 切换后新增记录按 `radar_published_at` 排序，同时保留原始 `published_at`。

<a id="entry-2608.27912"></a>
<details><summary>2026-09-01 · ITER · Adaptivity placement → interaction-conditioned retrieval <!-- timefirst:area=interaction-conditioned-retrieval --> — 把 trajectory history 放进 retriever：ranking 目标从当前 query relevance 变成相对于已探索 evidence 的 marginal utility。 <!-- timefirst:delta=interaction-conditioned-retrieval --></summary>

**问题。** 在 ranked interface 不变时，retriever 是否应该显式知道 Agent 已经搜过什么、看过什么？ <!-- timefirst:question=interaction-conditioned-retrieval -->

**证据。** 同 Qwen3-Embedding-0.6B family：LRAT / ITER SQ-only / default ITER 在 InfoSeek-Eval 为 **72.7/76.7/80.0**，BrowseComp-Plus 为 **43.4/43.7/46.6**；六个 agent backbone 的 12 个 task cell 中 default ITER 全部胜 LRAT。 <!-- timefirst:evidence=interaction-conditioned-retrieval~qwen3-embedding-0.6b-family -->

**限制。** success-conditioned trajectory + LLM verifier labels；collection de-duplicates candidate exposure，且 history-conditioned encoder 的 token/latency 成本未报告。 <!-- timefirst:caveat=interaction-conditioned-retrieval~llm-verifier-labels -->

**地图。** `early_signal`：interaction-conditioned retrieval 值得作为独立 placement variable，但单篇 retriever work 不改 durable map。

**链接。** [ITER: Interaction-Aware Retrieval for Agentic Search](https://arxiv.org/abs/2608.27912) · [英文深读](papers/2608.27912.md) · [中文深读](papers/2608.27912.zh.md)

</details>

<a id="entry-2608.28062"></a>
<details><summary>2026-09-01 · WeAgent-MMSearch · Evidence materialization → multimodal evidence persistence <!-- timefirst:area=multimodal-evidence-persistence --> — 把 tool-returned image 的跨 turn 可见性变成显式 harness variable，而不是把“搜到图”视为一次性 observation。 <!-- timefirst:delta=multimodal-evidence-persistence --></summary>

**问题。** visual evidence 被 retrieval 返回后，后续 search/reasoning 是否仍能访问原始 modality？ <!-- timefirst:question=multimodal-evidence-persistence -->

**证据。** 同 WeAgent-MMSearch-RL、同 WeAgent-Harness tool interface，只移除 image re-feed：八任务平均 **55.97→46.89**；MMBrowseComp **28.13→13.69**，VisTarget **30.22→10.44**。 <!-- timefirst:evidence=multimodal-evidence-persistence~weagent-mmsearch-rl -->

**限制。** 更大的 full-system gain 同时改变 data、RL、runtime recovery cache semantics；budget 是 cap，不是 matched realized cost。 <!-- timefirst:caveat=multimodal-evidence-persistence~runtime-recovery-cache-semantics -->

**地图。** `early_signal`：multimodal evidence persistence 应作为独立 materialization/interface variable；单篇 harness study 不改 durable map。

**链接。** [WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents](https://arxiv.org/abs/2608.28062) · [英文深读](papers/2608.28062.md) · [中文深读](papers/2608.28062.zh.md)

</details>

<a id="entry-2608.28476"></a>
<details><summary>2026-09-01 · ContextPilot · State persistence → proactive context management <!-- timefirst:area=proactive-context-management --> — 把 working context 当成可编辑 state：Agent 主动决定 plan、retain、compress、offload，并对关键 edit action 做细粒度 RL credit。 <!-- timefirst:delta=proactive-context-management --></summary>

**问题。** long-horizon search 中，哪些 state 应继续 materialize，哪些应 offload，以及这个 policy 能否被独立训练？ <!-- timefirst:question=proactive-context-management -->

**证据。** Qwen3-8B staged ablation 中 +Context → +Fine-grained 在 NovelQA/∞Bench/LME-S/BC+ 从 **83.05/73.94/61.40/51.08** 到 **83.88/75.25/64.27/54.18**，四格均提升。 <!-- timefirst:evidence=proactive-context-management~qwen3-8b-staged-ablation -->

**限制。** full method 同时扩展 tool surface、SFT、partial-rollout credit assignment；tool ablation 又是大模型 cumulative setup，完整 lifecycle cost 未配平。 <!-- timefirst:caveat=proactive-context-management~partial-rollout-credit-assignment -->

**地图。** `early_signal`：proactive context management 是 state-policy placement；单个 package 不改 durable Field Map。

**链接。** [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](https://arxiv.org/abs/2608.28476) · [Code](https://github.com/Tencent/ContextPilot) · [英文深读](papers/2608.28476.md) · [中文深读](papers/2608.28476.zh.md)

</details>

<a id="entry-2608.25618"></a>
<details><summary>2026-08-28 · AWM · Evidence materialization → answerable working memory <!-- timefirst:area=answerable-working-memory --> — 把 terminal working memory 当成独立 evidence artifact：即使找到正确页面，也要验证离开 page context 后这份 state 还能不能支持答案。 <!-- timefirst:delta=answerable-working-memory --></summary>

**问题。** retrieval 已到达相关页面后，Agent 写下来的 working state 是否仍可能成为独立 bottleneck？ <!-- timefirst:question=post-retrieval-memory-answerability -->

**证据。** same Qwen3-VL-4B family：Answer-GRPO → AWM-GRPO 的 final accuracy 为 **51.6→53.9 / 57.4→60.1**；EP-given 固定 gold evidence pages 后，final/memory-only accuracy **45.4/41.2→48.0/43.5**，`Pmmc` **19.1%→16.4%**。 <!-- timefirst:evidence=awm-controlled~gold-evidence-pages -->

**限制。** reward-supervision cost：每个 rollout 增加两次 frozen reader passes（Qwen3-14B）；memory-only answerability 依赖单一 reader/judge，且不是 claim-level source grounding。 <!-- timefirst:caveat=awm-boundary~frozen-reader-passes -->

**地图。** `early_signal`：需要把 evidence reached、evidence preserved、evidence grounded 分开测；单个 VQA study 不改 durable map。

**链接。** [AWM: Answerable Working Memory for Long-Document VQA Agents](https://arxiv.org/abs/2608.25618) · [Code](https://github.com/DongzhuoranZhou/AWM) · [英文深读](papers/2608.25618.md) · [中文深读](papers/2608.25618.zh.md)

</details>

<a id="entry-2608.24667"></a>
<details><summary>2026-08-27 · EviGraph · Evidence materialization → span-grounded evidence construction <!-- timefirst:area=span-grounded-evidence-construction --> — 把 verified source spans 写成 claim-level support/conflict state，再用它控制下一次搜索与 stopping。 <!-- timefirst:delta=span-grounded-evidence-construction --></summary>

**问题。** evidence 能否从线性 search trace 物化为可审计、可驱动控制的 claim–evidence state？ <!-- timefirst:question=explicit-claim-evidence-state -->

**证据。** BrowseComp-Plus 同一 dual-role architecture：no-RL **26.9% → RL 35.9%**；搜索量基本不变且 generated tokens 更少。 <!-- timefirst:evidence=evigraph-controlled~dual-role-architecture -->

**限制。** privileged verifier：frozen verifier 决定 span 与 polarity；structural validator 只保证 provenance/invariants，且 page-token/latency/dollar accounting 不完整。 <!-- timefirst:caveat=evigraph-boundary~page-token-latency-dollar -->

**地图。** `early_signal`：显式 evidence state 是值得独立比较的 representation/control point，但单篇工作还不能把 graph 提升为稳定方向。

**链接。** [EviGraph: Towards Verifiable Evidence Construction for Information-Seeking Agents](https://arxiv.org/abs/2608.24667) · [英文深读](papers/2608.24667.md) · [中文深读](papers/2608.24667.zh.md)

</details>

<a id="entry-2608.24794"></a>
<details><summary>2026-08-27 · CAFE · Adaptivity placement → feedback-request routing <!-- timefirst:area=co-evolving-feedback-routing --> — 把 corrective feedback 变成 trajectory 内可学习的 intervention，并让 critic 随 on-policy failures 更新。 <!-- timefirst:delta=co-evolving-feedback-routing --></summary>

**问题。** search policy 能否学会何时请求 feedback，并让 critic 跟随 policy 的 failure distribution 一起变化？ <!-- timefirst:question=feedback-request-and-recovery -->

**证据。** 同 feedback-SFT family：CAFE **52.5 EM / 60.7 F1** vs GRPO **49.7 / 58.0**；component ablation 支持两个 shaping term。 <!-- timefirst:evidence=cafe-controlled~feedback-sft-family -->

**限制。** schedule-and-cost confound：500 online steps 的不同 alternation schedule 自身就显著改变结果，额外 feedback calls 的完整 token/tool/latency 成本也未匹配。 <!-- timefirst:caveat=cafe-boundary~500-online-steps -->

**地图。** `early_signal`：adaptivity 可以包括“何时购买一次纠正”，但 full package 不能归因给 co-evolution 单项。

**链接。** [CAFE: Self-Improving Search Agents Need Co-Evolving Feedback](https://arxiv.org/abs/2608.24794) · [英文深读](papers/2608.24794.md) · [中文深读](papers/2608.24794.zh.md)

</details>

<a id="entry-2608.24809"></a>
<details><summary>2026-08-27 · Crase · Interface resolution → structurally bounded exploration <!-- timefirst:area=structurally-bounded-exploration --> — seed 后把 candidate space 与 stopping 固定在 citation graph，而不是继续由模型决定搜不搜。 <!-- timefirst:delta=structurally-bounded-exploration --></summary>

**问题。** domain structure 足够强时，能否把 open-ended exploration/stopping 从 policy 移到可审计的结构 substrate？ <!-- timefirst:question=bounded-versus-open-ended-search -->

**证据。** ICLR：Crase **R@50 0.3659** vs 两个 deep-research baseline **0.1220**，同时 5 vs 17–18 calls、235K vs 560–620K tokens、104 vs 249–272s、$0.37 vs $1.76–$2.06。 <!-- timefirst:evidence=crase-iclr~iclr-crase-r -->

**限制。** unmatched output/substrate：Crase 做 ranked scholarly retrieval，且 corpus/model/retrieval substrate 与 proprietary deep-research baselines 不同，不能把收益单独归给 boundedness。 <!-- timefirst:caveat=crase-boundary~corpus-model-retrieval-substrate -->

**地图。** `early_signal`：open-ended adaptivity 应该和 structurally bounded alternative 在相同 output contract 与成本下竞争。

**链接。** [Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch](https://arxiv.org/abs/2608.24809) · [Code](https://github.com/RadiantCrystal/CRASE) · [英文深读](papers/2608.24809.md) · [中文深读](papers/2608.24809.zh.md)

</details>

<a id="entry-2608.22767"></a>
<details><summary>2026-08-26 · EARM · State persistence → 经验摊销重排 <!-- timefirst:area=experience-amortized-memory-reranking --> — 复用此前经过判断的检索经验，对固定记忆库重新排序。 <!-- timefirst:delta=experience-amortized-memory-reranking --></summary>

**问题。** 检索经验能否保留为可复用排序状态，而不是每个查询都重新获取？ <!-- timefirst:question=experience-amortized-retrieval -->

**证据。** fixed-pool completion ablation：在同一 reranker 上加入 completion，LoCoMo F1 提升 0.78–2.79 点；完整系统把 direct LLM calls 减少 74.43%。 <!-- timefirst:evidence=earm-ablation~fixed-pool-completion -->

**限制。** single-store accounting：结果只覆盖固定 memory store 与 query order 的 LoCoMo，完整 token、latency 与 dollar accounting 缺失。 <!-- timefirst:caveat=earm-boundary~single-store-accounting -->

**地图。** `early_signal`：单一 benchmark 表明检索经验可能摊销后续排序成本，尚不构成方向。

**链接。** [The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory](https://arxiv.org/abs/2608.22767) · [Artifact](https://github.com/FengQi-HITSZ/earm) · [英文深读](papers/2608.22767.md) · [中文深读](papers/2608.22767.zh.md)

</details>

<a id="entry-2608.23045"></a>
<details><summary>2026-08-26 · NIS-Agent · Interface resolution → 职责隔离验证 <!-- timefirst:area=ownership-isolated-search-validation --> — 在综合答案前拆分搜索、证据检查和作答职责。 <!-- timefirst:delta=ownership-isolated-search-validation --></summary>

**问题。** 在检索证据固定时，隔离搜索与验证职责能否改善结果使用？ <!-- timefirst:question=search-validation-ownership -->

**证据。** Observer Mode holds tasks and search results fixed，re-search judgment 提升 15–30 点；完整 GPT-4o GAIA package 从 54.88→61.82，tokens 从 219.8K 降至 147.3K。 <!-- timefirst:evidence=nis-observer~observer-mode-holds-tasks-and-search-results-fixed -->

**限制。** packaged interface change：端到端系统同时改变 roles、stopping、prompts 与 tool flow，且 call 与 dollar accounting 不完整。 <!-- timefirst:caveat=nis-boundary~packaged-interface-change -->

**地图。** `early_signal`：fixed-results control 隔离出 interface effect，但不能把完整 trajectory gain 归因给 retrieval。

**链接。** [From Inertia to Objectivity: Improving Deep Research Agents with Noise Isolation](https://arxiv.org/abs/2608.23045) · [英文深读](papers/2608.23045.md) · [中文深读](papers/2608.23045.zh.md)

</details>

<a id="entry-2608.23417"></a>
<details><summary>2026-08-26 · SkillAlchemy · Adaptivity placement → 对比式能力获取 <!-- timefirst:area=contrastive-requirement-guided-acquisition --> — 用匹配任务上下文探测一个候选操作因子，再把源材料中的 procedure 判为 General、Scoped 或 Exclude。 <!-- timefirst:delta=contrastive-requirement-guided-acquisition --></summary>

**问题。** 匹配的任务上下文探针能否识别该获取哪种 procedure，以及它应以多窄的范围被接纳？ <!-- timefirst:question=contrastive-skill-acquisition -->

**证据。** 报告套件上 SkillAlchemy scores 55.8% versus MUSE 47.2%，OpenSkill 46.0%、no-skill 35.9%；移除组件会损失 5.0–15.7 点。 <!-- timefirst:evidence=skillalchemy-suite~skillalchemy-scores-55.8-versus-muse -->

**限制。** unmatched acquisition budget：系统间 sources、tokens、calls 与 artifact length 未控制，无法把 package gain 单独归给 contrastive admission。 <!-- timefirst:caveat=skillalchemy-boundary~unmatched-acquisition-budget -->

**地图。** `early_signal`：这是有潜力的 acquisition controller，但仍缺 matched interface-and-budget comparison。

**链接。** [SkillAlchemy: Open-World Agent Skill Creation](https://arxiv.org/abs/2608.23417) · [英文深读](papers/2608.23417.md) · [中文深读](papers/2608.23417.zh.md)

</details>

<a id="entry-2608.23265"></a>
<details><summary>2026-08-26 · EvoWiki · State persistence → 写入时 supersession <!-- timefirst:area=supersession-aware-state-assembly --> — 在增量写入时解析 current-valid state，同时保存版本账本。 <!-- timefirst:delta=write-time-supersession-resolution --></summary>

**问题。** supersession 应在回答时重建，还是在状态写入时物化？ <!-- timefirst:question=write-time-supersession -->

**证据。** matched no-overwrite control 保持 extraction、coreference、entity Wiki 与 reader 不变；移除 lifecycle invalidation 后，macro accuracy 从 60.09 降至 51.46。 <!-- timefirst:evidence=evowiki-overwrite~matched-no-overwrite-control -->

**限制。** complete-state exposure：读取每 query 使用 17,143 tokens，构建每 project 使用 114,016 tokens；traceability 本身未被直接评测。 <!-- timefirst:caveat=evowiki-boundary~complete-state-exposure -->

**地图。** `reinforces`：与 StateMem 共同说明，保留历史与解析 operative state 是两件事，可分别放在 answer time 或 write time。

**链接。** [EvoWiki: Incremental State Overwriting and Traceable Question Answering for Cross-Meeting Knowledge Evolution](https://arxiv.org/abs/2608.23265) · [英文深读](papers/2608.23265.md) · [中文深读](papers/2608.23265.zh.md)

</details>

<a id="entry-2608.22752"></a>
<details><summary>2026-08-26 · Compaction Cliff · State persistence → 类型化约束保留 <!-- timefirst:area=typed-constraint-retention --> — 在严重 compaction 下把 hard constraints 作为独立状态类型保护。 <!-- timefirst:delta=typed-constraint-retention --></summary>

**问题。** Agent 把状态压缩到原预算 10–50% 时，哪些信息类型必须存活？ <!-- timefirst:question=constraint-preserving-compaction -->

**证据。** Typed vs type-blind constraint recall 在 matched 50/25/10% budgets 下为 1.00/0.95/0.80 对 0.53/0.39/0.24；五轮后仍为 0.96。 <!-- timefirst:evidence=compaction-budget~typed-vs-type-blind -->

**限制。** Typed retrieval metadata advantage：它获得 type-blind controls 没有的任务特定 labels，且下游 retail-token budgets 未匹配。 <!-- timefirst:caveat=compaction-boundary~typed-retrieval-metadata-advantage -->

**地图。** `early_signal`：typed retention 暴露出有用的状态坐标；单一 synthetic failure family 不构成趋势。

**链接。** [The Compaction Cliff in Long-Running AI Agent Memory](https://arxiv.org/abs/2608.22752) · [Artifact](https://github.com/searchsim-org/cikm26-knowledge-triage) · [英文深读](papers/2608.22752.md) · [中文深读](papers/2608.22752.zh.md)

</details>

<a id="entry-2608.22751"></a>
<details><summary>2026-08-26 · Risk-Aware Reranking · Interface resolution → tool exposure <!-- timefirst:area=risk-aware-tool-exposure --> — 把执行前的 tool shortlist 作为显式风险面。 <!-- timefirst:delta=risk-aware-tool-exposure --></summary>

**问题。** executable tools 暴露给 Agent 之前，能否先权衡 relevance 与 operational risk？ <!-- timefirst:question=pre-execution-tool-exposure -->

**证据。** UltraTool risk-head relevance control：在同一 frozen representations 与 relevance head 上加入 risk，NDCG/RVR/SRR 从 0.558/0.188/0.097 变为 0.551/0.138/0.063。 <!-- timefirst:evidence=risk-head~ultratool-risk-head-relevance-control -->

**限制。** Exposure is not execution：没有实际执行工具，labels 与 evaluation 耦合，主比较 candidate sets 不同，strict filtering 还会让 NeedRisk-Hit 从 0.660 降至 0.397。 <!-- timefirst:caveat=risk-boundary~exposure-is-not-execution -->

**地图。** `early_signal`：candidate exposure 变得可测，但 downstream safety 与 matched-cost utility 仍未证明。

**链接。** [Risk-Aware Reranking for Agentic Tool Retrieval](https://arxiv.org/abs/2608.22751) · [Artifact](https://github.com/qli447/risk-aware-tool-retrieval-release) · [英文深读](papers/2608.22751.md) · [中文深读](papers/2608.22751.zh.md)

</details>

<a id="entry-2608.20627"></a>
<details><summary>2026-08-25 · AgenticRAG-FP · Resource accounting → causal failure attribution <!-- timefirst:area=causal-failure-attribution --> — 用 certified hop fault 与 counterfactual rerun 定位传播后的检索失败。 <!-- timefirst:delta=propagation-conditioned-failure-attribution --></summary>

**问题。** 失败改变后续检索后，哪个 hop 仍能被识别为因果起点？ <!-- timefirst:question=causal-hop-identification -->

**证据。** exact hop signal：strict dense Claude/MuSiQue 中，coverage 为 0.91/0/0，frozen-hop repair 为 0.51/0.25/0.48。 <!-- timefirst:evidence=failure-probes~exact-hop-signal -->

**限制。** survivor conditioned comparison：只对仍失败的 traces 计分，clean corpus 会修复 54–85% content faults，active probes 的计算也未匹配。 <!-- timefirst:caveat=failure-boundary~survivor-conditioned-comparison -->

**地图。** `early_signal`：加入 propagation-conditioned attribution 评测坐标；单一 narrow matrix 不构成稳定方向。

**链接。** [When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation](https://arxiv.org/abs/2608.20627) · [Artifact](https://github.com/anote-ai/Research-AgenticRAG) · [英文深读](papers/2608.20627.md) · [中文深读](papers/2608.20627.zh.md)

</details>

<a id="entry-2608.20771"></a>
<details><summary>2026-08-25 · CAS · Adaptivity placement → conformal evidence-set sizing <!-- timefirst:area=conformal-evidence-set-sizing --> — 用 calibrated retrieval mass 调整每次搜索的 evidence-set size。 <!-- timefirst:delta=query-conditioned-retrieval-width --></summary>

**问题。** top-k 能否成为 query-conditioned decision，而不是全局常数？ <!-- timefirst:question=adaptive-evidence-set-size -->

**证据。** matched component ablations：Qwen2.5-3B full 0.401，移除 ACI 为 0.384，fixed top-k=3 为 0.389。 <!-- timefirst:evidence=cas-components~matched-component-ablations -->

**限制。** calibration correctness gap：239 个 teacher-created queries 不保证跨数据集 exchangeability，answer NLL 也不等于 factual correctness。 <!-- timefirst:caveat=cas-guarantee~calibration-correctness-gap -->

**地图。** `early_signal`：加入 conformal evidence-set sizing，不把 marginal coverage 保证写成端到端可靠性。

**链接。** [CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting](https://arxiv.org/abs/2608.20771) · [代码](https://github.com/S1llyBird/CAS) · [英文深读](papers/2608.20771.md) · [中文深读](papers/2608.20771.zh.md)

</details>

<a id="entry-2608.21690"></a>
<details><summary>2026-08-25 · Scroll · State persistence → programmatic context materialization <!-- timefirst:area=programmatic-context-materialization --> — 保留 lossless event log，到查询时才把所需状态放入 prompt。 <!-- timefirst:delta=query-time-context-environment --></summary>

**问题。** Agent 能否让完整历史可恢复，却只 materialize 当前问题需要的 context？ <!-- timefirst:question=lossless-query-time-context -->

**证据。** persistent REPL ablation：BEAM10M full 73.1，移除 REPL 为 65.8，移除 index 为 71.3，lossy ingestion 为 19.9。 <!-- timefirst:evidence=scroll-mechanism~persistent-repl-ablation -->

**限制。** unmatched lifecycle accounting：Scroll 在 LOCA-256K 只比 CodeAct 高 1.4，跨系统比较与 latency/storage/CPU/dollar 成本未匹配。 <!-- timefirst:caveat=scroll-cost~unmatched-lifecycle-accounting -->

**地图。** `early_signal`：连接 retained state 与 query-time materialization；没有完整生命周期证据，不修改稳定地图。

**链接。** [Context as an Environment: Programmatic Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.21690) · [复现分支](https://github.com/niceIrene/QwenPaw/tree/scroll-research) · [英文深读](papers/2608.21690.md) · [中文深读](papers/2608.21690.zh.md)

</details>

<a id="entry-2608.21808"></a>
<details><summary>2026-08-25 · MCite-RL · Evidence materialization → visual localization reward <!-- timefirst:area=visual-evidence-localization --> — 用 final bbox 与 terminal crop reward 训练显式视觉引用。 <!-- timefirst:delta=terminal-visual-citation-reward --></summary>

**问题。** Visual RAG agent 能否学习定位支持答案的 image region？ <!-- timefirst:question=visual-evidence-citation -->

**证据。** citation reward ablation：7B full answer/citation 为 60.00/36.05，移除 citation rewards 后为 54.20/20.56。 <!-- timefirst:evidence=mcite-reward~citation-reward-ablation -->

**限制。** terminal crop supervision：所谓 process reward 只测 terminal crop；数据仅保留 8.6% teacher trajectories，也缺完整 runtime accounting。 <!-- timefirst:caveat=mcite-process~terminal-crop-supervision -->

**地图。** `early_signal`：加入 visual evidence-localization reward，不把 bbox overlap 直接当作 semantic support。

**链接。** [MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21808) · [英文深读](papers/2608.21808.md) · [中文深读](papers/2608.21808.zh.md)

</details>

<a id="entry-2608.22132"></a>
<details><summary>2026-08-25 · SSE-Bio · Adaptivity placement → dual-source routing <!-- timefirst:area=dual-source-retrieval-routing --> — 根据 structured gap state 在 KG、template、both 与 none 之间路由。 <!-- timefirst:delta=structured-gap-source-selection --></summary>

**问题。** 当前 biomedical reasoning gap 应触发哪一种 evidence source？ <!-- timefirst:question=biomedical-source-placement -->

**证据。** fixed policy comparison：learned Proxy 的 single/multi Both_cor 为 16.52/11.73，always-both 为 13.18/9.02。 <!-- timefirst:evidence=sse-routing~fixed-policy-comparison -->

**限制。** low absolute joint correctness：整体正确率仍低，wrong Proxy 只占 HLE failures 的 13.1%，每例平均 12.4K tokens 与 6.7 calls。 <!-- timefirst:caveat=sse-boundary~low-absolute-joint-correctness -->

**地图。** `early_signal`：加入 structured-gap dual-source routing；不把完整 multi-agent package gain 归给 Proxy。

**链接。** [SSE-Bio: A Structured Self-Evolving Agent with Agentic Retrieval Policy for Multi-Hop Biomedical Reasoning](https://arxiv.org/abs/2608.22132) · [代码](https://github.com/ZhaohanM/SSE-Bio) · [英文深读](papers/2608.22132.md) · [中文深读](papers/2608.22132.zh.md)

</details>

<a id="entry-2608.22479"></a>
<details><summary>2026-08-25 · GTA-RAG · Adaptivity placement → evidence-chain supervision <!-- timefirst:area=evidence-chain-supervision --> — 把 graph path 变成 retriever-validated target trajectory 再训练。 <!-- timefirst:delta=retriever-validated-trajectory-reward --></summary>

**问题。** Answer-only reward 之外，是否应直接监督完整 evidence-chain acquisition？ <!-- timefirst:question=evidence-chain-learning-target -->

**证据。** trajectory reward ablation：full vs no trajectory reward 的 full-chain 为 74.1 vs 58.7，EM 为 49.7 vs 46.2。 <!-- timefirst:evidence=gta-trajectory~trajectory-reward-ablation -->

**限制。** graph synthetic target distribution：held-out test 来自同一 graph-path construction，四跳只有 8 个样本，外部 baseline 的 substrate/budget 未匹配。 <!-- timefirst:caveat=gta-transfer~graph-synthetic-target-distribution -->

**地图。** `early_signal`：加入 retriever-validated evidence-chain supervision；不把 graph+interface+data+RL package gain 单独归给 reward。

**链接。** [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning](https://arxiv.org/abs/2608.22479) · [代码](https://github.com/cjcj46262/GTA-RAG) · [英文深读](papers/2608.22479.md) · [中文深读](papers/2608.22479.zh.md)

</details>

<a id="entry-2608.23252"></a>
<details><summary>2026-08-25 · ASCP · Adaptivity placement → context allocation <!-- timefirst:area=feedback-context-allocation --> — 把 fresh evidence rotation 与 feedback scheduler 分开测量。 <!-- timefirst:delta=fresh-evidence-allocation-factorial --></summary>

**问题。** 多轮生成的收益来自 context volume、fresh evidence，还是 feedback-conditioned selection？ <!-- timefirst:question=context-allocation-causality -->

**证据。** fresh evidence factorial：`k=2,T=12` rotation 的 PR 为 0.397，fixed reuse 为 0.257；等总量 `(2,12)` 比 `(24,1)` 高 0.144。 <!-- timefirst:evidence=ascp-allocation~fresh-evidence-factorial -->

**限制。** scheduler rotation statistical tie：full ASCP 0.309 vs deep rotation 0.303（q=0.343），且没有 matched resource delta。17.5s 对 1.7s 来自顺序 `(2,12)` 对 one-shot `(24,1)`。 <!-- timefirst:caveat=ascp-attribution~scheduler-rotation-statistical-tie -->

**地图。** `early_signal`：加入 fresh-evidence context allocation；feedback control 的增量价值尚未建立。

**链接。** [The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search](https://arxiv.org/abs/2608.23252) · [代码](https://github.com/PeiYangLiu/ascp) · [英文深读](papers/2608.23252.md) · [中文深读](papers/2608.23252.zh.md)

</details>

<a id="entry-2608.19652"></a>
<details><summary>2026-08-24 · StateMem · State persistence → supersession-aware state <!-- timefirst:area=supersession-aware-state --> — 把“取回历史”和“判断哪些事实及依赖仍然有效”拆成两个问题。 <!-- timefirst:delta=supersession-aware-state-assembly --></summary>

**问题。** 当检索历史同时包含已作废和仍有效的事实时，agent 能否组装出当前状态？ <!-- timefirst:question=evolving-state-assembly -->

**证据。** StateMem value chain structure：六个 backend 上，StateMemWrapper 在相同 full transcript、chunks、call 与长度预算之外贡献 15.0–31.7 个点。 <!-- timefirst:evidence=statemem-control~statemem-value-chain-structure -->

**限制。** Synthetic benchmark upper bound：benchmark 针对的正是方法所编码的 lazy-reader failure family；完整 StateMem 约用 165–600 次 ingest LLM calls，dependency propagation 有时有害，DeepSeek/LongMemEval 的结构增量仅 −5 到 +5 个点。 <!-- timefirst:caveat=statemem-boundary~synthetic-benchmark-upper-bound -->

**地图。** `early_signal`：为 State persistence 加入 supersession-aware state assembly；单个 benchmark/method package 不构成 durable direction。

**链接。** [Can Agent Memory Systems Track Evolving State?](https://arxiv.org/abs/2608.19652) · [英文深读](papers/2608.19652.md) · [中文深读](papers/2608.19652.zh.md)

</details>

<a id="entry-2608.18613"></a>
<details><summary>2026-08-21 · CTIFoundry · Interface resolution → agent-native corpus scaffold <!-- timefirst:area=agent-native-corpus-scaffold --> — 在同一底层 agent 上，把平面语料改造成具名实体、关系与 typed operations 的证据路径。 <!-- timefirst:delta=typed-evidence-path-operations --></summary>

**问题。** 语料 scaffold 与可操作接口，而非更换 agent，能否改善跨文档证据导航？ <!-- timefirst:question=corpus-scaffold-operation-surface -->

**证据。** four-model panel 全部提升 0.190–0.275 F1；GPT-5.4 从 flat base 0.610 提升到 tools+skills full 0.829，且 tools-only 0.746 高于 skills-only 0.672。 <!-- timefirst:evidence=ctifoundry-package~four-model-panel -->

**限制。** tools skills bundled：完整处理同时改变图/实体索引、七种 typed tools、工具输出与描述、system prompt 及用户轮次 skills；没有对齐每个分支的 online 成本和更新生命周期。 <!-- timefirst:caveat=ctifoundry-attribution~tools-skills-bundled -->

**地图。** `reinforces`：与 VisDocAgentBench 共同加强“在共享输出契约下显式暴露证据路径操作”这一接口轴，不把整套增益归给检索或规划。

**链接。** [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](https://arxiv.org/abs/2608.18613) · [英文深读](papers/2608.18613.md) · [中文深读](papers/2608.18613.zh.md)

</details>

<a id="entry-2608.17889"></a>
<details><summary>2026-08-21 · VisDocAgentBench · Interface resolution → ranked visual retrieval <!-- timefirst:area=ranked-visual-retrieval --> — 用统一 top-10 opaque page 输出测试静态与 iterative visual target discovery。 <!-- timefirst:delta=bridge-path-acquisition-benchmark --></summary>

**问题。** 在页面级视觉检索中，iterative visual target discovery 能否弥补静态检索从直接目标到复杂目标的崩塌？ <!-- timefirst:question=iterative-visual-target-discovery -->

**证据。** iterative search ablation 中，GPT-5.6-sol 视觉路径 R@1 从无迭代的 53.33 提升到 61.67，OCR 路径从 27.50 提升到 36.67；但最强静态 Nemotron 在 L3 仅 2.5%。 <!-- timefirst:evidence=visdoc-iteration~iterative-search-ablation -->

**限制。** input token history 未匹配：完整视觉 agent 约 177K input tokens，对照约 101K；agent 后端是 Qwen single-vector，而最强静态对照是 Nemotron late-interaction。 <!-- timefirst:caveat=visdoc-attribution~input-token-history -->

**地图。** `reinforces`：与 CTIFoundry 一起强化显式证据路径操作，但当前证据不能分离 policy、retriever 与累积历史。

**链接。** [VisDocAgentBench: Benchmarking Agents for Visually Rich Document Retrieval](https://arxiv.org/abs/2608.17889) · [项目](https://hulx2002.github.io/VisDocAgentBench/) · [代码](https://github.com/hulx2002/VisDocAgentBench) · [英文深读](papers/2608.17889.md) · [中文深读](papers/2608.17889.zh.md)

</details>

<a id="entry-2608.16502"></a>
<details><summary>2026-08-21 · ToolScout · Interface resolution → capability retrieval <!-- timefirst:area=capability-retrieval --> — 揭示工具检索器可能把来源风格误当成能力匹配信号。 <!-- timefirst:delta=source-style-capability-routing --></summary>

**问题。** capability retrieval transfer 到混合工具源时，失败来自 agent planning，还是上游候选工具没有被召回？ <!-- timefirst:question=capability-retrieval-transfer -->

**证据。** source-style collapse：专用检索器在匹配来源 depth-20 coverage 为 91.8%，混合来源仅 22.3%；路由到来源聚合器后为 86.1%。 <!-- timefirst:evidence=toolscout-transfer~source-style-collapse -->

**限制。** end-to-end execution missing：工作测量候选覆盖与 proxy generation，并未执行工具完成任务；“来源风格”还混合 query–tool pairing 与目标侧分布。 <!-- timefirst:caveat=toolscout-scope~end-to-end-execution-missing -->

**地图。** `early_signal`：把 capability coverage audit 放到 agent planning 之前；单篇迁移诊断不足以建立稳定方向。

**链接。** [When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval](https://arxiv.org/abs/2608.16502) · [英文深读](papers/2608.16502.md) · [中文深读](papers/2608.16502.zh.md)

</details>

<a id="entry-2608.16417"></a>
<details><summary>2026-08-21 · D2-ScaleAgent · Adaptivity placement → evidence-sufficiency routing <!-- timefirst:area=evidence-sufficiency-routing --> — 让 verifier 根据 Evidence Bank 在继续找新页与深入已找到页面之间路由。 <!-- timefirst:delta=breadth-depth-evidence-routing --></summary>

**问题。** breadth versus depth allocation 是否能由当前证据充分性显式控制，而不是固定增加检索轮数？ <!-- timefirst:question=breadth-versus-depth-allocation -->

**证据。** verifier loop ablation：GPT-4o 在 MMLongBench 上完整系统为 52.0，移除 verifier 为 44.1，移除 retrieval scale 为 46.8；oracle 为 54.9。 <!-- timefirst:evidence=d2-verifier~verifier-loop-ablation -->

**限制。** unmatched adaptive compute：完整系统自身为 21.4K tokens、16.22 秒与 5.02 次 routing-agent calls，但未给关键对照的匹配成本；Gemini direct VQA 在两项主 benchmark 上更强。 <!-- timefirst:caveat=d2-attribution~unmatched-adaptive-compute -->

**地图。** `early_signal`：为 evidence-sufficiency routing 增加一个受控信号，不把整套视觉文档 agent 的收益单独归给 verifier。

**链接。** [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](https://arxiv.org/abs/2608.16417) · [英文深读](papers/2608.16417.md) · [中文深读](papers/2608.16417.zh.md)

</details>

<a id="entry-2608.16185"></a>
<details><summary>2026-08-17 · LENS · Evidence materialization <!-- timefirst:area=evidence-materialization --> — 把证据边界从索引时预先固定，改为查询时在原始文档上按预算定位。 <!-- timefirst:delta=query-time-raw-region-localization --></summary>

**问题。** 在动态语料中，固定 chunk/index 与查询时原始文档定位，谁能以可归因的成本取得更完整证据？ <!-- timefirst:question=dynamic-evidence-localization -->

**证据。** D500 上 LENS 为 62.4% EM / 84.8% evidence localization recall，ReAct-style search 为 65.2% / 50.4%；核心增益是证据定位与 grounding，而不是答案 EM。 <!-- timefirst:evidence=lens-grounding~evidence-localization-recall -->

**限制。** 在线 proposal 与 relevance oracle 会增加 online token latency；当前仍缺少与最新索引维护成本对齐的完整生命周期比较。 <!-- timefirst:caveat=lens-cost~online-token-latency -->

**地图。** `early_signal`：进入 Evidence materialization 轴，不凭单篇改写稳定地图。

**链接。** [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](https://arxiv.org/abs/2608.16185) · [英文深读](papers/2608.16185.md) · [中文深读](papers/2608.16185.zh.md)

</details>

<a id="entry-2608.16370"></a>
<details><summary>2026-08-17 · Context Compression Cost · Resource accounting → context reacquisition <!-- timefirst:area=state-persistence-cost --> — 揭示上下文压缩可能把 token 成本转移为后续重新获取式检索。 <!-- timefirst:delta=compression-reacquisition-tax --></summary>

**问题。** 任务完成情况不变时，上下文压缩是否会因丢失可查询状态而产生新的检索成本？ <!-- timefirst:question=compression-reacquisition-cost -->

**证据。** 固定 24-turn protocol 的代表性实验中，retrieval calls surge 从 21.0 增至 63.9，任务完成情况却没有显著变化；oracle 恢复被丢弃但仍可查询的状态后，多数额外交互消失。 <!-- timefirst:evidence=compression-cost~retrieval-calls-surge -->

**限制。** ALFWorld negative boundary 没有同样的激增；检索调用数也不等于完整的耗时或金钱成本。 <!-- timefirst:caveat=environment-boundary~alfworld-negative-boundary -->

**地图。** `early_signal`：把 retained state 与 reacquisition cost 放进同一资源核算，但不由单项结果创建趋势。

**链接。** [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](https://arxiv.org/abs/2608.16370) · [英文深读](papers/2608.16370.md) · [中文深读](papers/2608.16370.zh.md)

</details>

<a id="entry-2608.15191"></a>
<details><summary>2026-08-15 · RAAC · State persistence → progress control <!-- timefirst:area=progress-control --> — 根据 coverage、novelty、query diversity 与 drift 显式决定继续、转向或停止。 <!-- timefirst:delta=observable-search-progress --></summary>

**问题。** 同一个 deep-research agent 能否观察搜索进展，在证据饱和时停下、停滞时改变方向？ <!-- timefirst:question=stagnation-control -->

**证据。** BrowseComp-Plus search calls 平均约减少 14 次，同时平均准确率提高约 3 个百分点；对照是同一底层 agent 加或不加 RAAC overlay。 <!-- timefirst:evidence=raac-overlay~browsecomp-plus-search-calls -->

**限制。** Controller rethinker cost 包含额外 LLM 调用，因此搜索次数减少不能直接解释为总计算成本更低；不同 agent / dataset 的结果也不完全一致。 <!-- timefirst:caveat=raac-cost~controller-rethinker-cost -->

**地图。** `early_signal`：强化 progress state 作为控制面；结论仍需资源匹配与干预拆分。

**链接。** [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](https://arxiv.org/abs/2608.15191) · [英文深读](papers/2608.15191.md) · [中文深读](papers/2608.15191.zh.md)

</details>

<a id="entry-2608.12888"></a>
<details><summary>2026-08-13 · ReFind · Interface resolution → raw-chat retrieval <!-- timefirst:area=retrieval-interface --> — 说明带会话、时间和局部上下文控制的多轮访问，可让原始归档替代一部分预构建语义记忆。 <!-- timefirst:delta=raw-chat-runtime-access --></summary>

**问题。** 在运行时控制条件对齐后，收益来自预构建语义结构，还是来自 agent 可操作的会话、时间和局部上下文接口？ <!-- timefirst:question=structure-versus-interface -->

**证据。** LongMemEval interface ablation 中，完整 interface 为 93.2/89.3，高于 generic multi-round BM25 的 78.7/82.2 与 one-search 的 84.7/68.9；六任务 mean accuracy 为 58.2。 <!-- timefirst:evidence=refind-interface~longmemeval-interface-ablation -->

**限制。** Lifecycle cost unmatched：实验主要面向文本对话，回答时平均仍需约 2.5–2.6 次搜索与 5 次 LLM 调用，不能据此推断结构化记忆普遍无用。 <!-- timefirst:caveat=refind-scope~lifecycle-cost-unmatched -->

**地图。** `early_signal`：进入 Interface resolution 轴；证据支持强 runtime control，不是淘汰 semantic structure。

**链接。** [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](https://arxiv.org/abs/2608.12888) · [英文深读](papers/2608.12888.md) · [中文深读](papers/2608.12888.zh.md)

</details>

<a id="entry-2608.11967"></a>
<details><summary>2026-08-12 · LoongReflect · State persistence → reversible search state <!-- timefirst:area=reversible-search-state --> — 让 agent 回滚受污染的分支，保留纠错经验后继续检索。 <!-- timefirst:delta=trajectory-rollback-control --></summary>

**问题。** 长程搜索中，agent 能否删除不可靠的轨迹后缀，避免错误证据继续污染后续动作？ <!-- timefirst:question=reversible-trajectory-recovery -->

**证据。** Qwen2.5-3B 的 seven benchmark F1 平均为 46.15，AgenticRAG-R1 为 33.55；固定 retrieval environment/tool budget 的组件消融支持 reflection/backtracking 与两条训练通道的组合。 <!-- timefirst:evidence=loongreflect-package~seven-benchmark-f1 -->

**限制。** 教师在训练时可查看全局轨迹（privileged teacher information）；当前证据不能把全部增益归因于回滚语义本身。 <!-- timefirst:caveat=loongreflect-attribution~privileged-teacher-information -->

**地图。** `early_signal`：把 reversible state 纳入控制面；单项 recovery-learning package 不构成稳定趋势。

**链接。** [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](https://arxiv.org/abs/2608.11967) · [英文深读](papers/2608.11967.md) · [中文深读](papers/2608.11967.zh.md)

</details>

<a id="entry-2608.12282"></a>
<details><summary>2026-08-12 · VAKRA · Interface resolution → cross-source evaluation <!-- timefirst:area=cross-source-evaluation --> — 把 API、文档检索、策略约束与多跳推理放进同一条可重放轨迹。 <!-- timefirst:delta=executable-cross-source-trajectory --></summary>

**问题。** 模型能否在固定评测框架中跨 API 与文档获取证据，同时保持实体 grounding、策略合规与多跳组合？ <!-- timefirst:question=cross-source-grounding -->

**证据。** 最佳模型 single-hop 为 70.4%，compositional API accuracy 约 50–51%，部分 policy-constrained unanswerable setting 低至 2.4%；tool calls 会被重新执行。 <!-- timefirst:evidence=vakra-depth~compositional-api-accuracy -->

**限制。** Fixed ReAct harness 只能隔离模型能力，不能说明哪种 planner、memory 或 retrieval controller 能修复失败；聚合轨迹仍混合多种原因。 <!-- timefirst:caveat=vakra-attribution~fixed-react-harness -->

**地图。** `early_signal`：为跨源执行增加 evaluation coordinate，不把 benchmark 难度直接当作某种 controller 的证据。

**链接。** [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](https://arxiv.org/abs/2608.12282) · [代码](https://github.com/IBM/vakra) · [英文深读](papers/2608.12282.md) · [中文深读](papers/2608.12282.zh.md)

</details>

<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>
## 7 天 / 30 天变化

方向条目只按 Radar 接纳时间判断；legacy 论文仍可提供领域背景，但不能冒充滚动窗口支撑。

<a id="last-7-days"></a>
### 过去 7 天 · 2026-08-26—2026-09-01

- **`new_signal` · Interaction conditioned retrieval · trajectory state 进入 retriever ranking。** <!-- timefirst:direction key="interaction-conditioned-retrieval" state="new_signal" supports="2608.27912" confidence="medium" implication="separate-retriever-history-from-query-policy" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[ITER](#entry-2608.27912)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate-retriever-history-from-query-policy）：固定 agent、ranked interface 与 retriever backbone，分别改变 query history representation 和 trajectory-relative supervision，并报告 encoder/token/latency 成本；先验地图证据：`none`。

- **`new_signal` · Multimodal evidence persistence · 搜到视觉证据与后续还能访问它是两件事。** <!-- timefirst:direction key="multimodal-evidence-persistence" state="new_signal" supports="2608.28062" confidence="medium" implication="separate-evidence-acquisition-from-cross-turn-visibility" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[WeAgent-MMSearch](#entry-2608.28062)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate-evidence-acquisition-from-cross-turn-visibility）：固定 policy、tool inventory、returned results 与预算，只切换原始 modality 的跨 turn 可见性，再分别测 acquisition、later use 与完整资源；先验地图证据：`none`。

- **`new_signal` · Proactive context management · working context 本身成为可学习的 state-control surface。** <!-- timefirst:direction key="proactive-context-management" state="new_signal" supports="2608.28476" confidence="medium" implication="separate-context-tool-surface-from-edit-policy" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[ContextPilot](#entry-2608.28476)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate-context-tool-surface-from-edit-policy）：固定 tool inventory、SFT data、rollout budget 与 base model，分别改变 edit policy、partial-rollout selection 和 credit assignment，并计入 retention/offloading 成本；先验地图证据：`none`。

- **`new_signal` · Answerable working memory · 找到证据后，terminal state 仍可能丢失后续作答所需信息。** <!-- timefirst:direction key="answerable-working-memory" state="new_signal" supports="2608.25618" confidence="medium" implication="separate-page-access-memory-answerability-and-source-grounding" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[AWM](#entry-2608.25618)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate page access memory answerability and source grounding）：固定 retrieval trajectory 与 answer model 后，分别改变 memory-writing objective，并独立测 answerability、claim grounding 和 downstream control；先验地图证据：`none`。

- **`new_signal` · Span grounded evidence construction · verified spans 被物化为 claim-level support/conflict state。** <!-- timefirst:direction key="span-grounded-evidence-construction" state="new_signal" supports="2608.24667" confidence="medium" implication="separate-retrieval-recording-and-stopping-under-matched-budget" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[EviGraph](#entry-2608.24667)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate retrieval recording and stopping under matched budget）：固定 raw results、verifier、answer model 与预算，独立改变 evidence representation、recording 与 stopping；先验地图证据：`none`。

- **`new_signal` · Co evolving feedback routing · corrective feedback 变成可学习的 trajectory intervention。** <!-- timefirst:direction key="co-evolving-feedback-routing" state="new_signal" supports="2608.24794" confidence="medium" implication="match-feedback-calls-schedule-and-search-budget-before-attribution" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[CAFE](#entry-2608.24794)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（match feedback calls schedule and search budget before attribution）：匹配 feedback/search calls、tokens 与 schedule 后，再独立切换 request policy 和 critic quality；先验地图证据：`none`。

- **`new_signal` · Structurally bounded exploration · domain structure 可预先界定 candidate space 与 stopping。** <!-- timefirst:direction key="structurally-bounded-exploration" state="new_signal" supports="2608.24809" confidence="medium" implication="compare-bounded-and-open-search-under-one-output-contract" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Crase](#entry-2608.24809)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（compare bounded and open search under one output contract）：固定 corpus、seed retriever、generator、output contract 与预算，比较 fixed bound、adaptive expansion 与 open-ended search；先验地图证据：`none`。

- **`new_signal` · Experience amortized memory reranking · 经过判断的检索经验可成为复用的排序状态。** <!-- timefirst:direction key="experience-amortized-memory-reranking" state="new_signal" supports="2608.22767" confidence="medium" implication="measure-amortization-across-stores-and-query-orders" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[EARM](#entry-2608.22767)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（measure amortization across stores and query orders）：在固定 retrieval pool、顺序、calls、tokens 与 latency 下比较 retained experience 和 reacquisition；先验地图证据：`none`。

- **`new_signal` · Ownership isolated search validation · 搜索结果职责与证据验证可和答案综合分开。** <!-- timefirst:direction key="ownership-isolated-search-validation" state="new_signal" supports="2608.23045" confidence="medium" implication="hold-results-fixed-before-crediting-search" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[NIS-Agent](#entry-2608.23045)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（hold results fixed before crediting search）：在固定 search results 与预算时，分别干预 ownership、stopping 与 validation；先验地图证据：`none`。

- **`new_signal` · Contrastive requirement guided acquisition · 匹配任务上下文探针可限定源材料 procedure 的接纳范围。** <!-- timefirst:direction key="contrastive-requirement-guided-acquisition" state="new_signal" supports="2608.23417" confidence="medium" implication="match-acquisition-sources-and-budgets" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[SkillAlchemy](#entry-2608.23417)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（match acquisition sources and budgets）：固定 source inventory、tokens、calls、skill length 与下游 harness 后，再把增益归给 admission logic；先验地图证据：`none`。

- **`new_signal` · Typed constraint retention · 严重 compaction 下，hard constraints 可能需要单独保护的状态通道。** <!-- timefirst:direction key="typed-constraint-retention" state="new_signal" supports="2608.22752" confidence="medium" implication="match-metadata-and-downstream-context" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Compaction Cliff](#entry-2608.22752)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（match metadata and downstream context）：用等价 labels、retained tokens 与下游 context budgets 比较 typed 和 type-blind compaction；先验地图证据：`none`。

- **`new_signal` · Risk aware tool exposure · 执行前 shortlist 是可独立测量的风险面。** <!-- timefirst:direction key="risk-aware-tool-exposure" state="new_signal" supports="2608.22751" confidence="medium" implication="separate-exposure-from-execution-safety" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Risk-Aware Reranking](#entry-2608.22751)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate exposure from execution safety）：匹配 candidate pools，并分别报告 risk exposure、tool selection、execution outcomes 与 cost；先验地图证据：`none`。

<a id="last-30-days"></a>
### 过去 30 天 · 2026-08-03—2026-09-01

- **`new_signal` · Interaction conditioned retrieval · trajectory state 进入 retriever ranking。** <!-- timefirst:direction key="interaction-conditioned-retrieval" state="new_signal" supports="2608.27912" confidence="medium" implication="separate-retriever-history-from-query-policy" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[ITER](#entry-2608.27912)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate-retriever-history-from-query-policy）：固定 agent、ranked interface 与 retriever backbone，分别改变 query history representation 和 trajectory-relative supervision，并报告 encoder/token/latency 成本；先验地图证据：`none`。

- **`new_signal` · Multimodal evidence persistence · 搜到视觉证据与后续还能访问它是两件事。** <!-- timefirst:direction key="multimodal-evidence-persistence" state="new_signal" supports="2608.28062" confidence="medium" implication="separate-evidence-acquisition-from-cross-turn-visibility" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[WeAgent-MMSearch](#entry-2608.28062)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate-evidence-acquisition-from-cross-turn-visibility）：固定 policy、tool inventory、returned results 与预算，只切换原始 modality 的跨 turn 可见性，再分别测 acquisition、later use 与完整资源；先验地图证据：`none`。

- **`new_signal` · Proactive context management · working context 本身成为可学习的 state-control surface。** <!-- timefirst:direction key="proactive-context-management" state="new_signal" supports="2608.28476" confidence="medium" implication="separate-context-tool-surface-from-edit-policy" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[ContextPilot](#entry-2608.28476)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate-context-tool-surface-from-edit-policy）：固定 tool inventory、SFT data、rollout budget 与 base model，分别改变 edit policy、partial-rollout selection 和 credit assignment，并计入 retention/offloading 成本；先验地图证据：`none`。

- **`new_signal` · Answerable working memory · 找到证据后，terminal state 仍可能丢失后续作答所需信息。** <!-- timefirst:direction key="answerable-working-memory" state="new_signal" supports="2608.25618" confidence="medium" implication="separate-page-access-memory-answerability-and-source-grounding" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[AWM](#entry-2608.25618)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate page access memory answerability and source grounding）：固定 retrieval trajectory 与 answer model 后，分别改变 memory-writing objective，并独立测 answerability、claim grounding 和 downstream control；先验地图证据：`none`。

- **`new_signal` · Span grounded evidence construction · verified spans 被物化为 claim-level support/conflict state。** <!-- timefirst:direction key="span-grounded-evidence-construction" state="new_signal" supports="2608.24667" confidence="medium" implication="separate-retrieval-recording-and-stopping-under-matched-budget" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[EviGraph](#entry-2608.24667)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate retrieval recording and stopping under matched budget）：固定 raw results、verifier、answer model 与预算，独立改变 evidence representation、recording 与 stopping；先验地图证据：`none`。

- **`new_signal` · Co evolving feedback routing · corrective feedback 变成可学习的 trajectory intervention。** <!-- timefirst:direction key="co-evolving-feedback-routing" state="new_signal" supports="2608.24794" confidence="medium" implication="match-feedback-calls-schedule-and-search-budget-before-attribution" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[CAFE](#entry-2608.24794)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（match feedback calls schedule and search budget before attribution）：匹配 feedback/search calls、tokens 与 schedule 后，再独立切换 request policy 和 critic quality；先验地图证据：`none`。

- **`new_signal` · Structurally bounded exploration · domain structure 可预先界定 candidate space 与 stopping。** <!-- timefirst:direction key="structurally-bounded-exploration" state="new_signal" supports="2608.24809" confidence="medium" implication="compare-bounded-and-open-search-under-one-output-contract" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Crase](#entry-2608.24809)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（compare bounded and open search under one output contract）：固定 corpus、seed retriever、generator、output contract 与预算，比较 fixed bound、adaptive expansion 与 open-ended search；先验地图证据：`none`。

- **`new_signal` · Experience amortized memory reranking · 经过判断的检索经验可成为复用的排序状态。** <!-- timefirst:direction key="experience-amortized-memory-reranking" state="new_signal" supports="2608.22767" confidence="medium" implication="measure-amortization-across-stores-and-query-orders" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[EARM](#entry-2608.22767)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（measure amortization across stores and query orders）：在固定 retrieval pool、顺序、calls、tokens 与 latency 下比较 retained experience 和 reacquisition；先验地图证据：`none`。

- **`new_signal` · Ownership isolated search validation · 搜索结果职责与证据验证可和答案综合分开。** <!-- timefirst:direction key="ownership-isolated-search-validation" state="new_signal" supports="2608.23045" confidence="medium" implication="hold-results-fixed-before-crediting-search" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[NIS-Agent](#entry-2608.23045)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（hold results fixed before crediting search）：在固定 search results 与预算时，分别干预 ownership、stopping 与 validation；先验地图证据：`none`。

- **`new_signal` · Contrastive requirement guided acquisition · 匹配任务上下文探针可限定源材料 procedure 的接纳范围。** <!-- timefirst:direction key="contrastive-requirement-guided-acquisition" state="new_signal" supports="2608.23417" confidence="medium" implication="match-acquisition-sources-and-budgets" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[SkillAlchemy](#entry-2608.23417)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（match acquisition sources and budgets）：固定 source inventory、tokens、calls、skill length 与下游 harness 后，再把增益归给 admission logic；先验地图证据：`none`。

- **`new_signal` · Typed constraint retention · 严重 compaction 下，hard constraints 可能需要单独保护的状态通道。** <!-- timefirst:direction key="typed-constraint-retention" state="new_signal" supports="2608.22752" confidence="medium" implication="match-metadata-and-downstream-context" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Compaction Cliff](#entry-2608.22752)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（match metadata and downstream context）：用等价 labels、retained tokens 与下游 context budgets 比较 typed 和 type-blind compaction；先验地图证据：`none`。

- **`new_signal` · Risk aware tool exposure · 执行前 shortlist 是可独立测量的风险面。** <!-- timefirst:direction key="risk-aware-tool-exposure" state="new_signal" supports="2608.22751" confidence="medium" implication="separate-exposure-from-execution-safety" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Risk-Aware Reranking](#entry-2608.22751)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate exposure from execution safety）：匹配 candidate pools，并分别报告 risk exposure、tool selection、execution outcomes 与 cost；先验地图证据：`none`。

- **`reinforced` · Evidence path operation surfaces · 显式证据路径操作获得跨任务证据。** <!-- timefirst:direction key="evidence-path-operation-surfaces" state="reinforced" supports="2608.17889,2608.18613" confidence="medium" implication="make-evidence-path-operations-explicit" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="field-map" -->
  支撑：[VisDocAgentBench](#entry-2608.17889) · [CTIFoundry](#entry-2608.18613)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（make evidence path operations explicit）：在共享输出契约下显式暴露 search / resolve / traverse / inspect / read，并以匹配后端、harness 与预算的静态对照检验；先验地图证据：[Interface resolution](#field-map)。

- **`new_signal` · Evidence sufficiency routing · 证据充分性可路由广度与深度。** <!-- timefirst:direction key="evidence-sufficiency-routing" state="new_signal" supports="2608.16417" confidence="medium" implication="separate-page-coverage-from-reading-depth" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[D2-ScaleAgent](#entry-2608.16417)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate page coverage from reading depth）：分别测量新页面覆盖和已命中页面的深读，并对齐 verifier 的 token、调用与延迟；先验地图证据：`none`。

- **`new_signal` · Source conditioned capability routing · 工具能力召回受来源分布制约。** <!-- timefirst:direction key="source-conditioned-capability-routing" state="new_signal" supports="2608.16502" confidence="medium" implication="audit-capability-coverage-before-agent-planning" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[ToolScout](#entry-2608.16502)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（audit capability coverage before agent planning）：先核验候选工具覆盖与跨来源迁移，再把最终失败归因给 agent planning；先验地图证据：`none`。

- **`reinforced` · Supersession aware state assembly · 历史保留与 operative-state resolution 可分别放在回答时或写入时。** <!-- timefirst:direction key="supersession-aware-state-assembly" state="reinforced" supports="2608.19652,2608.23265" confidence="medium" implication="compare-answer-time-and-write-time-validity" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="field-map" -->
  支撑：[StateMem](#entry-2608.19652) · [EvoWiki](#entry-2608.23265)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（compare answer time and write time validity）：在 history access、extraction、answer context、update cost 与 dependency handling 匹配时移动 supersession resolution；先验地图证据：[State persistence](#field-map)。

- **`new_signal` · Fresh evidence context allocation · Fresh evidence, not scheduler complexity, is the current result.** <!-- timefirst:direction key="fresh-evidence-context-allocation" state="new_signal" supports="2608.23252" confidence="medium" implication="compare-freshness-with-feedback-under-matched-cost" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[ASCP](#entry-2608.23252)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（compare freshness with feedback under matched cost）：匹配 evidence、context、rounds、tokens 与 latency 后，先检验 rotation，再检验 feedback scheduler 的增量；先验地图证据：`none`。

- **`new_signal` · Retriever validated evidence chain supervision · 完整证据链可成为显式训练目标。** <!-- timefirst:direction key="retriever-validated-evidence-chain-supervision" state="new_signal" supports="2608.22479" confidence="medium" implication="separate-chain-reward-from-retrieval-substrate" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[GTA-RAG](#entry-2608.22479)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（separate chain reward from retrieval substrate）：固定 graph、retriever、interface、data 与 compute，再独立改变 trajectory reward；先验地图证据：`none`。

- **`new_signal` · Structured gap dual source routing · 显式 reasoning gap 可决定使用哪类来源。** <!-- timefirst:direction key="structured-gap-dual-source-routing" state="new_signal" supports="2608.22132" confidence="medium" implication="intervene-on-routing-separately-from-reasoning" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[SSE-Bio](#entry-2608.22132)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（intervene on routing separately from reasoning）：匹配 source inventory 与 orchestration，分别干预 routing、retrieval 与 downstream reasoning；先验地图证据：`none`。

- **`new_signal` · Visual evidence localization rewards · 视觉证据区域可进入奖励与输出契约。** <!-- timefirst:direction key="visual-evidence-localization-rewards" state="new_signal" supports="2608.21808" confidence="medium" implication="validate-semantic-support-beyond-box-overlap" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[MCite-RL](#entry-2608.21808)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（validate semantic support beyond box overlap）：匹配 crop/search budget，并用人工或可审计证据验证 bbox 是否真正支持答案；先验地图证据：`none`。

- **`new_signal` · Query time programmatic context materialization · Lossless history 可在查询时选择性进入 prompt。** <!-- timefirst:direction key="query-time-programmatic-context-materialization" state="new_signal" supports="2608.21690" confidence="medium" implication="price-retention-querying-and-materialization-together" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[Scroll](#entry-2608.21690)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（price retention querying and materialization together）：共同核算 retention、query program、environment execution 与 materialized prompt 的成本；先验地图证据：`none`。

- **`new_signal` · Conformal evidence set sizing · Retrieval width 可由 calibrated score mass 调整。** <!-- timefirst:direction key="conformal-evidence-set-sizing" state="new_signal" supports="2608.20771" confidence="medium" implication="test-calibration-under-shift-and-realized-budgets" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[CAS](#entry-2608.20771)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（test calibration under shift and realized budgets）：在 dataset shift 下核验 evidence validity，并对齐 realized documents、calls、tokens 与 latency；先验地图证据：`none`。

- **`new_signal` · Propagation conditioned failure attribution · Retrieval failure 需要 live intervention 才能定位。** <!-- timefirst:direction key="propagation-conditioned-failure-attribution" state="new_signal" supports="2608.20627" confidence="medium" implication="report-healing-survivors-and-probe-costs" timing="radar_published_at" synthesized="2026-09-01T01:24:01Z" prior="none" -->
  支撑：[AgenticRAG-FP](#entry-2608.20627)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-01T01:24:01Z`（UTC）；研究设计含义（report healing survivors and probe costs）：同时报告 healed/failed trajectories、各 depth denominator 与 active probe 的 token/tool/latency 成本；先验地图证据：`none`。

封闭周期与长期压缩：[weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a><a id="research-map"></a>
## 领域地图

![Agentic RAG 领域设计轴](assets/editorial/field-overview.svg)

> **先建立一个简单模型：** `need information → search/access evidence → inspect → decide where/if to search again → answer or act`
>
> **当前判断：** “retriever 还是 agent”“一次 search 还是多次 search”都太粗。更稳定的设计轴是：**adaptivity 放在哪、evidence 何时 materialize、哪些 state 跨 action 保留、offline + online 到底花了多少资源。**

`information need → query/planning → retrieval interface → evidence materialization → inspection/reasoning → continue/redirect/stop → persistent state → answer/action`

| Axis | 核心问题 | 当前张力 |
|---|---|---|
| **Adaptivity placement** | 哪些操作可以在看到证据前预先编排，哪些必须根据返回结果调整？ | `pre-query compilation ↔ query-time adaptation` |
| **Evidence materialization** | 何时应把文本块、区域或工作区固化为可操作对象？ | `pre-materialized index ↔ raw/query-conditioned evidence` |
| **Interface resolution** | Agent 能观察和控制哪些检索操作与来源状态？ | `opaque top-k ↔ explicit search/resolve/traverse/inspect/read under shared output contract` |
| **State persistence** | 哪些证据、进度和推理状态应跨动作保留？ | `stateless loop ↔ persistent/recoverable state`；当前设计点：`answer-time ↔ write-time supersession resolution` |
| **Resource accounting** | 哪种方案的生命周期总成本更低？ | `local retrieval metric ↔ lifecycle cost + task outcome` |

[进入完整 research-question map →](categories/README.md) · [Research-question visual](assets/editorial/research-question-map.svg) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-rag)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该学到什么 |
|---|---|---|
| **检索控制和证据形成应放在哪个环节？** | [SIRA](papers/2605.06647.md) → [ITER](papers/2608.27912.zh.md) → [WeAgent-MMSearch](papers/2608.28062.zh.md) → [ContextPilot](papers/2608.28476.zh.md) | 从查询前编排，到结果条件式访问、查询时定位，再到跨轮 fresh evidence allocation；每次移动都要问 work 被放到了哪里。 |
| **哪些状态值得保留？** | [StateMem](papers/2608.19652.zh.md) → [EvoWiki](papers/2608.23265.zh.md) → [Context Compression Cost](papers/2608.16370.md) → [Scroll](papers/2608.21690.zh.md) | operative validity 可以在 answer time 或 write time 解析；reacquisition cost 与 lossless programmatic state 仍是另外两类 retained-state 问题。 |
| **怎样对检索结论做因果归因？** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [VAKRA](papers/2608.12282.md) → [AgenticRAG-FP](papers/2608.20627.zh.md) | 从 evidence coverage、interface/harness 匹配，到跨源执行和 live fault intervention，逐层定位因果路径。 |

<a id="library"></a>
## 研究资料库

历史工作可按问题与设计张力浏览，也可按论文或时间查找。

[按问题、研究路线与年份浏览](library/README.md) · [研究问题地图](categories/README.md) · [论文时间索引](papers/README.md) · [时间维度综述](digests/README.md)

## 怎么用这个 Radar

**先扫**时间线折叠行；**再展开**问题、证据、限制与地图影响；需要核验结论时进入深读。只有问题、没有论文名时，从领域地图或资料库进入。

## 收录范围

纳入的工作需要让 Agent 对**是否、检索什么、去哪里检索、如何检索、检索多少**拥有实质控制，或者改变支持这种控制的持久信息状态。普通固定式 RAG 如果没有真正的控制、接口或状态贡献，通常不纳入。

## 维护

这是研究判断地图，而不是穷举式信息流。证据标准是：**改了什么？与什么比较？实际固定了什么？还有哪些混杂因素？**

[Contributing](CONTRIBUTING.md) · [Curation](CURATION.md) · [Daily workflow](docs/DAILY_WORKFLOW.md)
