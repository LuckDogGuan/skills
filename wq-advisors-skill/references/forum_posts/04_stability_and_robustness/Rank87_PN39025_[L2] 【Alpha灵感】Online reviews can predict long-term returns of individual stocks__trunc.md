# 【Alpha灵感】Online reviews can predict long-term returns of individual stocks

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Online reviews can predict long-term returns of individual stocks_19294427764759.md
- **作者**: XM91020
- **发布时间/热度**: 2 years ago, 得票: 5

## 帖子正文

论文概述：

论文探讨了网上评论对股票长期回报的预测能力，特别是针对个股。作者基于1800多万条产品评论，从中提取了6246个特征，分为13个类别，建立了预测模型。通过交叉验证测试，作者选择的最佳分类器在准确性上比使用10个技术指标的领先解决方案提高了13.94%，相对随机值提高了18.28%。在现实场景中对模型的稳健性进行了评估和验证，证实了网上评论可以预测个股的长期回报。这项研究为长期投资个股的投资者提供了新的机会。

Author: Junran Wua, Ke Xua, Jichang Zhao

Year: 2019

Link:  [https://arxiv.org/abs/1905.03189](https://arxiv.org/abs/1905.03189)

参考数据集：

**Term**

**Datafield**

**Dataset**

related post

scl4_posts_total_tb

[Socialmedia4](https://platform.worldquantbrain.com/learn/data-and-operators/socialmedia4)

emotion

scl3_averagesentiment

[Socialmedia3](https://platform.worldquantbrain.com/learn/data-and-operators/socialmedia3)

因子构建：


> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1/TOP3000
> Convert to Multi-Simulation
> 1
> #
> Define
> the
> relevant
> datafields
> 2
> reviews_total
> SCI4_posts_total_tb;
> # Total
> number
> of posts
> related
> to
> the
> Stock
> 3
> average_sentiment
> SCl3_averagesentiment;
> # Average sentiment
> 0f
> the
> Stock's
> online
> reViews
> 5
> #
> Define parameters
> for
> the
> strategy
> 6
> long_threshold
> 0.5;
> # Threshold
> for entering
> long position
> short_threshold
> -0.5;
> # Threshold
> for entering
> short position
> 8
> 9
> 10
> # Calculate
> Sentiment
> SCore
> 35
> feature
> 11
> sentiment_score
> SCl3_averagesentiment
> returns;
> 12
> 13
> # Create
> signal based
> on
> Sentiment score
> 14
> alpha_signal
> if_else(sentiment_score
> threshold,
> 1, if_else
> (sentiment_score
> short_threshold,
> -1,
> 0));
> 15
> 16
> # Apply
> the alpha signal
> to
> trading
> decisions
> 17
> final_alpha
> ts_backfill(group_rank (
> rank(alpha_signal,
> 60) , industry) ,20);
> 18
> 19
> final_alpha
> long_
> tS_


---

## 讨论与评论 (1)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

可否将本Alpha的绩效PnL图表发出？ [XM91020](/hc/en-us/profiles/17548799403927-XM91020)

---

