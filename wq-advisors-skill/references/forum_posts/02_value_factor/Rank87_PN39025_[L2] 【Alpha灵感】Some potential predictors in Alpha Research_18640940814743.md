# 【Alpha灵感】Some potential predictors in Alpha Research

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Some potential predictors in Alpha Research_18640940814743.md
- **作者**: JZ22613
- **发布时间/热度**: 2 years ago, 得票: 7

## 帖子正文

Time-Series and Cross-Sectional Stock Return Forecasting: New Machine Learning Methods

Author: David Rapach, Guofu Zhou

Inspiration：This paper extends the machine learning methods developed in Han et al. (2019) for forecasting cross-sectional stock returns to a time-series context. The methods use the **elastic net** to refine the simple combination return forecast from Rapach et al. (2010). In a time-series application focused on forecasting the US market excess return using a large number of  **potential predictors,**  we find that the elastic net refinement substantively improves the simple combination forecast, thereby providing one of the best market excess return forecasts to date. We also discuss the cross-sectional return forecasts developed in Han et al. (2019), highlighting how machine learning methods can be used to improve combination forecasts in both the  **time-series and cross-sectional dimensions** .

- **U**  **seful datafields on BRAIN:**

Term  Datafield  Dataset

forecast  anl34_Stockdivforecasts_expectedamount  Analyst34

earning per share  anl4_epsa_flag  Analyst4

dividend per share  anl4_af_div_flag  Analyst4

Expression:

- log(ts_sum(anl4_epsa_flag,240))-log(sp500) -> EP
- log(ts_decay_linear(anl4_epsa_flag,240))+log(sp500) -> EP
- -log(ts_decay_linear(act_12m_dps_value,60))+log(sp500) -> DP
- log(ts_decay_linear(anl4_epsa_flag,240))-log(sp500) -> EP


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> N Chart
> Pnl
> 2511
> ZON
> TSU
> TO
> 5,000k
> 5OU
> 2012
> 201
> 3014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 3021



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.87
> 87.16% 0.52
> 31.34958.6297.199o0
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 0,44
> 81,96%
> 0,26
> 27.6195
> 58,62%
> 74c
> 494
> 2012
> 74.82%6
> 0.67
> 32.339
> 29.86%
> ,64965
> 532
> 2013
> 2.38
> 78.32%
> 2.10
> 60.8395
> 14.92%
> 15.5330
> 508
> 2014
> 0.66
> 52.119
> 0.35
> 17.7895
> 23.35%
> 7330
> 576
> 2015
> 0.43
> 91.12%
> 0.17
> 14.139
> 38.169
> 3.10930
> 504
> 2016
> 1,15
> 88,26%
> 0,77
> 39.4695
> 26,18%
> 8,943c
> 513
> 2017
> 94,82%6
> 1.12
> 32.8595
> 7,82%
> 9336
> 461
> 2018
> 0.52
> 96.62%
> -0.23
> 18.1795
> 52.15%
> ~3.76230
> 502
> 2019
> 104,64%
> 55.0595
> 16,38%
> 10.5230
> 484
> 2020
> 97.459
> 2.06
> 105.9996
> 39.4296
> 21.75900
> 484
> 2021
> 6.69
> 94.47%
> 9.91
> 207.20%
> 5.18%
> 43.869
> 514


---

## 讨论与评论 (0)

