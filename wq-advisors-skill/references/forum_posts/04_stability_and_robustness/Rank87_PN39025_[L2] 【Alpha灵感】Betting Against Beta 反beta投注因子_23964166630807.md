# 【Alpha灵感】Betting Against Beta （反beta投注因子）

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Betting Against Beta 反beta投注因子_23964166630807.md
- **作者**: 顾问 JY88060 (Rank 85)
- **发布时间/热度**: 2年前, 得票: 16

## 帖子正文

文章名称：Betting Against Beta

链接： [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2049939](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2049939)

**一. 论文总结**

**（一）文章**  **理论研究基础**  **：**

- 早期的实证研究发现，美国股票的证券市场线（SML）与标准CAPM相比更为平坦，这说明风险与收益的关系不能非常很好的满足CAPM。 
> [!NOTE] [图片 OCR 识别内容]
> 15.0%
> 13.0%
> 11.0%
> 9.0%
> 7.0%
> 5.0%
> 3.0%
> 1.0%
> 0%
> 2.0%
> 4.0%
> 6.0%
> 8.09
> 10.09
> 12.0%
> 14.0%
> 16.0%
> 18.0%
> 20.0%
> 1.0%


- 基于此Black et al.（1972）提出了改进版的双因子CAPM模型，即Black CAPM模型：  
> [!NOTE] [图片 OCR 识别内容]
> E[rj] = E[r](1 -Bj) + Elrm]8j

- 从以上模型可以发现，资产收益可分解为beta因子和负beta因子。

**（二）文章Idea**

1. Beta小于1的有效组合拥有最高的Sharpe比率，其中高Beta资产的Alpha更低。
2. 通过买入低Beta资产同时卖出高Beta资产构建的beta中性的BAB因子（反Beta投注因子）能够产生明显的经风险调整后正收益。
3. 当融资收紧，BAB组合当期预期收益会降低，随后未来收益会提高。
4. 当融资流动性风险提高的时候， 所有资产的Beta均会倾向于向1压缩。
5. 有杠杆限制的投资人会选择高beta的资产组合，而杠杆限制较少的投资人会选择带杠杆的低beta资产组合。

**（三）研究数据来源**

**数据池**

- 包括美国在内20个国家的股票数据
- 美国1-10年国债数据
- 美国信用债数据
- 基于各国权益指数，债券指数，外汇以及商品的期权，期货数据

**时间窗口及滞后区间**

- 文章选取了1年，3年及5年的滚动回归窗口，同时选取了1周作为滞后区间。

**（四）BAB因子的构建**

- 构建BAB因子，对beta进行排序，将资产等分入高beta组合和低beta组合；
- 各个资产权重为去均值后排序值的残差，并调整残差使得高beta组合和低beta组合的总权重均为1； 
> [!NOTE] [图片 OCR 识别内容]
> WH =k(Z-乏)
> W =K(Z-乏)
  
> [!NOTE] [图片 OCR 识别内容]
> K=2/1n12-U

- 根据以上计算的权重分别计算高beta组合和低beta组合的加权平均beta；
- 构建自融资组合，借入资金买入低beta组合，同时卖出高beta组合并将资金存入无风险资产，高beta资产与低beta资产组合的beta相等且均为1, BAB组合beta中性 
> [!NOTE] [图片 OCR 识别内容]
> BAB
> 1
> 1
> (r+1 -ri-
> (4+1-9
> Pl
> 陧
> TtI


**二. 复现过程**

**(一)数据探索**

**beta_last_360_days_spy**

- **数据覆盖：**  **平均在90%左右，基本非零，数据质量非常高 
> [!NOTE] [图片 OCR 识别内容]
> COVeraqe
> TOI_ZeTo
> 2012
> [45
> 6796
> 2013
> 8%
> 78%
> 2014
> 0
> 2015
> 83%
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
**
- **频率：**  **daily**
- **中位数：中位数为1左右**
- **数据范围：**  **基本在**  **[-**  **2**  **,**  **2**  **]**  **范围内 
> [!NOTE] [图片 OCR 识别内容]
> 2000
> 1800
> 1600
> 1400
> 1200
> I000
> 800
> GOO
> 400
> 200
> Oexel
> Iexc2
> 2exc3
**
- **数据分布：呈负偏形态；根据以上数据可以大致推断**  **16%**  **的数据在[-2, -1]间，34%的数据在[-1, 1]间，48%的数据在[1, 2]间。 
> [!NOTE] [图片 OCR 识别内容]
> 1400
> 1200
> I000
> 800
> GOO
> 400
> 200
> 02
> 0.5
**

**returns** : daily, coverage完全，范围约在[-1, 1]

**correlation_last_360_days_spy** : daily, coverage完全，范围约在[-1, 1]

**volume** : daily, coverage完全

**（二）因子组合构建**

**Alpha设定**

- **REGION** ：US
- **INSTRUMENT TYPE**  **：** Equity
- **UNIVERSE**  **：** US3000
- **Neutralization** : None
- **DECAY**  **：5**

**因子构建**

- **因为平台规则，无法在横截面层面计算加权平均的高beta组合和低beta组合的beta值，因此无法计算买入组合和卖出组合的价值比例，无法完全复现论文的因子构建；**
- **进一步理解论文因子构建的核心，BAB的核心在于：**

1. **beta**  **中性，即高beta组和低beta组的beta相等；**
2. **组合买卖不平衡，从价值上看，低beta组的风险资产绝对价值高于高beta组的风险资产绝对价值，根据论文的实证研究，风险资产买卖比例大约为**  **1.3**  **：0.85，即约3：2。根据之前对**  **beta**  **分布的分析，50%的资产beta是在[-2, 1]之间，另外部分是在[1,2]之间，粗略估计等分组合的beta比例大概率在2：1以上。**

- **替代思路主要为实现以上目标：**

1. **买卖组合beta相等**
2. **低beta价值约占总体的60%，高beta价值约占总体的40%**
3. **beta**  **越低或beta越高，在其所在组合的权重就越高**

- **因此，与论文不同，构建的是一个非等分的买卖组合，低beta**  **60%**  **，高beta40%（注意60%只是一个使得买卖价值比例为3：2的估计值，实际值可能不会是这个比例，可以调整至70%甚至于80%看以下稳健性；另外整个组合不是完全beta中性的，这只是为了更多低beta暴露的折中方法）**

beta_z = rank(beta_last_360_days_spy);

weight = 0.6 - beta_z

**（三）迭代过程**

**版本一：根据以上因子构建方法，建立一个初步版本，看是否有信号。**

beta_z = rank(beta_last_360_days_spy);

weight = 0.6 - beta_z;

scale(weight)

**结果：Sharpe在1.02, turnover6.12%，有明显信号**

**
> [!NOTE] [图片 OCR 识别内容]
> DOoK
> DOoK
> OOOK
> DOoK
> DOoK
> OOOK
> OOOK
> 2013
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN
> TC
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Rezurns
> Drawdown
> Wargin
> 1.02
> 6.129
> 0.87
> 9.11%
> 10.229
> 29.809000
**

**版本二：文章发现流动性限制对BAB有明显负影响，当流动性收紧，低beta资产收益下降较高beta资产更多，BAB因子的收益率降低。**

启示：BAB因子收益与资产流动性正相关，可以在低beta资产中增加高流动性资产的权重。进一步研究基于该论文的其他研究，发现论文A Market-Based Funding Liquidity Measure提出了流动性代表指标，包括特质风险，Amihud流动性指标，机构持有比率，分析师覆盖，以及市值。因为波动率也是流动性指标之一，加入短期波动率更容易捕捉流动性的变动。因此加入波动率，特质风险，Amihud流动性指标和市值指标，并选取改善最好的组合，看信号是否有改善。

volatility_st = ts_std_dev(returns < 0 ? returns: 0, 20);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

beta_z = rank(beta_last_360_days_spy);

weight = 0.6 - beta_z;

scale(weight) * scale_down(rank(-volatility_st)) * scale_down(rank(-illiquidity)) * scale_down(rank(-idiosyncratic))

结果： **Sharpe**  **提升至1.**  **46**  **, turnover**  **15.87**  **%**  **，**  **performance**  **改善明显**

**
> [!NOTE] [图片 OCR 识别内容]
> 16W
> 07118/2019
> 14N1
> Traln PI 14.2711
> 12W
> 1ONI
> OOOK
> DOoK
> OOOK
> DOoK
> 2013
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN
> TC
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJown
> Wargin
> 1.46
> 15.87%
> 1.66
> 20.54%
> 19.90%
> 25.89900
**

**版本三：考虑流动性的边际变动，如短期波动性高于长期波动性，说明资产流动性收紧，考虑减少该资产权重。选取一周波动率平均穿过一个月波动率平均，当流动性收紧，资产权重降低为原有权重的0.1（其实应该取0,但是取0会导致组合权重集中，因此取0.1）**

volatility_st = ts_std_dev(returns < 0 ? returns: 0, 20);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

cond = ts_mean(volatility_st, 5) > ts_mean(volatility_st, 20) ? 0.1 : 1;

beta_z = rank(beta_last_360_days_spy);

weight = (0.6 - beta_z) * cond;

scale(weight) * scale_down(rank(-volatility_st)) * scale_down(rank(-illiquidity)) * scale_down(rank(-idiosyncratic))

**结果**  **：Sharpe提升至1.**  **51**  **, turnover**  **22.15**  **%**  **，**  **performance**  **有意义提高**

**
> [!NOTE] [图片 OCR 识别内容]
> 1SW
> 02/05/2019
> Train Pn; 13.07N
> 12.5N
> 1ON
> DOoK
> 250OK
> 2013
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJown
> Wargin
> 1.51
> 22.15%
> 1.47
> 21.01%
> 19.37%
> 8.989600
> SOOK
**

**版本四：根据本论文研究，当市场资金流动性风险的增加将 所有资产的beta向1压缩。**

**启示：在流动性风险增加时，低beta资产和高beta资产的beta均会向1靠拢，beta分散性降低，BAB因子会失效；因此考虑提高与市场相关性低的资产的权重，提高BAB因子的显著性**  **。增加资产与市场收益相关性指标，该指标越高，资产权重越低。**

volatility_st = ts_std_dev(returns < 0 ? returns: 0, 20);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

cond = ts_mean(volatility_st, 5) > ts_mean(volatility_st, 20) ? 0.1 : 1;

beta_z = rank(beta_last_360_days_spy);

weight = (0.6 - beta_z) * cond;

scale(weight) * scale_down(rank(-volatility_st)) * scale_down(rank(-illiquidity)) * scale_down(rank(-correlation_last_30_days_spy)) * scale_down(rank(-idiosyncratic))

**结果**  **：Sharpe提升至1.**  **51**  **, turnover**  **22.15**  **%**  **，**  **performance**  **有意义提高 
> [!NOTE] [图片 OCR 识别内容]
> 1112412020
> Train Pn; 21.50N
> ZOW
> 17.5N
> 15NI
> 12.5N
> 1OW
> SOOK
> OOOK
> 250OK
> 2013
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJown
> Wargin
> 67
> 24.75%
> 1.70
> 25.73%
> 21.25%
> 20.79900
**

**版本五：一些尝试。论文进一步提出了一些实证发现，如低beta组合市帐率和动量更高。**

**启示：BAB因子和市帐率和动量相关性高，有可能市帐率和动量正向影响BAB因子收益率，也可能负向影响，也可能无影响，可以买入或卖出这两个因子查看是否有影响。**

volatility_st = ts_std_dev(returns < 0 ? returns: 0, 20);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

hml = ts_decay_exp_window(bookvalue_ps/close, 252);

mom = ts_decay_exp_window(returns, 252);

cond = ts_mean(volatility_st, 5) > ts_mean(volatility_st, 20) ? 0.1 : 1;

beta_z = rank(beta_last_360_days_spy);

weight = (0.6 - beta_z) * cond;

scale(weight) * scale_down(rank(-volatility_st)) * scale_down(rank(-illiquidity)) * scale_down(rank(-correlation_last_30_days_spy)) * scale_down(rank(-idiosyncratic)) * scale_down(rank(-hml)) * scale_down(rank(-mom))

**结果**  **：组合中卖出这两个因子**  **，**  **Sharpe**  **提升至1.**  **7**  **1**  **, turnover**  **2**  **9.05**  **%**  **，**  **performance**  **提高明显 
> [!NOTE] [图片 OCR 识别内容]
> 22.SN
> ZOW
> 17.5N
> 1SWI
> 12.5N
> 1OW
> SOOK
> OOOK
> 250OK
> 2013
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN
> TC
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Returns
> DrawJown
> Wargin
> 1.71
> 29.05%
> 1.66
> 27.43%
> 22.08%
> 18.8890
**

**版本六：再搜索引用了该论文的最新研究论文，发现论文Low Risk Anomalies?提到skewness尤其是跨期的coskewness能解释大部分BAB异像，尝试加入skewness。**

volatility_st = ts_std_dev(returns < 0 ? returns: 0, 20);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

hml = ts_decay_exp_window(bookvalue_ps/close, 252);

mom = ts_decay_exp_window(returns, 252);

cond = ts_mean(volatility_st, 5) > ts_mean(volatility_st, 20) ? 0.1 : 1;

beta_z = rank(beta_last_360_days_spy);

weight = (0.6 - beta_z) * cond;

scale(weight) * scale_down(rank(-volatility_st)) * scale_down(rank(-illiquidity)) * scale_down(rank(-correlation_last_30_days_spy)) * scale_down(rank(-idiosyncratic)) * scale_down(rank(-hml)) * scale_down(rank(-mom))

**结果**  **：Sharpe提升至1.**  **86**  **, turnover**  **2**  **9**  **.**  **48**  **%**  **，**  **performance**  **有意义提高 
> [!NOTE] [图片 OCR 识别内容]
> Z2.SN
> ZOW
> 17.5N
> 1SW
> 12.5N
> 1ONI
> 7SOOK
> DOoK
> SOOK
> 2013
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJown
> Wargin
> 86
> 29.48%
> 1.85
> 29.15%
> 20.1096
> 19.789600
**

**版本七：通过研究基于该论文的后续研究论文，寻找提升因子表现的思路，通过研究发现论文The Unintended Impact of Academic Research on Asset Returns: The CAPM Alpha，提出了基于BAB因子的Betting Against Alpha and Beta (BAAB因子)，同时买入低beta和低alpha资产，会进一步提升因子的显著性。**

**结果**  **：Sharpe反而下降明显**  **，剔除该因子，回到版本六。**

**（四）稳健性测试**

**1. 数据集**

- **beta**  **：**  **beta_last_**  **30**  **_days_spy, beta_last_60_days_spy, beta_last_**  **90**  **_days_spy**

结果：表现均有所下降，但下降并非明显，很可能是beta构建时间缩短，信号出现更频繁，使因子波动率提高，Sharpe下降。再次以ts_mean平滑beta数据后，因子表现又有所提升。

- Liquidity: 上文有提到流动性指标包括分析师覆盖和机构持有率，可理解为投资者指标，目前只找到snt_buzz (待更多探索)

结果：加入后Sharpe进一步明显提高，说明流动性指标对因子表现影响明显，可以进一步探索

- 买卖组合风险资产比率：60% - 70%探索

结果：在该范围内结果变动不大，但是如果在50%及以下，因子表现非常差，说明该因子需要明显的低beta资产暴露才会perform。

**2.operator**

加权方式：ts_decay_exp_window, ts_mean

结果：对结果影响不大

**(五)样本外测试结果 
> [!NOTE] [图片 OCR 识别内容]
> ZSW
> 22.SN
> ZOW
> 17.5N
> 1SW
> 12.5N
> 1ONI
> S0OK
> DOoK
> 250OK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJown
> Wargin
> 1.82
> 34.22%
> 1.65
> 27.97%
> 20.549
> 16.35900
**

**
> [!NOTE] [图片 OCR 识别内容]
> 回 |5
> Testing Status
> 5P4Ss
> Sharpe of
> 8215above CUoffof
> Fitness Of 1.65 Is above cutoff of
> Turnoverof 34.229 I5s above cutoffof 19。
> Turnoverof 34.22%
> below CUtOff of 70%。
> elght Is Well distributed over instruments
> IS ladder Sharpe Of 2.41 is above CUtoff of 2.37 for ladderyear 2: 1/24/2022..1/25/2020
> FAIL
> Sub-universe Sharpe Of 0.15 Is below CUtOff Of 0.79
> WARNING
> PENDING
**

**三. 反思及问题**

1. 在根据论文的思路进行构建及改进的过程中，每一步都改善都是非常明显的，但到最后才发现通过不了sub-universe测试，因为sub-universe有一个非常必要的neutralization是market neutralization，这个operator相当于不仅是把beta neuralized了，而且把低beta资产和高beta资产的风险值暴露一起neutralized了；但是这个因子的核心就在于低beta资产的绝对值暴露要高于高beta资产，基于beta，这个因子组合很可能在市值，行业等等都有集中的暴露，不进行neutralization是很重要的。因此，再进一步基于这个思路改善可能性不太大，需要更创新的找到提高低beta资产alpha暴露同时保持beta中性的构建方式。这也给我一个提示，在构建因子时第一步一定先做neutralization，不能设置为0
2. 在阅读论文中，基于原论文找到分解BAB因子风险的论文，可能能进一步找到不基于beta，而且可以进行风险价值暴露中性的因子。这是一篇非常经典的论文，结果明显且稳健，后续基于该论文进行的研究也非常丰富，可以基于此进一步深挖后续研究。

---

## 讨论与评论 (2)

### 评论 #1 (作者: TN48752, 时间: 2年前)

你好。感谢你的分享。我注意到，universe_sharpe sub 失败了，这表明 alpha 在高流动性市场中表现不佳。我认为你可以尝试消除一些因素，看看哪些因素给出了 alpha 的主要信号。

---

### 评论 #2 (作者: YQ76635, 时间: 1年前)

原文的链接，我打不开。

链接： [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2049939](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2049939)

我基本上把论坛上alpha灵感的帖子都看了一遍，现在想看下研报的原文或论文的原文。但好多的链接都打不开

---

