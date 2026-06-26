# 关于EUR地区的atom,ppa类型的简单模板和经验分享Alpha Template

- **链接**: [Commented] 关于EUR地区的atomppa类型的简单模板和经验分享Alpha Template.md
- **作者**: DA98440
- **发布时间/热度**: 9个月前, 得票: 79

## 帖子正文

我是IQC结束后7月份拿到的顾问权限。因为当时IQC交了很多表达式复杂，过拟合的alpha，导致我vf直接炸了，所以让我认识到了alpha的纯净和稳定的重要。所以我立马就开始了弄atom和ppa类型的alpha，也因为这种类型的alpha提交门槛低。

一、波动率调整

```
x / ts_std_dev(x, d)
```

当时也是ai推荐的一个简单模板，跑下来也还行，在eur的analyst也跑出了alpha


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 07/02/2025 EDT
> n0
> Add Alphato a List
> Code
> IS Summary
> Period
> I5S
> 05
> ts_backfill
> Vec_aVg
> anl69_
> best
> poe
> 4wk_chg
> /ts_std_dev
> VeC
> aVj
> anl6g_best
> roe_4wk_chg)
> 252),25
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDIIANALYST X1.5
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 1.92
> 12.399
> 1.84
> 11.449
> 6.6896
> 18.479600
> Instrument Type
> Region
> Universe
> Language
>  Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Har
> Equity
> EUR
> TOP2500
> Fast Expression
> 10
> 0.1
> Country
> Region
> On
> Off
> Verify
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> 2.16
> 12.44%
> 1.80
> 8.6796
> 2.73%6
> 13.939600
> 988
> 744
> 2014
> 2.51
> 13.11%6
> 2.84
> 16.7796
> 2.78%6
> 25.599600
> 1102
> 720
> 2015
> 3,16
> 13.1906
> 5.03
> 33.48%6
> 6896
> 50.769600
> 1010
> 814
> Clone Alpha
> 2016
> 85
> 12.36%
> 0.52
> 4.6796
> 4.32%6
> 7.559600
> 1012
> 839
> 2017
> 4.33
> 12.3006
> 4.32
> 12.4496
> 1.3996
> 20.239600
> 1011
> 68
> Chart
> Pnl
> 2018
> 2.34
> 12.22%
> 1.85
> 7.83%
> 2.4896
> 12.819600
> 1157
> 397
> 2019
> 1.66
> 11.83%
> 1.23
> 5.9196
> 3.9596
> 11.679600
> 1244
> 717
> 2020
> 0.85
> 11.849
> 6.6196
> 5.2696
> 11.179600
> 1081
> 818
> 1OM
> 2021
> 2.78
> 12.45%
> 2.59
> 10.8396
> 3.5096
> 17.409600
> 833
> 1212
> 2022
> 0.98
> 12.00%
> 6.1896
> 5.9996
> 10.319600
> 1072
> 389
> 7,50OK
> 2023
> 62
> 14.34%
> 0.28
> 2.8496
> 0.8396
> 3.979600
> 1282
> 626
> 5,00OK
> 70
> 2,50OK
> [
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run;
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
> Decay
> Long


然后有的可以在外面套一层group_op( x , group)


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 07/02/2025 EDT
> anonymous
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 0S
> group_rank(ts_backfill
> anl6g_Opp_expected_report
> dt/ts_std_
> dev(anl6g_Opp_expected_report_dt,
> 66
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDIIANALYST X1.5
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 2.05
> 9.179
> 1.29
> 4.959
> 3.059
> 10.799600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Han
> Equity
> EUR
> TOP2500
> Fast Expression
> 10
> Country
> Region
> On
> Off
> Verify
> Year
> Sharpe
> TUTIOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,66
> 9.3996
> 2.76
> 7.1196
> 1.2096
> 15.
> 596oo
> 724
> 801
> 2014
> 3.48
> 639
> 2.63
> 7.1696
> 8996
> 16.5996o0
> 784
> 369
> 2015
> 1.91
> 1.18
> 4.7696
> 2.2296
> 10.719600
> 776
> 354
> Clone Alpha
> 2016
> 3.80
> 8.78%
> 3.11
> 8.3796
> 1.4696
> 19.079600
> 360
> 2017
> 2.40
> 8.9696
> 1.38
> 4.1596
> 3096
> 9.279600
> 833
> 912
> Chart
> Pnl
> 2018
> 0.44
> 9.30%
> 0.12
> 0.9696
> 1.5796
> 2.079600
> 844
> 936
> 2019
> 3.07
> 9.62%
> 2.27
> 6.81%6
> 1.5996
> 14.149600
> 790
> 874
> 2020
> 48
> 9.36%
> 1.02
> 5.8896
> 3.0596
> 12.569600
> 783
> 860
> 2021
> 1.84
> 9.30%
> 1.05
> 4.0496
> .0896
> 8.679600
> 858
> 941
> 2022
> 0.32
> 9.55%
> ,08
> .82%6
> 2.96%
> 1.729600
> 802
> 8
> 2023
> -0.90
> 7.60%
> 0.37
> 2.0696
> 0.5596
> 5.439600
> 733
> 748
> Z,OOOK
> 0O
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
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
> 792



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> I5S
> 05
> group_rank(ts
> backfill (Vec
> aVg(anl4_basicconaf_pu ) /ts_std_
> deV
> VeC
> aVg(anl4_basicconaf_pu) _
> 252)
> Power Pool Alpha
> Pyramid theme: EURIDI/PV X1
> Pyramid theme: EURIDIIANALYST X1.5
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 2.21
> 9.829
> 1.60
> 6.549
> 2.81%
> 13.329600
> Instrument Type
> Region
> Universe
> Language
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Har
> Equity
> EUR
> T0P2500
> Fast Expression
> 10
> 0.1
> Country
> Region
> On
> Off
> Verify
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2013
> 2.69
> 9.97%
> 2.09
> 7.5896
> 1.3796
> 15.219600
> 850
> 853
> 2014
> 2.83
> 9.85%
> 2.03
> 5.4490
> 1.0796
> 13.089600
> 1062
> 1072
> 2015
> 0.91
> 10.200
> 0.39
> 2.33%6
> 1.9796
> 4.579600
> 1155
> 1151
> Clone Alpha
> 2016
> 2.79
> 889
> 2.24
> 0696
> 2.38%
> 16.329600
> 1201
> 1217
> 2017
> 3.46
> 9.76%
> 2.82
> 8.32%6
> 1.1696
> 17.059600
> 1352
> 1343
> N Chart
> Pnl
> 2018
> ,82
> 9.97%
> 1.09
> 4.4896
> 1.6896
> 8.999600
> 1356
> 1353
> 2019
> 0.96
> 9.5496
> 0.41
> 2.3096
> 2.1796
> 4.839600
> 1304
> 1322
> 2020
> 1.95
> 10.32%
> 1.55
> 7.9096
> 2.2896
> 15.309600
> 1249
> 1243
> 2021
> 2.47
> 9.4696
> 2.00
> 8.2196
> 1.2896
> 17.359600
> 1317
> 1288
> 2022
> 2.43
> 9.349
> 2.12
> 9.4896
> 2.8196
> 20.299600
> 1267
> 1250
> 4,00OK
> 2023
> 6.12
> 9.4896
> 6.73
> 15.1196
> 0.3296
> 31.889600
> 1224
> 1198
> 2,00OK
> Correlation
> Self Correlation
> MaximUm
> Minimum
> Last Run:
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
> Decay
> Delay



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> I5S
> 05
> group_zscore(ts_backfill
> anl6g_ptp_expected_report_dt/ts_std_dev(anl6g_ptp_expected_report_dt
> Power Pool Alpha
> Pyramid theme: EURIDIIPV X1
> Pyramid theme: EURIDIIANALYST X1.5
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 2.39
> 17.28%
> 2.12
> 13.639
> 4.869
> 15.789600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Har
> Equity
> EUR
> TOP2500
> Fast Expression
> 10
> 0.1
> Country _
> Region
> On
> Off
> Verify
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2013
> 4.63
> 17.94%
> 4.93
> 20.36%
> 3.28%6
> 22.709600
> 567
> 1273
> 2014
> 3.61
> 17.15%
> 3.85
> 19.5296
> 2.4296
> 22.769600
> 544
> 1450
> 2015
> 4.40
> 16.88%
> 5.60
> 27.3796
> 2.5996
> 32.449600
> 529
> 1448
> Clone Alpha
> 2016
> 2.52
> 15.82%
> 2.34
> 13.6396
> 1.9396
> 17.239600
> 501
> 1478
> 2017
> 1.76
> 16.83%
> 1.35
> 9.8996
> 2.71%6
> 11.759600
> 583
> 1535
> Chart
> Pnl
> 2018
> 1.37
> 17.90%
> 1.85
> 8896
> 4.86%
> 7.699600
> 586
> 1612
> 2019
> 2.90
> 17.83%
> 2.59
> 14.2496
> 3.1096
> 15.989600
> 1436
> 2020
> 1.90
> 17.559
> 1.70
> 14.0996
> 3.9496
> 16.0696o0
> 583
> 1414
> 2021
> 1.57
> 17.36%
> 1.11
> 8.6896
> 4.4996
> 10.0096o0
> 584
> 1611
> 2022
> 0.38
> 17.569
> 0.14
> 2.4496
> 3.8296
> 2.799600
> 605
> 1450
> 2023
> 1.37
> 17.64%
> 0.78
> 5.7496
> 0.5896
> 6.519600
> 588
> 1404
> 5,0OOK
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
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


这个模板ai给出的解释是


> [!NOTE] [图片 OCR 识别内容]
> 核心思想 (The Core Idea)
> 这种操作的目的]是*"风险平价" (Risk Parity) 或"波动率归
> ~化" (Volatility Normalization) xx=
> 1.当
> 的近期波动性增大时 (ts_std_dev 娈大),分
> 母娈大。整个表达式的结果就会娈小。这意味着系
> 统会降低对这个信号的权重。从而减少交易头寸,
> 以规避潜在的高风险。
> 2.当 X 的近期波动性减小时 (ts_std_dev 变小,分
> 母娈小,整个表达式的结果就会娈大。这意味着在
> 市场相对平稳时;
> 可以更相信这个信号。并相应地
> 增加交易头寸。
> 总结 (In Summary)
> ts_std_deV(X,
> 是一种动态调整信号强度的策
> 略。它不是直接使用原始信号 *
> 而是使用经过其自身
> 波动率调整后的信号。这样做的好处是,
> 可以让最终的
> 投资组合对于不同波动环境具有更强的适应性;
> 旨在获
> 得-个更平滑。风险更均衡的收益曲线,
> 而不是追求短
> 期内可能因高波动性而带来的极端收益 (或亏损)


感觉下来就是这种alpha比较吃数据字段本身的强度，冷门的数据字段出货率还是有限。

或许可以尝试一下把ts_std_dev替换成其它数据字段，寻找一下有没有更多模板。

二、与常见的数据相除

```
ts_bacfill(x/cap,500)
```


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> group_neutralize(ts_
> backfill (est
> I2m_pre_raisednum_Imth
> cap, 580 ),group_cartesian_product
> indust 
> Power Pool Alpha
> Pyramid theme: EURIDIIPV X1
> Pyramid theme: EURIDIIFUNDAMENTAL X1.1
> Pyramid theme: EURIDIIANALYST X1.5
> Simulation Settings
> Instrument Type
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Han
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.24
> 7.179
> 1.83
> 8.30%
> 5.349
> 23.149600
> Equity
> EUR
> TOP2500
> Fast Expression
> 10
> 0.1
> Country
> Region
> On
> Off
> Verify
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 4.03
> 7.849
> 3.91
> 11.7796
> 1.0996
> 30.029600
> 848
> 979
> Clone Alpha 
> 2014
> 2.93
> 7.1796
> 2.41
> 8.4896
> 1.9196
> 23.679600
> 924
> 1061
> 2015
> 0.58
> 7.35%
> 0.23
> 1.9596
> 2.6996
> 5.319600
> 920
> 1059
> 2016
> 2.55
> 7.629
> 2.03
> 7.9296
> 1.8396
> 20.
> g96oo
> 925
> 1047
> Chart
> Pnl
> 2017
> 3,85
> 7.06%
> 3.46
> 10.1296
> 2.0896
> 28.689600
> 1004
> 1109
> 2018
> 3.31
> 899
> 3.15
> 11.3596
> 1.6396
> 32.939600
> 1049
> 1160
> 2019
> 2.59
> 7.25%
> 2.13
> 8.439
> 2.6496
> 23.259600
> 308
> 1185
> 2020
> 0.11
> 5.78%
> 03
> 6890
> 5.3496
> 2.349600
> 882
> 1127
> 5,00OK
> 2021
> 3.12
> 7.08%
> 2.95
> 11.2096
> 1.3796
> 31.669600
> 1026
> 1166
> 2022
> 2.26
> 7.68%
> 2.05
> 10.2496
> 2.9296
> 26.679600
> 963
> 1113
> 2,5OOK
> 2023
> 4.18
> 6.13%
> 4.69
> 15.7296
> .3596
> 51.279600
> 956
> 1056
> 骷
> A
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
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
> 1.46
> 7.179
> 0.90
> 4.799
> 7.009
> 13.369600



> [!NOTE] [图片 OCR 识别内容]
> Code
> o IS Summary
> Period
> IS
> 05
> group_zscore(ts_
> backfill (mdl25_rpv4z1
> IIV
> cap,588 )
> group_cartesian_product (market, sector
> Power Pool Alpha
> Pyramid theme: EURIDIIPV X1
> Pyramid theme: EURIDIIMODEL X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 1.61
> 2.859
> 1.68
> 13.65%
> 7.7796
> 95.84900
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Har
> Equity
> EUR
> T0P2500
> Fast Expression
> 10
> 0.1
> Country / Region
> On
> Off
> Verify
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 64
> 3.6796
> 0.40
> 4.919
> 7.7396
> 26.799600
> 509
> 401
> 2014
> 2.27
> 3.19%
> 2.84
> 19.589
> 2.6296
> 122.9一
> 9600
> 522
> 460
> 2015
> 2.80
> 2.90%
> 3.58
> 20.4596
> 4.1296
> 140.929600
> 488
> 478
> Clone Alpha 
> 2016
> 0.32
> 3.05%
> 0.16
> 3.1096
> 7.2496
> 20.339600
> 478
> 493
> 2017
> 3.37
> 2.27%
> 4.15
> 18.9496
> .8596
> 166.539600
> 421
> 630
> N
> Chart
> Pnl
> 2018
> 2.53
> 2.46%
> 3.04
> 18.0696
> 0896
> 146.769600
> 501
> 584
> 2019
> 2.6296
> 0.58
> 5.8996
> 6.0596
> 45.029600
> 426
> 578
> 2020
> 1.74
> 2.739
> 2.29
> 21.6896
> 7.7796
> 158.879600
> 481
> 497
> 2021
> 1.97
> 2.29%
> 2.37
> 18.0996
> 5.9296
> 157.7一
> 900
> 667
> 398
> 1OM
> 2022
> 0.79
> 3.409
> 0.59
> 7.0396
> 7.3796
> 41.399600
> 543
> 473
> 2023
> 1.599
> 0.38
> 4.6096
> 8896
> 57.899600
> 497
> 492
> 5,0OOK
> 00
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 邮
> 1.10
> 2.859
> 0.87
> 7.829
> 9.339
> 54.909600
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
> Corrolatinn
> Delay


更多的我就不展示了，感觉出货率还行。

这是我第一次来到wq就了解到的模板，当时是用fundamental与cap相除。因为基本面分析的这种数据与cap更大概率产生有经济学意义，积极的组合。推荐使用fundamental，model，analyst关于经济的这种。如果是news这种相除的话，主观上就感觉不符合，容易过拟合。

然后就这样一共交了34个alpha，这是这34alpha的表现，也不知道算好还是算坏


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 1.05
> 0.95 more to Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 1.8
> 0.2 more to Grandmaster
> 0.5


然后隔了一个多月现在的话也是重新开始交alpha了，现在的目标是多做atom，一个alpha里只有同数据集的数据字段，做到数据纯净，曲线稳定。

不知道大家做atom有没有什么好的方法和模板，比如有的数据集我会让里面的数据字段做加减乘除两两组合，或者有的数据字段会在外面套一层 signed_power（ x，2 ）， signed_power（ x，0.5），-inverse（x）这种。

不知道大家有没有想法或者看法，欢迎在评论区留言。

---

## 讨论与评论 (23)

### 评论 #1 (作者: WL13229, 时间: 9个月前)

最后这个除以cap有点风险，其他ok/

---

### 评论 #2 (作者: WD67119, 时间: 9个月前)

学习了

---

### 评论 #3 (作者: GY56717, 时间: 9个月前)

学习了， 我试了一下，感觉可以用来快速摸一把dataset

---

### 评论 #4 (作者: AK76468, 时间: 9个月前)

首先感谢你的分享，用字段除以自身波动率的处理方式，可以让信号更加独特，同时也有可解释的经济学含义，如果分子取一年均值，该比率更类似于Sharpe Ratio。

然后关于您展示的第二个Alpha，其中字段anl69_ptp_expected_report_dt，它的含义是Expected Earnings Report Date，看起来它表示日期相关的字段。我的疑问是：用这个日期字段除以它本身的波动率，具有怎样的含义？

---

### 评论 #5 (作者: JB71859, 时间: 9个月前)

可以的，很不错的分享，我最近也是在跑EUR正好可以借鉴一下跑跑看，看有什么其他的效果出来。
===================================================================================

---

### 评论 #6 (作者: LX71036, 时间: 9个月前)

前面两个模板感觉既简单，而且出的又是atom，对vf也是有很大的好处，而且anl上的数据集，也是更有经济学含义，下次我去点anl的塔的时候也来试试看，感谢您的分享！

---

### 评论 #7 (作者: CW63908, 时间: 9个月前)

感谢分享，学习到了。

---

### 评论 #8 (作者: YQ84572, 时间: 9个月前)

很好的的想法，简单而清晰的带有经济学意义的模板，感谢您的分享！

---

### 评论 #9 (作者: LR93609, 时间: 9个月前)

感谢分享

对于第二个，我有一些自己的看法：

1. 这个做不了atom，只能在pv里面用，其他数据集混信号，不太推荐

```
ts_bacfill(x/cap,500)
```

2. 不过有很多数据集里面都有cap类似字段可以使用，

比如在GLB中就可以选择平替，不混信号，更为纯粹

analyst：mdl26_market_cap_u

model：mdl139_mktcap

pv37：pv37_cap_15

other：oth193_wolfe_shield_global_mktcap

再次感谢，不错的模板

---

### 评论 #10 (作者: MY82844, 时间: 9个月前)

经济学上，有时候enterprise value比cap更准确哇... backfill(x/cap, 500)可能没有backfill(x,500)/cap快？

---

### 评论 #11 (作者: DA98440, 时间: 9个月前)

[LR93609](/hc/en-us/profiles/30244554462231-LR93609)  感谢大佬指点，能够扩展出同数据集的数据字段无疑是最好的，能够多做atom也更有经济学意义。

---

### 评论 #12 (作者: DA98440, 时间: 9个月前)

*[MY82844](/hc/en-us/profiles/32294661710743-MY82844)  感谢回复，enterprise value的话学习到了，可以按自己的想法去扩展数据字段，可以把这看作是一个简单的作除的模板。backfill(x,500)/cap确实更好一点，因为cap是百分百覆盖的一个数据字段。*

---

### 评论 #13 (作者: AL13375, 时间: 9个月前)

感谢大佬的分享！

已经使用了大佬的模板并跑出来了不错的alpha，从各项指标来看都是挺好的，并且这些模板很简单，对于六维也是很友好的。

期待大佬更多的分享和模板的推荐，非常需要！

祝大佬vf1.0！

==========路漫漫其修远兮，吾将上下而求索==========

---

### 评论 #14 (作者: BL72197, 时间: 9个月前)

感觉大佬分享，这个模板正好可以在下个赛季用

---

### 评论 #15 (作者: MY82844, 时间: 9个月前)

[DA98440](/hc/en-us/profiles/30144996730519-DA98440)  不客气，另外看到有group_cartesian_product(market, sector)这种，是有什么考量吗？

---

### 评论 #16 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

多谢大佬的分享。学到了x/ts_std_dev(x, d)，准备在各个大区的数据字段比较少的数据集试一下，看看效果先。比如macro，imbalance。等有效果了，我再这里补充自己的测试结果。

---

### 评论 #17 (作者: DA98440, 时间: 9个月前)

[MY82844](/hc/en-us/profiles/32294661710743-MY82844)  当时只是因为没有用过group_cartesian_product操作字符，单纯多加上去遍历的，到现在看来反而多增加了一个操作字符。

---

### 评论 #18 (作者: MY49971, 时间: 8个月前)

很不错的模板，简单又具有经济学意义，正好拿去试验一下

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #19 (作者: YH53706, 时间: 8个月前)

哇，太感谢大佬的耐心指点了！您分享的模板调试建议真的特别实用，之前我在调试时总遇到各种卡壳，现在有了这些方向，一下子清晰多了。把模板记下来，接下来就准备照着试试，优化alpha，希望不要过多拟合，这些建议对我来说太有帮助了

---

### 评论 #20 (作者: JC31003, 时间: 8个月前)

学到了,但数据集纯净的Alpha真的对vf提升很重要

---

### 评论 #21 (作者: YL20304, 时间: 8个月前)

学到了，感谢大佬的分享！同样我也是在好几个月以前通过example，找到了ts_backfill(x,day),把填充后的数据进行分类，手搓出来几十个，VF上升0.6，最近也在搞ATOM 和 PPA。一直在glb地区寻找合适的想法，好难挖掘呀
=============================================================================================================================================================================================================希望大家能集思广益，再接再厉================

---

### 评论 #22 (作者: YY31580, 时间: 6个月前)

真不错，跑出了好几个，感谢分享

---

### 评论 #23 (作者: HH34943, 时间: 1个月前)

很不错的例子收藏了

---

