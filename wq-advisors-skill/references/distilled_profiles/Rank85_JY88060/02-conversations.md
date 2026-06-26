# 顾问 JY88060 (Rank 85) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 JY88060 (Rank 85) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: ATOM AMA 2024 - Ask me Anything被推荐的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] ATOM AMA 2024 - Ask me Anything被推荐的_26942011289751.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Hi everyone,

We are hosting an AMA (Ask Me Anything) session on the BRAIN forum for the ATOM competition. This is an opportunity for you to ask any questions you may have about the competition, and for our expert team to anything on your mind.

We understand that the competition can be challenging, and we want to ensure that you have the information and support you need to succeed.

Ask away!

**顾问 JY88060 (Rank 85) 的解答与建议**:
How comes that sometimes when I submit one more alpha, the total IS score decreased?


---

### 技术对话片段 2 (原帖: group_neutralize(alpha, bucket(rank(cap),range='0.2,1,0.2')))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 带你读论文系列活动第一期课后挑战1_23759895660183.md
- **时间**: 2年前

**提问/主帖背景 (WL13229)**:
作业要求：完成下列Alpha Checklist

- 文章链接与名称：
- 文章idea：
- 文章原文与Alpha相关的核心表达式（必须可复现或替代性复现）：
- 文章基础数据字段（datafield)：
- Operator：
- Universe：
- Decay:
- Neutralization：
- 初步的表达式：
- Performance Check: Sharpe至少大于1，Fitness至少大于0.5, Turnover是否低于45%，高于5%, 相关性检查是否通过?

**本次选择的论文必须完成上述check list,简要地说，需能将文章中心idea使用Alpha表达式进行表达。**

**顾问 JY88060 (Rank 85) 的解答与建议**:
**文章链接与名称** ：

《Betting Against Beta》 [[链接已屏蔽])

**文章idea：**

文章研究发现在控制市场beta及一些常见如市值，BM因子后，残差与市场beta负相关。通过买入低Beta资产同时卖出高Beta资产构建的beta中性的BAB因子（反Beta投注因子）能够产生明显的经风险调整后正收益。

**文章原文与Alpha相关的核心表达式：**

- **数据池** ：文章选取了20个国家的股票市场以及包括股票，债权，商品等数据进行稳健性测试。由于论文研究结果显示BAB因子收益在各个市场和资产类别均是显著的，因此复现时暂先选择流动性较高，资产beta更为分散的数据池—— **REGION** ：US； **INSTRUMENT TYPE：** Equity **;  UNIVERSE：** US3000。

- **时间窗口及滞后区间** ：文章选取了1年，3年及5年的滚动回归窗口，同时选取了1周作为滞后区间。为防止时间序列的结构性变化，复现时暂先选取 **1年作为回归窗口** （在后续作回归分析时体现），滞后区间与论文相同，即1周—— **DECAY** ：5
- **控制变量** （neutralization）：论文将Fama-French四因子作为控制变量，研究BAB组合的alpha。四因子分别为Market Return, SMB, HML, UMD，对应的因子载荷分别为市场beta，市值，市账比和动量。由于平台无法对构建的因子收益作回归，而只能对因子载荷进行回归，如果直接对市场beta值进行回归，BAB组合会在回归后抵消掉反beta的效应，而体现不出来BAB的alpha。因此我们采用了替代方法，先分别对 **市值(cap)，市账比(close/bookvalue_ps)及动量因子(fscore_momentum)** 进行回归，取残差；进一步根据市场beta将组合分为 **10组** ，对残差进行beta group neutralization; 最后卖出高beta组，买入低beta组。

**文章基础数据字段（datafield)：**

- returns;
- cap;
- close;
- bookvalue_ps;
- fscore_momentum;
- beta_last_360_days_spy

**Operator：**

- rank
- ts_regression
- group_neutralize

**Universe：**

- **REGION** ：US；
- **INSTRUMENT TYPE：** Equity **;**
- **UNIVERSE：** US3000

**Neutralization：**

论文将Fama-French四因子作为控制变量，并未对行业变量进行控制，因此Neutralization包括：

- cap;
- close/bookvalue_ps；
- fscore_momentum;
- beta_last_360_days_spy

**初步的表达式：**

resid_cap = ts_regression(returns, rank(cap), 360);

resid_bm = ts_regression(resid_cap, rank(close/bookvalue_ps), 360);

resid_mom = ts_regression(resid_cap, rank(fscore_momentum), 360);

rank(-group_neutralize(resid_mom, bucket(beta_last_360_days_spy, range='0.1, 1, 0.1')))

**Performance Check:**

- Sharpe:1.13，大于1
- Fitness:2.05，大于0.5
- Turnover: 6.32%，小于45%，高于5%


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> GoOd
> Period
> TRAIN
> TEST
> Agregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawdOwn
> Wargin
> 1.13
> 6.32%
> 2.05
> 40.95%
> 49.97%
> 129.539600
> Year
> Sharpe
> Tumover
> Returns
> Orawdown
> Margin
> Long Count
> Short Count
> 2017
> 5.189
> 1
> 32.5795
> 9.919
> 126.08C
> 974
> 2018
> ~0.51
> 9895
> 0.58
> -16.2495
> 49.97%
> 81.714
> 949
> 2019
> 1.81
> 3095
> 51.9596
> 17.74%
> 273.33
> 957
> 2020
> 1.6-
> 12.6495
> 4.45
> 930495
> 43.07%0
> 147.27
> 2021
> 511
> 8.5095
> 18.53
> 167.0895
> 529
> 393.03f
> 925
> 2021
> 1.49
> 19.559
> 222
> 43.519
> 16.38%
> 44.37
> 853
> 2022
> 6.53
> 320395
> 16.43
> -202359
> 14.449
> -126.651
> Fltness
  
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 17.5W
> 15W
> 12.5W
> TON
> 750OK
> 09/20/2019
> OOOK
> Trainpnl: 5,354.45k
> Z50OK
> Jul'17
> Jan '18
> Jul'18
> Jan'19
> Jul '19
> J30'20
> Jul20
> Jul21
> Jan 21
> Jan22



---

### 技术对话片段 3 (原帖: Improving diversification by adding normalizationFama_MacBeth_normalized = ts_zscore(Fama_MacBeth, 252);PCP_normalized = ts_zscore(PCP, 252);Adding a cap to the weights to prevent concentrationcapped_Fama_MacBeth = truncate(Fama_MacBeth_normalized, maxPercent=0.02);capped_PCP = truncate(PCP_normalized, maxPercent=0.02);Additional diversification stepscaled_Fama_MacBeth = scale_down(capped_Fama_MacBeth);scaled_PCP = scale_down(capped_PCP);Generating the final signalSignal = rank(scaled_Fama_MacBeth) + rank(scaled_PCP);Signal)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 带你读论文系列活动第一期课后挑战2_23807105368215.md
- **时间**: 2年前

**提问/主帖背景 (WL13229)**:
# 作业要求：完成下列Alpha Checklist

- 文章链接与名称：
- 文章idea：
- Alpha Setting:
- 所选数据的统计特征：
- Idea的Alpha Implementation-版本1：
- Idea的Alpha Implementation-版本2：
- Idea的Alpha Implementation-版本3：
- Idea的Alpha Implementation-版本4：
- Idea的Alpha Implementation-版本XXXXX：

- 分析：阐述各个版本的绩效及迭代思路
- 稳健性测试及分析（仅在确定Alpha形式后开展）：

- Performance Check: Sharpe至少大于1，Fitness至少大于0.5, Turnover是否低于45%，高于5%, 相关性检查是否通过?
- Alpha的拓展空间思考：

**本次选择的论文必须完成上述check list,简要地说，最后的Alpha表达式需有明显信号。鼓励大家将自己优秀的探索总结成《Alpha灵感》系列文章参加比赛，我们将进行评选并提供奖励。**

**顾问 JY88060 (Rank 85) 的解答与建议**:
**文章链接与名称：**

- 文章名称：Betting Against Beta

链接： [[链接已屏蔽])

**文章idea：**

- 早期的实证研究发现，美国股票的证券市场线（SML）与标准CAPM相比更为平坦，这说明风险与收益的关系不能非常很好的满足CAPM。基于此Black et al.（1972）提出了改进版的双因子CAPM模型，即Black CAPM模型： E[rj​]=E[rz​](1−βj​)+E[rm​]βj。从以上模型可以发现，资产收益可分解为beta因子和负beta因子。
- 文章核心发现为通过买入低Beta资产同时卖出高Beta资产构建的beta中性的BAB因子（反Beta投注因子）能够产生明显的经风险调整后正收益。除此以外，以下为有助于提升BAB表现的研究结果：

1. 文章发现流动性限制对BAB有明显负影响，当流动性收紧，低beta资产收益下降较高beta资产更多，BAB因子的收益率降低。启示：BAB因子收益与资产流动性正相关，可以在低beta资产中增加高流动性资产的权重。进一步研究基于该论文的其他研究，发现论文A Market-Based Funding Liquidity Measure提出了流动性代表指标，包括特质风险，Amihud流动性指标，机构持有比率，分析师覆盖。（迭代版本1）
2. 市场资金流动性风险的增加将 所有资产的beta向1压缩。启示：在流动性风险增加时，低beta资产和高beta资产的beta均会向1靠拢，beta分散性降低，BAB因子会失效；因此考虑提高与市场相关性低的资产的权重，提高BAB因子的显著性。（迭代版本2）
3. 通过研究基于该论文的后续研究论文，寻找提升因子表现的思路，通过研究发现论文The Unintended Impact of Academic Research on Asset Returns: The CAPM Alpha，提出了基于BAB因子的Betting Against Alpha and Beta (BAAB因子)，同时买入低beta和低alpha资产，会进一步提升因子的显著性。（迭代版本3）
4. 论文进一步提出了一些实证发现，如低beta组合市帐率和动量更高。启示：可以考虑在BAB因子中剔除市帐率和动量的影响。（迭代版本4）

- 构建BAB因子，对beta进行排序，将资产等分入高beta组合和低beta组合；各个资产权重为去均值后排序值的残差，并调整残差使得高beta组合和低beta组合的总权重均为1；构建自融资组合，借入资金买入低beta组合，同时卖出高beta组合并将资金存入无风险资产，高beta资产与低beta资产组合的beta相等且均为1, BAB组合beta中性。

**Alpha Setting:**

- **数据池** ：文章选取了20个国家的股票市场以及包括股票，债权，商品等数据进行稳健性测试。由于论文研究结果显示BAB因子收益在各个市场和资产类别均是显著的，因此复现时暂先选择流动性较高，资产beta更为分散的数据池
- **时间窗口及滞后区间** ：文章选取了1年，3年及5年的滚动回归窗口，同时选取了1周作为滞后区间。为防止时间序列的结构性变化，复现时暂先选取 **1**  **年作为回归窗口** （在后续作回归分析时体现），滞后区间与论文相同，即1周
- **控制变量** （neutralization）：论文没有明确的neutralization设置。

- **REGION** ：US
- **INSTRUMENT TYPE**  **：** Equity
- **UNIVERSE**  **：** US3000
- **Neutralization** : None
- **DECAY** ：5

**所选数据的统计特征：**

- **beta_last_360_days_spy** : daily, 平均coverage在2600左右，中位数1.08左右，范围约在[-3, 3]
- **returns** : daily, coverage完全，范围约在[-1, 1]
- **correlation_last_360_days_spy** : daily, coverage完全，范围约在[-1, 1]
- **volume** : daily, coverage完全

**Idea的Alpha Implementation-版本1：**

按论文思路构建BAB因子，按beta排名把资产分为低beta和高beta组，两组权重分别为中位数减去排序值，买入低beta组，卖出高beta组

beta_z = rank(beta_last_360_days_spy);

weight = ts_mean(1250 - beta_z, 252);

scale(weight, longscale=1.5, shortscale=0.8)


> [!NOTE] [图片 OCR 识别内容]
> ZSW
> ZOW
> 09/14/2018
> Train Pn; 17.95N
> M
> SW
> 1ON
> OOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> IS Summary
> Period
> TRAIN_
> TC
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Wargin
> 0.98
> 0.29%
> 1.63
> 34.37%
> 58.849
> 2,358.97000


结果显示sharpe为0.98,与论文研究结果相近，论文研究结果BAB因子sharpe在0.78左右。

**Idea的Alpha Implementation-版本2：**

加入流动性因素: volatility, illiquidity, idiosyncratic. 三个指标越高， 流动性越低

volatility = ts_std_dev(returns < 0 ? returns: 0, 252);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

beta_z = rank(beta_last_360_days_spy);

weight = ts_mean(1250 - beta_z, 252);

scale(weight) * scale_down(rank(-volatility)) * scale_down(rank(-illiquidity)) * scale_down(rank(-idiosyncratic))


> [!NOTE] [图片 OCR 识别内容]
> 27.SM
> ZSW
> 22.SN
> 05/12/2020
> TraIn PI. 20.9411
> ZOW
> 17.5N
> 15W
> 12.5N
> 1ON
> SOOK
> ODOK
> ZSDOK
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
> ABgregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Nargin
> 1.17
> 8.80%
> 1.91
> 33.16%
> 41.73%
> 75.329000


可以看出，加入流动性因素后，因子表现有了明显提升，sharpe从0.98提升到1.17

**Idea的Alpha Implementation-版本3：**

增加beta的分散性，提高BAB因子显著性，加入资产与市场的相关性，相关性越低，权重越高

volatility = ts_std_dev(returns < 0 ? returns: 0, 252);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

beta_z = rank(beta_last_360_days_spy);

weight = ts_mean(1250 - beta_z, 252);

scale(weight) * scale_down(rank(-volatility)) * scale_down(rank(-illiquidity)) * scale_down(rank(-idiosyncratic)) * scale_down(rank(-correlation_last_30_days_spy))


> [!NOTE] [图片 OCR 识别内容]
> 27.5N
> ZSW
> ZON
> 17.5N
> 09/20/2017
> 1SN
> Train PI: 15.8911
> 12.5N
> 1OW
> SOOK
> ODOK
> ZSDOK
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
> TRAIN_
> TC
> ABBr
> Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJown
> Wargin
> .24
> 17.70%
> 1.71
> 33.499
> 38.88%
> 37.849000
> Z2.SN
> eBate


可以看出，增加beta分散性后，因子表现有进一步提升，sharpe从1.17提升到1.24

**Idea的Alpha Implementation-版本4：**

将BAB因子进一步提升为BAAB因子，同时买入低beta和低alpha资产

volatility = ts_std_dev(returns < 0 ? returns: 0, 252);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

alpha = ts_decay_exp_window(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=1), 252);

beta_z = rank(beta_last_360_days_spy);

weight = ts_mean(1250 - beta_z, 252);

scale(weight) * scale_down(rank(-volatility)) * scale_down(rank(-illiquidity)) * scale_down(rank(-idiosyncratic)) * scale_down(rank(-correlation_last_30_days_spy)) * scale_down(rank(-alpha))


> [!NOTE] [图片 OCR 识别内容]
> 2SN
> 1212712019
> ZOW
> Train Pn; 20.59N
> 1SN
> 1ONI
> ODOK
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
> ABgregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Wargin
> 1.28
> 17.95%
> 1.79
> 34.959
> 41.00%
> 38.95900


同时买入高beta和高alpha之后，因子表现有了不明显提升

**Idea的Alpha Implementation-版本5：**

卖出高市帐率和高动量资产

volatility = ts_std_dev(returns < 0 ? returns: 0, 252);

illiquidity = ts_decay_exp_window(abs(returns)/volume, 252);

idiosyncratic = ts_decay_exp_window(power(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=4)/252, 0.5), 252);

alpha = ts_decay_exp_window(ts_regression(scale_down(returns), scale_down(beta_last_360_days_spy), 252, lag=0, rettype=1), 252);

hml = ts_decay_exp_window(bookvalue_ps/close, 252);

mom = ts_decay_exp_window(returns, 252);

beta_z = rank(beta_last_360_days_spy);

weight = ts_mean(1250 - beta_z, 252);

scale(weight) * scale_down(rank(-volatility)) * scale_down(rank(-illiquidity)) * scale_down(rank(-idiosyncratic)) * scale_down(rank(-correlation_last_30_days_spy)) * scale_down(rank(-alpha)) * scale_down(rank(-hml)) * scale_down(rank(-mom))


> [!NOTE] [图片 OCR 识别内容]
> 3OW
> ZSW
> 07130/2018
> ZOW
> TraIn PI. 20.8511
> 15W
> 1ON
> ODOK
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
> ABgregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Wargin
> 1.43
> 23.71 %
> 1.85
> 39.559
> 38.06%
> 33.35900


BAB因子有了进一步提升，从1.28到1.43

**Summary:**

**
> [!NOTE] [图片 OCR 识别内容]
> VM
> 351
> SON
> ZSW
> 01/03/2020
> TraIn PI. 23.3211
> ZOW
> 15W
> 1OW
> OOOK
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
> ABBrE
> Data
> Sharpe
> Turnover
> Fitness
> Rezurns
> Drawdown
> Wargin
> 41
> 36.649
> 0.25
> 13.629
> 22.749
> 7.439000
> eBate
**


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> PASS
> Fitness of
> 59 Is above cutoff of
> Turnoverof 25,03%
> above cutoffof 19
> Turnoverof 25.03%
> below CUtOff of 70%。
> Welght Is Well distributed over instruments.
> FAIL
> Sharpe of 1.31Is below CUOff of -
> SUb-universe Sharpe Of 0.49
> below CUOff OT 0.57。
> [5ladder Sharpe Of 1.27 is below CUtoff of 1.58 for ladder year 4: 1/24/2022...1/25/2018
> WARNING
> Theme GLB 01 Theme does not match with multiplierof 2
> PENDING


经过多个版本迭代可以看出，因子的sharp还是需要提高，每次迭代只是对BAB因子表现有部分提升，每次迭代收益率曲线形态基本是相似的。可以看出每次迭代都不能明显降低最大回撤，这有可能与beta在流动性限制的区间趋同，BAB因子失效有关，还需要进一步研究降低BAB趋同的方法。


---
