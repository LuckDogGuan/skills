# 【Alpha灵感】:Earnings, retained earnings, and book-to-market in the cross section of expected returns

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Earnings retained earnings and book-to-market in the cross section of expected returns_18640904315799.md
- **作者**: ES71704
- **发布时间/热度**: 2 years ago, 得票: 18

## 帖子正文

alpha：retained_earnings/cap

**论文题目：Earnings, retained earnings, and book-to-market in the cross section of expected returns，**

作者：Ray Bally, Joseph Gerakos, Juhani T. Linnainmaa and Valeri Nikolaev

alpha inspiration：会计指标是可以进一步分解成更具体的指标，因此该论文根据会计准则将账面市值比的分子股权账面价值分解成留存收益（retained earnings）和缴入资本（contributed earnings），要注明的是此处的缴入资本（Contributed earnings）等于过去累计发行股票的收入减去再回购股票流出的资金，进一步去探索账面市值比能够预测未来收益率的能力到底是他的哪一部分的成分提供的。

最终证明账面市值比之所以能够预测预期回报的横截面，是因为其中的留存收益市值比（retained earnings-to-market）的作用，但是留存收益是累计收入（accumulated earnings）与股息分红（dividends）之差，对于究竟是累计收入使得留存收益具有盈利收益率的预测能力还是累计股息分红这个问题，论文又在第七部分进行了详细论述，并证明了累计收益是驱动因素。

相关数据集：

retained_earnings(CHN)

cap(CHN)

表现：


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Good
> Stage
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.57
> 4.429
> 1.52
> 11.719
> 9.059
> 52.96900
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2016
> 0.73
> 4.5196
> 0.47
> 5.2596
> 5.2296
> 23.279600
> 696
> 919
> 2017
> 3.88
> 3.8696
> 5.86
> 28.5496
> 3.3996
> 147.939600
> 730
> 897
> 2018
> 1.32
> 4.5996
> 1.12
> 8.969
> 9.0596
> 39.06960
> 747
> 870
> 2019
> 0.97
> 4.5896
> 0.73
> 7.0596
> 8.1096
> 30.809600
> 765
> 802
> 2020
> 0.56
> 4.6996
> 0.34
> 4.6796
> 6.9496
> 19.949600
> 706
> 795
> 2021
> 3.17
> 3.8696
> 5.11
> 32.549
> 4.2496
> 168.72900
> 750
> 828
> Long


改进方向：

1、可以将留存收益继续拆分

2、留存收益对于上市时间久，总市值大的股票效果可能会优于小票

3、通过设置阈值筛选股票

4、可以尝试累计收益替代留存收益

---

## 讨论与评论 (1)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

如果可以分享一下表达式就更好了。或者留存收益（retained earnings）和缴入资本（contributed earnings）具体用到的数据字段

---

