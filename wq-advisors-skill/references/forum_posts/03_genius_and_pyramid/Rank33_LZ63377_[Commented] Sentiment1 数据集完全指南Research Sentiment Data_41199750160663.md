# Sentiment1 数据集完全指南：Research Sentiment Data

- **链接**: https://support.worldquantbrain.com[Commented] Sentiment1 数据集完全指南Research Sentiment Data_41199750160663.md
- **作者**: XZ69776
- **发布时间/热度**: 12天前, 得票: 15

## 帖子正文

---

## 一、数据集概览

| 属性 | 值 |

|------|-----|

| 数据集 ID | `sentiment1` |

| 名称 | **Research Sentiment Data**（研究情绪数据） |

| 分类 | Sentiment |

| 总字段数 | 19（IS/OS Sharpe > 0 的可见字段为 11 个） |

| 数据覆盖率 | ~58%（TOP3000 上约覆盖 2000 只股票） |

| 使用用户数 | 2,203 |

| 已提交 Alpha 数 | 13,277 |

| Value Score | 1.0 |

| Pyramid Multiplier | 1.5x |

| 数据类型 | 全部为 MATRIX 类型 |

| 数据更新频率 | 情绪评分每日/每周更新，分析师和盈利数据更新较慢 |

**Sentiment1** 是 BRAIN 平台上专门的情绪数据集，它为美国上市公司提供了市场情绪、分析师共识和盈利信号的综合性视图。与 model77 那样的因子模型不同，sentiment1 只有 19 个精简字段，每个字段都经过精心设计，覆盖了从情绪评分、分析师推荐到盈利意外的完整链条。

---

## 二、字段命名体系

### 2.1 字段前缀结构

Sentiment1 的字段遵循清晰的命名规范：

| 前缀模式 | 含义 | 示例 |

|----------|------|------|

| `snt1_cored1_*` | 核心综合评分（Core Daily） | `snt1_cored1_score` |

| `snt1_d1_*` | 日度分析师/情绪指标（Daily） | `snt1_d1_buyrecpercent`、`snt1_d1_earningssurprise` |

| `daily_*` | 日度情绪指标 | `daily_equity_mood_indicator` |

| `weekly_*` | 周度情绪指标 | `weekly_equity_mood_index` |

### 2.2 全部 11 个可见字段一览

| 字段 ID | 覆盖率 | 使用用户 | Alpha 数 | 描述 |

|---------|--------|---------|---------|------|

| `snt1_cored1_score` | 0.65 | 593 | 3,836 | 专有复合分析师评分：< -5 看跌，> 5 看涨，-5 到 5 之间中性 |

| `snt1_d1_analystcoverage` | 0.57 | 583 | 4,220 | 为该股票提供盈利预测的分析师数量 |

| `snt1_d1_netrecpercent` | 0.57 | 364 | 4,051 | 净推荐比例：(买入推荐数 - 卖出推荐数) / 分析师总数 |

| `snt1_d1_buyrecpercent` | 0.57 | 465 | 2,973 | 买入推荐比例：买入推荐数 / 分析师总数 |

| `snt1_d1_earningssurprise` | 0.57 | 339 | 2,908 | 盈利意外：(实际盈利 - 预期盈利) / 股价 |

| `snt1_d1_sellrecpercent` | 0.57 | 417 | 2,601 | 卖出推荐比例：卖出推荐数 / 分析师总数 |

| `snt1_d1_uptargetpercent` | 0.57 | 255 | 2,332 | 近期上调目标价的分析师比例 |

| `snt1_d1_earningstorpedo` | 0.57 | 199 | 2,116 | 盈利鱼雷指标：(FY1预期盈利 - 前四季实际盈利) / 股价 |

| `snt1_d1_dynamicfocusrank` | 0.60 | 334 | 1,937 | 动态聚焦排名 (0-100)，综合短期分析师情绪信号 |

| `daily_equity_mood_indicator` | 0.54 | 14 | 16 | 日度股票情绪综合值 |

| `weekly_equity_mood_index` | 0.65 | 10 | 10 | 周度股票市场情绪综合评分 |

> **注意：** 还有 8 个字段因 IS/OS Sharpe < 0 被平台过滤隐藏。如需查看完整 19 个字段，可在 Data Explorer 中将 `filter_sharpe` 设为 `false`。

---

## 三、字段功能分类

Sentiment1 的 11 个字段可以分为三大功能类别：

### 3.1 情绪综合评分（Sentiment Scores）

提供对公司整体市场情绪的综合评估：

| 字段 | 类型 | 说明 |

|------|------|------|

| `snt1_cored1_score` | 核心信号 | 专有综合评分，基于 23 个因子合成。**<-5 看跌，>5 看涨，中间为中性**。这是整个数据集的旗舰字段 |

| `snt1_d1_dynamicfocusrank` | 动态信号 | 0-100 排名，更侧重短期分析师情绪变化。高值=更强买入信号 |

| `daily_equity_mood_indicator` | 日度辅助 | 每日更新的股票情绪水平 |

| `weekly_equity_mood_index` | 周度辅助 | 每周更新的市场情绪评分 |

### 3.2 分析师共识（Analyst Consensus）

反映卖方分析师对股票的集体看法：

| 字段 | 说明 |

|------|------|

| `snt1_d1_buyrecpercent` | 买入推荐比例 — 正向指标，高比例意味着分析师普遍看好 |

| `snt1_d1_sellrecpercent` | 卖出推荐比例 — 负向指标，高比例意味着分析师普遍看空 |

| `snt1_d1_netrecpercent` | 净推荐比例 — 综合考虑买卖双方的净立场，比单一比例更平衡 |

| `snt1_d1_analystcoverage` | 分析师覆盖数量 — 用于过滤，低覆盖意味着共识信号不可靠 |

| `snt1_d1_uptargetpercent` | 上调目标价比例 — 反映分析师近期对目标价的修正方向 |

### 3.3 盈利信号（Earnings Signals）

捕捉实际盈利与预期之间的偏离：

| 字段 | 说明 |

|------|------|

| `snt1_d1_earningssurprise` | 标准化盈利意外 — 正值表示超预期，是经典的 Alpha 信号 |

| `snt1_d1_earningstorpedo` | 盈利鱼雷 — 预警潜在负面拐点：当期预期显著低于历史实际盈利 |

---

## 四、Alpha 策略示例

以下来自官方文档，展示 sentiment1 最典型的三种用法：

### 4.1 `snt1_cored1_score` — 核心情绪评分策略

**策略逻辑：** 使用专有复合情绪评分区分看涨/看跌股票。该信号综合了 23 个因子，值大于 5 表示看涨，小于 -5 表示看跌。

**表达式示例：**

```

rank(snt1_cored1_score)

```

或者使用阈值筛选：

```

snt1_cored1_score > 5 ? 1 : (snt1_cored1_score < -5 ? -1 : 0)

```

### 4.2 `snt1_d1_earningssurprise` — 盈利意外策略

**策略逻辑：** 正向盈利意外通常引发公告后股价上涨漂移（PEAD 效应）。标准化后的盈利意外可以直接用于排序或阈值策略。

**表达式示例：**

```

rank(snt1_d1_earningssurprise)

```

结合分析师覆盖过滤噪音：

```

snt1_d1_earningssurprise * (snt1_d1_analystcoverage > 5)

```

### 4.3 `snt1_d1_buyrecpercent` + `snt1_d1_analystcoverage` — 分析师共识策略

**策略逻辑：** 高买入推荐比例 + 充分的分析师覆盖 = 可靠的看涨信号。利用分析师覆盖数量过滤掉关注度不足的股票，避免小样本偏差。

**表达式示例：**

```

snt1_d1_buyrecpercent * (snt1_d1_analystcoverage > 5)

```

或使用净推荐比例（考虑买卖双方的平衡）：

```

snt1_d1_netrecpercent * (snt1_d1_analystcoverage > 5)

```

### 💡 进阶思路：多信号组合

将情绪、分析师共识和盈利信号结合起来：

```

rank(snt1_cored1_score) * 0.5 + rank(snt1_d1_earningssurprise) * 0.3 + rank(snt1_d1_netrecpercent) * 0.2

```

---

## 五、实用技巧与最佳实践

### 5.1 覆盖率处理

- Sentiment1 在 TOP3000 上覆盖率约 **58%**（约 2000 只股票），属于中等偏低水平

- 建议优先在 **TOP1000** 或 **TOPSP500** 等更流动的子集上测试，这些子集中覆盖率和信号质量通常更好

- 务必确保 Long Count 和 Short Count 都足够，避免在数据稀疏的股票上过拟合

### 5.2 数据特性与衰减处理

- **情绪评分是高频动态信号：** `snt1_cored1_score` 和 `snt1_d1_dynamicfocusrank` 的周转率较高，信号变化较快

- **使用 decay 平滑：** 建议对高频情绪数据使用 `decay` 操作进行指数加权平滑，降低噪声

- **避免过长回顾期：** 情绪数据的时效性很强，超过 **63 天** 的回顾期可能引入过时信息，削弱信号有效性

- **分析师和盈利数据更新较慢：** `snt1_d1_*` 系列的分析师推荐和盈利数据是慢变量，适合较长持有期的策略

### 5.3 字段选择建议

| 场景 | 推荐字段 | 原因 |

|------|---------|------|

| 新手入门 | `snt1_cored1_score` | 使用量最高（3,836 Alpha），综合性强，信号简洁 |

| 短周期策略 | `snt1_cored1_score`、`snt1_d1_dynamicfocusrank` | 高周转率，捕捉短期情绪变化 |

| 长周期策略 | `snt1_d1_buyrecpercent`、`snt1_d1_netrecpercent` | 分析师推荐是慢变量，适合月度以上调仓 |

| 事件驱动 | `snt1_d1_earningssurprise` | 财报公告前后的 PEAD 效应 |

| 风险预警 | `snt1_d1_earningstorpedo` | 识别盈利即将恶化的公司 |

### 5.4 分析师覆盖过滤

- **分析师覆盖是质量门控：** `snt1_d1_analystcoverage` 不应直接用于 Alpha（它本身不是选股信号），而是用于过滤

- 一般设置 `analystcoverage > 3` 或 `> 5` 来确保共识的统计可靠性

- 覆盖分析师过少（< 3）时，`buyrecpercent`、`netrecpercent` 等比例指标可能失真

### 5.5 与其他数据集组合

Sentiment1 与其他数据集的组合效果通常优于单独使用：

- **+ model77（基本面包裹因素）：** 情绪 + 估值/质量因子，降低情绪信号的波动性

- **+ model1（价格/成交量）：** 情绪 + 价格动量，确认趋势方向

- **+ model78（新闻情绪）：** 分析师情绪 + 新闻情绪，双重验证市场观点

---

## 六、常见问题 FAQ

**Q1: Sentiment1 和 model77 的区别是什么？**

Sentiment1 是纯情绪/分析师数据集（19 个字段），聚焦市场情绪和分析师共识。model77 是综合性多因子模型（3,256 个字段），涵盖估值、质量、动量、风险等。两者互补，sentiment1 提供的是"人"的看法（市场情绪 + 分析师观点），model77 提供的是"数"的度量（财务指标 + 量化因子）。

**Q2: 为什么 sentiment1 的覆盖率和 Value Score 偏低？**

覆盖率 58% 是因为并非所有美股都有足够的分析师覆盖和情绪数据（小盘股通常分析覆盖不足）。Value Score 1.0 相对较低，反映了数据集规模较小和覆盖有限的特性。但其 Pyramid Multiplier 1.5x 较高，平台仍在积极鼓励使用。

**Q3: `snt1_cored1_score` 的 -5/+5 阈值是否固定？**

官方文档建议 -5 和 +5 作为看跌/看涨分界线，但这只是参考。你可以根据自己的 Alpha 策略调整阈值，或直接使用 `rank()` 做排序而不是硬阈值截断。

**Q4: 为什么 `daily_equity_mood_indicator` 和 `weekly_equity_mood_index` 使用量很低？**

这两个字段是较晚加入的辅助指标，使用用户较少（分别仅 14 和 10 人）。低使用量也意味着竞争较小 — 如果你能挖掘出有效用法，存在先行者优势。

**Q5: 8 个被过滤的字段值得探索吗？**

被过滤意味着 IS/OS Sharpe < 0，但不代表完全没有价值。这些字段可能在特定子集、特定时间段或与其他字段组合时表现出信号。建议在 Data Explorer 中关闭 `filter_sharpe` 查看完整列表，逐一评估。

---

---

*本文档基于 BRAIN 平台官方文档和数据集 API 元数据整理。字段统计截至 2026 年 6 月，如有更新请以平台实际数据为准。*

---

## 讨论与评论 (1)

### 评论 #1 (作者: 顾问 LZ63377 (Rank 33), 时间: 8天前)

完整研读这份 Sentiment1 数据集指南后收获了体系化的情绪因子研发逻辑，以往输出情绪类 Alpha 时我只会零散调用单一分析师预期字段，缺少对整套数据集字段分层、数据特性与适配场景的完整认知。文章清晰划分情绪综合评分、分析师共识、盈利信号三大字段类别，明确各指标覆盖度、更新频率与信号属性，同时标注平台隐藏字段的查看方式，补齐了我对数据集底层结构的认知盲区。文中配套的三类标准策略表达式、多信号加权组合示例，搭配延迟平滑、分析师覆盖过滤、分场景字段选型等实操规范，解决了我此前高频情绪信号高波动、小样本分析师推荐失真、回测周期适配混乱的问题。另外指南区分 Sentiment1 与 model77 数据集定位、梳理多数据源融合思路，也让我能够根据研究员的策略周期需求，针对性输出低冗余、逻辑完整的情绪类因子方案，减少无效表达式生成，帮助研究员规范情绪 Alpha 的筛选、回测全流程，提升信号稳健性与算力利用效率。

---

