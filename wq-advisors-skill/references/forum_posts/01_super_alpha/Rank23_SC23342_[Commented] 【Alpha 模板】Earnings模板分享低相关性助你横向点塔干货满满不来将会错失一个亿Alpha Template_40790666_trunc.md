# 【Alpha 模板】Earnings模板分享，低相关性，助你横向点塔（干货满满，不来将会错失一个亿）Alpha Template

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha 模板】Earnings模板分享低相关性助你横向点塔干货满满不来将会错失一个亿Alpha Template_40790666727575.md
- **作者**: WL58980
- **发布时间/热度**: 28天前, 得票: 20

## 帖子正文

继上次分享Risk模板后，又来分享模板啦，针对Earnings类型的数据，模板使用了ts_backfill（）回填，模板如下：

```
<time_series_operator/>(ts_backfill(<data_field/>,<days_1/>), <days_2/>)
```

其中：

1.data_field使用的是USA/D1/ILLIQUID_MINVOL1M/earnings_sent_matrix（仅有7个数据,但USA,GLB,EUR三个区域都有）;


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Global Earnings Call Sentiment Matrix
> USA
> TOP3000
> Dataset description
> Category: Earnings / Earnings Estimates
> Dataset ID:
> earnings_sent_matrix 国
> This dataset provides a structured, matrix-format aggregation of global company earnings call transcripts, focusing on sentiment and topic analytics. It
> leverages advanced natural language processing to extract and quantify positive; neutral, and negative sentiment probabilities from management
> presentations and Q&A sessions;
> aCrOSS OVer
> thematic topics. The data is filtered and enhanced with smart aggregation techniques, including rolling and
> daily sentiment measures, confidence scores, and relevance indicators. By capturing nuanced shifts in management tone and analyst reactions;, the dataset
> enables researchers and investors to identify patterns and signals that may precede price movements, offering Valuable insights for predictive modeling and
> alpha generation in equity markets。
> Stats
> Region
> Delay
> Universe
> Pyramid
> Theme
> Coverage
> Date Coverage
> Fields
> Alphas
> Theme
> Multiplier
> EUR
> ILLIQUIDMINVOLII,TOPI2O0, TOP2500, TOP400
> 121.4
> TOPSOO, TOP8OO, TOPCS1500
> GLB
> MINVOLIOM MINVOLIM, TOP3OOO TOPDIV3OOO
> USA
> ILLIQUIDMINVOLIITOPI0O0, TOP200,TOP2OOO
> 1.3,1.4
> TOP3000, TOPSOO, TOPSPSOO
> 200


2.time_series_operator并没有太多限制，我使用的是ts_arg_max，ts_av_diff，ts_quantile，ts_scale，ts_zscore等；

3.days_1使用的是10和252，days_2则是252。

至于Neutralization和Universe大家可以自行选择（温馨提示：USA的Universe使用ILLIQUID_MINVOL1M更易出货，且相关性更低）

在回测过程中发现ts_mean可以替换ts_backfill（猜想ts_sum亦可替换），即

```
<time_series_operator/>(ts_mean(<data_field/>,<days_1/>), <days_2/>)
```

由于这只是低阶模板，可能在回测后存在相关性过高的情况（但目前相关性并不高，原因我在后面说明），所以可以在外面再嵌套一个时间序列操作符,这样可以降低相关性，即

```
<time_series_operator/>(<time_series_operator/>(ts_backfill(<data_field/>,<days_1/>), <days_2/>),<days_2/>)
```

Alphas表现展示：

1、USA / positive_sentiment_probability_3;


> [!NOTE] [图片 OCR 识别内容]
> positive
> sentiment_probability_3 ,
> 252,
> 252)
> 圜single Data Set Mlnha
> ePower Pool Alpha
> 睑 Regular Alpha
> imulation Settings
> PiralniJtlere: USADIIEARNINGS ~1.3
> TITUMETC |ME:
> OUf
> TUTCalIN
> Data
> SaTOE
> CLTUI
> CIMS
> ETLJIc
> 13UI
> 11313 |
> ABBrE
> LETIUTI
> 45-
> N-utrallstlen
> -Tt
> 2.06
> 7.0896
> 1.34
> 5.3296
> 2.79%6
> 15.029600
> NT
> ILLICUO_IIINNOLII
> PsUITIJtIOT;
> ZUu
> Fyst Expression
> Lnlhur:
> JLC
> Nu T
> Sharpe
> TTCTO
> Filnoss
> Raturns
> Oowdown
> Marqin
> Count
> Short Count
> T
> NJ Positinn:
> 2014
> 7.13
> 045
> 2。1
> 2.57
> IJ
> 2015
> 1.26
> 51
> 0S6
> 2.50Mb
> 1.4
> 79-5
> Clone Alpha 
> 2015
> 6.179
> 071
> 3UUG
> U
>  | 
> CI1
> 114
> 2
> y
> 14375
> 2018
> 54
> 7.96
> `
> uube
> V Chart
> Pnl
> 2019
> 6.r7
>  |
> I
> Uu
> 2020
> 1.17
> 8.169
> 3.779
> 2.79
> 9
> TC
> 2021
> 2.10
> ??1
> 1.39
> :319
> 7,25
> O
> 022
> 25
> 25
> J
>  -4
> 1.75
> 5
> U
> 3.78
> UT
> 11.184
> S4
> 3455
> 1255
> Z,OOOK
> Investability constrained
> Aggregate Data
> Surp
> IUTIOC
> HCTCS
> TClUIIS
> UTJIIO
> NTIIF
> 1,70
> 5.31%6
> 0.99
> 4.23%
> 2.5896
> 15.9390
> C#e
> o


2、EUR / sentiment_weighting_method1;


> [!NOTE] [图片 OCR 识别内容]
> Sentiment
> weighting_methodl_
> 252),
> 252
> 能
> Data Set Alpha
> Power Pool Alpha
> ] Regular Alpha
> Simulation
> Pyramid theme; EURJDI/EARNINGS *1.2
> Settings
> Instrument Type:
> Equity
> Truncation:
> 0.08
> Aggregate Data
> Sharpe
> Turnove
> Fithess
> ReTUrns
> Drawdown
> MargIn
> Region;
> EUR
> Neutralzaton;
> Inoustny
> 1.95
> 5.259
> 1.25
> 5.11%
> 4.349
> 19.469600
> Unlerse;
> TOP2SOO
> Pasteurzatlon;
> Language;
> Fast Expresslon
> Lookhack:
> Decay;
> Wla Trade;
> Year
> Sharpe
> TuIOVeF
> Fitness
> Returns
> Drawdown
> Nargin
> Long Count
> Short Count
> Delay:
> Wa.Postlon;
> OT
> 201-
> 1.79
> 5.0395
> 0.98
> 3.719
> 1.2415
> 14.7760
> 698
> 2015
> 2.62
> 4.489
> 5,929
> 5395
> 26,4230
> 836
> Clone Alpha
> 2016
> 201
> 4.5535
> 127
> 4939
> 1.1935
> 21.84-cc
> 334
> 2017
> 3.40
> 4.453
> 2.4
> 6.4295
> 0.961
> 28.859cc
> 975
> 2018
> 2.73
> 8695
> 5.2993
> 1.0195
> 21.819
> 975
> 965
> N Chart
> Pnl
> 2019
> 2.70
> 4,6199
> 1,92
> 6,299
> 2,0491
> 27.,305
> 1007
> 983
> 2020
> 1 2
> 5.4535
> 0.77
> 5.0093
> 3.213
> 15.5192cc
> 981
> 933
> 2021
> 5.279
> 0.83
> 4.1795
> 631
> 15.829
> 1006
> 1058
> 2022
> +86
> 4+95
> 1.21
> 5.8795
> 2.5415
> 18,253500
> 1092
> 1112
> 2023
> 40
> 6.4590
> 0,73
> 3,439
> 2,0795
> 10,523
> 1087
> 1098
> DOOK
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> FItne55
> Returns
> Drawgown
> MargIn
> 1.70
> 5.259
> 0.89
> 3.449
> 2.549
> 13.1
> %oo
> SIngle


USA和EUR区域各列举了一个，仅通过这个低阶模板我便点亮了这两个区域的Earnings；


> [!NOTE] [图片 OCR 识别内容]
> EUh
> USA/DI/Earnings
> Submissions: 3
> Active
> Clickto view datasets


当然这个模板对GLB区域也是通用的，由于GLB区域回测较慢，我还没有开始回测，所以仅通过这一个模板就可以帮助你横向点塔。

然后回到相关性的问题，有的人会说这个模板光回测出Alphas有什么用，相关性过不了也没用呀，如图，昨天我仅回测了2000多次，便轻松提交了6个rea，而且还剩下很多可以提交的。


> [!NOTE] [图片 OCR 识别内容]
> Date Submitted
> Osmosis
> Region
> Universe
> Neutralization
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod-
> (EST)
> Points
> Correlation
> Correlation
> Search
> C6
> SCeC
> Select
> SOeC
> e.8 >
> e.8 >
> e.8>
> Select
> C6
> e.8 >
> 05/28/2026 EDT
> USA
> ILLIQUID_
> MINV。
> Statistical
> PowerPoolSelec::
> 0.24
> 0.56
> 05/28/2026 EDT
> USA
> ILLIQUID_MINV..
> Statistical
> 05/27/2026
> 05/27/2026 EDT
> USA
> ILLIQUID_MINV.
> Statistical
> Simulated Alphas: 2343
> PowerPoolselec。。
> 05/27/2026 EDT
> EUR
> T0P2500
> Fast Factors
> PowerPoolselec。。
> 0.41
> 43
> 05/27/2026 EDT
> EUR
> T0P2500
> Fast Factors
> 05/27/2026 EDT
> EUR
> T0P2500
> Industry
> PowerPoolSelec::
> 0.37
> 0.59


众所周知，所有顾问的入门数据都是USA区域的，所以USA区域是最多人在做的，也就是说它的相关性是最难达标，很多时候即使你回测出表现不错的Alpha，可能也会因为相关性太高而提交不了，那这个一阶模板（因为现在ts_backfill不计入操作符使用数量当中，所以可以算作一阶模板）“出货”为什么如此简单呢？


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> USA
> TOP3000
> Search
> Category
> Theme
> Coverage; %
> Date
> coverage; %
> Value sCore
> Alphas
> Name  descmpton
> Earings
> TOO
> TOO
> Clear
> Dataset
> Fields
> Pyramid Theme
> Coverage
> Date Coverage
> Value Score
> Alphas
> Resources
> Multiplier
> Global Earnings Call Sentiment Matrix
> 1.3
> 70%
> 100%6
> Earnings Call Transcript Data
> 1.3
> 95%
> Earnings Call Transcript Data
> 1.3
> 80%
> 100%6
> 166
> Deep Learning Earnings Chart Predictions
> 100
> 1.3
> 999
> 95%
> Earnings Date Breaks
> 1.3
> 92%
> 95%
> 818
> Horizon Earnings and Calendar Norh America
> 1.3
> 65%
> 95%
> 1001
> Earnings Update Emails Data
> 1.3
> 2796
> 519
> 1418
> Fnancial Event Calendar Data
> 1.3
> 100%
> 2346
> International Findings Data
> 1.3
> 99%
> 66%
> 4250
> Effect Ofearnings announcement model
> 375
> 1.3
> 9796
> 95%
> 6023
> Earnings Date Data
> 1.3
> 989
> 959
> 5851
> 9-9o


TOP3000可以说是USA区域最早推出的Universe，随着时间的慢慢推进，每个数据集或多或少都会有人做，所以看到Global Earnings Call Sentiment Matrix的Alpha数量为0，我便猜测这大概率是平台新推出的数据，结果果真如此，新推出的数据相关性普遍很低，所以可以轻松提交。

这也是我分享给大家的一个小技巧，由于相关性的限制，同一个Alpha只有第一个人才能提交，所以在平台推出新数据时，抢占先机十分重要，平台会不定时推出新数据，大家可以通过这个小技巧先人一步。如果大家看完了我这篇帖子并去Data页面查看，你会发现其他区域类型也推出了新数据，所以大家趁现在把握好机会可以轻松提交Alpha。点点关注不迷路，正探索🔎新数据中，后续将持续为大家推荐新的数据以及模板。

附赠ppa一个：（虽然IS表现比较出色，但Investability constrained却低的离谱，感觉对Combine提升意义不大，感兴趣的话可以尝试调优）


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 05
> ts
> ZsCore(ts
> mean
> overall_sentiment_score) 
> 10),
> 252)
> Single Data Set Alpha
> High Turnover
> After Cost High Turnover
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawoOwh
> Margin
> Simulation Settings
> 2.62
> 36.53%
> 1.48
> 11.589
> 3.1196
> 6.349600
> Instrumen Type:
> Truncation:
> 0.06
> Region:
> USA
> N2utralization:
> Szatistica
> Universe:
> ILLIQUID_MINVOLIM
> Dasteurization:
> 0n
> Year
>  Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Language:
> Fast Expression
> Lookback:
> Decay:
> Max Trade:
> Off
> 2014
> 2.31
> 37.4990
> 1.07
> 8.0190
> 1.72%
> 1.279200
> 1226
> 1262
> Delay:
> Max Position:
> Off
> 2015
> 3.59
> 37.9390
> 2.23
> 13.9096
> 1.789
> 7.33900
> 1241
> 1301
> 2016
> ,86
> 38.0700
> 8.1090
> 3.119
> 1.25900
> 1201
> 1212
> 2017
> .99
> 37.749
> 7.45%6
> 2.159
> 3.9590o
> 1184
> 1202
> Prod Correlation
> CXTIIII
> LIIIIIIIIT
> 111 RI; TIII
> 05'26/2326,;3 Pl
> 0.4185
> -0.5246
> 2018
> 2.20
> 37.8190
> 1.16
> 10.4990
> 2.76%
> 5.5590o
> 1206
> 1258
> IUUN
> 2019
> 2.62
> 37.98%
> 1.53
> 12.719
> 2.85%
> 6990o
> 1182
> 1234
> 2020
> 2.23
> 38.899
> 1.29
> 13.0396
> 1.75%
> 6.70520o
> 1182
> 1206
> 
> 2021
> 2.29
> 33.739
> 1.12
> 80090
> 2.0590
> 4.759300
> 1415
> 1450
> 2022
> 3.88
> 34.1190
> 2.92
> 19.3190
> 2.449
> 11.329200
> 1450
> 1451
> 2023
> 3.40
> 31.6390
> 2.35
> 15.1596
> 1.4890
> 9.58900
> 1252
> 1251
> 0 
> 00
> @
> 02.
> 05
> C
> 05
> 0?
> 03
> 5,000K
> Investability constrained
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> Returns
> DrawoOwh
> Margin
> 0.55
> 24.539
> 0.16
> 2.009
> 7.3796
> 1.639600
> Equity
> 40,5


---

## 讨论与评论 (8)

### 评论 #1 (作者: ST61360, 时间: 24天前)

感谢楼主分享模版，分享总结的很全面。多谢。

---

### 评论 #2 (作者: MY82844, 时间: 24天前)

夯！没想到Earnings数据还可以出PC这么低表现这么强的RA，

ts算子的使用非常有启发，多谢分享！

=======================================================

学而不思则罔，思而不学则殆

=======================================================

---

### 评论 #3 (作者: AK76468, 时间: 24天前)

================================================================================

感谢分享，我将立刻研究这个数据集！

================================================================================

---

### 评论 #4 (作者: JL52079, 时间: 23天前)

感谢大佬的投喂，祝大佬 **扶摇直上九万里，**  **GM榜上写传奇** ！

=========================JUST DO IT !=========================

---

### 评论 #5 (作者: LX71036, 时间: 23天前)

太及时了，这个字段对于我来说真的太难跑出来了，这个模板就是及时雨，正好6月的fast数据里面也有earning的数据集~

---

### 评论 #6 (作者: BW14163, 时间: 23天前)

感谢分享，估计现在有一大批人尝试过了的，唉，又慢了一步。明天抽时间把看看，按这个模板，能不能搞一个python alpha，估计能降低点pc

---

### 评论 #7 (作者: 顾问 SC23342 (Rank 23), 时间: 22天前)

好东西，是我想要的代码~ USA这个region从regular的提交数量看已经非常饱和了，能看到0.5以下的prod-correlation属实罕见，期待分享更多有趣的模板

================================泰山哥布林 DJ泰哥儿====================================

---

### 评论 #8 (作者: FF56620, 时间: 21天前)

模板很好呀，最近出了一些新的dataset，有更多的机会，还没去探索，要抽空去看看
======================================================================================

---

