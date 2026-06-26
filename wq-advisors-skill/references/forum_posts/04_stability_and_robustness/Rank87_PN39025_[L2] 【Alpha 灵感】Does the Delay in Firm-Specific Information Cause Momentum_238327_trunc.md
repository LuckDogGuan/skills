# 【Alpha 灵感】Does the Delay in Firm-Specific Information Cause Momentum?

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha 灵感】Does the Delay in Firm-Specific Information Cause Momentum_23832785873943.md
- **作者**: DL92496
- **发布时间/热度**: 2 years ago, 得票: 8

## 帖子正文

论文内容：文章通过探讨公司特定信息延时(FSID)与市场动态之间的关系，重点研究了FSID如何影响股票波动率、动量和套利机会。研究发现，股票的信息不确定性放大了动量效应，因此信息不确定性较高的股票表现出更强的动量效应。由于公司特定信息对股价的影响有一定的滞后性，因此FSID较高的公司会有更高的回报率波动和更低的市场效率。

实现策略：

1. 股票的信息不确定性和动量效应

实现方案：

1.使用收益率波动性来识别和衡量信息不确定性。
                  2.做多动量大且信息不确定性高的股票，做空动量小且信息不确定性低的股票。

Datafiel 选择：

收益率计算：return

动量计算：close

Operator选择：

ts_std_dev()

rank()

delay()

info_uncertainty = ts_std_dev(returns, 150);

momentum = close - delay(close, 12);

rank_info_uncertainty = rank(info_uncertainty);

rank_momentum = rank(momentum);

alpha_signal = rank_info_uncertainty * rank_momentum;

rank(alpha_signal) > 0.5 ? -(1-rank(alpha_signal)) : rank(alpha_signal);

1. FSID和套利限制

实现方案：

1.根据公司的信息不确定性排序。

2.做多信息不确定低的股票，做空信息不确定性高的股票。

Datafiel 选择：

收益率计算作为信息不确定性：return

Operator选择：

ts_std_dev()

rank()

info_uncertainty = ts_std_dev(returns, 150);

rank_info_uncertainty = rank(info_uncertainty);

alpha_signal = rank_info_uncertainty ;

rank(alpha_signal) > 0.5 ? -(1-rank(alpha_signal)) : rank(alpha_signal);

Alpha 测试结果：

1. 股票的信息不确定性和动量效应


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 35OOK
> 30OOK
> 2SOOK
> 恻
> 2OOOK
> TSOOK
> OOOK
> SOO
> 2013
> 201
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> M


1. FSID和套利限制


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> Sattings
> N Chart
> Pnl
> OOOK
> 5OO
> SOO
> 1OOOr
> 1,50Or
> 2000k
> 2013
> 201
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Uw
> 么


**反思与改进**  **:**  
Sharpe比率偏低，FSID结合动量效果更好，后续可以探索不同的动量范围和datafield。

---

## 讨论与评论 (2)

### 评论 #1 (作者: KJ42842, 时间: 2 years ago)

"momentum = close - delay(close, 12)"

不同股票的涨跌数值的量纲不一致，使用涨跌幅的比较会更合理。

---

### 评论 #2 (作者: YH72588, 时间: 2 years ago)

对"momentum = close - delay(close, 12)"，可以消除量纲

比如，除以delay(close)，即KJ42842所说的涨跌幅。或除以ts_std_dev(close)

---

