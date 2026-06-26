# 顾问 JY88060 (Rank 85) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 JY88060 (Rank 85) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: Research Paper 07: Relative Strength Strategies for InvestingPinned
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

### 帖子 #2: Research Paper 08: Good Volatility, Bad Volatility and the Cross-Section of Stock ReturnsPinned
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

### 帖子 #3: Research Paper 61: Anomalies in the China A-share Market
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper 61 Anomalies in the China A-share Market_17611091334295.md
- **讨论数**: 30

**Abstract:**

This paper sheds light on the similarities and differences with respect to the presence of anomalies in the China A-share market and other markets. To this end, we examine the existence of 32 anomalies in the China A-share market over the period 2000-2019. We find that value, risk, and trading anomalies carry over to China A-shares. Evidence for anomalies in the size, quality, and past return categories is substantially weaker, with the exception of a strong residual momentum and reversal effect. We document that most anomalies cannot be explained by industry composition, and are present among large, mid, and small capitalization stocks. We are the first to examine the existence of residual reversal, return seasonalities, and connected firm momentum for the China A-share market. We find strong out-of-sample evidence for the former two, but not the latter. Specific characteristics of the China A-share market, such as short-sale restrictions, the prevalence of state-owned enterprises, and the effect of stock market reforms, are examined in more detail. These features do not seem to be important drivers of our empirical findings.

Author : Maarten Jansen, Laurens Swinkels, Weili Zhou

Year : 2021

Link :  **[[链接已屏蔽])**

**Key ideas and Comments from WorldQuant:**

- Page 3 paragraph 2
- Page 4 paragraph 2
- Page 5 paragraph 2

**Term**

**Data field**

**Dataset**

Risk

fnd17_beta

**[Direct Fundamental Data]([链接已屏蔽])**

Residual momentum

oth545_chn_wolfe_nemo_v2_mpd

**[Other 545]([链接已屏蔽])**

Value momentum

mdl39_val_mo_industry_rank

**[Value momentum data]([链接已屏蔽])**

---

### 帖子 #4: Research paper 71: The Information Content of Option Demand
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

### 帖子 #5: Research Paper 72: Testing for Asset Price Bubbles using Options Data
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

### 帖子 #6: Research Paper: Factor Investing: Get Your Exposures Right!Pinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper Factor Investing Get Your Exposures RightPinned_15102958024087.md
- **讨论数**: 0

**Abstract:**

This paper is devoted to the question of optimal portfolio construction for equity factor investing. The first part of the paper focusses on how to make sure that a given equity portfolio has the targeted factor exposures, even before imposing any constraints. We show that such portfolios can be derived from mean-variance optimization using stock expected returns as inputs provided these are built in a robust way from information about the factors. We propose a framework to build those robust stock expected returns and show that the targeted factor exposures are retained by the portfolios both before and after applying realistic constraints, e.g. long-only. Other more simplistic approaches fail. In the second part of the paper we illustrate the application of the framework to a practical case where the objectives are, first, to decide about the risk budget allocation to factors in some pragmatic way; and second, to construct a long-only constrained portfolio that retains the targeted exposures to four factors from well-known asset pricing equity models, namely High-minus-Low (HML), Robust-minus-Weak (RMW), Conservative-minus-Aggressive (CMA) and Momentum (MOM).

Key ideas:

- Page 3 paragraph 1
- Page 23 paragraph 2

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

mean-variance optimization

mdl175_variance120

[Model175]([链接已屏蔽])

volatility

mdl175_realizedvolatility

[Model175]([链接已屏蔽])

stock return

anl14_high_roa_fp1

[Analyst14]([链接已屏蔽])

factor return

mdl175_revs10

[Model175]([链接已屏蔽])

Author: François Soupé, Xiao Lu, Raul Leote de Carvalho

Year : 2018

Link:  [[链接已屏蔽])

---

### 帖子 #7: Research Paper: First Impression Bias: Evidence from Analyst ForecastsPinned
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

### 帖子 #8: Research Paper: Investor Learning, Earnings Signals, and Stock ReturnsPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper Investor Learning Earnings Signals and Stock ReturnsPinned_13801504994455.md
- **讨论数**: 0

**Abstract :**

Prior studies show that investor learning about earnings-based return predictors from academic research erodes return predictability. However, the signaling power of “bottom-line” earnings has declined over time, which complicates assessments of investor learning about profitability signals underlying earnings. We show that modified earnings variables with lower susceptibility to signal weakening exhibit rates of return attenuation that are 30-64% lower than rates for bottom-line earnings variables over our sample period. Notably, return gaps between bottom-line and less susceptible variables are widest in recent years, especially within non-overlapping samples and samples with weak bottom-line signals (e.g., special items, losses, fourth fiscal quarter). Our results hold after controlling for risk factors known to predict returns, they do not appear to be attributable to ex ante earnings volatility, and they are robust to alternative sample selection criteria, sub-period partitions, and portfolio holding windows. Overall, our results suggest that while investor learning is apparent in the data, learning efforts to date have been suboptimal at exploiting profitability signals within firms’ earnings streams.

Key Ideas :

- Page 6 para 1
- Page 15 para 3

Term

Datafield

Dataset

Book-to-market ratio
mdl230_us5000_cusip_rel5ybp
 [model230]([链接已屏蔽]) 

expected earnings per share
act_q_gps_surprisemean
 [analyst7]([链接已屏蔽]) 

expected operating profit per share
anl14_mean_opp_fp1
 [analyst14]([链接已屏蔽]) 

expected operating profit per share
act_q_opr_surprisemean
 [analyst7]([链接已屏蔽]) 

gross profit
fnd23_annfv1a_prgs
 [fundamental23]([链接已屏蔽]) 

operating profit per share
fnd28_annsttc_value_05509a
 [fundamental28]([链接已屏蔽])

Authors: Chiu, Peng-Chia and Haight, Timothy

Year: 2019

Link :  [[链接已屏蔽])

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

### 帖子 #10: Understanding Modern Portfolio Theory to Enhance MAPC ScoreResearch
- **主帖链接**: https://support.worldquantbrain.com[L2] Understanding Modern Portfolio Theory to Enhance MAPC ScoreResearch_24558442254615.md
- **讨论数**: 10

**Introduction:**  In MAPC, all Alphas submitted by you are combined together in an equal weighted fashion to created a merged performance series. The PnL Chart of this series is then used to calculate metrics like Sharpe, Returns/Drawdown ratio and turnover. The detailed Scoring of MAPC 2024 is provided here:  [[链接已屏蔽])

This article explores how Modern Portfolio Theory (MPT) can provide insights into understanding MAPC scoring and suggests ways to improve the Merged Performance Score.

**Modern Portfolio Theory (MPT) and MAPC** : Modern Portfolio Theory offers a mathematical framework for constructing portfolios that aim to maximize expected returns while considering the associated risk. It suggests that by combining assets with different risk and return profiles, an optimal portfolio can be constructed to achieve a desired level of risk. In MAPC, the portfolio consists of multiple Alphas submitted by you, each with its unique risk and return characteristics. By combining these Alphas in an equal-weighted fashion, you generate a merged performance series with an expected return and expected risk profile.

**Expected Return Calculation:**  The expected return of the merged Alpha portfolio in MAPC can be mathematically expressed as the weighted average of the expected returns of individual Alphas.


> [!NOTE] [图片 OCR 识别内容]
> E(R
> SywE(R )
> Where;
> F(RJisthe expected return
> the porttolio
> thc rclght otassct
> Inthc porttolio。
> E(R)
> the expected return ol asser


Since all Alphas are equally weighted, the weight for each Alpha is 1/n, where n is the number of Alphas submitted.

**Variance Calculation and Risk Reduction** : The variance of the merged portfolio determines its overall risk. The variance of the same merged portfolio (let’s say with 2 assets) can be calculated as follows:


> [!NOTE] [图片 OCR 识别内容]
> w
> vo
> ZVIWOIOPIT
> Is the Jarlance OIthe Cortlolio。
> an0
> 0arothe vanances Ofasspts
> TOspectIvC y
> ondoarotho stondard doatons Of055cts
> ong
> rCspectiwoly。
> Ihe correlalion Coclficient beIcen the relurns Olassels
> and 2
> hr


Generalizing for N assets, the variance calculation becomes:


> [!NOTE] [图片 OCR 识别内容]
> 咛= CriCi-1 wiwjoiajpij
> Where Pyj Is the Correlation coefficient between the returns ofassets
> and ]


Note that from the formula for variance calculation, by incorporating Alphas with lower or negative correlations, the merged portfolio's risk can be reduced. This is because non-synchronous movements among Alphas can offset each other's risks, resulting in a smoother return profile. Hence, submitting Alphas with low correlation improves the Merged Performance Score.

**Why do you get a negative expected score if you submit correlated Alphas in MAPC?**

Submitting highly correlated Alphas increases the susceptibility of the merged portfolio to higher overall risk. This leads to a decrease in the Sharpe ratio of the Merged Portfolio (Returns/Standard deviation of returns), which explains the negative expected score. To avoid this, it’s advisable to submit Alphas with low correlation.

**Besides lowering correlation, can anything else help improve Merged Performance Score?**

The Merged Performance Score is directly proportional to Returns/Drawdown Ratio. Major drawdowns in the merged performance series may arise from factor-specific risks. Eg – Crowding Risk. Neutralizing Alphas to crowding risk factors such as hedge fund ownership, short interest, and momentum factors can help mitigate these risks. Data Explorer can be utilized to identify such risk factors and neutralize Alphas to these risks effectively. Additionally, neutralizing Alphas to well-documented risk factors like size, volatility also aids in diversification. Besides this, lowering Alpha turnover using operators that help maintain or improve Alpha signal can be helpful. Eg – Using ts_decay_exp_window instead of linear decay can be a useful tool! Instead of increasing decay to reduce turnover, Alpha signal can be refined much better by using various operators. Do you use any such operators in your Alpha Expression, feel free to post them in the comments!

**Conclusion:**  In the above article, you understood that by submitting Alphas with low correlation, you may enhance your Merged Performance Score in MAPC. Besides neutralizing to risk factors may also be helpful for diversification.

Do you have any other questions or observations from your experience while submitting Alphas in MAPC? Feel free to ask/share in the comments!

---

### 帖子 #11: [BRAIN TIPS] 6 ways to quickly evaluate a new datasetFeatured
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

### 帖子 #12: [BRAIN TIPS] Addressing Year-Specific Performance Dips
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] Addressing Year-Specific Performance Dips_17518157913751.md
- **讨论数**: 7

Encountering fluctuating results while researching Alphas is common. Sometimes, Alphas may show poor performance (dips in PNL) in specific years, which can be confusing. You can improve your Alpha's performance by looking not just at the in-sample (IS) summary section but also the year-by-year results (under the ‘Aggregate Data’). Here are some tips:

**Why do performance dips happen?**

- When Alphas show frequent poor performance, they might pose a greater risk in the future
- A decline in the PnL chart over a few years (image below) can be a warning sign for your Alpha’s robustness and OS performance
- This decline could be due to:
  - Random noise or overfitting
  - The Alpha being used by many quants, making it unviable
  - Major events like the COVID-19 crash in 2020, could also affect Alpha performance if the Alpha is not robust
- If an Alpha performs poorly during the in-sample period, it's generally safer not to utilize it. This is why the IS-ladder test is one of the consultant submission tests. 
> [!NOTE] [图片 OCR 识别内容]
> 1SGr
> J25
> 3Ce
> T
> 35Cus
> 222
> 30r
> ITor
> 150
> L25r
> LO


**How to improve dips in the in-sample period?**

- To address the dip in specific years, consider eliminating risks not associated with your main Alpha idea
- If your Alpha idea is strong, but the Alpha is volatile and less robust during certain periods, try neutralizing these risks. For example, if you want to assign more weight on stocks with high ROE, remember that ROE can differ by industry: internet service companies may have higher ROE than manufacturing companies. Then, a decline in internet service industry might severely impact your Alpha. So, neutralizing these risks can be one of the solutions to remove temporal poor performance.
- Here are some ways to neutralize:
- [Neutralization]([链接已屏蔽])  option in the settings
  - Besides Market to Subindustry neutralization, try using Slow factors and Fast factors.
- [Neutralizing operators]([链接已屏蔽])
  - Group_neutralize, group_rank or group_zscore operators
  - Vector_neut operator
  - Regression_neut operator
  - Ts_vector_neut operator

**Other types of dips/spikes issues**

If your turnover chart shows short-period spikes, this could be due to using datafields with low coverage. See the example below.


> [!NOTE] [图片 OCR 识别内容]
> Chart
> OIIITII


If the low coverage datafields lack some data at certain timestamps, the Alpha using this datafield would change all its positions. This situation may result in a large reduction in coverage for these days, causing the Alpha to fail the concentrated weight test. To tackle this, try filling operators like ts_backfill or group_backfill to lower spiking turnover and prevent low coverage.

---

### 帖子 #13: [BRAIN TIPS] How can I use the test period to improve the OS performance of my Alpha?
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] How can I use the test period to improve the OS performance of my Alpha_22205077935895.md
- **讨论数**: 8

**Why is test period important?**

A good In Sample (IS) performance of an Alpha doesn't guarantee good Out Sample (OS) performance because the Alpha was developed using the IS data, which means it was specifically designed to fit the IS data well. The distinction between fitting and overfitting is delicate and can often lead to significant degradation of the Alpha's performance in OS.

One solution to tackle this issue is Validation. Validation involves comparing the performance of your Alpha in scenarios that differ from the data it was originally trained on. It then assesses the stability of the performance during this test period, which provides an idea about the robustness of the Alpha and its performance in the Out Sample (OS).

Using the Test Period feature on the platform, you can split the IS period into training and test period. Test Period option is available under Simulation settings while simulating an Alpha. You can then create Alphas using the training data and check its performance in the test period to see if your Alpha is overfitted or not.
 
> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equit
> REGION
> UNIVERSE
> DEUY
> USA
> TOPZO0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 01
> PASTEURIZATION
> UNIT HANDUING
> NAN HANDUING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verity
> On
> Saveas Delault 
> Apply


**How to perform Validation on BRAIN?**

1. Split the IS period into a training and test period. As a rule of thumb, an 80-20 split between training and test data is ideal. For example, if you have a 5-year period,  **setting the test period as 1 year** can help achieve this configuration.
2. Use the training data period (4-year period in this case) to develop your Alpha
3. Simulate your Alpha and compute Alpha stats for the training IS period.
4. The stats for test period are hidden by default. Compare the stats for test period with training period by clicking the “Show test period button” on top of the Simulation results. 
> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> Show test period
> Test period and overall stats are hidden by default when test period is specified。
> Chart
> Dnl
> 30OOK
> SOOK
> OJOK


**Best Practices**

1. If there is a decrease of more than 50% in performance stats (such as Sharpe ratio, fitness, etc.) during the test period compared to the training period, it may indicate overfitting
2. Use multiple/ longer test periods (20%, 30%, 40% of total IS period) to enhance confidence in observed training performance
3. Avoid fitting your Alphas specifically to the test period. To ensure this, evaluate the stats of the test period only after you have completed the Alpha backtesting and are satisfied with the performance in the training period
4. Use validation along with rank tests and sub/super universe tests  to assess the robustness of Alpha performance
5. Compare similar implementations of an Alpha idea using validation; submit the Alpha with the most stable performance in training and test periods.
6. You can accept or reject Alpha ideas based on drastic performance decline in the test period, which could be indicative of potential poor OS performance.

---

### 帖子 #14: 【Alpha灵感】Betting Against Beta （反beta投注因子）
- **主帖链接**: 【Alpha灵感】Betting Against Beta 反beta投注因子.md
- **讨论数**: 2

文章名称：Betting Against Beta链接：[链接已屏蔽]一. 论文总结（一）文章理论研究基础：早期的实证研究发现，美国股票的证券市场线（SML）与标准CAPM相比更为平坦，这说明风险与收益的关系不能非常很好的满足CAPM。基于此Black et al.（1972）提出了改进版的双因子CAPM模型，即Black CAPM模型：从以上模型可以发现，资产收益可分解为beta因子和负beta因子。（二）文章IdeaBeta小于1的有效组合拥有最高的Sharpe比率，其中高Beta资产的Alpha更低。通过买入低Beta资产同时卖出高Beta资产构建的beta中性的BAB因子（反Beta投注因子）能够产生明显的经风险调整后正收益。当融资收紧，BAB组合当期预期收益会降低，随后未来收益会提高。当融资流动性风险提高的时候， 所有资产的Beta均会倾向于向1压缩。有杠杆限制的投资人会选择高beta的资产组合，而杠杆限制较少的投资人会选择带杠杆的低beta资产组合。（三）研究数据来源数据池包括美国在内20个国家的股票数据美国1-10年国债数据美国信用债数据基于各国权益指数，债券指数，外汇以及商品的期权，期货数据时间窗口及滞后区间文章选取了1年，3年及5年的滚动回归窗口，同时选取了1周作为滞后区间。（四）BAB因子的构建构建BAB因子，对beta进行排序，将资产等分入高beta组合和低beta组合；各个资产权重为去均值后排序值的残差，并调整残差使得高beta组合和低beta组合的总权重均为1；根据以上计算的权重分别计算高beta组合和低beta组合的加权平均beta；构建自融资组合，借入资金买入低beta组合，同时卖出高beta组合并将资金存入无风险资产，高beta资产与低beta资产组合的beta相等且均为1, BAB组合beta中性二. 复现过程(一)数据探索beta_last_360_days_spy数据覆盖：平均在90%左右，基本非零，数据质量非常高频率：daily中位数：中位数为1左右数据范围：基本在[-2,2]范围内数据分布：呈负偏形态；根据以上数据可以大致推断16%的数据在[-2, -1]间，34%的数据在[-1, 1]间，48%的数据在[1, 2]间。returns: daily, coverage完全，范围约在[-1, 1]correlation_last_360_days_spy: daily, coverage完全，范围约在[-1, 1]volume: daily, coverage完全（二）因子组合构建Alpha设定REGION：USINSTRUMENT TYPE：EquityUNIVERSE：US3000Neutralization: NoneDECAY：5因子构建因为平台规则，无法在横截面层面计算加权平均的高beta组合和低beta组合的beta值，因此无法计算买入组合和卖出组合的价值比例，无法完全复现论文的因子构建；进一步理解论文因子构建的核心，BAB的核心在于：beta中性，即高beta组和低beta组的beta相等；组合买卖不平衡，从价值上看，低beta组的风险资产绝对价值高于高beta组的风险资产绝对价值，根据论文的实证研究，风险资产买卖比例大约为1.3：0.85，即约3：2。根据之前对beta分布的分析，50%的资产beta是在[-2, 1]之间，另外部分是在[1,2]之间，粗略估计等分组合的beta比例大概率在2：1以上。替代思路主要为实现以上目标：买卖组合beta相等低beta价值约占总体的60%，高beta价值约占总体的40%beta越低或beta越高，在其所在组合的权重就越高因此，与论文不同，构建的是一个非等分的买卖组合，低beta60%，高beta40%（注意60%只是一个使得买卖价值比例为3：2的估计值，实际值可能不会是这个比例，可以调整至70%甚至于80%看以下稳健性；另外整个组合不是完全beta中性的，这只是为了更多低beta暴露的折中方法）beta_z=rank(beta_last_360_days_spy);weight=0.6-beta_z（三）迭代过程版本一：根据以上因子构建方法，建立一个初步版本，看是否有信号。beta_z=rank(beta_last_360_days_spy);weight=0.6-beta_z;scale(weight)结果：Sharpe在1.02, turnover6.12%，有明显信号版本二：文章发现流动性限制对BAB有明显负影响，当流动性收紧，低beta资产收益下降较高beta资产更多，BAB因子的收益率降低。启示：BAB因子收益与资产流动性正相关，可以在低beta资产中增加高流动性资产的权重。进一步研究基于该论文的其他研究，发现论文A Market-Based Funding Liquidity Measure提出了流动性代表指标，包括特质风险，Amihud流动性指标，机构持有比率，分析师覆盖，以及市值。因为波动率也是流动性指标之一，加入短期波动率更容易捕捉流动性的变动。因此加入波动率，特质风险，Amihud流动性指标和市值指标，并选取改善最好的组合，看信号是否有改善。volatility_st=ts_std_dev(returns<0?returns:0,20);illiquidity=ts_decay_exp_window(abs(returns)/volume,252);idiosyncratic=ts_decay_exp_window(power(ts_regression(scale_down(returns),scale_down(beta_last_360_days_spy),252,lag=0,rettype=4)/252,0.5),252);beta_z=rank(beta_last_360_days_spy);weight=0.6-beta_z;scale(weight)*scale_down(rank(-volatility_st))*scale_down(rank(-illiquidity))*scale_down(rank(-idiosyncratic))结果：Sharpe提升至1.46, turnover15.87%，performance改善明显版本三：考虑流动性的边际变动，如短期波动性高于长期波动性，说明资产流动性收紧，考虑减少该资产权重。选取一周波动率平均穿过一个月波动率平均，当流动性收紧，资产权重降低为原有权重的0.1（其实应该取0,但是取0会导致组合权重集中，因此取0.1）volatility_st=ts_std_dev(returns<0?returns:0,20);illiquidity=ts_decay_exp_window(abs(returns)/volume,252);idiosyncratic=ts_decay_exp_window(power(ts_regression(scale_down(returns),scale_down(beta_last_360_days_spy),252,lag=0,rettype=4)/252,0.5),252);cond=ts_mean(volatility_st,5)>ts_mean(volatility_st,20)?0.1:1;beta_z=rank(beta_last_360_days_spy);weight=(0.6-beta_z)*cond;scale(weight)*scale_down(rank(-volatility_st))*scale_down(rank(-illiquidity))*scale_down(rank(-idiosyncratic))结果：Sharpe提升至1.51, turnover22.15%，performance有意义提高版本四：根据本论文研究，当市场资金流动性风险的增加将 所有资产的beta向1压缩。启示：在流动性风险增加时，低beta资产和高beta资产的beta均会向1靠拢，beta分散性降低，BAB因子会失效；因此考虑提高与市场相关性低的资产的权重，提高BAB因子的显著性。增加资产与市场收益相关性指标，该指标越高，资产权重越低。volatility_st=ts_std_dev(returns<0?returns:0,20);illiquidity=ts_decay_exp_window(abs(returns)/volume,252);idiosyncratic=ts_decay_exp_window(power(ts_regression(scale_down(returns),scale_down(beta_last_360_days_spy),252,lag=0,rettype=4)/252,0.5),252);cond=ts_mean(volatility_st,5)>ts_mean(volatility_st,20)?0.1:1;beta_z=rank(beta_last_360_days_spy);weight=(0.6-beta_z)*cond;scale(weight)*scale_down(rank(-volatility_st))*scale_down(rank(-illiquidity))*scale_down(rank(-correlation_last_30_days_spy))*scale_down(rank(-idiosyncratic))结果：Sharpe提升至1.51, turnover22.15%，performance有意义提高版本五：一些尝试。论文进一步提出了一些实证发现，如低beta组合市帐率和动量更高。启示：BAB因子和市帐率和动量相关性高，有可能市帐率和动量正向影响BAB因子收益率，也可能负向影响，也可能无影响，可以买入或卖出这两个因子查看是否有影响。volatility_st=ts_std_dev(returns<0?returns:0,20);illiquidity=ts_decay_exp_window(abs(returns)/volume,252);idiosyncratic=ts_decay_exp_window(power(ts_regression(scale_down(returns),scale_down(beta_last_360_days_spy),252,lag=0,rettype=4)/252,0.5),252);hml=ts_decay_exp_window(bookvalue_ps/close,252);mom=ts_decay_exp_window(returns,252);cond=ts_mean(volatility_st,5)>ts_mean(volatility_st,20)?0.1:1;beta_z=rank(beta_last_360_days_spy);weight=(0.6-beta_z)*cond;scale(weight)*scale_down(rank(-volatility_st))*scale_down(rank(-illiquidity))*scale_down(rank(-correlation_last_30_days_spy))*scale_down(rank(-idiosyncratic))*scale_down(rank(-hml))*scale_down(rank(-mom))结果：组合中卖出这两个因子，Sharpe提升至1.71, turnover29.05%，performance提高明显版本六：再搜索引用了该论文的最新研究论文，发现论文Low Risk Anomalies?提到skewness尤其是跨期的coskewness能解释大部分BAB异像，尝试加入skewness。volatility_st=ts_std_dev(returns<0?returns:0,20);illiquidity=ts_decay_exp_window(abs(returns)/volume,252);idiosyncratic=ts_decay_exp_window(power(ts_regression(scale_down(returns),scale_down(beta_last_360_days_spy),252,lag=0,rettype=4)/252,0.5),252);hml=ts_decay_exp_window(bookvalue_ps/close,252);mom=ts_decay_exp_window(returns,252);cond=ts_mean(volatility_st,5)>ts_mean(volatility_st,20)?0.1:1;beta_z=rank(beta_last_360_days_spy);weight=(0.6-beta_z)*cond;scale(weight)*scale_down(rank(-volatility_st))*scale_down(rank(-illiquidity))*scale_down(rank(-correlation_last_30_days_spy))*scale_down(rank(-idiosyncratic))*scale_down(rank(-hml))*scale_down(rank(-mom))结果：Sharpe提升至1.86, turnover29.48%，performance有意义提高版本七：通过研究基于该论文的后续研究论文，寻找提升因子表现的思路，通过研究发现论文The Unintended Impact of Academic Research on Asset Returns: The CAPM Alpha，提出了基于BAB因子的Betting Against Alpha and Beta (BAAB因子)，同时买入低beta和低alpha资产，会进一步提升因子的显著性。结果：Sharpe反而下降明显，剔除该因子，回到版本六。（四）稳健性测试1. 数据集beta：beta_last_30_days_spy, beta_last_60_days_spy, beta_last_90_days_spy结果：表现均有所下降，但下降并非明显，很可能是beta构建时间缩短，信号出现更频繁，使因子波动率提高，Sharpe下降。再次以ts_mean平滑beta数据后，因子表现又有所提升。Liquidity:上文有提到流动性指标包括分析师覆盖和机构持有率，可理解为投资者指标，目前只找到snt_buzz (待更多探索)结果：加入后Sharpe进一步明显提高，说明流动性指标对因子表现影响明显，可以进一步探索买卖组合风险资产比率：60% - 70%探索结果：在该范围内结果变动不大，但是如果在50%及以下，因子表现非常差，说明该因子需要明显的低beta资产暴露才会perform。2.operator加权方式：ts_decay_exp_window, ts_mean结果：对结果影响不大(五)样本外测试结果三. 反思及问题在根据论文的思路进行构建及改进的过程中，每一步都改善都是非常明显的，但到最后才发现通过不了sub-universe测试，因为sub-universe有一个非常必要的neutralization是market neutralization，这个operator相当于不仅是把beta neuralized了，而且把低beta资产和高beta资产的风险值暴露一起neutralized了；但是这个因子的核心就在于低beta资产的绝对值暴露要高于高beta资产，基于beta，这个因子组合很可能在市值，行业等等都有集中的暴露，不进行neutralization是很重要的。因此，再进一步基于这个思路改善可能性不太大，需要更创新的找到提高低beta资产alpha暴露同时保持beta中性的构建方式。这也给我一个提示，在构建因子时第一步一定先做neutralization，不能设置为0在阅读论文中，基于原论文找到分解BAB因子风险的论文，可能能进一步找到不基于beta，而且可以进行风险价值暴露中性的因子。这是一篇非常经典的论文，结果明显且稳健，后续基于该论文进行的研究也非常丰富，可以基于此进一步深挖后续研究。

---

### 帖子 #15: 【Alpha灵感】Betting Against Beta （反beta投注因子）
- **主帖链接**: https://support.worldquantbrain.com【Alpha灵感】Betting Against Beta 反beta投注因子_23964166630807.md
- **讨论数**: 2

文章名称：Betting Against Beta

链接： [[链接已屏蔽])

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

### 帖子 #16: 利用Brain Lab进行数据探索系列一：单data field数据特征研究、数据预处理，以及MCP Prompt构建经验分享
- **主帖链接**: 利用Brain Lab进行数据探索系列一单data field数据特征研究数据预处理以及MCP Prompt构建经验分享.md
- **讨论数**: 9

概览：一、为什么要进行数据特征研究及数据预处理？二、结合Brain lab分析可能存在的数据问题，以及如何进行数据预处理三、需要关注的数据特征四、数据预处理整体流程梳理五、构建MCP prompt对数据进行预处理正文：一、为什么要进行数据特征研究及数据预处理？“因子”是基于Ross的APT理论，Fama和French通过三因子模型所开创的领域，是属于实证金融而非理论金融的范畴。实证金融的基础是统计学，具体到因子分析上，构成因子的每个金融工具特征在截面上的同质性和因子在时间序列上的平稳性是重要假设前提。具体到Brain平台上的Alpha generation，数据预处理的目的有二：1.通过数据预处理保证数据的同质及平稳，可以更大程度保障IS及OS的一致性，使我们对OS表现更有信心。2.对于涉及多个数据字段的alpha，我们需要保证多个字段的可比性。需要注意的问题是，原始数据的平稳性与因子平稳性是不一样的。我们更关注的是因子的平稳性。举个例子，news数据通常是脉冲式的，随机出现的，因此news数据段一般是不平稳的。但是，如果我们基于news数据构建一个事件驱动因子，我们对每一个新闻执行同样的交易策略，那我们的因子数据的事件空间就是所有的有新闻的时间，而非整个交易时间段，那么因子数据就很可能是平稳的。二、结合Brain lab分析可能存在的数据问题，以及如何进行数据预处理首先，要理解原始数据是一个面板，从数据每个截面上看是不同的金融工具在同一日期的不同特征表现；从每个时间序列上看是同一金融工具在不同日期的特征表现。 因此，在横截面上和时间序列上都需要对数据可能出现的问题进行研究和处理。进一步，考虑数据可能出现的、对同质性和平稳性有影响的问题。基于Brain lab给出的案例，数据可能出现的问题有如下几类：缺失数据(missing data)。在cross section和time series上都可能出现该问题，如果缺失数据比例较大，则因子的统计有效性是存疑的。另外，缺失数据可能被命名为-1或者99，如果不处理会扭曲真实数据情况。周期性数据(cyclical data)。如果数据在time series上出现周期性特征，则数据是不平稳的，可能存在自相关，那么得出的统计量是不可靠的。极值(outlier)。会扭曲数据的真实分布，使得统计量不可靠。非正态分布(non normal distribution)。非正态分布一般不会产生重大问题。平台关注的统计量基本都是参数估计，但如果数据本身是非正态分布的，那么很多经典的参数检验都是无效的，对判断统计量的有效性产生一定难度。还有一些虽然不影响因子有效性，但处理数据时应当小心的问题：向量数据(vector data)。应该了解vector data原始数据的状态，再进一步考虑如何使用具体vector operator进行处理。非可比数据(non-comparable data)。如果涉及两个或两个以上字段进行分析，那么这些字段只有在单位上可比才能联合分析。以下均使用USA, Delay1, TOP3000, dividend数据字段做示例。1.通过数据可视化初步判断数据可能出现的问题缺失数据：通过分布图和数据覆盖图判断是否有缺失值，缺失值是否应该处理，以及应该如何处理情况一：大量、无规律缺失。处理方式：首先判断数据是否可有用于构建事件驱动策略，如可能，则不处理；如果不能，则放弃该字段。情况二：大量、有规律缺失。处理方式：方法一：构建事件驱动策略因子；方法二：通过自回归、周期加总使数据平稳；方法三：简单缺失值回填。情况三少量缺失：处理方式：方法一：简单缺失值回填；方法二：不处理。示例：通过Visualize Field查看数据分布以及覆盖从覆盖图上可以看出，数据90%以上为0，没有nan数据。这时候我们需要注意，这个0数据到底是缺失值被回填为0了，还是它本来就是0？我们放大数据可以看出，覆盖数据在时间上具有一定周期性。再看turnover数据，周期性非常明显。再结合这个字段是股利数据，那么，我们可以大胆判断，这个数据的缺失属于情况二，大量、有规律缺失。（类似的字段还有财务报表的原始数据）我们可以再结合个股数据再次验证。再看频率分布图，大量的数据集中在0，对y轴采用log，可以看出数据有少量的非零数据，非零数据具有尖峰厚尾的统计特征。另外我们注意到，数据并没有把缺失值表示为-1, 999之类。极值通过统计量判断是否存在极值，极值应到如何处理情况一：与策略相关，如捕捉异常财务数据，因为亏损、会计调整等等出现财务指标出现异常数据，那么要么不处理，要么捕捉这些异常后再进行处理。情况二：去极值，使数据同质、平稳。示例：根据统计量分布图查看百分位数的分布从统计量分布图可以看出max值相对于75分位值有scale上的差异，因此这个数据集的极值是会扭曲数据分布的，因为dividend的数据本来就少，所以预计基于异常值很难组成有效因子，所以对于这个字段最好的处理方式就是去极值。非正态分布通过频率分布图查看数据是否属于正态分布。从之前的分布图可以看出数据明显左偏，也就是出现极值的概率大于正态分布。自变量不一定需要调整成正态分布，主要还是看使用数据的目的。比如担心极值会扭曲数据关系，或者希望数据预测更加稳健，可以将数据调整成正态分布。数据可比性通过频率分布图对相关数据进行单位及分布进行判断，调整数据使相关数据字段可比。2.可以采用的数据预处理方式以下是一些示例，采用mcp后会提供更多的数据预处理方式缺失数据：将数值转化为nan：pasteurize, purify, to_nan, nan_out回填nan数据：nan_mask, ts_backfill, kth_element极值：去极值：winsorize, truncate非正态分布：分布调整：log, sigmoid, tanh三、需要关注的数据特征连续还是离散缺失值类型及比例数据频率数据单位和分布四、数据预处理整体流程梳理第一步：点击Visualize Field初步查看数据特征，了解缺失值、异常值和分布数据覆盖图+turnover图+个股数据图判断数据频率、周期性及数据分布数据覆盖图+频率分布图查看缺失值统计特征图查看极值第二步：建立关键统计量定律描述数据概况（利用Brain lab进行分析）1.零值和nan值比例2.数据频率及周期。3.关键统计量分别计算原始非零数据的关键统计量和去极值后的数据的关键统计量。第三步：构建MCP数据分析的prompt，进行数据预处理。五、prompt模板Before we start the alpha generation, we need to preprocess the raw data to improve the quality of the alpha data.Each data field in the Brain Platform database is panel data, i.e., it contains aggregated time-series data of all the financial instruments in the universe in interest.The following is the statistical summary of the data field. After you digesting the data info, you will generate content I later ask you to provide.Data Summary:1. data field{“delay”: 1,“universe”: “USA”,“data set id”: “pv1”,“data field id”: “dividend”}2.measurement scaleThe value in the data field is continuous, not discrete.3. data coverageFrom the time series perspective, the proportion of zero values is{"mean": 0.9920,"min": 0.9455,"25%": 0.9906,"50%": 0.9943,"75%": 0.9968,"max": 1, }.The proportion of nan values in the time series is 0.4. data frequencyThe data has pulse-like periodicity for each instrument in the time series perspective.For each financial instrument, calculate the average days between adjacent non-zero values in its time series, and then conduct statistical analysis on all financial instruments, with the conclusions: {"mean": 87,"min": 1.5,"25%": 1.5,"50%": 91,"75%": 91,"max": 1650}5. data distributionStatistical analysis on all non-zero data shows:{"mean": 0.3541,"min": 0.000003,"25%": 0.12,"50%": 0.23,"75%": 0.4025,"max": 103.75,"skewness": 49.54,"kurtosis": 5101.7}After cross-sectional data winsorization applying the IQR rule, the statistical analysis results are: {"mean": 0.2993,"min": 0.000003,"25%": 0.12,"50%": 0.23,"75%": 0.40,"max": 6.5,"skewness": 1.89,"kurtosis": 10.16}.Now please provide multiple data preprocessing expressions based on your understanding of the operators in the Brain Platform:Step 1. Handling missing data.Step 2. Handling outliers.Optional step. Adjust data distribution for better statistical results.Additional requirement:1. Employ as many as possible operators in the platform以下是分析结果示例：这是单数据字段的分析示例，可以进一步改进prompt，了解数据单位和分布特征后，数据预处理可以实现多个数据字段的对齐，使之可比，是alpha质量更高。另：也在此提问，怎么去理解lab字段分析中的turnover？我理解是abs（单日数据-长期平均值之间差异）/长期平均值，不知道理解是否正确

---

### 帖子 #17: 利用Brain Lab进行数据探索系列一：单data field数据特征研究、数据预处理，以及MCP Prompt构建经验分享
- **主帖链接**: https://support.worldquantbrain.com利用Brain Lab进行数据探索系列一单data field数据特征研究数据预处理以及MCP Prompt构建经验分享_34425237001495.md
- **讨论数**: 9

**概览：**

一、为什么要进行数据特征研究及数据预处理？

二、结合Brain lab分析可能存在的数据问题，以及如何进行数据预处理

三、需要关注的数据特征

四、数据预处理整体流程梳理

五、构建MCP prompt对数据进行预处理

**正文：**

**一、为什么要进行数据特征研究及数据预处理？**

“因子”是基于 **Ross**  **的**  **APT**  **理论**  **，**  **Fama**  **和French通过三因子模型所开创的领域，** 是属于实证金融而非理论金融的范畴。实证金融的基础是统计学，具体到因子分析上，构成因子的每个金融工具特征在截面上的同质性和因子在时间序列上的平稳性是重要假设前提。

具体到Brain平台上的Alpha generation， **数据预处理的目的有二** ：

1.通过数据预处理 **保证数据的同质及平稳** ，可以更大程度保障IS及OS的一致性，使我们对OS表现更有信心。

2.对于涉及多个数据字段的alpha，我们需要 **保证多个字段的可比性** 。

需要注意的问题是， **原始数据的平稳性与因子平稳性是不一样的** 。我们 **更关注的是因子的平稳性** 。举个例子，news数据通常是脉冲式的，随机出现的，因此news数据段一般是不平稳的。但是，如果我们基于news数据构建一个事件驱动因子，我们对每一个新闻执行同样的交易策略，那我们的因子数据的事件空间就是所有的有新闻的时间，而非整个交易时间段，那么因子数据就很可能是平稳的。

**二、结合Brain lab分析可能存在的数据问题，以及如何进行数据预处理**

首先，要理解 **原始数据是一个面板** ，从数据每个截面上看是不同的金融工具在同一日期的不同特征表现；从每个时间序列上看是同一金融工具在不同日期的特征表现。 因此，在横截面上和时间序列上都需要对数据可能出现的问题进行研究和处理。

进一步，考虑数据可能出现的、对同质性和平稳性有影响的问题。基于Brain lab给出的案例，数据可能出现的问题有如下几类：

- **缺失数据(missing data)** 。在cross section和time series上都可能出现该问题，如果缺失数据比例较大，则因子的统计有效性是存疑的。另外，缺失数据可能被命名为-1或者99，如果不处理会扭曲真实数据情况。
- **周期性数据(cyclical data)** 。如果数据在time series上出现周期性特征，则数据是不平稳的，可能存在自相关，那么得出的统计量是不可靠的。
- **极值(outlier)** 。会扭曲数据的真实分布，使得统计量不可靠。
- **非正态分布(non normal distribution)** 。非正态分布一般不会产生重大问题。平台关注的统计量基本都是参数估计，但如果数据本身是非正态分布的，那么很多经典的参数检验都是无效的，对判断统计量的有效性产生一定难度。

还有一些虽然不影响因子有效性，但处理数据时应当小心的问题：

- **向量数据(vector data)** 。应该了解vector data原始数据的状态，再进一步考虑如何使用具体vector operator进行处理。
- **非可比数据(non-comparable data)** 。如果涉及两个或两个以上字段进行分析，那么这些字段只有在单位上可比才能联合分析。

以下均使用 **USA, Delay1, TOP3000, dividend数据字段** 做示例。

**1.通过数据可视化初步判断数据可能出现的问题**

- ***缺失数据：***

通过分布图和数据覆盖图判断是否有缺失值，缺失值是否应该处理，以及应该如何处理

情况一：大量、无规律缺失。处理方式：首先判断数据是否可有用于构建事件驱动策略，如可能，则不处理；如果不能，则放弃该字段。

情况二：大量、有规律缺失。处理方式：方法一：构建事件驱动策略因子；方法二：通过自回归、周期加总使数据平稳；方法三：简单缺失值回填。

情况三少量缺失：处理方式：方法一：简单缺失值回填；方法二：不处理。

***示例：***

通过Visualize Field查看数据分布以及覆盖


> [!NOTE] [图片 OCR 识别内容]
> What % of dividend values are NaN Or Zero?
> I00
> percent_nan
> percent_ZerO
> 
> 201
> 2016
> 2018
> 2020
> 2022
> Date


从覆盖图上可以看出，数据90%以上为0，没有nan数据。这时候我们需要注意，这个0数据到底是缺失值被回填为0了，还是它本来就是0？我们放大数据可以看出，覆盖数据在时间上具有一定周期性。


> [!NOTE] [图片 OCR 识别内容]
> How otten do dividend Values update?
> 
> 2014
> 2016
> 2013
> 2020
> 2022
> Date



> [!NOTE] [图片 OCR 识别内容]
> How do the dividend Values change over time for the top 5 instruments with the highest coverage?
> 詈
> 201
> 2016
> 2013
> 2020
> 2022
> Date


再看turnover数据，周期性非常明显。再结合这个字段是股利数据，那么，我们可以大胆判断，这个数据的缺失属于情况二，大量、有规律缺失。（类似的字段还有财务报表的原始数据）我们可以再结合个股数据再次验证。


> [!NOTE] [图片 OCR 识别内容]
> What is the range of dividend values and their frequency?
> IOK
> 
> IO0I
> 100
> ValUe


再看频率分布图，大量的数据集中在0，对y轴采用log，可以看出数据有少量的非零数据，非零数据具有尖峰厚尾的统计特征。另外我们注意到，数据并没有把缺失值表示为-1, 999之类。

- **极值**

通过统计量判断是否存在极值，极值应到如何处理

情况一：与策略相关，如捕捉异常财务数据，因为亏损、会计调整等等出现财务指标出现异常数据，那么要么不处理，要么捕捉这些异常后再进行处理。

情况二：去极值，使数据同质、平稳。

***示例：***

根据统计量分布图查看百分位数的分布


> [!NOTE] [图片 OCR 识别内容]
> What are the
> statistical characteristics (min, max;
> mean
> medlan
> and quantiles) of the dividend Values over time?
> In
> I00
> Iean
> max
> median
> 25th_quantile
> 75th_quantile
> `
> 2014
> 2016
> 2018
> 2020
> 2022
> Date
> key


从统计量分布图可以看出max值相对于75分位值有scale上的差异，因此这个数据集的极值是会扭曲数据分布的，因为dividend的数据本来就少，所以预计基于异常值很难组成有效因子，所以对于这个字段最好的处理方式就是去极值。

- **非正态分布**

通过频率分布图查看数据是否属于正态分布。

从之前的分布图可以看出数据明显左偏，也就是出现极值的概率大于正态分布。自变量不一定需要调整成正态分布，主要还是看使用数据的目的。比如担心极值会扭曲数据关系，或者希望数据预测更加稳健，可以将数据调整成正态分布。

- **数据可比性**

通过频率分布图对相关数据进行单位及分布进行判断，调整数据使相关数据字段可比。

**2. 可以采用的数据预处理方式**

以下是一些示例，采用mcp后会提供更多的数据预处理方式

- **缺失数据：**

```
将数值转化为nan：pasteurize, purify, to_nan, nan_out
```

```
回填nan数据：nan_mask, ts_backfill, kth_element
```

- **极值：**

```
去极值：winsorize, truncate
```

- **非正态分布：**

```
分布调整：log, sigmoid, tanh
```

**三、需要关注的数据特征**

1. 连续还是离散
2. 缺失值类型及比例
3. 数据频率
4. 数据单位和分布

**四、数据预处理整体流程梳理**

**第一步：** 点击Visualize Field初步查看数据特征，了解缺失值、异常值和分布

- 数据覆盖图+turnover图+个股数据图判断数据频率、周期性及数据分布
- 数据覆盖图+频率分布图查看缺失值
- 统计特征图查看极值

**第二步：** 建立关键统计量定律描述数据概况（利用Brain lab进行分析）

1.零值和nan值比例


> [!NOTE] [图片 OCR 识别内容]
> 521.
> ZE「O5
> Ser
> dividend_field_adj_
> Map (lambda
> 1 讦
> X=0
> else
> nan/
> SUM(axi5=1) /
> top3000_field_df
> ototal
> Instruments"
> Ze「OS
> Dct
> Ser.describe ()
> 521.
> Count
> 2518.000000
> Tean
> 992074
> 5td
> 007820
> Tin
> 945548
> 253
> 990641
> 506
> 994291
> 758
> 996802
> Max
> 000000
> dtype:
> float64
> Dct



> [!NOTE] [图片 OCR 识别内容]
> [53]:
> dividend_field_nanfilled_df
> dividend field df.fillna
> 99991
> top3000_field_adf_df
> 0an
> Ser
> dividend
> field_nanfilled
> map (lambda
> 1  1
> X-np
> nan
> else
> 0). SUM (axis=1) /
> top3000_field_df
> total
> Instruments"
> 0an
> SE「
> describe
> 「53]:
> Count
> 2518
> mean
> Std
> mIn
> 258
> 508
> 758
> max
> dtype:
> float64
> pct
> pct


2.数据频率及周期。


> [!NOTE] [图片 OCR 识别内容]
> [25]:
> def
> gap
> bty nonzeros
> Series
> how=
> Nean
> TOnZe「o5
> Indices
> Series [Series
> Index
> tolist( )
> gap_counts
> 1 len(nonzeros_
> indices )>=
> for
> in range(l
> len (nonzeros_indices) ):
> 9ap
> nonzeros_indices [1]
> nonzeros_indices [11]
> gap
> Counts
> append (gap. Jays )
> hOW
> mean"
> 「e5Ult
> nP.
> mean (9a_
> Counts )
> elif
> hOW
> median"
> 「e5Ult
> percentile (9ap_counts,
> 9=501
> Feturn
> result
> else
> Feturn
> 0an
> 「26]:
> gap_btw_
> nonzeros
> pd .DataFrame ({"mean"
> dividend_field_df.apply (get_gap_btw
> nonzeros
> how=
> mean
> median"
> dividend_field_df.apply(get_gap_
> btW
> nonzeros
> how="median" )] )
> [27]:
> btw_
> nonzeros.describe ( )
> 「27]。
> mean
> median
> count
> 3705.000000
> 3705.000000
> mean
> 86.618056
> 82.532524
> std
> 104.394479
> 101.624741
> min
> 1.448328
> 1.000000
> 25%
> 1.450893
> 1.000000
> 5096
> 91.179487
> 91.000000
> 75%
> 91.500000
> 91.000000
> Max
> 1650.000000
> 1650.000000
> get
> ga0


3.关键统计量

分别计算 **原始非零数据的关键统计量** 和 **去极值后的数据的关键统计量** 。


> [!NOTE] [图片 OCR 识别内容]
> [14]:
> dividend_field_adj
> Ze「05
> dividend_field_adj_df . replace (0
> np.nan)
> [15]:
> dividend_field_adj
> Zeros_stats
> dividend_field_adj _
> ZerOS_df. melt() . describe( )
> dividend_field
> a0]
> ZerOs
> Stats
> loc["skewness
> "Value
> dividend_field_adj
> Zeros_df.melt () .Value. skew ( )
> dividend_field_adj
> Zeros_stats
> loc
> "KUrtosis "
> "Value"
> dividend_field_adj_
> Zeros_df.melt () .Value
> kurtosis ()
> dividend_field_adj
> ZerOs
> Stats
> [15]:
> Value
> COIINt
> 62304.000000
> mean
> 0.354163
> std
> 0.793399
> mln
> 0.000003
> 2596
> 0.120000
> 5096
> 0.230000
> 7596
> 402500
> max
> 103.750000
> skewness
> 49.535142
> kurtosis
> 5101.695646



> [!NOTE] [图片 OCR 识别内容]
> [IbJ
> MPT
> DOXPLOT_VInsorIze (Trame
> aXIS-I
> WIISKeI
> TaCTOT=I.5:
> quantile(0.25
> axis=axis )
> frame . quantile (0.75
> axis=axis )
> iqr
> Lower_bound
> Whisker_factor
> iqr
> Upper
> bound
> Whisker_factor
> Iqr
> i axis==l:
> lower_bound
> Lower_bound .values . reshape( -1,
> Upper
> bound
> UPPer
> bound
> Values.reshape( 1
> 「eturn
> frame. clip (lower=lower
> bound
> upperupper_bound )
> [19]:
> dividend_field_adj_winsorized_
> boxplot_winsorize (dividend_field_adj
> Zero5_df; aXi5=I,
> Whisker_factor=l. 5)
> [18]:
> dividend_field_adj_winsorized_stats
> dividend_field_adj_winsorized_df.melt( )
> describe( )
> dividend_field_adj_winsorized_
> Stats
> loc ["skewness
> nValue
> dividend_field_adj_winsorized_df.melt( ) .value . skew( )
> dividend_field_adj_winsorized_stats
> loc
> kurtosis"
> "Value
> dividend_field_adj_winsorized_df.melt() .Value . kurtosis ( )
> Oividend
> field_adj
> WinsorIzed
> 5tats
> [18]:
> Value
> COIINt
> 62304.000000
> mean
> 0.299259
> std
> 0.251143
> mln
> 000003
> 2596
> 0.120000
> 5096
> 0.230000
> 7596
> 0.400000
> max
> 500000
> skewness
> 1.892581
> kurtosis
> 10.158696
> frame


**第三步：** 构建MCP数据分析的prompt，进行数据预处理。

**五、prompt模板**

Before we start the alpha generation, we need to preprocess the raw data to improve the quality of the alpha data.

Each data field in the Brain Platform database is panel data, i.e., it contains aggregated time-series data of all the financial instruments in the universe in interest.

The following is the statistical summary of the data field. After you digesting the data info, you will generate content I later ask you to provide.

Data Summary:

1. data field

{“delay”: 1,

“universe”: “USA”,

“data set id”: “pv1”,

“data field id”: “dividend”}

2.  **measurement scale**

The value in the data field is continuous, not discrete.

3. data coverage

From the time series perspective, the proportion of zero values is

{"mean": 0.9920,

"min": 0.9455,

"25%": 0.9906,

"50%": 0.9943,

"75%": 0.9968,

"max": 1, }.

The proportion of nan values in the time series is 0.

4. data frequency

The data has pulse-like periodicity for each instrument in the time series perspective.

For each financial instrument, calculate the average days between adjacent non-zero values in its time series, and then conduct statistical analysis on all financial instruments, with the conclusions: {"mean": 87,

"min": 1.5,

"25%": 1.5,

"50%": 91,

"75%": 91,

"max": 1650

}

5. data distribution

Statistical analysis on all non-zero data shows:

{"mean": 0.3541,

"min": 0.000003,

"25%": 0.12,

"50%": 0.23,

"75%": 0.4025,

"max": 103.75,

"skewness": 49.54,

"kurtosis": 5101.7}

After cross-sectional data winsorization applying the IQR rule, the statistical analysis results are: {"mean": 0.2993,

"min": 0.000003,

"25%": 0.12,

"50%": 0.23,

"75%": 0.40,

"max": 6.5,

"skewness": 1.89,

"kurtosis": 10.16}.

Now please provide multiple data preprocessing expressions based on your understanding of the operators in the Brain Platform:

Step 1. Handling missing data.

Step 2. Handling outliers.

Optional step. Adjust data distribution for better statistical results.

Additional requirement:

1. Employ as many as possible operators in the platform

以下是分析结果示例：


> [!NOTE] [图片 OCR 识别内容]
> Step 1: Handling Missing Data Preprocessing Expressions
> Groyp Based Backfill With Winsorization
> processed
> dividend
> group_backfill (winsorize(dividend
> 3.01,
> Sector
> 60
> 3.01
> Construction Process: Uses group_backfi11 ! ! to Fill missing values with winsorized group means. The operator calculates winsorized mean OFnon-NaN
> Values within each
> groUp over past 60 days Using
> standard deviation threshold For outlier handling
> 2. Time Series K th Element Imputation
> processed
> dividend
> i
> else(is
> nan (dividend) ,
> kth
> element (dividend .
> 250
> 11,
> dividend )
> Construction Process: Uses kthelement (Jiidemy
> 25@.1 to find the first nOn-NaN value in the past 250
> The 』e5e() operator
> conditionally replaces NaN Values while presering existing Valid Jata
> 3. Sector-Regression Based Imputation
> regression_prediction
> ts_regression (dividend ,
> 9roup_Vector
> proj(cap
> VolUme
> SeCtOr)
> 90,
> processed
> dividend
> i else(is nan(dividend)
> regression_prediction ,
> dividend )
> Construction Process: Uses #!egression() to predict missing values based on sector-projected capitalizationand volume relationships over 90 days
> grauR
> Vector_Pro] !!
> ensures Sector-appropriate relationships。
> 4. Multi-Period Exponential Decay Backfill
> ProCeSSeO
> dividend
> backfill (dividend
> 90
> "NAN"
> ProCeSSeO
> dividend
> decay_exp_window (processed
> dividend ,
> 30,
> 0.91
> SeCtOr
> 4ay5.



> [!NOTE] [图片 OCR 识别内容]
> 2: Handling Outliers Preprocessing Expressions
> 1.Multi-Standard Deviation Winsorization
> processed
> dividend
> Winsorize (dividend
> processed
> dividend
> clamp (processed_
> dividend
> upper=6 . 51
> Construction Process: Uses winsorize (Jildend 。3.@1 to cap Values a
> standard deviations; Followed by clamp (wpper6 .51 to enforce the IQR-
> derived maximum OF 6.5 based on the statistica
> analySI5
> 2.Dynamic IQR Based Outlier Detection
> percentage ( dividend ,
> 250
> 0.25 1
> percentage (dividend
> 250
> 0.75 1
> iqr
> subtract (93
> 911
> UpPeT
> bound
> add(43,
> Multiply (I.5,
> iqr) )
> processed
> dividend
> if_else(greater (dividend
> Upper
> bound)
> Upper
> bound ,
> dividend )
> Construction Process: Implements IQR method using As_percentage( ! For quartile calculation thenapplies the
> SNIOR rule to cap extreme Values
> 3. Sector-Adaptive Winsorization
> Sector
> Std
> 9roup
> std_dey (dividend
> SeCtOr)
> SeCtOI
> mean
> group_mean (dividend
> SeCtor I
> Upper
> limit
> add ( sector
> Mean,
> multiply (3 .0
> Sector
> std) )
> processed
> dividend
> else(greater (dividend ,
> Upper
> limit) ,
> Upper
> limit ,
> dividend )
> Construction Process: Uses Sector-specific statistics with grolRstd_de ( ) and grolR_mean( ) to create adaptive thresholds thal respect sector
> characteristics。
> Step



> [!NOTE] [图片 OCR 识别内容]
> Optional
> Adjust Data Distribution Expressions
> Log-Transform with Zero Handling
> ProCeSSeO
> dividend
> (add (dividend,
> 0000011 )
> ProCeSSeO
> dividend
> Winsorize (processed_dividend
> 3.01
> Construction Process: Uses Log(addldiidend 。 @ .@00o@1! to apply logarithmic transformation with
> smalloffset to handle Zero Values, reducing
> skewness From 49.54Lo nearnorma
> levels。
> 2. Box-Cox style Power Transformation
> lambda
> Val
> 0.3
> Optimal
> Tor
> reducing
> SKewness  based
> analysis
> ProCeSSeO
> dividend
> divide
> subtract (power (dividend
> lambda_Val) ,
> 11 ,
> lambda
> Val)
> processed
> dividend
> Winsorize (processed_dividend
> 3.01
> Construction Process: Implements Box-Cox transformation using power(diidend
> ahdaya  with 1=0.3, optimized to reduce the extreme
> skewness obsered in the data
> 3. Rank Based Normalization
> processed
> dividend
> quantile (dividend
> gaussian"
> 1.01
> processed
> dividend
> group_neutralize (processed
> dividend ,
> Sector)
> Construction Process: Uses qyantie
> 9a5a
> totransform Values to standard normal distribution, Followed by
> growReut !a3! to remove sector blases。
> Step:
> 1og
> sl.0)
> g* t。


这是单数据字段的分析示例，可以进一步改进prompt，了解数据单位和分布特征后，数据预处理可以实现多个数据字段的对齐，使之可比，是alpha质量更高。

另：也在此提问，怎么去理解lab字段分析中的turnover？我理解是abs（单日数据-长期平均值之间差异）/长期平均值，不知道理解是否正确

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《ATOM AMA 2024 - Ask me Anything被推荐的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] ATOM AMA 2024 - Ask me Anything被推荐的_26942011289751.md
- **评论时间**: 1年前

How comes that sometimes when I submit one more alpha, the total IS score decreased?

---

### 探讨 #2: 关于《group_neutralize(alpha, bucket(rank(cap),range='0.2,1,0.2'))》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 带你读论文系列活动第一期课后挑战1_23759895660183.md
- **评论时间**: 2年前

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

### 探讨 #3: 关于《Improving diversification by adding normalizationFama_MacBeth_normalized = ts_zscore(Fama_MacBeth, 252);PCP_normalized = ts_zscore(PCP, 252);Adding a cap to the weights to prevent concentrationcapped_Fama_MacBeth = truncate(Fama_MacBeth_normalized, maxPercent=0.02);capped_PCP = truncate(PCP_normalized, maxPercent=0.02);Additional diversification stepscaled_Fama_MacBeth = scale_down(capped_Fama_MacBeth);scaled_PCP = scale_down(capped_PCP);Generating the final signalSignal = rank(scaled_Fama_MacBeth) + rank(scaled_PCP);Signal》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 带你读论文系列活动第一期课后挑战2_23807105368215.md
- **评论时间**: 2年前

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
