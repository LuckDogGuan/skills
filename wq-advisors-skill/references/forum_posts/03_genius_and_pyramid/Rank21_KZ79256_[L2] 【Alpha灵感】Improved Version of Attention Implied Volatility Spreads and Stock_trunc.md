# 【Alpha灵感】Improved Version of "Attention: Implied Volatility Spreads and Stock Return"

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Improved Version of Attention Implied Volatility Spreads and Stock Return_21120326355479.md
- **作者**: DK85731
- **发布时间/热度**: 2 years ago, 得票: 3

## 帖子正文

- 论文概述：使用SEC的EDGAR日志文件中新颖直接的投资者关注度衡量方法，研究者重新检验了通过投资者关注度视角的看涨-看跌隐含波动率差对股票回报的可预测性。研究发现，随着投资者关注度的提高，波动率差的回报预测性变得更加明显，这为信息交易假说提供了有力的证据，而不是错误定价假说。更重要的是，研究记录了基于波动率差和高关注度的投资组合的构建和盈利能力。一个在最受投资者关注和波动率差最大的股票上做多，在最受关注和波动率差最小的股票上做空的投资组合，能够产生2.43%的月度Fama-French 5因子alpha值。
- 论文链接： [https://doi.org/10.1080/15427560.2019.1692846](https://doi.org/10.1080/15427560.2019.1692846)
- 核心idea：投资者关注度较高的股票，若同时出现较大的期权implied volatility的spread，则有可能为informed trader在进行提前买入期权以获得最大化收益，可以预计股票在未来一段时间内走高
- 期权波动率数据选取：  opt4_call_vola_30d ，opt4_put_vola_30d 等不同期限的期权波动率数据
- 交易者关注度数据选取：brain平台具有类似SEC的EDGAR日志文件的data field Search Engine Data，但由于其coverage的时间极为短暂，仅在2021年后有大量数据，故需要采取替代数据以量度交易者关注度，本次论文选取 交易热度因子： volume/cap，与交易者情绪因子：mws85_sentiment 来取代交易者热度因子
- 该论文并未回测策略，故在其中并未找到Universe: TOP 200 or Neutralization
- 核心Alpha的 Expression1: (设置交易热度的threshold)

```
ratio_1 = rank_by_side( opt4_put_vega_60d - opt4_call_vega_60d);ratio_2 = rank(volume/cap);ratio_1 * ((rank(ratio_2 )>0.9))
```

- 核心Alpha的 Expression 2:(设置期权spread的threshold)

```
ratio_1 = rank_by_side( opt4_put_vega_60d - opt4_call_vega_60d);ratio_2 = rank(volume/cap);ratio_1 * ((rank(ratio_1)>0.9) || (rank(ratio_1)<0.1)) * ratio_2 
```

- 回测表现：
- Expression1 在如下setting的情况下，取得的最好表现为：


> [!NOTE] [图片 OCR 识别内容]
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILLIQUID_MINVOLIM
> NEUTRAUIZATION
> DECAY
> TRUNCATION
> Market
> 0.04
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> SaVe a5 Default
> Apply



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.77
> 53.739
> 1.26
> 27.149
> 39.33%
> 10.109oo
> Year
> Sharpe
> TuIOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 4.12
> 47.82%
> 4.47
> 56.289
> 7.01%
> 23.539600
> 1724
> 228
> 2013
> 1.34
> 45.73%
> 0.77
> 15.03%
> 5.78%
> 6.579600
> 1857
> 2012
> 3.52
> 57.11%
> 3.18
> 46.509
> 7.25%
> 16.299300
> 1724
> 448
> 2015
> 3.55
> 61.24%
> 3.18
> 48.99%
> 7.18%
> 16.00960o
> 694
> 2016
> 0.50
> 62.9495
> 0.25
> 10.55%
> 19.1395
> 3.359300
> 1372
> 759
> 2017
> 0.19
> 56.23%
> 0.04
> 2.249
> 11.849
> 0.809300
> 719
> 1356
> 2018
> 1.04
> 52.9395
> 0.52
> 13.119
> 9.25%
> 4.959300
> 1572
> 2019
> 1.57
> 49.27%
> 1.04
> 21.77%
> 13.73%
> 8.849600
> 905
> 1232
> 2020
> 0.52
> 51.34%
> 0.26
> 12.78%
> 24.09%5
> 4.989600
> 1544
> 550
> 2021
> 2.19
> 51.90%
> .86
> 37.29%
> 20.60%
> 14.379600
> 2151
> 329
> 2022
> 7.59
> 57.9695
> 12.44
> 151.749
> 249
> 52.369600
> 2510
> 158



> [!NOTE] [图片 OCR 识别内容]
> PASS
> 2 FALL
> Most illiquid 50% instruments after cost Sharpe of 0.75 is below cutoff of 0.79 (1.51 original universe after cost
> Sharpel
> IS ladder Sharpe of 1.56 is below cutoff of 1.58 for ladder year 2: 1/24/2022...1/25/2020。
> WARNING
> 3 PENDING


- Expression2 在如下setting的情况下，取得的最好表现为：


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILLIQUID_MINVOLIM
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 0.04
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> Apply
> 5aVe 35 Default



> [!NOTE] [图片 OCR 识别内容]
> Start Date
> Snarpe
> Turhover
> Fitness
> Returns
> Drawdown
> Margin
> 01/23/2022 Cr
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> 05/15 Ratio
> Pre Close Sharpe
> PreClose Ratio
> Self-Correlation
> Year
> Sharpe
> TUIOVeT
> Fitness
> Returns
> DrawdOwn
> Margmn
> Long Count
> Short Count
> 2012
> 4.67
> 50.90%
> 3.85
> 34.5795
> 4.20%
> 13.589600
> 1595
> 359
> 2013
> 2.09
> 55.25%
> 0.98
> 12.159
> 2.2796
> 4.40960o
> 634
> 378
> 2014
> 5.51
> 61.00%
> 429
> 36.9595
> 4.38%
> 12.1
> 90o
> 1579
> 593
> 2015
> 4.44
> 62.7695
> 3.16
> 31.6990
> 4.24%
> 10.
> 090o
> 622
> 543
> 2016
> 1.55
> 64.,09%
> 0.76
> 15.4795
> 8.72%
> 4.839600
> 531
> 501
> 2017
> 0.71
> 57.85%
> 0.20
> 4.68%
> 3.73%
> .629600
> 1579
> 497
> 2018
> 2.89
> 49.21%
> 23.10%
> 5.22%
> 9.399600
> 1762
> 435
> 2019
> 47.1495
> 0.34
> 7.6795
> 73%
> 3.259600
> 1730
> 407
> 2020
> 56.46%
> 0.77
> 17.1795
> 849
> 0830o
> 1477
> 518
> 2021
> 2.36
> 54.23%
> 1.52
> 22.48%
> 8.28%
> 8.299600
> 1858
> 522
> 2022
> 6.50
> 53.80%
> 7.85
> 78.53%
> 0.96%
> 29.19900
> 2185
> 483


（该因子已提交）

- 思考：该因子主要从detect informed trader的角度进行思考，并对option implied volatility 所提供的信号进行进一步的优化，进而得到了有效因子。本文作者由该模板，从不同角度思考后提取出满足提交条件的两个有效因子。而detect informed trader 在中国市场应有着更加重要的作用，但需对隐含波动率与交易者热度两个基础因子进行一定程度的替代，正如本文前半部分所做的那样，该潜在扩展有待读者深思。
- 代码总结反思： 进行2450次参数调优与数据替换的simulation，共用时两个小时，暂时未发现性能局限，故短时间内将保持原模板。平台将自动统计因子表现，故在因子同质的基础上，建议直接使用sharpe/turnover排序选取最有效的因子，而非耗费时间在提取因子回报上

---

## 讨论与评论 (1)

### 评论 #1 (作者: BC25356, 时间: 2 years ago)

我看到您这里long count 和 short count差异很大，这个策略用API跑的时候，成功率高吗？

---

