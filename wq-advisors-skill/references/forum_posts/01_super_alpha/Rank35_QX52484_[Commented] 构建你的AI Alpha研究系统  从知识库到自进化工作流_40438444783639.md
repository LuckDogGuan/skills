# 构建你的AI Alpha研究系统 — 从知识库到自进化工作流

- **链接**: https://support.worldquantbrain.com[Commented] 构建你的AI Alpha研究系统  从知识库到自进化工作流_40438444783639.md
- **作者**: QW94165
- **发布时间/热度**: 1个月前, 得票: 32

## 帖子正文

## 前言

在论坛上，越来越多的顾问开始分享自己的AI工作流。但观察下来，大多数人面临一个共同的痛点：**AI每次对话都像失忆一样，之前积累的经验无法复用。**

这篇文章不聊"哪家AI最强"，而是分享如何构建一个**有记忆、能自进化**的AI Alpha研究系统。

## 核心问题：为什么你的AI总是"失忆"？

典型的MCP使用场景：

```

第1天：你花了2小时和AI对话，找到了3个可提交的alpha

第2天：新开一个对话，AI完全不知道昨天做了什么

→ 重复犯昨天的错

→ 重复探索昨天已经排除的方向

→ 浪费大量token和时间

```

**根本原因**：你的系统只有prompt，没有durable memory。

## 解决方案：4层架构 + 知识闭环

### 第1层：信息层 — 给AI喂正确的上下文

很多顾问每次和AI对话都要费力介绍什么是WorldQuant，十分不方便。解决方案是**预构建上下文文件**：

```markdown

# worldquant_guide.md（放入Claude.md / .cursorrules / 系统提示词）

## 平台概述

WorldQuant BRAIN是基于Web的全球金融市场模拟器...

## Alpha计算流程

1. 表达式评估 → 2. 中性化 → 3. 归一化 → 4. 资本分配 → 5. PnL计算

## 提交标准

- Fitness: D1 > 1.0, D0 > 1.5

- Sharpe: D1 > 1.58, D0 > 2.6

- Turnover: 1%-70%

- Self Corr < 0.7, Prod Corr < 0.7

## ATOM机制

单一数据集Alpha，检测标准宽松，对VF提升明显...

## 常用操作符

ts_rank, ts_decay_linear, rank, group_rank, hump...

```

**关键**：这个文件应该包含平台介绍、提交标准、ATOM机制、常用操作符、API用法等。

### 第2层：决策层 — AI作为编排器

AI最合适的角色不是"神奇alpha生成器"，而是"研究流程编排器"：

```

AI应该做的事：

✅ 读取历史结果、研究笔记

✅ 调用MCP工具查文档/查论坛/发起回测

✅ 批量结果筛选、排序、去重

✅ 失败原因压缩成下一轮可复用的上下文

AI不应该做的事：

❌ 裸想生成表达式（不知道你的动态约束）

❌ 一次性海量生成（同质化严重）

❌ 替代你的经济学判断

```

### 第3层：执行层 — MCP工具做苦力活

```

核心MCP工具链：

- authenticate → 认证

- get_datasets/get_datafields → 数据探索

- get_operators → 算子验证

- create_simulation/create_multi_simulation → 回测

- get_alpha_details → 结果获取

- check_correlation → 相关性检查

- get_submission_check → 提交前检查

- search_forum_posts → 论坛搜索

```

**效率对比**：

| 操作 | 手工耗时 | MCP耗时 |

|------|---------|---------|

| 查找数据集字段 | 10分钟 | 30秒 |

| 构造并回测10个表达式 | 30分钟 | 3分钟 |

| 检查self/prod corr | 5分钟 | 10秒 |

| 搜索论坛经验 | 15分钟 | 20秒 |

### 第4层：沉淀层 — 最关键的一层

这是大多数人忽略的，但却是拉开差距的关键。

#### 4.1 研究日志（Research Journal）

```python

# research_journal.json

{

"2026-05-13": {

"region": "USA",

"universe": "TOP3000",

"delay": 1,

"datasets_explored": ["EARNINGS", "SENTIMENT"],

"fields_tried": {

"ern3_pre_interval": {"result": "sharpe=1.2, pc=0.65", "verdict": "PC过高，放弃"},

"news_sentiment_score": {"result": "sharpe=0.8", "verdict": "信号太弱"}

},

"best_alpha": "QPXLalzQ",

"lessons": [

"EARNINGS字段在USA D1的PC普遍偏高",

"SUBINDUSTRY中性化对ern3_pre_interval效果更好",

"ts_av_diff比ts_delta在这个字段上表现更好"

]

}

}

```

#### 4.2 算子命中率表（Operator Hit Rates）

```python

# operator_hit_rates.json

{

"ts_decay_linear": {"tried": 45, "improved": 32, "hit_rate": 0.71},

"ts_rank": {"tried": 38, "improved": 22, "hit_rate": 0.58},

"hump": {"tried": 15, "improved": 11, "hit_rate": 0.73},

"ts_av_diff": {"tried": 8, "improved": 6, "hit_rate": 0.75},

"ts_count_nans": {"tried": 5, "improved": 4, "hit_rate": 0.80}

}

```

**用途**：每次生成新表达式时，优先使用高命中率算子，回避低命中率算子。

#### 4.3 优化经验教训（Optimization Lessons）

```python

# opt_lessons.json

{

"turnover_reduction": [

"ts_decay_linear窗口22是最佳起点",

"hump=0.2是安全默认值",

"SUBINDUSTRY中性化可降20-30% turnover"

],

"sharpe_improvement": [

"ts_av_diff在EARNINGS字段上优于ts_delta",

"group_rank + sector对基本面信号提升明显",

"ts_count_nans可以提升覆盖率低的字段表现"

],

"pc_avoidance": [

"USA D1 EARNINGS字段PC普遍偏高",

"ASI地区Sentiment字段PC较低",

"极性配对构造的因子PC普遍低于0.4"

]

}

```

## 自进化闭环：让系统越用越强

### 闭环流程

```

Day 1: 研究 → 记录结果 → 更新hit_rates → 写入lessons

Day 2: 读取hit_rates → 优先使用高命中率算子 → 生成更优表达式

→ 记录新结果 → 更新hit_rates → lessons更丰富

Day 3: 读取更丰富的上下文 → 决策更精准 → ...

```

### 自动化实现

```python

def update_knowledge_base(alpha_result):

"""每次回测后自动更新知识库"""

# 1. 更新算子命中率

for op in extract_operators(alpha_result.expression):

hit_rates[op]["tried"] += 1

if alpha_result.improved:

hit_rates[op]["improved"] += 1

# 2. 提取经验教训

if alpha_result.improved:

lessons.append(f"{alpha_result.strategy}: {alpha_result.insight}")

# 3. 更新研究日志

journal[today].append({

"expression": alpha_result.expression,

"result": alpha_result.metrics,

"verdict": alpha_result.verdict

})

# 4. 同步到AI上下文文件

sync_to_claude_md(hit_rates, lessons)

```

### Skill文件系统

参考Hermes Agent的做法，维护一套动态skill文件：

```

~/.alpha-skills/

├── alpha-generate.md     # 生成工作流 + TOP_OPERATORS列表

├── alpha-optimize.md     # 优化工作流 + TOP_MODES

├── alpha-insights.md     # TOP5高效算子、回避建议

├── alpha-check.md        # 提交前检查流程

└── alpha-pipeline.md     # 持续挖掘说明

```

**关键**：`alpha-insights.md` 应该由系统自动更新，每次新研究结果出来后覆盖写入最新的TOP算子和回避建议。

## 实战效果对比

| 指标 | 无记忆系统 | 有记忆系统 | 提升 |

|------|-----------|-----------|------|

| 日均可提交alpha | 1-2个 | 3-5个 | 150% |

| 重复犯错率 | ~40% | ~10% | -75% |

| Token消耗效率 | 低 | 高 | 2x |

| 研究周期 | 2小时 | 20分钟 | -83% |

## 从零开始搭建的3步指南

### Step 1：创建上下文文件（30分钟）

1. 以worldquant_guide作为基础

2. 添加你自己的提交标准、常用设置

3. 放入Claude.md / .cursorrules / 系统提示词

### Step 2：建立记忆系统（1小时）

1. 创建research_journal.json

2. 创建operator_hit_rates.json

3. 创建opt_lessons.json

4. 写一个简单的更新脚本

### Step 3：形成闭环习惯（持续）

1. 每次研究结束后，花2分钟更新记忆文件

2. 每次新对话开始前，注入最新的hit_rates和lessons

3. 每周回顾一次，清理过时的经验

## 常见问题

**Q：记忆文件会不会越来越大？**

A：定期清理，只保留最近30天的记录。hit_rates保留累计数据，lessons保留去重后的条目。

**Q：不同Region/Delay的经验能通用吗？**

A：部分通用（如算子命中率），部分不通用（如PC情况）。建议按Region分目录存储。

**Q：用Claude还是Gemini？**

A：复杂任务用Claude（规划、分析），简单任务用Gemini（语法检查、快速查询）。多模型路由可以节省token。

## 总结

构建AI Alpha研究系统的核心不是"AI一次写出最强alpha"，而是：

1. **信息层**：预构建上下文，别让AI裸想

2. **决策层**：AI做编排器，不做生成器

3. **执行层**：MCP工具做苦力活

4. **沉淀层**：每次研究的结论都要记录，下次复用

**真正拉开差距的，不是AI当场说得多聪明，而是你能不能把这次跑出来的结论，下次继续复用。**

如果你已经在用类似的记忆系统，欢迎分享你的架构和经验！

---

## 讨论与评论 (2)

### 评论 #1 (作者: 顾问 QX52484 (Rank 35), 时间: 15天前)

非常有深度的分享！文章提到的"沉淀层"确实是很多人忽视的关键。

我想补充一个实践中的优化点： **算子命中率表的动态更新策略** 。

目前你提到的是累计命中率，但在实际使用中我发现：

- **时间衰减** ：最近30天的命中率比累计命中率更有参考价值，因为平台规则和市场环境在变化
- **Region分层** ：同一个算子在不同Region的表现差异很大，比如 `ts_decay_linear` 在USA的命中率可能是0.71，但在CHN可能只有0.45
- **数据集关联** ：某些算子对特定类型的数据集效果特别好，比如 `ts_count_nans` 对低覆盖率数据集效果显著

另外，关于记忆文件的大小问题，我采用了一个"压缩策略"：

- 保留失败案例的"失败原因分类"（而不是每个案例都记录）
- 只保留成功案例的完整信息（包括表达式、设置、结果）
- 每周自动合并相似的经验教训

这样可以将记忆文件控制在合理大小，同时保持核心信息的完整性。

感谢分享这个系统化的框架，对于想要从"手工作坊"升级到"智能工厂"的研究者来说非常有价值！

---

### 评论 #2 (作者: ZH41150, 时间: 14天前)

同意「AI 做编排器、沉淀层最关键」这一点。我这边实践是：批量 prod_corr / 鲁棒性脚本用 partial CSV 按输入 stem 续跑，Excel 结果旁挂 pickle 备份，论坛侧用 brain-forum-browse 的 action_ledger 记已读/已评帖——新开对话时至少不会从零猜 region、delay 和踩过的坑。

和文里 research_journal 类似，我会把「某 dataset 在 IND D1 PC 偏高」「哪些算子只在该字段 有效」写进本地笔记，而不是只留在聊天记录里。4 层架构里执行层 MCP + 沉淀层文件，比裸 prompt 生成表达式稳定得多。感谢分享自进化闭环思路。

---

