# 【Alpha灵感】凸显理论（Salience Theory）

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】凸显理论Salience Theory_20262909489431.md
- **作者**: ML15895
- **发布时间/热度**: 2 years ago, 得票: 24

## 帖子正文

- **研报题目** ：
  1. 行为金融新视角——“凸显性收益”因子 STR（招商证券， 2022年12月14日）
  2. 凸显理论之 A 股“价”“量”应用（广发证券，2023年3月23日）
- **研报简介** ：
  传统的资产定价模型通常假设投资者完全理性并且能够利用市场上所有的可得信 息， 但在实际投资中， 大多数投资者对资产进行定价时往往会受隐形的“心理权 重”影响。因此，基于凸显理论（Salience Theory）对投资者进行投资决策时的心理权重进行了定量描绘，构建了“凸显性收益”因子 STR，当 STR 为显著正时，投资者往往过度关注股票的上涨潜力，从而成为风险寻求者；当投资者过分关注股票的负收益并强调其下行风险时， STR 显著为负，相关的股票可能面临低估。第二篇中结合了A股市场的涨跌幅限制和高换手率等市场特征，构建凸显因子。
- **核心交易idea** ：根据凸显理论构建STR，通过排序做多STR低的股票，做空STR高的股票执行策略。
  1. 计算股票日收益率的凸显性系数sigma
  2. 根据sigma计算凸显性权重weight
  3. 计算STR因子
  感兴趣的话，具体公式可以参考第一篇研报的公式（4-6）
- **数据字段** ：returns, volume, sharesout
- **Simulation设置** ：
  
> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> CHN
> TOP3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 5
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> On
> Verify
> Off
> SaVe as Default
> Apply

- Alpha表达式和表现：
  1. 原始STR
  
> [!NOTE] [图片 OCR 识别内容]
> Jelta
> 0.7;
> theta
> 0.1;
> market_return
> group_median
> Teturns
> market)
> sigma
> ab5
> Teturns
> market_return)
> (ab5
> returns 1
> abs (market_return
> theta 1
> Jays
> 22;
> k = ts_rank (-sigma;
> days I+days;
> K_l = iT_else (k==0
> 1, kI;
> weight
> power (delta,
> tS_rank (k_l
> Jays) )
> ts_meanl power (delta,
> ts_rank (k_I,  Jays/
> days)
> STR
> covariance Iweight ,
> returns
> days) ;
> qroup_neutralize (ZSCore (-STR)
> bucket ( rank (capI ,
> range='0,
> 1, 0.1')
 表现（Pnl, IS Summary)
  
> [!NOTE] [图片 OCR 识别内容]
> 161
> 15I
> 41
> 131
> 12N
> 1OI
> ODOK
> OODK
> ODOK
> ODOK
> ODOK
> ODOK
> OODK
> ODOK
> ODOK
> OOOK
> Jul'11
> Jan '12
> Jul '12
> Jan '13
> Jul'13
> Jan '14
> Jul '14
> Jan '15
> Jul'15
> Jan '15
> Ju1'16
> Jan'17
> Jul'17
> Jan 18
> Jul'18
> Jan '19
> Jul'19
> Jul 20
> Jan 21
> IS Summary
> Period
> Aggregate Data
> Snarpe
> TUrnOVer
> FItness
> ReUrns
> CTIIIO
> Marain
> 2.04
> 15.87%
> 2.09
> 16.68%
> 19.78%
> 21.01%oo
> URN  N
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> STJTOL
> VUTIOUE |
> LICTIES '
> RETUIRS
> UTJIOTITI
> Nariln
> 2.04
> 15.87%
> 2.09
> 16.68%
> 19.78%
> 21.01%o。
> Year
> Sharpe
> Turnover
> Htness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2011
> 2.15
> 16.039
> 705
> 14.70%
> 3.52%
> 18.2554
> 1113
> 1035
> 2012
> 4.15
> 15.5295
> 542
> 25.45%
> 2.99%
> 34.09532
> 1200
> 1094
> 2013
> 2.37
> 15.459
> 2.55
> 19.46%
> 4.52%
> 25.1954
> 1273
> 1103
> 201
> 3.46
> 15.2795
> 4.25
> 23.02%
> 3.41%
> 30.155
> 1277
> 1103
> 2015
> 0.22
> 16.3395
> 003
> 2.47%
> 19.78%
> 3.01533
> 1245
> 1133
> 201
> 3.33
> 15.349
> 21.94%
> 3.14%
> 27.7053
> 1405
> 1251
> 2017
> 2.54
> 15.559
> 7.37
> 20.04]
> 4.27%
> 25.5954
> 1575
> 1401
> 2013
> 3.22
> 16.2595
> 3.83
> 23.74%
> 2.24%
> 29.2252
> 565
> 1434
> 2019
> 3.42
> 16.209
> 4.20
> 24.45]
> 3.14%
> 30.1355
> 1615
> 1334
> 2020
> 1.24
> 16.0795
> 1.14
> 13.68%
> 15.31%
> 17.02533
> 1633
> 1372
> 2021
> 1.07
> 16.3395
> 1.03
> 15.22%
> 3.17%
> 18.57535
> 1601
> 1417
> 医 Correlation
> Self Correlation
> HBhest Correlatlon
> LaSt RJn
> Prod Correlation
> HlBhest Correlation
> LasC RUn: Tue
> 01/0212024.11.47 PM
> Lonq
 可以看到时有信号的，同时prod corr较高， 所以还要改进。
  2. 根据第二篇研报， **引入换手率
  
> [!NOTE] [图片 OCR 识别内容]
> Jelta
> 0.7;
> theta
> 0.1;
> market_return
> 9roup
> median ( returns
> TaTket;
> 5iqma
> ab5 (returns
> market_return)
> (abs (returns)
> ab5 (market_return !
> thetal
> turnover
> Lume
> SharesoUt;
> market
> turnover
> qroup
> mean ( turnover;
> market)
> sigma
> abs (turnover
> market_turnover
> 1ab5
> tUrnoverI
> abs (market
> turnover
> theta1
> Jays
> 22;
> ts_rank (-sigma,
> days / +days;
> k_1 = if_else(k==0
> 儿;
> weight
> powerldelta,
> ts_rank (k_1,
> days 1
> Mean ( power
> delta,
> rank (k_1i  Jays/'
> Jays
> STT
> Covariance (weight
> returns
> days ;
> group_neutralize
> ZSCOre |-STTI ,
> bucket ( rank (capl ,
> range=
> 1, 0.1'1
**  
> [!NOTE] [图片 OCR 识别内容]
> 1ONI
> 9 OOOK
> ODOK
> ODOK
> ODOK
> 5OOOK
> ODOK
> 3ODOK
> ODOK
> ODOK
> Jul'11
> Jan '12
> Jul'12
> Jan '13
> Jul '13
> Jan '14
> JU1'14
> Jan '15
> Jul'15
> Jan '16
> Jan'17
> 117
> Jan 18
> Jul'18
> Jan '19
> Jul 19
> Jul'20
> Jan
> IS Summary
> Period
> Aggregate Data
> Sharpe
> TUTNTIe
> FItness
> Returns
> Drwdown
> Margln
> 1.91
> 14.46%
> 1.74
> 11.97%
> 15.80%
> 16.56900
> JJUI
> JJUl
 3. 用 **与换手率之间的协方差** 替换与日收益率之间的关系：
  
> [!NOTE] [图片 OCR 识别内容]
> delta
> 0.7;
> theta
> 0.1;
> market
> return
> 9roup_median (returns, market);
> 5igma
> abs ( returns
> market_return)
> (abs (returns)
> abs (market
> returnl
> thetal ;
> turnover
> Volume/ sharesout;
> market_turnover
> qroup_mean ( turnover,
> market);
> abs ( turnover
> narket
> turnover
> (abs (turnover
> abs (market_turnover )
> thetal ;
> 22;
> ts_rank(-5igma, days /*days;
> K_l = iT_else (k==0
> 1, kl
> weight
> power (delta,
> ts_rank (k_I, Jays/)
> tS_mean
> power (delta,
> ts_rank (k_I
> Jays) )
> days
> # STT
> ts_covariance (weight ,
> returns
> days) ;
> STTZ
> ts_Covariance (weight,
> turnover Jays);
> 9roup_neutralize ( ZSCore (-STTZI ,
> bucket ( rank (cap)
> range='0,
> 0.1') 1
> sigma
> days

  
> [!NOTE] [图片 OCR 识别内容]
> 22N
> ZON
> 8M
> 16N
> 4 |
> 121|
> 1ONI
> ODOK
> OODK
> OODK
> OODK
> Jul'11
> Jan '12
> Jul'12
> Jan '13
> Jul'13
> Jan '14
> Jul '14
> Jan '15
> Jul'15
> Jan '15
> JuI'16
> Jan'17
> Jul'17
> Jan'18
> Jul'18
> Jan '19
> Jul 20
> Jan
> IS Summary
> Period
> Aggregate Data
> Snarpe
> TUrnOVer
> TITICSc
> ReUrns
> CTIIIO
> Marain
> 2.92
> 10.83%
> 4.13
> 24.99%
> 16.14%
> 46.179o0
> J4119
 4.  **引入涨跌幅限制** ：
  
> [!NOTE] [图片 OCR 识别内容]
> delta
> 0.7;
> theta
> 0.1;
> turnover
> V0lume
> Sharesout;
> market
> turnover
> group_mean (turnover;
> market;
> 5iqma
> abs (turnover
> market
> turnover
> (abs (turnover)
> ab5 (market
> turnover
> theta)
> Sigma
> if_elselabs
> returns
> >0.1,
> 305
> returns 1+1000,
> turnover ;
> Jays
> 22;
> ts_rank (-sigma,
> Jays 1+day5 ;
> K_l = ir_else (k==0
> 1, ki;
> weight
> power(delta,
> ts_rank (k_1,
> Jays/
> mean (power
> delta,
> ts_rank (k_1,
> day5 /
> Jays
> STV
> Covariance (weight;
> returns
> days ;
> group_neutralize (ZsCore(-STV)
> bucket ( rank ( capI
> range='0,
> 1,0.1'1
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Snarpe
> TITMIIPI
> FItRess
> Returns
> Drloown
> Wargln
> -0.43
> 15.88%
> -0.16
> -2.18%
> 54.97%
> -2.74900
> Year
> Sharpe
> TurnOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.25
> 16.1595
> 11.50%
> 2.53%
> 14.24532
> 1105
> 1045
> 2012
> 15.919
> 5.53%
> 4.22%
> 2053
> 1153
> 1133
> 2013
> 205
> 16.2795
> 9.09%
> 1.72%
> 11.17533
> ZO0
> 1131
> 2014
> 1.70
> 15.7395
> 1.14
> 7.03%
> 2.75%
> 9453
> 1213
> 1170
> 2015
> 16.029
> 5.37
> 23.00%
> 30.59%
> 34.9455
> 1170
> 1253
> 2015
> 0.25
> 15.5395
> 0.99%
> 03%
> 2720
> 1375
> 1293
> 2017
> 15.3095
> 1.53
> 10.75%
> 3.52%
> 14.04532
> 552
> 1423
> 2013
> 15.589
> 0.31
> +38%
> 7.53%
> 4.3150
> 1501
> 1503
> 2019
> 3.49
> 16.0095
> 3.42
> 15.33%
> 15.38%
> 19.1752
> 501
> 1502
> 2020
> 16.179
> 17.12%
> 15.91%
> 21.1855
> 1481
> 1530
> 2021
> 15.539
> 0.21
> 3.28%
> 1.47%
> 1855
> 1534
> 1490
> Correlation
> Self Correlation
> NlBhest Correlatlon
> LaSt RUn
> Prod Correlation
> HBhest Correlatlon
> Last Run: Wed, 0110312024,12.07 ANI
> 0.6


- ****总结与反思：**** 1. 总的来说，凸显理论用的数据字段和操作符比较简单，但是可以看到还是比较有效的，搜了一下Brain平台少有涉及这一理论的，所以还是值得分享一下。
  2. 这个方法主要是做月度调仓，想问问大家怎么能够实现，看到keep这个操作符，但是没有想到如何实操。
  3. 这个思路想法简单，做法也容易实现，这可能是prod corr较高的原因之一，对于减少这个方法的prod corr试了一些方法，由于没有更多的知识，效果都不太好有点可惜，希望大家如果能够继续在这个方向上能提交alpha，可以评论区留言告知，我也希望学习到多一些的经验。

---

## 讨论与评论 (5)

### 评论 #1 (作者: ML15895, 时间: 2 years ago)

可以通过trade_when和rank(cap)仅交易市值低的股票，这样可以降低prod corr，然后我成功提交了一个alpha！如果大家有更好的想法，欢迎留言

---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

关于月度调仓和Keep operator,欢迎查看我们的小贴士19👉 [BRAIN小贴士(这里有你想要的硬核内容！持续周更中） – WorldQuant BRAIN]([L2] 【学习资料】BRAIN小贴士这里有你想要的硬核内容持续周更中Pinned_15152019662487.md?page=1#community_comment_20281447539095)

---

### 评论 #3 (作者: deleted user, 时间: 2 years ago)

您可以使用 trade_when(volume>adv20,alpha,-1) 来减少 prod corr

---

### 评论 #4 (作者: ML15895, 时间: 2 years ago)

非常感谢@WL13229！

---

### 评论 #5 (作者: KW15253, 时间: 2 years ago)

引入涨跌幅限制之后sharpe降低了好多，有什么办法嘛

[ML15895](/hc/en-us/profiles/18428687822103-ML15895)

---

