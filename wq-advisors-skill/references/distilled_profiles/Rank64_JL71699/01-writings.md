# 顾问 JL71699 (Rank 64) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 JL71699 (Rank 64) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: data存储与主题数据高效获取方法代码优化
- **主帖链接**: data存储与主题数据高效获取方法代码优化.md
- **讨论数**: 8

目前的很多主题活动都会限制活动数据集，但是每一次都去通知里面找起来一个一个修改很麻烦，所以本人分享自己存储数据集与应用数据集的一个好方法首先第一步，先获取所有能用到的dataseturl = brain_api_url + "/data-sets?" +\f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"这个url可以获得所有能用上的dataset然后通过下面这个url获取所有datafieldurl_template = ("[链接已屏蔽])然后对matrix数据和vec数据做相应操作，本人对vec操作是遍历自己有的所有vec操作符，最后以dataframe的格式作为储存，如下图所示然后是筛选主题数据url=f'[链接已屏蔽]通过这个url可以得到所有的活动数据然后做一个简单判断就能得到活动数据就ok了同理，用这种数据储存结构也能做到定向点塔希望这个方法能对大家对数据处理有新的帮助

---

### 帖子 #2: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.comdata存储与主题数据高效获取方法代码优化_38187278934551.md
- **讨论数**: 8

目前的很多主题活动都会限制活动数据集，但是每一次都去通知里面找起来一个一个修改很麻烦，所以本人分享自己存储数据集与应用数据集的一个好方法

首先第一步，先获取所有能用到的dataset

url = brain_api_url + "/data-sets?" +\

f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"

这个url可以获得所有能用上的dataset

然后通过下面这个url获取所有datafield

url_template = (" [[链接已屏蔽]) ?"

f"instrumentType={instrument_type}&region={region}&delay={delay}"

f"&universe={universe}&dataset.id={dataset_id}&limit=50&offset={{x}}")

然后对matrix数据和vec数据做相应操作，

本人对vec操作是遍历自己有的所有vec操作符，

最后以dataframe的格式作为储存，如下图所示


> [!NOTE] [图片 OCR 识别内容]
> Py
> dataset
> datafields
> USA/DIIIMBALANCE
> imbalancel
> [imbl_datatime; imbl_imbalance; imbl_value]
> USA/DIIIMBALANCE
> imbalances
> [imb5_mktcap; imb5_score]
> 2
> USA/DIIINSIDERS
> insiders1
> [buy_to
> amount_ratio_Imo;
> to_
> amo。
> 3
> USA/DIIINSIDERS
> insiders3
> [insd3_1Ok_freq_
> insd3_1Ok_freq_latest_fi._
> USA/DI/INSIDERS
> insiders4
> [vec_avg(insd4_bonus); vec_stddev(insd4_bonus)
> 56
> USA/DI/SOCIALMEDIA
> socialmedia3g
> [Vec
> avg(scl3g_top5_people_also_watch_ticker_i
> 57
> USA/DI/SOCIALMEDIA
> socialmedia4
> [vec_avg(scl4_actions_per_post_fb); Vec_stddev。
> 58
> USA/DI/SOCIALMEDIA
> socialmedias
> [vec_avg(scl5_createdts_time); Vec_stddev(scls。
> 59
> USA/DI/SOCIALMEDIA
> socialmedia8
> [snt_social_value; snt_social_volume]
> 60
> USA/DI/SOCIALMEDIA
> socialmediag
> [vec_avg(sclg_dispersion), vec_stddev(sclg_dis._
> _Sell
> buy_t
> _sell
> flag;


然后是筛选主题数据

url=f' [[链接已屏蔽]) '

通过这个url可以得到所有的活动数据

然后做一个简单判断就能得到活动数据就ok了

同理，用这种数据储存结构也能做到定向点塔

希望这个方法能对大家对数据处理有新的帮助

---

### 帖子 #3: ATOM比赛经验分享之如何获得更好的OS分数
- **主帖链接**: https://support.worldquantbrain.com[L2] ATOM比赛经验分享之如何获得更好的OS分数_28112779430423.md
- **讨论数**: 5

这次很荣幸在ATOM获得了全球总分第一名，其中我的IS分数是全球总分第二，OS分数是全球总分第一。在这里分享一些我获得高的OS分数的心得，也希望能帮助大家打接下来的比赛。即使不打比赛，这些经验对于平时提升value factor，或者merged os performance，也应当会有所帮助。

OS分数即组合的样本外表现，既取决于单个alpha的质量，也取决于alphas等权组合的整体效果。因此这篇文章也将从组合整体与单个alpha两个角度出发去阐释这个问题。

组合整体：

1. IS分数高的，OS分数也高。

如果把组合优化看成训练一个模型，那么IS分数可以说是样本内的拟合程度。如果一个模型本身欠拟合，我们只能期待他在样本外的表现与样本内波动小，但无法期待它样本外的表现能有多好。 **比赛的IS分数，本质上是在引导参赛者提交高sharpe，低turnover，高margin，低drawdown，以及最关键的，低self-correlation的alphas。** 这里的低self-correlation不仅仅指的是与组合里最高的alpha的self-correlation，而是跟组合里所有的alphas的self-correlation。

就个人经验而言，哪怕一个alpha它的max self-correlation并不高，可能0.38左右，但是组合里面有大量与之在0.2~0.3之间的self-correlation的alphas，那么这个alpha是很难加分的。

关于这其中的原理，可以参考 [ZL29184](/hc/en-us/profiles/22955594228503-ZL29184)  的文章：

[为什么要尽量交低相关的Alpha?Why similar alpha fails: intuition from Markowitz portfolio management theory – WorldQuant BRAIN](../顾问 CT68712 (Rank 27)/[Commented] 为什么要尽量交低相关的AlphaWhy similar alpha fails  intuition from Markowitz portfolio management theory_27986550038423.md)


> [!NOTE] [图片 OCR 识别内容]
> Hanoi Ur
> 0N41247
> 105
> 67,272
> 52,033
> 55,842
> 31,652
> 24,601
> 10,788
> 9,752
> 7,884
> Science
> Technold
> The Univ
> TL87739
> 130
> 64,247
> 60,980
> 61,797
> 5,015
> 4,120
> 20,134
> 7,764
> 3,472
> 9,993
> WD90077
> 134
> 63,161
> 53,092
> 55,609
> 12,375
> 3,654
> 19,886
> 7,975
> 13,928
> 11,320
> Peking
> VNU - Ur
> TN48752
> 114
> 62,613
> 59,601
> 60,354
> 29,809
> 8,391
> 22,037
> 11,054
> 6,479
> 25,187
> Enginee
> Technola
> Universit
> 65
> H026227
> 47
> 60,589
> 27,010
> 35,405
> 21,984
> 9,563
> 3,882
> 37,165
> and Com
> Symbios
> RP41479
> 82
> 59,619
> 56,403
> 57,207
> 19,701
> 6,916
> 9,244
> 11,373
> Internat
> Universit
> 16
> TC50299
> 59,493
> 44,978
> 48,606
> 5,890
> 12,487
> Academy
> 15
> 5138692
> 74
> 59,303
> 45,445
> 48,910
> 7,837
> 31,449
> 7,695
> Hanyang
> Academy
> 11
> NM98411
> 58,940
> 48,609
> 51,192
> 8,330
> 12,889
> 17,620
> Cryptogr
> Techniau
> Kong


把ATOM榜单按照IS降序排名，发现IS高分的多数OS也高分。

因此，如果想要提高OS分数但又不知从何入手，把IS分数往上打，是一个简单而又好用的思路。

2. alphas数量多的，OS表现好。


> [!NOTE] [图片 OCR 识别内容]
> Natione
> 64
> ]C85226
> 68
> 35,404
> 35,696
> 35,623
> 10,297
> 23,037
> 8,245
> 6,138
> Chiao
> Natione
> 10
> KK82709
> 164
> 48,811
> 52,328
> 51,449
> 17,293
> 5,475
> 24,300
> 17,166
> 5,446
> Univer
> Johns
> 36
> T77745
> 158
> 27,081
> 46,776
> 41,852
> 9,831
> 3,183
> 16,399
> 15,482
> 7,474
> 7,091
> Univer
> Natione
> 49
> 顾问 CC40930 (Rank 95)
> 157
> 39,879
> 37,332
> 37,968
> 10,861
> 29,543
> 7,539
> Univer
> Univer
> Econon
> 33
> PT27687
> 154
> 36,390
> 44,976
> 42,830
> 12,785
> 17,546
> 20,109
> 11,454
> Vietnar
> Univer
> Minh
> Natione
> 210
> HC40538
> 154
> 16,023
> 29,965
> 26,479
> 6,691
> 9,049
> 3,824
> Univer
> 90
> LN78195
> 147
> 46,217
> 29,123
> 33,397
> 15,219
> 17,748
> 5,224
> 33,169
> 296
> 0164461
> 141
> 8,308
> 27,898
> 23,001
> 3,508
> 5,902
> 4,755
> Foreigr
> Univer
> 214
> 0030226
> 136
> 11,719
> 31,336
> 26,432
> 9,559
> CHUKA


将ATOM比赛榜单按数量降序可以看出，提交数量多的人之中，绝大多数的OS都好于IS，尤其是IS分数在2w~4w分的段位上。

提交更多的，稳健的，相关性低的alphas，也就是更diverse的，对于一个好的OS是至关重要的，这也符合组合优化的基本原理。

个人九月份交的alphas少，所以最新一期的value factor从0.88骤减到0.13，也是这个观点的作证...

3. 优化组合

这个问题既是整体问题，也涉及到单个alpha该怎么提交的问题。总的来说，在提交单一alpha的时候，除了关注alpha本身的稳健性和pnl，我们还格外需要关注这个alpha放入组合之后对组合带来的变化。

展示一下ATOM在中后期的时候我截图的一个alpha，放入组合之后的表现：


> [!NOTE] [图片 OCR 识别内容]
> N
> Performance Comparison
> Delay-1 Score
> Before Submission
> After Submission
> Change
> Last Run; Fri, 11/08/2024,10:08 AM
> 55,704
> 56,062
> 358
> Delay-1 Weekly Score
> Before Submission
> After SUbmission
> Change
> 3,472
> 3,472
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawqown
> Margin
> 13.97
> 0.06
> 13.64 % ,-0.05
> 10.46
> 40.08
> 7.64 %
> 40.01
> 0.15 % .0.00
> 11.20 %oo 40.05
> IS Performance After Submission (ATOM 2024 alphas)
> Combined performance data is shown forall ATOM 2024 alphas
> Submitting this alpha will not effect the combined performance Of your other alphas_
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2012
> 16.93
> 0.10
> 15.06 %
> 0.06
> 12.23
> 0.05
> 7.86 %
> 0.06
> 0.04 %
> 0.00
> 10.44 %00
> 0.04
> 2013
> 14.56
> 0.17
> 14.30 %
> 0.05
> 10.91
> 0.15
> 8.03 %
> 00
> 0.099
> 0.00
> 11.24900
> 0.06
> 2014
> 17.10
> 0.13
> 13.74 %
> -0.06
> 13.00
> 0.15
> 7.94 %
> 0.03
> 0.07 %
> 11.56 %00
> 0.10
> 2015
> 17.83
> 0.16
> 13.65 %
> -0.06
> 14.71
> 0.20
> 9.29%
> 0.05
> 0.06 9
> 0.00
> 13.61 %00
> 0.12
> 2016
> 13.53
> 0.09
> 13.65 %
> -0.05
> 9.69
> 0.09
> 7.00 %
> 0.01
> 0.12 %
> 00
> 10.26 %oo
> 0.06
> 2017
> 14.39
> 0.12
> 13.49 %
> 0.04
> 9.79
> 0.15
> 6.24 %
> 0.06
> 0.07 %
> 0.00
> 9.25 %00
> 0.12
> 2018
> 12.49
> 0.07
> 13.50 %
> 0.04
> 8.57
> 0.09
> 6.35 %
> 0.04
> 0.11 %
> 0.00
> 9.41 %0o
> 0.09
> 2019
> 13.31
> 0.07
> 13.45 %
> ~0.05
> 9.15
> 0.08
> 6.35 %
> 0.02
> 0.06 9
> 0.00
> 9.44%00
> 0.06
> 2020
> 10.82
> -0.07
> 13.47 %
> -0.06
> 7.54
> 0.08
> 6.54 %
> 0.08
> 0.15 %
> 9.71 %00
> 0.08
> 2021
> 13.50
> -0.12
> 13.09 %
> 0.06
> 11.30
> -0.10
> 9.17 %
> 0.04
> 0.10 %
> 0.01
> 14.02%0o
> 0.01
> 2022
> 14.85
> 0.05
> 13.15 %
> -0.06
> 13.41
> 0.08
> 10.73 %
> 0.01
> 0.0796
> 00
> 16.32%00
> 0.09
> Pnl


这个alpha本身是一个不错的alpha，也可以加分，但是提交后会进一步降低组合在2020年的sharpe。我的组合本来在2020年的sharpe就比较低了，这意味着组合面对2020年的市场条件下，预测能力有所减弱。一个比较好的组合，我们是希望他在每一年的sharpe差异比较小的，也就意味着它在不同的年份，即不同的市场条件下，都有稳定的预测能力。因此这个alpha我并没有立刻提交，而是留了一段时间。

在比较后期我的组合pnl截图：


> [!NOTE] [图片 OCR 识别内容]
> Pnl
> 6,0OOK
> 5,0OOK
> 4,0OOK
> 3,00OK
> 2,00OK
> 1,00OK
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
> Pnl Before Submission
> Pnl After Submission


从单个alpha的角度：

1. 对于不同中性化设置稳健的alpha。

在各种研报和论文之中，作者往往会把自己实证的factor对各类风格因子进行中性化，目的就是检验这个factor不能被这些风格因子所解释部分的预测能力。如果一个alpha，切换中性化后效果大打折扣，那么很可能它的收益是暴露在这个分组之上的。这种alpha能给组合带来的信息增益是有限的。

2. pnl表现稳健的alpha

这个原理是类同于整体pnl的，也就是单个alpha我们希望它能在不同市场条件下都有稳定的预测能力。比起短期的回撤，我会更在乎出现一年及以上的平缓期或者回撤。尤其不希望在近一年decay。

好的pnl示例：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 4,5OOK
> 4,0OOK
> 3,50OK
> 3,00OK
> 25OOK
> 2,0OOK
> 1,5OOK
> 1,00OK
> SOOK
> 07/19/2012
> IPn: 12.53k
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


不好的pnl示例：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 7,00OK
> OOOK
> 5,OOOK
> 4,0OOK
> 3,00OK
> 2,00OK
> 1,00OK
> 04/04/2013
> ISPnL; 142.35k
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
> NM


上图2的alpha，从2016年一路回撤到了2018年夏天，这种长达2年的回撤是足以让人质疑这个alpha的稳健性的。

尽管pnl分析法会认为图1更稳定，但是取决于OS的时间段，图2alpha的OS表现不一定就弱于图1，或者说有些alpha就是风格暴露、行业暴露，但是正好暴露在了OS时间赚钱的风格/行业上，它OS就是容易好。

因此从打比赛的角度考虑，图二这样的alpha也不是不能交，但是需要建立在已经有大量稳健优质的alpha、图二的alpha要与组合有低的相关性，以及能够优化组合的一些指标，的前提之上。

3. 指标好看的alpha


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawcown
> Margin
> 2.37
> 4.759
> 2.53
> 14.24%
> 8.979
> 59.929600


一般做alpha的时候，注意力往往会集中在sharpe和fitness上，但是margin同样也是十分重要的，这意味着这个alpha在扣除手续费之后到底能不能赚到钱。有一些比赛，会测试扣除手续费之后的os，那么组合里如果都是margin低的alphas，可想而知会有更低的分数。

---

### 帖子 #4: Research Paper 07: Relative Strength Strategies for InvestingPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper 07 Relative Strength Strategies for InvestingPinned_15602317429655.md
- **讨论数**: 0

**Abstract:**

The purpose of this paper is to present simple quantitative methods that improve risk-adjusted returns for investing in US equity sectors and global asset class portfolios. A relative strength model is tested on the French-Fama US equity sector data back to the 1920s that results in increased absolute returns with equity-like risk. The relative strength portfolios outperform the buy and hold benchmark in approximately 70% of all years and returns are persistent across time. The addition of a trend-following parameter to dynamically hedge the portfolio decreases both volatility and drawdown. The relative strength model is then tested across a portfolio of global asset classes with supporting results.

Author: Meb Faber

Year: 2010

Link:  [[链接已屏蔽])

**Key ideas and Comments from WorldQuant:**

- Page 6 and page 7
- Page 11 and page 12

*Faber presents that using a simple moving average timing strategy could avoid the large drawdowns in momentum portfolios.*

**Useful datafields on BRAIN:**

**Term**

**Datafield**

**Dataset**

returns

returns

[**Price Volume Data for Equity**]([链接已屏蔽])

dividends

dividend

[**Price Volume Data for Equity**]([链接已屏蔽])

---

### 帖子 #5: Research Paper 08: Good Volatility, Bad Volatility and the Cross-Section of Stock ReturnsPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper 08 Good Volatility Bad Volatility and the Cross-Section of Stock ReturnsPinned_15765182114071.md
- **讨论数**: 0

**Abstract**

Based on intraday data for a large cross-section of individual stocks and newly developed econometric procedures, we decompose the realized variation for each of the stocks into separate so-called realized up and down semi-variance measures, or “good” and “bad” volatilities, associated with positive and negative high-frequency price increments, respectively. Sorting the individual stocks into portfolios based on their normalized good minus bad volatilities results in economically large and highly statistically significant differences in the subsequent portfolio returns. These differences remain significant after controlling for other firm characteristics and explanatory variables previously associated with the cross-section of expected stock returns.

Author: Tim Bollerslev, Sophia Zhengzi Li, and Bingzhi Zhao

Year : 2018

Link: [**[链接已屏蔽])

**Key ideas and Comments from WorldQuant:**

- Page 21 Paragraph 2
- Page 23 Paragraph 2

*This new categorization of volatility acts well as a factor in D1 alphas, moreover, it is quite useful in intraday alpha research.*

**Term**

**Data field**

**Dataset**

price

mdf_pri

**Model Data**

stock return

returns

[**Price Volume Data for Equity**]([链接已屏蔽])

high

high

[**Price Volume Data for Equity**]([链接已屏蔽])

---

### 帖子 #6: Research paper 71: The Information Content of Option Demand
- **主帖链接**: https://support.worldquantbrain.com[L2] Research paper 71 The Information Content of Option Demand_17611254171031.md
- **讨论数**: 46

**Abstract :**

This paper combines the concept of market sidedness with excess option demand (changes in open interest) to solve the empirical challenge of separating directional from uninformed trading motives in widely available, unsigned options data. Our measure of options market sidedness persistently predicts the sign and strength of stock returns.

Trading strategies conditional on the measure are highly profitable. For instance, when the measure indicates positive (negative) information, out-of-the-money calls (puts) generate returns of 27% (32%) over roughly four weeks. Risk-adjusted returns of a long-short equity strategy yield more than 2%. An increase in directionally informed demand predicts a decrease in option liquidity and increases in pricing inefficiency.

Author : Kerstin Kehrle , Tatjana Xenia Puhan

Year 2015

Link :  [[链接已屏蔽])

**Key ideas and Comments from WorldQuant:**

Page 20 para 3

Page 17 para 2

Page 26 para 2

**Term**

**Datafield**

**Link**

change

opt4_total_openinterest

[Option4]([链接已屏蔽])

volatility

opt1_p_deltasurface_d1_vi

[Option1]([链接已屏蔽])

asymmetric information'

mdl230_totalcap_cusip_pc_ratio

[Model32]([链接已屏蔽])

---

### 帖子 #7: Research Paper 72: Testing for Asset Price Bubbles using Options Data
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper 72 Testing for Asset Price Bubbles using Options Data_16412791948695.md
- **讨论数**: 29

**Abstract**

We present a new approach to identifying asset price bubbles based on options data. We estimate asset bubbles by exploiting the differential pricing between put and call options. We apply our methodology to two stock market indexes, the S&P 500 and the Nasdaq-100, and two technology stocks, Amazon and Facebook, over the 2014-2018 sample period. We find that, while indexes do not exhibit significant bubbles, Amazon and Facebook show frequent and significant bubbles. The estimated bubbles tend to be associated with high trading volume and earning announcement days. Since our approach can be implemented in real time, it is useful to both policy-makers and investors. As an illustration we consider two case studies: the Nasdaq dot-com bubble (between 1999 to 2002) and GameStop (between December 2020 and January 2021). In both cases we identify significant and persistent bubbles.

Author: Nicola Fusari, Robert Jarrow, Sujan Lamichhane

Year: 2020

Link:  [[链接已屏蔽])

Key ideas and Comments from WorldQuant:

- Page 11 Paragraph 2
- Page 22 Paragraph 2,3
- Page 25 Paragraph 1
- Page 28 Paragraph 2

**Term**

**Data field**

**Dataset**

option

fnd6_optgr

[Company Fundamental Data for Equity]([链接已屏蔽])

call option

call_breakeven_10

[Options Analytics]([链接已屏蔽])

---

### 帖子 #8: Research Paper: First Impression Bias: Evidence from Analyst ForecastsPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper First Impression Bias Evidence from Analyst ForecastsPinned_14353241718423.md
- **讨论数**: 0

**Abstract:**

We present evidence of first impression bias among finance professionals in the field. Equity analysts’ forecasts, target prices, and recommendations suffer from first impression bias. If a firm performs particularly well (poorly) in the year before an analyst follows it, that analyst tends to issue optimistic (pessimistic) evaluations. Consistent with negativity bias, we find that negative first impressions have a stronger effect than positive ones. The market adjusts for analyst first impression bias with a lag. Finally, our findings contribute to the literature on experience effects. We show that a set of professionals in the field, equity analysts, apply U-shaped weights to their sequence of past experiences, with greater weight on first experiences and recent experiences than on intermediate ones.

Key ideas:

- Page 19 paragraph 1
- Page 22 paragraph 3

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

eps forecast

mdl77_ooearningsmomemtummodel_spe2yfvc_cf

**[Model77]([链接已屏蔽])**

consensus analysis

mdl77_fc_rev6

**[Model77]([链接已屏蔽])**

dividend forecast

anl34_Stockdivforecasts_expectedamount

**[Analyst34]([链接已屏蔽])**

Author: David A. Hirshleifer, Ben Lourie, Thomas Ruchti, Phong Truong

Year : 2020

Link:  [[链接已屏蔽])

---

### 帖子 #9: Research Paper: Stock Return Autocorrelations and Expected Option ReturnsPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper Stock Return Autocorrelations and Expected Option ReturnsPinned_14437549763223.md
- **讨论数**: 0

**Abstract:**

We present a new finding that the return autocorrelation of underlying stock is an important determinant of expected equity option returns. Using an extended Black-Scholes model incorporating the presence of stock return autocorrelation, we show that expected returns of both call and put options are increasing in return autocorrelation coefficient of the underlying stock. Consistent with this insight, we find strong empirical support in the cross-section of average returns of equity options. Average returns of calls and puts as well as average returns of straddles all show monotonically increasing relationship with the degree of underlying stock's return autocorrelation coefficient. Additional equity option portfolio analysis shows that the information on stock return autocorrelation helps investors to significantly improve the out-of-sample performance of their portfolios.

Key ideas:

- Page 11 paragraph 2
- Page 19 paragraph 1

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

moneyness

opt1_raw_deltasurface_d1_moneyness

[**Option1**]([链接已屏蔽])

equity option

opt14_lastprice

[**Option14**]([链接已屏蔽])

Author: Yoontae Jeon, Raymond Kan, Gang Li

Year : 2020

Link:  [[链接已屏蔽])

---

### 帖子 #10: Robustness Test
- **主帖链接**: https://support.worldquantbrain.com[L2] Robustness Test_25238340364695.md
- **讨论数**: 13

**Robustness Test**

The IS performance of an Alpha isn’t the ultimate goal when researching an idea for an Alpha. The true goal is to create a robust Alpha that can still retain performance under different scenarios. To actually test if your Alpha hypothesis is true, a strong IS performance when backtesting on the BRAIN platform isn’t enough. So you should incorporate your own robustness test into your Alpha Creation Engine (ACE).

- **Super/Sub universe test:**

You can conduct the super/sub universe test on your own by using a smaller/bigger universe in the simulation setting. Though the result may differ from the result message in the IS testing status of your original Alpha, you can define the performance threshold as:

1. For sub universe test:


> [!NOTE] [图片 OCR 识别内容]
> SizeTargetlni
> TargetUniPerformance
> Tatio
> OrigiallniPerforace
> SizeOriginallJi


Here, you can aim for the performance to retain 70%. For the original Alpha without any subuniverse, you can skip this test (be aware that the ILLIQUID universe is completely different from the smaller universe, so their performance can’t be compared)

1. For super universe test:


> [!NOTE] [图片 OCR 识别内容]
> TargetUniPerforace
> Tatio
> OriginalUniPerforance


Here, you can also aim for the performance to retain 70%. For the original Alpha without any super universe, you can skip this test.

- **Self OS test:**

Another way to assess how robust your Alpha is, is by recreating a self OS test, where you only research Alpha with a part of the backtest period as your IS, and reserve the other part as your self OS. You can choose any period you want, but a rule of thumb is the self OS period should be around 2-4 years to ensure that the IS period is long enough so that its performance is actually meaningful. After creating a submittable Alpha on the IS period, you can assess the robustness on the self OS period. Some metrics that you can use are:

You can create a self OS/IS period by doing so using the ace library. Here is a pseudo-code snippet:

```
        pnl = get_alpha_pnl(s, alpha_id)        tvr = get_alpha_turnover(s, alpha_id)        is_cutoff = ‘2021-01-01’        self_is_pnl, self_os_pnl =  pnl.loc[df.index < is_ cutoff], pnl.loc[df.index >= is_ cutoff]        self_is_tvr, self_os_tvr = tvr.loc[df.index < is_ cutoff], tvr.loc[df.index >= is_ cutoff]
```

From the above self IS/OS period, you can calculate your alpha Sharpe, Turnover, and Return. If you create your alpha optimization algorithm, try to only optimize it on the self IS period, and validate the optimized alpha performance on the self OS period. Some more robustness tests you can use to validate your alpha performance are:

1. OS sharpe over IS sharpe ratio:

You can define your own performance threshold as:


> [!NOTE] [图片 OCR 识别内容]
> OSSharpe
> Tatio
> ISSharpe


Here, you can aim for the performance to retain around 70% when comparing between the OS and IS period.

1. Turnover ratio:

A sudden turnover jump during the backtest is also undesirable:


> [!NOTE] [图片 OCR 识别内容]
> OSTuOUer
> 三 Tatio
> ISTTODeT


Here, you can aim for the turnover changes to be less than one when comparing between the OS and IS period.

- **Distribution test:**

1. Rank test

To ensure that your alpha doesn’t favor some stocks, you can resimulate the Alpha but with the rank operation at the end of the Alpha, in order to redistribute the Alpha weight uniformly. And check how much the performance drops:


> [!NOTE] [图片 OCR 识别内容]
> RankSharpe
> 0.5
> OrigaiSharne


You can aim to have an Alpha that retains at least 50% of its performance after the rank operation.

1. Sign test

Another test to check the your Alpha performance without the original Alpha weight distribution is by applying the sign operation at the end of the Alpha, and assessing how good the Alpha is at predicting the instrument price direction.


> [!NOTE] [图片 OCR 识别内容]
> SignSharpe
> 0.4
> OrigmalSharne


You can aim to have an Alpha that retains at least 40% of its performance after the sign operation.

---

### 帖子 #11: WorldQuant Brain Insights: Tips for Boosting Research and Model Effectiveness
- **主帖链接**: https://support.worldquantbrain.com[L2] WorldQuant Brain Insights Tips for Boosting Research and Model Effectiveness_27731484228247.md
- **讨论数**: 36

Some valuable tips to improve your quantitative models and research:

1. **Company Fundamental Data for Equity**
   - Use time series operators like  `ts_rank` ,  `ts_zscore` , and  `ts_delta`  to analyze well-structured company fundamental data.
2. **Achieving Reasonable Margin Rates**
   - Optimize margin rates using operators like  `hump_decay` ,  `ts_decay_linear` , and  `ts_decay_exp_window` .
3. **Evaluating Company Well-being Through Employee Data**
   - Assess how well a company cares for its employees by using employee-related data to identify correlations with company performance.
4. **Alpha Submission Criteria Based on Sharpe Retention**
   - Submit alphas that retain at least 70% of their Sharpe ratio when applied to a sub-universe or super-universe.
5. **Ensuring Data Coverage Through Backfilling**
   - Improve data coverage by using operators like  `ts_backfill` ,  `group_backfill` , and  `group_extra`  to backfill missing data.
6. **Increasing Novelty to Reduce Correlation**
   - Try using operators and settings you haven't used before to reduce correlation with others' work. Refer to  *Detailed Operator Descriptions*  for new ideas.
7. **Exploring Neutralizations Beyond Country and Sector**
   - While country and sector neutralizations are effective, try experimenting with other groups such as industries to improve model robustness.
8. **Using  `ts_step(1)`  as a Time Variable in  `ts_regression`**
   - Set time as a variable in regression by using  `ts_step(1)`  within the  `ts_regression`  operator to model trends over time.
9. **Utilizing Seasonality Datafields in Research Indicators**
   - Enhance your signals by leveraging seasonality datafields to uncover patterns based on time cycles.
10. **Comparing Model Predictions with Returns**
   - Use  `ts_corr`  and  `ts_regression`  to compare model predictions with actual returns for validation and performance evaluation.
11. **Creating Alphas with High Dataset Value Scores**
   - Try creating alphas using datasets with a high dataset value score (e.g., Earnings Datasets, Macro Datasets, Insider Datasets) to reduce product correlation.
12. **Focusing on Idea Refinement Over Parameter Fitting**
   - Focus on improving alphas by refining your ideas rather than adding or fitting parameters, factors, or reversion elements.
13. **Reducing Turnover of Illiquid Universe**
   - Use the  `rank()`  operator to reduce turnover for illiquid parts of the universe. As a proxy for liquidity, you can use market cap or average volume.
14. **Ensuring Coverage by Backfilling Datafields and Alpha**
   - Improve coverage by backfilling datafields and the final alpha using operators such as  `ts_backfill` ,  `group_backfill` , and  `group_extra` .
15. **Improving Alphas by Refining Ideas, Not by Adding Parameters**
   - Focus on refining your ideas rather than adding more parameters, factors, or reversion elements to enhance the quality of your alphas.

Feel free to share your own tips and insights if you have any! The more we contribute, the better we can enhance our skills in model building and research. Let’s all work together to improve our quantitative strategies and generate better alphas!

---

### 帖子 #12: [BRAIN TIPS] 6 ways to quickly evaluate a new datasetFeatured
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] 6 ways to quickly evaluate a new datasetFeatured_11807866133911.md
- **讨论数**: 15

WorldQuant BRAIN has thousands of datafields for you to create alphas. But how do you quickly understand a new datafield? Here are 6 ways. Simulate the below expressions in “None” neutralization and decay 0 setting. And obtains insights of specific parameters using the Long Count and Short Count in the IS Summary section of the results.

**Sr. No**

**Expression**

**Insight**

1

datafield

%  **coverage** , would approximately be ratio of (Long Count + Short Count in the IS Summary )/ (Universe Size in the settings)

2

datafield != 0 ? 1 : 0

**Coverage** . Long Count indicates average non-zero values on a daily basis

3

ts_std_dev(datafield,N) != 0 ? 1 : 0

**Frequency**  of unique data (daily, weekly, monthly etc.).

Some datasets have data backfilled for missing values, while some do not. The given expression can be used to find the frequency of unique datafield updates by varying N (no. of days).

Datafields with a quarterly unique data frequency would see a Long Count + Short Count value close to its actual coverage when N = 66 (quarter). When N = 22 (month) Long Count + Short Count would be lower (approx. 1/3rd of coverage) and when N = 5 (week), Long Count + Short Count would be even lower.

4

abs(datafield) > X

**Bounds**  of the datafield. Vary the values of X and see the Long Count. For example, X=1 will indicate if the field is normalized to values between -1 and +1?

5

ts_median(datafield, 1000) > X

**Median**  of the datafield over 5 years. Vary the values of X and see the Long Count. Similar process can be applied to check the mean of the datafield.

6

X < scale_down(datafield) && scale_down(datafield) < Y

**Distribution**  of the datafield. scale_down acts as a MinMaxScaler that can preserve the original distribution of the data. X and Y are values that vary between 0 and 1 that allow us to check how the datafield distribute across its range.

For example, if you simulate [close <= 0], You will see Long and Short Counts as 0. This implies that closing price always has a positive value (as expected!)

---

### 帖子 #13: [BRAIN TIPS] Increasing the capacity of alphas
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] Increasing the capacity of alphas_8677091679383.md
- **讨论数**: 1

Broadly speaking, a high capacity alpha can be associated with three major norms: high liquidity, low correlation and low turnover. Of these, the most significant contributor to the increase in capacity is  **low turnover.**  By definition, low turnover means that the alpha is trading with less frequency — which means fewer transactions are being processed and in that way we have the capability to trade more easily. Hence, we are increasing the capacity of the alpha. There are many ways of reducing wasteful turnover of an alpha. A very basic method is the  [**hump operation**]([链接已屏蔽]) . This operation is supposed to analyze the alpha values of an existing alpha and then manipulate some of them to reduce the turnover of that alpha.
 **Basic Idea:**  In general, for a normal alpha the value changes every day per its formula. Many times the alpha’s value doesn’t change significantly, yet the alpha still has to simulate a trade. The simulated PnL generated in these transactions is not that great, but the transaction costs involved are still pretty high. This is wasteful turnover that can be reduced smartly with simple techniques. We can define a threshold in terms of the percentage of change in the alpha value and  **simulate a trade only when the percentage change crosses that threshold value** .

 **Improvement:**  The single threshold value could be variable depending upon market conditions (different ways of evaluating — e.g., movement/volatility of index).

Each instrument could have a variable threshold (liquidity/market-cap/volatility).

There can also be a single threshold value for a group (subindustry/sector/custom group).

Increasing the threshold values either uniformly or not uniformly after ranking the instruments on the basis of a few factors (market-cap/volatility) can help.

 **Future direction:**  The impact of volatility is much more important than any other factor for deciding the capacity of the alpha, and also the individual thresholds of stocks in the hump operation. Looking at it a bit differently, try to think in line with an event alpha. Keep monitoring the short-term volatility of the stock, and also keep a sense of average long-term stock volatility. Whenever the stock volatility has a spike and crosses a certain (customizable) threshold, the alpha starts simulating a trade as per its values, with the idea that this is the period in which the alpha might generate simulated profits. For the other times, we keep holding the stock, or alternatively we can continue with the previous hump operation during these times but with a much stricter threshold.

---

### 帖子 #14: [BRAIN TIPS] Using trade_when for Event Alphas and Low Turnover Alphas
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] Using trade_when for Event Alphas and Low Turnover Alphas_8360363631127.md
- **讨论数**: 10

You can use the following targeting to create event-driven alphas and low turnover alphas.

 **Concept:** 
If (event) {
Assign alpha values;
} else {
Hold alpha values;
}
Expression:

```
trade_when(Event_condition, Alpha_expression, -1)
```

**Pros:**

- Good alpha coverage
- Flexible in determining events
- Can be used to enhance signals by trading at the right time
- Low turnover and low cost alpha

**Cons:**

- Not easy to get high Sharpe alpha
- Not easy to get high return alpha

**Approach:** 
Define events: Any spike in returns, data values and technical indicators can be used to define events.
Alpha assignment: Look for signals that are aligned with the abnormality of an event — that is, alphas that need to be executed when such events happen.

 **Note:** 
Hold alpha can be replaced by decaying alpha linearly or exponentially.
Check alpha coverage to make sure events are not so rare.

---

### 帖子 #15: 【Alpha灵感】Gordon Growth Model
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Gordon Growth Model_19925969895191.md
- **讨论数**: 4

**标题：** 增强动态戈登增长模型 **作者：** 巴特图勒嘎·甘库

**关联:**  [[链接已屏蔽])

**什么是戈登增长模型（GGM）？** 
戈登增长模型（GGM）是一个公式，用于根据未来一系列以恒定速率增长的股息来确定股票的内在价值。 它是股息贴现模型 (DDM) 的一种流行且简单的变体。 GGM 假设股息以恒定的速度无限增长，并求解一系列未来股息的现值。

由于该模型假设增长率恒定，因此一般仅用于每股股息增长率稳定的公司。

**戈登增长模型公式** 
戈登增长模型公式基于以恒定速率增长的无限系列数字的数学特性。 该模型中的三个关键输入是每股股息 (DPS)、每股股息增长率和所需回报率 (ROR)。


> [!NOTE] [图片 OCR 识别内容]
> D(1+8)
> p
> k - 吕
> P
> intrinsic stock Value
> Current annual
> D
> dividend per share
> K
> required annual
> rate ofreturn
> annual dividend
> 8
> growth rate


GGM 试图计算股票的公允价值，而不考虑当前的市场条件，并考虑股息支付因素和市场的预期回报。 如果从模型中获得的价值高于股票的当前交易价格，则该股票被认为被低估并有资格购买，反之亦然。

每股股息代表公司每年向其普通股股东支付的金额，而每股股息增长率是每股股息从一年到另一年的增长率。 所需回报率是投资者在购买公司股票时愿意接受的最低回报率，投资者可以使用多种模型来估计该回报率。

**戈登增长模型的例子** 
作为一个假设的例子，考虑一家公司的股票交易价格为每股 110 美元。 该公司要求最低回报率为 8%（r），明年（D1）将支付每股 3 美元的股息，预计每年增加 5%（g）。

股票的内在价值（P）计算如下：

```
P = ($3)/(.08 - .05) = $100
```

根据戈登增长模型，该股目前在市场上被高估了 10 美元。


> [!NOTE] [图片 OCR 识别内容]
> Simulation 6
> CODE
> RESULTS
> LEARN
> D4TA
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Settings
> USA/DIIILLIQUID_MINVOLIN
> Conyertto Multi Simulation
> Close; #Stock price
> mdf
> #dividend per share
> mdf_roi;
> #rate f
> return
> mdf_hdg;
> #dividend Browth rate
> IS Summary
> Period
> instinct_stock_value
> 0(1+8)/(k-8);
> alpha
> trade_when(P
> instinct_stock_Value
> rank(ts
> decay
> e/
> window(ts_delta(close,7 ),358) ),-1);
> Aggregate Data
> Sharpe
> LUTTI
> FITESs
> KETUFRS
> P3UCC
> Iarain
> Vector
> neut (alpha, close )
> 2,24
> 40,7296
> 1,09
> 9,669
> 6,359
> 4,749000
> Year
> Sharpe
> TUIIOeT
> Htness
> Returns
> Drawdown
> Narqin
> Count
> Short Cownt
> 2011
> 一,3
> 一-
> 11
> 315:1
> 33:
> 1
> 731
> 2012
> 43
> 3,741
> 141151
> 11193
> 1,100:
> 713
> 733
> 2013
> 33,35:
> 4,155
> 2021
> 1
> 3+
> 201-
> 31
> 3,331
> 3,14
> 3-593
> 330:
> 755
> 33
> 715
> 0,51
> -1,731
> 02
> 3
> 一2293
> +30:
> 744
> 775
> 2015
> 一,31:
> 0-3
> 4,945
> 6.351
> :
> 535
> 735
> 2017
> 一
> 072
> 5,334
> _
> 520
> 63
> 733
> 713
> 1,51
> -1,253
> 5
> 5,2151
> 33
> 530:
> 535
> 742
> 2019
> 705
> 41,0495
> 036
> 7,255
> 25291
> 5
> 75
> 762
> 7020
> 355
> -2,373
> 325
> 3,4351
> 25393
> 50:
> 77
> 771
> 7021
> 41,4295
> 03-
> 4551
> 22193
> 1,450:
> 715
> 733
> 医 Correlation
> Qone this Alphaina neW tab
> Self Correlation
> HiEhes: Correlation
> L+ RIn:
> Example
> Simwlate
> Visualization
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> div;
> Long



> [!NOTE] [图片 OCR 识别内容]
> Simulation 6
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DI/ILLIQUID
> MINVOLIN
> Convert to Multi-Simulation
> N Chart
> Pnl
> UANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> OOO
> REGION
> UNIVERSE
> DELAY
> Iose,7 ),358)),-1);
> USA
> ILUIQUID_MINVOLIM
> OOO
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 7.0OOK
> Subindustry
> 0,06
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> OOO
> On
> Verify
> Off
> 5,0OOK
> Apply
> SaVe as Default
> LOOO
> 3,00OK
> Z.OOO
> OOO
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> Qone tis Nlphaina new tab
> Example
> Simwlate
> Visualization
> udd Aphato
> List
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha


结果表明该模型在10年回测中有效


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Turnover
> 70
> 60
> 5095
> 405
> 30-
> 209
> 2012
> 2013
> 201
> 2015
> 201
> 2017
> 2013
> 2019
> 2020
> 2021


但营业额波动较大（40%），如何改善？

实验表明，更改为顾问专用的数据字段将有助于减少 prod corr，但我不会在本文中提及它，因为该文章将发布到中国顾问论坛，并且因为我是其他国家的顾问，所以我可以'别看它。 我希望中国的咨询论坛能够开放给其他国家的咨询师参与、观看和贡献。 我非常钦佩中国论坛的活动，并期待向您了解更多。

---

### 帖子 #16: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **讨论数**: 37


> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN]([Commented] 【插件】Genius Rank分析代码优化_29496672188951.md) 
             Github插件地址： [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 安装插件
> .访问插件 GitHub 地址: https
> //github. com /zhangkaihua88 / WebDataScope
> 能访问Gitlub的请跳过这红色部分
> 0)如果访问不了 github.
> COm
> 换一个浏览器试试,
> 有几率解决 ,
> 如果不行 ,
> 请按照以下步骤操作。
> 〈 〉 C 命 ^ 众
> 0
> [链接已屏蔽] MebDataScope
> 器
> 无法访问此网站
> 连接已重置。
> 请试试以下办法:
> 检查网络连接
> 检查代理服务器和防火墙
> 运行 Windows 网络诊断
> ERR_CONNECTION_RESET
> 重新加载
> 详情
> 1)同时按住 [Window
> Or
> Start ]
> + R, 输入 cmd 打开命令提示符,
> 然后输入 pin
> 吕
> github.com
> 如果 ping 不通,表现为
> ping
> 不是内部或外部命令,
> 也不是可运行的程序
  
> [!NOTE] [图片 OCR 识别内容]
> 或批处理文件=
> 建议将此错误扔给
> AI
> 解决,多半是环境娈量 问题)
> 得到并复制 gith
> ub 的 ip 地址.
> C:IWINDOWSIsystem3zlcmd.
> X
> Microsoft Windows
> [版本
> 10.0.26100.6584]
> Cc)
> Microsoft
> Corporation。
> 保留所有权利
> 0
> C: |Users
> Dping github
> C0I
> 正在
> Pinq
> qithub
> C0I
> 23
> 205.243.166]  具有
> 32  字节的数据:
> 20.205
> 243.166
> 复:  字节=32
> 时间=75ms
> TTL=I03
> 20.205
> 243
> 166
> 的
> 复:  字节=32  时间=75ms
> TTL=I03
> 黧
> 20.205.243.166  的
> 复:  字节=32  时间 =75ms
> TTL=I03
> 20.205.243.166  的
> 复:  字节=32  时间=75ms
> TTL=I03
> 20.205.243.166  的 Ping 统计信息 :
> 数据包:  已发送
> 二  4,
> 已接收 =4,
> 丢失
> 二
> 0
> (0%  丢失 ),
> 往返行程的估计时间 (以毫秒为单位 ):
> 最短
> 二
> T5mS,
> 最长
> 二
> T5mS,
> 平均
> 二
> T5ms
> 2)  复制 ip 地址。在服务器  搜索栏  输入 C: WWindows |System3z Idrivers letc Ihost
> 5 ,
> 打开方式选择  记事本 ,然后马上关闭记事本。接着在  搜索栏  搜索  记事本 并 右击
> 选择以管理员身份运行 ,随即将 github.com 的 ip 地址粘贴在最后.
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1 `
> :三 `
> 8 工 O  a
> # Copyright (c) 1993-2009 Microsoft
> #
> # This is asample HOSTS file used by Microsoft TCPIIP for Windows。
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept onan individual line. The IP address should
> # be placed in the first column followed by the corresponding host name:
> # The IP address and the host name should be separated by at least one
> # space。
> #
> # Additionally, comments (such as these) may be inserted on individual
> # lines O[
> following the machine name denoted by a '#' symbol。
> #
> # Forexample:
> #
> 102.54.94.97
> rhino.acme.com
> # SOUrCe Serer
> 38.25.63.10
> Xacme.com
> # X client host
> # localhost name resolution is handled within DNS itself
> #
> 127.0.0.1
> localhost
> #
> 门
> localhost
> 20.205.243.166
> 行10,列2
> 818个亨符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-8
> 3)
> 点击记事本左上角的 文件 然后选择  保存  即可。切记记得看记事本上面是
> 而不是 O 才算保存成功。
> Corp:
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1
> :三 `
> 8 工 O g
> # Copyright (c) 1993-2009 Microsoft Corp.
> #
> # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept on an individual line. The IP address should
> # be placed in the first column followed by the corresponding host name。
> # The IP address and the host name should be separated by at least one
> # space:
> #
> # Additionally comments (such as these) may be inserted on individual
> # lines Or following the machine name denoted by a '#' symbol。
> #
> # For example:
> #
> 102.54.94.97
> rhino.acme.com
> SOUrCe Serer
> 38.25.63.10
> X.acme.com
> client host
> # localhost name resolution is handled within DNS itself。
> #
> 127.0.0.1
> localhost
> Iocalhost
> 20.205.243.166
> 行22,列15
> 818个字符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-S
> 4)  在 搜索栏  搜索
> cmd 并 右击选择以管理员身份运行 ,在  命令提示符  面板上键入 ip
> config/flushdns
> 返回
> 己成功刷新DN5解析缓存  便表示成功了.
> C
> 管理员: 命令提示符
> 义
> Uicrosoft Nindows [版不 10.0.26100.6584]
> (C)
> Iicrosoft Corporation。 保留所有权利。
> C: |Iindows |System32>ipconfig / flushdns
> Iindows
> IP 配置
> 己成功刷新 DVS 解析缓存。
> C: {Tindows |System32>
> # X
  
> [!NOTE] [图片 OCR 识别内容]
> 5)
> 访问华子哥的 Bithub 地址 https: //github_
> COm
> zhangkaihua88 /WebDatascope
> 成功.
> 囟 M。『图』 &
> WorldQuant BRAIN
> GitHub
> ZhangkalhuaBBNe
> C
> https /Igithubcom/zhangkaihuagg NebDatascope
> C 囤  &
> 8 &
> 器 ^4  泊
> 器
> Platform
> Solutions
> Resources
> Open Source
> Enterprise
> Search Orjump to.。
> Signin
> Sign up
> Zhangkaihua88 / WebDataScope
> Public
> Notifications
> Fork
> Stal
> Code
> SSUeS
> Pullrequests
> Actions
> Projects
> Security
> Insights
> main
> Branches
> GOto fle
> Code
> About
> No description website
> Ortopics provided。
> Zhangkaihuagg fix
> 0183285
> 2Weeks a90
> 118 Commits
> Readme
> Delete img/screenshotpng
> last year
> Apache 2.0license
> Activity
> SIC
> Weeks ago
> 69 stars
>  gitignore
> V0.4.3
> last year
> watching
> LICENSE
> VO.1.0
> last year
> 14 forks
> Report repository
> READMEmd
> 2 months ago
> manifestjson
> Weeks ago
> Releases
> responsejson
> Weeks ago
> WebDataScope 0.9.3 Release
> Lalest
> onIunT4
> 16 releases
> README
> Apache- 2 0 license
> Packages
> 以上为不能访问Gitlub解决方法
> 2
> 点击绿色
> Code 弹出
> Download
> ZIP
> 下载插件压缩包. Zip文件,
> 或者使用 &
> i
> 克隆 git
> clone https: //github.com/zhangkaihua88 / WebDataScope . git
> 将压缩包保
> 存在某目录下,比如我保存在
> 0:
> worldquant_plugin 目录下
> 确认下载
> About
> 链接:
> hub.comlzhangkaihuaggMebDataScopelziplrefs/heads/main
> No description, website; or topics provided。
> 文件名:
> WebDatascope-mainzip
> 394KB
> 0
> Readme
> 保存到:
> 0: {worldquant_plugin
> Apache- 2.0 license
> A
> Activity
> 打开
> 保存
> 取消
> 69 stars
> watching
> V0.1.0
> Open with GitHub Desktop
> 9
> 14 forks
> Download ZIP
> Report repository
> UP
> 3
> 使用解压软件将压缩包解压到(默认)当前目录下.
> Pricing
> Tags
> img
  
> [!NOTE] [图片 OCR 识别内容]
> Worldquant_plugin
> 此电脑
> 新加眷 (D:)
> worldquant_plugin
> 在 worldquant_plugin 中搜索
> 新逮
> 排序
> 三  苎看
> 全部解压宿
> 详洇信息
> 名祢
> 修改曰期
> 大小
> 主文仵夹
> WebDataScope-main
> 2025/9/1218:13
> 压宿(pped)文件。
> 394 KB
> 图库
> 捉敢压缩(Zipped]文件夹
> 选择
> 个目标并提取文件
> 文裆
> 文件将被捉致到这个文件夹(F:
> 囱片
> Dilworldquant_plugin WebDataScope main
> 浏览(R)
> 音乐
> 完戎时显示捉敢的文件(H)
> 视频
> 此电脑
> 本地硭岛 (C:)
> 新加卷(0:)
> 捉取(
> 职消
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 个项目
> 逆中
> 个目
> 393 KB
> 在浏览器中打开扩展管理页面,
> 网页键入 chrome:
> /extensions
> (如
> chrome: //extensions
> 八.
> WorldQuant BRAIN
> 扩展程序
> Cent BroWseT
> chrome /extensions
> 器 |#
> 省
> 器
> quant
> 节点
> MP3袼式
> 显化群每曰总若
> 常用网
> 扩展程序
> 搜索扩展程序
> 开发者摸式
> 我。}展穆序
> 键盘快捷键
> 在 CentBrowser 应田酋店中查找扩展程序和主题背景
> 在 Cent Browser 应jd店中
> 发现更多扩展程序和主题
> 5
> 开启
> 开发者模式》
> 点击 <加载己解压的扩展程序》
> 选择插件文件
> 夹。成功会显示  扩展加载完毕
> edge:
  
> [!NOTE] [图片 OCR 识别内容]
> 选择扩展程序目录
> worldquant_Pl
> WebDatascope main
> WebDatascope-main
> 器
> #
> 阎
> c识
> 新逮文件夹
> 名称
> 佟改曰期
> 开发者摸式
> 此电脑
> WebDataScope-main
> 2025/9/1218.27
> 文件夹
> 本地磁盘 (C:)
> 新加巷 (0;)
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 围l店中查找扩展程序和主题背景
> 文件夹:
> WebDatascope-main
> 迸文4夫
> 驭消
> 2
> 使用插件功能
> 打开 Genius 页面
> 安装完成后 ,打开 WorldQuantBrain 网页 Genius 页面 https : /Iplatform.worl
> dquantbrain.com/genius /
> (安装完成后第一次打开需要刷新页面等待若干(少许)时
> 间才能加载出插件)
> @
> 匕
> https:/Iplatform worldquantbrain com/genius/
> C 囤  众
> 8Q
> 器 ^4  省
> 器 ^8 quant
> U  节点
> MP3袼式
> 昱化群l日总结
> 常用网址
> WORLDOUANT
> BRANI
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> 恩 Competitions (5)
> Community
> Status
> Leaderboard
> FAQ
> Gsnlus
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析 
> 显示排名列表
> Genius level: Gold
> Best level: Gold
> Current quarter end: September 3oth; 2025
> SOLD
> 页面加载后,你会看到  配置插件
> 运算符分析
> 显示运算符分析  和「排名分析」
> 和「显示排名分析」以及「显示排名列表」六个按钮
> 依次点击  配置插件
> 运算符分析
> 显示运算符分析
> 配置插件  点击的作用是啥我不是很清楚,
> 这个得问华子哥才知道。点击  运算符
> 分析  按钮后插件会开始抓取你本季度交付的 alpha 全部操作符数量和使用数据 (按
> 钮上会显示抓取进度) ,抓取完成后,
> 点击显示运算符分析 ,会在页面最下方会生
> 成关于操作符的分析表格。右上角显示过去和美区分析 (何时分析)时间.会展示你
  
> [!NOTE] [图片 OCR 识别内容]
> 本赛季所有的操作符和数量以及使用情况.
> 命
> https: / /platform worldquantbrain comlgenius/
> C 困 &
> 8 ^Q  器 ^4
> 器 ^8 quant
> U  节 
> MP3格式
> 量化群每曰总结
> `用网址
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统
> 为substrac
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符末被使用。
> '有两种含义分别是substract和revers, 此处统一
> 为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x; Y, filter
> false), X -y
> 52
> COMBOREGULARSELECTION
> base
> Arithmetic
> multiply(xyy
> filter-false); *
> 76
> COMBO,REGULAR SELECTION
> base
> 依次点击「排名分析」和「显示排名分析」以及「显示排名列表」
> 点击「排名分析」需要等待0.5 ~ 1min 左右 ,
> 需要计算排名情况, 计算完成
> 后点击「显示排名分析」 ,就可以看见比较多的信息,
> 包括但不限于顾问的总人
> 数,以及目前 genius 不同级别达标分别有多少人和自己目前的等级 ,
> 以及自己的
> 最终定级大概会在什么等级 ,
> 以及自己的六维数据。
> q
> 匕
> https:/Iplatform worldquantbraincom /genius/
> C 囤 。 令
> 凸 /Q 器 』4  省 :
> 器 ^8 quant
> 节忘
> MP3袼式
> 导化拜#曰总结
> 常用网址
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207:22:18北京时间: 2025/9/1219:22;18
> 我的排名信息
> 美东时间:2025/9/1207:22:18 北京时间:2025/9/1219:22.18
> 总人敛{9104
> 可能的基璀人数:2926 人
> (交够40个)
> 各个Level 满足的人数 /最终的人:
> For Expert;(512/ 585
> For Master: 4131234
> ForGranamaster
> 该用户目前满足的级别
> grandmaster
> 绢辑六维指标
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:87
> 585
> 总排名:91
> 234
> 总排名:34
> Operator Count: 307 名
> Operator Count: 200 名
> Operator Count: 39 名
> Operator
> 141名
> Operator
> 44名
> Operator AVg: 7名
> Field Count; 263 名
> Field Count; 152 名
> Field Count; 36 名
> Field
> 112名
> Field
> 30名
> Field
> 7名
> Community Activity: 252名
> Community Actiity: 142 名
> Community Activity: 27 名
> Completed Referrals: 1 名
> Completed Referrals:
> Completed Referrals: 1 名
> Max Simulation Streak: 903 名
> Max Simulation Streak: 338名
> Max Simulation Streak: 45 名
> Total Rank: 1979名
> Total Rank: 907 名
> TotalRank: 162 名
> 同时还有贴心的可以 编辑六维数据  按钮,这个功能非常还好,
> 可以让你知道自
> 己目前所处的级别到达是差在哪里,怎么去弥补自己的差分点.非常 nice!
> 点击「显示排名列表」可以多维度查看和分析所有顾问的某些数据,
> 想比对
> 想查看哪位大佬的数据都可以查看,同时支持多维度过滤筛选.
> AVB;
> AVg:
> Avg:
> Ave:
> Avg:
  
> [!NOTE] [图片 OCR 识别内容]
> https:/ /platform worldquantbrain com/genius /leaderboard
> C 囤
> 8Q
> 器 ^^4
> ^
> 器 ^9 quant
> 节点
> 1P3恪式
> 呈化群每曰总结
> 穷用网址
> Genius Rank List
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> 排名信息
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> Minimum 排名:
> Maximum 排名
> entries per page
> Search:
> 下荭原始J5JN
> 显示隐蒉列
> 排名
> 用FID
> 达成等级
> 最终等级
> 国家1区
> K279256
> grandmaster
> grandmaster
> CN
> J71699
> grandmaster
> grandmaster
> FL39657
> grandmaster
> grandmaster
> CN
> 064461
> grandmaster
> grandmaster
> VN
> YN82626
> grandmaster
> grandmaster
> TW
> PP87148
> grandmaster
> grandmaster
> IN
> AT56452
> grandmaster
> grandmaster
> RP76828
> grandmaster
> grandmaster
> CN
> F069320
> grandmaster
> grandmaster
> CN
> 2H78994
> grandmaster
> grandmaster
> T
> Showing
> TO 10of 5,116 entries
> 512
> 查看他人排名数据
> 华子哥的插件还有非常贴心的功能,就是可以查看别人的排名,
> 比如:  华子
> 哥
> K279256
> 课代表 XX
> 游戏王
> ZS(CL ) [ZSC]59763  和常州MG
> 顾问 MG88592 (Rank 38)
> 大佬等等.
> WORLDOUANT
> B人I
> Simulate
> 6Alphas
> Learn
> Data
> Labs
> Genius
> @ Competitions (5)
> Community
> 号
> Refer
> friend
> StatUs
> Leaderboard
> FAQ
> Genius
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207;22:18 北京时间:2025/9/1219:22:18
> 我的排名信息
> 美东时问:  2025/9/1207.22:18北京时问:2025/9/1219:22:18
> 总人数:9104人
> 可能的基准人数:2926  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 1512
> 585
> FOr Master: 413
> 234
> For Grandmaster: 47/59
> 点击
> Leaderboard
> 将鼠标放置在某大佬的 ID 上,
> 便可查看六维排名和
> Geniu
> s等级。
  
> [!NOTE] [图片 OCR 识别内容]
> https:/platform worldquantbrain com /genius/leaderboard
> 出  ^
> {|仑
> JIIVIIOIIOC
> IIUIIOICC
> 386
> 顾问 ML47973 (Rank 100) (Mej
> Gold
> Gold
> 266
> 2.39
> 1.79
> 0.00
> 3.41
> [792
> 167
> 2.70
> RP76828 排名信息
> AK40g
> 总人数:9067人
> 6.17
> 可能的基准人数:2921人 (交够40个)
> HI3900
> 5,38
> 各个Level 满足的人数
> 最终的人数:
> RP768;
> 2.81
> For Expert: 1508
> 584
> YH250;
> For Master: 410
> 234
> 105
> 5.83
> ForGrandmaster: 45
> 58
> P11976
> 5,82
> 该用户目前满足的级别: Srandmaster
> LV571
> 编辑六维指标
> CM456
> 6.91
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> TV5921
> 8.26
> 总排名:4
> 584
> 总排名:4/234
> 总排名:7/58
> LV598
> 4.70
> Operator Count: 35 名
> Operator Count: 34 名
> Operator Count: 15 名
> DVGAAI
> Operator AVg: 64名
> Operator AVg: 17名
> Operator AVg: 4 名
> 3,73
> Field Count: 283名
> Field Count: 160 名
> Field Count: 35 名
> 儿7169
> Field AVg: 33名
> Field AVg: 7 名
> Field
> 名
> 100
> 3.58
> Community Activity: 96 名
> Community Activity: 71 名
> Community Activity: 20名
> EYg42
> Completed Referrals:
> Completed Referrals:
> 名
> Completed Referrals:
> 名
> 6.15
> Max Simulation Streak:
> Max Simulation Streak:
> Max Simulation Streak: 33
> 501 名
> 222名
> ID51
> 5,91
> Total Rank; 1013 名
> Total Rank: 512名
> Total Rank; 109 名
> 56764
> 116
> 7.35
> AN154671
> Expert
> Expert
> 366
> 0.48
> 0.12
> 0.21
> 6.47
> https;lIplatform worldquantbrain comprofle/public/RP76823
> Master
> Master
> 365
> 0,79
> 0.89
> 0,91
> 8,61
> 致谢
> 再次感谢华子哥和贡献者们的无私分享 !这个工具极大方便了排名分析,同
> 时在前端的颜色。样式和大小展示方面也贴合美观设,
> 无论是自我提升还是学习
> 他人策略都非常有用。建议大家试用并反馈 ,
> 共同完善插件 !
> AVE:


---

### 帖子 #17: 【0基础手搓alpha】介绍一种手搓alpha摆脱模版束缚的方法（含有overfit风险）
- **主帖链接**: 【0基础手搓alpha】介绍一种手搓alpha摆脱模版束缚的方法含有overfit风险.md
- **讨论数**: 7

提交了很多machine alpha，有一天心血来潮，想手搓一个，但是没有idea，就随便写一个最简单的想法吧idea： 买收益率高的股票（纯瞎想的，没参考任何材料文献）先确定setting，由于本人比较懒，啥也没改，直接USA top3000 其他没动（至于为什么，也是有原因的，本人在IQC2024 mainland China final上说过，如果你尝试把中性化设置为none，你就会发现USA基本上怎么买都不会亏，你写个1都是大好走势，虽然最近不太行，但是也很不错了）下图为USA setting none 其余默认 alpha表达式为1看到这个走势是不是很想做alpha呢？初步想法ts_rank(returns,time)随便写一个时间窗口，发现效果还是很不错的很奇怪，为什么会是负的曲线，如果有大佬读到这篇文章，希望不吝赐教然后加一些过滤符，手动@ATOM2024 1st TL87739，感谢大佬的不吝赐教直接加上trade_when(group_count(alpha,market)>count,alpha,0)这个运算符很好避免了Weight concentration报错情况，之前经常遇到，感谢大佬可以将我救赎（如果你也有和我一样的困惑，可以尝试一下这个运算符）得到下面这根曲线，已经很不错了，但是turnover比较高，fitness也比较低接下来就是最喜欢的微调环节（又叫overfit环节）众所周知，turnover高了可以使用trade_when操作符降低，大家可以加入自己喜欢的条件（萝卜青菜各有所爱），当然我也在2024IQC mainland China final上介绍过其他类似的操作符，如if_else,left_tail等运算符。经过一顿操作，alpha已经只差fitness了，这下又要@研究小组里的大佬了，直接上group运算符，使用pv13（别问为什么，问就是大佬甄选），然后这个alpha的fitness得到了明显改善，但是还差一点，由于本人比较偷懒，不想再加运算符了，直接加了一个之前submit过的高fitness的alpha让他两综合，就到了可以提交的标准prod也是很低的一个alpha，幸福感又提升了一点捏，毕竟全程也只用了returns一个dataset虽然表现一般般，但是这个alpha是本人第一个手搓的alpha，还是比较有成就感的。大家应该也会有一样的想法，虽然手搓困难，但是当你能做出来，就是要比纯machine要开心一点，希望大家多多尝试（不需要你有太多知识储备，只要你敢尝试就能做出来，就像我的idea是多么普通，但是prod却很低）

---

### 帖子 #18: 【0基础手搓alpha】介绍一种手搓alpha摆脱模版束缚的方法（含有overfit风险）
- **主帖链接**: https://support.worldquantbrain.com【0基础手搓alpha】介绍一种手搓alpha摆脱模版束缚的方法含有overfit风险_28328131324823.md
- **讨论数**: 7

提交了很多machine alpha，有一天心血来潮，想手搓一个，但是没有idea，就随便写一个最简单的想法吧

***idea： 买收益率高的股票（纯瞎想的，没参考任何材料文献）***

先确定setting，由于本人比较懒，啥也没改，直接USA top3000 其他没动

（至于为什么，也是有原因的，本人在IQC2024 mainland China final上说过，如果你尝试把中性化设置为none，你就会发现USA基本上怎么买都不会亏，你写个1都是大好走势，虽然最近不太行，但是也很不错了）

下图为USA setting none 其余默认 alpha表达式为1


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> ZSN
> ZONI
> TSN
> TONI
> 00JK
> Jul"13
> J1"14
> Jul'15
> J1'15
> JUl17
> Jl'13
> Jul"19
> Jul20
> JUl21
> NNN


***看到这个走势是不是很想做alpha呢？***

初步想法ts_rank(returns,time)随便写一个时间窗口，发现效果还是很不错的

很奇怪，为什么会是负的曲线，如果有大佬读到这篇文章，希望不吝赐教


> [!NOTE] [图片 OCR 识别内容]
> ZOOOK
> OOOK
> ~6OOOK
> BOOOK
> ~1ON


然后加一些过滤符，手动@ATOM2024 1st TL87739，感谢大佬的不吝赐教

直接加上

trade_when(group_count(alpha,market)>count,alpha,0)

这个运算符很好避免了 [Weight concentration](/hc/en-us/articles/19248385997719)  报错情况，之前经常遇到，感谢大佬可以将我救赎（如果你也有和我一样的困惑，可以尝试一下这个运算符）

得到下面这根曲线，已经很不错了，但是turnover比较高，fitness也比较低


> [!NOTE] [图片 OCR 识别内容]
> OOOK
> OOOK
> OOOK
> OOOK
> Jul'13
> Jul1
> Jul15
> Jul '165
> Jul'17
> Jul '18
> Ju1'19
> Jul'20
> Jul'21


接下来就是最喜欢的微调环节（又叫overfit环节）

众所周知，turnover高了可以使用trade_when操作符降低，大家可以加入自己喜欢的条件（萝卜青菜各有所爱），当然我也在2024IQC mainland China final上介绍过其他类似的操作符，如if_else,left_tail等运算符。

经过一顿操作，alpha已经只差fitness了，这下又要@研究小组里的大佬了，直接上group运算符，使用pv13（别问为什么，问就是大佬甄选），然后这个alpha的fitness得到了明显改善，但是还差一点，由于本人比较偷懒，不想再加运算符了，直接加了一个之前submit过的高fitness的alpha让他两综合，就到了可以提交的标准


> [!NOTE] [图片 OCR 识别内容]
> 8 PASS
> STZrZE OT2.30
> above CUtofTof 1.58。
> Fitness Of 1.02
> aDOVE ~UOffof
> TmOVErOT 48.78%
> abOVe CUTOff af 1%.
> Tmowerof 48.78%
> bElow CUCOfrof 70%
> Weshtis Wz
> Jistrbued OVerinsrument。
> Sub-unierse Sharpe cf21
> EDOVE ~UTOff Of
> 15 IadJe
> Of 2.44i5 abowe Cutof Of 2.37 for ladder yEaT 3: 7/15/2022。
> 7116/2019.
> Tyramidthene USAIDIIPrice Volume Matches with multiplier 3f1.
> STTUE


prod也是很低的一个alpha，幸福感又提升了一点捏，毕竟全程也只用了returns一个dataset


> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> NaYITUT
> Hinimum
> L52 RUI: -
> Prod Correlatlon
> ItIMUM
> TNIIUN
> Last Run: Fri。 12/05/2024,10;27 Pl
> 0.5219
> -0.4158
> TOON
> 1OR
> 
> ~9
> 00
> 0,6


虽然表现一般般，但是这个alpha是本人第一个手搓的alpha，还是比较有成就感的。

大家应该也会有一样的想法，虽然手搓困难，但是当你能做出来，就是要比纯machine要开心一点，希望大家多多尝试（不需要你有太多知识储备，只要你敢尝试就能做出来，就像我的idea是多么普通，但是prod却很低）

---

### 帖子 #19: 【New】一键检验alpha稳定性V10.22代码优化
- **主帖链接**: 【New】一键检验alpha稳定性V1022代码优化.md
- **讨论数**: 17

一键检验alpha稳定性发布了五个月，得到了很多好评，作者为了进一步拓展稳定性检验功能，加入了可视化检验模块，最近发布了新版本。一键检验alpha稳定性一键稳定性检验V10.22新增功能：对一键稳定性检验加入支持一阶op模块，如在alpha前加入rank,sign等一阶操作符可滑动窗口查看pnl时间序列新增一键可视化检验输入需要alpha_id即可得到可视化检验本地画图可对所有region的alpha分sector查看pnl，Sharpe，及平均Sharpe可对非单一region的alpha分country查看pnl，Sharpe，及平均Sharpe优化部分：减少重登次数更新画图工具为plotly优化get_alpha函数优化post_alpha函数删除部分多余代码tips：可以和本地计算相关性结合使用可以获取pnl做更深入研究下载链接：[链接已屏蔽]部分图像如下所示

---

### 帖子 #20: 【New】一键检验alpha稳定性V10.22代码优化
- **主帖链接**: https://support.worldquantbrain.com【New】一键检验alpha稳定性V1022代码优化_35797801981975.md
- **讨论数**: 17

一键检验alpha稳定性发布了五个月，得到了很多好评，作者为了进一步拓展稳定性检验功能，加入了可视化检验模块，最近发布了新版本。

- [一键检验alpha稳定性](一键检验alpha稳定性代码优化_32008506789655.md?input_string=%E4%B8%80%E9%94%AE%E6%A3%80%E9%AA%8Calpha%E7%A8%B3%E5%AE%9A%E6%80%A7V10.22)

一键稳定性检验V10.22

新增功能：

对一键稳定性检验加入支持一阶op模块，如在alpha前加入rank,sign等一阶操作符

可滑动窗口查看pnl时间序列

新增一键可视化检验

输入需要alpha_id即可得到可视化检验本地画图

可对所有region的alpha分sector查看pnl，Sharpe，及平均Sharpe

可对非单一region的alpha分country查看pnl，Sharpe，及平均Sharpe

优化部分：

减少重登次数

更新画图工具为plotly

优化get_alpha函数

优化post_alpha函数

删除部分多余代码

tips：

可以和本地计算相关性结合使用

可以获取pnl做更深入研究

下载链接：

[[链接已屏蔽])

部分图像如下所示 
> [!NOTE] [图片 OCR 识别内容]
> 多时间序列对比 (可交互缩放)
> 111
> 51
> nppgdpGa
> MPMI88n8
> 018WZAN2
> 3.51
> OmOkQQ3V
> npxkzkoa
> MPMIBII9
> 311
> NIXWjGrx
> 2r84Z9Y8
> 2.511
> OOOWMWRO
> 1.SN1
> 0.511
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
  
> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Sector ( 平均值:  0.38)
> 贷黍阈倬
> 0.74
> 0.5
> 0.55
> 0.52
> 0.52
> -均值: 0.38
> 0.38
> 0.38
> 0.23
> 0.21
> 0.2
> 』
> 0,01
> 风险闰值
> 类别
>  Cyclicals
> Industrial
> Financlal
> Diversitied
> Communications
> Nalerials
> Cyclicals
> Utilities
> Technology
> Energy
> Consumer
> Non-c
> Basic
> Consumer
  
> [!NOTE] [图片 OCR 识别内容]
> 行业Pnl 趋势 (可交互缩放)
> 111
> 51
> utilities
> Communications
> SOOK
> fnancial
> basicllaterials
> energy
> industrial
> 40Ok
> ConsumerNonCyclicals
> diversified
> ConsumerCyclicals
> 30O
> technology
> funds
> 忘
> ZOOk
> DO
> DO
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
  
> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Country
> Region (平均值: 0.21)
> 0.95
> 0.95
> 0.85
> 0.62
> 0.45
> 0.44
> 0.39
> -均值:
> 鬻
> -0,01
> -0.03
> -0.12
> 0.13
> 0.18
> -0.21
> -0.34
> 0.51
> 冈囝值
> 类别
> Switzerland
> Ireland
> Denmark
> Finland
> Belglum
>  Kingdom
> France
> AIrica
> Netherlands
> Ioly
> Portugal
> Sweden
> Austna
> Norway
> Spain
> Germany
> South
> Uned
  
> [!NOTE] [图片 OCR 识别内容]
> 国家/地区Pnl 趋势 (可交互缩放)
> 111
> 51
> 1.SN1
> 0.51
> 忘
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


---

### 帖子 #21: 【求助】刚入门的时候提交的一些质量很差的alpha，能删除之前提交的alpha吗？
- **主帖链接**: https://support.worldquantbrain.com【求助】刚入门的时候提交的一些质量很差的alpha能删除之前提交的alpha吗_23913899595671.md
- **讨论数**: 2



---

### 帖子 #22: 一键检验alpha稳定性代码优化
- **主帖链接**: 一键检验alpha稳定性代码优化.md
- **讨论数**: 36

很多顾问提交的alpha都是machine alpha，就会遇到一个问题，如何检验稳定性，通过常规方法就是改变neutralization和decay观察信号是否有明显的变化，于是我就有下面的思路，原理是我输一个id，get了alpha的信息，修改alpha setting，就自动发送命令，然后抢线发送，然后顺着发送的链接，get到alphaid再爬回来稳定性检验alpha的数据及pnl，之后本地绘制pnl并且绘制表格，给出对比只需要输入想进行稳定性分析的alphaid，就能得到下面的图像，具体的稳定性测试方法可以在代码中进行修改。具体代码我已经开源到研究小组，有需要可自取[链接已屏蔽]下图为示例，并且会有跟随的alpha表格（具体未展示）

---

### 帖子 #23: 一键检验alpha稳定性代码优化
- **主帖链接**: https://support.worldquantbrain.com一键检验alpha稳定性代码优化_32008506789655.md
- **讨论数**: 30

很多顾问提交的alpha都是machine alpha，就会遇到一个问题，如何检验稳定性，通过常规方法就是改变neutralization和decay观察信号是否有明显的变化，于是我就有下面的思路，原理是我输一个id，get了alpha的信息，修改alpha setting，就自动发送命令，然后抢线发送，然后顺着发送的链接，get到alphaid再爬回来稳定性检验alpha的数据及pnl，之后本地绘制pnl并且绘制表格，给出对比

只需要输入想进行稳定性分析的alphaid，就能得到下面的图像，具体的稳定性测试方法可以在代码中进行修改。

具体代码我已经开源到研究小组，有需要可自取 [[链接已屏蔽])

下图为示例，并且会有跟随的alpha表格（具体未展示）


> [!NOTE] [图片 OCR 识别内容]
> 126
> 多时间序列邓比
> WO7qbpx
> PSLrOZWI
> 7YPqAd1
> VATnqMQ
> MGvlog6
> XTWMOII
> gaNqvlQ
> QORrm7r
> LKobeMe
> LKobq7m
> 日期
> rTa6QPI
> 2014
> 2015
> 2018
> 2019
> 2013
> 2016
> 2017
> 2020
> 2022
> 2023
> 2021


---

### 帖子 #24: 什么是超级alpha？作为顾问我一天提交了6个alpha，我得到的付费是取决于前四个的质量，还是6个alpha中质量最好的四个alpha呢？
- **主帖链接**: https://support.worldquantbrain.com什么是超级alpha作为顾问我一天提交了6个alpha我得到的付费是取决于前四个的质量还是6个alpha中质量最好的四个alpha呢_23914887019287.md
- **讨论数**: 1



---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《Achievement update- Master》的评论回复
- **帖子链接**: [Commented] Achievement update- Master.md
- **评论时间**: 1年前

非常感謝您與我們分享這么精彩的作品！您的文字不僅展現了您的才華，還提供了寶貴的見解與靈感。我真切地感受到您投入其中的時間與精力，為創作出這樣富有深意且貼心的內容。您在講故事方面顯然有著天賦，您的作品給我留下了深刻的印象。請繼續分享您的精彩創作，我已經開始期待您的下一篇作品了！再次感謝您的慷慨與專注。

---

### 探讨 #2: 关于《Achievement update- Master》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Achievement update- Master_29144812991639.md
- **评论时间**: 1年前

非常感謝您與我們分享這么精彩的作品！您的文字不僅展現了您的才華，還提供了寶貴的見解與靈感。我真切地感受到您投入其中的時間與精力，為創作出這樣富有深意且貼心的內容。您在講故事方面顯然有著天賦，您的作品給我留下了深刻的印象。請繼續分享您的精彩創作，我已經開始期待您的下一篇作品了！再次感謝您的慷慨與專注。

---

### 探讨 #3: 关于《Advise needed for Boosters》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Advise needed for Boosters_29286699135767.md
- **评论时间**: 1年前

Boost alpha performance by improving Sharpe and fitness. Keep turnover <20% and drawdowns <4%. Test boosters across datasets and market conditions for robustness and avoid overfitting. Focus on dynamic adjustments and  R/D >2 for sustainable results.

---

### 探讨 #4: 关于《Advise needed for Boosters》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Advise needed for Boosters_29286699135767.md
- **评论时间**: 1年前

增強器（Boosters）通過提升信號品質和適應市場環境來提高Alpha表現。重點改進夏普比率、損益趨勢、適應度並減少回撤。在不同數據集、地區和市場環境中測試增強器，確保其一致性。使用排名（rank）、時間序列排名（ts_rank）、分組均值（group_mean）、中性化（neutralize）和時間序列相關性（ts_corr）等操作符來穩定和精煉Alpha。始終進行實驗並客觀評估影響！

---

### 探讨 #5: 关于《Dataset Deepdives - Option23 (Option Implied Volatility and Greeks)被推荐的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Dataset Deepdives - Option23 Option Implied Volatility and Greeks被推荐的_27569589603863.md
- **评论时间**: 1年前

感謝您對“Options23”數據集的精彩介紹，這篇文章不僅清晰地拆解了數據結構，還突出了其在Alpha生成中的巨大潛力。您對實值、虛值水平的解釋，以及對數據來源和衍生指標（如加權平均隱含波動率和期權希臘值）的闡述非常透徹。尤其是圍繞隱含波動率變化和波動率偏斜的Alpha示例，為探索交易策略提供了絕佳的起點。

對於剛接觸這個數據集的研究者來說，您強調在不同數據來源之間保持一致性以實現公平比較，這一點至關重要。文章在引導讀者如何高效地梳理如此龐大的數據集並激發結構化假設生成方面，表現得非常出色。

---

### 探讨 #6: 关于《Dataset DeepdivesResearch》的评论回复
- **帖子链接**: [Commented] Dataset DeepdivesResearch.md
- **评论时间**: 1年前

### 管理Alpha的推荐方法

- **数据预处理** ：对于不完整或稀疏数据，可通过填补缺失值（如均值填补、插值）或数据平滑（如移动平均）来增强数据质量。
- **模型选择** ：优先选择对稀疏数据鲁棒性强的模型，如随机森林或XGBoost。
- **特征工程** ：利用自动相关决定（ARD）先验等方法实现特征选择，减少噪声。
- **回测与验证** ：通过严格的交叉验证评估Alpha的可靠性。

### 自定义群组和nest资料的技巧

- **群组管理** ：在Nest框架中，可以通过定义模型和关系来管理群组。例如，创建聊天室表和用户表，通过关联实现群组功能。
- **数据结构优化** ：利用Nest的模块化特性，将数据分层管理，便于扩展和维护。

---

### 探讨 #7: 关于《Dataset DeepdivesResearch》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Dataset DeepdivesResearch_27405599813399.md
- **评论时间**: 1年前

### 管理Alpha的推荐方法

- **数据预处理** ：对于不完整或稀疏数据，可通过填补缺失值（如均值填补、插值）或数据平滑（如移动平均）来增强数据质量。
- **模型选择** ：优先选择对稀疏数据鲁棒性强的模型，如随机森林或XGBoost。
- **特征工程** ：利用自动相关决定（ARD）先验等方法实现特征选择，减少噪声。
- **回测与验证** ：通过严格的交叉验证评估Alpha的可靠性。

### 自定义群组和nest资料的技巧

- **群组管理** ：在Nest框架中，可以通过定义模型和关系来管理群组。例如，创建聊天室表和用户表，通过关联实现群组功能。
- **数据结构优化** ：利用Nest的模块化特性，将数据分层管理，便于扩展和维护。

---

### 探讨 #8: 关于《From Data to Trade: A Machine Learning Approach to Quantitative Trading》的评论回复
- **帖子链接**: [Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading.md
- **评论时间**: 1年前

Hey, that's quite an interesting paper. It's great that it efficiently deals with common alpha features and explores various ways for extraction and normalization. Co-authored by ChatGPT makes it even more worth checking out. I'll surely go through the link provided to dig deeper into those diverse methods they've explored. Looking forward to seeing how it can inspire our factor building and strategy design here.

---

### 探讨 #9: 关于《From Data to Trade: A Machine Learning Approach to Quantitative Trading》的评论回复
- **帖子链接**: [Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading.md
- **评论时间**: 1年前

Hey, that sounds really interesting, folks! The paper seems to have a good approach in dealing with common alpha features. Exploring different ways to extract and normalize them is crucial indeed. By extracting effectively, we can dig out valuable signals for our quant strategies. And normalization helps to put everything on a comparable scale, making the factors more reliable. Kudos to the authors for this work. I'll surely check out the link to learn more details.

---

### 探讨 #10: 关于《From Data to Trade: A Machine Learning Approach to Quantitative Trading》的评论回复
- **帖子链接**: [Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading.md
- **评论时间**: 1年前

這篇研究論文是一個寶藏，深入探討了量化交易策略以及機器學習在增強Alpha生成中的角色。它對數據預處理、特徵工程以及先進的機器學習技術（如圖神經網絡和變壓器）的詳細關注尤其值得讚揚。論文中強調的實用應用，使其成為希望在金融市場中運用尖端方法的交易員的必讀之作。真是太棒了！

---

### 探讨 #11: 关于《From Data to Trade: A Machine Learning Approach to Quantitative Trading》的评论回复
- **帖子链接**: [Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading.md
- **评论时间**: 1年前

這篇研究對量化交易領域有著重要的貢獻。它深入探討了常見的Alpha特徵，並引入了新的提取和標準化方法，為提升交易策略提供了寶貴的見解。此外，研究還融入了機器學習技術，進一步凸顯了人工智能在現代金融進化中的重要作用。

---

### 探讨 #12: 关于《From Data to Trade: A Machine Learning Approach to Quantitative Trading》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading_25238140123799.md
- **评论时间**: 1年前

Hey, that's quite an interesting paper. It's great that it efficiently deals with common alpha features and explores various ways for extraction and normalization. Co-authored by ChatGPT makes it even more worth checking out. I'll surely go through the link provided to dig deeper into those diverse methods they've explored. Looking forward to seeing how it can inspire our factor building and strategy design here.

---

### 探讨 #13: 关于《From Data to Trade: A Machine Learning Approach to Quantitative Trading》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading_25238140123799.md
- **评论时间**: 1年前

Hey, that sounds really interesting, folks! The paper seems to have a good approach in dealing with common alpha features. Exploring different ways to extract and normalize them is crucial indeed. By extracting effectively, we can dig out valuable signals for our quant strategies. And normalization helps to put everything on a comparable scale, making the factors more reliable. Kudos to the authors for this work. I'll surely check out the link to learn more details.

---

### 探讨 #14: 关于《Genius Program Guide》的评论回复
- **帖子链接**: [Commented] Genius Program Guide.md
- **评论时间**: 1年前



---

### 探讨 #15: 关于《Genius Program Guide》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Genius Program Guide_28772081460503.md
- **评论时间**: 1年前



---

### 探讨 #16: 关于《Momentum in Prices and Volume of Trades》的评论回复
- **帖子链接**: [Commented] Momentum in Prices and Volume of Trades.md
- **评论时间**: 1年前

如果您的因子受到特定行业或板块表现的强烈影响，可能会引入不必要的风险暴露并增加相关性。对行业或板块相关的因子进行中性化处理，可以确保您的Alpha信号不受这些系统性因素的影响。例如，如果某一板块（如科技）表现突出，中性化处理可以确保您的信号在多个行业中仍然有效。

---

### 探讨 #17: 关于《Momentum in Prices and Volume of Trades》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Momentum in Prices and Volume of Trades_29301176116759.md
- **评论时间**: 1年前

如果您的因子受到特定行业或板块表现的强烈影响，可能会引入不必要的风险暴露并增加相关性。对行业或板块相关的因子进行中性化处理，可以确保您的Alpha信号不受这些系统性因素的影响。例如，如果某一板块（如科技）表现突出，中性化处理可以确保您的信号在多个行业中仍然有效。

---

### 探讨 #18: 关于《My Experience as a Consultant: Key Learnings》的评论回复
- **帖子链接**: [Commented] My Experience as a Consultant Key Learnings.md
- **评论时间**: 1年前

That's really an inspiring journey, mate! Your key learnings make a lot of sense. Following guidance indeed helps us avoid detours. And persistence is crucial in this field as there're always setbacks. Targeting niche datasets is a smart way to stand out. Building quantity first also gives us more room for improvement later. Continuous learning is what keeps us updated. Thanks for sharing these valuable experiences with us.

---

### 探讨 #19: 关于《My Experience as a Consultant: Key Learnings》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] My Experience as a Consultant Key Learnings_29169009990423.md
- **评论时间**: 1年前

That's really an inspiring journey, mate! Your key learnings make a lot of sense. Following guidance indeed helps us avoid detours. And persistence is crucial in this field as there're always setbacks. Targeting niche datasets is a smart way to stand out. Building quantity first also gives us more room for improvement later. Continuous learning is what keeps us updated. Thanks for sharing these valuable experiences with us.

---

### 探讨 #20: 关于《Recipe for Quantitative Trading with Machine Learning》的评论回复
- **帖子链接**: [Commented] Recipe for Quantitative Trading with Machine Learning.md
- **评论时间**: 1年前

Thank- you for sharing your research paper and link for Recipe for Quantitative Trading with Machine Learning and a neural network, designed to help with stock trading. It looks at financial data and uses advanced deep learning techniques (a type of artificial intelligence) to figure out patterns or signals that can predict whether the market will go up or down. In simple terms, it’s like teaching a machine to understand and make sense of stock market trends so it can give better advice on when to buy or sell.

---

### 探讨 #21: 关于《Recipe for Quantitative Trading with Machine Learning》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Recipe for Quantitative Trading with Machine Learning_25238156762135.md
- **评论时间**: 1年前

Thank- you for sharing your research paper and link for Recipe for Quantitative Trading with Machine Learning and a neural network, designed to help with stock trading. It looks at financial data and uses advanced deep learning techniques (a type of artificial intelligence) to figure out patterns or signals that can predict whether the market will go up or down. In simple terms, it’s like teaching a machine to understand and make sense of stock market trends so it can give better advice on when to buy or sell.

---

### 探讨 #22: 关于《4、 **减少生产相关性**》的评论回复
- **帖子链接**: [Commented] Reduce Production Correlations.md
- **评论时间**: 1 year ago

将多种资产类别（如股票、大宗商品、债券和货币）的信号纳入投资策略，可以降低对单一资产类别的过度依赖，从而分散风险。例如，结合大宗商品和股票的信号，能够捕捉不同的市场因素，降低相关性，实现更好的多样化。这种策略在不同市场环境下表现各异，但通常能在极端波动或危机时期提供一定的风险缓冲。

---

### 探讨 #23: 关于《4、 **减少生产相关性**》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Reduce Production Correlations_29301199149463.md
- **评论时间**: 1 year ago

将多种资产类别（如股票、大宗商品、债券和货币）的信号纳入投资策略，可以降低对单一资产类别的过度依赖，从而分散风险。例如，结合大宗商品和股票的信号，能够捕捉不同的市场因素，降低相关性，实现更好的多样化。这种策略在不同市场环境下表现各异，但通常能在极端波动或危机时期提供一定的风险缓冲。

---

### 探讨 #24: 关于《Reducing Drawdown and Enhancing Alpha Stability: Lessons from CHN Region》的评论回复
- **帖子链接**: [Commented] Reducing Drawdown and Enhancing Alpha Stability Lessons from CHN Region.md
- **评论时间**: 1年前

Hey, great analysis here, mate! I totally agree with your points. The strategies you mentioned for reducing drawdown and enhancing stability are really practical. Just wondering, when building those intelligent filters, what specific criteria do you usually use for defining low liquidity or high risk stocks exactly? Looking forward to your reply.

---

### 探讨 #25: 关于《Reducing Drawdown and Enhancing Alpha Stability: Lessons from CHN Region》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Reducing Drawdown and Enhancing Alpha Stability Lessons from CHN Region_29160143596951.md
- **评论时间**: 1年前

Hey, great analysis here, mate! I totally agree with your points. The strategies you mentioned for reducing drawdown and enhancing stability are really practical. Just wondering, when building those intelligent filters, what specific criteria do you usually use for defining low liquidity or high risk stocks exactly? Looking forward to your reply.

---

### 探讨 #26: 关于《Single Dataset Alphas》的评论回复
- **帖子链接**: [Commented] Single Dataset Alphas.md
- **评论时间**: 1年前

創建有效的單數據集Alpha需要深入了解數據集、應用創新的轉換方法並降低與現有Alpha的相關性。首先分析數據集的特徵和關係，然後應用移動平均、Z分數和時間序列分析等統計方法。中和行業或市值等偏見，並通過實驗參數來創建獨特的信號。專注於未充分利用的字段，並根據反饋持續迭代。結合這些策略，可以構建更具特色和有效的Alpha。

---

### 探讨 #27: 关于《Single Dataset Alphas》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Single Dataset Alphas_29159542563991.md
- **评论时间**: 1年前

創建有效的單數據集Alpha需要深入了解數據集、應用創新的轉換方法並降低與現有Alpha的相關性。首先分析數據集的特徵和關係，然後應用移動平均、Z分數和時間序列分析等統計方法。中和行業或市值等偏見，並通過實驗參數來創建獨特的信號。專注於未充分利用的字段，並根據反饋持續迭代。結合這些策略，可以構建更具特色和有效的Alpha。

---

### 探讨 #28: 关于《The 101 ways to measure portfolio performance.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] The 101 ways to measure portfolio performance_25238156125207.md
- **评论时间**: 1年前

感謝分享這篇關於投資組合業績評價方法分類的精彩論文！它詳細分類了101種評價方法，為從資產選擇、風險調整和市場時機等多個維度評價投資組合提供了寶貴框架。論文對這些方法的優缺點進行了討論，幫助讀者根據具體情境選擇最合適的評價指標，無論是學術研究還是實踐應用都非常有價值。這些方法還可以作為機器驅動研究中的有效適應度函數，提升金融模型的優化效果。這項工作對投資組合業績評價的貢獻非常顯著，非常感謝！

---

### 探讨 #29: 关于《The 101 ways to measure portfolio performance.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] The 101 ways to measure portfolio performance_25238156125207.md
- **评论时间**: 1年前

感謝分享這篇關於投資組合業績評價方法分類的精彩論文。它詳細分類了101種方法，為從資產選擇、風險調整和市場時機等多個維度評價投資組合提供了寶貴框架。論文對這些方法的優缺點進行了討論，有助於根據具體情境選擇最合適的評價指標，無論是學術研究還是實踐應用都非常有價值。這些方法還可以作為機器驅動研究中的有效適應度函數，提升金融模型的優化效果。這項工作對投資組合業績評價的貢獻非常顯著，非常感謝！

---

### 探讨 #30: 关于《The 101 ways to measure portfolio performance.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] The 101 ways to measure portfolio performance_25238156125207.md
- **评论时间**: 1年前

這篇論文對於希望提升投資組合評價技術的人來說，無疑是一個寶藏！將這些方法作為機器驅動研究中的適應度函數的想法非常有趣，也非常符合現代量化金融的實踐。我很期待探索這些多樣化的策略，並看看它們如何融入系統化的投資組合優化中。感謝您分享這么有見解的資源！

---

### 探讨 #31: 关于《Tips for Success in the High Capacity Alphas Competition被推荐的》的评论回复
- **帖子链接**: [Commented] Tips for Success in the High Capacity Alphas Competition被推荐的.md
- **评论时间**: 1年前

提升HCAC中Alpha得分的精彩見解！強調將換手率保持在10%以下並對齊夏普比率以實現最佳得分，非常有價值。得分公式的拆解凸顯了每個Alpha的貢獻重要性。技術如線性衰減（ts_decay_linear）和新引入的操作符，特別是換手率峰值操作符（ts_target_tvr_hump），提供了平衡換手率與業績的實用方案。關於在控制換手率同時管理風險中性化的建議也很有幫助。這些可操作的策略是希望在比賽中出類拔萃的參賽者的必讀內容，謝謝分享！

---

### 探讨 #32: 关于《Tips for Success in the High Capacity Alphas Competition被推荐的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Tips for Success in the High Capacity Alphas Competition被推荐的_29520890528151.md
- **评论时间**: 1年前

提升HCAC中Alpha得分的精彩見解！強調將換手率保持在10%以下並對齊夏普比率以實現最佳得分，非常有價值。得分公式的拆解凸顯了每個Alpha的貢獻重要性。技術如線性衰減（ts_decay_linear）和新引入的操作符，特別是換手率峰值操作符（ts_target_tvr_hump），提供了平衡換手率與業績的實用方案。關於在控制換手率同時管理風險中性化的建議也很有幫助。這些可操作的策略是希望在比賽中出類拔萃的參賽者的必讀內容，謝謝分享！

---

### 探讨 #33: 关于《Understanding the arithmetic Operator in Quantitative Finance》的评论回复
- **帖子链接**: [Commented] Understanding the arithmetic Operator in Quantitative Finance.md
- **评论时间**: 1年前

Arithmetic operators are vital in quantitative finance for calculating returns, managing risk, and optimizing portfolios. They include addition for aggregating assets, subtraction for price differences, multiplication for compounding effects, division for ratios, and exponentiation for compound growth. These operators are applied in returns calculation, portfolio metrics, options pricing, and risk management, enabling professionals to perform essential financial computations and analyze data effectively. Understanding their application is crucial for developing strategies that can navigate real-world market complexities.

复制再试一次分享

---

### 探讨 #34: 关于《Understanding the arithmetic Operator in Quantitative Finance》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Understanding the arithmetic Operator in Quantitative Finance_28729357984919.md
- **评论时间**: 1年前

Arithmetic operators are vital in quantitative finance for calculating returns, managing risk, and optimizing portfolios. They include addition for aggregating assets, subtraction for price differences, multiplication for compounding effects, division for ratios, and exponentiation for compound growth. These operators are applied in returns calculation, portfolio metrics, options pricing, and risk management, enabling professionals to perform essential financial computations and analyze data effectively. Understanding their application is crucial for developing strategies that can navigate real-world market complexities.

复制再试一次分享

---

### 探讨 #35: 关于《Using Genetic Algorithms to Find Technical Trading Rules: A Comment on Risk Adjustment》的评论回复
- **帖子链接**: [Commented] Using Genetic Algorithms to Find Technical Trading Rules A Comment on Risk Adjustment.md
- **评论时间**: 1年前

艾倫和卡爾賈萊寧（Allen and Karjalainen）在1999年的研究中，運用遺傳編程開發了針對標普500指數的交易規則，雖然顯示出一定的預測能力，但並未顯著超越買入並持有策略。這項研究進一步驗證了他們的發現，強調風險調整的重要性，並再次印證了市場效率理論。分析嚴謹且富有洞見，對評估交易策略及未來研究具有重要貢獻。

---

### 探讨 #36: 关于《Using Genetic Algorithms to Find Technical Trading Rules: A Comment on Risk Adjustment》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Using Genetic Algorithms to Find Technical Trading Rules A Comment on Risk Adjustment_25238156621975.md
- **评论时间**: 1年前

艾倫和卡爾賈萊寧（Allen and Karjalainen）在1999年的研究中，運用遺傳編程開發了針對標普500指數的交易規則，雖然顯示出一定的預測能力，但並未顯著超越買入並持有策略。這項研究進一步驗證了他們的發現，強調風險調整的重要性，並再次印證了市場效率理論。分析嚴謹且富有洞見，對評估交易策略及未來研究具有重要貢獻。

---

### 探讨 #37: 关于《Value factor & weight factor》的评论回复
- **帖子链接**: [Commented] Value factor  weight factor.md
- **评论时间**: 1年前

提升Alpha表現，專注於低相關性的Alpha是一個很好的策略。通過精煉Alpha信號來降低相關性，確保它們能獨立貢獻，從而增強組合的多樣化並提升風險調整後的回報。可以使用主成分分析（PCA）等技術來識別並剔除冗餘信號，同時進行深入的相關性分析，以保留最具獨特性和互補性的信號。這樣，Alpha信號能夠更有效地協同工作，從而實現更強的整體表現。

---

### 探讨 #38: 关于《Value factor & weight factor》的评论回复
- **帖子链接**: [Commented] Value factor  weight factor.md
- **评论时间**: 1年前

增加權重因子需要時間和持續努力，因為它高度依賴於高質量Alpha的選擇。為了提升權重，應優先創建具有高夏普比率、低換手率和多樣化信號覆蓋的Alpha。關注美國（USA）和全球（GLB）等數據豐富且選擇潛力大的區域，將提供更多機會。此外，確保Alpha在隱藏的樣本外（OS）期間表現良好，這對於長期權重提升至關重要。定期分析和優化策略，以保持競爭力和穩定性。

---

### 探讨 #39: 关于《Value factor & weight factor》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Value factor  weight factor_29270495128087.md
- **评论时间**: 1年前

提升Alpha表現，專注於低相關性的Alpha是一個很好的策略。通過精煉Alpha信號來降低相關性，確保它們能獨立貢獻，從而增強組合的多樣化並提升風險調整後的回報。可以使用主成分分析（PCA）等技術來識別並剔除冗餘信號，同時進行深入的相關性分析，以保留最具獨特性和互補性的信號。這樣，Alpha信號能夠更有效地協同工作，從而實現更強的整體表現。

---

### 探讨 #40: 关于《Value factor & weight factor》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Value factor  weight factor_29270495128087.md
- **评论时间**: 1年前

增加權重因子需要時間和持續努力，因為它高度依賴於高質量Alpha的選擇。為了提升權重，應優先創建具有高夏普比率、低換手率和多樣化信號覆蓋的Alpha。關注美國（USA）和全球（GLB）等數據豐富且選擇潛力大的區域，將提供更多機會。此外，確保Alpha在隱藏的樣本外（OS）期間表現良好，這對於長期權重提升至關重要。定期分析和優化策略，以保持競爭力和穩定性。

---

### 探讨 #41: 关于《Value factor and weight factor》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Value factor and weight factor_29159546910871.md
- **评论时间**: 1年前

價值因子的表現取決於半樣本外（Semi-OS）階段的表現。要提升Alpha，需要創建能夠捕捉市場動態的強勁信號，而不是過度擬合。而權重因子的更新則需要更長時間，因為它取決於Alpha是否被選中。從觀察來看，低相關性、低換手率且屬於全球（GLB）和美國（USA）等地區的Alpha更有可能被優先選中。

---

### 探讨 #42: 关于《[Alpha Improvement Needed] Buying in excessive fear and high volume》的评论回复
- **帖子链接**: [Commented] [Alpha Improvement Needed] Buying in excessive fear and high volume.md
- **评论时间**: 1年前

Certainly, here are concise suggestions to enhance your alpha strategy:

1. **Enhance Sentiment Analysis**: Integrate diverse sentiment indicators and use adaptive weighting based on predictive accuracy.

2. **Adaptive Weighting**: Implement dynamic weighting that responds to market conditions and recent performance.

3. **Volume-Price Dynamics**: Analyze relative volume changes and open interest for stronger price movement validation.

4. **Optimize Mean Reversion**: Fine-tune look-back periods and statistical methods for identifying mean reversion opportunities.

5. **Risk Management**: Introduce stop-loss and position sizing based on asset volatility and liquidity.

6. **Backtesting**: Perform extensive backtesting to find optimal parameter combinations and strategy refinements.

---

### 探讨 #43: 关于《[Alpha Improvement Needed] Buying in excessive fear and high volume》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [Alpha Improvement Needed] Buying in excessive fear and high volume_28720123103255.md
- **评论时间**: 1年前

Certainly, here are concise suggestions to enhance your alpha strategy:

1. **Enhance Sentiment Analysis**: Integrate diverse sentiment indicators and use adaptive weighting based on predictive accuracy.

2. **Adaptive Weighting**: Implement dynamic weighting that responds to market conditions and recent performance.

3. **Volume-Price Dynamics**: Analyze relative volume changes and open interest for stronger price movement validation.

4. **Optimize Mean Reversion**: Fine-tune look-back periods and statistical methods for identifying mean reversion opportunities.

5. **Risk Management**: Introduce stop-loss and position sizing based on asset volatility and liquidity.

6. **Backtesting**: Perform extensive backtesting to find optimal parameter combinations and strategy refinements.

---

### 探讨 #44: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: [Commented] 【插件】Genius Rank分析代码优化.md
- **评论时间**: 1年前

华子哥太强了。这个数据分析功能希望还有更加多的人可以分析，像是GLB就有很多的数据等待分析，希望能有更多的人加入到完善数据功能改进之中，同时也很惊讶于作者的能力，实在是太强了，有了排名可以直接看更加好分析自己的段位了，谢谢开发者

---

### 探讨 #45: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md
- **评论时间**: 1 year ago

华子哥太强了。这个数据分析功能希望还有更加多的人可以分析，像是GLB就有很多的数据等待分析，希望能有更多的人加入到完善数据功能改进之中，同时也很惊讶于作者的能力，实在是太强了，有了排名可以直接看更加好分析自己的段位了，谢谢开发者

---
